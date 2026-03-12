<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# HESPERIA v0.4.0 — Calibration

- **Spec:** [docs/CALIBRATION_RUN_SPEC_v0_4_0.md](../docs/CALIBRATION_RUN_SPEC_v0_4_0.md)
- **Dataset:** `data/calibration_100_sentences.json` (100 sentences, 5 domains × 20)
- **Runner:** `scripts/run_calibration_v040.py` → one parsable JSONL
- **Output:** `docs/hesperia_runtime_output/calibration_run.jsonl` (200 + 50 lines by default)

Run from repo root `CLIENTS/hesperia`:

```bash
PYTHONPATH=. python3 scripts/run_calibration_v040.py
```
