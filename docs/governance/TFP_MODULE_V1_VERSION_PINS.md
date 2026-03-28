# TFP module v1 — `VERSION.yaml` and `HESPERIA_CALIB_DICT_VERSION`

**TFP-V1-12 (Sophia):**

- **`defaults.active_calibration_dict_pack`** — default pack directory name under `assets/calibration/dicts/<pack>/` for validators and tooling.
- **`tfp_module_v1.pinned_calibration_dict_pack`** — must **equal** `active_calibration_dict_pack` on mainline (enforced by `tools/validate_version_consistency.py`).
- **`tfp_module_v1.seal_requested`** — when `true`, `hesperia.modules.tfp.seal` treats the module as sealed (warn path unless env overrides to `block`).
- **`HESPERIA_CALIB_DICT_VERSION`** — runtime override for dict directory name; operators must keep it aligned with a committed pack when testing releases (see [`HESPERIA_TFP_MODULE_DICTS.md`](../HESPERIA_TFP_MODULE_DICTS.md)).

`SIGNED: Sophia (pins) | TFP module v1 | 2026-03-28 | TFP-V1-12`
