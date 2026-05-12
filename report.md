# Local model eval report

- Model tag(s): gemma4-26b-a4b-q8km
- Source file(s): gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl
- Capabilities: coding, coherence, instruction_following, long_context, reasoning, writing
- Thinking modes: off, on
- Total calls: 236  (graded 236, pending rubric 0)

## Run configuration

- Model tag: gemma4-26b-a4b-q8km
- Served model id: gemma-4-26b-a4b
- Model file: gemma-4-26B-A4B-it-UD-Q8_K_XL.gguf
- Parameters: 25,233,142,046 (~25.2 B)
- File size: 27,620,407,416 bytes (~25.7 GiB)
- Context (n_ctx): 262144
- Trained context: 262144
- Embedding dim: 2816
- Vocab size: 262144
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/gemma-4-26B-A4B-it-UD-Q8_K_XL.gguf -ngl 99 -c 524288 --parallel 2 -t 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on --jinja --host 0.0.0.0 --port 8080 --metrics -a gemma-4-26b-a4b`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=1.0, top_p=0.95, top_k=64
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 2
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=262144
- Run started: 2026-05-11T19-51-18
- Run duration (min): 98.9
- Total calls: 236
- n_ctx_used_by_runner: 262144
- capabilities: ['coherence', 'reasoning', 'coding', 'instruction_following', 'long_context', 'writing']
- thinking_modes: ['on', 'off']
- calls_planned: 236
- calls_per_sec: 0.04
- results: pass=152, fail=2, pending_rubric=82, error=0

## Overall

| scope | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| all | 236 | 98.3% | 0.976 | 21540 | 352 |

## By thinking mode

| thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| off | 118 | 98.3% | 0.975 | 8140 | 118 |
| on | 118 | 98.3% | 0.976 | 52645 | 898 |

## By capability

| capability | n | pass rate | mean score | median latency (ms) | median out-tokens | pending |
|---|---|---|---|---|---|---|
| coding | 42 | 97.6% | 0.976 | 13875 | 244 |  |
| coherence | 40 | 97.5% | 0.963 | 47676 | 866 |  |
| instruction_following | 42 | 97.6% | 0.976 | 7267 | 122 |  |
| long_context | 28 | 100.0% | 1.000 | 26057 | 263 |  |
| reasoning | 42 | 100.0% | 1.000 | 21150 | 388 |  |
| writing | 42 | 97.6% | 0.946 | 25769 | 468 |  |

## Capability × thinking mode

| capability | thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|
| coding | off | 21 | 95.2% | 0.952 | 3676 | 58 |
| coding | on | 21 | 100.0% | 1.000 | 49495 | 905 |
| coherence | off | 20 | 100.0% | 0.990 | 27710 | 498 |
| coherence | on | 20 | 95.0% | 0.935 | 74619 | 1321 |
| instruction_following | off | 21 | 95.2% | 0.952 | 1444 | 18 |
| instruction_following | on | 21 | 100.0% | 1.000 | 15352 | 266 |
| long_context | off | 14 | 100.0% | 1.000 | 14957 | 134 |
| long_context | on | 14 | 100.0% | 1.000 | 66353 | 685 |
| reasoning | off | 21 | 100.0% | 1.000 | 14389 | 258 |
| reasoning | on | 21 | 100.0% | 1.000 | 35322 | 638 |
| writing | off | 21 | 100.0% | 0.964 | 6376 | 114 |
| writing | on | 21 | 95.2% | 0.929 | 68283 | 1246 |

## Rubric criteria (mean, normalized 0–1)

| capability | criterion | n | mean |
|---|---|---|---|
| coherence | accuracy | 4 | 1.000 |
| coherence | age_appropriateness | 2 | 1.000 |
| coherence | argument_quality | 2 | 1.000 |
| coherence | arithmetic_consistency | 2 | 1.000 |
| coherence | balance | 2 | 1.000 |
| coherence | causal_chain | 2 | 0.600 |
| coherence | clarity | 38 | 0.974 |
| coherence | completeness | 22 | 0.991 |
| coherence | consistency_with_own_explanation | 2 | 0.900 |
| coherence | consistent_application | 2 | 1.000 |
| coherence | consistent_concept_use | 2 | 1.000 |
| coherence | definition_accuracy | 2 | 1.000 |
| coherence | definition_quality | 2 | 0.900 |
| coherence | explanation_clarity | 2 | 1.000 |
| coherence | follow_through | 2 | 1.000 |
| coherence | food_web_consistency | 2 | 1.000 |
| coherence | handles_tension_coherently | 2 | 1.000 |
| coherence | inference_grounded | 2 | 1.000 |
| coherence | inference_grounded_in_setup | 2 | 1.000 |
| coherence | internal_consistency | 18 | 0.922 |
| coherence | internal_consistency_each_side | 2 | 1.000 |
| coherence | logical_flow | 4 | 1.000 |
| coherence | no_new_claims | 2 | 1.000 |
| coherence | numerical_correctness | 2 | 1.000 |
| coherence | period_plausibility | 2 | 1.000 |
| coherence | persuasiveness | 2 | 1.000 |
| coherence | pitch_quality | 2 | 1.000 |
| coherence | plot_coherence | 2 | 1.000 |
| coherence | practical_correctness | 2 | 1.000 |
| coherence | reasoning_quality | 4 | 1.000 |
| coherence | resolution | 2 | 0.500 |
| coherence | rule_completeness | 2 | 1.000 |
| coherence | sample_game_obeys_rules | 2 | 0.800 |
| coherence | scientific_accuracy | 2 | 0.900 |
| coherence | section_separation | 2 | 1.000 |
| coherence | self_consistency | 2 | 0.900 |
| coherence | self_reference_accuracy | 2 | 1.000 |
| coherence | steps_ingredients_consistency | 2 | 1.000 |
| coherence | tldr_faithfulness | 2 | 1.000 |
| coherence | tone_appropriate | 2 | 1.000 |
| coherence | verdict_follows_from_arguments | 2 | 0.800 |
| writing | adherence_to_prompt | 10 | 1.000 |
| writing | age_appropriateness | 2 | 1.000 |
| writing | appropriateness | 2 | 1.000 |
| writing | atmosphere | 2 | 1.000 |
| writing | balanced_critique | 2 | 1.000 |
| writing | bookend_constraint_met | 2 | 0.600 |
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
| writing | length | 8 | 0.900 |
| writing | length_adherence | 2 | 1.000 |
| writing | lightness_humor | 2 | 1.000 |
| writing | limerick_form | 2 | 1.000 |
| writing | meaning_preserved | 2 | 0.800 |
| writing | narrative_arc | 2 | 0.500 |
| writing | narrative_completeness | 2 | 1.000 |
| writing | narrative_quality | 2 | 1.000 |
| writing | naturalistic_dialogue | 2 | 1.000 |
| writing | on_topic | 2 | 1.000 |
| writing | persuasiveness | 2 | 1.000 |
| writing | professional_tone | 2 | 1.000 |
| writing | prose_quality | 8 | 0.900 |
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
| writing | under_280_chars | 2 | 0.900 |
| writing | variety | 2 | 1.000 |
| writing | vividness_improved | 2 | 0.800 |
| writing | warmth_humor_balance | 2 | 0.900 |

## Failures (4)

| capability | prompt | mode | score | notes | finish/err |
|---|---|---|---|---|---|
| coherence | coh-03 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (finish=length) | length |
| coding | cod-15 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 5, in <module>\n  | stop |
| instruction_following | if-11 | off | 0.000 | 38 words (want 39..41) | stop |
| writing | wr-21 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (finish=length) | length |
