#!/usr/bin/env python3
"""Regenerate TESTS.md — the per-prompt catalog — from prompts/*.jsonl.

Run:  python3 scripts/make_tests_md.py        # writes ../TESTS.md
      python3 scripts/make_tests_md.py -      # prints to stdout
Re-run this after editing prompts (i.e. after `python3 scripts/gen_prompts.py`).
"""
import json, re, glob, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"

# display order + titles for the capability sets
ORDER = ["reasoning", "coding", "coding_quality", "instruction_following", "long_context", "writing", "coherence",
         "reasoning_hard", "coding_hard", "coding_quality_hard", "instruction_following_hard",
         "long_context_hard", "writing_hard", "coherence_hard"]
def title(cap):
    base, _, h = cap.partition("_hard")
    return f"{base} — {'hard' if h == '' and cap.endswith('_hard') else ('hard' if cap.endswith('_hard') else 'base')}"
# simpler/robuster:
def title(cap):
    return (cap[:-5] + " — hard") if cap.endswith("_hard") else (cap + " — base")


def grader_summary(g):
    if g is None:
        return "—"
    items = g if isinstance(g, list) else [g]
    out = []
    for s in items:
        t = s.get("type")
        if t == "rubric":
            out.append("rubric[" + ", ".join(s.get("criteria", [])) + "]")
        elif t == "numeric":
            out.append(f"numeric(={s.get('gold')})")
        elif t in ("word_count", "line_count", "bullets"):
            out.append(f"{t}({s.get('min', s.get('exact'))}..{s.get('max', s.get('exact'))})")
        elif t in ("paragraph_count", "sentence_count"):
            out.append(f"{t}({s.get('exact', '?')})")
        elif t == "contains":
            out.append(f"contains({','.join(map(str, s.get('values', [])))[:30]})")
        elif t == "regex":
            out.append("regex" + ("·must_not" if s.get("must_not") else ""))
        elif t == "regex_all":
            out.append("regex_all")
        elif t == "forbid_char":
            out.append(f"forbid_char({s.get('chars', s.get('char'))})")
        elif t == "starts_ends":
            out.append("starts_ends(" + ", ".join(f"{k}={v!r}" for k, v in s.items() if k != "type") + ")")
        elif t == "json":
            out.append("json(" + ", ".join(s.get("required_keys", [])) + ")")
        elif t == "count":
            rng = s.get("exact", f"{s.get('min')}..{s.get('max')}")
            out.append(f"count({s.get('needle')!r}={rng})")
        elif t == "python":
            out.append("python·unit-tests")
        elif t == "code_quality":
            out.append(f"code_quality(fn={s.get('fn_name')})")
        else:
            out.append(t or "?")
    return " + ".join(out)


def probe(d):
    cap = d.get("capability", "")
    u = d.get("user", "")
    if "long_context" in cap:
        m = re.search(r"Question:\s*(.+?)(?:\s*End your reply.*)?$", u, re.S)
        q = (m.group(1).strip() if m else u)[:130].replace("\n", " ")
        ntag = next((t for t in d.get("tags", []) if t.startswith("n")), "")
        return f"[{ntag}] {q}" if ntag else q
    u = u.replace("\n", " ").strip()
    return u[:160] + ("…" if len(u) > 160 else "")


def build():
    cat = {}
    for f in sorted(glob.glob(str(PROMPTS / "*.jsonl"))):
        cap = os.path.basename(f)[:-6]
        cat[cap] = [json.loads(line) for line in open(f) if line.strip()]
    L = []
    p = L.append
    p("# Test catalog\n")
    p("Every prompt in the eval, grouped by capability and tier. **Generated from `prompts/*.jsonl` by "
      "`scripts/make_tests_md.py` — regenerate it after editing prompts.** The harness runs each of these **twice** "
      "— once with the model's thinking mode on, once off — so the call counts below double.\n")
    p("Grader shorthand: `numeric(=N)` exact-number answer-check · `word_count(a..b)` / `line_count` / "
      "`sentence_count` / `paragraph_count` / `bullets` structural counts · `contains` / `regex` / `regex_all` text "
      "checks · `forbid_char` forbidden characters · `starts_ends` first/last word · `json(keys)` JSON-shape · "
      "`count('x'=n)` substring-occurrence count · `python·unit-tests` extracted code run against hidden asserts · "
      "`code_quality(fn=…)` ast+ruff static analysis · `rubric[criteria…]` Claude scores 1–5 per named criterion "
      "(writing/coherence only). A `+` joins multiple sub-graders (all must pass).\n")
    total = sum(len(v) for v in cat.values())
    p(f"**{total} prompts** across **{len(cat)} capability sets** → **{total * 2} calls** per full run (both "
      "thinking modes).\n")
    p("| set | # prompts |")
    p("|---|---|")
    seen = set()
    for cap in ORDER:
        if cap in cat:
            p(f"| {title(cap)} | {len(cat[cap])} |"); seen.add(cap)
    for cap in sorted(set(cat) - seen):
        p(f"| {title(cap)} | {len(cat[cap])} |")
    p("")
    for cap in ORDER + sorted(set(cat) - set(ORDER)):
        if cap not in cat:
            continue
        rows = cat[cap]
        syss = {r.get("system", "") for r in rows if r.get("system")}
        sysnote = ""
        if syss:
            s = next(iter(syss))
            sysnote = f"\n\n*System prompt:* {s[:300]}{'…' if len(s) > 300 else ''}"
        p(f"## {title(cap)}  ({len(rows)} prompts){sysnote}\n")
        p("| id | what it probes | grader |")
        p("|---|---|---|")
        for d in rows:
            pr = probe(d).replace("|", "\\|")
            gs = grader_summary(d.get("grader")).replace("|", "\\|")
            p(f"| `{d['id']}` | {pr} | {gs} |")
        p("")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    md = build()
    if len(sys.argv) > 1 and sys.argv[1] == "-":
        sys.stdout.write(md)
    else:
        out = ROOT / "TESTS.md"
        out.write_text(md)
        print(f"wrote {out} ({md.count(chr(10))} lines)")
