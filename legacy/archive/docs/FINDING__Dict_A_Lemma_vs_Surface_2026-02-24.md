<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Finding: Dict A keys are structural IDs; tokenizer strips underscore — natural text cannot match

**Date**: 2026-02-24
**Status**: Root cause confirmed

---

## 1. JSON shape (answer)

The frozen Dict A is the **first** form:

```json
{
  "altruism_1_10": [ { "side_id": 0, "weight": 0.4, "map_code": "structural_label_slug_v0413" } ],
  "gooaltruismfocus_1_0": [ ... ],
  ...
}
```

So: **keys are structural identifiers** (`lemma_slug_index`), not user-facing words like `"altruism"`. There is no key `"altruism"` in Dict A.

**File**: `CLIENTS/hesperia/hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json`

---

## 2. Does tokenization strip underscore?

**Yes.** Underscore is in the punctuation set and is stripped.

**Code**: `CLIENTS/hesperia/sphere_rag/attribution_v033.py`

```python
# Line 59-61
_PUNCT = re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
_STRIP_PUNCT_RE = re.compile(f"[{_PUNCT}]")

# Line 80-86: tokenize = split on whitespace, then strip punctuation from each token
def tokenize(normalized: str) -> list[str]:
    tokens = normalized.split()
    return [_STRIP_PUNCT_RE.sub("", t).strip() for t in tokens if _STRIP_PUNCT_RE.sub("", t).strip()]
```

So:

- User input `{"text":"altruism_1_10"}` → one token after normalize/tokenize → `_STRIP_PUNCT_RE.sub("", "altruism_1_10")` → **`"altruism110"`** (underscores removed).
- Dict A key is `"altruism_1_10"`.
- Lookup: `dict_a["altruism110"]` → **not in dict** → no match.

So even if the user sent the structured key literally, the current tokenizer would break the match.

---

## 3. Runtime lookup

- **Dict A** is loaded by `load_dict_a_v033()` and stored as `lemma -> { "familyGlobal", "altitude" }` with keys **unchanged** from the JSON (only `k.strip().lower()`), i.e. `"altruism_1_10"`, `"gooaltruismfocus_1_0"`, etc.
- **Attribution** in `attribute()` does exact lookup: `dict_a[t]` where `t` is the token (after tokenize).
- So the runtime expects the **exact key** to appear in the token stream. No mapping from surface word `"altruism"` to key `"altruism_1_10"`.

---

## 4. Conclusion

1. **Underscore stripped** → structured key `altruism_1_10` becomes `altruism110` → never matches.
2. **Dict keys are structural**, not surface: no `"altruism"` key; only `"altruism_1_10"`. So natural language token "altruism" has nothing to match even if `_` were not stripped.
3. **The freeze step stored internal structural identifiers as the lemma keys.** The runtime lexical gate does exact key match. So natural text never matches; the engine is not lexically usable for user-facing words until either:
   - Dict A (or a separate surface layer) exposes **surface lemmas** (e.g. `"altruism"`) and the runtime maps surface → structural key, or
   - Dict A keys are changed to surface forms and structural ID is carried inside the value (breaking change vs current freeze).

---

## 5. Immediate test (user request)

In GPT Builder, call:

```json
{"text":"altruism_1_10"}
```

- If **200** → dictionary expects full structured key and tokenizer is not stripping `_` in that path (or input is not tokenized the same way).
- If **400** → consistent with: underscore stripped (→ `altruism110`), or Dict A not loaded, or lookup expects different format.

Given the code above, **400 is expected**: token becomes `altruism110`, no key in dict.

---

## 6. Recommended direction

- **Short term**: Document that the current API expects structural keys (or accept 400 for natural language until a surface layer exists). Optionally add a test in the harness: `{"text":"altruism_1_10"}` with expected 400 until fixed.
- **Design**: Introduce a **surface lemma layer**: e.g. Dict A entries carry both structural key and one or more surface forms; tokenize matches surface form and resolves to structural key for attribution. Or a separate B0-style map: surface token → structural key (or side_id/familyGlobal). Then freeze Dict A (or a derived artifact) so that **user-facing tokens** (e.g. `"altruism"`) are what the runtime looks up.

---

**SIGNED: Cursor | repo context | 2026-02-24 | finding**
