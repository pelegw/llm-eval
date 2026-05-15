# Local-model eval — 5-way analysis

*gemma-4-26b-a4b · gemma-4-31b · qwen3.6-27b · qwen3.6-35b-a3b · qwen3.5-122b-a10b — written 2026-05-12, updated 2026-05-15*

This is the narrative companion to `report_compare.md` (which has the raw numbers tables) and the eval memory at
`~/.claude/projects/-home-peleg/memory/local-model-eval.md`. All five models were run through the eval harness
in `~/llm-eval/` (llama.cpp OpenAI-compatible endpoint, concurrency 1, both thinking modes). **Coherence was
excluded from all five** by request — the base/`*_hard` tiers below cover reasoning, coding, code-quality,
instruction-following, long-context, writing, and (new for the 2026-05-14 run onward) tool_calling.

**Quant caveat for the 5th model**: qwen3.5-122b-a10b was run at **Q3_K_XL** (aggressive 3-bit), much more
quantized than the other four (Q5/Q8). The discussion below flags where the underperformance is plausibly
quant-attributable.

---

## TL;DR

| model | architecture | quant | overall pass / mean | rank |
|---|---|---|---|---|
| **gemma-4-31b** | 31B dense | Q5_K_XL | **97.4%** / 0.975 mean (470 calls) | **🥇 1st** |
| **gemma-4-26b-a4b** | 26B MoE, ~4B active | Q8_K_XL | 95.2% / 0.955 mean (746 calls, multi-run) | **🥈 2nd** |
| **qwen3.6-27b** | 27B dense | Q8_K_XL | **95.1%** / 0.959 mean (470 calls) | **🥉 3rd — new model 2026-05-14** |
| **qwen3.6-35b-a3b** | 35B MoE, ~3B active | Q8_K_XL | 93.0% / 0.943 mean (470 calls) | 4th |
| **qwen3.5-122b-a10b** | 122B MoE, ~10B active | Q3_K_XL | 92.6% / 0.943 mean (470 calls) | 5th — Q3 quant penalty |

- **Gemma-4-31B is the outright #1.** Cleanest run across the board — only 1 truncation in 470 calls, lowest of
  any model. Best mean rubric score for writing. Wins or ties on every cap except tool_calling (where Gemma-26B-A4B
  pulled the perfect 52/52). The "dense-and-disciplined" pick.
- **Gemma-26B-A4B (MoE) is 2nd** but with the *most* over-thinking truncations (26 across 746 calls — note the
  inflated n comes from having two full base runs plus a separate code-quality run; per-run rate is ~3%). When it
  produces output, quality is competitive with the 31B; the truncation pathology is the main thing keeping it from
  tying. Won tool_calling outright (52/52 perfect).
- **Qwen3.6 27B (the new dense Qwen) takes a strong 3rd.** Beats its 35B-A3B MoE sibling by 2pp despite being
  smaller in total params — the dense-architecture-at-this-scale story. Tool_calling perfect 52/52. Writing-hard
  thinking-on 14/14 (joining Gemma-31B as the only two models to clear that cell). Zero writing truncations of
  any kind. Pays for it on instruction_following_hard off-mode (56.2%, weakest cell in its run).
- **Qwen3.6-35B-A3B (MoE) drops to 4th** behind its smaller-but-dense Qwen sibling. Same character as before:
  slips on basic coding-off (85.7%) and basic IF-off (81.0%), worst IF-hard-off in the cohort at 50%, plus the
  enum-pick and parallel-call discipline misses on tool_calling.
- **Qwen3.5-122B-A10B at Q3 finishes 5th** — *despite ~4× the parameter count of Qwen3.6*. It matches the Gemmas on
  reasoning + hard-coding correctness (100% both), but falls apart on `coding_quality_hard`-off (**53.3%**, the
  lowest cell in any model × cap), shows the **most truncations** of any model (13, all thinking-on), and is **2×
  slower** than Qwen3.6 wall-clock. The aggressive Q3 quant is the most likely culprit — bigger model, more lossy
  weights, the loss dominates the size advantage.
- **Code quality is the least-differentiating axis at the base tier** — all five write solid, idiomatic,
  well-typed, well-documented Python at thinking-on (`coding_quality` mean ≥ 0.96 for everyone). At the *hard*
  tier off-mode the spread is huge — Gemma-31B 93% → Qwen3.6 27B 87% → Qwen3.6 35B-A3B 73% → Qwen3.5-Q3 53%.
- **Practical:** run any of these **thinking-on for precision-sensitive work** (exact counts, stacked constraints,
  correctness-critical code) — but the three MoEs (26B-A4B, Qwen3.6-A3B, Qwen3.5-A10B-Q3) will sometimes burn the
  whole token budget thinking and emit nothing on hard prompts, so give them a generous `max_tokens` cap /
  fallback. The two dense models (Gemma-31B, Qwen3.6-27B) are the safest bets: they deliberate *and* land the
  answer.

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
  sampling (`temp 1.0, top_p 0.95, top_k 64`); both Qwen runs used Qwen3's (`temp 0.7, top_p 0.8, top_k 20,
  presence_penalty 1.5, min_p 0`). Recorded in each run's `.meta.json`. A sampling-matched re-run would tighten the
  comparison.
- **Quant — also NOT identical**: gemma-4-26b-a4b at Q8_K_XL, qwen3.6-35b-a3b at Q8_K_XL, gemma-4-31b at Q5_K_XL,
  qwen3.5-122b-a10b at **Q3_K_XL** (much more aggressive). The Q3 means qwen3.5's results aren't strictly
  apples-to-apples — they're "what this model looks like at the quant it actually fits in", which is the realistic
  product question, but means a "raw architecture quality" attribution to it would be wrong.
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
- **Latency:** *fastest off-mode of the cohort* — only ~3B active, median ~1s for thinking-off calls (vs ~3–4s for
  the Gemmas). Thinking-on it's verbose (median ~1.2k output tokens). Q8 weights, ~20.4 GiB on disk. (Server ran
  with `--temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5` — Qwen3 rec — and the harness matched it.)

### qwen3.6-27b (27B dense, Q8_K_XL) — 3rd, the dense Qwen surprise (run 2026-05-14)

- **Overall: 95.1% / 0.959 mean** across 470 calls in 11h32m. Beats its 35B-A3B MoE sibling by 2pp and finishes a
  hair behind Gemma-26B-A4B at 95.2% — effectively tied for 2nd/3rd. Architecturally, this is the same model family
  as Qwen3.6 35B-A3B but **dense at 27B**, on **Qwen3 sampling** (`temp 0.7, top_p 0.8, top_k 20, presence_penalty
  1.5, min_p 0`), Q8_K_XL (~32.9 GiB).
- **Perfect caps**: reasoning + reasoning_hard 84/84 (matches everyone). coding_hard 40/40 both modes. **tool_calling
  + tool_calling_hard 52/52 (matches Gemma-26B-A4B as the only two to ace tool calling)**. writing_hard thinking-on
  14/14 (matches Gemma-31B as the only two; the 35B-A3B was 100% here too actually, while the 26B and Qwen3.5-Q3
  blew up with 5 truncations apiece).
- **The clearest "dense beats MoE" evidence in the eval**: compared to its 35B-A3B sibling, the 27B dense:
  - Cleans up basic IF-off (90.5% vs 81.0%)
  - Cleans up basic coding-off (100% vs 85.7% — no cod-05/08/14 misses)
  - Cleans up basic long_context (100% on, vs the 35B-A3B's lc-14-off off-by-one — *but the 27B still hit
    lc-14-off the same way, 92.9%*)
  - Matches on coding_quality_hard-off (86.7% vs 73.3%, big improvement)
  - Hits the same IF-hard-off pathology (56.2% vs 50%, slight improvement)
- **Where it slips**: coding/cod-12-on truncation (10.7 min of thinking → empty), instruction_following_hard-off
  56.2% (the universal off-mode constraint-stacking failure), one timeout *error* on long_context_hard/lc-h-09-on
  (the 900s request cap — first error of any run in the eval), and a few writing nits (cover letter 223 words, story
  continuation 167 words, recursion story 150 — model trends slightly long off-mode).
- **The Qwen-family over-thinking pathology shows up here too, just less.** 4 truncations total
  (cod-12-on, if-h-02-on, cq-h-13-on, cq-h-14-on), all coding-style hard prompts where the trace spirals into
  draft-and-redraft loops. Better than 35B-A3B's 5 / Qwen3.5-Q3's 13 / 26B-A4B's 11, but more than Gemma-31B's 1.
  Refutes the "purely architectural MoE-only" theory of truncations — the Qwen3-rec sampling and chat-template
  thinking style contribute, even for dense models.
- **Latency**: slowest of the cohort. 691.8 min wall-clock for 470 calls = ~88s/call avg. Comparable to
  Qwen3.5-Q3 (slower per-token than Gemma-31B). Q8 dense 27B on this hardware isn't a speed pick.
- **Notable writing strengths**: the wr-h-03 falling-in-love dialogue ("I kept the receipt from your birthday...
  even the way you hum when you think I'm asleep") earned full marks; wr-h-04 staircase poem hit all 8 word-counts
  exactly; wr-h-05 tone-pair (bus-stop coffee-spilled-on-letter) is excellent in both registers; wr-h-09 50-word
  twist horror ends with "Doll." — the entire earlier domestic-violence scene reframes as a child throwing dolls.
  Sharp craft when it lands. The wr-h-12 pun limerick ("Mike/pitch" rhyme broken) is the model's worst single
  writing prompt — same family of failure the 35B-A3B had.

### qwen3.5-122b-a10b (MoE, ~10B active, **Q3_K_XL**) — 5th, with quant caveat

- **Base + hard (one run, 418 calls): 91.9% / 0.938.** Despite being ~4× the parameter count of Qwen3.6, it lands
  *behind* it on overall score — a clear signal that the Q3 quant is biting. 95.5% thinking-on vs 88.0% off
  (biggest on/off gap of the four models).
- **The two things it does as well as anyone:** `reasoning` + `reasoning_hard` 100%/100% both modes (matches all
  four), and `coding_hard` 100%/100% (matches all four — its correctness is intact under Q3).
- **The places it fails worst:**
  - `coding_quality_hard` thinking-off **53.3%** — the lowest cell of any model × any cap. Of the 7 fails:
    quality issues on multiple "well-typed correct code under static analysis" prompts (complexity/nesting/ruff)
    plus a handful of correctness misses. Thinking-on it recovers to 86.7% (same as Qwen3.6) — deliberation
    rescues most of the gap.
  - `instruction_following_hard` thinking-off **62.5%** (10/16) — *better than Qwen3.6's 50%* but still well off
    the Gemmas (75% and 68.8%). Thinking-on: 75% with 4 truncations — verbose thinking eating the budget.
  - `writing_hard` thinking-on **64.3%** (rubric 0.693) — *tied with the Gemma-26B-A4B for the lowest rubric on
    this cap*, and for the same reason: **5 truncations** (wr-h-08, -09, -11, -12, -13 all thinking-on emit empty
    or chaotic output). Off-mode it recovers to 85.7% (rubric 0.829), still the weakest of the four off-mode but
    a real signal that "thinking" isn't reliable on hard creative tasks here.
- **It also has the over-thinking truncation trait, *worse* than Qwen3.6** — 13 total `finish=length`, all
  thinking-on (rate ~3%, up from Qwen3.6's ~1%). Cluster: 4× instruction_following_hard, 5× writing_hard, 2×
  coding_quality_hard, 1× instruction_following base, 1× writing base. Larger active-params (~10B) didn't tame
  the over-thinking — if anything they made it slower and more prone to budget-blow.
- **Quality of *output* when it produces output**: the *successful* thinking-on outputs are often very good — e.g.
  its `wr-h-05`-on comic/tragic vase-drop pair is sharply crafted; `wr-h-10`-on three-genres locked-drawer set
  hits all three voices distinctly; its `wr-h-04`-on staircase poem nails all 8 word-counts exactly; its
  `wr-h-14`-on six-stanza VCVCBC with identical chorus and genuine bridge departure is clean. The model has
  capacity; it's reliability and quant-cost that drag the numbers down.
- **Latency: the slowest of all four by a wide margin.** 552 min wall-clock for 418 calls = 0.76 calls/min
  (compare Qwen3.6's ~5h, Gemma-31B's ~6h for the same workload). Q3 quant on this MoE doesn't recover
  per-active-param compute the way Q8 does. Thinking-on writing prompts: median ~3k output tokens, max latency
  > 400s. Per-call latency 2–3× the next slowest model in most caps.
- **Q3 caveat in one line:** at Q4+ this model is presumably more competitive; at Q3_K_XL, it's a slow
  4th-place finisher on this hardware. The "more parameters = better" reflex doesn't hold below a quant floor.

---

## Capability-by-capability (thinking-off shown where it discriminates; all five are ~100% / near-ceiling
thinking-on on most of these except where noted)

| capability | gemma-31b | gemma-26b-A4B | qwen3.6-27b | qwen3.6-35b-A3B | qwen3.5-122b-A10B-Q3 |
|---|---|---|---|---|---|
| `reasoning` (base) | 100% | 100% | 100% | 100% | 100% |
| `reasoning_hard` | 100%/100% | 100% off / 95% on (1t) | 100%/100% | 100% off / 95% on (1t) | 100%/100% |
| `coding` (base) | 100%/100% | 95–100% off/100% on | 100% off / 95.2% on (1t) | **85.7% off**/100% on | 95.2% off/100% on |
| `coding_hard` | 100%/100% | 100%/100% | 100%/100% | 100%/100% | 100%/100% |
| `coding_quality` | 100% (~0.97) | 100% (~0.99) | 93% off / 100% on | 93% off / 100% on | 93% off / 100% on |
| `coding_quality_hard` | 93% off / 93% on | 87% off / 100% on | 87% off / 80% on (2t) | **73% off**/87% on | **53% off**/87% on |
| `instruction_following` (base) | 95.2% off/100% on | 95.2% off/100% on | 90.5% off/100% on | **81.0% off**/100% on | **85.7% off**/95.2% on (1t) |
| `instruction_following_hard` | 68.8% off/100% on | 75% off / 75% on (trunc) | **56.2% off** / 93.8% on (1t) | **50% off**/87.5% on | **62.5% off** / 75% on (4t) |
| `long_context` (base) | 92.9% off/100% on | 100%/100% | 92.9% off/100% on | 92.9% off/100% on | 100%/100% |
| `long_context_hard` | 91.7% off/100% on | 100% off / 92% on (1t) | 91.7%/91.7% (**1 err**) | **83.3% off**/100% on | 91.7%/100% |
| `tool_calling` (base+hard) | 51/52 (98.1%) | **52/52 (100%)** | **52/52 (100%)** | 50/52 (96.2%) | 51/52 (98.1%) |
| `writing` (base, rubric) | 100%/100% (~0.97) | 100% off / 95% on (~0.95) | 100%/100% (~0.96) | 95% off / 100% on (~0.95) | 100% off / 95% on (1t, ~0.94) |
| `writing_hard` (rubric) | 100% off / **93% on** (1t) | 100% off / **64% on** (5t) | **79% off** / **100% on** | 86% off / 100% on (~0.88) | **86% off** / **64% on** (5t, ~0.69) |

`(Nt)` = N truncations on this cap. **Bold = noticeably worse than the field on that cap.**

Patterns: the **31B-dense has no red cells anywhere**, just one truncation total. The **26B-A4B's red cells
are all thinking-ON truncations** (most of which are on writing_hard-on). The **27B-dense** sits between the
two patterns — cleaner basic-tier than the MoEs, slightly weaker IF-hard-off than the Gemmas, only 4 truncations.
The **Qwen3.6-35B-A3B red cells are all thinking-OFF capability gaps**, plus the truncation issue. The
**Qwen3.5-Q3 has BOTH problems** (worst-of-both: gaps off-mode + worst truncation rate on-mode).

---

## Tool calling — backfilled 2026-05-14, Qwen3.6 27B added 2026-05-15 (52 calls per model, both modes)

| model | tc base | tc hard | combined | wall-clock | notes |
|---|---|---|---|---|---|
| **gemma-4-26b-a4b** | 26/26 | **26/26** | **52/52 (100%)** | 2.5 min | one of two perfect scores; tool-call discipline is intact even thinking-on |
| **qwen3.6-27b** | 26/26 | **26/26** | **52/52 (100%)** | (part of full run) | the other perfect score; matches Gemma-26B-A4B on tool calling outright |
| **gemma-4-31b** | 26/26 | 25/26 | 51/52 (98.1%) | 4.2 min | 1 fail: tc-h-03 on, *silently translated Hindi in content* instead of explaining the enum doesn't support it — bypasses the spec's transparency requirement |
| **qwen3.5-122b-a10b-Q3** | 26/26 | 25/26 | 51/52 (98.1%) | 2.5 min × 2 (base + hard) | 1 fail: tc-h-03 on, thinking trace correctly identified "Hindi unsupported" then called translate(target_lang="zh") anyway — *real thinking-vs-action gap* |
| **qwen3.6-35b-a3b** | 26/26 | 24/26 | 50/52 (96.2%) | 3.9 min | 2 fails: (1) tc-h-03 off invented `target_lang="hi"` (not in the enum) — schema-discipline failure; (2) tc-h-05 on emitted only the Paris/celsius call, dropped the parallel Houston/fahrenheit call entirely |

**Key takeaways**:

1. **Tool calling is the most-uniformly-good cap of the eval** — the base tier is 100% across all 4 models in both modes (108/108 calls); only the hard tier discriminates, and only by 0–2 fails. **None of these models is *bad* at single-step tool use.**
2. **Wall-clock varies 1.7×**: the smaller-active-params models (Gemma-26B-A4B 2.5 min, Qwen3.5 5 min combined) finished fastest because tool-call outputs are short. The dense 31B is the slowest of the four for this cap (4.2 min, ~30s/call thinking-on average).
3. **`tc-h-03` (Hindi-not-in-enum) is the universally hardest prompt** — every model except the 26B-A4B failed it in one mode or another. Three distinct failure modes surfaced:
   - **Qwen3.6 off**: invented `"hi"` outside the enum (worst: ignored the schema entirely)
   - **Qwen3.5 on**: enumerated correctly in thinking, then called with `"zh"` (thinking-action gap)
   - **Gemma-31B on**: silently bypassed by translating to Hindi in content (no transparency)
   - **Gemma-26B-A4B both**: correctly refused + explained — clean pass
4. **`tc-h-05` (parallel mixed-enum: Paris in C, Houston in F)** caught Qwen3.6-on dropping one call entirely — real parallel-call discipline failure.
5. **The 26B-A4B's over-thinking pathology does NOT bite tool calling** — tool-call outputs are short, the thinking budget never gets exhausted, all 13 hard prompts pass thinking-on. This is the model's most-confident-passing cap.
6. **Q3-quant cost is absent here** — Qwen3.5-Q3 ties Gemma-31B-Q5 at 98.1%. Whatever the Q3 quant breaks in other caps (code-quality, instruction-following), it doesn't reach the structured-emission pathway.

**Implication for model selection**: if your use case is *single-step* tool calling (the "given a tool, call it right" pattern that covers most agent invocation paths), **the 26B-A4B and the 27B-dense both ace it**. Pick by other criteria — 26B-A4B is faster off-mode (~3B active); 27B-dense is more reliable on the rest of the eval. Both pair well with thinking-off for low-latency tool routing.

---

## Failure-pattern summary (the "what actually goes wrong" view)

1. **Over-thinking → empty/truncated output** (`finish=length`, always thinking-ON). 26B-A4B: 11. Qwen3.6-A3B: 5.
   **Qwen3.5-A10B-Q3: 13** (the new worst). 31B-dense: 1. The three MoEs all spend the whole 8192-token budget
   reasoning and emit nothing on hard prompts; the larger active-param count of Qwen3.5 didn't help, possibly
   because Q3 makes the deliberation pass less efficient per token. The 31B-dense reliably wraps up.
2. **Exact word/length counts, thinking-OFF.** All four slip here ("exactly 50 words", "exactly 100 words", "60–80
   words", etc.) — the 31B least, Qwen3.6 most (and Qwen3.6 consistently *overshoots*); Qwen3.5-Q3 misses some
   (wr-h-02-off: 89 words instead of exactly 100, wr-18-off: 103 instead of ≤100). Thinking-ON, all four count
   explicitly in the trace and get them right.
3. **Strict char-forbid constraints, thinking-OFF.** Used punctuation in a "lowercase + spaces only" prompt; used a
   word containing the forbidden letter (e.g. "Read" → 'e', "stars" → 's'). All four; Qwens worst.
4. **Long-list counting off-by-ones.** "How many records have lucky number > 500" → off by 1–6. 31B, Qwen3.6, and
   Qwen3.5 hit these on `lc-14` / `lc-h-09`; the 26B mostly didn't (but truncated on `lc-h-05`-on instead).
5. **Poetry/form precision.** Rhyme schemes (limericks where line 5 doesn't rhyme with 1–2; sonnet A-rhymes that
   are slant), syllable counts, the staircase-poem line-word-counts, an acrostic that spells the wrong word.
   Qwen3.5-Q3-off blows the staircase poem (4 of 8 line-word-counts wrong) and the iambic-pentameter mug ad
   (1 of 4 lines off by a syllable); Qwen3.6 had similar trouble. The Gemmas have a few.
6. **Hard-coding correctness, thinking-OFF.** Only Qwen3.6 has *genuine* hard-coding correctness misses
   (`wildcard_match`, `dijkstra` wrong off-mode); the Gemmas and Qwen3.5 pass those. Qwen3.5-Q3 instead loses
   on `coding_quality_hard`-off (quality + a few correctness mid-cases).
7. **Over-engineered / lint-dirty code quality.** All four flunk the `evaluate` recursive-descent-parser prompt on
   *quality* (works, but deeply nested + over-long + ruff hits) when thinking-off. Common to all four — a real
   architectural bias of this cohort, not a specific weakness.
8. **Over-delivery on "rewrite this sentence".** Models give a menu of 5–12 rewrite options + a "tips" section
   instead of *one* rewrite — both Gemmas badly; both Qwens mildly thinking-off, and both Qwens *cleanly* (one
   rewrite) thinking-on.
9. **The pun-limerick failure mode (Qwen3.5-Q3-off specifically)**: produces 4 draft limericks with
   `*(Wait, let me refine...)*` annotations between them — leaks thinking-style commentary into the response. A
   classic small-model-under-pressure failure that the bigger architecture didn't prevent under Q3.

---

## Verdict

**Gemma-4-31B is the outright #1.** The dense-and-disciplined pick. 97.4% pass, 0.975 mean, only 1 truncation in
470 calls — the cleanest run of any model in the cohort. Wins or ties on every cap except tool_calling (where it
loses to Gemma-26B-A4B and Qwen3.6-27B by a single prompt). Best mean rubric on writing. If you can fit Q5_K_XL
(~20 GiB), this is the daily-driver pick.

**Gemma-26B-A4B (MoE) is 2nd.** Output quality is competitive with the 31B; the *only* thing keeping it from
tying is the 26 over-thinking truncations across its multiple runs (per-run rate ~3%, concentrated in writing_hard
thinking-on where it loses 5 of 14). Won tool_calling outright (52/52). Mitigation if you want to use it: thinking-off
for hard creative prompts, or bump `max_tokens` past 8192.

**Qwen3.6 27B (the new dense Qwen) takes a strong 3rd.** 95.1% pass, beating its 35B-A3B MoE sibling by 2pp
despite being smaller in total params. Tool_calling perfect (52/52). Writing-hard thinking-on perfect (14/14, one
of only two models to clear that cell). Zero writing truncations of any kind. Pays for it on
`instruction_following_hard`-off (56%, the weakest cap in its run) and one timeout error on `long_context_hard`-on.
**Best dense-Qwen pick if you don't want a Gemma**, and a useful data point in the dense-vs-MoE-at-this-scale
question (the answer: dense wins by a couple of pp, all things equal in quant).

**Qwen3.6-35B-A3B (MoE) drops to 4th.** Same character as before: nails the reasoning traps, writes good code, has
its best thinking-on creative work that matches the Gemmas — but slips on basic coding and basic
instruction-following thinking-off, falls apart on the hard tiers off-mode, has the over-thinking truncation issue,
and overshoots length constraints. If you need fast-and-loose off-mode for simple stuff, it's the *fastest* in the
cohort (~1s median); for anything precision-sensitive its 27B-dense sibling is now the better choice.

**Qwen3.5-122B-A10B at Q3_K_XL finishes 5th — but with a quant asterisk.** The aggressive Q3 quant clearly costs
it: the *worst* `coding_quality_hard`-off rate of any model (53%), the *worst* truncation rate (13 thinking-on
truncations vs 1–11 for the others), and the *slowest* wall-clock by ~2× over Qwen3.6. It's not architecturally
worse than Qwen3.6 — when its thinking-on outputs do land they're often very good — but the
"more parameters under a more aggressive quant" tradeoff doesn't pay off below Q4 on this hardware. **If you can
fit Q4+ of a 70–122B model**, that's the right comparison to make next; this Q3 run isn't a verdict on the
architecture, just on the *quant×architecture* point you're forced to take.

Across all five: this is a "tiny-to-moderate active-params" cohort, and the eval surfaces the characteristic
weaknesses of that class — precision under constraint (thinking-off), runaway reasoning (thinking-on, for the
MoEs but also for the dense Qwens via the Qwen3-rec sampling style), and a quant floor below which raw parameter
count stops paying. None of them is in trouble; the differences are about *how much* of each failure mode shows up
and on which cap.

---

## Files

- `~/llm-eval/report_compare.md` — all 5 model runs, raw numbers, the `### Capability × thinking mode × run` table.
- `~/llm-eval/results/*.jsonl` — raw per-call records (full responses, reasoning traces, per-criterion grading,
  latencies, token usage). Key ones: `gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl` (26B base),
  `gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl` (26B hard), `gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl` +
  `…12-44-12.jsonl` (26B code-quality), `gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl` (31B base+hard) +
  `…2026-05-12T15-12-37.jsonl` (31B code-quality), `qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl` (Qwen3.6 35B full),
  `qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl` (Qwen3.5 full at Q3_K_XL),
  `qwen3.6-27b-q8kxl__2026-05-14T21-14-47.jsonl` (Qwen3.6 27B full, the first run with native `tool_calling`).
- Tool-calling backfill files (one per pre-existing model, 2026-05-13/14): `qwen3.5-122b-a10b-q3kxl__…23-02-43`
  + `…22-59-11`, `qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36`, `gemma4-31b-q5kxl__2026-05-14T00-16-43`,
  `gemma4-26b-a4b-q8km__2026-05-14T00-42-42`.
- `~/llm-eval/prompts/*.jsonl` — the prompt sets (base + `*_hard` + `coding_quality` + `coding_quality_hard` +
  `tool_calling` + `tool_calling_hard`).
- `~/llm-eval/scripts/` — `gen_prompts.py`, `run_eval.py`, `graders.py`, `report.py`, `grade_rubrics.py`,
  `make_tests_md.py`.
- Eval memory: `~/.claude/projects/-home-peleg/memory/local-model-eval.md` — run history, harness notes, the
  sampling caveat (revert `SAMPLING` to the right values per model family before any re-run).

## Open items (none urgent)

- A sampling-matched comparison (re-run a Gemma with Qwen's sampling, or vice versa) would tighten the 5-way.
- A **Q4+ rerun of qwen3.5-122b-a10b** would let us isolate quant cost from architecture quality.
- A `coherence`/`coherence_hard` run for any of these (deliberately skipped everywhere; ~1 hr per model).
- A harder `coding_quality_hard` tier, or pairwise/relative rubric grading for writing, to discriminate further at
  the top.
- `MAXTOK_THINKING` bump from 8192 → 16384 (would cut the 30+ truncations across models to a handful;
  doubles worst-case latency for the slow MoEs).
- A multi-step / agentic-loop tool-calling tier (the current `tool_calling` only tests *single-step* calls).
