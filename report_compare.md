# Local model eval report

- Model tag(s): gemma4-26b-a4b-q8km, gemma4-31b-q5kxl, qwen3.6-35b-a3b-q8kxl
- Source file(s): gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl, gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl, gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl, gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl, gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl, gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl, qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl
- Capabilities: coding, coding_hard, coding_quality, coding_quality_hard, coherence, instruction_following, instruction_following_hard, long_context, long_context_hard, reasoning, reasoning_hard, writing, writing_hard
- Thinking modes: off, on
- Total calls: 1294  (graded 1294, pending rubric 0)

## Run configuration

### gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl

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

### gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl

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
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=262144
- Run started: 2026-05-12T03-22-57
- Run duration (min): 157.9
- Total calls: 164
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning_hard', 'coding_hard', 'instruction_following_hard', 'long_context_hard', 'writing_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 164
- calls_per_sec: 0.017
- results: pass=126, fail=10, pending_rubric=28, error=0

### gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl

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
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=262144
- Run started: 2026-05-12T06-18-31
- Run duration (min): 22.7
- Total calls: 28
- n_ctx_used_by_runner: 262144
- capabilities: ['coding_quality']
- thinking_modes: ['on', 'off']
- calls_planned: 28
- calls_per_sec: 0.021
- results: pass=28, fail=0, pending_rubric=0, error=0

### gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl

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
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=262144
- Run started: 2026-05-12T12-44-12
- Run duration (min): 36.3
- Total calls: 30
- n_ctx_used_by_runner: 262144
- capabilities: ['coding_quality_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 30
- calls_per_sec: 0.014
- results: pass=28, fail=2, pending_rubric=0, error=0

### gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl

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

### gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl

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
- Run started: 2026-05-12T15-12-37
- Run duration (min): 53.7
- Total calls: 58
- n_ctx_used_by_runner: 262144
- capabilities: ['coding_quality', 'coding_quality_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 58
- calls_per_sec: 0.018
- results: pass=56, fail=2, pending_rubric=0, error=0

### qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl

- Model tag: qwen3.6-35b-a3b-q8kxl
- Served model id: qwen3.6-35b-a3b
- Model file: Qwen3.6-35B-A3B-UD-Q8_K_XL.gguf
- Parameters: 34,660,610,688 (~34.7 B)
- File size: 38,440,192,512 bytes (~35.8 GiB)
- Context (n_ctx): 262144
- Trained context: 262144
- Embedding dim: 2048
- Vocab size: 248320
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/Qwen3.6-35B-A3B-UD-Q8_K_XL.gguf -ngl 99 -c 524288 --parallel 2 -t 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on --jinja --host 0.0.0.0 --port 8080 --metrics --temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.0 -a qwen3.6-35b-a3b`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=262144
- Run started: 2026-05-12T16-41-05
- Run duration (min): 244.6
- Total calls: 418
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning', 'coding', 'coding_quality', 'instruction_following', 'long_context', 'writing', 'reasoning_hard', 'coding_hard', 'instruction_following_hard', 'long_context_hard', 'writing_hard', 'coding_quality_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 418
- calls_per_sec: 0.028
- results: pass=320, fail=28, pending_rubric=70, error=0

## Overall

| scope | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| all | 1294 | 95.1% | 0.958 | 19043 | 402 |

## By run (source file)

| source file | tag | n_ctx | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|---|
| gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | gemma4-26b-a4b-q8km | 262144 | 236 | 98.3% | 0.976 | 21540 | 352 |
| gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | gemma4-26b-a4b-q8km | 262144 | 164 | 90.9% | 0.935 | 17588 | 466 |
| gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl | gemma4-26b-a4b-q8km | 262144 | 28 | 100.0% | 0.986 | 26746 | 938 |
| gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl | gemma4-26b-a4b-q8km | 262144 | 30 | 93.3% | 0.954 | 26222 | 916 |
| gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | gemma4-31b-q5kxl | 262144 | 360 | 97.5% | 0.978 | 18282 | 259 |
| gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | gemma4-31b-q5kxl | 262144 | 58 | 96.6% | 0.952 | 38229 | 629 |
| qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | qwen3.6-35b-a3b-q8kxl | 262144 | 418 | 92.6% | 0.940 | 14884 | 509 |

### Capability × thinking mode × run

| capability | thinking | run | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|---|
| coding | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 95.2% | 0.952 | 3676 | 58 |
| coding | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 3836 | 58 |
| coding | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 85.7% | 0.857 | 1766 | 64 |
| coding | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 49495 | 905 |
| coding | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 26539 | 445 |
| coding | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 27537 | 1110 |
| coding_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 100.0% | 1.000 | 3507 | 116 |
| coding_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 7120 | 114 |
| coding_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 100.0% | 1.000 | 4141 | 161 |
| coding_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 100.0% | 1.000 | 40828 | 1426 |
| coding_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 43481 | 719 |
| coding_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 100.0% | 1.000 | 59412 | 2374 |
| coding_quality | off | gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl | 14 | 100.0% | 0.985 | 7753 | 265 |
| coding_quality | off | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 14 | 100.0% | 0.968 | 13084 | 216 |
| coding_quality | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 92.9% | 0.958 | 5697 | 226 |
| coding_quality | on | gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl | 14 | 100.0% | 0.988 | 75538 | 2586 |
| coding_quality | on | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 14 | 100.0% | 0.975 | 61655 | 1003 |
| coding_quality | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 100.0% | 0.979 | 91542 | 3626 |
| coding_quality_hard | off | gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl | 15 | 86.7% | 0.939 | 12947 | 447 |
| coding_quality_hard | off | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 15 | 93.3% | 0.952 | 25774 | 425 |
| coding_quality_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 15 | 73.3% | 0.899 | 11504 | 461 |
| coding_quality_hard | on | gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl | 15 | 100.0% | 0.969 | 122152 | 4105 |
| coding_quality_hard | on | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 15 | 93.3% | 0.915 | 119464 | 1866 |
| coding_quality_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 15 | 86.7% | 0.877 | 150599 | 5758 |
| coherence | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 20 | 100.0% | 0.990 | 27710 | 498 |
| coherence | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 20 | 95.0% | 0.935 | 74619 | 1321 |
| instruction_following | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 95.2% | 0.952 | 1444 | 18 |
| instruction_following | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 95.2% | 0.952 | 1388 | 18 |
| instruction_following | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 81.0% | 0.865 | 928 | 20 |
| instruction_following | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 15352 | 266 |
| instruction_following | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 14073 | 233 |
| instruction_following | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 15410 | 616 |
| instruction_following_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 16 | 75.0% | 0.917 | 1225 | 32 |
| instruction_following_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 16 | 68.8% | 0.875 | 2176 | 30 |
| instruction_following_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 16 | 50.0% | 0.755 | 1581 | 40 |
| instruction_following_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 16 | 75.0% | 0.844 | 98057 | 3334 |
| instruction_following_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 16 | 100.0% | 1.000 | 85797 | 1382 |
| instruction_following_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 16 | 87.5% | 0.896 | 49503 | 1990 |
| long_context | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 14 | 100.0% | 1.000 | 14957 | 134 |
| long_context | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 92.9% | 0.929 | 13864 | 73 |
| long_context | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 92.9% | 0.929 | 3060 | 107 |
| long_context | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 14 | 100.0% | 1.000 | 66353 | 685 |
| long_context | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 100.0% | 1.000 | 33844 | 326 |
| long_context | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 100.0% | 1.000 | 22408 | 394 |
| long_context_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 12 | 100.0% | 1.000 | 17985 | 238 |
| long_context_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 12 | 91.7% | 0.917 | 26350 | 170 |
| long_context_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 12 | 83.3% | 0.833 | 8417 | 292 |
| long_context_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 12 | 91.7% | 0.917 | 118082 | 3230 |
| long_context_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 12 | 100.0% | 1.000 | 143073 | 1673 |
| long_context_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 12 | 100.0% | 1.000 | 60532 | 1552 |
| reasoning | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 14389 | 258 |
| reasoning | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 10138 | 171 |
| reasoning | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 8709 | 338 |
| reasoning | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 35322 | 638 |
| reasoning | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 31228 | 526 |
| reasoning | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 24618 | 1017 |
| reasoning_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 100.0% | 1.000 | 11478 | 404 |
| reasoning_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 20416 | 342 |
| reasoning_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 100.0% | 1.000 | 13653 | 539 |
| reasoning_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 95.0% | 0.950 | 32174 | 1134 |
| reasoning_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 59994 | 985 |
| reasoning_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 95.0% | 0.950 | 45247 | 1822 |
| writing | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 0.964 | 6376 | 114 |
| writing | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 0.967 | 6743 | 111 |
| writing | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 95.2% | 0.926 | 3388 | 118 |
| writing | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 95.2% | 0.929 | 68283 | 1246 |
| writing | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 0.967 | 41810 | 701 |
| writing | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 0.986 | 42296 | 1706 |
| writing_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 14 | 100.0% | 0.954 | 4787 | 156 |
| writing_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 100.0% | 0.964 | 7078 | 116 |
| writing_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 85.7% | 0.832 | 3877 | 134 |
| writing_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 14 | 64.3% | 0.696 | 224944 | 7311 |
| writing_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 92.9% | 0.918 | 163928 | 2536 |
| writing_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 100.0% | 0.925 | 94983 | 3744 |

## By thinking mode

| thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| off | 647 | 93.4% | 0.950 | 6374 | 142 |
| on | 647 | 96.9% | 0.966 | 49361 | 1198 |

## By capability

| capability | n | pass rate | mean score | median latency (ms) | median out-tokens | pending |
|---|---|---|---|---|---|---|
| coding | 126 | 96.8% | 0.968 | 9595 | 257 |  |
| coding_hard | 120 | 100.0% | 1.000 | 15450 | 356 |  |
| coding_quality | 84 | 98.8% | 0.976 | 27426 | 617 |  |
| coding_quality_hard | 90 | 88.9% | 0.925 | 47734 | 1018 |  |
| coherence | 40 | 97.5% | 0.963 | 47676 | 866 |  |
| instruction_following | 126 | 95.2% | 0.962 | 5376 | 115 |  |
| instruction_following_hard | 96 | 76.0% | 0.881 | 7163 | 159 |  |
| long_context | 84 | 97.6% | 0.976 | 19055 | 220 |  |
| long_context_hard | 72 | 94.4% | 0.944 | 38499 | 464 |  |
| reasoning | 126 | 100.0% | 1.000 | 18709 | 410 |  |
| reasoning_hard | 120 | 98.3% | 0.983 | 22638 | 684 |  |
| writing | 126 | 98.4% | 0.956 | 18293 | 313 |  |
| writing_hard | 84 | 90.5% | 0.882 | 24864 | 656 |  |

## Capability × thinking mode

| capability | thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|
| coding | off | 63 | 93.7% | 0.937 | 3402 | 58 |
| coding | on | 63 | 100.0% | 1.000 | 29977 | 735 |
| coding_hard | off | 60 | 100.0% | 1.000 | 4839 | 121 |
| coding_hard | on | 60 | 100.0% | 1.000 | 43913 | 1310 |
| coding_quality | off | 42 | 97.6% | 0.970 | 9006 | 229 |
| coding_quality | on | 42 | 100.0% | 0.981 | 76134 | 2478 |
| coding_quality_hard | off | 45 | 84.4% | 0.930 | 15974 | 447 |
| coding_quality_hard | on | 45 | 93.3% | 0.920 | 123902 | 3784 |
| coherence | off | 20 | 100.0% | 0.990 | 27710 | 498 |
| coherence | on | 20 | 95.0% | 0.935 | 74619 | 1321 |
| instruction_following | off | 63 | 90.5% | 0.923 | 1227 | 19 |
| instruction_following | on | 63 | 100.0% | 1.000 | 14879 | 337 |
| instruction_following_hard | off | 48 | 64.6% | 0.849 | 1671 | 34 |
| instruction_following_hard | on | 48 | 87.5% | 0.913 | 62825 | 1962 |
| long_context | off | 42 | 95.2% | 0.952 | 12456 | 110 |
| long_context | on | 42 | 100.0% | 1.000 | 34467 | 394 |
| long_context_hard | off | 36 | 91.7% | 0.917 | 18856 | 238 |
| long_context_hard | on | 36 | 97.2% | 0.972 | 84911 | 2143 |
| reasoning | off | 63 | 100.0% | 1.000 | 10387 | 242 |
| reasoning | on | 63 | 100.0% | 1.000 | 30737 | 700 |
| reasoning_hard | off | 60 | 100.0% | 1.000 | 14146 | 400 |
| reasoning_hard | on | 60 | 96.7% | 0.967 | 44178 | 1196 |
| writing | off | 63 | 98.4% | 0.952 | 5537 | 114 |
| writing | on | 63 | 98.4% | 0.960 | 47098 | 1246 |
| writing_hard | off | 42 | 95.2% | 0.917 | 4661 | 132 |
| writing_hard | on | 42 | 85.7% | 0.846 | 108770 | 3744 |

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
| writing | adherence_to_prompt | 30 | 0.980 |
| writing | age_appropriateness | 6 | 1.000 |
| writing | appropriateness | 6 | 0.967 |
| writing | atmosphere | 6 | 1.000 |
| writing | balanced_critique | 6 | 1.000 |
| writing | bookend_constraint_met | 6 | 0.867 |
| writing | call_to_action | 6 | 1.000 |
| writing | characterization | 6 | 1.000 |
| writing | chorus_identical | 6 | 1.000 |
| writing | clear_value_prop | 6 | 1.000 |
| writing | completeness | 6 | 1.000 |
| writing | concision | 18 | 0.789 |
| writing | description_clarity | 6 | 0.967 |
| writing | emotional_resonance | 6 | 1.000 |
| writing | emotional_theme | 6 | 1.000 |
| writing | encouragement | 6 | 1.000 |
| writing | evokes_dawn | 6 | 1.000 |
| writing | fluency | 60 | 0.983 |
| writing | format | 6 | 1.000 |
| writing | four_lines | 6 | 1.000 |
| writing | hook | 6 | 1.000 |
| writing | humor | 6 | 0.600 |
| writing | imagery | 18 | 0.922 |
| writing | length | 24 | 0.917 |
| writing | length_adherence | 6 | 1.000 |
| writing | lightness_humor | 6 | 1.000 |
| writing | limerick_form | 6 | 0.900 |
| writing | meaning_preserved | 6 | 0.833 |
| writing | narrative_arc | 6 | 0.833 |
| writing | narrative_completeness | 6 | 1.000 |
| writing | narrative_quality | 6 | 1.000 |
| writing | naturalistic_dialogue | 6 | 1.000 |
| writing | on_topic | 6 | 1.000 |
| writing | persuasiveness | 6 | 1.000 |
| writing | professional_tone | 6 | 1.000 |
| writing | prose_quality | 24 | 0.967 |
| writing | realism | 6 | 1.000 |
| writing | restraint | 6 | 0.800 |
| writing | rhyme_and_meter | 6 | 0.700 |
| writing | rhyme_scheme_correct | 6 | 1.000 |
| writing | sensory_detail | 6 | 1.000 |
| writing | sincerity | 6 | 1.000 |
| writing | six_lines | 6 | 1.000 |
| writing | soothing_tone | 6 | 1.000 |
| writing | specific_detail | 6 | 1.000 |
| writing | specificity | 6 | 0.900 |
| writing | structure_correct | 6 | 1.000 |
| writing | tagline_punchiness | 6 | 1.000 |
| writing | three_line_form | 6 | 1.000 |
| writing | three_sentences | 6 | 0.967 |
| writing | tonal_continuity | 6 | 0.967 |
| writing | tone | 36 | 1.000 |
| writing | under_280_chars | 6 | 0.833 |
| writing | variety | 6 | 1.000 |
| writing | vividness_improved | 6 | 0.833 |
| writing | warmth_humor_balance | 6 | 0.967 |
| writing_hard | about_fifty_words | 6 | 0.667 |
| writing_hard | acrostic_spells_WINTER | 6 | 0.867 |
| writing_hard | actually_funny | 6 | 0.500 |
| writing_hard | age_appropriate | 6 | 1.000 |
| writing_hard | all_three_mention_locked_drawer | 6 | 0.900 |
| writing_hard | bridge_is_a_genuine_departure | 6 | 1.000 |
| writing_hard | chorus_identical_all_three_times | 6 | 1.000 |
| writing_hard | coherent_poem | 6 | 1.000 |
| writing_hard | coherent_poem_not_filler | 6 | 0.800 |
| writing_hard | comic_version_genuinely_comic | 6 | 1.000 |
| writing_hard | craft | 12 | 1.000 |
| writing_hard | creepiness | 6 | 0.633 |
| writing_hard | dialogue_only_no_narration | 6 | 1.000 |
| writing_hard | each_line_iambic_pentameter | 6 | 0.867 |
| writing_hard | each_opening_clearly_its_genre | 6 | 1.000 |
| writing_hard | earlier_text_supports_twist | 6 | 0.567 |
| writing_hard | emotional_coherence | 6 | 0.900 |
| writing_hard | emotional_resonance | 6 | 0.900 |
| writing_hard | events_identical_across_versions | 6 | 0.933 |
| writing_hard | exactly_100_words | 6 | 0.767 |
| writing_hard | exactly_four_lines | 6 | 1.000 |
| writing_hard | exactly_six_lines | 6 | 1.000 |
| writing_hard | final_word_recontextualizes | 6 | 0.567 |
| writing_hard | fluency | 12 | 0.717 |
| writing_hard | fourteen_lines | 6 | 1.000 |
| writing_hard | has_narrative_arc | 6 | 0.833 |
| writing_hard | imagery | 12 | 0.833 |
| writing_hard | imagery_and_theme | 6 | 1.000 |
| writing_hard | is_one_grammatical_sentence | 6 | 0.867 |
| writing_hard | limerick_form_correct | 6 | 0.700 |
| writing_hard | line_word_counts_1_through_8 | 6 | 0.733 |
| writing_hard | love_conveyed_through_subtext | 6 | 1.000 |
| writing_hard | meter_roughly_iambic_pentameter | 6 | 0.933 |
| writing_hard | narrative_progresses | 6 | 1.000 |
| writing_hard | narrative_quality | 6 | 1.000 |
| writing_hard | no_jargon_no_lesson_tone | 6 | 1.000 |
| writing_hard | no_love_words_used | 6 | 1.000 |
| writing_hard | no_modern_slips | 6 | 0.967 |
| writing_hard | persuasive_and_on_topic | 6 | 0.800 |
| writing_hard | present_tense_throughout | 6 | 0.867 |
| writing_hard | prose_quality | 18 | 0.856 |
| writing_hard | pun_on_pitch_works_both_ways | 6 | 0.633 |
| writing_hard | reads_naturally | 6 | 0.867 |
| writing_hard | realization_lands_emotionally | 6 | 0.867 |
| writing_hard | recursion_idea_conveyed | 6 | 1.000 |
| writing_hard | register_matched_throughout | 6 | 0.967 |
| writing_hard | rhyme_scheme_ABAB_CDCD_EFEF_GG | 6 | 0.933 |
| writing_hard | second_person_throughout | 6 | 0.867 |
| writing_hard | structure_VCVCBC | 6 | 1.000 |
| writing_hard | three_distinct_voices | 6 | 1.000 |
| writing_hard | tragic_version_genuinely_tragic | 6 | 1.000 |

## Failures (63)

| capability | prompt | mode | score | notes | finish/err |
|---|---|---|---|---|---|
| coherence | coh-03 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (finish=length) | length |
| coding | cod-15 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 5, in <module>\n  | stop |
| instruction_following | if-11 | off | 0.000 | 38 words (want 39..41) | stop |
| writing | wr-21 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (finish=length) | length |
| reasoning_hard | rea-h-11 | on | 0.000 | got 5 want 7 (tol 0) | length |
| instruction_following_hard | if-h-01 | on | 0.667 | X:0 non-empty lines (want 7..7) \| ok:pattern absent (good) \| ok:forbidden chars seen: none | length |
| instruction_following_hard | if-h-02 | on | 0.333 | X:0 words (want 50..50) \| ok:forbidden chars seen: none \| X:does not end with 'done' | length |
| instruction_following_hard | if-h-02 | off | 0.667 | X:47 words (want 50..50) \| ok:forbidden chars seen: none \| ok:ok | stop |
| instruction_following_hard | if-h-08 | on | 0.000 | X:0 words (want 100..100) \| X:does not start with 'Begin'; does not end with 'End' \| X:hit | length |
| instruction_following_hard | if-h-10 | off | 0.750 | ok:4 paragraphs (want 4..4) \| ok:8 sentences (want 8..8) \| X:32 words (want 60..80) \| ok:p | stop |
| instruction_following_hard | if-h-13 | off | 0.750 | ok:3 sentences (want 3..3) \| ok:1x 'however' (want 1..1) \| ok:pattern absent (good) \| X:22 | stop |
| instruction_following_hard | if-h-16 | on | 0.500 | X:0 words (want 40..50) \| ok:forbidden chars seen: none | length |
| instruction_following_hard | if-h-16 | off | 0.500 | ok:47 words (want 40..50) \| X:forbidden chars seen: {'e': 3} | stop |
| long_context_hard | lc-h-05 | on | 0.000 | no number in response | length |
| writing_hard | wr-h-02 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted 8192-token budget (2700+ words reasoning, finish | length |
| writing_hard | wr-h-04 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (3500+ words reasoning, finish=leng | length |
| writing_hard | wr-h-09 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (4400+ words reasoning, finish=leng | length |
| writing_hard | wr-h-12 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (4600+ words reasoning, finish=leng | length |
| writing_hard | wr-h-13 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted token budget (3400+ words reasoning, finish=leng | length |
| coding_quality_hard | cq-h-04 | off | 0.606 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 79, in <module> | stop |
| coding_quality_hard | cq-h-14 | off | 0.893 | ok:tests pass \| ok:tests pass \| X:quality complexity=0.73, nesting=0.50, length=0.20, ruff | stop |
| instruction_following | if-09 | off | 0.000 | match=None | stop |
| long_context | lc-14 | off | 0.000 | got 56 want 55 (tol 0) | stop |
| instruction_following_hard | if-h-02 | off | 0.333 | X:49 words (want 50..50) \| X:forbidden chars seen: {'s': 1} \| ok:ok | stop |
| instruction_following_hard | if-h-08 | off | 0.667 | X:101 words (want 100..100) \| ok:ok \| ok:hit=['one hundred words'] miss=[] forbidden_seen= | stop |
| instruction_following_hard | if-h-10 | off | 0.750 | ok:4 paragraphs (want 4..4) \| ok:8 sentences (want 8..8) \| X:29 words (want 60..80) \| ok:p | stop |
| instruction_following_hard | if-h-13 | off | 0.750 | ok:3 sentences (want 3..3) \| ok:1x 'however' (want 1..1) \| ok:pattern absent (good) \| X:22 | stop |
| instruction_following_hard | if-h-16 | off | 0.500 | ok:47 words (want 40..50) \| X:forbidden chars seen: {'e': 2} | stop |
| long_context_hard | lc-h-09 | off | 0.000 | got 88 want 90 (tol 0) | stop |
| writing_hard | wr-h-09 | on | 0.200 | rubric: EMPTY OUTPUT - thinking exhausted 8192-token budget (3900+ words of reasoning), fi | length |
| coding_quality_hard | cq-h-12 | on | 0.279 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 48, in <module> | stop |
| coding_quality_hard | cq-h-14 | off | 0.881 | ok:tests pass \| ok:tests pass \| X:quality complexity=0.73, nesting=0.25, length=0.18, ruff | stop |
| coding | cod-05 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 8, in <module>\n  | stop |
| coding | cod-08 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 22, in <module>\n | stop |
| coding | cod-14 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 51, in <module>\n | stop |
| coding_quality | cq-14 | off | 0.896 | ok:tests pass \| ok:tests pass \| X:quality complexity=0.50, length=0.00, ruff=0.00 | stop |
| instruction_following | if-03 | off | 0.667 | ok:forbidden chars seen: none \| X:4 words (want 6..None) \| ok:match='.' | stop |
| instruction_following | if-09 | off | 0.000 | match=None | stop |
| instruction_following | if-11 | off | 0.000 | 44 words (want 39..41) | stop |
| instruction_following | if-18 | off | 0.500 | ok:3 non-empty lines (want 3..3) \| X:missing_patterns=['(?m)^\\s*(\\S+\\s+){8}\\S+[.!?\\"\ | stop |
| long_context | lc-14 | off | 0.000 | got 54 want 55 (tol 0) | stop |
| writing | wr-08 | off | 0.550 | rubric: FAIL — the AABBA rhyme is broken (glitch / skill don't rhyme); no real punchline | stop |
| reasoning_hard | rea-h-12 | on | 0.000 | no number in response | length |
| instruction_following_hard | if-h-01 | off | 0.667 | ok:7 non-empty lines (want 7..7) \| ok:pattern absent (good) \| X:forbidden chars seen: {'a' | stop |
| instruction_following_hard | if-h-02 | on | 0.333 | X:0 words (want 50..50) \| ok:forbidden chars seen: none \| X:does not end with 'done' | length |
| instruction_following_hard | if-h-02 | off | 0.333 | X:45 words (want 50..50) \| X:forbidden chars seen: {'s': 10} \| ok:ok | stop |
| instruction_following_hard | if-h-05 | off | 0.750 | ok:6 non-empty lines (want 6..6) \| ok:hit=['silver'] miss=[] forbidden_seen=[] \| X:pattern | stop |
| instruction_following_hard | if-h-08 | on | 0.000 | X:0 words (want 100..100) \| X:does not start with 'Begin'; does not end with 'End' \| X:hit | length |
| instruction_following_hard | if-h-08 | off | 0.667 | X:126 words (want 100..100) \| ok:ok \| ok:hit=['one hundred words'] miss=[] forbidden_seen= | stop |
| instruction_following_hard | if-h-09 | off | 0.667 | X:22 words (want 15..20) \| ok:1 non-empty lines (want 1..1) \| ok:match='the sun rises slow | stop |
| instruction_following_hard | if-h-12 | off | 0.500 | ok:5 non-empty lines (want 5..5) \| X:pattern matched: 'It chased a mouse,' | stop |
| instruction_following_hard | if-h-13 | off | 0.500 | ok:3 sentences (want 3..3) \| ok:1x 'however' (want 1..1) \| X:pattern matched: ',' \| X:16 w | stop |
| instruction_following_hard | if-h-16 | off | 0.000 | X:39 words (want 40..50) \| X:forbidden chars seen: {'e': 11} | stop |
| long_context_hard | lc-h-09 | off | 0.000 | got 84 want 90 (tol 0) | stop |
| long_context_hard | lc-h-10 | off | 0.000 | got 6 want 7 (tol 0) | stop |
| writing_hard | wr-h-04 | off | 0.500 | rubric: FAIL — lines 5/6/7/8 have 4/4/3/4 words, not 5/6/7/8; the prompt's entire point is | stop |
| writing_hard | wr-h-12 | off | 0.400 | rubric: FAIL — line 5 ('control of the pitch') doesn't rhyme with lines 1-2 (shrill/thrill | stop |
| coding_quality_hard | cq-h-05 | off | 0.562 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 85, in <module> | stop |
| coding_quality_hard | cq-h-08 | off | 0.636 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 81, in <module> | stop |
| coding_quality_hard | cq-h-11 | off | 0.890 | ok:tests pass \| ok:tests pass \| X:quality complexity=0.60, nesting=0.75, length=0.00, ruff | stop |
| coding_quality_hard | cq-h-13 | on | 0.222 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 3, in <module>\ | length |
| coding_quality_hard | cq-h-14 | on | 0.222 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 3, in <module>\ | length |
| coding_quality_hard | cq-h-15 | off | 0.898 | ok:tests pass \| ok:tests pass \| X:quality complexity=0.56, length=0.00, ruff=0.00 | stop |
