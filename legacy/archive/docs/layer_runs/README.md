# L1–L9 layer math run output (logged)

**Purpose**: Canonical directory for full-pass L1–L9 script output. Run → output → logged → reportable.

**Script**: From `CLIENTS/hesperia` (ensure `docs/layer_runs` exists: `mkdir -p docs/layer_runs`):
```bash
python3 -m sphere_rag.layers.run_l1_through_l9 --out docs/layer_runs/latest_L1_L9_output.json
```
Or with absolute path: `--out /path/to/CLIENTS/hesperia/docs/layer_runs/latest_L1_L9_output.json`

**Link (path)**: [CLIENTS/hesperia/docs/layer_runs/](.) — output log dir.

Latest run JSON: `latest_L1_L9_output.json` (overwritten each full pass).
