# L1–L9 layer math run output (logged)

**Purpose**: Canonical directory for full-pass L1–L9 script output. Run → output → logged → reportable.

**Script**: From repo root (ensure `artifacts/layer_runs` exists: `mkdir -p artifacts/layer_runs`):
```bash
python3 -m sphere_rag.layers.run_l1_through_l9 --out artifacts/layer_runs/latest_L1_L9_output.json
```
Or with absolute path: `--out /path/to/repo/artifacts/layer_runs/latest_L1_L9_output.json`

**Link (path)**: `artifacts/layer_runs/` — output log dir (see [ORDER.md](../../ORDER.md)).

Latest run JSON: `latest_L1_L9_output.json` (overwritten each full pass).
