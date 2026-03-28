# Dict A runtime face — `tfp_v1` vs `assets/` (TFP-DATA-T05)

**Until loader ADR (TFP-DATA-T13) ships:** sealed runtime and CI continue to resolve **`assets/calibration/dicts/<pack>/dict_a.jsonl`** via `HESPERIA_CALIB_DICT_VERSION` / `VERSION.yaml` pins.

**Module SSoT:** `hesperia/modules/tfp/data/tfp_v1/dict_a/runtime/dict_a.jsonl` is populated by **`tools/migrate_research_tfp_to_module_tfp_v1.sh`** and refreshed by **`tools/sync_tfp_module_data.sh`** from the **same** pack directory — content should match byte-for-byte after each sync.

**Promotion rule:** When editing Dict A for operations, edit under **`tfp_v1/`** workflow first; promote to **`assets/calibration/dicts/<pack>/`** with explicit Ethan/owner row.

`SIGNED: Cursor (Gena lane) | TFP-DATA-T05 | 2026-03-28`
