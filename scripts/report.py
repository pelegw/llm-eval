#!/usr/bin/env python3
"""Markdown comparison report over one or more results JSONL files.

Usage: report.py results/file1.jsonl [results/file2.jsonl ...] [--out report.md]
Reports pass rate, mean grader score, and median latency, overall and broken down
by capability and by thinking mode (and capability x thinking mode).
"""
import argparse, json, statistics, sys
from collections import defaultdict
from pathlib import Path

# Capabilities whose records are kept out of the main eval's aggregates.
# Includes both qualitative-only caps (political_bias — no grader, no pass/fail)
# AND graded-but-isolated caps (security_review — programmatic + rubric, but
# its methodology is still being calibrated and we don't want it contaminating
# the main 5-way ranking yet). Their data lives in parallel subfolders
# (political_bias/results/, security_review/results/) with their own README +
# ANALYSIS; this set is the belt-and-suspenders filter in case someone passes
# a subfolder path explicitly. See METHODOLOGY.md §12.
QUALITATIVE_CAPS = {"political_bias", "security_review", "security_review_hard"}


def load(paths):
    rows = []
    for p in paths:
        for line in Path(p).read_text().splitlines():
            line = line.strip()
            if line:
                r = json.loads(line)
                if r.get("capability") in QUALITATIVE_CAPS:
                    continue
                rows.append(r)
    return rows


def load_meta(paths, explicit=None):
    """Return {results_filename: meta_dict}. Auto-discovers <results>.meta.json next to each
    results file; an explicit --meta path is applied to the first results file."""
    out = {}
    for i, p in enumerate(paths):
        cand = Path(str(p)[:-6] + ".meta.json") if str(p).endswith(".jsonl") else Path(str(p) + ".meta.json")
        if explicit and i == 0:
            cand = Path(explicit)
        if cand.exists():
            try:
                out[Path(p).name] = json.loads(cand.read_text())
            except Exception as e:
                out[Path(p).name] = {"_error": f"could not parse {cand}: {e}"}
    return out


def render_config(metas, rows):
    """Markdown for the run-configuration section. metas: {filename: meta}. Also derives
    sampling / thinking toggle from the first record as a fallback."""
    L = ["## Run configuration", ""]
    # sampling derived from data (fallback / cross-check)
    req0 = next((r.get("request", {}) for r in rows if r.get("request")), {})
    samp = {k: req0[k] for k in ("temperature", "top_p", "top_k", "max_tokens") if k in req0}
    KEY_ORDER = ["model_tag", "served_model_id", "model_file", "quantization", "architecture",
                 "n_params", "file_size_bytes", "n_ctx", "n_ctx_train", "n_embd", "n_vocab",
                 "server", "server_build", "server_cmdline", "endpoint", "hardware",
                 "measured_gpu_power_during_generation_w", "sampling", "thinking_toggle",
                 "server_total_slots", "slot_n_ctx", "client_concurrency",
                 "max_tokens_policy", "run_started", "run_duration_min", "calls"]
    PRETTY = {"model_tag": "Model tag", "served_model_id": "Served model id", "model_file": "Model file",
              "quantization": "Quantization", "architecture": "Architecture", "n_params": "Parameters",
              "file_size_bytes": "File size", "n_ctx": "Context (n_ctx)", "n_ctx_train": "Trained context",
              "n_embd": "Embedding dim", "n_vocab": "Vocab size", "server": "Inference server",
              "server_build": "Server build", "server_cmdline": "Server cmdline", "endpoint": "Endpoint",
              "hardware": "Hardware", "measured_gpu_power_during_generation_w": "Measured GPU power (generation)",
              "sampling": "Sampling", "thinking_toggle": "Thinking-mode toggle",
              "max_tokens_policy": "max_tokens policy", "run_started": "Run started",
              "server_total_slots": "Server slots (--parallel)", "slot_n_ctx": "Context per slot",
              "client_concurrency": "Client concurrency",
              "run_duration_min": "Run duration (min)", "calls": "Total calls"}

    def fmt_val(k, v):
        if k == "n_params" and isinstance(v, (int, float)):
            return f"{v:,} (~{v/1e9:.1f} B)"
        if k == "file_size_bytes" and isinstance(v, (int, float)):
            return f"{v:,} bytes (~{v/2**30:.1f} GiB)"
        if k == "measured_gpu_power_during_generation_w":
            return f"~{v} W (both GPUs, card-level)"
        if isinstance(v, dict):
            return ", ".join(f"{kk}={vv}" for kk, vv in v.items())
        if k in ("server_cmdline",):
            return f"`{v}`"
        return str(v)

    if not metas:
        L.append("_No `*.meta.json` sidecar found; configuration below derived from the results file only._")
        L.append("")
        if samp:
            L.append(f"- Sampling (from request log): {', '.join(f'{k}={v}' for k,v in samp.items())}")
        ctk = next((r["request"].get("chat_template_kwargs") for r in rows
                    if r.get("request", {}).get("chat_template_kwargs")), None)
        if ctk is not None:
            L.append(f"- Thinking toggle (from request log): `chat_template_kwargs={ctk}` (varied per call)")
        L.append("")
        return L
    for fn, m in metas.items():
        if len(metas) > 1:
            L.append(f"### {fn}")
            L.append("")
        seen = set()
        for k in KEY_ORDER + [k for k in m if k not in KEY_ORDER]:
            if k in seen or k not in m or k.startswith("_"):
                continue
            seen.add(k)
            L.append(f"- {PRETTY.get(k, k)}: {fmt_val(k, m[k])}")
        if "sampling" not in m and samp:
            L.append(f"- Sampling (from request log): {', '.join(f'{k}={v}' for k,v in samp.items())}")
        if m.get("_error"):
            L.append(f"- ⚠️ {m['_error']}")
        L.append("")
    return L


def agg(rows):
    """-> dict with n, n_graded, n_pass, n_pending, pass_rate, mean_score, median_latency"""
    n = len(rows)
    pend = [r for r in rows if r.get("grading", {}).get("pending")]
    graded = [r for r in rows if not r.get("grading", {}).get("pending")
              and r.get("grading", {}).get("score") is not None]
    npass = sum(1 for r in graded if r["grading"].get("passed"))
    scores = [float(r["grading"]["score"]) for r in graded]
    lat = [float(r["latency_ms"]) for r in rows if r.get("latency_ms") is not None]
    ctok = [int(r["usage"]["completion_tokens"]) for r in rows
            if isinstance(r.get("usage"), dict) and r["usage"].get("completion_tokens") is not None]
    return {
        "n": n,
        "n_graded": len(graded),
        "n_pending": len(pend),
        "n_pass": npass,
        "pass_rate": (npass / len(graded)) if graded else None,
        "mean_score": (sum(scores) / len(scores)) if scores else None,
        "median_latency": statistics.median(lat) if lat else None,
        "median_ctok": statistics.median(ctok) if ctok else None,
    }


def fmt_pct(x):
    return "—" if x is None else f"{100*x:.1f}%"

def fmt_f(x, nd=3):
    return "—" if x is None else f"{x:.{nd}f}"

def fmt_i(x):
    return "—" if x is None else f"{x:.0f}"


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join("---" for _ in headers) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--out", default=None)
    ap.add_argument("--meta", default=None, help="path to a run-config JSON (else auto: <results>.meta.json)")
    args = ap.parse_args()

    rows = load(args.paths)
    if not rows:
        print("no rows"); sys.exit(1)
    metas = load_meta(args.paths, args.meta)

    tags = sorted({r.get("model_tag") for r in rows})
    caps = sorted({r.get("capability") for r in rows})
    modes = sorted({r.get("thinking_mode") for r in rows})

    L = []
    L.append(f"# Local model eval report")
    L.append("")
    L.append(f"- Model tag(s): {', '.join(tags)}")
    L.append(f"- Source file(s): {', '.join(Path(p).name for p in args.paths)}")
    L.append(f"- Capabilities: {', '.join(caps)}")
    L.append(f"- Thinking modes: {', '.join(modes)}")
    o = agg(rows)
    L.append(f"- Total calls: {o['n']}  (graded {o['n_graded']}, pending rubric {o['n_pending']})")
    L.append("")

    L += render_config(metas, rows)

    L.append("## Overall")
    L.append("")
    L.append(table(["scope", "n", "pass rate", "mean score", "median latency (ms)", "median out-tokens"],
                   [["all", o["n"], fmt_pct(o["pass_rate"]), fmt_f(o["mean_score"]),
                     fmt_i(o["median_latency"]), fmt_i(o["median_ctok"])]]))
    L.append("")

    # multi-file comparison view
    multi = len(args.paths) > 1
    by_src = {}
    if multi:
        by_src = {Path(p).name: load([p]) for p in args.paths}
        L.append("## By run (source file)")
        L.append("")
        rr = []
        for fn, rs in by_src.items():
            a = agg(rs)
            tag = (metas.get(fn) or {}).get("model_tag") or (rs[0].get("model_tag") if rs else "")
            nctx = (metas.get(fn) or {}).get("n_ctx_used_by_runner") or (metas.get(fn) or {}).get("n_ctx") or ""
            rr.append([fn, tag, nctx, a["n"], fmt_pct(a["pass_rate"]), fmt_f(a["mean_score"]),
                       fmt_i(a["median_latency"]), fmt_i(a["median_ctok"])])
        L.append(table(["source file", "tag", "n_ctx", "n", "pass rate", "mean score", "median latency (ms)", "median out-tokens"], rr))
        L.append("")
        L.append("### Capability × thinking mode × run")
        L.append("")
        rr = []
        for c in caps:
            for m in modes:
                for fn, rs in by_src.items():
                    sub = [r for r in rs if r.get("capability") == c and r.get("thinking_mode") == m]
                    if not sub:
                        continue
                    a = agg(sub)
                    rr.append([c, m, fn, a["n"], fmt_pct(a["pass_rate"]), fmt_f(a["mean_score"]),
                               fmt_i(a["median_latency"]), fmt_i(a["median_ctok"])])
        L.append(table(["capability", "thinking", "run", "n", "pass rate", "mean score", "median latency (ms)", "median out-tokens"], rr))
        L.append("")

    L.append("## By thinking mode")
    L.append("")
    rr = []
    for m in modes:
        a = agg([r for r in rows if r.get("thinking_mode") == m])
        rr.append([m, a["n"], fmt_pct(a["pass_rate"]), fmt_f(a["mean_score"]),
                   fmt_i(a["median_latency"]), fmt_i(a["median_ctok"])])
    L.append(table(["thinking", "n", "pass rate", "mean score", "median latency (ms)", "median out-tokens"], rr))
    L.append("")

    L.append("## By capability")
    L.append("")
    rr = []
    for c in caps:
        a = agg([r for r in rows if r.get("capability") == c])
        rr.append([c, a["n"], fmt_pct(a["pass_rate"]), fmt_f(a["mean_score"]),
                   fmt_i(a["median_latency"]), fmt_i(a["median_ctok"]), a["n_pending"] or ""])
    L.append(table(["capability", "n", "pass rate", "mean score", "median latency (ms)", "median out-tokens", "pending"], rr))
    L.append("")

    L.append("## Capability × thinking mode")
    L.append("")
    rr = []
    for c in caps:
        for m in modes:
            sub = [r for r in rows if r.get("capability") == c and r.get("thinking_mode") == m]
            if not sub:
                continue
            a = agg(sub)
            rr.append([c, m, a["n"], fmt_pct(a["pass_rate"]), fmt_f(a["mean_score"]),
                       fmt_i(a["median_latency"]), fmt_i(a["median_ctok"])])
    L.append(table(["capability", "thinking", "n", "pass rate", "mean score", "median latency (ms)", "median out-tokens"], rr))
    L.append("")

    # rubric criterion breakdown (if any rubric items were scored)
    crit = defaultdict(list)   # (capability, criterion) -> [score 0..1]
    for r in rows:
        g = r.get("grading", {})
        pc = g.get("per_criterion")
        if pc:
            for k, v in pc.items():
                # per_criterion is stored on a 1..5 scale (see grade_rubrics.py); normalize to 0..1
                crit[(r.get("capability"), k)].append(float(v) / 5.0)
    if crit:
        L.append("## Rubric criteria (mean, normalized 0–1)")
        L.append("")
        rr = []
        for (c, k), vals in sorted(crit.items()):
            rr.append([c, k, len(vals), fmt_f(sum(vals) / len(vals))])
        L.append(table(["capability", "criterion", "n", "mean"], rr))
        L.append("")

    # failures list (compact)
    fails = [r for r in rows if not r.get("grading", {}).get("pending")
             and r.get("grading", {}).get("passed") is False]
    L.append(f"## Failures ({len(fails)})")
    L.append("")
    if fails:
        rr = []
        for r in fails:
            rr.append([r.get("capability"), r.get("prompt_id"), r.get("thinking_mode"),
                       fmt_f(r.get("grading", {}).get("score")),
                       str(r.get("grading", {}).get("notes"))[:90].replace("|", "\\|"),
                       r.get("finish_reason") or r.get("error", "")[:30]])
        L.append(table(["capability", "prompt", "mode", "score", "notes", "finish/err"], rr))
    else:
        L.append("_none_")
    L.append("")

    md = "\n".join(L)
    if args.out:
        Path(args.out).write_text(md)
        print(f"wrote {args.out}")
    else:
        print(md)


if __name__ == "__main__":
    main()
