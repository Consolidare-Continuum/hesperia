# TFP module data mirror (interim)

**Status:** Normalization / anchoring / proposing for this phase are **done**; this tree holds **copies** of corpus + dict bundles for the next pipeline steps. **Canonical runtime** still loads from `assets/` (`HESPERIA_CALIB_DICT_VERSION`, `assets/data/engine_dynamics_v060/`) until the full pipe and dict state live under module architecture.

**Do not edit** `research/` for this workflow — sources are read-only for sync.

## Layout (after sync)

| Path under `data/` | Source (repo) |
|--------------------|----------------|
| `corpus/ru_2_cleaned/` | `research/_noone_local/2_cleaned/` (copy) |
| `corpus/en_2_cleaned/` | `research/_noone_local/english_2_cleaned/` (copy) |
| `dicts/calibration/<version>/` | `assets/calibration/dicts/<version>/` (copy) |
| `dicts/engine_dynamics_v060/` | `assets/data/engine_dynamics_v060/` (copy) |

Default version for calibration mirror: **`v0_6_0_clr_v052_1`** (override with env in sync script).

## Populate / refresh

From repository root:

```bash
./tools/sync_tfp_module_data.sh
```

Optional:

- `HESPERIA_CALIB_DICT_VERSION=v0_tfp_cal_wave_002 ./tools/sync_tfp_module_data.sh` — mirror that calibration version instead of the default.

Large trees are **gitignored** here; run the script after clone to materialize files.

## Resolver hint (future)

`HESPERIA_TFP_MODULE_DATA_ROOT` may be wired to this directory once loaders move; default implicit root: `hesperia/modules/tfp/data/` relative to import path / repo root.
