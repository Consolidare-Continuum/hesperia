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

## Conflict Integrity Gates (v0.5.8 task9)

Promotion on **contradiction handling integrity**, not on raw contradiction magnitude.

| Verdict | Meaning | Typical evidence |
|--------|---------|------------------|
| **PASS** | All six structured gates `PASS`; `conflict_integrity_score` high | `99_tfp_bundle_inspect.json` → `promotion_conflict_verdict`, `release_conflict_gates.aggregate` |
| **QUALIFIED_PASS** | No `FAIL`; at least one gate `WARN` — usable for research / calibration / controlled demos | Same artifact; `promotion_conflict_reasons` lists gate tags |
| **FAIL** | Any gate `FAIL` — promotion blocked | `contradiction_visibility_gate`, `crossplane_alignment_gate`, `latent_conflict_gate`, `family_conflict_gate`, `contamination_honesty_gate`, `runtime_vs_calibration_split_gate` |

**Authority:** `tools/inspect_tfp_bundle_output.py` (bundle inspect). Product layer may echo `release_conflict_readiness` in `06_product_analyze.json` extended fields; it is **not** the gate authority.

**Optional CI / local enforcement:** `python3 tools/tfp_pipeline_standard_run.py --inspect-bundle-dir <bundle> --fail-on-conflict-gate` exits `5` on `FAIL`; `--min-conflict-integrity-score 0.70` exits `6` below threshold. Default pipeline runs unchanged when these flags are not used.

## CI

Primary enforcement: **`sealed-runtime-gate.yml`** steps + integrity pytest list; determinism via `test_env_determinism.py`.

---

`SIGNED: Cursor (workflow) | TFP-GATE-A2A3 | 2026-03-28`
