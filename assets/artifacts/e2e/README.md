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
| `run_output_e2e_sphere_math_100.json` | Sphere math on first N calibration sentences |

**Regenerate all:**

```bash
python3 -m runtime.pipeline.run_e2e_all
```

Optional: `--out-dir PATH` to write elsewhere; default: `assets/artifacts/e2e/`.

**E2E tests:** `pytest tests/test_e2e_flows.py -v`
