# Grace triage — invoke Ethan on main Hesperia (no TFP)

**Date:** 2026-03-26  
**Task ID:** TASK-2026-GRACE-ETHAN-HESPERIA-MAINLINE  
**Owner:** Ethan  
**Status:** CLOSED for slice ML-07 (2026-03-26); further Ethan mainline work needs a new `active.md` row.

## Intent

**Engine repo (host):** `/data/hesperia/hesperia` — paths below are relative to that root.

Operator: **Ethan works on mainline Hesperia**. **Do not touch TFP** calibration / dict wiring / clinical experimental surfaces while this assignment stands.

## In scope (mainline)

- Sealed product path: `hesperia/engine`, `hesperia/nlp` (non-TFP-only flows), `assets/data/engine_dynamics_v060/` **mainline** assets (`dict_b_seed.jsonl`, `semantic_dynamics/area_inhibition_matrix_main_v1.json`, etc.).
- Proceed lists: `hesperia` engine repo — `docs/governance/working/ETHAN-OPEN-WORKFLOW-PROCEED.md` — pick items that are **not** TFP-only.
- `docs/CURSOR_OPEN_WORKFLOW.md` §2: **post-A.6**, **post-options** (non-TFP sub-rows), mainline docs (e.g. ML-07 speaker-aware prose) — **not** the “TFP runnable” row.
- Mainline policy: `docs/governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md`.

## Out of scope (do not modify / defer)

- `dict_b_tfp.jsonl`, `tfp/`, `HESPERIA_TFP_DLCR`, TFP file pipeline clinical stages.
- `docs/governance/working/ETHAN-TFP-RUNNABLE-DICT-WIRING.md` — leave to separate calibration coordination.
- `research/` surfaces tied to dict calibration — respect any Grace boundary doc in-repo (`GRACE-WORKFLOW-BOUNDARY*` if present).
- Semantic dynamics: default **`build_h_total_concepts`** mainline inputs only; **`--use-tfp-inputs`** is **off** unless Grace reopens TFP.

## Handoff

- Code implementation after Ethan specs → **Gena** as usual.
- Infra/deploy → **Abelard**.

## Done criteria

Ethan (or Cursor as Ethan context) marks **DONE** in `active.md` when mainline next slice is specified or delivered per one coherent outcome (doc update + scoped task list, or merged mainline change without TFP edits).

---

`SIGNED: Triage (Grace) | hesperia mainline invoke | 2026-03-26 | operator: no TFP touch`
