<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# R1–R4 and sphere-math deliverables — agent-safe format and context (Ethan)

**Purpose:** Fix deliverables so they do not trigger Cursor decoding/formatting loops. Invokes Ethan context: pipeline outputs are **structured (JSON per schema)**; spec tables are **reference only**; large run outputs are **not** used as full context. **Owner:** Ethan. **Refs:** [FINDINGS__Cursor_Decoding_Loop_2026-02-27.md](../docs/FINDINGS__Cursor_Decoding_Loop_2026-02-27.md), [AVOID__R1_R4_Spec_Until_Reasonable.md](../docs/AVOID__R1_R4_Spec_Until_Reasonable.md). **Date:** 2026-02-27.

---

## 1. Context (trigger summary)

Two triggers were isolated:

- **R1–R4 spec** (`docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md`): 183 markdown table rows. If the model is asked to “output in this format” or “fill this table,” it can get stuck in a decoding loop.
- **sphere_math_100_sentences** (~28k lines): Large, repetitive context can stress decoding; do not attach the full file as agent context.

---

## 2. Deliverable fix — R1–R4

**Canonical deliverable format for R1–R4 is JSON only.**

- Pipeline outputs **must** be **JSON** conforming to `schema/Unit.schema.json`, `schema/BookProfile.schema.json`, `schema/SI_metrics.schema.json`. Validate with Part C schemas; do not ask the model to emit or fill the **markdown tables** in the spec.
- The **tables in the spec are reference only** (definitions, thresholds, examples). Implementation and tooling produce **JSON**. No task shall require the model to “output in table format” or “fill the following table” from that spec.
- If a human or agent needs a table for reporting, **generate it from the JSON** (e.g. script or tool that reads JSON and prints markdown); the model is not asked to stream or repeat table rows.

**Rule:** R1–R4 deliverables = JSON per schema. No table-fill or table-format output from the spec in agent prompts.

---

## 3. Deliverable fix — sphere_math run outputs

**Do not attach the full 100-sentence run output as agent context.**

- `sphere_math_100_sentences.txt` (or `.json`) is **~28k lines**. Do **not** attach it as context in a single turn. Use one of:
  - **Programmatic access:** Run `sphere_rag.layers.run_sphere_math_100_sentences` with `--limit N` (e.g. `--limit 5`) to produce a small JSON sample for context, or
  - **Single-sentence run:** Use `sphere_rag.layers.run_sphere_math_values` for one input (small output), or
  - **Summary:** If you need aggregate or summary stats, produce a short summary artifact (e.g. counts, one row per sentence id) and attach that instead of the full 28k-line file.

**Rule:** For agent context, use `--limit N`, single-sentence run, or a summary artifact; never the full 100-sentence dump.

---

## 4. Summary for Grace and agents

| Artifact | Safe usage | Avoid |
|----------|------------|--------|
| R1–R4 spec | Reference only; implement from spec; output **JSON** per schema. | Do not ask model to “output in this format” or “fill this table.” |
| sphere_math_100_sentences (full) | Programmatic use; generate summaries or samples. | Do not attach full file as context. |
| R1–R4 pipeline outputs | JSON (Unit, BookProfile, SI_metrics). Optional **units.jsonl** (one unit per line) via `--out-units-jsonl` for streaming/safe context (e.g. `head -n 20 units.jsonl`). | No markdown table as the requested output format. |

These rules stand until the Grace task on the R1–R4 spec is re-reasoned and a safe approach is documented; they remain as the **deliverable and context fix** after that.

**SIGNED: Architecture (Ethan) | R1–R4 and sphere-math deliverable/context fix | 2026-02-27 | governance**
