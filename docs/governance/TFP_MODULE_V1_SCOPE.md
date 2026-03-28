# TFP module v1 — scope and freeze line

**Authority:** Ethan packet **ETHAN-TFP-MODULE-V1-ROUNDUP-15-2026-03-28** in brain repo `operational/assignments/`. **Hesperia** is the implementation repo.

## In scope (v1)

- Public **`hesperia.modules.tfp`** surface documented in [`hesperia/modules/tfp/ENTRYPOINTS.md`](../../hesperia/modules/tfp/ENTRYPOINTS.md).
- **DLCR / calibration** pins: `VERSION.yaml` `defaults.active_calibration_dict_pack` + `tfp_module_v1` block (see [`TFP_MODULE_V1_SEAL_CHECKLIST.md`](TFP_MODULE_V1_SEAL_CHECKLIST.md)).
- **CI:** path-filtered workflow when `hesperia/modules/tfp/**` or `assets/calibration/dicts/**` changes (`.github/workflows/tfp-module-v1-paths.yml`); full gate remains `sealed-runtime-gate.yml`.
- **Gold digests** for `run_dlcr_pipeline` (no `research/`): `tests/test_tfp_module_v1_dlcr_golds.py`.
- **Governance:** resolution contract + module dicts as v1 authoritative (signed § in those files); env flag audit [`TFP_ENV_FLAGS_V1.md`](TFP_ENV_FLAGS_V1.md); release order [`TFP_MODULE_V1_RELEASE.md`](TFP_MODULE_V1_RELEASE.md).

## Out of scope (v1)

- New TFP **module** features, new public entrypoints, or resolver/heuristic changes under `hesperia/modules/tfp/` after **seal** without a new Grace row.
- Product shipping guarantees for `/product/tfp` — see [`TFP_PRODUCT_TFP_N_A_V1.md`](TFP_PRODUCT_TFP_N_A_V1.md).

## Freeze line

- **Pre-seal:** module code, schemas under `schemas/tfp_bundle/`, and tests may change only while **TFP-V1-*** rows are OPEN or under explicit triage.
- **Post-seal:** see north star in the roundup packet — **dict / calibration packs only** unless Grace adds a row that reopens module work.

## Related

- Dict SSoT: [`docs/HESPERIA_TFP_MODULE_DICTS.md`](../HESPERIA_TFP_MODULE_DICTS.md)  
- Resolution: [`TFP_RESOLUTION_CONTRACT.md`](TFP_RESOLUTION_CONTRACT.md)  
- Metric registry gaps: [`TFP_V1_METRIC_REGISTRY_GAPS.md`](TFP_V1_METRIC_REGISTRY_GAPS.md)  
- Version pins: [`TFP_MODULE_V1_VERSION_PINS.md`](TFP_MODULE_V1_VERSION_PINS.md)

`SIGNED: Ethan (scope) | TFP module v1 | 2026-03-28 | TFP-V1-01`
