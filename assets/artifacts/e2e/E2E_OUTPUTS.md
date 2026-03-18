<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
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
| 2 | `run_output_e2e_l1_l9.json` | L1–L9 + USF + interpretation_metrics + prolog_logic + guards + diagnostics |
| 3 | `run_output_e2e_r1_r4.json` | R1–R4 pipeline; units + book_profile |
| 4 | `run_output_e2e_sphere_math_values.json` | Sphere math (L1–L9 values only) for default text |
| 5 | `run_output_e2e_sphere_math_100.json` | Sphere math on first **3** calibration sentences (smoke) |
| 5b | `run_output_e2e_calibration_100_structural.json` | Full batch structural rows per sentence (default **100**; `HESPERIA_E2E_CALIBRATION_BATCH_N`) |
| 5c | `run_output_e2e_calibration_100_summary.json` | Histograms + means for that batch |
| 6 | `run_output_e2e_domain_metrics.json` | Domain metrics stage: 6 primitives, 35 derived, 41-signal fingerprint, vectorHash |
| 7 | `run_output_e2e_session_kme.json` | Session NLP → KME + TRIZ (`run_session_kme_pipeline`) |
| 8 | `run_output_e2e_triz_complete.json` | TRIZ complete report (`run_triz_analysis_complete`; CSV as byte lengths) |
| 9 | `run_output_e2e_session_topology.json` | Clinical session topology (segmented windows; segments may be truncated) |
| 10 | `run_output_e2e_tfp_smoke.json` | TFP smoke: structural batch + session stages + speaker-aware dialogue (`detect_tfp_stage`) |
| 11 | `run_output_e2e_capability_matrix.json` | Gena sweep + **KME run_document/run_corpus**, **batch_runner**, **mvp_acceptance**, **experiment_runner**; multiscale if `HESPERIA_E2E_MULTISCALE=1` |
| 12 | `run_output_e2e_field_dynamics.json` | With `HESPERIA_FIELD_DYNAMICS=1`: **`PHASE3`**, **`PHASE2`**, **`dynamics_stack`**, etc. |

## Absolute paths (default run)

Paths under `$REPO/assets/artifacts/e2e/` — **13** base JSON files (incl. calibration 5b–5c); field_dynamics = 14th when flag set.

## Verify

`test_e2e_run_e2e_all_produces_all_artifacts` runs **with `HESPERIA_FIELD_DYNAMICS=1`** and asserts **14** files (13 base + field_dynamics); calibration batch uses `HESPERIA_E2E_CALIBRATION_BATCH_N=5` in CI.

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py tests/nlp/test_role_direction_and_temporal.py::test_detect_tfp_stage -v
```
