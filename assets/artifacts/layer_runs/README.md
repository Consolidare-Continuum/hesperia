<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# L1–L9 layer math run output (logged)

**Purpose**: Canonical directory for full-pass L1–L9 script output. Run → output → logged → reportable.

**Script**: From repo root (ensure `assets/artifacts/layer_runs` exists: `mkdir -p assets/artifacts/layer_runs`):
```bash
python3 -m runtime.pipeline.run_l1_through_l9 --out assets/artifacts/layer_runs/latest_L1_L9_output.json
```
Or with absolute path: `--out /path/to/repo/assets/artifacts/layer_runs/latest_L1_L9_output.json`

**Link (path)**: `assets/artifacts/layer_runs/` — output log dir.

Latest run JSON: `latest_L1_L9_output.json` (overwritten each full pass).
