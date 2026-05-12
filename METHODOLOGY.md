# Methodology

How this eval works — what it tests, how it grades, what's recorded, and what it does *not* measure. The full
per-prompt catalog is in **[`TESTS.md`](TESTS.md)**; results write-ups are in **[`ANALYSIS.md`](ANALYSIS.md)** (the
narrative) and **`report_compare.md`** (the numbers tables).

---

## 1. What this is

A small, self-hosted eval for local LLMs served via [llama.cpp](https://github.com/ggml-org/llama.cpp)'s
OpenAI-compatible HTTP endpoint. It hits the model with a fixed prompt set, captures every response **and its
reasoning trace**, grades each call, and writes one JSONL line per call. The goal is a reproducible, head-to-head
comparison of *crisp, gradeable sub-skills* across models and across the "thinking on / thinking off" axis — not a
benchmark of everything a model can do (see §11 for what's deliberately out of scope).

Everything lives in `~/llm-eval/`:

```
prompts/        the prompt sets (one .jsonl per capability/tier) — see TESTS.md
scripts/        gen_prompts.py · run_eval.py · graders.py · grade_rubrics.py · report.py
results/        one .jsonl per run (+ .log mirror + .meta.json) — the raw record
report*.md      generated comparison reports
ANALYSIS.md     narrative analysis of the runs done so far
METHODOLOGY.md  (this file)
TESTS.md        the per-prompt catalog table
```

---

## 2. The harness flow (`run_eval.py`)

1. **Probe the server** (`/v1/models`, `/props`, the `llama-server` cmdline) to record what's actually running:
   model file, served id, llama.cpp build, served context length, server cmdline, hardware. Stored in
   `<run>.meta.json`.
2. **Build the plan**: for each requested capability, load `prompts/<cap>.jsonl`; for each prompt, for each
   requested thinking mode, emit one call. So a prompt set of N prompts run with `--modes on,off` = 2N calls.
3. **Run each call**: send `{messages, max_tokens, sampling…, chat_template_kwargs:{enable_thinking: bool}}` to
   `POST /v1/chat/completions`. Capture `content`, `reasoning_content`, `finish_reason`, token usage, latency.
4. **Grade it** immediately (programmatic graders run inline; rubric graders mark the record `pending` for a later
   pass — see §6).
5. **Write** one JSONL line per call to `results/<tag>__<ISO-timestamp>.jsonl`, plus a `.log` mirror of progress.
   The `--tag` is the name the run is recorded under (e.g. `gemma4-31b-q5kxl`); it's *not* tied to the server's
   model id.

`--concurrency` controls how many requests are in flight at once (default 1 = strictly serial → clean, uncontended
latencies; >1 exercises continuous batching but makes per-call latency contended and writes results out of plan
order — every line is self-describing so the report doesn't care, but latency numbers become non-comparable). All
the runs reported in `ANALYSIS.md` used `--concurrency 1`.

---

## 3. The thinking-on / thinking-off axis

Every prompt is run **twice** — once with the model's reasoning ("thinking") mode on, once off — because whether
deliberation *helps* is itself a key result. The toggle is `chat_template_kwargs: {enable_thinking: true|false}`
(the convention used by both Gemma and Qwen chat templates in recent llama.cpp builds); reasoning comes back in a
separate `reasoning_content` field and the `content` is cleaned of `<think>` tags. Before a real run on a new model,
the harness's behavior is verified with a quick manual probe (does `reasoning_content` populate when on / stay empty
when off?).

What this surfaces in practice: small models often *need* the scratchpad to hit exact-constraint prompts (they
count words/syllables/lines in the trace and get them right); but small-active-params MoEs can also *over-think* —
spend the entire token budget reasoning and emit nothing (`finish=length` with empty `content`). Both behaviors are
real, repeatable, and exactly what running both modes is meant to expose.

---

## 4. Two tiers per capability

- **Base tier** (`prompts/<cap>.jsonl`) — ~14–21 prompts each, broad coverage, deliberately *not* hard. It's a
  sanity floor: a competent model should ceiling it. Frozen, so prior runs stay comparable. The downside is the
  ceiling effect — it can't separate two strong models.
- **Hard tier** (`prompts/<cap>_hard.jsonl`) — ~12–20 each, deliberately tricky: prompts a strong model should miss
  some of. Subtle correctness traps, asymptotics that bite (enforced by a timeout on a large input), stacked
  constraints, form precision. This is the discriminating set. Opt-in via `--caps <cap>_hard` / `--caps hard` /
  `--caps everything`.
- Plus two code-specific tiers — `coding_quality` and `coding_quality_hard` — which grade *correctness AND code
  quality* (see §7).

Run shortcuts in `run_eval.py`: `--caps all` = the base caps; `--caps hard` = the `*_hard` caps; `--caps everything`
= both; or an explicit comma-separated list. `--caps … --smoke` does 2 prompts/cap, stdout only (always do one
before a real run).

---

## 5. The capabilities

| capability | what it probes | grading |
|---|---|---|
| **reasoning** | multi-step word problems, logic puzzles, the classic "trap" problems (bat-and-ball, Monty Hall, lily-pads-half-the-lake, harmonic-mean speed, 25-horses, knights-and-knaves, gcd/lcm, river-crossing…) — does the model compute the *right* answer | programmatic (the answer is a specific number / fraction / word) |
| **coding** | write a Python function to spec — palindrome, FizzBuzz, flatten, Roman↔int, GCD, Caesar cipher, interval-merge, RLE, etc. | programmatic (extracted code run against hidden unit tests) |
| **coding_quality** | write *production-quality* Python — must work AND be clean: type hints, docstring, input validation, efficient idiomatic approach. Has its own permissive system prompt (the regular coding one forbids docstrings) | programmatic: correctness unit tests + robustness tests + an `ast`+`ruff` static-analysis grader (see §7) |
| **instruction_following** | follow *literal* constraints — exact word/line/paragraph counts, forbidden characters, "first word X, last word Y", JSON-shape, "only lowercase and spaces", numbered/bulleted structure. The hard tier stacks 2–4 constraints at once | programmatic (counts, char-forbids, regex structure, JSON-shape, substring-occurrence counts) |
| **long_context** | retrieve / scan / count over a synthetic haystack of 60–250 short personnel records — needle ("what's X's lucky number"), count ("how many live in city Y"), the Nth-occurrence-of-a-hobby, windowed counts, retrieve-3-and-sum, contradiction/correction handling. Haystacks are generated, so the gold answer is known exactly | programmatic (numeric / name-from-records) |
| **writing** | craft tasks — haiku, sonnet (ABAB CDCD EFEF GG), cover letter, mystery opening, limerick, bedtime story, "rewrite this sentence", flash fiction with a bookend constraint, song lyric with an identical chorus, acrostic, 100-word single-sentence story, second-person/present-tense scene, archaic-register continuation… | rubric (Claude scores 1–5 per named criterion — see §6) |
| **coherence** | internal consistency under self-imposed structure — invent terms and reason from them, interleaved causal chains, a dungeon with a provably-shortest path, invent a base-6 numeral system and verify the arithmetic, a 4-generation family tree + distant-relation queries, necessary-vs-sufficient classification. *(Currently excluded from the comparison runs by choice — it's a "is it broken" floor that strong models ceiling.)* | rubric |

The exact prompts, ids, and graders for every one of these are in **[`TESTS.md`](TESTS.md)**.

---

## 6. Grading

### Programmatic graders (`scripts/graders.py`)

Objective, reproducible, binary pass/fail. A `grader` is a dict `{"type": …, …}` or a list of such dicts (all must
pass; the score is the mean of the sub-scores). Types:

- `numeric {gold, tol}` — pulls the answer number (prefers the first number after the last "answer" mention, then
  `\boxed{…}`, then the last number) and compares to `gold` within `tol`.
- `regex {pattern, group, group_equals, must_not, ignorecase}` / `regex_all {patterns}` — text-pattern checks;
  `must_not` flips it (the pattern must *not* match).
- `contains {values, mode, excludes, ignorecase}` — substring presence/absence.
- `word_count` / `line_count` / `sentence_count` / `paragraph_count` / `bullets` — structural counts, `{min, max}`
  or `{exact}` (word count can target the whole response or just the last paragraph).
- `forbid_char {chars}` — none of these characters may appear.
- `starts_ends {startswith, endswith}` — first / last word (tolerates surrounding punctuation/quotes).
- `json {required_keys, equals, top_type}` — extracts a fenced ```json block or the first balanced `{…}`/`[…]`,
  checks shape and key/value matches.
- `count {needle, regex, min/max/exact, ignorecase}` — counts occurrences of a literal or regex needle.
- `python {test, timeout}` — extracts the code block from the response, runs `code + test + print("OK_GRADER_PASS")`
  in an isolated subprocess (`python3 -I`), passes iff exit 0 and the sentinel printed. This is how coding and the
  robustness sub-tests are graded. A timeout (default 10s) on a deliberately large input is how some hard-coding
  prompts catch O(n²)-or-worse / exponential solutions.
- `code_quality {fn_name, require_type_hints, require_docstring, max_cc, max_nesting, max_body_lines, run_ruff, …}` —
  see §7.

### Rubric graders (writing & coherence) — `scripts/grade_rubrics.py`

There's no programmatic answer for "is this a good poem", so these are scored by Claude. A `rubric` grader names
~4 criteria (e.g. `rhyme_scheme_correct`, `imagery`, `length_adherence`, `fluency`); during the run the call is
marked `pending`, and afterwards a grading pass dumps each pending item — the prompt, the **reasoning trace**, and
the response — and Claude assigns 1–5 per criterion. Score = mean / 5, normalized to [0,1]; pass ≥ 0.6. The
reasoning trace is read alongside the response (it shows whether the model got there for the right reasons, whether
it caught its own constraint slips, etc.).

Calibration: rubric scoring is intentionally tuned to "is this *competent* / does it follow the brief / does it hit
the form" more than "is this *exceptional*". That means it compresses the top end — a merely-good and a brilliant
output can both land ~0.95. **Trust big gaps, not 0.05 differences.** A future improvement is pairwise/relative
grading (given model A's and B's output to the same prompt, pick the better one) which is far more reliable than
absolute 1–5.

---

## 7. The `coding_quality` tiers (correctness + robustness + static analysis)

`coding` only checks correctness. `coding_quality` / `coding_quality_hard` check *whether the code is good code*,
via a three-part grader per prompt:

1. **Correctness** — a `python` grader with the spec's unit tests.
2. **Robustness** — a second `python` grader with extra asserts beyond correctness: raises an appropriate exception
   on bad input; doesn't mutate its arguments; handles empty/None/single-element edge cases; and (where applicable)
   doesn't time out on a large input — a crude-but-real complexity check (the naive O(2ⁿ) recursive `nth_fibonacci`
   dies on n=40; the O(n²) `running_average` dies on n=60k; the O(n·k) `moving_max` dies on n=80k, k=2k).
3. **`code_quality`** — `ast`-based checks: does the target function have type hints on all params + return? a
   docstring? is its cyclomatic-complexity proxy ≤ ceiling? nesting depth ≤ ceiling? body length (docstring
   *excluded*) ≤ ceiling? any smells (bare `except`, mutable default args, `== None`)? — plus a `ruff check` lint
   pass if `ruff` is on PATH. Score = mean of the enabled checks; passes ≥ 0.7.

The automated score is the mean of those three (≥0.6 passes the list-grader). The "rubric layer" — Claude reading
the code for readability / idiom / right-algorithm — is a *report annotation*, not part of the automated grading
(this keeps the headline number objective and reproducible). The hard-tier prompts are chosen to be quality-
sensitive: tasks where the naive-but-correct solution looks bad, or that explicitly demand production quality, or
where the obvious implementation has the wrong asymptotics. Example finding: all three models tested so far flunk
the `evaluate` recursive-descent-parser prompt on *quality* when thinking-off (it works, but it's a deeply-nested,
over-long, lint-dirty blob).

> Setup note: `code_quality` uses `ruff` (`pip install --break-system-packages ruff`); if `ruff` isn't installed
> that sub-check is skipped (the `ast` checks still run). `radon` is *not* used — there's an `ast`-based McCabe
> cyclomatic-complexity proxy instead.

---

## 8. Sampling

Sampling parameters are set per the **loaded model's vendor recommendation** and recorded in each run's
`.meta.json` (so it's never ambiguous which run used which). Gemma rec: `temperature=1.0, top_p=0.95, top_k=64`.
Qwen3 rec: `temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0`. **Consequence:** a cross-model
comparison is *not* sampling-identical — a sampling-matched re-run (run model A with model B's sampling, or vice
versa) would tighten it. If you re-run a model, set `SAMPLING` in `run_eval.py` to that model's recommendation
first.

---

## 9. The results schema (the cross-run contract)

Each line of `results/<tag>__<ts>.jsonl` is one call. Keep this shape stable — it's what makes runs comparable:

```jsonc
{
  "model_tag": "...", "prompt_id": "...", "capability": "...", "thinking_mode": "on|off",
  "timestamp": "...", "tags": [...],
  "request": { "messages": [...], "max_tokens": N, ...sampling..., "chat_template_kwargs": {...} },
  "grader": { ... },                       // the grader spec used
  "response_text": "...",                  // model's answer (content)
  "thinking_text": "...",                  // reasoning_content (empty when thinking off)
  "latency_ms": ..., "usage": {...}, "finish_reason": "stop|length|...",
  "grading": { "score": 0..1|null, "passed": bool|null, "pending": bool, "notes": "...", ... }
}
```

`<run>.meta.json` records the served model id, file, params/size, n_ctx, llama.cpp build, server cmdline, sampling,
run duration, and the pass/fail/pending/error tallies. `report.py` takes one or more `.jsonl` paths and emits a
markdown report (overall, by thinking mode, by capability, by run, by capability×mode×run, plus per-rubric-criterion
means and a failures table) — it groups by `model_tag`, so a multi-file invocation is a multi-model comparison.

---

## 10. Reproducibility & adding a model

- **Prompt generation is deterministic** — `scripts/gen_prompts.py` is seeded, so `python3 scripts/gen_prompts.py`
  regenerates byte-identical prompt files (including the synthetic long-context haystacks). Re-run it after editing
  any prompt.
- **To eval a new model:** point llama.cpp at the GGUF, confirm it's serving (`/v1/models`), set `run_eval.py`'s
  `SAMPLING` to the model's vendor recommendation, do a quick `--smoke` (and a manual probe of the thinking toggle),
  then `python3 scripts/run_eval.py --tag <name> --caps everything --modes on,off --concurrency 1` (or a subset of
  caps). Grade the rubric items (`grade_rubrics.py list` → score → `grade_rubrics.py apply`), then add the new
  `.jsonl` to a `report.py` invocation alongside the others.

---

## 11. What this does *not* measure (limitations)

- **Ceiling effects.** The base tier maxes out for any competent model — it can't rank two strong models. That's
  what the hard tier is for, and even the hard tier should get harder for frontier models.
- **Rubric subjectivity.** Writing/coherence scores are one reviewer's calibrated judgment; they compress the top
  end. (Pairwise grading would fix this.)
- **Coverage.** The whole eval tests *crisp, gradeable sub-skills* — arithmetic, function-writing, constraint-
  following, retrieval, bounded creative tasks. It does **not** test long-horizon planning, multi-file reasoning,
  novel synthesis, tool use, or sustained agentic work. A model could ace every prompt here and still be a worse
  *assistant* than one that aces them too but also has the deeper capabilities the eval never probes. **"Tops this
  eval" ≠ "best model."** This caveat cuts against over-trusting the eval for strong models — not toward favoring
  weak ones (the design choices that look like "reward minimalism" — penalizing over-delivery, rewarding concise
  code — are really "reward instruction-following and clean code", both of which the better model wins).
- **Sampling not identical across models** (see §8).
- **Latency is comparable only at `--concurrency 1`**, and only between models run on the same hardware/server
  config; the `n_ctx` and `max_tokens` policy also affect thinking-on behavior (a small thinking-token budget makes
  over-thinking models truncate).

---

## See also

- **[`TESTS.md`](TESTS.md)** — every prompt, its id, what it probes, its grader.
- **[`ANALYSIS.md`](ANALYSIS.md)** — narrative analysis of the runs done so far (3 models: gemma-4-26b-a4b,
  gemma-4-31b, qwen3.6-35b-a3b).
- **`report_compare.md`** — the numbers tables for those runs.
