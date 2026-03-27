# MODEL_CARD — CD pipeline position (v1.0)

**Frozen fragment** for full `docs/MODEL_CARD.md` merge.

## Layer chain (locked)

`A` (lexical evidence) → `B` (concept identity / resolver) → **`CD`** (Concept Dictionary: behavior + constraints) → **`C_agg`** (families / areas / hex aggregation) → **Topology** (session / segments).

**After A is green:** **`B` before `CD`** — CD rows reference `concept_id` from B; do not author CD as a parallel concept source ahead of B. Rationale: `docs/governance/working/ETHAN-DICT-LAYER-ORDER-AFTER-A.md`.

## CD role

- Deterministic operational registry: **no lexical strings** in CD rows.
- **Phase 1** (MVP): `type`, `activation`, `requires` / `excludes`, `structure.primary_area`.
- **Phase 2+**: `effects`, `validation` thresholds, `co_occurs` (soft — formula in `CO_OCCURS_MATH_PHASE2.md`).
- Default row `*` when a B concept has no explicit CD entry.

## Runtime wiring

- Module: `hesperia.engine.concept_dictionary`.
- Pipeline: `hesperia/engine/lexical_concept/pipeline.py` after `_stabilize_concept_weights`, before `_post_hex_concept_feedback`.
- **Opt-in**: set `HESPERIA_CD_ENABLED=1` (and optionally `HESPERIA_CD_JSONL`, `HESPERIA_CD_PHASE`).
- **Disable**: `HESPERIA_CD_DISABLE=1`.

## Calibration

Version `concept_dict_cd.jsonl` with engine release; regression: `tests/concept_dictionary/test_cd_executor.py` (double-run equality).

SIGNED: Architect (Ethan) | MODEL_CARD CD fragment | 2026-03-28 | Hesperia repo (B-before-CD note added)
