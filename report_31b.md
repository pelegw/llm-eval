# Local model eval report

- Model tag(s): gemma4-31b-q5kxl
- Source file(s): gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl
- Capabilities: coding, coding_hard, instruction_following, instruction_following_hard, long_context, long_context_hard, reasoning, reasoning_hard, writing, writing_hard
- Thinking modes: off, on
- Total calls: 360  (graded 360, pending rubric 0)

## Run configuration

- Model tag: gemma4-31b-q5kxl
- Served model id: gemma-4-31b
- Model file: gemma-4-31B-it-UD-Q5_K_XL.gguf
- Parameters: 30,697,345,596 (~30.7 B)
- File size: 21,874,594,032 bytes (~20.4 GiB)
- Context (n_ctx): 262144
- Trained context: 262144
- Embedding dim: 5376
- Vocab size: 262144
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/gemma-4-31B-it-UD-Q5_K_XL.gguf -ngl 99 -c 524288 --parallel 2 -t 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on --jinja --host 0.0.0.0 --port 8080 --metrics -a gemma-4-31b`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=1.0, top_p=0.95, top_k=64
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=262144
- Run started: 2026-05-11T22-16-53
- Run duration (min): 287.5
- Total calls: 360
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning', 'coding', 'instruction_following', 'long_context', 'writing', 'reasoning_hard', 'coding_hard', 'instruction_following_hard', 'long_context_hard', 'writing_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 360
- calls_per_sec: 0.021
- results: pass=279, fail=11, pending_rubric=70, error=0

## Overall

| scope | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| all | 360 | 97.5% | 0.978 | 18282 | 259 |

## By thinking mode

| thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| off | 180 | 95.6% | 0.966 | 6993 | 100 |
| on | 180 | 99.4% | 0.990 | 40455 | 646 |

## By capability

| capability | n | pass rate | mean score | median latency (ms) | median out-tokens | pending |
|---|---|---|---|---|---|---|
| coding | 42 | 100.0% | 1.000 | 12438 | 204 |  |
| coding_hard | 40 | 100.0% | 1.000 | 18564 | 308 |  |
| instruction_following | 42 | 97.6% | 0.976 | 4862 | 78 |  |
| instruction_following_hard | 32 | 84.4% | 0.938 | 9110 | 149 |  |
| long_context | 28 | 96.4% | 0.964 | 24957 | 227 |  |
| long_context_hard | 24 | 95.8% | 0.958 | 51453 | 462 |  |
| reasoning | 42 | 100.0% | 1.000 | 17538 | 296 |  |
| reasoning_hard | 40 | 100.0% | 1.000 | 27191 | 456 |  |
| writing | 42 | 100.0% | 0.967 | 16913 | 282 |  |
| writing_hard | 28 | 96.4% | 0.941 | 36438 | 604 |  |

## Capability × thinking mode

| capability | thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|
| coding | off | 21 | 100.0% | 1.000 | 3836 | 58 |
| coding | on | 21 | 100.0% | 1.000 | 26539 | 445 |
| coding_hard | off | 20 | 100.0% | 1.000 | 7120 | 114 |
| coding_hard | on | 20 | 100.0% | 1.000 | 43481 | 719 |
| instruction_following | off | 21 | 95.2% | 0.952 | 1388 | 18 |
| instruction_following | on | 21 | 100.0% | 1.000 | 14073 | 233 |
| instruction_following_hard | off | 16 | 68.8% | 0.875 | 2176 | 30 |
| instruction_following_hard | on | 16 | 100.0% | 1.000 | 85797 | 1382 |
| long_context | off | 14 | 92.9% | 0.929 | 13864 | 73 |
| long_context | on | 14 | 100.0% | 1.000 | 33844 | 326 |
| long_context_hard | off | 12 | 91.7% | 0.917 | 26350 | 170 |
| long_context_hard | on | 12 | 100.0% | 1.000 | 143073 | 1673 |
| reasoning | off | 21 | 100.0% | 1.000 | 10138 | 171 |
| reasoning | on | 21 | 100.0% | 1.000 | 31228 | 526 |
| reasoning_hard | off | 20 | 100.0% | 1.000 | 20416 | 342 |
| reasoning_hard | on | 20 | 100.0% | 1.000 | 59994 | 985 |
| writing | off | 21 | 100.0% | 0.967 | 6743 | 111 |
| writing | on | 21 | 100.0% | 0.967 | 41810 | 701 |
| writing_hard | off | 14 | 100.0% | 0.964 | 7078 | 116 |
| writing_hard | on | 14 | 92.9% | 0.918 | 163928 | 2536 |

## Rubric criteria (mean, normalized 0–1)

| capability | criterion | n | mean |
|---|---|---|---|
| writing | adherence_to_prompt | 10 | 1.000 |
| writing | age_appropriateness | 2 | 1.000 |
| writing | appropriateness | 2 | 1.000 |
| writing | atmosphere | 2 | 1.000 |
| writing | balanced_critique | 2 | 1.000 |
| writing | bookend_constraint_met | 2 | 1.000 |
| writing | call_to_action | 2 | 1.000 |
| writing | characterization | 2 | 1.000 |
| writing | chorus_identical | 2 | 1.000 |
| writing | clear_value_prop | 2 | 1.000 |
| writing | completeness | 2 | 1.000 |
| writing | concision | 6 | 0.733 |
| writing | description_clarity | 2 | 1.000 |
| writing | emotional_resonance | 2 | 1.000 |
| writing | emotional_theme | 2 | 1.000 |
| writing | encouragement | 2 | 1.000 |
| writing | evokes_dawn | 2 | 1.000 |
| writing | fluency | 20 | 0.980 |
| writing | format | 2 | 1.000 |
| writing | four_lines | 2 | 1.000 |
| writing | hook | 2 | 1.000 |
| writing | humor | 2 | 0.600 |
| writing | imagery | 6 | 0.933 |
| writing | length | 8 | 1.000 |
| writing | length_adherence | 2 | 1.000 |
| writing | lightness_humor | 2 | 1.000 |
| writing | limerick_form | 2 | 1.000 |
| writing | meaning_preserved | 2 | 0.800 |
| writing | narrative_arc | 2 | 1.000 |
| writing | narrative_completeness | 2 | 1.000 |
| writing | narrative_quality | 2 | 1.000 |
| writing | naturalistic_dialogue | 2 | 1.000 |
| writing | on_topic | 2 | 1.000 |
| writing | persuasiveness | 2 | 1.000 |
| writing | professional_tone | 2 | 1.000 |
| writing | prose_quality | 8 | 1.000 |
| writing | realism | 2 | 1.000 |
| writing | restraint | 2 | 0.700 |
| writing | rhyme_and_meter | 2 | 0.800 |
| writing | rhyme_scheme_correct | 2 | 1.000 |
| writing | sensory_detail | 2 | 1.000 |
| writing | sincerity | 2 | 1.000 |
| writing | six_lines | 2 | 1.000 |
| writing | soothing_tone | 2 | 1.000 |
| writing | specific_detail | 2 | 1.000 |
| writing | specificity | 2 | 0.900 |
| writing | structure_correct | 2 | 1.000 |
| writing | tagline_punchiness | 2 | 1.000 |
| writing | three_line_form | 2 | 1.000 |
| writing | three_sentences | 2 | 1.000 |
| writing | tonal_continuity | 2 | 1.000 |
| writing | tone | 12 | 1.000 |
| writing | under_280_chars | 2 | 0.800 |
| writing | variety | 2 | 1.000 |
| writing | vividness_improved | 2 | 0.800 |
| writing | warmth_humor_balance | 2 | 1.000 |
| writing_hard | about_fifty_words | 2 | 0.600 |
| writing_hard | acrostic_spells_WINTER | 2 | 1.000 |
| writing_hard | actually_funny | 2 | 0.600 |
| writing_hard | age_appropriate | 2 | 1.000 |
| writing_hard | all_three_mention_locked_drawer | 2 | 1.000 |
| writing_hard | bridge_is_a_genuine_departure | 2 | 1.000 |
| writing_hard | chorus_identical_all_three_times | 2 | 1.000 |
| writing_hard | coherent_poem | 2 | 1.000 |
| writing_hard | coherent_poem_not_filler | 2 | 1.000 |
| writing_hard | comic_version_genuinely_comic | 2 | 1.000 |
| writing_hard | craft | 4 | 1.000 |
| writing_hard | creepiness | 2 | 0.500 |
| writing_hard | dialogue_only_no_narration | 2 | 1.000 |
| writing_hard | each_line_iambic_pentameter | 2 | 0.900 |
| writing_hard | each_opening_clearly_its_genre | 2 | 1.000 |
| writing_hard | earlier_text_supports_twist | 2 | 0.500 |
| writing_hard | emotional_coherence | 2 | 0.900 |
| writing_hard | emotional_resonance | 2 | 0.900 |
| writing_hard | events_identical_across_versions | 2 | 0.900 |
| writing_hard | exactly_100_words | 2 | 1.000 |
| writing_hard | exactly_four_lines | 2 | 1.000 |
| writing_hard | exactly_six_lines | 2 | 1.000 |
| writing_hard | final_word_recontextualizes | 2 | 0.500 |
| writing_hard | fluency | 4 | 0.950 |
| writing_hard | fourteen_lines | 2 | 1.000 |
| writing_hard | has_narrative_arc | 2 | 1.000 |
| writing_hard | imagery | 4 | 0.900 |
| writing_hard | imagery_and_theme | 2 | 1.000 |
| writing_hard | is_one_grammatical_sentence | 2 | 1.000 |
| writing_hard | limerick_form_correct | 2 | 1.000 |
| writing_hard | line_word_counts_1_through_8 | 2 | 1.000 |
| writing_hard | love_conveyed_through_subtext | 2 | 1.000 |
| writing_hard | meter_roughly_iambic_pentameter | 2 | 1.000 |
| writing_hard | narrative_progresses | 2 | 1.000 |
| writing_hard | narrative_quality | 2 | 1.000 |
| writing_hard | no_jargon_no_lesson_tone | 2 | 1.000 |
| writing_hard | no_love_words_used | 2 | 1.000 |
| writing_hard | no_modern_slips | 2 | 1.000 |
| writing_hard | persuasive_and_on_topic | 2 | 0.800 |
| writing_hard | present_tense_throughout | 2 | 1.000 |
| writing_hard | prose_quality | 6 | 1.000 |
| writing_hard | pun_on_pitch_works_both_ways | 2 | 1.000 |
| writing_hard | reads_naturally | 2 | 0.900 |
| writing_hard | realization_lands_emotionally | 2 | 1.000 |
| writing_hard | recursion_idea_conveyed | 2 | 1.000 |
| writing_hard | register_matched_throughout | 2 | 1.000 |
| writing_hard | rhyme_scheme_ABAB_CDCD_EFEF_GG | 2 | 1.000 |
| writing_hard | second_person_throughout | 2 | 1.000 |
| writing_hard | structure_VCVCBC | 2 | 1.000 |
| writing_hard | three_distinct_voices | 2 | 1.000 |
| writing_hard | tragic_version_genuinely_tragic | 2 | 1.000 |

## Failures (9)

| capability | prompt | mode | score | notes | finish/err |
|---|---|---|---|---|---|
| instruction_following | if-09 | off | 0.000 | match=None | stop |
| long_context | lc-14 | off | 0.000 | got 56 want 55 (tol 0) | stop |
| instruction_following_hard | if-h-02 | off | 0.333 | X:49 words (want 50..50) \| X:forbidden chars seen: {'s': 1} \| ok:ok | stop |
| instruction_following_hard | if-h-08 | off | 0.667 | X:101 words (want 100..100) \| ok:ok \| ok:hit=['one hundred words'] miss=[] forbidden_seen= | stop |
| instruction_following_hard | if-h-10 | off | 0.750 | ok:4 paragraphs (want 4..4) \| ok:8 sentences (want 8..8) \| X:29 words (want 60..80) \| ok:p | stop |
| instruction_following_hard | if-h-13 | off | 0.750 | ok:3 sentences (want 3..3) \| ok:1x 'however' (want 1..1) \| ok:pattern absent (good) \| X:22 | stop |
| instruction_following_hard | if-h-16 | off | 0.500 | ok:47 words (want 40..50) \| X:forbidden chars seen: {'e': 2} | stop |
| long_context_hard | lc-h-09 | off | 0.000 | got 88 want 90 (tol 0) | stop |
| writing_hard | wr-h-09 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted 8192-token budget (3900+ words of reasoning), fi | length |
