# `outputs/` layout (Hesperia)

Generated trees stay **gitignored** except this file. **Do not** drop ad-hoc TFP runs at the root of `outputs/` — use the structure below.

## TFP file-pipeline and related tooling

| Path | Purpose |
|------|--------|
| **`tfp/runs/`** | Default root for **`gena_tfp_bundle_run`**, **`tfp_pipeline_standard_run`**, and **`run_tfp_file_pipeline`** (under `tfp_pipeline_run/<uuid>/`). Named experiments, calibration passes, controlled session runs, Grace gold runs. |
| **`tfp/smoke/`** | Short wiring / TRIZ / Gena input smoke dirs (not production bundles). |
| **`tfp/tool/`** | One-shot tool outputs (e.g. `tfp_api_calibration_one_shot`). |

Symlinks at **`outputs/latest_tfp_calibration_run`** and **`outputs/prev_tfp_calibration_run`** point into **`tfp/runs/`** (relative targets).

**Naming:** Prefer `tfp_calibration_run_<YYYYMMDD>_<HHMMSS>_<suffix>` — avoid the historical `_ru_` typo for “run”.

## Other top-level dirs

`benchmarks/`, `dict_calibration/`, `e2e/`, `openai_calibration/`, `operator_sessions/`, `reports/`, `semantic_dynamics/`, `smoke/` — harnesses or categories **outside** the TFP file-pipeline default tree unless you intentionally place work there.

Canonical doc: repo root **`TFP_VALUES_LIST`** §0.
