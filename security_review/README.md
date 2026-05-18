# security_review

A benchmark for "given a code snippet, find the security vulnerabilities."
Probes single-step security code review — naming the CWE class, pinpointing
the file/line, proposing a fix. Covers Python web, JS/Node, C, and C++ across
a base tier (one obvious bug each) and a hard tier (subtle bugs, "looks fixed
but isn't", multi-file vulnerabilities, multi-bug-with-decoy prompts).

**Status: isolated from the main eval's data pool** while the methodology is
still being calibrated. Not in `CAP_ORDER` / `HARD_CAPS`, not in
`report_compare.md`, opt-in only via `--caps security_review[,_hard]`. See
[METHODOLOGY.md §13](../METHODOLOGY.md#13-isolated-capabilities-outside-the-scoring-eval-subfolder-pattern)
for why and how.

## What's in here

| file | what it is |
|---|---|
| [`prompts/security_review.jsonl`](prompts/security_review.jsonl) | 21 base-tier prompts (one bug each, ~12 CWE classes + 2 clean-code "must flag nothing" decoys) |
| [`prompts/security_review_hard.jsonl`](prompts/security_review_hard.jsonl) | 19 hard-tier prompts (subtle single-file, multi-file, multi-bug+decoy) |
| [`results/`](results/) | Per-call JSONL + `.meta.json` + `.log` mirrors for every run. One file per (model × run) — naming follows the main eval (`<tag>__<ISO-timestamp>.jsonl`). |

## What it measures

**Per prompt:**
- Did the model name the right CWE class? (regex match against a per-prompt
  allowlist of accepted names — e.g. `"SQL injection"` / `"CWE-89"` / `"sqli"`)
- Did it pinpoint the right file + line / function?
- Did it avoid flagging the per-prompt decoys (false-positive guards)?
- For clean-code prompts (sr-20, sr-21): did it affirm "no vulnerabilities"
  rather than hallucinate bugs?

**Per call:**
- `sec_review` programmatic floor: per-bug 0/0.5/1.0 (missed / named-only /
  named+located), mean over all intended bugs, minus 0.25 per decoy
  false-positive flagged, floored at 0.0. Pass at ≥0.6. Plus a `must_say`
  affirmation gate for clean-code prompts.
- `rubric` layer (Claude scores 1–5 per criterion): `fix_soundness`,
  `explanation_correctness`, `no_false_positives`, `actionability`.
- Final call score = mean of the two via the list-grader. Same hybrid shape
  as `coding_quality`.

**Multi-file prompts** (sr-h-03 through sr-h-04, sr-h-15, sr-h-16, sr-h-17)
render multiple files into one user message with `## File: path` headers and
fenced code blocks — same format PR review tools feed models. The
vulnerability is only visible by reading two or three files together.

**Multi-bug + decoy prompts** (sr-h-18, sr-h-19) ask the model to find 3-4
real bugs while NOT flagging a plausible-sounding decoy class that isn't
actually present.

## How to reproduce

```bash
# Generate the prompts (deterministic, includes the SR_SYS shared system prompt)
python3 scripts/gen_prompts.py

# Run against the model loaded on :8080
python3 scripts/run_eval.py \
  --tag <model-tag> \
  --caps security_review,security_review_hard \
  --modes on,off \
  --concurrency 1
# Results land in security_review/results/ automatically (via SUBFOLDER_CAPS).

# Smoke (2 prompts per cap, written to a __SMOKE-suffixed file):
python3 scripts/run_eval.py --tag <model-tag> \
  --caps security_review,security_review_hard --modes on,off --smoke

# Sampling noise check — re-run a model at greedy decoding:
# 1. Edit scripts/run_eval.py SAMPLING:
#       dict(temperature=0, top_k=1, top_p=1.0, min_p=0.0, seed=42)
#    (Per llama.cpp guidance, temp=0 alone isn't greedy post-PR #9897;
#    top_k=1 + min_p=0 + seed are the belt-and-suspenders set.)
# 2. Re-run as above. Each (prompt, mode) cell becomes deterministic.
```

## Runs so far

40 prompts × 2 thinking modes = 80 calls per model run.

| tag | sampling | calls | sec_review floor pass rate | found-the-bug rate | when |
|---|---|---|---|---|---|
| `claude-opus-4-7` | Anthropic API defaults | 40* | **95.0% (38/40)** | **100% (40/40)** | 2026-05-18 |
| `qwen3.6-27b-q8kxl` | Qwen3 rec (T=0.7, top_p=0.8, top_k=20) | 80 | **92.5% (74/80)** | **100% (80/80)** | 2026-05-18 |
| `gemma4-31b-q5kxl` | Gemma rec (T=1.0, top_p=0.95, top_k=64) | 80 | **90.0% (72/80)** | 93.75% (75/80) | 2026-05-18 |
| `gemma4-26b-a4b-q8km` | Gemma rec (T=1.0, top_p=0.95, top_k=64) | 80 | **88.75% (71/80)** | 93.75% (75/80) | 2026-05-18 |

*Opus has one record per prompt (vs locals' on+off pair) — extended thinking
is implicit and the Agent tool didn't surface `reasoning_content`. Sampling
defaults are not the locals' vendor rec. It's a ceiling reference, not a
direct head-to-head; see [`results/claude-opus-4-7__2026-05-18T02-15-00.meta.json`](results/)
for the full caveat list.

**Pending:**
- Greedy re-run of `gemma4-31b-q5kxl` at `temp=0, top_k=1` to separate real
  capability gaps from single-sample sampling noise.
- Backfill `qwen3.6-35b-a3b` and `qwen3.5-122b-a10b-q3kxl`.
- Rubric-layer grading pass (`grade_rubrics.py`) — programmatic-floor scores
  above are what report.py uses; combined pass rate requires the rubric pass.

## What's deliberately out of scope (v1)

- Memory safety in Rust (`unsafe` blocks).
- Concurrency primitives beyond simple races (only TOCTOU is covered).
- Supply-chain attacks (typosquatted dependencies, postinstall scripts).
- Secrets-in-git-history.
- Infrastructure-as-code (terraform / k8s manifests).
- Exploit development — we score *recognition*, not "write a working PoC".

## Why isolated from the main eval

Three things are still being calibrated and don't belong in the headline ranking yet:

1. **Decoy false-positive handling.** A thorough reviewer often writes "this
   code correctly prevents SQL injection" or "in addition, you should
   consider command injection here"; flat CWE-name decoy regexes can fire on
   either. Phase 2 added the `must_say` affirmation gate for clean-code
   prompts; the analogous fix for thoroughness-FP on bug prompts is still
   open (it's not clear it should be "fixed" — penalizing thoroughness
   is arguable methodology).
2. **Single-sample variance at vendor-rec temperatures.** Gemma's
   recommended sampling is `temp=1.0, top_p=0.95, top_k=64` — high enough
   that a borderline call (model 60/40 between "find" and "miss") has a
   real chance of flipping per run. The cross-model patterns reported here
   are a mix of capability signal and sampling noise. A greedy-decoded
   re-run (in queue) will help disentangle them.
3. **Multi-bug precision/recall.** sr-h-18 / sr-h-19 use the per-bug mean
   approach (3 of 4 bugs = 0.75). Whether that's the right scoring shape vs
   strict F1 or weighted-by-severity is up for discussion.
