# Local model eval report

- Model tag(s): gemma4-26b-a4b-q8km, gemma4-31b-q5kxl, qwen3.5-122b-a10b-q3kxl, qwen3.6-35b-a3b-q8kxl
- Source file(s): _aborted_19-48-54_concurrency1.jsonl, _aborted_22-10-29_hardrun_4calls.jsonl, gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl, gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl, gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl, gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl, gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl, gemma4-26b-a4b-q8km__2026-05-12T03-21-56__SMOKE.jsonl, gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl, gemma4-26b-a4b-q8km__2026-05-12T06-13-52__SMOKE.jsonl, gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl, gemma4-26b-a4b-q8km__2026-05-12T11-49-54__SMOKE.jsonl, gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl, gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl, gemma4-31b-q5kxl__2026-05-11T22-14-41__SMOKE.jsonl, gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl, gemma4-31b-q5kxl__2026-05-12T15-07-51__SMOKE.jsonl, gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl, gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl, qwen3.5-122b-a10b-q3kxl__2026-05-13T12-20-57__SMOKE.jsonl, qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl, qwen3.5-122b-a10b-q3kxl__2026-05-13T22-54-51__SMOKE.jsonl, qwen3.5-122b-a10b-q3kxl__2026-05-13T22-59-11.jsonl, qwen3.5-122b-a10b-q3kxl__2026-05-13T23-02-43.jsonl, qwen3.6-35b-a3b-q8kxl__2026-05-12T16-39-39__SMOKE.jsonl, qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl, qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl
- Capabilities: coding, coding_hard, coding_quality, coding_quality_hard, coherence, coherence_hard, instruction_following, instruction_following_hard, long_context, long_context_hard, reasoning, reasoning_hard, tool_calling, tool_calling_hard, writing, writing_hard
- Thinking modes: off, on
- Total calls: 2251  (graded 2232, pending rubric 19)

## Run configuration

### _aborted_22-10-29_hardrun_4calls.jsonl

- Model tag: gemma4-26b-a4b-q8km
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
- Run started: 2026-05-11T22-10-29
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning_hard', 'coding_hard', 'instruction_following_hard', 'long_context_hard', 'writing_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 164

### gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl

- Model tag: gemma4-26b-a4b-q8km
- Served model id: gemma-4-26b-a4b
- Model file: gemma-4-26B-A4B-it-UD-Q8_K_XL.gguf
- Quantization: Q8_K_XL (Unsloth dynamic; ~Q8_0 weights)
- Architecture: Gemma 4 26B-A4B (sparse MoE, ~4B active params)
- Parameters: 25,233,142,046 (~25.2 B)
- File size: 27,620,407,416 bytes (~25.7 GiB)
- Context (n_ctx): 8192
- Trained context: 262144
- Embedding dim: 2816
- Vocab size: 262144
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/gemma-4-26B-A4B-it-UD-Q8_K_XL.gguf -ngl 99 -c 8192 -t 8 -sm layer -ts 1/1 --jinja --host 0.0.0.0 --port 8080 --metrics -a gemma-4-26b-a4b`
- Endpoint: http://localhost:8080/v1/chat/completions
- Hardware: 2x Intel Arc Battlemage G31 [PCI 8086:e223], 230 W cap each; AMD host CPU; model split across both GPUs (-sm layer -ts 1/1, all layers offloaded)
- Measured GPU power (generation): ~267 W (both GPUs, card-level)
- Sampling: temperature=1.0, top_p=0.95, top_k=64
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true = thinking on, false = off); reasoning returned in reasoning_content field
- Server slots (--parallel): 4
- Context per slot: 8192
- Client concurrency: 1 (run_eval.py issues requests strictly sequentially; at most one request in flight, so only 1 of the 4 server slots was ever active — latencies are uncontended single-request, not throughput-under-load)
- max_tokens policy: per-prompt cap (default 3072 thinking-on / 1536 thinking-off, long_context up to 4096), clamped to fit n_ctx
- Run started: 2026-05-11T17:04:05
- Run duration (min): 75.9
- Total calls: 236

### gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl

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
- Run started: 2026-05-11T19-13-05
- n_ctx_used_by_runner: 262144
- capabilities: ['coherence', 'reasoning', 'coding', 'instruction_following', 'long_context', 'writing']
- thinking_modes: ['off', 'on']
- calls_planned: 24

### gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl

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
- Run started: 2026-05-11T19-38-57
- Run duration (min): 8.9
- Total calls: 24
- n_ctx_used_by_runner: 262144
- capabilities: ['coherence', 'reasoning', 'coding', 'instruction_following', 'long_context', 'writing']
- thinking_modes: ['on', 'off']
- calls_planned: 24
- calls_per_sec: 0.045
- results: pass=16, fail=0, pending_rubric=8, error=0

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

### gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl

- Model tag: gemma4-26b-a4b-q8km
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
- Run started: 2026-05-11T22-05-22
- Run duration (min): 2.0
- Total calls: 12
- n_ctx_used_by_runner: 262144
- capabilities: ['coherence_hard', 'reasoning_hard', 'coding_hard', 'instruction_following_hard', 'long_context_hard', 'writing_hard']
- thinking_modes: ['off']
- calls_planned: 12
- calls_per_sec: 0.099
- results: pass=8, fail=0, pending_rubric=4, error=0

### gemma4-26b-a4b-q8km__2026-05-12T03-21-56__SMOKE.jsonl

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
- Run started: 2026-05-12T03-21-56
- Run duration (min): 0.8
- Total calls: 4
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.086
- results: pass=4, fail=0, pending_rubric=0, error=0

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

### gemma4-26b-a4b-q8km__2026-05-12T06-13-52__SMOKE.jsonl

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
- Run started: 2026-05-12T06-13-52
- Run duration (min): 3.7
- Total calls: 4
- n_ctx_used_by_runner: 262144
- capabilities: ['coding_quality']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.018
- results: pass=4, fail=0, pending_rubric=0, error=0

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

### gemma4-26b-a4b-q8km__2026-05-12T11-49-54__SMOKE.jsonl

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
- Run started: 2026-05-12T11-49-54
- Run duration (min): 4.1
- Total calls: 4
- n_ctx_used_by_runner: 262144
- capabilities: ['coding_quality_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.016
- results: pass=4, fail=0, pending_rubric=0, error=0

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

### gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl

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
- Run started: 2026-05-14T00-42-42
- Run duration (min): 2.5
- Total calls: 52
- n_ctx_used_by_runner: 262144
- capabilities: ['tool_calling', 'tool_calling_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 52
- calls_per_sec: 0.343
- results: pass=52, fail=0, pending_rubric=0, error=0

### gemma4-31b-q5kxl__2026-05-11T22-14-41__SMOKE.jsonl

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
- Run started: 2026-05-11T22-14-41
- Run duration (min): 1.6
- Total calls: 4
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.041
- results: pass=4, fail=0, pending_rubric=0, error=0

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

### gemma4-31b-q5kxl__2026-05-12T15-07-51__SMOKE.jsonl

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
- Run started: 2026-05-12T15-07-51
- Run duration (min): 3.9
- Total calls: 4
- n_ctx_used_by_runner: 262144
- capabilities: ['coding_quality']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.017
- results: pass=4, fail=0, pending_rubric=0, error=0

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

### gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl

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
- Run started: 2026-05-14T00-16-43
- Run duration (min): 4.2
- Total calls: 52
- n_ctx_used_by_runner: 262144
- capabilities: ['tool_calling', 'tool_calling_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 52
- calls_per_sec: 0.205
- results: pass=51, fail=1, pending_rubric=0, error=0

### qwen3.5-122b-a10b-q3kxl__2026-05-13T12-20-57__SMOKE.jsonl

- Model tag: qwen3.5-122b-a10b-q3kxl
- Served model id: qwen3.5-122b-a10b-q3
- Model file: Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf
- Parameters: 122,111,526,912 (~122.1 B)
- File size: 56,959,537,152 bytes (~53.0 GiB)
- Context (n_ctx): 153600
- Trained context: 262144
- Embedding dim: 3072
- Vocab size: 248320
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/UD-Q3_K_XL/Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf -ngl 99 -c 153600 --parallel 1 --threads 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on -b 4096 -ub 1024 --jinja --host 0.0.0.0 --port 8080 --metrics --temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.0 -a qwen3.5-122b-a10b-q3`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=153600
- Run started: 2026-05-13T12-20-57
- Run duration (min): 2.1
- Total calls: 4
- n_ctx_used_by_runner: 153600
- capabilities: ['reasoning']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.032
- results: pass=4, fail=0, pending_rubric=0, error=0

### qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl

- Model tag: qwen3.5-122b-a10b-q3kxl
- Served model id: qwen3.5-122b-a10b-q3
- Model file: Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf
- Parameters: 122,111,526,912 (~122.1 B)
- File size: 56,959,537,152 bytes (~53.0 GiB)
- Context (n_ctx): 153600
- Trained context: 262144
- Embedding dim: 3072
- Vocab size: 248320
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/UD-Q3_K_XL/Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf -ngl 99 -c 153600 --parallel 1 --threads 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on -b 4096 -ub 1024 --jinja --host 0.0.0.0 --port 8080 --metrics --temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.0 -a qwen3.5-122b-a10b-q3`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=153600
- Run started: 2026-05-13T12-23-32
- Run duration (min): 552.2
- Total calls: 418
- n_ctx_used_by_runner: 153600
- capabilities: ['reasoning', 'coding', 'coding_quality', 'instruction_following', 'long_context', 'writing', 'reasoning_hard', 'coding_hard', 'instruction_following_hard', 'long_context_hard', 'writing_hard', 'coding_quality_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 418
- calls_per_sec: 0.013
- results: pass=322, fail=26, pending_rubric=70, error=0

### qwen3.5-122b-a10b-q3kxl__2026-05-13T22-54-51__SMOKE.jsonl

- Model tag: qwen3.5-122b-a10b-q3kxl
- Served model id: qwen3.5-122b-a10b-q3
- Model file: Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf
- Parameters: 122,111,526,912 (~122.1 B)
- File size: 56,959,537,152 bytes (~53.0 GiB)
- Context (n_ctx): 153600
- Trained context: 262144
- Embedding dim: 3072
- Vocab size: 248320
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/UD-Q3_K_XL/Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf -ngl 99 -c 153600 --parallel 1 --threads 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on -b 4096 -ub 1024 --jinja --host 0.0.0.0 --port 8080 --metrics --temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.0 -a qwen3.5-122b-a10b-q3`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=153600
- Run started: 2026-05-13T22-54-51
- Run duration (min): 0.3
- Total calls: 4
- n_ctx_used_by_runner: 153600
- capabilities: ['tool_calling']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.199
- results: pass=4, fail=0, pending_rubric=0, error=0

### qwen3.5-122b-a10b-q3kxl__2026-05-13T22-59-11.jsonl

- Model tag: qwen3.5-122b-a10b-q3kxl
- Served model id: qwen3.5-122b-a10b-q3
- Model file: Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf
- Parameters: 122,111,526,912 (~122.1 B)
- File size: 56,959,537,152 bytes (~53.0 GiB)
- Context (n_ctx): 153600
- Trained context: 262144
- Embedding dim: 3072
- Vocab size: 248320
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/UD-Q3_K_XL/Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf -ngl 99 -c 153600 --parallel 1 --threads 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on -b 4096 -ub 1024 --jinja --host 0.0.0.0 --port 8080 --metrics --temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.0 -a qwen3.5-122b-a10b-q3`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=153600
- Run started: 2026-05-13T22-59-11
- Run duration (min): 2.5
- Total calls: 26
- n_ctx_used_by_runner: 153600
- capabilities: ['tool_calling_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 26
- calls_per_sec: 0.176
- results: pass=25, fail=1, pending_rubric=0, error=0

### qwen3.5-122b-a10b-q3kxl__2026-05-13T23-02-43.jsonl

- Model tag: qwen3.5-122b-a10b-q3kxl
- Served model id: qwen3.5-122b-a10b-q3
- Model file: Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf
- Parameters: 122,111,526,912 (~122.1 B)
- File size: 56,959,537,152 bytes (~53.0 GiB)
- Context (n_ctx): 153600
- Trained context: 262144
- Embedding dim: 3072
- Vocab size: 248320
- Inference server: llama.cpp
- Server build: b9101-389ff61d7
- Server cmdline: `llama-server -m /models/UD-Q3_K_XL/Qwen3.5-122B-A10B-UD-Q3_K_XL-00001-of-00003.gguf -ngl 99 -c 153600 --parallel 1 --threads 8 -sm layer -ts 1/1 -ctk q8_0 -ctv q8_0 -fa on -b 4096 -ub 1024 --jinja --host 0.0.0.0 --port 8080 --metrics --temp 0.7 --top-p 0.8 --top-k 20 --presence-penalty 1.5 --min-p 0.0 -a qwen3.5-122b-a10b-q3`
- Endpoint: http://localhost:8080/v1/chat/completions
- Sampling: temperature=0.7, top_p=0.8, top_k=20, presence_penalty=1.5, min_p=0.0
- Thinking-mode toggle: chat_template_kwargs.enable_thinking (true=on / false=off); reasoning returned in reasoning_content
- Client concurrency: 1
- max_tokens policy: per-prompt cap (default 8192 thinking-on / 2048 off; long_context uses each prompt's value); clamped to fit n_ctx=153600
- Run started: 2026-05-13T23-02-43
- Run duration (min): 2.2
- Total calls: 26
- n_ctx_used_by_runner: 153600
- capabilities: ['tool_calling']
- thinking_modes: ['on', 'off']
- calls_planned: 26
- calls_per_sec: 0.201
- results: pass=26, fail=0, pending_rubric=0, error=0

### qwen3.6-35b-a3b-q8kxl__2026-05-12T16-39-39__SMOKE.jsonl

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
- Run started: 2026-05-12T16-39-39
- Run duration (min): 0.9
- Total calls: 4
- n_ctx_used_by_runner: 262144
- capabilities: ['reasoning']
- thinking_modes: ['on', 'off']
- calls_planned: 4
- calls_per_sec: 0.071
- results: pass=4, fail=0, pending_rubric=0, error=0

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

### qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl

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
- Run started: 2026-05-14T00-04-36
- Run duration (min): 3.9
- Total calls: 52
- n_ctx_used_by_runner: 262144
- capabilities: ['tool_calling', 'tool_calling_hard']
- thinking_modes: ['on', 'off']
- calls_planned: 52
- calls_per_sec: 0.221
- results: pass=50, fail=2, pending_rubric=0, error=0

## Overall

| scope | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| all | 2251 | 94.8% | 0.955 | 14553 | 336 |

## By run (source file)

| source file | tag | n_ctx | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|---|
| _aborted_19-48-54_concurrency1.jsonl | gemma4-26b-a4b-q8km |  | 2 | — | — | 25172 | 888 |
| _aborted_22-10-29_hardrun_4calls.jsonl | gemma4-26b-a4b-q8km | 262144 | 4 | 100.0% | 1.000 | 16688 | 280 |
| gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | gemma4-26b-a4b-q8km | 8192 | 236 | 93.6% | 0.935 | 10672 | 352 |
| gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | gemma4-26b-a4b-q8km | 262144 | 21 | 100.0% | 1.000 | 7498 | 234 |
| gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | gemma4-26b-a4b-q8km | 262144 | 24 | 100.0% | 1.000 | 9699 | 312 |
| gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | gemma4-26b-a4b-q8km | 262144 | 236 | 98.3% | 0.976 | 21540 | 352 |
| gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | gemma4-26b-a4b-q8km | 262144 | 12 | 100.0% | 1.000 | 8456 | 116 |
| gemma4-26b-a4b-q8km__2026-05-12T03-21-56__SMOKE.jsonl | gemma4-26b-a4b-q8km | 262144 | 4 | 100.0% | 1.000 | 10744 | 376 |
| gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | gemma4-26b-a4b-q8km | 262144 | 164 | 90.9% | 0.935 | 17588 | 466 |
| gemma4-26b-a4b-q8km__2026-05-12T06-13-52__SMOKE.jsonl | gemma4-26b-a4b-q8km | 262144 | 4 | 100.0% | 0.964 | 37610 | 1302 |
| gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl | gemma4-26b-a4b-q8km | 262144 | 28 | 100.0% | 0.986 | 26746 | 938 |
| gemma4-26b-a4b-q8km__2026-05-12T11-49-54__SMOKE.jsonl | gemma4-26b-a4b-q8km | 262144 | 4 | 100.0% | 0.965 | 52149 | 1775 |
| gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl | gemma4-26b-a4b-q8km | 262144 | 30 | 93.3% | 0.954 | 26222 | 916 |
| gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl | gemma4-26b-a4b-q8km | 262144 | 52 | 100.0% | 1.000 | 1817 | 50 |
| gemma4-31b-q5kxl__2026-05-11T22-14-41__SMOKE.jsonl | gemma4-31b-q5kxl | 262144 | 4 | 100.0% | 1.000 | 21050 | 356 |
| gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | gemma4-31b-q5kxl | 262144 | 360 | 97.5% | 0.978 | 18282 | 259 |
| gemma4-31b-q5kxl__2026-05-12T15-07-51__SMOKE.jsonl | gemma4-31b-q5kxl | 262144 | 4 | 100.0% | 0.976 | 21806 | 360 |
| gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | gemma4-31b-q5kxl | 262144 | 58 | 96.6% | 0.952 | 38229 | 629 |
| gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl | gemma4-31b-q5kxl | 262144 | 52 | 98.1% | 0.981 | 3371 | 48 |
| qwen3.5-122b-a10b-q3kxl__2026-05-13T12-20-57__SMOKE.jsonl | qwen3.5-122b-a10b-q3kxl | 153600 | 4 | 100.0% | 1.000 | 31674 | 600 |
| qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | qwen3.5-122b-a10b-q3kxl | 153600 | 418 | 91.9% | 0.938 | 27376 | 551 |
| qwen3.5-122b-a10b-q3kxl__2026-05-13T22-54-51__SMOKE.jsonl | qwen3.5-122b-a10b-q3kxl | 153600 | 4 | 100.0% | 1.000 | 4527 | 66 |
| qwen3.5-122b-a10b-q3kxl__2026-05-13T22-59-11.jsonl | qwen3.5-122b-a10b-q3kxl | 153600 | 26 | 96.2% | 0.962 | 3973 | 66 |
| qwen3.5-122b-a10b-q3kxl__2026-05-13T23-02-43.jsonl | qwen3.5-122b-a10b-q3kxl | 153600 | 26 | 100.0% | 1.000 | 3751 | 62 |
| qwen3.6-35b-a3b-q8kxl__2026-05-12T16-39-39__SMOKE.jsonl | qwen3.6-35b-a3b-q8kxl | 262144 | 4 | 100.0% | 1.000 | 12700 | 508 |
| qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | qwen3.6-35b-a3b-q8kxl | 262144 | 418 | 92.6% | 0.940 | 14884 | 509 |
| qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl | qwen3.6-35b-a3b-q8kxl | 262144 | 52 | 96.2% | 0.962 | 2680 | 78 |

### Capability × thinking mode × run

| capability | thinking | run | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|---|
| coding | off | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 95.2% | 0.952 | 2108 | 58 |
| coding | off | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 2655 | 82 |
| coding | off | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 2630 | 82 |
| coding | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 95.2% | 0.952 | 3676 | 58 |
| coding | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 3836 | 58 |
| coding | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 95.2% | 0.952 | 3288 | 64 |
| coding | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 85.7% | 0.857 | 1766 | 64 |
| coding | on | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 95.2% | 0.952 | 22957 | 927 |
| coding | on | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 23294 | 817 |
| coding | on | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 12762 | 448 |
| coding | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 49495 | 905 |
| coding | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 26539 | 445 |
| coding | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 100.0% | 1.000 | 72257 | 1536 |
| coding | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 27537 | 1110 |
| coding_hard | off | gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | 2 | 100.0% | 1.000 | 9488 | 156 |
| coding_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 100.0% | 1.000 | 3507 | 116 |
| coding_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 7120 | 114 |
| coding_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 20 | 100.0% | 1.000 | 4768 | 96 |
| coding_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 100.0% | 1.000 | 4141 | 161 |
| coding_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 100.0% | 1.000 | 40828 | 1426 |
| coding_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 43481 | 719 |
| coding_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 20 | 100.0% | 1.000 | 99434 | 2104 |
| coding_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 100.0% | 1.000 | 59412 | 2374 |
| coding_quality | off | gemma4-26b-a4b-q8km__2026-05-12T06-13-52__SMOKE.jsonl | 2 | 100.0% | 0.952 | 15874 | 548 |
| coding_quality | off | gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl | 14 | 100.0% | 0.985 | 7753 | 265 |
| coding_quality | off | gemma4-31b-q5kxl__2026-05-12T15-07-51__SMOKE.jsonl | 2 | 100.0% | 0.982 | 14522 | 240 |
| coding_quality | off | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 14 | 100.0% | 0.968 | 13084 | 216 |
| coding_quality | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 14 | 92.9% | 0.923 | 12101 | 256 |
| coding_quality | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 92.9% | 0.958 | 5697 | 226 |
| coding_quality | on | gemma4-26b-a4b-q8km__2026-05-12T06-13-52__SMOKE.jsonl | 2 | 100.0% | 0.976 | 95598 | 3204 |
| coding_quality | on | gemma4-26b-a4b-q8km__2026-05-12T06-18-31.jsonl | 14 | 100.0% | 0.988 | 75538 | 2586 |
| coding_quality | on | gemma4-31b-q5kxl__2026-05-12T15-07-51__SMOKE.jsonl | 2 | 100.0% | 0.969 | 101716 | 1574 |
| coding_quality | on | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 14 | 100.0% | 0.975 | 61655 | 1003 |
| coding_quality | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 14 | 100.0% | 0.994 | 254053 | 5214 |
| coding_quality | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 100.0% | 0.979 | 91542 | 3626 |
| coding_quality_hard | off | gemma4-26b-a4b-q8km__2026-05-12T11-49-54__SMOKE.jsonl | 2 | 100.0% | 0.960 | 14558 | 504 |
| coding_quality_hard | off | gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl | 15 | 86.7% | 0.939 | 12947 | 447 |
| coding_quality_hard | off | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 15 | 93.3% | 0.952 | 25774 | 425 |
| coding_quality_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 15 | 53.3% | 0.812 | 21798 | 467 |
| coding_quality_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 15 | 73.3% | 0.899 | 11504 | 461 |
| coding_quality_hard | on | gemma4-26b-a4b-q8km__2026-05-12T11-49-54__SMOKE.jsonl | 2 | 100.0% | 0.970 | 109559 | 3680 |
| coding_quality_hard | on | gemma4-26b-a4b-q8km__2026-05-12T12-44-12.jsonl | 15 | 100.0% | 0.969 | 122152 | 4105 |
| coding_quality_hard | on | gemma4-31b-q5kxl__2026-05-12T15-12-37.jsonl | 15 | 93.3% | 0.915 | 119464 | 1866 |
| coding_quality_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 15 | 86.7% | 0.880 | 302657 | 6107 |
| coding_quality_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 15 | 86.7% | 0.877 | 150599 | 5758 |
| coherence | off | _aborted_19-48-54_concurrency1.jsonl | 1 | — | — | 16889 | 599 |
| coherence | off | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 20 | 100.0% | 0.972 | 10772 | 431 |
| coherence | off | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | — | — | 11010 | 377 |
| coherence | off | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | — | — | 12319 | 436 |
| coherence | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 20 | 100.0% | 0.990 | 27710 | 498 |
| coherence | on | _aborted_19-48-54_concurrency1.jsonl | 1 | — | — | 33456 | 1176 |
| coherence | on | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 20 | 90.0% | 0.903 | 33583 | 1344 |
| coherence | on | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | — | — | 38967 | 1365 |
| coherence | on | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | — | — | 117120 | 3906 |
| coherence | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 20 | 95.0% | 0.935 | 74619 | 1321 |
| coherence_hard | off | gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | 2 | — | — | 6584 | 102 |
| instruction_following | off | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 90.5% | 0.929 | 903 | 22 |
| instruction_following | off | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 571 | 8 |
| instruction_following | off | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 681 | 13 |
| instruction_following | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 95.2% | 0.952 | 1444 | 18 |
| instruction_following | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 95.2% | 0.952 | 1388 | 18 |
| instruction_following | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 85.7% | 0.881 | 1730 | 21 |
| instruction_following | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 81.0% | 0.865 | 928 | 20 |
| instruction_following | on | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 85.7% | 0.881 | 7280 | 290 |
| instruction_following | on | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 5742 | 199 |
| instruction_following | on | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 5069 | 174 |
| instruction_following | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 15352 | 266 |
| instruction_following | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 14073 | 233 |
| instruction_following | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 95.2% | 0.952 | 28620 | 609 |
| instruction_following | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 15410 | 616 |
| instruction_following_hard | off | gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | 2 | 100.0% | 1.000 | 3366 | 51 |
| instruction_following_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 16 | 75.0% | 0.917 | 1225 | 32 |
| instruction_following_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 16 | 68.8% | 0.875 | 2176 | 30 |
| instruction_following_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 16 | 62.5% | 0.812 | 2880 | 42 |
| instruction_following_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 16 | 50.0% | 0.755 | 1581 | 40 |
| instruction_following_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 16 | 75.0% | 0.844 | 98057 | 3334 |
| instruction_following_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 16 | 100.0% | 1.000 | 85797 | 1382 |
| instruction_following_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 16 | 75.0% | 0.844 | 137654 | 2906 |
| instruction_following_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 16 | 87.5% | 0.896 | 49503 | 1990 |
| long_context | off | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 14 | 100.0% | 1.000 | 12121 | 152 |
| long_context | off | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 6964 | 117 |
| long_context | off | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 7930 | 154 |
| long_context | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 14 | 100.0% | 1.000 | 14957 | 134 |
| long_context | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 92.9% | 0.929 | 13864 | 73 |
| long_context | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 14 | 100.0% | 1.000 | 4612 | 86 |
| long_context | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 92.9% | 0.929 | 3060 | 107 |
| long_context | on | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 14 | 78.6% | 0.786 | 31575 | 694 |
| long_context | on | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 14730 | 380 |
| long_context | on | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 55916 | 1711 |
| long_context | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 14 | 100.0% | 1.000 | 66353 | 685 |
| long_context | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 100.0% | 1.000 | 33844 | 326 |
| long_context | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 14 | 100.0% | 1.000 | 50882 | 660 |
| long_context | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 100.0% | 1.000 | 22408 | 394 |
| long_context_hard | off | gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | 2 | 100.0% | 1.000 | 20780 | 64 |
| long_context_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 12 | 100.0% | 1.000 | 17985 | 238 |
| long_context_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 12 | 91.7% | 0.917 | 26350 | 170 |
| long_context_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 12 | 91.7% | 0.917 | 11257 | 202 |
| long_context_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 12 | 83.3% | 0.833 | 8417 | 292 |
| long_context_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 12 | 91.7% | 0.917 | 118082 | 3230 |
| long_context_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 12 | 100.0% | 1.000 | 143073 | 1673 |
| long_context_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 12 | 100.0% | 1.000 | 86279 | 1194 |
| long_context_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 12 | 100.0% | 1.000 | 60532 | 1552 |
| reasoning | off | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 100.0% | 1.000 | 5934 | 232 |
| reasoning | off | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 7670 | 266 |
| reasoning | off | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 8686 | 304 |
| reasoning | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 14389 | 258 |
| reasoning | off | gemma4-31b-q5kxl__2026-05-11T22-14-41__SMOKE.jsonl | 2 | 100.0% | 1.000 | 13718 | 231 |
| reasoning | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 10138 | 171 |
| reasoning | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-20-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 16256 | 336 |
| reasoning | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 100.0% | 1.000 | 11087 | 236 |
| reasoning | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-39-39__SMOKE.jsonl | 2 | 100.0% | 1.000 | 9628 | 380 |
| reasoning | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 8709 | 338 |
| reasoning | on | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 100.0% | 1.000 | 16137 | 652 |
| reasoning | on | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 2 | 100.0% | 1.000 | 17553 | 619 |
| reasoning | on | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 20418 | 722 |
| reasoning | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 1.000 | 35322 | 638 |
| reasoning | on | gemma4-31b-q5kxl__2026-05-11T22-14-41__SMOKE.jsonl | 2 | 100.0% | 1.000 | 34807 | 584 |
| reasoning | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 1.000 | 31228 | 526 |
| reasoning | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-20-57__SMOKE.jsonl | 2 | 100.0% | 1.000 | 45987 | 912 |
| reasoning | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 100.0% | 1.000 | 45228 | 975 |
| reasoning | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-39-39__SMOKE.jsonl | 2 | 100.0% | 1.000 | 18516 | 754 |
| reasoning | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 1.000 | 24618 | 1017 |
| reasoning_hard | off | _aborted_22-10-29_hardrun_4calls.jsonl | 2 | 100.0% | 1.000 | 10682 | 180 |
| reasoning_hard | off | gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | 2 | 100.0% | 1.000 | 12257 | 204 |
| reasoning_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-21-56__SMOKE.jsonl | 2 | 100.0% | 1.000 | 7582 | 260 |
| reasoning_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 100.0% | 1.000 | 11478 | 404 |
| reasoning_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 20416 | 342 |
| reasoning_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 20 | 100.0% | 1.000 | 23919 | 502 |
| reasoning_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 100.0% | 1.000 | 13653 | 539 |
| reasoning_hard | on | _aborted_22-10-29_hardrun_4calls.jsonl | 2 | 100.0% | 1.000 | 25531 | 420 |
| reasoning_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-21-56__SMOKE.jsonl | 2 | 100.0% | 1.000 | 15755 | 544 |
| reasoning_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 20 | 95.0% | 0.950 | 32174 | 1134 |
| reasoning_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 20 | 100.0% | 1.000 | 59994 | 985 |
| reasoning_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 20 | 100.0% | 1.000 | 68426 | 1459 |
| reasoning_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 20 | 95.0% | 0.950 | 45247 | 1822 |
| tool_calling | off | gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl | 13 | 100.0% | 1.000 | 999 | 21 |
| tool_calling | off | gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl | 13 | 100.0% | 1.000 | 1930 | 20 |
| tool_calling | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T22-54-51__SMOKE.jsonl | 2 | 100.0% | 1.000 | 1807 | 34 |
| tool_calling | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T23-02-43.jsonl | 13 | 100.0% | 1.000 | 1721 | 33 |
| tool_calling | off | qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl | 13 | 100.0% | 1.000 | 1048 | 38 |
| tool_calling | on | gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl | 13 | 100.0% | 1.000 | 3462 | 114 |
| tool_calling | on | gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl | 13 | 100.0% | 1.000 | 5374 | 82 |
| tool_calling | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T22-54-51__SMOKE.jsonl | 2 | 100.0% | 1.000 | 8239 | 112 |
| tool_calling | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T23-02-43.jsonl | 13 | 100.0% | 1.000 | 7598 | 106 |
| tool_calling | on | qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl | 13 | 100.0% | 1.000 | 5355 | 153 |
| tool_calling_hard | off | gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl | 13 | 100.0% | 1.000 | 1224 | 30 |
| tool_calling_hard | off | gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl | 13 | 100.0% | 1.000 | 2340 | 30 |
| tool_calling_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T22-59-11.jsonl | 13 | 100.0% | 1.000 | 1924 | 37 |
| tool_calling_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl | 13 | 92.3% | 0.923 | 1141 | 40 |
| tool_calling_hard | on | gemma4-26b-a4b-q8km__2026-05-14T00-42-42.jsonl | 13 | 100.0% | 1.000 | 4100 | 143 |
| tool_calling_hard | on | gemma4-31b-q5kxl__2026-05-14T00-16-43.jsonl | 13 | 92.3% | 0.923 | 6741 | 106 |
| tool_calling_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T22-59-11.jsonl | 13 | 92.3% | 0.923 | 8602 | 126 |
| tool_calling_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-14T00-04-36.jsonl | 13 | 92.3% | 0.923 | 5198 | 159 |
| writing | off | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 100.0% | 0.962 | 3345 | 118 |
| writing | off | gemma4-26b-a4b-q8km__2026-05-11T19-13-05__SMOKE.jsonl | 1 | — | — | 1136 | 19 |
| writing | off | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | — | — | 3871 | 125 |
| writing | off | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 100.0% | 0.964 | 6376 | 114 |
| writing | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 0.967 | 6743 | 111 |
| writing | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 100.0% | 0.960 | 5652 | 105 |
| writing | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 95.2% | 0.926 | 3388 | 118 |
| writing | on | gemma4-26b-a4b-q8km__2026-05-11T17-04-05.jsonl | 21 | 85.7% | 0.855 | 31322 | 1261 |
| writing | on | gemma4-26b-a4b-q8km__2026-05-11T19-38-57__SMOKE.jsonl | 2 | — | — | 19480 | 687 |
| writing | on | gemma4-26b-a4b-q8km__2026-05-11T19-51-18.jsonl | 21 | 95.2% | 0.929 | 68283 | 1246 |
| writing | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 21 | 100.0% | 0.967 | 41810 | 701 |
| writing | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 21 | 95.2% | 0.926 | 142664 | 3014 |
| writing | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 21 | 100.0% | 0.986 | 42296 | 1706 |
| writing_hard | off | gemma4-26b-a4b-q8km__2026-05-11T22-05-22__SMOKE.jsonl | 2 | — | — | 8178 | 126 |
| writing_hard | off | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 14 | 100.0% | 0.954 | 4787 | 156 |
| writing_hard | off | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 100.0% | 0.964 | 7078 | 116 |
| writing_hard | off | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 14 | 85.7% | 0.829 | 8373 | 168 |
| writing_hard | off | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 85.7% | 0.832 | 3877 | 134 |
| writing_hard | on | gemma4-26b-a4b-q8km__2026-05-12T03-22-57.jsonl | 14 | 64.3% | 0.696 | 224944 | 7311 |
| writing_hard | on | gemma4-31b-q5kxl__2026-05-11T22-16-53.jsonl | 14 | 92.9% | 0.918 | 163928 | 2536 |
| writing_hard | on | qwen3.5-122b-a10b-q3kxl__2026-05-13T12-23-32.jsonl | 14 | 64.3% | 0.693 | 238539 | 4904 |
| writing_hard | on | qwen3.6-35b-a3b-q8kxl__2026-05-12T16-41-05.jsonl | 14 | 100.0% | 0.925 | 94983 | 3744 |

## By thinking mode

| thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|
| off | 1132 | 93.9% | 0.954 | 5252 | 118 |
| on | 1119 | 95.7% | 0.957 | 43591 | 1055 |

## By capability

| capability | n | pass rate | mean score | median latency (ms) | median out-tokens | pending |
|---|---|---|---|---|---|---|
| coding | 218 | 96.8% | 0.968 | 8436 | 223 |  |
| coding_hard | 162 | 100.0% | 1.000 | 14053 | 311 |  |
| coding_quality | 120 | 98.3% | 0.971 | 25871 | 617 |  |
| coding_quality_hard | 124 | 84.7% | 0.907 | 53269 | 1034 |  |
| coherence | 90 | 96.2% | 0.950 | 31467 | 866 | 10 |
| coherence_hard | 2 | — | — | 6584 | 102 | 2 |
| instruction_following | 218 | 93.1% | 0.943 | 4049 | 113 |  |
| instruction_following_hard | 130 | 74.6% | 0.870 | 6335 | 120 |  |
| long_context | 148 | 96.6% | 0.966 | 17721 | 242 |  |
| long_context_hard | 98 | 94.9% | 0.949 | 39722 | 530 |  |
| reasoning | 230 | 100.0% | 1.000 | 15282 | 422 |  |
| reasoning_hard | 170 | 98.8% | 0.988 | 24929 | 689 |  |
| tool_calling | 108 | 100.0% | 1.000 | 2786 | 56 |  |
| tool_calling_hard | 104 | 96.2% | 0.962 | 3416 | 66 |  |
| writing | 215 | 97.1% | 0.944 | 15822 | 325 | 5 |
| writing_hard | 114 | 86.6% | 0.851 | 24864 | 566 | 2 |

## Capability × thinking mode

| capability | thinking | n | pass rate | mean score | median latency (ms) | median out-tokens |
|---|---|---|---|---|---|---|
| coding | off | 109 | 94.5% | 0.945 | 3108 | 58 |
| coding | on | 109 | 99.1% | 0.991 | 33125 | 923 |
| coding_hard | off | 82 | 100.0% | 1.000 | 4839 | 119 |
| coding_hard | on | 80 | 100.0% | 1.000 | 53027 | 1471 |
| coding_quality | off | 60 | 96.7% | 0.959 | 10334 | 232 |
| coding_quality | on | 60 | 100.0% | 0.983 | 92646 | 3164 |
| coding_quality_hard | off | 62 | 77.4% | 0.903 | 17029 | 455 |
| coding_quality_hard | on | 62 | 91.9% | 0.912 | 152268 | 4564 |
| coherence | off | 45 | 100.0% | 0.981 | 15145 | 490 |
| coherence | on | 45 | 92.5% | 0.919 | 49370 | 1329 |
| coherence_hard | off | 2 | — | — | 6584 | 102 |
| instruction_following | off | 109 | 89.9% | 0.919 | 1213 | 20 |
| instruction_following | on | 109 | 96.3% | 0.968 | 15410 | 367 |
| instruction_following_hard | off | 66 | 65.2% | 0.845 | 1848 | 38 |
| instruction_following_hard | on | 64 | 84.4% | 0.896 | 69287 | 2096 |
| long_context | off | 74 | 97.3% | 0.973 | 10731 | 112 |
| long_context | on | 74 | 95.9% | 0.959 | 40760 | 550 |
| long_context_hard | off | 50 | 92.0% | 0.920 | 17963 | 232 |
| long_context_hard | on | 48 | 97.9% | 0.979 | 86279 | 1569 |
| reasoning | off | 115 | 100.0% | 1.000 | 10138 | 242 |
| reasoning | on | 115 | 100.0% | 1.000 | 28372 | 725 |
| reasoning_hard | off | 86 | 100.0% | 1.000 | 15066 | 400 |
| reasoning_hard | on | 84 | 97.6% | 0.976 | 47745 | 1230 |
| tool_calling | off | 54 | 100.0% | 1.000 | 1436 | 28 |
| tool_calling | on | 54 | 100.0% | 1.000 | 5461 | 114 |
| tool_calling_hard | off | 52 | 98.1% | 0.981 | 1453 | 36 |
| tool_calling_hard | on | 52 | 94.2% | 0.942 | 6701 | 134 |
| writing | off | 108 | 99.0% | 0.956 | 4620 | 114 |
| writing | on | 107 | 95.2% | 0.932 | 53977 | 1459 |
| writing_hard | off | 58 | 92.9% | 0.895 | 5367 | 142 |
| writing_hard | on | 56 | 80.4% | 0.808 | 163910 | 3970 |

## Rubric criteria (mean, normalized 0–1)

| capability | criterion | n | mean |
|---|---|---|---|
| coherence | accuracy | 8 | 1.000 |
| coherence | age_appropriateness | 4 | 1.000 |
| coherence | argument_quality | 4 | 1.000 |
| coherence | arithmetic_consistency | 4 | 1.000 |
| coherence | balance | 4 | 1.000 |
| coherence | causal_chain | 4 | 0.550 |
| coherence | clarity | 76 | 0.961 |
| coherence | completeness | 44 | 0.977 |
| coherence | consistency_with_own_explanation | 4 | 0.900 |
| coherence | consistent_application | 4 | 1.000 |
| coherence | consistent_concept_use | 4 | 1.000 |
| coherence | definition_accuracy | 4 | 1.000 |
| coherence | definition_quality | 4 | 0.900 |
| coherence | explanation_clarity | 4 | 1.000 |
| coherence | follow_through | 4 | 1.000 |
| coherence | food_web_consistency | 4 | 1.000 |
| coherence | handles_tension_coherently | 4 | 1.000 |
| coherence | inference_grounded | 4 | 1.000 |
| coherence | inference_grounded_in_setup | 4 | 1.000 |
| coherence | internal_consistency | 36 | 0.883 |
| coherence | internal_consistency_each_side | 4 | 1.000 |
| coherence | logical_flow | 8 | 1.000 |
| coherence | no_new_claims | 4 | 1.000 |
| coherence | numerical_correctness | 4 | 1.000 |
| coherence | period_plausibility | 4 | 0.800 |
| coherence | persuasiveness | 4 | 1.000 |
| coherence | pitch_quality | 4 | 1.000 |
| coherence | plot_coherence | 4 | 0.950 |
| coherence | practical_correctness | 4 | 1.000 |
| coherence | reasoning_quality | 8 | 1.000 |
| coherence | resolution | 4 | 0.500 |
| coherence | rule_completeness | 4 | 0.950 |
| coherence | sample_game_obeys_rules | 4 | 0.750 |
| coherence | scientific_accuracy | 4 | 0.950 |
| coherence | section_separation | 4 | 1.000 |
| coherence | self_consistency | 4 | 0.950 |
| coherence | self_reference_accuracy | 4 | 0.950 |
| coherence | steps_ingredients_consistency | 4 | 1.000 |
| coherence | tldr_faithfulness | 4 | 1.000 |
| coherence | tone_appropriate | 4 | 1.000 |
| coherence | verdict_follows_from_arguments | 4 | 0.900 |
| writing | adherence_to_prompt | 50 | 0.988 |
| writing | age_appropriateness | 10 | 0.920 |
| writing | appropriateness | 10 | 0.980 |
| writing | atmosphere | 10 | 1.000 |
| writing | balanced_critique | 10 | 1.000 |
| writing | bookend_constraint_met | 10 | 0.760 |
| writing | call_to_action | 10 | 1.000 |
| writing | characterization | 10 | 0.980 |
| writing | chorus_identical | 10 | 1.000 |
| writing | clear_value_prop | 10 | 1.000 |
| writing | completeness | 10 | 1.000 |
| writing | concision | 30 | 0.833 |
| writing | description_clarity | 10 | 0.980 |
| writing | emotional_resonance | 10 | 1.000 |
| writing | emotional_theme | 10 | 1.000 |
| writing | encouragement | 10 | 1.000 |
| writing | evokes_dawn | 10 | 1.000 |
| writing | fluency | 100 | 0.982 |
| writing | format | 10 | 1.000 |
| writing | four_lines | 10 | 1.000 |
| writing | hook | 10 | 1.000 |
| writing | humor | 10 | 0.560 |
| writing | imagery | 30 | 0.907 |
| writing | length | 40 | 0.865 |
| writing | length_adherence | 10 | 1.000 |
| writing | lightness_humor | 10 | 0.980 |
| writing | limerick_form | 10 | 0.820 |
| writing | meaning_preserved | 10 | 0.860 |
| writing | narrative_arc | 10 | 0.740 |
| writing | narrative_completeness | 10 | 0.920 |
| writing | narrative_quality | 10 | 0.980 |
| writing | naturalistic_dialogue | 10 | 1.000 |
| writing | on_topic | 10 | 0.920 |
| writing | persuasiveness | 10 | 0.920 |
| writing | professional_tone | 10 | 1.000 |
| writing | prose_quality | 40 | 0.935 |
| writing | realism | 10 | 1.000 |
| writing | restraint | 10 | 0.780 |
| writing | rhyme_and_meter | 10 | 0.640 |
| writing | rhyme_scheme_correct | 10 | 1.000 |
| writing | sensory_detail | 10 | 1.000 |
| writing | sincerity | 10 | 1.000 |
| writing | six_lines | 10 | 1.000 |
| writing | soothing_tone | 10 | 0.920 |
| writing | specific_detail | 10 | 1.000 |
| writing | specificity | 10 | 0.840 |
| writing | structure_correct | 10 | 1.000 |
| writing | tagline_punchiness | 10 | 0.960 |
| writing | three_line_form | 10 | 1.000 |
| writing | three_sentences | 10 | 0.980 |
| writing | tonal_continuity | 10 | 0.980 |
| writing | tone | 60 | 1.000 |
| writing | under_280_chars | 10 | 0.900 |
| writing | variety | 10 | 0.980 |
| writing | vividness_improved | 10 | 0.860 |
| writing | warmth_humor_balance | 10 | 0.960 |
| writing_hard | about_fifty_words | 8 | 0.650 |
| writing_hard | acrostic_spells_WINTER | 8 | 0.900 |
| writing_hard | actually_funny | 8 | 0.425 |
| writing_hard | age_appropriate | 8 | 0.975 |
| writing_hard | all_three_mention_locked_drawer | 8 | 0.925 |
| writing_hard | bridge_is_a_genuine_departure | 8 | 1.000 |
| writing_hard | chorus_identical_all_three_times | 8 | 1.000 |
| writing_hard | coherent_poem | 8 | 1.000 |
| writing_hard | coherent_poem_not_filler | 8 | 0.775 |
| writing_hard | comic_version_genuinely_comic | 8 | 0.975 |
| writing_hard | craft | 16 | 1.000 |
| writing_hard | creepiness | 8 | 0.600 |
| writing_hard | dialogue_only_no_narration | 8 | 1.000 |
| writing_hard | each_line_iambic_pentameter | 8 | 0.725 |
| writing_hard | each_opening_clearly_its_genre | 8 | 1.000 |
| writing_hard | earlier_text_supports_twist | 8 | 0.550 |
| writing_hard | emotional_coherence | 8 | 0.925 |
| writing_hard | emotional_resonance | 8 | 0.900 |
| writing_hard | events_identical_across_versions | 8 | 0.950 |
| writing_hard | exactly_100_words | 8 | 0.750 |
| writing_hard | exactly_four_lines | 8 | 0.900 |
| writing_hard | exactly_six_lines | 8 | 1.000 |
| writing_hard | final_word_recontextualizes | 8 | 0.525 |
| writing_hard | fluency | 16 | 0.688 |
| writing_hard | fourteen_lines | 8 | 1.000 |
| writing_hard | has_narrative_arc | 8 | 0.825 |
| writing_hard | imagery | 16 | 0.838 |
| writing_hard | imagery_and_theme | 8 | 1.000 |
| writing_hard | is_one_grammatical_sentence | 8 | 0.900 |
| writing_hard | limerick_form_correct | 8 | 0.600 |
| writing_hard | line_word_counts_1_through_8 | 8 | 0.700 |
| writing_hard | love_conveyed_through_subtext | 8 | 1.000 |
| writing_hard | meter_roughly_iambic_pentameter | 8 | 0.900 |
| writing_hard | narrative_progresses | 8 | 0.900 |
| writing_hard | narrative_quality | 8 | 0.975 |
| writing_hard | no_jargon_no_lesson_tone | 8 | 0.950 |
| writing_hard | no_love_words_used | 8 | 1.000 |
| writing_hard | no_modern_slips | 8 | 0.875 |
| writing_hard | persuasive_and_on_topic | 8 | 0.725 |
| writing_hard | present_tense_throughout | 8 | 0.750 |
| writing_hard | prose_quality | 24 | 0.800 |
| writing_hard | pun_on_pitch_works_both_ways | 8 | 0.550 |
| writing_hard | reads_naturally | 8 | 0.775 |
| writing_hard | realization_lands_emotionally | 8 | 0.775 |
| writing_hard | recursion_idea_conveyed | 8 | 1.000 |
| writing_hard | register_matched_throughout | 8 | 0.875 |
| writing_hard | rhyme_scheme_ABAB_CDCD_EFEF_GG | 8 | 0.900 |
| writing_hard | second_person_throughout | 8 | 0.800 |
| writing_hard | structure_VCVCBC | 8 | 1.000 |
| writing_hard | three_distinct_voices | 8 | 1.000 |
| writing_hard | tragic_version_genuinely_tragic | 8 | 1.000 |

## Failures (116)

| capability | prompt | mode | score | notes | finish/err |
|---|---|---|---|---|---|
| coherence | coh-02 | on | 0.200 | EMPTY response — thinking hit token cap (finish=length), 0 words | length |
| coherence | coh-03 | on | 0.200 | EMPTY — thinking hit token cap | length |
| coding | cod-14 | on | 0.000 | rc=1 stderr='File "<string>", line 1\n    ```python\n    ^\nSyntaxError: invalid syntax' | length |
| coding | cod-15 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 5, in <module>\n  | stop |
| instruction_following | if-03 | on | 0.500 | ok:forbidden chars seen: none \| X:hit=[] miss=['ocean'] forbidden_seen=[] | length |
| instruction_following | if-03 | off | 0.500 | ok:forbidden chars seen: none \| X:hit=[] miss=['ocean'] forbidden_seen=[] | stop |
| instruction_following | if-11 | on | 0.000 | 0 words (want 39..41) | length |
| instruction_following | if-11 | off | 0.000 | 38 words (want 39..41) | stop |
| instruction_following | if-18 | on | 0.000 | X:0 non-empty lines (want 3..3) \| X:missing_patterns=['(?m)^\\s*(\\S+\\s+){4}\\S+[.!?\\"\' | length |
| long_context | lc-11 | on | 0.000 | no number in response | length |
| long_context | lc-12 | on | 0.000 | no number in response | length |
| long_context | lc-14 | on | 0.000 | no number in response | length |
| writing | wr-08 | on | 0.200 | EMPTY — thinking hit token cap (finish=length) | length |
| writing | wr-11 | on | 0.200 | EMPTY — thinking hit token cap | length |
| writing | wr-21 | on | 0.200 | EMPTY — thinking hit token cap | length |
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
| tool_calling_hard | tc-h-03 | on | 0.000 | X:no tool call (good) but content missing /(hindi\|hi\b\|only support\|cannot\|don'?t support\| | stop |
| coding | cod-14 | off | 0.000 | rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 18, in <module>\n | stop |
| coding_quality | cq-03 | off | 0.333 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 25, in <module> | stop |
| instruction_following | if-09 | off | 0.000 | match=None | stop |
| instruction_following | if-11 | on | 0.000 | 0 words (want 39..41) | length |
| instruction_following | if-11 | off | 0.000 | 44 words (want 39..41) | stop |
| instruction_following | if-18 | off | 0.500 | ok:3 non-empty lines (want 3..3) \| X:missing_patterns=['(?m)^\\s*(\\S+\\s+){8}\\S+[.!?\\"\ | stop |
| writing | wr-21 | on | 0.200 | rubric: bookend_constraint_met=1, narrative_arc=1, prose_quality=1, length=1 | length |
| instruction_following_hard | if-h-01 | on | 0.667 | X:0 non-empty lines (want 7..7) \| ok:pattern absent (good) \| ok:forbidden chars seen: none | length |
| instruction_following_hard | if-h-02 | on | 0.333 | X:0 words (want 50..50) \| ok:forbidden chars seen: none \| X:does not end with 'done' | length |
| instruction_following_hard | if-h-02 | off | 0.333 | X:38 words (want 50..50) \| X:forbidden chars seen: {'s': 4} \| ok:ok | stop |
| instruction_following_hard | if-h-05 | off | 0.750 | ok:6 non-empty lines (want 6..6) \| ok:hit=['silver'] miss=[] forbidden_seen=[] \| X:pattern | stop |
| instruction_following_hard | if-h-08 | on | 0.000 | X:0 words (want 100..100) \| X:does not start with 'Begin'; does not end with 'End' \| X:hit | length |
| instruction_following_hard | if-h-08 | off | 0.667 | X:103 words (want 100..100) \| ok:ok \| ok:hit=['one hundred words'] miss=[] forbidden_seen= | stop |
| instruction_following_hard | if-h-12 | off | 0.500 | ok:5 non-empty lines (want 5..5) \| X:pattern matched: 'And danced on the window pane.' | stop |
| instruction_following_hard | if-h-13 | off | 0.750 | ok:3 sentences (want 3..3) \| ok:1x 'however' (want 1..1) \| ok:pattern absent (good) \| X:36 | stop |
| instruction_following_hard | if-h-16 | on | 0.500 | X:0 words (want 40..50) \| ok:forbidden chars seen: none | length |
| instruction_following_hard | if-h-16 | off | 0.000 | X:38 words (want 40..50) \| X:forbidden chars seen: {'e': 6} | stop |
| long_context_hard | lc-h-09 | off | 0.000 | got 93 want 90 (tol 0) | stop |
| writing_hard | wr-h-04 | off | 0.550 | rubric: line_word_counts_1_through_8=1, coherent_poem_not_filler=3, imagery=3, fluency=4 | stop |
| writing_hard | wr-h-08 | on | 0.200 | rubric: register_matched_throughout=1, no_modern_slips=1, narrative_progresses=1, prose_qu | length |
| writing_hard | wr-h-09 | on | 0.200 | rubric: about_fifty_words=1, final_word_recontextualizes=1, earlier_text_supports_twist=1, | length |
| writing_hard | wr-h-11 | on | 0.200 | rubric: exactly_four_lines=1, each_line_iambic_pentameter=1, reads_naturally=1, persuasive | length |
| writing_hard | wr-h-12 | on | 0.200 | rubric: limerick_form_correct=1, pun_on_pitch_works_both_ways=1, actually_funny=1, fluency | length |
| writing_hard | wr-h-12 | off | 0.350 | rubric: limerick_form_correct=2, pun_on_pitch_works_both_ways=2, actually_funny=1, fluency | stop |
| writing_hard | wr-h-13 | on | 0.200 | rubric: second_person_throughout=1, present_tense_throughout=1, realization_lands_emotiona | length |
| coding_quality_hard | cq-h-01 | off | 0.643 | ok:tests pass \| X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line | stop |
| coding_quality_hard | cq-h-02 | off | 0.591 | ok:tests pass \| X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line | stop |
| coding_quality_hard | cq-h-04 | off | 0.634 | ok:tests pass \| X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line | stop |
| coding_quality_hard | cq-h-07 | on | 0.222 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 3, in <module>\ | length |
| coding_quality_hard | cq-h-08 | off | 0.592 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 81, in <module> | stop |
| coding_quality_hard | cq-h-10 | off | 0.625 | ok:tests pass \| X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line | stop |
| coding_quality_hard | cq-h-11 | off | 0.647 | ok:tests pass \| X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line | stop |
| coding_quality_hard | cq-h-14 | on | 0.222 | X:rc=1 stderr='Traceback (most recent call last):\n  File "<string>", line 3, in <module>\ | length |
| coding_quality_hard | cq-h-14 | off | 0.893 | ok:tests pass \| ok:tests pass \| X:quality complexity=0.68, nesting=0.75, length=0.00, ruff | stop |
| tool_calling_hard | tc-h-03 | on | 0.000 | X:emitted 1 call(s): ['translate'] | tool_calls |
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
| tool_calling_hard | tc-h-03 | off | 0.000 | X:emitted 1 call(s): ['translate'] | tool_calls |
| tool_calling_hard | tc-h-05 | on | 0.000 | required call#1 get_weather({'city': {'equals': 'Houston'}, 'units': {'equals': 'fahrenhei | tool_calls |
