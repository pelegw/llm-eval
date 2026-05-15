#!/usr/bin/env python3
"""Local LLM eval runner.

Usage:
  run_eval.py --tag <model_tag> --caps coherence,reasoning,... --modes on,off
              [--limit N] [--concurrency N] [--smoke]

Hits the llama.cpp OpenAI-compatible endpoint, runs every prompt for each requested
thinking mode, grades programmatically (rubric items left pending), and writes one JSONL
line per call to results/<tag>__<ISO-timestamp>.jsonl  (+ a .log mirror of progress and a
.meta.json with model/server/run config).

--concurrency N sends N requests in flight at once (default 1 = strictly serial, clean
uncontended latencies). With N>1 the server batches across its parallel slots — higher
throughput but per-call latency becomes contended and result lines are written out of
plan order (each line is self-describing, so report.py doesn't care).

The per-line schema is the cross-run comparison contract -- keep it stable. See
~/.claude/projects/-home-peleg/memory/local-model-eval.md.
"""
import argparse, datetime, json, re, sys, threading, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import graders as G

PROMPTS_DIR = ROOT / "prompts"
RESULTS_DIR = ROOT / "results"
ENDPOINT = "http://localhost:8080/v1/chat/completions"
MODEL_ID = "qwen3.6-27b"              # server-side id (label only; llama.cpp ignores it) — the run is recorded under --tag
N_CTX = 8192                          # served context per slot; auto-detected at startup (fallback)
# Sampling: set per the loaded model's vendor recommendation (recorded in each run's .meta.json).
# Gemma rec: dict(temperature=1.0, top_p=0.95, top_k=64).  Qwen3 rec (current): below.
SAMPLING = dict(temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0)   # Qwen3 recommendation
SAFETY_TOKENS = 96                    # leave a little headroom under n_ctx
# default per-prompt generation cap (clamped to fit n_ctx); thinking needs lots of room
MAXTOK_THINKING = 8192
MAXTOK_PLAIN = 2048

CAP_ORDER = ["coherence", "reasoning", "coding", "coding_quality", "instruction_following",
             "long_context", "writing", "tool_calling"]
_HARD_BASE = ["coherence", "reasoning", "coding", "instruction_following", "long_context",
              "writing", "tool_calling"]
HARD_CAPS = [c + "_hard" for c in _HARD_BASE] + ["coding_quality_hard"]   # discriminating "hard tier" (separate prompt files)
FULL_ORDER = CAP_ORDER + HARD_CAPS


def est_tokens(s: str) -> int:
    # deliberate over-estimate so we never blow past n_ctx (real ratio ~4 chars/tok)
    return int(len(s) / 3.2) + 1


def call_model(messages, thinking, max_tokens, tools=None, tool_choice=None, timeout=900):
    body = {
        "model": MODEL_ID,
        "messages": messages,
        "max_tokens": max_tokens,
        "stream": False,
        "chat_template_kwargs": {"enable_thinking": bool(thinking)},
        **SAMPLING,
    }
    if tools is not None:
        body["tools"] = tools
    if tool_choice is not None:
        body["tool_choice"] = tool_choice
    data = json.dumps(body).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        resp = json.loads(r.read().decode())
    dt_ms = round((time.time() - t0) * 1000, 1)
    ch = resp["choices"][0]
    msg = ch.get("message", {})
    # Normalize tool_calls -> [{id, name, arguments(JSON-string)}, ...]; flatten the
    # OpenAI "function" envelope so graders see one consistent shape.
    tool_calls = []
    for tc in (msg.get("tool_calls") or []):
        fn = tc.get("function") or {}
        tool_calls.append({"id": tc.get("id"),
                           "name": fn.get("name") or tc.get("name"),
                           "arguments": fn.get("arguments") if "function" in tc else tc.get("arguments")})
    return {
        "text": msg.get("content") or "",
        "thinking": msg.get("reasoning_content") or "",
        "finish_reason": ch.get("finish_reason"),
        "usage": resp.get("usage", {}),
        "latency_ms": dt_ms,
        "request_body": body,
        "tool_calls": tool_calls,
    }


_TOOL_CONTENT_FENCE = re.compile(r'```[ \t]*(?:json)?[ \t]*\r?\n(.*?)```', re.S)


def _rescue_calls_from_content(text):
    """Some chat templates emit tool-call JSON into message.content rather than
    populating tool_calls. Best-effort recover {name, arguments(JSON-string)} from
    object/array/fenced shapes. Returns [] on no match."""
    m = _TOOL_CONTENT_FENCE.search(text or "")
    blob = m.group(1) if m else (text or "")
    for opn, cls in (('{', '}'), ('[', ']')):
        i, j = blob.find(opn), blob.rfind(cls)
        if 0 <= i < j:
            try:
                obj = json.loads(blob[i:j+1])
            except Exception:
                continue
            items = obj if isinstance(obj, list) else [obj]
            out = []
            for it in items:
                if isinstance(it, dict) and "name" in it:
                    args = it.get("arguments", it.get("args", {}))
                    if not isinstance(args, str):
                        try: args = json.dumps(args)
                        except Exception: args = str(args)
                    out.append({"id": None, "name": it["name"], "arguments": args})
            if out:
                return out
    return []


def probe_server_meta(model_tag):
    """Best-effort: capture the served model metadata + llama.cpp build + server cmdline so
    the report can show 'what was actually running'. Never raises."""
    meta = {"model_tag": model_tag, "endpoint": ENDPOINT, "sampling": dict(SAMPLING),
            "thinking_toggle": "chat_template_kwargs.enable_thinking (true=on / false=off); "
                               "reasoning returned in reasoning_content"}
    try:
        with urllib.request.urlopen("http://localhost:8080/v1/models", timeout=5) as r:
            d = json.loads(r.read().decode())
        m = (d.get("data") or [{}])[0]
        meta["served_model_id"] = m.get("id")
        mm = m.get("meta", {}) or {}
        for k in ("n_ctx", "n_ctx_train", "n_embd", "n_vocab", "n_params", "size"):
            if k in mm:
                meta[k if k != "size" else "file_size_bytes"] = mm[k]
    except Exception:
        pass
    try:
        with urllib.request.urlopen("http://localhost:8080/props", timeout=5) as r:
            p = json.loads(r.read().decode())
        if p.get("build_info"):
            meta["server_build"] = p["build_info"]
    except Exception:
        pass
    # find the llama-server process command line
    try:
        import glob as _glob
        for cl in _glob.glob("/proc/[0-9]*/cmdline"):
            try:
                parts = open(cl, "rb").read().split(b"\0")
                parts = [x.decode("utf-8", "replace") for x in parts if x]
                if parts and ("llama-server" in parts[0] or "llama-server" in " ".join(parts[:2])):
                    meta["server"] = "llama.cpp"
                    meta["server_cmdline"] = " ".join(parts)
                    for i, a in enumerate(parts):
                        if a == "-m" and i + 1 < len(parts):
                            meta["model_file"] = parts[i + 1].rsplit("/", 1)[-1]
                    break
            except Exception:
                continue
    except Exception:
        pass
    return meta


def load_prompts(cap):
    fp = PROMPTS_DIR / f"{cap}.jsonl"
    if not fp.exists():
        raise FileNotFoundError(f"missing prompt file {fp}")
    out = []
    for line in fp.read_text().splitlines():
        line = line.strip()
        if line:
            out.append(json.loads(line))
    return out


def build_messages(p):
    # Multi-turn prompts (tool-calling tests with pre-injected tool results)
    # provide a full `messages` list; we use it verbatim, optionally prepending
    # a `system` if one is also set and missing from the sequence.
    if isinstance(p.get("messages"), list) and p["messages"]:
        msgs = list(p["messages"])
        if p.get("system") and not (msgs and msgs[0].get("role") == "system"):
            msgs.insert(0, {"role": "system", "content": p["system"]})
        return msgs
    msgs = []
    if p.get("system"):
        msgs.append({"role": "system", "content": p["system"]})
    msgs.append({"role": "user", "content": p["user"]})
    return msgs


def run_one(idx, total, tag, cap, p, mode):
    """Build request, call the model, grade. Returns (idx, rec, log_line, kind)
    where kind in {'pass','fail','pend','err'}. Never raises."""
    thinking = (mode == "on")
    msgs = build_messages(p)
    tools = p.get("tools")
    tool_choice = p.get("tool_choice")
    prompt_tok = sum(est_tokens(m.get("content") or "") for m in msgs)
    ask = p.get("max_tokens", MAXTOK_THINKING if thinking else MAXTOK_PLAIN)
    max_tokens = max(64, min(ask, N_CTX - prompt_tok - SAFETY_TOKENS))
    rec = {
        "model_tag": tag,
        "prompt_id": p["id"],
        "capability": cap,
        "thinking_mode": mode,
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "tags": p.get("tags", []),
        "request": {
            "messages": msgs,
            "max_tokens": max_tokens,
            **SAMPLING,
            "chat_template_kwargs": {"enable_thinking": thinking},
            **({"tools": tools} if tools is not None else {}),
            **({"tool_choice": tool_choice} if tool_choice is not None else {}),
        },
        "grader": p.get("grader"),
        **({"tools_offered": [t.get("function", {}).get("name") for t in tools]} if tools else {}),
    }
    try:
        r = call_model(msgs, thinking, max_tokens, tools=tools, tool_choice=tool_choice)
        rec["response_text"] = r["text"]
        rec["thinking_text"] = r["thinking"]
        rec["latency_ms"] = r["latency_ms"]
        rec["usage"] = r["usage"]
        rec["finish_reason"] = r["finish_reason"]
        rec["tool_calls"] = r["tool_calls"]
        # Template-variance rescue: if tools were offered and tool_calls came back
        # empty, try parsing tool-call JSON out of content.
        if tools and not rec["tool_calls"]:
            rescued = _rescue_calls_from_content(r["text"])
            if rescued:
                rec["tool_calls"] = rescued
                rec["tool_calls_in_content"] = True
        gr = G.grade(p.get("grader"), r["text"], rec=rec)
        rec["grading"] = gr
        if gr.get("pending"):
            kind, status = "pend", "PEND-RUBRIC"
        elif gr.get("passed"):
            kind, status = "pass", "PASS"
        else:
            kind, status = "fail", "FAIL"
        ctok = r["usage"].get("completion_tokens")
        fr = r["finish_reason"]
        extra = f" finish={fr}" if fr not in (None, "stop") else ""
        line = (f"[{idx}/{total}] {cap}/{p['id']} mode={mode} {status}"
                f" score={gr.get('score')} {r['latency_ms']}ms ntok={ctok}{extra} :: {str(gr.get('notes'))[:120]}")
        return idx, rec, line, kind
    except Exception as e:
        rec["error"] = repr(e)
        rec["grading"] = {"score": 0.0, "passed": False, "pending": False, "notes": f"call/grade error: {e!r}"}
        return idx, rec, f"[{idx}/{total}] {cap}/{p['id']} mode={mode} ERROR {e!r}", "err"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--caps", required=True,
                    help="comma-separated capability names; or 'all' (the 6 base caps), "
                         "'hard' (the 6 *_hard caps), or 'everything' (base + hard)")
    ap.add_argument("--modes", default="on,off", help="comma-separated subset of {on,off}")
    ap.add_argument("--limit", type=int, default=None, help="max prompts per capability (debug)")
    ap.add_argument("--concurrency", type=int, default=1,
                    help="number of requests in flight at once (default 1 = strictly serial). "
                         "Server has N parallel slots; >1 exercises continuous batching but makes "
                         "per-call latency contended and writes results out of plan order.")
    ap.add_argument("--smoke", action="store_true", help="2 prompts/cap, prints to stdout only")
    args = ap.parse_args()
    concurrency = max(1, args.concurrency)

    if args.caps == "all":
        caps = list(CAP_ORDER)
    elif args.caps == "hard":
        caps = list(HARD_CAPS)
    elif args.caps in ("everything", "all+hard"):
        caps = list(FULL_ORDER)
    else:
        caps = [c.strip() for c in args.caps.split(",") if c.strip()]
    # honor the canonical order (coherence-family first per standing instructions) but keep user-given extras
    caps = [c for c in FULL_ORDER if c in caps] + [c for c in caps if c not in FULL_ORDER]
    modes = [m.strip() for m in args.modes.split(",") if m.strip()]
    limit = 2 if args.smoke else args.limit

    RESULTS_DIR.mkdir(exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    suffix = "__SMOKE" if args.smoke else ""
    out_path = RESULTS_DIR / f"{args.tag}__{ts}{suffix}.jsonl"
    log_path = RESULTS_DIR / f"{args.tag}__{ts}{suffix}.log"
    meta_path = RESULTS_DIR / f"{args.tag}__{ts}{suffix}.meta.json"
    logf = open(log_path, "w")

    meta = probe_server_meta(args.tag)
    meta["run_started"] = ts
    global N_CTX
    if isinstance(meta.get("n_ctx"), int) and meta["n_ctx"] > 0:
        N_CTX = meta["n_ctx"]                       # use the server's actual per-slot context
    meta["n_ctx_used_by_runner"] = N_CTX
    meta["max_tokens_policy"] = (f"per-prompt cap (default {MAXTOK_THINKING} thinking-on / {MAXTOK_PLAIN} off; "
                                 f"long_context uses each prompt's value); clamped to fit n_ctx={N_CTX}")

    def emit(*a):
        s = " ".join(str(x) for x in a)
        print(s, flush=True)
        logf.write(s + "\n"); logf.flush()

    # build plan
    plan = []
    for cap in caps:
        ps = load_prompts(cap)
        if limit:
            ps = ps[:limit]
        for p in ps:
            for mode in modes:
                plan.append((cap, p, mode))

    emit(f"# run {ts}  tag={args.tag}  caps={caps}  modes={modes}  concurrency={concurrency}  -> {out_path.name}")
    emit(f"# {len(plan)} calls planned  (endpoint={ENDPOINT} model={MODEL_ID} n_ctx={N_CTX})")
    meta.update(capabilities=caps, thinking_modes=modes, calls_planned=len(plan), client_concurrency=concurrency)
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")
    t_start = time.time()
    counts = {"pass": 0, "fail": 0, "pend": 0, "err": 0}
    total = len(plan)
    write_lock = threading.Lock()
    fout = open(out_path, "w")

    def handle(result):
        idx, rec, line, kind = result
        with write_lock:
            counts[kind] += 1
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fout.flush()
            emit(line)

    if concurrency <= 1:
        for i, (cap, p, mode) in enumerate(plan, 1):
            handle(run_one(i, total, args.tag, cap, p, mode))
    else:
        with ThreadPoolExecutor(max_workers=concurrency) as ex:
            futs = [ex.submit(run_one, i, total, args.tag, cap, p, mode)
                    for i, (cap, p, mode) in enumerate(plan, 1)]
            for fut in as_completed(futs):
                handle(fut.result())
    fout.close()

    dt = time.time() - t_start
    rate = total / dt if dt else 0
    emit(f"# done in {dt/60:.1f} min ({rate:.2f} calls/s, concurrency={concurrency}) :: "
         f"pass={counts['pass']} fail={counts['fail']} pending_rubric={counts['pend']} error={counts['err']} -> {out_path}")
    meta.update(run_duration_min=round(dt / 60, 1), calls=total, calls_per_sec=round(rate, 3),
                results={"pass": counts["pass"], "fail": counts["fail"],
                         "pending_rubric": counts["pend"], "error": counts["err"]})
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")
    logf.close()
    print(str(out_path))


if __name__ == "__main__":
    main()
