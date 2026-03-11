# Historical reference (pre-refactor)

# HESPERIA v0.6 — Operational spec

**Status:** Operational. Version 0.6. All active code and artifacts use v0.6 naming.

## 1. Objective

- **Attribution:** Dict A (288-field) → sentence aggregation → Dict B (structural coherence, area projection, diffusion) → 6-key + extended.
- **Contract:** Same 6 keys; extended includes `dict_b` (exclusion_conflict_energy, coherence_index, entropy_area).
- **Mode:** Default `HESPERIA_ATTRIBUTION_MODE=v06`; fallback `sparse`.

## 2. Paths and artifacts

| Artifact | Purpose |
|----------|--------|
| `assets/v06/dict_a_v06.jsonl` | Dict A token → topk + metrics. |
| `assets/v06/family_prior_v06.json` | Family prior. |
| `assets/v06/dict_a_v06.sha256` | Integrity. |
| `hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.json` | Surface → lemma. |
| `sphere_rag/analyze.py` | Entry: `analyze(text, ...)`. |
| `sphere_rag/attribution.py` | Dict A load, sentence vector, run_attribution_pipeline. |
| `sphere_rag/dict_b.py` | run_dict_b_pipeline: structural layer. |

## 3. Scripts

| Script | Purpose |
|--------|--------|
| `scripts/run_calibration_v06.py` | Full spec run 100 sentences. |
| `scripts/verify_v06_operational.py` | Operational checks. |
| `scripts/calibration_metrics_v06.py` | Per-domain metrics. |
| `sphere_rag/build_dict_a.py` | Build Dict A. |
| `sphere_rag/validate_dict_a.py` | Validate artifact. |
| `sphere_rag/audit_dict_a_runtime.py` | Runtime audit. |

## 4. API

- **0.6.0.** POST /hesperia/analyze; assets at `assets/v06`.

## 5. Fresh start

From v0.6 onward: fresh thinking and math wiring process. See [NOTE__v0_6_fresh_start.md](NOTE__v0_6_fresh_start.md).
