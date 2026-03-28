# TFP-related `HESPERIA_*` environment flags (v1 allowlist)

**Purpose (TFP-V1-05):** Every `HESPERIA_TFP_*` name used in repo tooling or runtime must appear here and in `runtime/shipping/env_guard.py` `ALLOWED_HESPERIA_ENV`.

## Allowlist (`HESPERIA_TFP_*` and neighbors)

| Variable | Role |
|----------|------|
| `HESPERIA_TFP4_ROOT` | Legacy corpus root for `tfp4_*` ingest tools (default path in tools). |
| `HESPERIA_TFP_DLCR` | When truthy, TFP smoke attaches `session_dlcr_bundles` (see E2E / pipeline docs). |
| `HESPERIA_TFP_PIPELINE_RUN_ID` | Stable run id for pipeline / bundle tooling (`gena_tfp_bundle_run`, file pipeline). |
| `HESPERIA_TFP_GOLD_BUNDLE_DIR` | Optional override for goldset comparison dir (benchmarks / CI fixtures). |
| `HESPERIA_TFP_MODULE_DATA_ROOT` | Optional future loader root; default remains `assets/` (see `hesperia/modules/tfp/data/README.md`). |
| `HESPERIA_TFP_MODULE_SEALED` | `1` / `true` → warn on `TFPModule.project`; `block` → raise `RuntimeError` on `project` (see `hesperia/modules/tfp/seal.py`). |

**Strict unknown-env mode:** shipping API honors `HESPERIA_SHIPPING_ENV_STRICT=1` (with `true`/`yes`/`on`) → `check_hesperia_env(strict=True)` so **any** unknown `HESPERIA_*` fails closed at startup.

## Policy

- Do not introduce new `HESPERIA_TFP_*` without updating this file, `env_guard.py`, and (if needed) `tools/list_hesperia_env_for_guard.py` regeneration instructions in `env_guard` header.

`SIGNED: Gena (audit) | TFP module v1 | 2026-03-28 | TFP-V1-05`
