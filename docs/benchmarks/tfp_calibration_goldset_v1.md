# TFP calibration goldset v1

**Machine file:** `tests/gold/tfp_calibration_goldset_v1.json`  
**Runner:** `python3 tools/run_tfp_calibration_goldset.py --bundle-dir DIR [--verbose]`

## Layers

| Layer | Intent |
|-------|--------|
| `raw_integrity_gold` | Forbidden cross-plane states (split-brain signatures). |
| `aggregation_gold` | Numeric floors / dominant rank expectations for a pinned session. |
| `readability_gold` | Envelope / operational discipline checks. |

## Reference session

**`1-11-09-2023`** — Russian TFP transcript under `research/_noone_local/1-11-09-2023.md`.  
Documented in gold **gold_reasoning_note** fields: pre-fix failure mode vs post-fix expectations.

## CI

The sealed runtime workflow runs:

- `tools/validate_tfp_bundle_schemas.py --bundle-dir tests/fixtures/tfp_calibration_bundle_ci`
- `tools/run_tfp_calibration_goldset.py --bundle-dir tests/fixtures/tfp_calibration_bundle_ci`
- `tools/calibration_release_gate.py … --skip-schema --skip-gold` (envelope / blocking smoke)

For **live** engine output instead of the synthetic fixture, run the file pipeline in the job and point `--bundle-dir` at that directory (or set `HESPERIA_TFP_GOLD_BUNDLE_DIR` in a custom job).

## Related

- Anomalies: `docs/specs/output_anomaly_taxonomy_v1.md`
- Release gate: `docs/specs/calibration_release_gate_v1.md`
