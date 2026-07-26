# Grace — Hesperia TFP: one bundle folder, documented (2026-04-14)

**Role:** Operational pointer (brain repo). Canonical text lives in the **Hesperia** repo.

**Canonical doc (Hesperia):** `TFP_VALUES_LIST` — **§0 One bundle directory — not multiple “canons”**

**Summary**

- A TFP file-pipeline run is **one `--out-dir`** containing `00`–`09` (and optional `12_*`, etc.). Look in **that** directory only for that run.
- **Defaults differ by tool** (`gena_tfp_bundle_run` vs `tfp_pipeline_standard_run` vs raw `run_tfp_file_pipeline`). That is not duplicate canon — it is different wrappers. Always note **tool + path** when comparing runs across chats.
- **Input:** The file passed to `-i` is what the pipeline processes; TFP domain pack defaults are manifest-recorded (`HESPERIA_DLCR_DOMAIN_PACK=tfp` unless opted out).
- **Not in the same folder by default:** `10`/`11` (Gena post-steps), `99` (inspect path), API one-shots, E2E harness outputs under `assets/artifacts/e2e/` — see §0 table.

**Code pointers updated:** `runtime/pipeline/run_tfp_file_pipeline.py` (module docstring), `tools/gena_tfp_bundle_run.py` (docstring) → link to `TFP_VALUES_LIST` §0.

**Disk layout (2026-04-14):** Flat TFP clutter under `hesperia/outputs/` was moved into **`outputs/tfp/runs/`**, **`outputs/tfp/smoke/`**, **`outputs/tfp/tool/`**; calibration folders renamed `tfp_calibration_ru_*` → `tfp_calibration_run_*`; symlinks `latest_tfp_calibration_run` / `prev_tfp_calibration_run` retargeted. Defaults for Gena / standard run / file pipeline now write under `outputs/tfp/runs/`. See Hesperia `outputs/README.md`.

`SIGNED: Grace (triage) | Hesperia TFP output discipline | 2026-04-14 | brain operational pointer`
