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
| 5 | `run_output_e2e_sphere_math_100.json` | Sphere math on first N calibration sentences (limit 3) |
| 6 | `run_output_e2e_domain_metrics.json` | Domain metrics stage: 6 primitives, 35 derived, 41-signal fingerprint, vectorHash |
| 7 | `run_output_e2e_session_kme.json` | Session NLP → KME + TRIZ (`run_session_kme_pipeline`) |
| 8 | `run_output_e2e_triz_complete.json` | TRIZ complete report (`run_triz_analysis_complete`; CSV as byte lengths) |
| 9 | `run_output_e2e_session_topology.json` | Clinical session topology (segmented windows; segments may be truncated) |

## Absolute paths (default run)

Paths follow `$REPO/assets/artifacts/e2e/run_output_e2e_*.json` for basenames 1–9 above.

## Verify

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py -v
```
