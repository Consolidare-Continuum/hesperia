<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# E2E artifacts

Planned outputs from the unified e2e run. No calibration of results; existence only.

| File | Flow |
|------|------|
| `run_output_e2e_sentence.json` | analyze (6-key + attribution + dict_b + R1–R4) |
| `run_output_e2e_l1_l9.json` | L1–L9 execution_flow (layer contract) |
| `run_output_e2e_r1_r4.json` | R1–R4 execution_flow (units + book_profile) |
| `run_output_e2e_sphere_math_values.json` | Sphere math values (L1–L9 single text) |
| `run_output_e2e_sphere_math_100.json` | Sphere math on first **3** calibration sentences |
| `run_output_e2e_calibration_100_structural.json` | Calibration batch structural (default 100 sentences) |
| `run_output_e2e_calibration_100_summary.json` | Calibration batch summary stats |
| `run_output_e2e_domain_metrics.json` | Structural execution_flow + KME domain metrics |
| `run_output_e2e_session_kme.json` | Session → KME + TRIZ |
| `run_output_e2e_triz_complete.json` | TRIZ full stack (API parity) |
| `run_output_e2e_session_topology.json` | Clinical session topology |
| `run_output_e2e_tfp_smoke.json` | TFP smoke: batch structural + stages + speaker-aware + session hex microstructure |
| `run_output_e2e_hex_microstructure_tfp.json` | Full hex microstructure bundle (primary text + TFP sessions) |
| `run_output_e2e_sealed_multiscale.json` | **v0.5 sealed stack:** hex → family/area → product_signals → **HSPR** |
| `run_output_e2e_capability_matrix.json` | Cross-stack capability sweep + **semantic_field_and_hci** |
| `run_output_e2e_semantic_field.json` | Ontology → matrix_builders → semantic field (`runtime/configs/semantic_field_ontology_example.json`) |
| `run_output_e2e_field_calibration.json` | HCI grid (mini); also `_best.json`, `_topk.json` |
| `run_output_e2e_field_dynamics.json` | With `HESPERIA_FIELD_DYNAMICS=1`: Ethan phases + **semantic_field_v1** |

**Baseline count:** **19** JSON files (+ optional `run_output_e2e_field_dynamics.json`; + optional `run_output_e2e_dlcr.json` when `HESPERIA_E2E_DLCR=1`). **Order:** `docs/E2E_RUN_ORDER.md` · **Manifest:** `E2E_OUTPUTS.md`

**Regenerate all:**

```bash
python3 -m runtime.execution_flow.run_e2e_all
```

Optional: `--out-dir PATH` to write elsewhere; default: `assets/artifacts/e2e/`.

**E2E tests:** `pytest tests/test_e2e_flows.py -v`
