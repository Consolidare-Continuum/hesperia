# RUNBOOK — Dict / calibration release gates

**Purpose:** One entrypoint before promoting calibration assets or tagging a dict-heavy release.

## Command

From Hesperia repo root:

```bash
./tools/run_dict_release_gates.sh
```

## What it runs

1. `python3 tools/validate_version_consistency.py` — `VERSION.yaml` vs `pyproject.toml` (+ mirror file checks).
2. If `assets/calibration/dicts/<HESPERIA_CALIB_DICT_VERSION>/dict_a.jsonl` exists: `tools/run_b_cd_wave_after_a.sh` (DLCR validators + CD pytest + runtime smoke). If missing: **SKIP** log (same idea as `.github/workflows/sealed-runtime-gate.yml`).

## Env

- `HESPERIA_CALIB_DICT_VERSION` — default `v0_6_0_clr_v052_2`.

`SIGNED: Cursor (workflow) | RUNBOOK dict gates | 2026-03-28 | Hesperia repo`
