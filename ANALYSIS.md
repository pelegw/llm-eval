# Local-model eval — 3-way analysis

*gemma-4-26b-a4b · gemma-4-31b · qwen3.6-35b-a3b — written 2026-05-12*

This is the narrative companion to `report_compare.md` (which has the raw numbers tables) and the eval memory at
`~/.claude/projects/-home-peleg/memory/local-model-eval.md`. All three models were run through the eval harness
in `~/llm-eval/` (llama.cpp OpenAI-compatible endpoint, concurrency 1, both thinking modes). **Coherence was
excluded from all three** by request — the base/`*_hard` tiers below cover reasoning, coding, code-quality,
instruction-following, long-context, and writing.

---

## TL;DR

| model | architecture | quant | overall (base+hard) | rank |
|---|---|---|---|---|
| **gemma-4-31b** | 31B dense | Q5_K_XL | base+hard run: **97.5%** / 0.978 mean | **co-leader** |
| **gemma-4-26b-a4b** | 26B MoE, ~4B active | Q8_K_XL | base run **98.3%** / 0.976; hard run 90.9% / 0.935 | **co-leader** |
| **qwen3.6-35b-a3b** | 35B MoE, ~3B active | Q8_K_XL | **92.6%** / 0.940 mean | **clear 3rd** |

- The **two Gemmas are co-leaders** — effectively tied on the base tier (~98%); the **31B-dense edges the hard
  tier** (95.7% vs the 26B-A4B's 90.9%), and the *entire* gap is the 26B-A4B over-thinking itself into
  `finish=length` truncated/empty outputs. With thinking **off**, they're neck-and-neck even on the hard tier.
- **Qwen3.6-35B-A3B is a clear third**: it shares the over-thinking truncation trait (a bit milder than the
  26B-A4B) *and* additionally lags on basic coding, basic instruction-following, hard-IF, hard-code-quality
  correctness, and long-context counting — especially thinking-off — plus more poetry-form misses.
- **Code quality is the least-differentiating axis** — all three write solid, idiomatic, well-typed, well-documented
  Python; all three flunk the same over-engineered-`evaluate`-parser quality bar when thinking-off.
- **Practical:** run any of these **thinking-on for precision-sensitive work** (exact counts, stacked constraints,
  correctness-critical code) — but the two MoEs (26B-A4B, Qwen-A3B) will sometimes burn the whole token budget
  thinking and emit nothing on hard prompts, so give them a generous `max_tokens` cap / fallback. The 31B-dense
  is the safest bet: it deliberates *and* lands the answer.

---

## Setup / methodology (so the numbers are interpretable)

- **Harness:** `~/llm-eval/` — fires a fixed prompt set at the llama.cpp endpoint, captures every response *and*
  its reasoning trace, grades each call, writes one JSONL line per call. Every prompt runs **twice** (thinking
  on / off, via `chat_template_kwargs:{enable_thinking:…}`; reasoning comes back in `reasoning_content`). All runs
  here used `--concurrency 1` (clean, uncontended latencies).
- **Two tiers per capability:** a **base** tier (~14–21 prompts each, broad, deliberately *not* hard — a sanity
  floor that strong models ceiling) and a **hard** tier (`*_hard`, ~12–20 each, deliberately tricky — the
  discriminating set). Plus two code-specific tiers, `coding_quality` and `coding_quality_hard`.
- **Grading:** *programmatic* for reasoning (numeric/regex answer-checks), coding & code-quality (extracted code
  run against hidden unit tests + robustness tests + an `ast`+`ruff` static-analysis grader), instruction-following
  (word/line/paragraph/sentence counts, char-forbids, regex structure, JSON-shape), long-context (needle/scan/count
  over generated haystacks). *Rubric* for writing — Claude scores 1–5 on ~4 named criteria per prompt, reading both
  the response and the reasoning trace; pass ≥ 0.6.
- **Sampling — NOT identical across models** (this is the main caveat): the Gemma runs used Gemma's recommended
  sampling (`temp 1.0, top_p 0.95, top_k 64`); the Qwen run used Qwen3's (`temp 0.7, top_p 0.8, top_k 20,
  presence_penalty 1.5, min_p 0`). Recorded in each run's `.meta.json`. A sampling-matched re-run would tighten the
  comparison.
- **Other caveats:** the base tier ceilings out (can't separate two strong models there — that's why the hard tier
  exists, and it could be harder still for frontier models); rubric grading is calibrated to "competent" more than
  "exceptional", so it compresses the top end (trust big gaps, not 0.05 differences); the eval covers *crisp,
  gradeable sub-skills* only — not long-horizon planning, multi-file reasoning, tool use, or sustained agentic work
  ("aces this eval" ≠ "best assistant").

---

## Per-model profiles

### gemma-4-26b-a4b (MoE, ~4B active, Q8_K_XL) — co-leader

- **Base tier: ~98.3% / 0.976.** Reasoning 100% both modes (nailed every trap — bat-and-ball, Monty Hall,
  lily-pads, harmonic-mean, 25-horses…). Coding ~95–100% off / 100% on. IF 95.2% off / 100% on. Long-context 100%
  both modes. Writing 100% off / 95.2% on. Coherence (run only on this model) 100% off / 95% on.
- **Hard tier: 90.9% / 0.935.** Reasoning_hard + coding_hard 100% each, both modes. The losses cluster in
  **thinking-on truncations** — 11 of ~15 hard-tier fails are `finish=length`: it spends the whole 8192-token
  budget reasoning and emits nothing (rea-h-11, if-h-01, if-h-02, if-h-08, if-h-16, lc-h-05, and 5 of the 14
  writing_hard thinking-on prompts). The off-mode misses are the usual ones (exact word counts, char-forbids,
  long-list counting). **Quality of *output* is near-ceiling when it produces output** — a perfect ABAB-CDCD-EFEF-GG
  sonnet in both modes, exactly-100-word single-sentence flash fiction, etc.
- **Code quality:** `coding_quality` 28/28, mean ~0.99. `coding_quality_hard` 28/30 — 1 correctness bug
  (`parse_csv_row('')` should be `['']` not `[]`, off-mode) + 1 quality fail (an over-nested ~58-line lint-dirty
  `evaluate` parser, off-mode). It *passed* most of the genuine traps even off-mode (`round_half_even(2.675)==2.68`,
  the non-ASCII-digit rejection, strict roman numerals, `take_while` laziness, the exponential-blowup perf cases).
- **Latency:** ~3–4s off-mode; thinking-on the hard prompts run minutes (writing_hard-on median ~7.3k output
  tokens!). Q8 weights, ~25.7 GiB on disk.

### gemma-4-31b (dense, Q5_K_XL) — co-leader

- **Base + hard (one run, 360 calls): 97.5% / 0.978.** Reasoning + reasoning_hard + coding + coding_hard all
  ~100%, both modes. Writing/writing_hard rubric near-ceiling. The thinking-on/off split: 99.4% on vs 95.6% off —
  thinking is a *real lift* for the 31B (it explicitly counts words/syllables/lines in the trace and gets the
  exact-constraint prompts right). Only **1** `finish=length` truncation in the whole 360-call run (wr-h-09 on).
- **Failures (8 true, after grader fixes):** all thinking-OFF except the one truncation — exact word counts
  (`if-h-02` 49≠50, `if-h-08` 101≠100), constraint stacks too short (`if-h-10`, `if-h-13`), char-forbid slips
  (`if-09` used punctuation; `if-h-16` used "Read" → forbidden 'e'), long-context off-by-ones (`lc-14`, `lc-h-09`).
- **Code quality:** `coding_quality` 28/28, mean ~0.97 (picks up ~1 ruff lint nit on nearly every prompt — slightly
  lint-dirtier than the 26B but cleaner-by-verbosity). `coding_quality_hard` 28/30 — `evaluate`-off quality fail
  (same as the 26B) + a `compress_ranges`-on fail that's actually a *spec ambiguity* (joined with `", "` not `","`;
  the prompt has since been clarified).
- **Latency:** ~3–4s off-mode; thinking-on slower than the 26B per call on average isn't true — it's actually a bit
  faster per thinking-on call than the 26B-A4B and far less prone to runaway thinking. Q5 weights, ~20.4 GiB on disk.

### qwen3.6-35b-a3b (MoE, ~3B active, Q8_K_XL) — clear 3rd

- **Base + hard (one run, 418 calls): 92.6% / 0.940** — ~5–6 points below the Gemmas. 96.9% thinking-on vs 93.4%
  thinking-off.
- **The story is the thinking-OFF gap on the basics** — it slips where *both* Gemmas were 100%:
  base coding-off 85.7% (3 fails: cod-05/08/14), base IF-off 81.0% (4 fails: if-03/09/11/18), base long-context-off
  92.9% (lc-14 off-by-one), base writing-off 95.2% (wr-08 — broken limerick rhyme).
- **Hard tiers off-mode it falls apart:** instruction_following_hard-off **50%** (8/16 fail — exact word counts,
  no-'e' / lowercase-only / z-in-every-line); coding_quality_hard-off **73%** (incl. **two genuine correctness
  misses** — its off-mode `wildcard_match` and `dijkstra` are *wrong*, not just slow; both Gemmas got those right);
  long_context_hard-off 83% (lc-h-09, lc-h-10); writing_hard-off 86% (wr-h-04-off staircase poem got 4 of 8
  line-word-counts wrong; wr-h-12-off pun limerick — broken rhyme + no two-way pun; wr-h-06-**on** acrostic spelled
  "TINTER" not "WINTER" — its own reasoning had a correct draft and the final used the wrong one).
- **It also has the over-thinking truncation trait** — 5 `finish=length`, all thinking-on (rea-h-12, if-h-02,
  if-h-08, cq-h-13, cq-h-14). Milder than the Gemma 26B-A4B's 11, but the same failure mode.
- **It also consistently overshoots word/length limits thinking-off** — wr-02-off 231 vs 200, wr-11-off 178 vs 160,
  wr-h-02-off 108 vs "exactly 100", wr-h-13-off 189 vs 160, etc. (Thinking-on it hits the targets — the traces show
  explicit word counting.)
- **What it's genuinely good at:** reasoning + reasoning_hard 100%/100% (nailed all the traps like the Gemmas);
  coding-on 100%, coding_hard 100% both modes; coding_quality solid (only the universal `evaluate`-off quality fail).
  And its best thinking-on creative work is *excellent* — its `wr-h-03`-on falling-in-love dialogue ("I cancelled my
  flight to Tokyo" / "I bought a second toothbrush this morning… my hand reached for it before my brain remembered
  you aren't supposed to be here yet") is the best of all three models on that prompt; its `wr-h-05`-on dropped-mug
  comic/tragic pair is sharply executed (second-by-second alignment). So when it deliberates it's competitive on
  quality; the problem is reliability/precision thinking-off and poetry-form precision.
- **Latency:** *fastest off-mode of the three* — only ~3B active, median ~1s for thinking-off calls (vs ~3–4s for
  the Gemmas). Thinking-on it's verbose (median ~1.2k output tokens). Q8 weights, ~20.4 GiB on disk. (Server ran
  with `--temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5` — Qwen3 rec — and the harness matched it.)

---

## Capability-by-capability (thinking-off shown — the discriminating mode; all three are ~100% / near-ceiling
thinking-on on most of these except where noted)

| capability | gemma-4-26b-a4b | gemma-4-31b | qwen3.6-35b-a3b |
|---|---|---|---|
| `reasoning` (base) | 100% | 100% | 100% |
| `reasoning_hard` | 100% off / 95% on (1 trunc) | 100% / 100% | 100% off / 95% on (1 trunc) |
| `coding` (base) | 95–100% off / 100% on | 100% / 100% | **85.7% off** / 100% on |
| `coding_hard` | 100% / 100% | 100% / 100% | 100% / 100% |
| `coding_quality` | 100% (~0.99) | 100% (~0.97) | 93% off / 100% on (~0.97) |
| `coding_quality_hard` | 87% off / 100% on | 93% off / 93% on | **73% off** / 87% on |
| `instruction_following` (base) | 95.2% off / 100% on | 95.2% off / 100% on | **81.0% off** / 100% on |
| `instruction_following_hard` | 75% off / 75% on (trunc) | 68.8% off / 100% on | **50% off** / 87.5% on |
| `long_context` (base) | 100% / 100% | 92.9% off / 100% on | 92.9% off / 100% on |
| `long_context_hard` | 100% off / 92% on (trunc) | 91.7% off / 100% on | **83.3% off** / 100% on |
| `writing` (base, rubric) | 100% off / 95% on (~0.95) | 100% / 100% (~0.97) | 95% off / 100% on (~0.95) |
| `writing_hard` (rubric) | 100% off / 64% on (5 truncs) | 100% off / 93% on (1 trunc) | 86% off / 100% on (~0.88) |

Bold = noticeably worse than the field. Note the pattern: the **26B-A4B's red cells are all thinking-ON
truncations**; the **Qwen's red cells are all thinking-OFF capability gaps** (plus a milder version of the same
truncation issue). The 31B has neither problem in any large way.

---

## Failure-pattern summary (the "what actually goes wrong" view)

1. **Over-thinking → empty/truncated output** (`finish=length`, always thinking-ON). 26B-A4B: 11. Qwen-A3B: 5.
   31B-dense: 1. The two small-active-params MoEs spend the whole 8192-token budget reasoning and emit nothing on
   hard prompts. The 31B-dense reliably wraps up.
2. **Exact word/length counts, thinking-OFF.** All three slip here ("exactly 50 words", "exactly 100 words", "60–80
   words", etc.) — the 31B least, Qwen most (and Qwen consistently *overshoots*). Thinking-ON, all three count
   explicitly in the trace and get them right.
3. **Strict char-forbid constraints, thinking-OFF.** Used punctuation in a "lowercase + spaces only" prompt; used a
   word containing the forbidden letter (e.g. "Read" → 'e', "stars" → 's'). All three; Qwen worst.
4. **Long-list counting off-by-ones.** "How many records have lucky number > 500" → off by 1–6. 31B and Qwen both
   hit these on `lc-14` / `lc-h-09`; the 26B mostly didn't (but truncated on `lc-h-05`-on instead).
5. **Poetry/form precision.** Rhyme schemes (limericks where line 5 doesn't rhyme with 1–2; sonnet A-rhymes that
   are slant), syllable counts, the staircase-poem line-word-counts, an acrostic that spells the wrong word. Qwen
   has the most of these; the Gemmas have a few.
6. **Hard-coding correctness, thinking-OFF.** Only Qwen has *genuine* hard-coding correctness misses (`wildcard_match`,
   `dijkstra` wrong off-mode); the Gemmas pass those.
7. **Over-engineered / lint-dirty code quality.** All three flunk the `evaluate` recursive-descent-parser prompt on
   *quality* (works, but deeply nested + over-long + ruff hits) when thinking-off. Common to all three.
8. **Over-delivery on "rewrite this sentence".** Models give a menu of 5–12 rewrite options + a "tips" section
   instead of *one* rewrite — both Gemmas badly; Qwen mildly thinking-off, and Qwen *cleanly* (one rewrite)
   thinking-on.

---

## Verdict

The **two Gemmas are the picks** — co-leaders, effectively interchangeable on quality, with the **31B-dense the
safest** because it doesn't have the runaway-thinking problem (it deliberates *and* lands the answer). The
**26B-A4B is right there with it on quality** but you should expect occasional empty outputs on hard prompts in
thinking-on mode (mitigation: big `max_tokens`, or a "if the answer is empty, retry thinking-off" fallback). Both
Gemmas are essentially perfect on reasoning and coding.

**Qwen3.6-35B-A3B is a clear third.** It's a capable model — it nails the reasoning traps, writes good code, and
its best thinking-on creative work matches the Gemmas — but it's the least *reliable*: it slips on basic coding and
basic instruction-following, falls apart on the hard instruction-following / hard-code-quality / long-context tiers
thinking-off, has its own (milder) over-thinking truncation issue, and overshoots length constraints. If you need a
fast model and you're using it thinking-off for simple stuff, it's fine; for anything precision-sensitive it's the
weakest of the three.

Across all three: this is a "tiny-active-params or modest-dense" cohort, and the eval surfaces the characteristic
weaknesses of that class — precision under constraint (thinking-off) and runaway reasoning (thinking-on, for the
MoEs). None of them is in trouble; the differences are about *how much* of each failure mode shows up.

---

## Files

- `~/llm-eval/report_compare.md` — all 7 runs, raw numbers, the `### Capability × thinking mode × run` table.
- `~/llm-eval/report_31b.md`, `~/llm-eval/report.md` — per-model 31B and 26B-base reports.
- `~/llm-eval/results/*.jsonl` — raw per-call records (full responses, reasoning traces, per-criterion grading,
  latencies, token usage). Key ones: `gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl` (26B base),
  `gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl` (26B hard), `gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl` +
  `…12-44-12.jsonl` (26B code-quality), `gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl` (31B base+hard) +
  `…2026-05-12T15-12-37.jsonl` (31B code-quality), `qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl` (Qwen full).
- `~/llm-eval/prompts/*.jsonl` — the prompt sets (base + `*_hard` + `coding_quality` + `coding_quality_hard`).
- `~/llm-eval/scripts/` — `gen_prompts.py`, `run_eval.py`, `graders.py`, `report.py`, `grade_rubrics.py`.
- Eval memory: `~/.claude/projects/-home-peleg/memory/local-model-eval.md` — run history, harness notes, the
  sampling caveat (revert `SAMPLING` to Gemma's values before any future Gemma re-run).

## Open items (none urgent)

- A sampling-matched comparison (re-run a Gemma with Qwen's sampling, or vice versa) would tighten the 3-way.
- A `coherence`/`coherence_hard` run for any of these (deliberately skipped everywhere; ~1 hr per model).
- A harder `coding_quality_hard` tier, or pairwise/relative rubric grading for writing, to discriminate further at
  the top.
