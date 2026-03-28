# TFP release — pytest bar (TFP-GATE-A2A3)

**Purpose:** Define “green” for TFP-related CI beyond cosmetic pass.

## Rules

1. **No `xfail`** on the release slice listed below (fix or `skip` with issue link — not silent xfail).
2. **Warnings:** Prefer `pytest -W error::Warning` for the slice when dependencies allow; otherwise document ignored categories in `pytest.ini` and re-review quarterly.
3. **Runtime budget:** Record wall time for the slice on reference hardware (e.g. prichindel); investigate if **> 10×** vs last recorded baseline without code volume justification.

## Commands (documented slice)

```bash
export PYTHONHASHSEED=0
export HESPERIA_STRICT_DETERMINISM=1
python3 -m pytest tests/test_tfp_module_main_run.py tests/test_env_determinism.py \
  tests/concept_dictionary/test_cd_executor.py -q --tb=short
```

Extend with `tests/test_e2e_flows.py -m tfp` when TFP E2E is in scope.

## CI

Primary enforcement: **`sealed-runtime-gate.yml`** steps + integrity pytest list; determinism via `test_env_determinism.py`.

---

`SIGNED: Cursor (workflow) | TFP-GATE-A2A3 | 2026-03-28`
