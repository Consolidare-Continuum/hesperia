# TFP / lexical resolution — single source of truth (TFP-GATE-B1)

**Authority:** Ethan / Grace packet 2026-03-28.

## Hard rule

- **Single source of truth for dict payloads:** `assets/` trees (`assets/calibration/dicts/<pack>/…`, `assets/data/engine_dynamics_v060/…`) as named in governance and `HESPERIA_TFP_MODULE_DICTS.md`.
- **Mirrors** (e.g. `hesperia/modules/tfp/data/dicts/…` after `sync_tfp_module_data.sh`) are **derived** — never authoritative; **no second edited copy** of dict JSONL.

## Precedence (debug order)

1. **`HESPERIA_*` env overrides** (e.g. `HESPERIA_CALIB_DICT_VERSION`) when loader honors them.  
2. **Module path redirect** (if implemented) — **path resolution only**; must still read bytes from the resolved `assets/` location (or identical mirror checksum).  
3. **Default:** `assets/` paths per `VERSION.yaml` `defaults.active_calibration_dict_pack` and engine defaults.

## Matrix (document only)

| Surface | `HESPERIA_CALIB_DICT_VERSION` | `HESPERIA_CD_ENABLED` | Resolution |
|--------|-------------------------------|------------------------|------------|
| Mainline run | set / unset | 0 / 1 | Env → calibration dir under `assets/calibration/dicts/`; CD executor reads `concept_dict_cd.jsonl` under `assets/data/engine_dynamics_v060/concept_dict/` when enabled |

**Loader stretch:** If a loader adds indirection, it must **not** duplicate dict files on disk — only change how paths are resolved.

---

`SIGNED: Cursor (workflow) | TFP-GATE-B1 | 2026-03-28`

---

## v1 authoritative (TFP-V1-06)

This contract is **authoritative for Hesperia TFP / lexical resolution v1** alongside [`HESPERIA_TFP_MODULE_DICTS.md`](../HESPERIA_TFP_MODULE_DICTS.md). Module scope and post-seal policy: [`TFP_MODULE_V1_SCOPE.md`](TFP_MODULE_V1_SCOPE.md).

`SIGNED: Ethan (governance) | TFP resolution v1 | 2026-03-28 | TFP-V1-06`
