# Test catalog

Every prompt in the eval, grouped by capability and tier. **Generated from `prompts/*.jsonl` by `scripts/make_tests_md.py` — regenerate it after editing prompts.** The harness runs each of these **twice** — once with the model's thinking mode on, once off — so the call counts below double.

Grader shorthand: `numeric(=N)` exact-number answer-check · `word_count(a..b)` / `line_count` / `sentence_count` / `paragraph_count` / `bullets` structural counts · `contains` / `regex` / `regex_all` text checks · `forbid_char` forbidden characters · `starts_ends` first/last word · `json(keys)` JSON-shape · `count('x'=n)` substring-occurrence count · `python·unit-tests` extracted code run against hidden asserts · `code_quality(fn=…)` ast+ruff static analysis · `tool_call(fn)` / `no_tool_call` / `tool_calls_set[…]` checks the model's emitted tool calls (function name + arg constraints; for `no_tool_call`, asserts none was emitted) · `rubric[criteria…]` Claude scores 1–5 per named criterion (writing/coherence only). A `+` joins multiple sub-graders (all must pass).

**269 prompts** across **16 capability sets** → **538 calls** per full run (both thinking modes).

| set | # prompts |
|---|---|
| reasoning — base | 21 |
| coding — base | 21 |
| coding_quality — base | 14 |
| instruction_following — base | 21 |
| long_context — base | 14 |
| writing — base | 21 |
| coherence — base | 20 |
| tool_calling — base | 13 |
| reasoning — hard | 20 |
| coding — hard | 20 |
| coding_quality — hard | 15 |
| instruction_following — hard | 16 |
| long_context — hard | 12 |
| writing — hard | 14 |
| coherence — hard | 14 |
| tool_calling — hard | 13 |

## reasoning — base  (21 prompts)

| id | what it probes | grader |
|---|---|---|
| `rea-01` | A bookstore sold 23 books on Monday and 41 on Tuesday. On Wednesday it sold twice as many as Monday and Tuesday combined. How many books did it sell over the th… | numeric(=192) |
| `rea-02` | Tom is 4 years older than Jerry. In 6 years, the sum of their ages will be 40. How old is Tom now? Show your work, then end with 'Answer: <number>'. | numeric(=16) |
| `rea-03` | A rectangular garden is 3 times as long as it is wide, and its perimeter is 64 meters. What is its area in square meters? Show your work, then end with 'Answer:… | numeric(=192) |
| `rea-04` | All Florbs are Glips. Some Glips are Wodgers. No Wodger is a Florb. Can a Florb be a Wodger? Answer with one word — Yes or No — and a one-sentence reason. | regex |
| `rea-05` | What number comes next in the sequence 2, 6, 12, 20, 30, ___ ? Explain the pattern, then end with 'Answer: <number>'. | numeric(=42) |
| `rea-06` | What is the next number in this sequence: 1, 1, 2, 3, 5, 8, 13, ___ ? End with 'Answer: <number>'. | numeric(=21) |
| `rea-07` | If today is Wednesday, what day of the week will it be 100 days from now? Explain briefly, then end with 'Answer: <day name>'. | contains(friday) |
| `rea-08` | If 5 machines make 5 widgets in 5 minutes, how many minutes does it take 100 machines to make 100 widgets? Explain, then end with 'Answer: <number>'. | numeric(=5) |
| `rea-09` | A car travels 60 km in its first hour and 90 km in its second hour. What was its average speed in km/h over those two hours? End with 'Answer: <number>'. | numeric(=75) |
| `rea-10` | A jacket costs $80. It is discounted 25%, and then a further 10% is taken off the already-discounted price. What is the final price in dollars? Show your work, … | numeric(=54) |
| `rea-11` | How many distinct arrangements are there of the letters in the word 'LEVEL'? Explain, then end with 'Answer: <number>'. | numeric(=30) |
| `rea-12` | Ana, Beto, and Carla each own a different pet — a cat, a dog, or a fish. Ana does not own the dog. Carla owns neither the dog nor the cat. Who owns the dog? End… | contains(beto) |
| `rea-13` | A snail climbs 3 meters up a 10-meter wall each day but slips back 2 meters each night. On which day does it first reach the top? Explain, then end with 'Answer… | numeric(=8) |
| `rea-14` | Solve for x: 3(x - 4) = 2x + 5. Show your steps, then end with 'Answer: <number>'. | numeric(=17) |
| `rea-15` | A recipe for 4 servings calls for 300 g of flour and 2 eggs. You want to make 10 servings. How many grams of flour do you need? End with 'Answer: <number>'. | numeric(=750) |
| `rea-16` | If it rains, the match is cancelled. The match was not cancelled. Did it rain? Answer with one word — Yes or No — and a brief reason. | regex |
| `rea-17` | How many times does the digit 7 appear when you write out every integer from 1 to 100 inclusive? Explain, then end with 'Answer: <number>'. | numeric(=20) |
| `rea-18` | I think of a number. I double it, add 6, then divide the result by 2, and I get 11. What was my original number? Show your work, then end with 'Answer: <number>… | numeric(=8) |
| `rea-19` | A right triangle has legs of length 9 and 12. How long is the hypotenuse? End with 'Answer: <number>'. | numeric(=15) |
| `rea-20` | Two trains start 300 km apart on the same track, heading toward each other. One travels at 70 km/h, the other at 80 km/h. After how many hours do they meet? Exp… | numeric(=2) |
| `rea-21` | On an island, Knights always tell the truth and Knaves always lie. You meet A and B. A says: 'B is a Knave.' B says: 'We are both Knights.' What is A — a Knight… | regex |

## coding — base  (21 prompts)

*System prompt:* You are an expert Python programmer. When asked for a function, reply with ONLY a single Python code block containing just that function definition — no example usage, no prints, no explanation, no extra text.

| id | what it probes | grader |
|---|---|---|
| `cod-01` | Write `is_palindrome(s)` that returns True iff the string s reads the same forwards and backwards, ignoring case, spaces, and punctuation, else False. | python·unit-tests |
| `cod-02` | Write `fizzbuzz(n)` returning a list of strings for the integers 1..n: 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for multiples of 15, oth… | python·unit-tests |
| `cod-03` | Write `two_sum(nums, target)` returning a tuple of two distinct indices (i, j) with nums[i] + nums[j] == target, or None if no such pair exists. | python·unit-tests |
| `cod-04` | Write `flatten(lst)` that fully flattens an arbitrarily nested list of integers into a single flat list, preserving order. | python·unit-tests |
| `cod-05` | Write `word_count(text)` returning a dict mapping each lowercase word to its frequency. A word is a maximal run of alphanumeric characters; comparison is case-i… | python·unit-tests |
| `cod-06` | Write `roman_to_int(s)` converting a Roman numeral string (I,V,X,L,C,D,M; standard subtractive notation; values 1..3999) to an integer. | python·unit-tests |
| `cod-07` | Write `is_prime(n)` returning True iff the non-negative integer n is a prime number. | python·unit-tests |
| `cod-08` | Write `merge_intervals(intervals)` that merges a list of [start, end] intervals and returns the merged list sorted by start. | python·unit-tests |
| `cod-09` | Write `gcd(a, b)` returning the greatest common divisor of two positive integers. Do not use math.gcd. | python·unit-tests |
| `cod-10` | Write `caesar(text, shift)` applying a Caesar cipher: shift each ASCII letter by `shift` positions, wrapping within its own case; leave non-letters unchanged. N… | python·unit-tests |
| `cod-11` | Write `balanced(s)` returning True iff the bracket characters in s (only ()[]{}) are balanced and properly nested. Any other characters appear and should be ign… | python·unit-tests |
| `cod-12` | Write `running_max(nums)` returning a list whose i-th element is the maximum of nums[0..i]. | python·unit-tests |
| `cod-13` | Write `dedupe(seq)` returning a list with duplicates removed, keeping the first occurrence of each element and preserving order. | python·unit-tests |
| `cod-14` | Write `to_snake_case(s)` that converts a camelCase or PascalCase identifier to snake_case by inserting an underscore before each uppercase letter and lowercasin… | python·unit-tests |
| `cod-15` | Write `chunk(lst, n)` that splits lst into consecutive sublists of length n (the last one may be shorter). Assume n >= 1. | python·unit-tests |
| `cod-16` | Write `count_vowels(s)` returning the number of vowels (a,e,i,o,u; case-insensitive) in s. | python·unit-tests |
| `cod-17` | Write `transpose(matrix)` returning the transpose of a rectangular 2D list. transpose([]) returns []. | python·unit-tests |
| `cod-18` | Write `most_common(seq)` returning the element that appears most often in seq; ties may be broken arbitrarily. Assume seq is non-empty. | python·unit-tests |
| `cod-19` | Write `fib(n)` returning the n-th Fibonacci number with fib(0)=0 and fib(1)=1. It must run in O(n) time and handle n up to 50. | python·unit-tests |
| `cod-20` | Write `rle_encode(s)` that run-length-encodes a string: each maximal run of a character c of length k becomes 'c' followed by k. Example: 'aaabbc' -> 'a3b2c1'. … | python·unit-tests |
| `cod-21` | Write `is_anagram(a, b)` returning True iff a and b are anagrams of each other, ignoring case and spaces. | python·unit-tests |

## coding_quality — base  (14 prompts)

*System prompt:* You are a senior Python engineer writing production-quality code. Reply with ONLY a single Python code block containing the requested function — no example usage, no prints, no surrounding prose. Write it the way you'd want it to pass code review: a clear name, a concise docstring, type hints on eve…

| id | what it probes | grader |
|---|---|---|
| `cq-01` | Write `nth_fibonacci(n)` returning the n-th Fibonacci number (0-indexed: nth_fibonacci(0) is 0, nth_fibonacci(1) is 1). Raise ValueError if n is negative. It mu… | python·unit-tests + python·unit-tests + code_quality(fn=nth_fibonacci) |
| `cq-02` | Write `chunk(lst, size)` returning `lst` split into a list of consecutive sublists of length `size` (the final sublist may be shorter). Raise ValueError if `siz… | python·unit-tests + python·unit-tests + code_quality(fn=chunk) |
| `cq-03` | Write `is_anagram(a, b)` returning True iff `a` and `b` are anagrams of each other, comparing case-insensitively and ignoring whitespace. | python·unit-tests + python·unit-tests + code_quality(fn=is_anagram) |
| `cq-04` | Write `running_average(nums)` returning a list whose i-th element is the average (a float) of nums[0] through nums[i] inclusive. Raise ValueError if `nums` is e… | python·unit-tests + python·unit-tests + code_quality(fn=running_average) |
| `cq-05` | Write `flatten_dict(d, sep='.')` that flattens an arbitrarily nested dict into a single-level dict whose keys are the original key paths joined by `sep`. Non-di… | python·unit-tests + python·unit-tests + code_quality(fn=flatten_dict) |
| `cq-06` | Write `dedupe(seq)` returning a list of the elements of `seq` with duplicates removed, preserving the order of first occurrence. Do not mutate `seq`. | python·unit-tests + python·unit-tests + code_quality(fn=dedupe) |
| `cq-07` | Write `clamp(value, low, high)` returning `value` constrained to the inclusive range [low, high]. Raise ValueError if `low` is greater than `high`. | python·unit-tests + python·unit-tests + code_quality(fn=clamp) |
| `cq-08` | Write `word_frequencies(text)` returning a dict mapping each word to its count, comparing words case-insensitively where a word is a maximal run of alphanumeric… | python·unit-tests + python·unit-tests + code_quality(fn=word_frequencies) |
| `cq-09` | Write `parse_query_string(qs)` that parses a URL query string such as 'a=1&b=2&a=3' into a dict mapping each key to the list of its values, in order. A paramete… | python·unit-tests + python·unit-tests + code_quality(fn=parse_query_string) |
| `cq-10` | Write `moving_max(nums, k)` returning a list of the maximum value of each contiguous window of length `k` as the window slides across `nums`. Raise ValueError i… | python·unit-tests + python·unit-tests + code_quality(fn=moving_max) |
| `cq-11` | Write `safe_get(d, path, default=None)` that returns the value found in the nested dict `d` by following the dotted key `path` (e.g. 'a.b.c'), or `default` if a… | python·unit-tests + python·unit-tests + code_quality(fn=safe_get) |
| `cq-12` | Write `title_case(s)` that returns `s` with the first letter of each word capitalized and the rest lowercased, except that the small words a, an, and, as, at, b… | python·unit-tests + python·unit-tests + code_quality(fn=title_case) |
| `cq-13` | Write `validate_email(addr)` returning True iff `addr` looks like a basic email address: it contains exactly one '@', the part before the '@' is non-empty, and … | python·unit-tests + python·unit-tests + code_quality(fn=validate_email) |
| `cq-14` | Write `merge_sorted_lists(lists)` that merges a list of already-sorted lists into one sorted list. Merge them — do not simply concatenate everything and re-sort… | python·unit-tests + python·unit-tests + code_quality(fn=merge_sorted_lists) |

## instruction_following — base  (21 prompts)

| id | what it probes | grader |
|---|---|---|
| `if-01` | List exactly three reasons people enjoy hiking. Format each as a markdown bullet starting with '- '. Output nothing else. | bullets(3..3) + line_count(3..3) |
| `if-02` | Respond with exactly the word ACKNOWLEDGED in all capital letters and nothing else. | regex |
| `if-03` | Write one grammatical English sentence (at least 6 words, ending with a period) that does not contain the letter 'e' anywhere in it. | forbid_char(eE) + word_count(6..None) + regex |
| `if-04` | Output a JSON object with exactly these three keys: "name", "age", "city", with any plausible values. Output only the JSON — no code fence, no commentary. | json(name, age, city) |
| `if-05` | Output exactly five lines. Each line must contain a single word and nothing else. | line_count(5..5) + regex_all |
| `if-06` | Reply with exactly three lines. Every line must begin with the word 'Winter'. Output only those three lines. | line_count(3..3) + regex_all |
| `if-07` | Answer in exactly one sentence ending with a single period: why is the sky blue? | regex |
| `if-08` | Write a 4-line poem about coffee. Then, on a new line after the poem, write the word DONE. Output nothing at all after DONE. | regex + regex + line_count(5..6) |
| `if-09` | Respond using only lowercase letters and spaces — no uppercase letters, no punctuation, no digits. Write two sentences about your favorite season. | regex |
| `if-10` | Output the numbers 1 through 10 separated by commas, on a single line, with no spaces anywhere. Output nothing else. | regex |
| `if-11` | Write a product description for a reusable water bottle in exactly 40 words. Output only the description — no title, no preamble. | word_count(39..41) |
| `if-12` | Reply with exactly two paragraphs separated by one blank line. The first paragraph must be about cats; the second about dogs. Do not use any bullet points or nu… | regex + regex·must_not + contains(cat) + contains(dog) |
| `if-13` | Translate this sentence into French and output ONLY the French translation, nothing else: 'The cat is on the table.' | contains(chat,table) + regex·must_not |
| `if-14` | Give three synonyms for the word 'happy'. Number them 1., 2., 3., one per line. Output only the numbered list. | bullets(3..3) + regex_all |
| `if-15` | Write a single sentence that contains the word 'serendipity' and ends with an exclamation mark. | contains(serendipity) + regex |
| `if-16` | Repeat the word 'echo' exactly five times, separated by single spaces, and output nothing else. | regex |
| `if-17` | Respond with a valid JSON array containing exactly the first five prime numbers in ascending order. Output only the array. | json() + regex |
| `if-18` | Write exactly three sentences, each on its own line. The first sentence must have 5 words, the second 7 words, the third 9 words. | line_count(3..3) + regex_all |
| `if-19` | Answer in fewer than 20 words: what is photosynthesis? | word_count(5..19) |
| `if-20` | List the two days of the weekend (Saturday, Sunday) as a comma-separated list on one line. Then, on the next line, write exactly 'TOTAL: 2'. Output nothing else… | regex + regex |
| `if-21` | Write exactly one paragraph of exactly three sentences about the importance of getting enough sleep — but do not use the word 'sleep' itself anywhere; use 'rest… | regex·must_not + regex |

## long_context — base  (14 prompts)

| id | what it probes | grader |
|---|---|---|
| `lc-01` | [needle] What is Mira Marsh's lucky number? | numeric(=478) |
| `lc-02` | [needle] What is Luca Galloway's lucky number? | numeric(=923) |
| `lc-03` | [needle] What is Esme Calloway's lucky number? | numeric(=638) |
| `lc-04` | [needle] What is Nadia Voss's lucky number? | numeric(=863) |
| `lc-05` | [needle] What is Niko Volkov's lucky number? | numeric(=339) |
| `lc-06` | [needle] What is Rafa Thackeray's lucky number? | numeric(=247) |
| `lc-07` | [needle] What is Kofi Larkspur's lucky number? | numeric(=417) |
| `lc-08` | [needle] What is Anand Marsh's hobby? | contains(photography) |
| `lc-09` | [needle] What is Priya Osei's profession? | contains(electrician) |
| `lc-10` | [n80] How many of the people listed live in Norrath? | numeric(=4) |
| `lc-11` | [n120] How many of the people listed work as a optician? | numeric(=4) |
| `lc-12` | [n100] How many of the people listed joined in 2006? | numeric(=2) |
| `lc-13` | [n90] Which person has the lucky number 863? Give their full name. | contains(Sofia Kovac) |
| `lc-14` | [n100] How many of the people listed have a lucky number greater than 500? | numeric(=55) |

## writing — base  (21 prompts)

| id | what it probes | grader |
|---|---|---|
| `wr-01` | Write a haiku about a city waking up at dawn. | rubric[three_line_form, imagery, evokes_dawn, fluency] |
| `wr-02` | Write a 150–200 word cover letter for a junior data analyst position, addressed to a hiring manager named Priya Rao, mentioning SQL and a willingness to learn. | rubric[adherence_to_prompt, professional_tone, specificity, fluency] |
| `wr-03` | Write an online product description (50–80 words) for a stainless steel insulated travel mug. Persuasive but not over-the-top. | rubric[adherence_to_prompt, persuasiveness, restraint, fluency] |
| `wr-04` | Continue this story in 100–150 words, keeping the tone consistent: 'The elevator stopped between floors, and the lights flickered twice before settling into a d… | rubric[tonal_continuity, narrative_quality, prose_quality, length_adherence] |
| `wr-05` | Write a four-line poem about the sea that uses an ABAB rhyme scheme. | rubric[rhyme_scheme_correct, imagery, fluency, four_lines] |
| `wr-06` | Write a polite but firm email (under 120 words) declining a meeting invitation because of a scheduling conflict, and proposing two alternative times next week. | rubric[adherence_to_prompt, tone, completeness, concision] |
| `wr-07` | Write the opening paragraph (about 80 words) of a mystery novel set in a coastal town. Establish atmosphere and hint that something is wrong. | rubric[atmosphere, hook, prose_quality, length] |
| `wr-08` | Write a limerick about a programmer who can't find a bug. | rubric[limerick_form, humor, rhyme_and_meter, on_topic] |
| `wr-09` | Write a 3-sentence toast for a friend's 30th birthday — warm, a little funny, not cheesy. | rubric[tone, warmth_humor_balance, three_sentences, fluency] |
| `wr-10` | Rewrite this sentence to be more vivid and engaging while keeping the meaning: 'The meeting was long and we discussed many things.' | rubric[vividness_improved, meaning_preserved, concision, fluency] |
| `wr-11` | Write a bedtime story for a 5-year-old (120–160 words) about a sleepy little fox. Gentle, simple vocabulary, soothing ending. | rubric[age_appropriateness, soothing_tone, narrative_completeness, length] |
| `wr-12` | Write a tweet (under 280 characters) announcing the launch of a free open-source note-taking app called 'Margin'. Include a clear call to action. | rubric[under_280_chars, clear_value_prop, call_to_action, tone] |
| `wr-13` | Write a six-line free-verse poem about the feeling of finishing a long project. | rubric[emotional_resonance, imagery, six_lines, fluency] |
| `wr-14` | Write a 100-word review of a fictional ramen shop called 'Steam & Stone'. Mention one dish, the ambiance, and one small criticism. | rubric[adherence_to_prompt, specific_detail, balanced_critique, fluency] |
| `wr-15` | Write a motivational paragraph (about 90 words) for someone restarting a fitness routine after a long break — encouraging, realistic, not preachy. | rubric[tone, realism, encouragement, fluency] |
| `wr-16` | Write a short dialogue (8–12 lines) between a customer and a barista in which the customer is comically indecisive. Keep it light and natural. | rubric[naturalistic_dialogue, characterization, lightness_humor, format] |
| `wr-17` | For an app that helps friends split bills, write a one-sentence description of the app and three distinct tagline options. | rubric[adherence_to_prompt, tagline_punchiness, description_clarity, variety] |
| `wr-18` | Write an 80–100 word description of a fictional mountain village in autumn, in a warm, slightly nostalgic tone. | rubric[tone, sensory_detail, length, prose_quality] |
| `wr-19` | Write a short, encouraging note (under 60 words) to leave for a coworker who is having a hard week. | rubric[tone, sincerity, concision, appropriateness] |
| `wr-20` | Compose a four-stanza song lyric in the order verse, chorus, verse, chorus, about coming home after a long time away. The chorus must be word-for-word identical… | rubric[structure_correct, chorus_identical, emotional_theme, fluency] |
| `wr-21` | Write a 120-word piece of flash fiction that begins and ends with the exact same sentence: 'The kettle was still warm.' | rubric[bookend_constraint_met, narrative_arc, prose_quality, length] |

## coherence — base  (20 prompts)

| id | what it probes | grader |
|---|---|---|
| `coh-01` | Explain why the sky appears blue during the day and why sunsets appear red. Make sure both explanations rely on the same underlying physics and do not contradic… | rubric[internal_consistency, scientific_accuracy, logical_flow, clarity] |
| `coh-02` | Write a 180–220 word description of a typical workday for a lighthouse keeper in the year 1850. Keep every detail mutually consistent (available technology, dai… | rubric[internal_consistency, period_plausibility, completeness, clarity] |
| `coh-03` | Tell a short story in exactly 7 sentences in which each sentence is a direct logical consequence of the one before it. The final sentence must resolve the situa… | rubric[causal_chain, internal_consistency, resolution, clarity] |
| `coh-04` | Give 4 arguments for and 4 arguments against a four-day work week, then write a concluding paragraph that weighs them and reaches a verdict consistent with the … | rubric[balance, verdict_follows_from_arguments, logical_flow, clarity] |
| `coh-05` | Define the word 'recursion' for a 10-year-old. Then, using only the concepts you introduced in that definition, explain how a recursive function computes a fact… | rubric[definition_quality, self_consistency, age_appropriateness, clarity] |
| `coh-06` | Describe a fictional city called Aldermere: its geography, climate, main industry, and a typical festival. Then answer: given what you said, what would be the c… | rubric[internal_consistency, inference_grounded_in_setup, completeness, clarity] |
| `coh-07` | Explain the water cycle (evaporation, condensation, precipitation, collection). Then trace a single water molecule through one full loop, referencing each stage… | rubric[accuracy, consistency_with_own_explanation, completeness, clarity] |
| `coh-08` | Summarize, in one paragraph, the plot of an invented film called 'The Cartographer's Daughter'. Then list its three main characters with one-line descriptions t… | rubric[internal_consistency, plot_coherence, completeness, clarity] |
| `coh-09` | In a clearly labeled section, argue that remote work increases productivity. In a second clearly labeled section, argue the opposite. Each section must be inter… | rubric[section_separation, internal_consistency_each_side, argument_quality, clarity] |
| `coh-10` | Explain the rules of an invented card game called 'Tides' (setup, turn structure, win condition). Then walk through a sample 3-turn game between Ana and Ben tha… | rubric[rule_completeness, sample_game_obeys_rules, internal_consistency, clarity] |
| `coh-11` | Write a persuasive paragraph (about 100 words) recommending a Mediterranean-style diet. Then write a one-sentence TL;DR that accurately compresses your paragrap… | rubric[tldr_faithfulness, no_new_claims, persuasiveness, clarity] |
| `coh-12` | Describe how a bill becomes a law in a fictional parliamentary republic (you may invent the institutions). Keep the chamber names, vote thresholds, and the head… | rubric[internal_consistency, completeness, follow_through, clarity] |
| `coh-13` | Explain the difference between weather and climate. Then evaluate this statement using your own definitions: 'It snowed in April, so climate change isn't real.'… | rubric[definition_accuracy, consistent_application, reasoning_quality, clarity] |
| `coh-14` | Invent a small software company: give its name, its product, its target customer, and its pricing. Then write a 3-sentence elevator pitch and a one-line tagline… | rubric[internal_consistency, pitch_quality, completeness, clarity] |
| `coh-15` | Walk me through cooking scrambled eggs for two people, step by step. Then list the exact ingredients and quantities used — they must match the steps you describ… | rubric[steps_ingredients_consistency, completeness, practical_correctness, clarity] |
| `coh-16` | Explain compound interest with a worked example: $1,000 at 5% annual interest, compounded yearly, for 3 years. Show the balance after each year, and make sure y… | rubric[arithmetic_consistency, explanation_clarity, completeness, numerical_correctness] |
| `coh-17` | Describe a fictional island ecosystem: name 4 species and their relationships (who eats whom, who pollinates what). Then answer: if species #2 went extinct, wha… | rubric[food_web_consistency, inference_grounded, completeness, clarity] |
| `coh-18` | Give three predictions for what personal computing will look like in 2040. Then identify which of your own three predictions is the least likely and explain why… | rubric[self_reference_accuracy, handles_tension_coherently, reasoning_quality, clarity] |
| `coh-19` | Explain how vaccines train the immune system, introducing the terms antigen, memory cells, and antibodies. Then use those same three terms, in the same sense, t… | rubric[accuracy, consistent_concept_use, completeness, clarity] |
| `coh-20` | Write the 'About' section for a fictional national park: describe its landscape, one signature animal, one hiking trail (with length and difficulty), and the be… | rubric[internal_consistency, completeness, tone_appropriate, clarity] |

## tool_calling — base  (13 prompts)

*System prompt:* You have access to function tools. Call a function when it would help the user. If no tool is appropriate, answer the user directly in plain text. Use only the named tools provided. Today's date is 2026-05-13.

| id | what it probes | grader |
|---|---|---|
| `tc-01` | What is the weather in Paris right now? | tool_call(get_weather) |
| `tc-02` | Search the web for the latest SpaceX Starship launch results. | tool_call(web_search) |
| `tc-03` | Give me the weather in Berlin in Fahrenheit. | tool_call(get_weather) |
| `tc-04` | Please convert 7.5 miles into kilometers. | tool_call(convert_units) |
| `tc-05` | Set a calendar event called Dentist for 3pm next Friday. | tool_call(calendar_create_event) |
| `tc-06` | Set a 90-second timer. | tool_call(set_timer) |
| `tc-07` | What's AAPL trading at? | tool_call(get_stock_price) |
| `tc-08` | What's the capital of Australia? | no_tool_call |
| `tc-09` | Translate 'good morning' into Japanese. | tool_call(translate) |
| `tc-10` | What is 23% of 84? | tool_call(calculator) |
| `tc-11` | What's the current weather in Paris AND in Tokyo? Use celsius for both. | tool_calls_set[get_weather,get_weather] |
| `tc-12` | [multi-turn] What is the current price of MSFT? Answer in one short sentence. | no_tool_call + contains(410,MSFT) |
| `tc-13` | Find flights from New York to London on July 4, 2026. | tool_call(search_flights) |

## reasoning — hard  (20 prompts)

| id | what it probes | grader |
|---|---|---|
| `rea-h-01` | A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost, in cents? Show your reasoning, then end with 'Answer:… | numeric(=5) |
| `rea-h-02` | In a lake there is a patch of lily pads. Every day the patch doubles in size. It takes 48 days for the patch to cover the entire lake. On which day was the patc… | numeric(=47) |
| `rea-h-03` | A car travels uphill at 30 km/h and then back down the same road at 60 km/h. What is its average speed for the whole round trip, in km/h? Show your work, then e… | numeric(=40) |
| `rea-h-04` | A game show has three doors; behind one is a car, behind the other two are goats. You pick door 1. The host, who knows what is behind each door, opens door 3 to… | regex |
| `rea-h-05` | How many positive integers less than 1000 are divisible by 3 or by 5 but not by 15? Show your reasoning, then end with 'Answer: <number>'. | numeric(=400) |
| `rea-h-06` | What is the smaller angle, in degrees, between the hour hand and the minute hand of an analog clock at exactly 3:15? Show your work, then end with 'Answer: <num… | numeric(=7.5) |
| `rea-h-07` | On an island, knights always tell the truth and knaves always lie. A says: 'B is a knight.' B says: 'A and I are of different types.' What is B — a knight or a … | regex |
| `rea-h-08` | How many trailing zeros are there at the end of 100! (100 factorial) when written out in full? Explain, then end with 'Answer: <number>'. | numeric(=24) |
| `rea-h-09` | Working together, Alice and Bob finish a job in 4 hours. Alice working alone would take 6 hours. How many hours would Bob take working alone? Show your work, th… | numeric(=12) |
| `rea-h-10` | What is the last digit of 7 raised to the power 222? Explain the pattern, then end with 'Answer: <number>'. | numeric(=9) |
| `rea-h-11` | You have 25 horses and a track that fits 5 horses per race. You have no timer — each race only tells you the finishing order of those 5 horses. What is the mini… | numeric(=7) |
| `rea-h-12` | A digital clock loses 5 minutes every hour. It is set to the correct time at 12:00 noon. When the true time is midnight, 12 hours later, how many minutes behind… | numeric(=60) |
| `rea-h-13` | In how many ways can you make exactly 25 cents using only pennies (1¢), nickels (5¢), and dimes (10¢)? Order does not matter, and using zero of any coin is allo… | numeric(=12) |
| `rea-h-14` | Two positive integers have a product of 588 and a greatest common divisor of 7. What is their least common multiple? Explain, then end with 'Answer: <number>'. | numeric(=84) |
| `rea-h-15` | If the day before yesterday was a Thursday, what day of the week will the day after tomorrow be? Reason it out, then end with 'Answer: <day name>'. | contains(monday) |
| `rea-h-16` | A fair coin is flipped 4 times. What is the probability of getting exactly two heads? Give it as a fraction in lowest terms, then end with 'Answer: <fraction>'. | regex |
| `rea-h-17` | The average of 5 numbers is 20. When one of the numbers is removed, the average of the remaining 4 numbers is 18. What is the value of the number that was remov… | numeric(=28) |
| `rea-h-18` | Some philosophers are not wise. All wise people are happy. Does it logically follow that some philosophers are not happy? Answer with one word — Yes or No — and… | regex |
| `rea-h-19` | A farmer must cross a river with a wolf, a goat, and a cabbage. The boat carries the farmer plus at most one of the three. If left alone together, the wolf eats… | numeric(=7) |
| `rea-h-20` | A snail is at the bottom of a 30-foot well. Each day it climbs up 3 feet, and each night it slides back 2 feet. On which day does the snail first reach the top?… | numeric(=28) |

## coding — hard  (20 prompts)

*System prompt:* You are an expert Python programmer. When asked for a function, reply with ONLY a single Python code block containing just that function definition — no example usage, no prints, no explanation, no extra text.

| id | what it probes | grader |
|---|---|---|
| `cod-h-01` | Write `longest_unique_substring(s)` returning the length (an int) of the longest substring of s that contains no repeated characters. | python·unit-tests |
| `cod-h-02` | Write `edit_distance(a, b)` returning the Levenshtein edit distance (an int) between strings a and b — the minimum number of single-character insertions, deleti… | python·unit-tests |
| `cod-h-03` | Write `is_valid_brackets(s)` returning True iff the string s, containing only the characters ()[]{}, is a correctly nested and matched bracket sequence, else Fa… | python·unit-tests |
| `cod-h-04` | Write `coin_change(coins, amount)` returning the fewest number of coins (an int) drawn from the list `coins` that sum exactly to `amount` (each coin may be used… | python·unit-tests |
| `cod-h-05` | Write `max_subarray(nums)` returning the largest possible sum (an int) of any non-empty contiguous subarray of the integer list `nums`. | python·unit-tests |
| `cod-h-06` | Write `spiral_order(matrix)` returning a flat list of the elements of the rectangular 2-D list `matrix`, visited in clockwise spiral order starting from the top… | python·unit-tests |
| `cod-h-07` | Write `rotate_right(lst, k)` returning a NEW list equal to `lst` rotated to the right by k positions. k may be 0, larger than len(lst), or negative (negative ro… | python·unit-tests |
| `cod-h-08` | Write `int_to_roman(n)` converting an integer n with 1 <= n <= 3999 to its Roman-numeral string using standard subtractive notation (4 -> 'IV', 9 -> 'IX', 40 ->… | python·unit-tests |
| `cod-h-09` | Write `group_anagrams(words)` that groups the strings in `words` by anagram class. Return a list of groups; within each group sort the words ascending; sort the… | python·unit-tests |
| `cod-h-10` | Write `lower_bound(arr, x)` for a list `arr` sorted in non-decreasing order: return the index (an int) of the first element that is >= x, or len(arr) if no such… | python·unit-tests |
| `cod-h-11` | Write `count_islands(grid)` returning the number (an int) of connected groups of 1s in the 2-D list `grid` of 0s and 1s, where two cells are connected if they a… | python·unit-tests |
| `cod-h-12` | Write `decode_string(s)` decoding a string encoded with the rule k[encoded] meaning the substring `encoded` repeated k times; k is a positive integer and bracke… | python·unit-tests |
| `cod-h-13` | Write `longest_common_prefix(strs)` returning the longest string that is a prefix of every string in the list `strs`. If `strs` is empty or there is no common p… | python·unit-tests |
| `cod-h-14` | Write `power_set(nums)` returning a list of all subsets of the list of distinct integers `nums`. Sort each subset ascending, and sort the outer list using Pytho… | python·unit-tests |
| `cod-h-15` | Write `eval_rpn(tokens)` evaluating a list of Reverse Polish Notation tokens and returning the integer result. Operators are '+', '-', '*', '/'; division trunca… | python·unit-tests |
| `cod-h-16` | Write `trap_water(heights)` returning the total units of rainwater (an int) trapped between the bars whose heights are given by the list `heights`, where each b… | python·unit-tests |
| `cod-h-17` | Write `find_duplicate(nums)` for a list `nums` of n+1 integers where every integer is between 1 and n inclusive: return the value that appears more than once (t… | python·unit-tests |
| `cod-h-18` | Write `simplify_path(path)` returning the canonical form of an absolute Unix-style path: collapse repeated slashes, resolve '.' (current dir) and '..' (parent d… | python·unit-tests |
| `cod-h-19` | Write `next_permutation(nums)` returning a NEW list that is the next lexicographically greater permutation of the integer list `nums`; if `nums` is already the … | python·unit-tests |
| `cod-h-20` | Write `pascal_row(n)` returning the n-th row (0-indexed) of Pascal's triangle as a list of ints; row 0 is [1]. | python·unit-tests |

## coding_quality — hard  (15 prompts)

*System prompt:* You are a senior Python engineer writing production-quality code. Reply with ONLY a single Python code block containing the requested function — no example usage, no prints, no surrounding prose. Write it the way you'd want it to pass code review: a clear name, a concise docstring, type hints on eve…

| id | what it probes | grader |
|---|---|---|
| `cq-h-01` | Write `parse_int(s)` that parses a string to an int the way a strict base-10 parser should: allow leading/trailing whitespace, an optional single leading '+' or… | python·unit-tests + python·unit-tests + code_quality(fn=parse_int) |
| `cq-h-02` | Write `merge_intervals(intervals)` taking a list of (start, end) pairs (start <= end) and returning the sorted list of merged, non-overlapping (start, end) tupl… | python·unit-tests + python·unit-tests + code_quality(fn=merge_intervals) |
| `cq-h-03` | Write `take_while(predicate, iterable)` that yields items from `iterable` for as long as `predicate(item)` is true, then stops. As soon as an element fails the … | python·unit-tests + python·unit-tests + code_quality(fn=take_while) |
| `cq-h-04` | Write `parse_csv_row(line)` that parses a single CSV row (RFC 4180 style, single line — no embedded newlines) into a list of field strings. Fields are comma-sep… | python·unit-tests + python·unit-tests + code_quality(fn=parse_csv_row) |
| `cq-h-05` | Write `wildcard_match(pattern, text)` returning True iff `text` matches `pattern`, where '*' matches any sequence of characters (including empty) and '?' matche… | python·unit-tests + python·unit-tests + code_quality(fn=wildcard_match) |
| `cq-h-06` | Write `topological_sort(graph)` where `graph` is a dict mapping each node to a list of its successor nodes. Return a list of all nodes (a node that appears only… | python·unit-tests + python·unit-tests + code_quality(fn=topological_sort) |
| `cq-h-07` | Write `round_half_even(x, ndigits=0)` that rounds the number `x` to `ndigits` decimal places using round-half-to-even (banker's rounding) on the decimal value a… | python·unit-tests + python·unit-tests + code_quality(fn=round_half_even) |
| `cq-h-08` | Write `dijkstra(graph, start, end)` where `graph` is a dict mapping each node to a list of (neighbor, weight) pairs with non-negative numeric weights (a node th… | python·unit-tests + python·unit-tests + code_quality(fn=dijkstra) |
| `cq-h-09` | Write `lis_length(nums)` returning the length of the longest strictly increasing subsequence of the list `nums` (the subsequence need not be contiguous). The em… | python·unit-tests + python·unit-tests + code_quality(fn=lis_length) |
| `cq-h-10` | Write `parse_duration(s)` that parses a duration string into a total number of seconds (an int). The string is one or more segments, each a non-negative integer… | python·unit-tests + python·unit-tests + code_quality(fn=parse_duration) |
| `cq-h-11` | Write `deep_merge(a, b)` that returns a new dict merging dicts `a` and `b`: for keys present in both whose values are both dicts, merge recursively; otherwise `… | python·unit-tests + python·unit-tests + code_quality(fn=deep_merge) |
| `cq-h-12` | Write `compress_ranges(nums)` taking a list of integers (any order, possibly with duplicates) and returning a string of the sorted distinct values joined by com… | python·unit-tests + python·unit-tests + code_quality(fn=compress_ranges) |
| `cq-h-13` | Write `find_anagram_indices(text, pattern)` returning the sorted list of every start index in `text` where the length-len(pattern) substring is an anagram of `p… | python·unit-tests + python·unit-tests + code_quality(fn=find_anagram_indices) |
| `cq-h-14` | Write `evaluate(expr)` that evaluates a string arithmetic expression over the binary operators + - * / (standard precedence, left-associative), parentheses, opt… | python·unit-tests + python·unit-tests + code_quality(fn=evaluate) |
| `cq-h-15` | Write `roman_to_int(s)` that converts a Roman numeral string to its integer value (1 to 3999), accepting only well-formed standard numerals. Raise ValueError fo… | python·unit-tests + python·unit-tests + code_quality(fn=roman_to_int) |

## instruction_following — hard  (16 prompts)

| id | what it probes | grader |
|---|---|---|
| `if-h-01` | Output exactly 7 lines. Every line must start with '- ' (a hyphen then a space). The whole response must not contain the letter 'a' or 'A' anywhere. Output noth… | line_count(7..7) + regex·must_not + forbid_char(aA) |
| `if-h-02` | Write a single paragraph of exactly 50 words about coffee. The paragraph must not contain the letter 's' or 'S' anywhere. End the paragraph with the word 'done'… | word_count(50..50) + forbid_char(sS) + starts_ends(endswith='done') |
| `if-h-03` | Reply with a single JSON object and absolutely nothing else — no code fence, no commentary, no markdown. It must have exactly these keys: "title" (a non-empty s… | json(title, count, items) + regex·must_not |
| `if-h-04` | Write exactly 4 bullet points, each starting with '- '. Every bullet must begin with the word 'The' (capital T) immediately after the '- '. The word 'because' m… | bullets(4..4) + line_count(4..4) + regex·must_not + count('because'=2..2) |
| `if-h-05` | Write a 6-line poem. It must not contain the word 'the' anywhere (case-insensitive). The 3rd line must contain the word 'silver'. No line may start with a lower… | line_count(6..6) + contains(silver) + regex·must_not + regex·must_not |
| `if-h-06` | Output the first 8 prime numbers on a single line, separated by ' -> ' (space, arrow, space). No other text, no trailing arrow. | line_count(1..1) + regex |
| `if-h-07` | Write a haiku (3 lines) about winter. The middle line must be exactly, word for word: 'Cold wind bites the bare branches'. Output only the 3 lines. | line_count(3..3) + regex |
| `if-h-08` | Write a response of exactly 100 words. The first word must be 'Begin' and the last word must be 'End'. Somewhere in between, include the exact phrase 'one hundr… | word_count(100..100) + starts_ends(startswith='Begin', endswith='End') + contains(one hundred words) |
| `if-h-09` | Respond using only lowercase letters and single spaces — no uppercase, no punctuation, no digits, no line breaks. In one line, describe a sunrise in 15 to 20 wo… | word_count(15..20) + line_count(1..1) + regex |
| `if-h-10` | Write exactly 4 paragraphs separated by single blank lines. Each paragraph must be exactly 2 sentences. The whole response must be between 60 and 80 words. Do n… | paragraph_count(4) + sentence_count(8) + word_count(60..80) + regex·must_not |
| `if-h-11` | Output a comma-separated list of exactly 12 two-letter lowercase words on a single line. No spaces anywhere, no trailing comma, no other text. | regex |
| `if-h-12` | Write a 5-line limerick about a cat. Every one of the 5 lines must contain the letter 'z' (lowercase or uppercase) somewhere. Output only the 5 lines. | line_count(5..5) + regex·must_not |
| `if-h-13` | Reply with exactly three sentences. The word 'however' must appear exactly once. No sentence may contain a comma. The total word count must be between 25 and 35… | sentence_count(3) + count('however'=1) + regex·must_not + word_count(25..35) |
| `if-h-14` | Output a markdown table with exactly 3 columns headed Name, Age, and City, and exactly 4 data rows. Immediately after the table, on its own line, write exactly … | regex + count('(?m)^\\s*\\\|.*\\\|.*\\\|.*\\\|\\s*$'=6) + regex |
| `if-h-15` | Write a numbered list (1., 2., 3., ...) of exactly 5 programming languages, one per line. Then a blank line. Then the single word 'END' in all caps on its own l… | bullets(5..5) + regex_all + regex + regex·must_not |
| `if-h-16` | Write a paragraph about the importance of reading, between 40 and 50 words. It must not contain the letter 'e' or 'E' anywhere. Output only the paragraph. | word_count(40..50) + forbid_char(eE) |

## long_context — hard  (12 prompts)

| id | what it probes | grader |
|---|---|---|
| `lc-h-01` | [needle] In what year did Sofia Voss join? | numeric(=2008) |
| `lc-h-02` | [needle] In what year did Niko Goswami join? | numeric(=1996) |
| `lc-h-03` | [n150] Among everyone listed, consider only the people whose profession is 'actuary'. Of those, who appears FIRST in the list (lowest rec | numeric(=648) |
| `lc-h-04` | [nth_occurrence] Going through the list in order, find the THIRD person whose hobby is 'gardening'. What is that person's record number? | numeric(=65) |
| `lc-h-05` | [n180] Considering ONLY the records numbered 45 through 105 inclusive, how many of those people have a lucky number greater than 500? | numeric(=35) |
| `lc-h-06` | [n140] What is the sum of the lucky numbers of the people in records 85, 120, and 124? | numeric(=935) |
| `lc-h-07` | [n150] Among everyone who lives in Aldermere, who has the HIGHEST lucky number? Give their full name. | contains(Lena Kovac) |
| `lc-h-08` | [n170] What are the lucky numbers of Mira Larkspur and Hana Renfield, in that order? | regex_all |
| `lc-h-09` | [n160] How many of the people listed joined in an even-numbered year? | numeric(=90) |
| `lc-h-10` | [n150] After applying the correction above, how many of the people listed live in Aldermere? | numeric(=7) |
| `lc-h-11` | [n180] Exactly one person listed is a librarian whose hobby is painting. Who is it? Give their full name. | contains(Bea Achebe) |
| `lc-h-12` | [n220] What is the sum of the lucky numbers of the people in records 2, 89, and 206? | numeric(=1234) |

## writing — hard  (14 prompts)

| id | what it probes | grader |
|---|---|---|
| `wr-h-01` | Write a Shakespearean sonnet — 14 lines, rhyme scheme ABAB CDCD EFEF GG, roughly iambic pentameter — about the dread of an approaching deadline. | rubric[fourteen_lines, rhyme_scheme_ABAB_CDCD_EFEF_GG, meter_roughly_iambic_pentameter, imagery_and_theme] |
| `wr-h-02` | Write a complete piece of flash fiction of exactly 100 words that is a single grammatically correct sentence. It must have a beginning, a turn, and an end. | rubric[exactly_100_words, is_one_grammatical_sentence, has_narrative_arc, prose_quality] |
| `wr-h-03` | Write a 12-line dialogue between two people that makes it unmistakable they are falling in love — but neither character may use the word 'love' or any direct sy… | rubric[love_conveyed_through_subtext, no_love_words_used, dialogue_only_no_narration, emotional_resonance] |
| `wr-h-04` | Write a poem of exactly 8 lines where line 1 is exactly one word, line 2 is exactly two words, line 3 is exactly three words, and so on, up to line 8 being exac… | rubric[line_word_counts_1_through_8, coherent_poem_not_filler, imagery, fluency] |
| `wr-h-05` | Describe the exact same 60-second event twice — Version A in a comic register, Version B in a tragic register. The underlying events must be identical (same act… | rubric[events_identical_across_versions, comic_version_genuinely_comic, tragic_version_genuinely_tragic, craft] |
| `wr-h-06` | Write a 6-line acrostic poem: reading the first letter of each line from top to bottom spells WINTER. It must also be a coherent poem about winter — not just a … | rubric[acrostic_spells_WINTER, exactly_six_lines, coherent_poem, imagery] |
| `wr-h-07` | Write a children's story of 110–140 words that secretly teaches the idea of recursion (a thing that contains a smaller version of itself, with a stopping point)… | rubric[recursion_idea_conveyed, no_jargon_no_lesson_tone, age_appropriate, narrative_quality] |
| `wr-h-08` | Here is the opening line of a story in a deliberately ornate, archaic register: 'It was upon the seventh eve of the harvest moon that Mistress Aldworth, her bom… | rubric[register_matched_throughout, no_modern_slips, narrative_progresses, prose_quality] |
| `wr-h-09` | Write a 50-word horror micro-story whose final word forces the reader to reinterpret everything before it. The twist must be genuine — the earlier text must act… | rubric[about_fifty_words, final_word_recontextualizes, earlier_text_supports_twist, creepiness] |
| `wr-h-10` | Write three distinct opening sentences for what could be three different novels — one literary, one thriller, one romance — and each opening sentence must menti… | rubric[all_three_mention_locked_drawer, each_opening_clearly_its_genre, three_distinct_voices, craft] |
| `wr-h-11` | Write a product description for an ordinary ceramic coffee mug as exactly 4 lines, each line in iambic pentameter (ten syllables, da-DUM five times) — without i… | rubric[exactly_four_lines, each_line_iambic_pentameter, reads_naturally, persuasive_and_on_topic] |
| `wr-h-12` | Write a limerick (5 lines, AABBA, anapestic rhythm) whose final line lands a genuine pun on two different meanings of the word 'pitch'. The pun should actually … | rubric[limerick_form_correct, pun_on_pitch_works_both_ways, actually_funny, fluency] |
| `wr-h-13` | Write a 130–160 word scene told entirely in the second person ('you') and the present tense, in which the reader-character realizes something they have been in … | rubric[second_person_throughout, present_tense_throughout, realization_lands_emotionally, prose_quality] |
| `wr-h-14` | Write a six-stanza song lyric in the order verse, chorus, verse, chorus, bridge, chorus, about leaving a hometown. The chorus must be word-for-word identical al… | rubric[structure_VCVCBC, chorus_identical_all_three_times, bridge_is_a_genuine_departure, emotional_coherence] |

## coherence — hard  (14 prompts)

| id | what it probes | grader |
|---|---|---|
| `coh-h-01` | Invent three terms — a 'Wend', a 'Glark', and a 'Trune' — and give precise definitions such that all of the following hold: every Wend is a Glark; no Trune is a… | rubric[definitions_precise, constraints_mutually_satisfiable, inference_strictly_follows, clarity] |
| `coh-h-02` | Write a story of exactly 9 sentences in which, for N from 3 to 9, sentence N is a direct consequence of sentence N-2 (NOT of sentence N-1) — i.e. there are two … | rubric[exactly_9_sentences, interleaved_causality_holds, both_threads_resolved, explanation_accurate] |
| `coh-h-03` | Take the claim: 'A government should always prioritize economic growth over environmental protection.' Write the strongest one-paragraph argument FOR it, then t… | rubric[both_arguments_strong, weakness_in_each_identified, critiques_specific_not_circular, clarity] |
| `coh-h-04` | Describe a small dungeon of exactly 6 rooms (R1..R6) and list every door (each door connects two rooms and is two-way). Then state the shortest route from R1 to… | rubric[door_list_complete_and_consistent, stated_route_valid, route_is_actually_shortest, alternative_route_valid] |
| `coh-h-05` | Explain the Ship of Theseus paradox in your own words. Then commit to a definite position on whether the fully-replaced ship is 'the same ship', and defend it. … | rubric[paradox_stated_accurately, position_is_definite, defense_consistent_with_framing, reasoning_quality] |
| `coh-h-06` | Invent a positional number system in base 6 using six distinct invented single-character digit symbols, stating which symbol means 0, 1, 2, 3, 4, 5. Then add tw… | rubric[symbol_mapping_clear, base6_addition_and_carries_correct, base10_verification_correct, internally_consistent] |
| `coh-h-07` | Construct a family tree spanning 4 generations with at least 9 named people; for each person state their parents (or note they married into the family). Then an… | rubric[tree_well_specified, relationship_answers_correct, handles_distant_relations, clarity] |
| `coh-h-08` | Give a timeline of 7 dated events (with specific years) for a fictional interstate conflict. Then write a causal analysis stating which events caused which — bu… | rubric[timeline_dated_and_ordered, causality_respects_chronology, counterfactual_grounded_in_chain, clarity] |
| `coh-h-09` | Define 'necessary condition' and 'sufficient condition' precisely. Then classify each of the following correctly, using your definitions and explaining each one… | rubric[definitions_correct, all_four_classified_correctly, explanations_apply_own_defs, clarity] |
| `coh-h-10` | Write a dialogue of exactly 10 turns between two characters, Q and S, where every line spoken by Q is a question ending in '?' and every line spoken by S is a d… | rubric[exactly_10_turns, Q_only_questions_S_only_statements, coherent_story_arc, natural_dialogue] |
| `coh-h-11` | Pick any well-known proverb and state it. Then write a short scenario (about 110 words) in which faithfully following that proverb leads to a clearly BAD outcom… | rubric[same_proverb_same_sense_both_times, bad_scenario_genuinely_follows_proverb, good_scenario_genuinely_follows_proverb, prose_quality] |
| `coh-h-12` | Explain the difference between correlation and causation. Then give one concrete made-up example with specific numbers showing a strong correlation between two … | rubric[distinction_correct, example_concrete_with_numbers, three_causal_stories_each_fit, clarity] |
| `coh-h-13` | Design a tiny, consistent magic system as exactly 5 numbered rules (what powers it, its cost, its hard limit, who can use it, what it cannot do). Then write a r… | rubric[five_rules_coherent, scene_obeys_all_rules, rule3_constraint_correctly_identified, prose_quality] |
| `coh-h-14` | State a small decision or logic problem with one clearly correct answer (you invent it — e.g. a tiny expected-value bet, or a short logic puzzle). Solve it corr… | rubric[correct_solution_is_correct, wrong_solution_is_genuinely_plausible, error_precisely_located, clarity] |

## tool_calling — hard  (13 prompts)

*System prompt:* You have access to function tools. Call a function when it would help the user. If no tool is appropriate, answer the user directly in plain text. Use only the named tools provided. Today's date is 2026-05-13.

| id | what it probes | grader |
|---|---|---|
| `tc-h-01` | Send Bob an email. | no_tool_call |
| `tc-h-02` | Summarize the latest reviews of the iPhone 16. | tool_call(web_search) |
| `tc-h-03` | Translate 'Welcome to my home' into Hindi for me. | no_tool_call |
| `tc-h-04` | Look up the user named Sarah Chen for me. | tool_call(find_user) |
| `tc-h-05` | What's the weather in Paris in Celsius and Houston in Fahrenheit? | tool_calls_set[get_weather,get_weather] |
| `tc-h-06` | Translate the word 'Welcome' into French, and then schedule a 9am reminder for tomorrow with that translation as the title. | tool_call(translate) |
| `tc-h-07` | Can you clean up my desktop for me? | no_tool_call |
| `tc-h-08` | Three weeks from today at 10am, meeting with Sara. | tool_call(calendar_create_event) |
| `tc-h-09` | [multi-turn] What's the weather in Reykjavik right now? Answer in one short sentence. | no_tool_call + contains(-3,snow) |
| `tc-h-10` | What is the weather in Paris? | tool_call(get_weather) |
| `tc-h-11` | Set a timer for two and a half minutes. | tool_call(set_timer) |
| `tc-h-12` | Weather in Paris. | tool_call(get_weather) |
| `tc-h-13` | [multi-turn] What's the current price of XYZQ? | no_tool_call + regex |

