# TFP calibration — mirror sync and CI SKIP behavior

**TFP-V1-14 (Abelard / ops pointer):**

- **Mirror:** `./tools/sync_tfp_module_data.sh` refreshes **`tfp_v1/`** dict faces from `assets/` (no `research/`). **Operational corpus + lineage** under `hesperia/modules/tfp/data/tfp_v1/` via migrate script. **Authoritative runtime bytes** remain under `assets/` until loader ADR ships — see [`HESPERIA_TFP_MODULE_DICTS.md`](../HESPERIA_TFP_MODULE_DICTS.md) and [`TFP_RESOLUTION_CONTRACT.md`](TFP_RESOLUTION_CONTRACT.md).
- **CI large artifacts:** `sealed-runtime-gate.yml` **SKIP**s `run_b_cd_wave_after_a.sh` when `assets/calibration/dicts/v0_6_0_clr_v052_2/dict_a.jsonl` is missing; **SKIP**s `check_metrics_gate.py` when `metrics.json` is missing. This is intentional for shallow clones.
- **Path gate:** `.github/workflows/tfp-module-v1-paths.yml` still runs version + DLCR regression + module v1 pytest when TFP/dict paths change — keep dict commits and workflow green on full checkouts.

No mass Chroma ingest in this path; cluster docs remain in brain repo `cluster/` if needed.

`SIGNED: Abelard (ops note) | TFP module v1 | 2026-03-28 | TFP-V1-14`
