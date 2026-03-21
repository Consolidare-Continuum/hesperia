# Calibration release gate v1

**Purpose:** Block **ship** of bundles that fail schema, anomaly, consistency, or gold thresholds.

## Profiles

| Profile | Use |
|---------|-----|
| `research_allow_degraded` | Local research; anomalies allowed; **manifest optional** — missing `00_manifest.json` still yields `pass: true` with a default envelope. Other profiles fail with `G004_MISSING_BUNDLE_MANIFEST`. |
| `internal_review` | Warn on `error` severity; block on `blocking` + structural failure. |
| `product_candidate` | Stricter: no `A001`/`A002`/`A005`; consistency_score floor. |
| `ship_blocking` | Any blocking anomaly or gate failure → exit non-zero. |

## Checks (machine)

1. JSON Schema validation for each present artifact (when schema exists).
2. `operational_envelope` present on each artifact root.
3. Anomaly severity vs profile (`hesperia.engine.calibration_release_gate`).
4. `10_calibration_audit.json` `consistency_score` vs floor (if present).
5. Goldset pass rate (optional `--goldset` path).

## Output

- **`11_calibration_release_gate.json`** — decision, profile, checks[], blocking_reason, rollback_advice.

## CLI

`PYTHONPATH=. python3 tools/calibration_release_gate.py --bundle-dir DIR --profile internal_review`

CI runs the same tools on `tests/fixtures/tfp_calibration_bundle_ci/` (see `.github/workflows/sealed-runtime-gate.yml`).
