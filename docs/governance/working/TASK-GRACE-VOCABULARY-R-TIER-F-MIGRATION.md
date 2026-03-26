<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
Grace-led team task — documentation vocabulary (R / Tier / F).
-->

# Task: Grace + team — vocabulary migration (R1–R10, Tier 0–11, F0–F10)

**Added:** 2026-03-22 · **Status:** OPEN — **plan + inventory only**; execution per phased PRs after Grace ACK.  
**Issued by:** Ethan (naming / semantics thread).  
**Purpose:** Remove overloaded **“layer”** and **L*** indices across docs and (later) code by adopting **distinct name families** and **semantic titles** for field phases, without breaking seals or public JSON until an explicit release gate.

**Normative vocabulary:** [LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md)  
**Inventory (files + terms, do not execute blindly):** [ETHAN-VOCABULARY-MIGRATION-INVENTORY.md](ETHAN-VOCABULARY-MIGRATION-INVENTORY.md)  
**Sequencing:** [ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md](ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md)

---

## Owners

| Role | Responsibility |
|------|----------------|
| **Grace** | ACK Phase 0 symbols; prioritize Tier A→E PRs; ensure triage report and AGENTS stay consistent; block public JSON / CLI renames without seal review |
| **Ethan (spec)** | Fill **F0–F10 semantic name** table in ETHAN Part A; resolve edge cases (H*, Part B) vs **R** narrative |
| **Docs / team** | Execute inventory file lists; open PRs per suggested split in inventory §8 |
| **Implementation** | Tier E: docstrings and user-visible strings first; **no** `layer_id` key changes without Phase 4 sign-off |

---

## Deliverables

1. **Phase 0 (merged):** Maintainer/Grace ACK on [LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md); ETHAN spec terminology box + **F*k*** semantic name column (draft from Part A).  
2. **Phase 1:** Tier A files in inventory — binding docs use **R / Tier / F**; [GRACE_TRIAGE_REPORT.md](../../specs/triage/GRACE_TRIAGE_REPORT.md) updated with a **Vocabulary** subsection (status + top gaps).  
3. **Phases 2–4:** Per [ETHAN-VOCABULARY-MIGRATION-INVENTORY.md](ETHAN-VOCABULARY-MIGRATION-INVENTORY.md) §8.

---

## Hard rules

1. **F*k* ≠ R*k*.** Field phase index does not imply metric cascade stage index.  
2. **No breaking JSON / OpenAPI / seal** in the same PR as prose-only migration (split per inventory).  
3. **LEVEL*** architecture spec filenames are not the same as **Tier*** — disambiguate in edits (see inventory Tier D).  
4. **Dynamics implementation code** may keep internal “L6/L7” comments until Ethan supplies a **crosswalk table** (F ↔ internal step names).

---

## Handoff line

> **Grace + team:** Please take ownership of [ETHAN-VOCABULARY-MIGRATION-INVENTORY.md](ETHAN-VOCABULARY-MIGRATION-INVENTORY.md). Run Phase 0 ACK, then Tier A PRs, extend **GRACE_TRIAGE_REPORT** with vocabulary status, and schedule Tier B–E per capacity. **Ethan** to supply **F0–F10 semantic names** anchored to Part A sections.

---

*Grace task — R / Tier / F migration (documentation-first).*
