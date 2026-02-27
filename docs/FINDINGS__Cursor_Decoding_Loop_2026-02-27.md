# Cursor decoding loop — repo audit (2026-02-27)

**Run ID (archived):** `4a32fa6e-3a4e-461a-b110-6d405c3515dd`  
**Symptom:** Repeated `begin_of_sentence | >%<` pattern; model stuck in decoding/formatting loop (~22s).  
**Source:** cursor.com feedback — "this is not normal behavior."

---

## Audit scope

Searched the repo for anything that could trigger a malformed structured-output constraint, extension state, or format instruction leading to that loop.

---

## Findings

### 1. No literal trigger in repo

- **Grep:** No occurrences of `begin_of_sentence`, `>%<`, or `| %` in the codebase. Those tokens are consistent with **Cursor/model-internal** (e.g. BOS or special formatting tokens), not with project text.
- **Conclusion:** The loop is not caused by a literal string in specs, code, or config.

### 2. Project Cursor config

- **`.cursor/`** exists but is **empty** (no rules, no `.cursorrules`).
- **Conclusion:** No project-level rule or instruction in this repo that could inject a bad output format.

### 3. Plausible context triggers (if that run had these in context)

| Trigger | Location | Why it could matter |
|--------|----------|----------------------|
| **R1–R4 spec markdown tables** | `docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md` | 183 table rows (`| ... |`), 1234 lines. If the model was asked to "output in this format" or "fill this table," it may have tried to emit table rows under a constraint and gotten stuck (e.g. repeated line start). |
| **Very large output file** | `sphere_math_100_sentences.txt` (~28k lines) | If this was in context, repetitive structure + size could stress decoding or context handling. |
| **Strict JSON schemas** | `schema/Unit.schema.json`, `schema/SI_metrics.schema.json` | If the run used structured output (e.g. "output valid Unit JSON") and Cursor applied schema-based constraints, a bug in that path could cause retry/loop behavior. |

### 4. Code and run scripts

- **`sphere_rag/layers/layer_1.py`** (modified): Normal Python; no format strings or instructions that could cause the loop.
- **`run_sphere_math_100_sentences.py`**, **`run_sphere_math_values.py`**: CLI scripts; no prompt or output-format injection.
- **AGENTS.md**: Standard guidelines; no special delimiters or output templates.

---

### 5. Large jsonl run outputs (same context rule)

- **calibration_run.jsonl**, **dict_a_v06.jsonl**, and any **per-line run output** (one JSON object per line) can become very large. Same principle as the 28k-line sphere_math file: **do not attach full jsonl run output as agent context** in a single turn.
- **Rule:** For agent context, use a **bounded sample** (e.g. first N lines), a **summary artifact**, or **streaming/head** (e.g. `head -n 20 file.jsonl`). Prefer pipeline options like `--limit N` or optional **jsonl output** (one unit per line) so consumers can read incrementally without loading a single huge JSON.

---

## Conclusion

- **No smoking gun in the repo.** The loop is consistent with a **Cursor-side** issue (decoding, structured output, or extension state), not with HESPERIA docs or code.
- **Isolated trigger:** R1–R4 spec + **Grace task on that spec** (implement/validate/produce from spec). Avoid until re-reasoning is done.

## Isolation and avoidance (in place)

- **AGENTS.md §5a** documents the isolated trigger and avoidance rules:
  - Do not use `docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md` as primary context for agent tasks.
  - Do not attempt to complete or extend the Grace task on the R1–R4 spec; defer to human re-reasoning.
  - Prefer not attaching the R1–R4 spec or `sphere_math_100_sentences.txt` with structured-output/table-format requests.
- **Lift:** Remove or relax §5a when the Grace task on the spec has been re-reasoned and a safe approach is documented.

## Deliverable fix (Ethan)

**Governance:** [governance/ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md](../governance/ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md) defines the fix:

- **R1–R4:** Canonical deliverable format = **JSON per schema** (Unit, BookProfile, SI_metrics). Do not ask the model to “output in this format” or “fill this table”; spec tables are reference only.
- **sphere_math_100_sentences:** Do not attach the full ~28k-line output as context. Use `--limit N` (e.g. `python3 -m sphere_rag.layers.run_sphere_math_100_sentences --limit 5`), single-sentence run (`run_sphere_math_values`), or a summary artifact.

---

## Report reference

When reporting to Cursor, include:

- **Run ID:** `4a32fa6e-3a4e-461a-b110-6d405c3515dd`
- **Repo:** HESPERIA (this workspace)
- **This audit:** `docs/FINDINGS__Cursor_Decoding_Loop_2026-02-27.md`
