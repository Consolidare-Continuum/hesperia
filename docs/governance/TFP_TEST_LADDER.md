# TFP test ladder L0–L3 (TFP-GATE-B2)

| Level | Scope | Enforcement |
|-------|--------|-------------|
| **L0** | Schema + determinism | `sealed-runtime-gate.yml` integrity list; `tests/test_env_determinism.py`; `validate_version_consistency.py` |
| **L1** | Length / dominance-style invariants | CD executor tests `tests/concept_dictionary/test_cd_executor.py`; HC / dominance paths in existing HC-WAVE1 deliverables |
| **L2** | CI fixture, no `research/`, bounded runtime | `tools/run_b_cd_wave_after_a.sh`, `tools/run_tfp_phase_c_smoke.sh`; pytest slices in `TFP_RELEASE_PYTEST_BAR.md` |
| **L3** | Optional API parity | Deferred to product API tasks when TFP endpoints are in release scope |

## Conflict integrity (release dimension)

Treat **contradiction integrity** as a first-class release axis alongside schema/determinism: inspect artifact `99_tfp_bundle_inspect.json` (when produced) must record `promotion_conflict_verdict`, `conflict_integrity_score`, and per-gate `release_conflict_gates`. See `TFP_RELEASE_PYTEST_BAR.md` (Conflict Integrity Gates) and `tests/triz/test_conflict_release_gating.py`.

---

`SIGNED: Cursor (workflow) | TFP-GATE-B2 | 2026-03-28`
