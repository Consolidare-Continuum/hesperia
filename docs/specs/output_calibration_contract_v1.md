# Output calibration contract v1 (TFP multi-plane bundle)

**Status:** v1 — binding for **numeric semantics** and **presentation separation** across planes A/B/C and clinical extensions.  
**Scope:** Structural (L1–L9 + multiscale), session stages, hex microstructure, DLCR, sealed stack, `analyze()`, KME, TRIZ, topology.

## 1. Shared scale policy

| Kind | Storage | Range / rule |
|------|---------|----------------|
| Probability / confidence | float | `[0, 1]` |
| Normalized activation | float | `[0, 1]` unless raw mass is documented |
| Percentage | **not** stored | Derive only at presentation (`value * 100`, label `%`) |
| Count | int | Non-negative integers |
| Energy / raw mass | float | May be unbounded; if only normalized is operational, store **`value_norm`** and optional **`value_raw`** |

## 2. Per-field metadata (registry)

Each public or cross-plane field SHOULD have an entry in `assets/config/output_metric_registry_v1.json`:

- `semantic_type`: e.g. `probability`, `normalized_mass`, `count`, `index`, `energy`
- `range_min`, `range_max`
- `null_policy`: `forbidden` | `omit` | `explicit_null`
- `zero_meaning`: `no_signal` | `floor` | `invalid` | `context_dependent`
- `display_precision`: int (decimal places for UI)
- `sortable`: bool
- `comparable_across_runs`: bool (stable normalization)

## 3. Computational vs presentation

- **Computational:** full-precision values in execution_flow JSON (subject to existing E2E rounding).
- **UI-friendly:** `display_value` + `band_label` produced by the readout layer (`hesperia.engine.output_readout`) from `assets/config/metric_bands_v1.json`.
- **Diagnostic raw:** optional `diagnostics.*`, `interpretability_trace`, `calibration_status` — not part of public product schema unless explicitly projected.

## 4. Migration — inconsistent legacy fields

| Artifact / field | Issue | v1 handling |
|------------------|-------|-------------|
| Structural L1 with zero markers | Dead zeros vs analyze | `calibration_status` + optional `CALIBRATION_FALLBACK_USED` on L1 |
| Sealed hex sample slice | Sub-epsilon values shown as 0 | Prefer `total_mass` + registry `display_precision`; consider scientific notation in diagnostic channel only |
| Trust / HSPR | Mixed scales | Registry: treat HSPR as `[0,1]` index; map L7 tags separately |
| Stage `areas_top` | NLP session, not lexicon | Registry `comparable_across_runs: false` vs structural areas unless explicitly aligned |
| KME primitives | Mixed units | Each primitive row in registry |

## 5. Implementation plan (5-task pack)

1. **Registry + spec** (this doc + JSON) — source of truth for tools and UI.
2. **Dead-zero fixes** — hex line search + sealed flags + L1 fallback (done — see ETHAN Task 2 note).
3. **Harness** — `tools/tfp_calibration_audit.py` → `10_calibration_audit.json`.
4. **Readout** — bands + formatter component; no metric in UI without band policy.
5. **Profiles** — `assets/config/calibration_profiles_v1.yaml` + deterministic replay from fixed intermediates (future hardening).

## 6. Related paths

- Root cause: `docs/governance/working/ETHAN-CALIBRATION-PACK-TASK2-ROOT-CAUSE.md`
- Metric bands: `assets/config/metric_bands_v1.json`
- Profiles: `assets/config/calibration_profiles_v1.json`
- Audit tool: `tools/tfp_calibration_audit.py`
- **Tasks 6–10 (operational discipline):** goldset `tests/gold/tfp_calibration_goldset_v1.json` + `tools/run_tfp_calibration_goldset.py`; anomalies `docs/specs/output_anomaly_taxonomy_v1.md`; trace `docs/specs/output_metric_provenance_v1.md`; schemas `schemas/tfp_bundle/` + `tools/validate_tfp_bundle_schemas.py`; gate `docs/specs/calibration_release_gate_v1.md` + `tools/calibration_release_gate.py`.
- **Gena one-shot:** `tools/gena_tfp_bundle_run.py` runs the file execution_flow then audit, schema check, and gate (see `docs/governance/working/ETHAN-TFP-RUNNABLE-DICT-WIRING.md` §3a).
