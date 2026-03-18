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
| `run_output_e2e_l1_l9.json` | L1–L9 pipeline (layer contract) |
| `run_output_e2e_r1_r4.json` | R1–R4 pipeline (units + book_profile) |
| `run_output_e2e_sphere_math_values.json` | Sphere math values (L1–L9 single text) |
| `run_output_e2e_sphere_math_100.json` | Sphere math on first **3** calibration sentences |
| `run_output_e2e_calibration_100_structural.json` | Calibration batch structural (default 100 sentences) |
| `run_output_e2e_calibration_100_summary.json` | Calibration batch summary stats |
| `run_output_e2e_domain_metrics.json` | Structural pipeline + KME domain metrics |
| `run_output_e2e_session_kme.json` | Session → KME + TRIZ |
| `run_output_e2e_triz_complete.json` | TRIZ full stack (API parity) |
| `run_output_e2e_session_topology.json` | Clinical session topology |
| `run_output_e2e_tfp_smoke.json` | TFP smoke: batch structural + `detect_tfp_stage` + speaker-aware |
| `run_output_e2e_capability_matrix.json` | Cross-stack capability sweep (see `docs/E2E_RUN_ORDER.md`) |

**Order:** `docs/E2E_RUN_ORDER.md`

**Regenerate all:**

```bash
python3 -m runtime.pipeline.run_e2e_all
```

Optional: `--out-dir PATH` to write elsewhere; default: `assets/artifacts/e2e/`.

**E2E tests:** `pytest tests/test_e2e_flows.py -v`
