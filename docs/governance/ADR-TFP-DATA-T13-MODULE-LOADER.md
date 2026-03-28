# ADR — TFP module data loader (`HESPERIA_TFP_MODULE_DATA_ROOT`, `tfp_v1` first)

**Status:** Accepted (documentation phase; code cutover optional follow-up). **Task:** TFP-DATA-T13.

## Context

Operational dict/corpus work moves to **`hesperia/modules/tfp/data/tfp_v1/`**. CI and legacy runners may still read **`assets/calibration/dicts/<pack>/`**.

## Decision

1. **`tools/tfp_v1_paths.py`** defines the canonical **`tfp_v1`** root (overridable by **`HESPERIA_TFP_MODULE_DATA_ROOT`**).
2. **Future loader change** (implementation task): when resolving `dict_a_paths` for DLCR/calibration tooling, prefer **`${tfp_v1}/dict_a/runtime/dict_a.jsonl`** if present, else **`assets/calibration/dicts/${HESPERIA_CALIB_DICT_VERSION}/dict_a.jsonl`**.
3. **Failure mode:** If strict sync is required, set **`HESPERIA_TFP_SYNC_STRICT=1`** on `sync_tfp_module_data.sh` so missing runtime face fails closed.

## Consequences

- No behavior change for production engine until code imports this ADR; docs and sync path are ahead of code.

`SIGNED: Cursor (Marcus lane) | TFP-DATA-T13 | 2026-03-28`
