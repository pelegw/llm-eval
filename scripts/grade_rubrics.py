#!/usr/bin/env python3
"""Rubric-grading helper (rubric items are scored by Claude, then written back).

  grade_rubrics.py list  results/file.jsonl
      -> prints every pending rubric item with its index, prompt, response, criteria.

  grade_rubrics.py apply results/file.jsonl '<json>'
      <json> = {"<idx>": {"<criterion>": 1..5, ..., "_notes": "..."}, ...}
      For each idx: sets grading.per_criterion (1..5), grading.score = mean/5,
      grading.passed = score >= 0.6, grading.pending = False, grading.notes,
      grading.graded_by = "claude". Rewrites the file in place (atomic).

Indices are 0-based line numbers within the file.
"""
import json, sys
from pathlib import Path


def read(path):
    return [json.loads(l) for l in Path(path).read_text().splitlines() if l.strip()]


def is_pending(rec):
    return bool(rec.get("grading", {}).get("pending"))


def cmd_list(path):
    rows = read(path)
    pend = [(i, r) for i, r in enumerate(rows) if is_pending(r)]
    print(f"{len(pend)} pending rubric item(s) in {path}\n")
    for i, r in pend:
        g = r.get("grading", {})
        crits = g.get("criteria") or [c if isinstance(c, str) else c.get("name") for c in
                                      (r.get("grader", {}) or {}).get("criteria", [])]
        print("=" * 100)
        print(f"IDX {i} | {r.get('capability')}/{r.get('prompt_id')} | mode={r.get('thinking_mode')} "
              f"| rubric={g.get('rubric_name')} | finish={r.get('finish_reason')}")
        print(f"CRITERIA: {crits}")
        sysmsg = next((m['content'] for m in r['request']['messages'] if m['role'] == 'system'), None)
        if sysmsg:
            print(f"SYSTEM: {sysmsg}")
        usermsg = next((m['content'] for m in r['request']['messages'] if m['role'] == 'user'), '')
        print(f"PROMPT: {usermsg}")
        think = r.get("thinking_text") or ""
        if think:
            CAP = 1800
            shown = think if len(think) <= CAP else think[:CAP] + f"  …[+{len(think)-CAP} chars truncated]"
            print(f"--- THINKING ({len(think.split())} words) ---")
            print(shown)
        print(f"--- RESPONSE ({len((r.get('response_text') or '').split())} words) ---")
        print(r.get("response_text") or "<empty>")
        print()


def cmd_apply(path, payload):
    rows = read(path)
    scores = json.loads(payload)
    changed = 0
    for k, v in scores.items():
        i = int(k)
        rec = rows[i]
        notes = v.pop("_notes", None) if isinstance(v, dict) else None
        nums = {ck: float(cv) for ck, cv in v.items()}
        if not nums:
            print(f"!! idx {i}: no criterion scores, skipping"); continue
        norm = sum(nums.values()) / (len(nums) * 5.0)
        g = rec.setdefault("grading", {})
        g["per_criterion"] = nums                       # 1..5 scale
        g["score"] = round(norm, 4)                     # 0..1
        g["passed"] = norm >= 0.6
        g["pending"] = False
        g["graded_by"] = "claude"
        if notes:
            g["notes"] = notes
        else:
            g["notes"] = "rubric: " + ", ".join(f"{ck}={cv:g}" for ck, cv in nums.items())
        changed += 1
        print(f"idx {i} {rec.get('capability')}/{rec.get('prompt_id')} mode={rec.get('thinking_mode')}"
              f" -> score={g['score']} passed={g['passed']} ({g['notes']})")
    tmp = Path(str(path) + ".tmp")
    tmp.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    tmp.replace(path)
    print(f"\nupdated {changed} item(s) in {path}")
    remaining = sum(1 for r in rows if is_pending(r))
    print(f"{remaining} rubric item(s) still pending")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("list", "apply"):
        print(__doc__); sys.exit(1)
    if sys.argv[1] == "list":
        cmd_list(sys.argv[2])
    else:
        cmd_apply(sys.argv[2], sys.argv[3])
