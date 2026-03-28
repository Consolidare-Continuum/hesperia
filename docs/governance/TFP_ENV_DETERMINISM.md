# TFP / release — environment determinism (TFP-GATE-A0)

**Purpose:** Avoid false-green tests when hash randomization or version/dict drift goes unchecked.

## PYTHONHASHSEED

- Set **`PYTHONHASHSEED=0`** in the environment **before** starting Python (CI job env, local shell).
- **CI:** `sealed-runtime-gate.yml` sets job-level `PYTHONHASHSEED: "0"` and `HESPERIA_STRICT_DETERMINISM: "1"`.
- **Local:** `export PYTHONHASHSEED=0` then `pytest` / wave scripts; or use `tools/run_tfp_env_precheck.sh`.

Setting hash seed from `conftest.py` is **too late** for interpreter-global hash behavior — use the wrapper or shell export.

## Version ↔ calibration pack

- **`VERSION.yaml`** field **`defaults.active_calibration_dict_pack`** must name a directory under `assets/calibration/dicts/<pack>/` with **`dict_a.jsonl`** present.
- **`tools/validate_version_consistency.py`** enforces this (run in CI).

## RNG / seeds (audit)

- **2026-03-28:** `grep` for `random.seed`, `np.random.seed`, `torch.manual_seed` under `hesperia/engine/**/*.py` → **no matches** (engine path not using explicit floating seeds). Re-audit when adding stochastic code.

## Precheck script

From repo root:

```bash
bash tools/run_tfp_env_precheck.sh
```

---

`SIGNED: Cursor (workflow) | TFP-GATE-A0 doc | 2026-03-28`
