<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# E2E pre-freeze output files

Single manifest of all outputs produced by the canonical E2E run.  
**Entrypoint:** `python3 -m runtime.pipeline.run_e2e_all [--out-dir path]`  
**Default out-dir:** `assets/artifacts/e2e/`  
**Run order (modules, dependencies):** `docs/E2E_RUN_ORDER.md`

## Output files (all under `assets/artifacts/e2e/`)

| # | Basename | Description |
|---|----------|-------------|
| 1 | `run_output_e2e_sentence.json` | Analyze (6-key + attribution + dict_b + R1–R4); result + extended |
| 2 | `run_output_e2e_l1_l9.json` | L1–L9 + USF + … + **`narrative_microstructure_e2e`** (hex maps + Option A + TFP slice) |
| 3 | `run_output_e2e_r1_r4.json` | R1–R4 pipeline; units + book_profile |
| 4 | `run_output_e2e_sphere_math_values.json` | Sphere math (L1–L9 values only) for default text |
| 5 | `run_output_e2e_sphere_math_100.json` | Sphere math on first **3** calibration sentences (smoke) |
| 5b | `run_output_e2e_calibration_100_structural.json` | Full batch structural rows per sentence (default **100**; `HESPERIA_E2E_CALIBRATION_BATCH_N`) |
| 5c | `run_output_e2e_calibration_100_summary.json` | Histograms + means for that batch |
| 6 | `run_output_e2e_domain_metrics.json` | Domain metrics: 6 primitives, 35 derived, 41-signal fingerprint, vectorHash |
| 7 | `run_output_e2e_session_kme.json` | Session NLP → KME + TRIZ (`run_session_kme_pipeline`) |
| 8 | `run_output_e2e_triz_complete.json` | TRIZ complete report (`run_triz_analysis_complete`; CSV as byte lengths) |
| 9 | `run_output_e2e_session_topology.json` | Clinical session topology (segmented windows; segments may be truncated) |
| 10 | `run_output_e2e_tfp_smoke.json` | TFP smoke: structural batch + session stages + speaker-aware + **session_hex_microstructure_tfp** |
| 10b | `run_output_e2e_hex_microstructure_tfp.json` | Hex microstructure + Option A closure + TFP provenance (primary text + smoke sessions) |
| 10c | `run_output_e2e_sealed_multiscale.json` | **Sealed multiscale:** hex map sample, **family_activation_vector**, **area_activation_vector**, **hotspot_map**, contradiction/propagation/density, **innovation_index**, **hspr_index** |
| 11 | `run_output_e2e_capability_matrix.json` | Gena sweep + **semantic_field_and_hci**; KME run_document/run_corpus, batch_runner, mvp_acceptance, experiment_runner; multiscale if `HESPERIA_E2E_MULTISCALE=1` |
| 11a | `run_output_e2e_semantic_field.json` | **Semantic field:** ontology → matrix_builders → equations (see `runtime/configs/semantic_field_ontology_example.json`) |
| 11b–d | `run_output_e2e_field_calibration.json` (+ `_best`, `_topk`) | **HCI calibration** mini-grid (ontology-derived matrices) |
| 12 | `run_output_e2e_field_dynamics.json` | With `HESPERIA_FIELD_DYNAMICS=1`: Ethan phases + optional **`semantic_field_v1`** |

## Counts

**19** base JSON files (incl. **10c** sealed multiscale); **field_dynamics** = **20th** when flag set.

## Full encompassing pipe (`run_e2e_full_stack`)

**Entrypoint:** `python3 -m runtime.pipeline.run_e2e_full_stack [--out-dir path]` (default `assets/artifacts/e2e_full_stack/`)  
**Shell:** `./tools/e2e_full_deliverables.sh` → same orchestrator.

Writes **all rows above** (same basenames) **plus:**

| | Basename | Description |
|---|----------|-------------|
| P | `run_output_e2e_full_product_surface.json` | `run_structural_analysis` → schema guard (product-shaped JSON) |
| M | `run_output_e2e_full_stack_manifest.json` | Index: every artifact `path`, `bytes`, `sha256`; `system_seal` report; `steps`; `ok` |

Physics validation + system seal run as part of the pipe (unless `--skip-physics` / `--skip-seal`). See `docs/E2E_RUN_ORDER.md`.

## Verify

`test_e2e_run_e2e_all_produces_all_artifacts` runs **with `HESPERIA_FIELD_DYNAMICS=1`** and asserts **20** files; calibration batch uses `HESPERIA_E2E_CALIBRATION_BATCH_N=5` in CI.

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py -v
```
