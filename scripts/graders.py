"""Programmatic + rubric grader registry for the local-model eval harness.

A `grader` is a dict {"type": ..., ...} or a list of such dicts (all must pass;
score = mean of sub-scores). `grade(grader, text)` returns:
    {score: float|None in [0,1], passed: bool|None, notes: str, pending: bool, ...}
`pending=True` means a human (Claude) must score it later (rubric graders).
Keep the return shape stable -- it is part of the cross-run results contract.
"""
import re, json, subprocess, ast, shutil

_RUFF = shutil.which("ruff")   # used by the code_quality grader; None -> that check is skipped

# ---------------------------------------------------------------- helpers ----
_NUM_RE = re.compile(r'-?\d[\d,]*\.?\d*')

def _last_number(s):
    s = s.replace('−', '-').replace('–', '-')
    nums = _NUM_RE.findall(s)
    return nums[-1].replace(',', '') if nums else None

def _norm(s):
    return re.sub(r'\s+', ' ', str(s).strip().lower())

_CODE_BLOCK = re.compile(r'```[ \t]*(?:python|py)?[ \t]*\r?\n(.*?)```', re.S)

def extract_code(s):
    blocks = _CODE_BLOCK.findall(s)
    if blocks:
        return '\n\n'.join(b.rstrip() for b in blocks)
    return s  # assume the whole reply is code

# Tool graders need to see the per-call record (tool_calls etc), not just text;
# every other grader still takes (g, text) -- zero edits to the 16 existing ones.
_TOOL_TYPES = {"tool_call", "no_tool_call", "tool_calls_set"}

# ---------------------------------------------------------------- entry -------
def grade(grader, text, rec=None):
    if grader is None:
        return dict(score=None, passed=None, notes="no grader", pending=False)
    if isinstance(grader, list):
        subs = [grade(g, text, rec) for g in grader]
        if any(s.get("pending") for s in subs):
            return dict(score=None, passed=None, pending=True,
                        notes=" | ".join(s.get("notes", "") for s in subs), sub=subs)
        passed = all(bool(s["passed"]) for s in subs)
        score = sum(float(s["score"]) for s in subs) / len(subs)
        return dict(score=round(score, 4), passed=passed, pending=False,
                    notes=" | ".join(f"{'ok' if s['passed'] else 'X'}:{s['notes']}" for s in subs),
                    sub=subs)
    t = grader.get("type")
    fn = GRADERS.get(t)
    if fn is None:
        return dict(score=0.0, passed=False, notes=f"unknown grader type {t!r}", pending=False)
    try:
        return fn(grader, text or "", rec) if t in _TOOL_TYPES else fn(grader, text or "")
    except Exception as e:  # a broken grader should not abort the run
        return dict(score=0.0, passed=False, notes=f"grader error: {e!r}", pending=False)

def _res(ok, notes):
    return dict(score=1.0 if ok else 0.0, passed=bool(ok), notes=notes, pending=False)

# ---------------------------------------------------------------- graders ----
def g_contains(g, text):
    """{values:[...], mode:'all'|'any'(=all), excludes:[...], ignorecase:True}"""
    ic = g.get("ignorecase", True)
    hay = text.lower() if ic else text
    vals = g["values"]
    hit = [v for v in vals if (v.lower() if ic else v) in hay]
    ok = (len(hit) == len(vals)) if g.get("mode", "all") == "all" else (len(hit) > 0)
    bad = [v for v in g.get("excludes", []) if (v.lower() if ic else v) in hay]
    return _res(ok and not bad, f"hit={hit} miss={[v for v in vals if v not in hit]} forbidden_seen={bad}")

def g_regex(g, text):
    """{pattern, ignorecase:True, group, group_equals, must_not:bool}"""
    flags = re.I if g.get("ignorecase", True) else 0
    m = re.search(g["pattern"], text, flags)
    if g.get("must_not"):
        return _res(not m, f"pattern {'matched: '+repr(m.group(0)[:60]) if m else 'absent (good)'}")
    ok = bool(m)
    if ok and "group_equals" in g:
        ok = _norm(m.group(g.get("group", 1))) == _norm(g["group_equals"])
    return _res(ok, f"match={repr(m.group(0)[:80]) if m else None}")

def g_regex_all(g, text):
    """{patterns:[...], ignorecase:True}  -- all must match"""
    flags = re.I if g.get("ignorecase", True) else 0
    miss = [p for p in g["patterns"] if not re.search(p, text, flags)]
    return _res(not miss, f"missing_patterns={miss}")

def g_numeric(g, text):
    """{gold: number, tol: 0}  -- prefers the first number after the last 'answer' mention,
    then \\boxed{...}, then the last number anywhere in the response."""
    gold, tol = float(g["gold"]), float(g.get("tol", 0))
    cand = None
    ans_pos = [m.end() for m in re.finditer(r'answer', text, re.I)]
    if ans_pos:
        m = _NUM_RE.search(text[ans_pos[-1]:].replace('−', '-').replace('–', '-'))
        if m:
            cand = m.group(0)
    if cand is None:
        boxed = re.findall(r'\\boxed\{\s*(-?\d[\d,]*\.?\d*)', text)
        cand = boxed[-1] if boxed else _last_number(text)
    if cand is None:
        return _res(False, "no number in response")
    try:
        val = float(cand.replace(',', ''))
    except ValueError:
        return _res(False, f"unparsable number {cand!r}")
    return _res(abs(val - gold) <= tol, f"got {val:g} want {gold:g} (tol {g.get('tol', 0)})")

def g_word_count(g, text):
    """{min, max} or {exact} ; counts words in whole response (or last paragraph if last_para)"""
    src = text
    if g.get("last_para"):
        paras = [p for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
        src = paras[-1] if paras else text
    n = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", src))
    lo = g.get("min", g.get("exact"))
    hi = g.get("max", g.get("exact"))
    ok = (lo is None or n >= lo) and (hi is None or n <= hi)
    return _res(ok, f"{n} words (want {lo}..{hi})")

def g_line_count(g, text):
    """non-empty lines; {min,max} or {exact}"""
    n = len([l for l in text.splitlines() if l.strip()])
    lo, hi = g.get("min", g.get("exact")), g.get("max", g.get("exact"))
    return _res((lo is None or n >= lo) and (hi is None or n <= hi), f"{n} non-empty lines (want {lo}..{hi})")

def g_bullets(g, text):
    """count markdown bullets / numbered items; {min,max} or {exact}"""
    n = len(re.findall(r'^[ \t]*(?:[-*•]|\d+[.)])[ \t]+\S', text, re.M))
    lo, hi = g.get("min", g.get("exact")), g.get("max", g.get("exact"))
    return _res((lo is None or n >= lo) and (hi is None or n <= hi), f"{n} bullets (want {lo}..{hi})")

def g_count(g, text):
    """count occurrences of a substring or regex; {needle, regex:False, ignorecase:True, min,max,exact}"""
    needle = g["needle"]
    if g.get("regex"):
        flags = re.I if g.get("ignorecase", True) else 0
        n = len(re.findall(needle, text, flags))
    else:
        hay = text.lower() if g.get("ignorecase", True) else text
        nd = needle.lower() if g.get("ignorecase", True) else needle
        n = hay.count(nd)
    lo = g.get("min", g.get("exact")); hi = g.get("max", g.get("exact"))
    ok = (lo is None or n >= lo) and (hi is None or n <= hi)
    return _res(ok, f"{n}x {needle!r} (want {lo}..{hi})")

def g_sentence_count(g, text):
    """count sentences (runs of text ending in . ! or ?); {min,max} or {exact}"""
    n = len([s for s in re.split(r'[.!?]+(?=\s|$)', text.strip()) if s.strip()])
    lo, hi = g.get("min", g.get("exact")), g.get("max", g.get("exact"))
    return _res((lo is None or n >= lo) and (hi is None or n <= hi), f"{n} sentences (want {lo}..{hi})")

def g_paragraph_count(g, text):
    """count blank-line-separated paragraphs; {min,max} or {exact}"""
    n = len([p for p in re.split(r'\n[ \t]*\n', text.strip()) if p.strip()])
    lo, hi = g.get("min", g.get("exact")), g.get("max", g.get("exact"))
    return _res((lo is None or n >= lo) and (hi is None or n <= hi), f"{n} paragraphs (want {lo}..{hi})")

def g_json(g, text):
    """{required_keys:[...], equals:{k:v}, top_type:'object'|'array'}
    Extracts a fenced ```json block if present, else the first balanced {...} / [...]."""
    m = re.search(r'```[ \t]*(?:json)?[ \t]*\r?\n(.*?)```', text, re.S)
    blob = m.group(1) if m else text
    obj = None
    for opn, cls in (('{', '}'), ('[', ']')):
        i, j = blob.find(opn), blob.rfind(cls)
        if 0 <= i < j:
            try:
                obj = json.loads(blob[i:j + 1]); break
            except Exception:
                continue
    if obj is None:
        return _res(False, "no parseable JSON found")
    notes, ok = [], True
    if "top_type" in g:
        want = {"object": dict, "array": list}[g["top_type"]]
        if not isinstance(obj, want):
            ok = False; notes.append(f"top type {type(obj).__name__}!={g['top_type']}")
    look = obj if isinstance(obj, dict) else {}
    for k in g.get("required_keys", []):
        if k not in look:
            ok = False; notes.append(f"missing key {k!r}")
    for k, v in g.get("equals", {}).items():
        if _norm(look.get(k)) != _norm(v):
            ok = False; notes.append(f"{k}={look.get(k)!r}!={v!r}")
    return _res(ok, "; ".join(notes) or "valid & matches")

def g_forbid_char(g, text):
    """{chars:'eE' | char:'e'}  -- none of these characters may appear"""
    chars = g.get("chars") or g["char"]
    counts = {c: text.count(c) for c in set(chars) if text.count(c)}
    return _res(not counts, f"forbidden chars seen: {counts or 'none'}")

def g_starts_ends(g, text):
    """{startswith:..., endswith:...}  -- ignores surrounding whitespace; case-insensitive"""
    s = text.strip()
    ok, notes = True, []
    if "startswith" in g and not s.lower().startswith(g["startswith"].lower()):
        ok = False; notes.append(f"does not start with {g['startswith']!r}")
    if "endswith" in g:
        tail = s.rstrip('."\'!? ).')  # tolerate trailing punctuation/quotes
        if not (s.lower().endswith(g["endswith"].lower()) or tail.lower().endswith(g["endswith"].lower())):
            ok = False; notes.append(f"does not end with {g['endswith']!r}")
    return _res(ok, "; ".join(notes) or "ok")

def g_python(g, text):
    """{test:'assert f(1)==2\\n...', timeout:10}  -- runs extracted code + test in a subprocess."""
    code = extract_code(text)
    src = code + "\n\n" + g["test"] + "\nprint('OK_GRADER_PASS')\n"
    try:
        r = subprocess.run(["python3", "-I", "-c", src], capture_output=True, text=True,
                           timeout=g.get("timeout", 10))
    except subprocess.TimeoutExpired:
        return _res(False, "timeout running candidate code")
    except Exception as e:
        return _res(False, f"exec error: {e!r}")
    ok = r.returncode == 0 and "OK_GRADER_PASS" in r.stdout
    return _res(ok, "tests pass" if ok else f"rc={r.returncode} stderr={r.stderr.strip()[-400:]!r}")

def g_rubric(g, text):
    """{name:..., criteria:[...]}  -- deferred to Claude; see scripts/grade_rubrics.py."""
    return dict(score=None, passed=None, pending=True, rubric_name=g.get("name"),
                criteria=list(g["criteria"]), notes="awaiting rubric grading")

# --------------------------------------------------------- code_quality ------
_CC_DECISION = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.IfExp, ast.ExceptHandler, ast.comprehension)
_NEST_BLOCKS = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith, ast.Try)

def _cc_proxy(fn):
    """McCabe-style cyclomatic-complexity proxy via ast: 1 + count of decision points."""
    cc = 1
    for n in ast.walk(fn):
        if isinstance(n, _CC_DECISION):
            cc += 1
        elif isinstance(n, ast.BoolOp):
            cc += len(n.values) - 1
        elif n.__class__.__name__ == "Match":            # py3.10+
            cc += len(getattr(n, "cases", []))
    return cc

def _nesting_depth(node):
    """Max depth of nested control-flow blocks within node."""
    def rec(n):
        best = 0
        for c in ast.iter_child_nodes(n):
            sub = rec(c) + (1 if isinstance(c, _NEST_BLOCKS) else 0)
            best = max(best, sub)
        return best
    return rec(node)

def g_code_quality(g, text):
    """Static-analysis quality score for a Python code response (NOT correctness — pair it with a
    `python` grader in a list for that). Config keys (all optional):
      fn_name           name of the function to inspect (else the first def)
      require_type_hints (default True)   require annotations on params + return
      require_docstring  (default True)   require a docstring on the target function
      max_cc            (default 8)       cyclomatic-complexity proxy ceiling
      max_nesting       (default 4)       nesting-depth ceiling
      max_body_lines    (default 40)      target-function source-line ceiling
      run_ruff          (default True)    run `ruff check` if ruff is on PATH
      ruff_select       (default "E,W,F,B,SIM,C4,RET,UP,PIE")
      ruff_ignore       (default "E501,UP035,UP006,UP007")  # don't punish line length / py-version typing nits
      pass_at           (default 0.7)
    Returns score = mean of the enabled checks (each 0..1); passed iff score >= pass_at.
    Stores `code_quality_checks` (per-check breakdown) and `smells` in the result."""
    code = extract_code(text)
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return dict(score=0.0, passed=False, pending=False, notes=f"code does not parse: {e}",
                    code_quality_checks={"parses": 0.0}, smells=["syntax-error"])
    checks = {}
    funcs = [n for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    fn_name = g.get("fn_name")
    target = next((f for f in funcs if f.name == fn_name), None) if fn_name else None
    if target is None:
        target = funcs[0] if funcs else None
    checks["has_target_fn"] = 1.0 if target is not None else 0.0
    if target is not None:
        if g.get("require_type_hints", True):
            a = target.args
            params = list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs)
            if a.vararg: params.append(a.vararg)
            if a.kwarg: params.append(a.kwarg)
            n_ann = sum(1 for p in params if p.annotation is not None) + (1 if target.returns is not None else 0)
            checks["type_hints"] = (n_ann / (len(params) + 1)) if params else (1.0 if target.returns is not None else 0.0)
        if g.get("require_docstring", True):
            checks["docstring"] = 1.0 if ast.get_docstring(target) else 0.0
        cc, max_cc = _cc_proxy(target), g.get("max_cc", 8)
        checks["complexity"] = 1.0 if cc <= max_cc else max(0.0, 1.0 - (cc - max_cc) / max_cc)
        nd, max_nd = _nesting_depth(target), g.get("max_nesting", 4)
        checks["nesting"] = 1.0 if nd <= max_nd else max(0.0, 1.0 - (nd - max_nd) / max_nd)
        body_span = (target.end_lineno or target.lineno) - target.lineno
        ds = target.body[0] if target.body else None      # don't count a (multi-line) docstring as "code"
        if isinstance(ds, ast.Expr) and isinstance(getattr(ds, "value", None), ast.Constant) and isinstance(ds.value.value, str):
            body_span -= (ds.end_lineno or ds.lineno) - ds.lineno + 1
        body_lines = max(0, body_span)
        max_bl = g.get("max_body_lines", 30)
        checks["length"] = 1.0 if body_lines <= max_bl else max(0.0, 1.0 - (body_lines - max_bl) / max_bl)
    smells = []
    for n in ast.walk(tree):
        if isinstance(n, ast.ExceptHandler) and n.type is None:
            smells.append("bare-except")
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for d in list(n.args.defaults) + list(n.args.kw_defaults):
                if isinstance(d, (ast.List, ast.Dict, ast.Set)):
                    smells.append("mutable-default-arg")
        elif isinstance(n, ast.Compare):
            for op, comp in zip(n.ops, n.comparators):
                if isinstance(op, (ast.Eq, ast.NotEq)) and isinstance(comp, ast.Constant) and comp.value is None:
                    smells.append("== None")
    checks["no_smells"] = 1.0 if not smells else max(0.0, 1.0 - 0.34 * len(smells))
    if g.get("run_ruff", True) and _RUFF:
        sel = g.get("ruff_select", "E,W,F,B,SIM,C4,RET,UP,PIE")
        ign = g.get("ruff_ignore", "E501,UP035,UP006,UP007")
        try:
            r = subprocess.run([_RUFF, "check", "--no-cache", "--quiet", "--output-format", "concise",
                                "--stdin-filename", "snippet.py", f"--select={sel}", f"--ignore={ign}", "-"],
                               input=code if code.endswith("\n") else code + "\n",
                               capture_output=True, text=True, timeout=20)
            nviol = len([l for l in r.stdout.splitlines() if l.strip()])
            checks["ruff"] = 1.0 if nviol == 0 else max(0.0, 1.0 - nviol / 4.0)
        except Exception:
            pass
    score = sum(checks.values()) / len(checks) if checks else 0.0
    failed = [k for k, v in checks.items() if v < 1.0]
    return dict(score=round(score, 4), passed=score >= g.get("pass_at", 0.7), pending=False,
                code_quality_checks={k: round(v, 3) for k, v in checks.items()},
                smells=sorted(set(smells)),
                notes="quality " + (", ".join(f"{k}={checks[k]:.2f}" for k in failed) if failed
                                    else f"all {len(checks)} checks clean"))

# ---------------------------------------------------------------- tool helpers ----
def _norm_tool_calls(rec):
    """Return [{name, args_obj, args_text}, ...] from a result rec. llama.cpp
    serves `arguments` as a JSON string; we also accept already-parsed shapes."""
    raw = (rec or {}).get("tool_calls") or []
    out = []
    for tc in raw:
        name = tc.get("name") or (tc.get("function") or {}).get("name")
        a = tc.get("arguments")
        if a is None:
            a = (tc.get("function") or {}).get("arguments")
        if isinstance(a, str):
            args_text = a
            try: args_obj = json.loads(a)
            except Exception: args_obj = None
        else:
            args_obj = a
            try: args_text = json.dumps(a)
            except Exception: args_text = str(a)
        out.append({"name": name, "args_obj": args_obj, "args_text": args_text})
    return out

def _args_ok(spec, args):
    """Per-arg constraints. Each entry in `spec` is:
        "*"                        arg must be present, any value
        {"equals": v}              exact value (string-normalized)
        {"in": [v1, ...]}          enum
        {"regex": "..."}           re.search on str(value), case-insensitive
        {"contains": "x"}          substring of str(value), case-insensitive
        {"type": "string|number|int|bool|array|object"}
    Combinations in one dict are AND-ed. Returns (ok, notes_list)."""
    notes, ok = [], True
    if not isinstance(args, dict):
        args = {}
    pytypes = {"string": str, "number": (int, float), "int": int,
               "bool": bool, "array": list, "object": dict}
    for k, c in spec.items():
        if k not in args:
            ok = False; notes.append(f"missing arg {k!r}"); continue
        v = args[k]
        if c == "*":
            continue
        if isinstance(c, dict):
            if "equals" in c and _norm(v) != _norm(c["equals"]):
                ok = False; notes.append(f"{k}={v!r}!={c['equals']!r}")
            if "in" in c and _norm(v) not in {_norm(x) for x in c["in"]}:
                ok = False; notes.append(f"{k}={v!r} not in {c['in']}")
            if "regex" in c and not re.search(c["regex"], str(v), re.I):
                ok = False; notes.append(f"{k}={v!r} no-match /{c['regex']}/")
            if "contains" in c and c["contains"].lower() not in str(v).lower():
                ok = False; notes.append(f"{k}={v!r} missing {c['contains']!r}")
            if "type" in c:
                # bool is a subclass of int -- guard explicitly
                tp = pytypes[c["type"]]
                if c["type"] == "int" and isinstance(v, bool):
                    ok = False; notes.append(f"{k} wrong type bool (want int)")
                elif c["type"] == "number" and isinstance(v, bool):
                    ok = False; notes.append(f"{k} wrong type bool (want number)")
                elif not isinstance(v, tp):
                    ok = False; notes.append(f"{k} wrong type {type(v).__name__}")
    return ok, notes

# ---------------------------------------------------------------- tool graders ----
def g_tool_call(g, text, rec):
    """{name, args, allow_extra_args:True, forbid_content:False}
    Pass iff exactly 1 tool call to `name`, args satisfy constraints,
    optionally no extra args / no content alongside."""
    calls = _norm_tool_calls(rec)
    if not calls:
        return _res(False, "no tool call emitted")
    if len(calls) != 1:
        return _res(False, f"expected 1 call, got {len(calls)}: {[c['name'] for c in calls]}")
    c = calls[0]
    if c["name"] != g["name"]:
        return _res(False, f"wrong fn: called {c['name']!r} want {g['name']!r}")
    ok, notes = _args_ok(g.get("args", {}), c["args_obj"] or {})
    if ok and not g.get("allow_extra_args", True):
        extra = set((c["args_obj"] or {}).keys()) - set(g.get("args", {}))
        if extra:
            ok = False; notes.append(f"extra args {sorted(extra)}")
    if ok and g.get("forbid_content") and (text or "").strip():
        ok = False; notes.append(f"unexpected content alongside call: {text[:60]!r}")
    return _res(ok, f"call={c['name']}({c['args_text'][:120]})  {'; '.join(notes) or 'ok'}")

def g_no_tool_call(g, text, rec):
    """{must_say_regex?:'...'}  Pass iff zero tool calls, and (optionally) the
    content matches must_say_regex. Use for 'should answer directly' or
    'should ask clarifying question'."""
    calls = _norm_tool_calls(rec)
    if calls:
        return _res(False, f"emitted {len(calls)} call(s): {[c['name'] for c in calls]}")
    pat = g.get("must_say_regex")
    if pat and not re.search(pat, text or "", re.I):
        return _res(False, f"no tool call (good) but content missing /{pat}/")
    return _res(True, "no tool call as required")

def g_tool_calls_set(g, text, rec):
    """{calls:[{name,args}], order:'any'|'strict', allow_extra_calls:False}
    Pass iff every required call (matched by name + arg constraints) was emitted.
    order='strict' enforces emission order. allow_extra_calls permits extras."""
    want = g["calls"]
    got = _norm_tool_calls(rec)
    if not got:
        return _res(False, "no tool calls emitted")
    used = [False] * len(got)
    matches = []
    for i, w in enumerate(want):
        chosen = -1
        for j, c in enumerate(got):
            if used[j] or c["name"] != w["name"]:
                continue
            ok, _ = _args_ok(w.get("args", {}), c["args_obj"] or {})
            if ok:
                chosen = j; used[j] = True; break
        if chosen < 0:
            return _res(False, f"required call#{i} {w['name']}({w.get('args')}) not found "
                               f"(got {[c['name'] for c in got]})")
        matches.append(chosen)
    if g.get("order", "any") == "strict" and matches != sorted(matches):
        return _res(False, f"calls present but order wrong: idx_seq={matches}")
    if not g.get("allow_extra_calls", False) and any(not u for u in used):
        extras = [got[j]["name"] for j, u in enumerate(used) if not u]
        return _res(False, f"unwanted extra calls: {extras}")
    return _res(True, f"matched {len(want)}/{len(want)} calls (order={g.get('order','any')})")

# --------------------------------------------------------- security review ---
def g_sec_review(g, text):
    """Programmatic floor for security_review prompts.

    Spec: {
      bugs:     [{cwe:[regex,...], location:[regex,...]}, ...]   # bugs the model should find
      decoys:   [[regex,...], ...]                                # CWE classes it must NOT flag
      must_say: [regex, ...]                                      # optional: any-match required
    }

    Per-bug score:
      1.0   if any `cwe` pattern matches AND any `location` pattern matches
      0.5   if only `cwe` matched (named but not pinpointed)
      0.0   if no `cwe` pattern matched (bug missed entirely)
      If `location` is omitted for a bug, only the CWE match is required (1.0 / 0.0).
    raw = mean of per-bug scores; raw=1.0 if `bugs` is empty (clean-code prompt).
    Each decoy false-positive (any of its patterns matched) subtracts 0.25 from raw.
    Final score floored at 0.0. Pass at score >= 0.6.

    All patterns are regex, evaluated case-insensitively against the response text.
    This is the programmatic half of the security_review hybrid; the rubric half
    (fix_soundness + explanation_clarity) is a separate `rubric` grader composed
    via the list-grader, same as `coding_quality`.
    """
    t = text or ""
    bugs = g.get("bugs", [])
    decoys = g.get("decoys", [])

    per_bug, notes = [], []
    for i, bug in enumerate(bugs):
        cwes = bug.get("cwe", [])
        locs = bug.get("location", [])
        named = any(re.search(p, t, re.I) for p in cwes)
        if not named:
            per_bug.append(0.0)
            notes.append(f"bug{i}({cwes[0] if cwes else '?'}):MISSED")
            continue
        if not locs:
            per_bug.append(1.0)
            notes.append(f"bug{i}({cwes[0]}):named(no-loc-req)")
            continue
        located = any(re.search(p, t, re.I) for p in locs)
        per_bug.append(1.0 if located else 0.5)
        notes.append(f"bug{i}({cwes[0]}):{'both' if located else 'named-not-located'}")

    raw = (sum(per_bug) / len(per_bug)) if per_bug else 1.0

    fp = 0
    for j, decoy in enumerate(decoys):
        if any(re.search(p, t, re.I) for p in decoy):
            fp += 1
            notes.append(f"decoy{j}({decoy[0] if decoy else '?'}):FP")
    score = max(0.0, raw - 0.25 * fp)

    # `must_say` is an optional any-match affirmation gate, used by clean-code
    # decoy prompts where flat CWE-name decoy regexes can't distinguish "model
    # claims X is present" from "model correctly says X is absent". If any of
    # the given patterns matches the response, the gate passes; otherwise the
    # model didn't clearly affirm cleanliness and score is set to 0.
    must_say = g.get("must_say") or []
    if must_say:
        affirmed = any(re.search(p, t, re.I) for p in must_say)
        if not affirmed:
            notes.append(f"must_say: none of {len(must_say)} affirmation patterns matched")
            score = 0.0
        else:
            notes.append("must_say:ok")

    return dict(score=round(score, 4), passed=score >= 0.6, pending=False,
                notes="; ".join(notes) or "ok")


GRADERS = {
    "contains": g_contains, "regex": g_regex, "regex_all": g_regex_all, "numeric": g_numeric,
    "word_count": g_word_count, "line_count": g_line_count, "bullets": g_bullets, "json": g_json,
    "forbid_char": g_forbid_char, "starts_ends": g_starts_ends, "python": g_python, "rubric": g_rubric,
    "count": g_count, "sentence_count": g_sentence_count, "paragraph_count": g_paragraph_count,
    "code_quality": g_code_quality,
    "tool_call": g_tool_call, "no_tool_call": g_no_tool_call, "tool_calls_set": g_tool_calls_set,
    "sec_review": g_sec_review,
}
