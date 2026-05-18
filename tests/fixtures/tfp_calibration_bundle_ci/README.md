# TFP calibration CI fixture bundle

Pinned under-repo JSON that satisfies `tests/gold/tfp_calibration_goldset_v1.json` for session stem `1-11-09-2023`: aggregation bounds, raw-integrity (no split-brain), and root `operational_envelope` on `01` / `05` / `06`.

Used by `.github/workflows/sealed-runtime-gate.yml` with:

- `python3 tools/validate_tfp_bundle_schemas.py --bundle-dir tests/fixtures/tfp_calibration_bundle_ci`
- `python3 tools/run_tfp_calibration_goldset.py --bundle-dir tests/fixtures/tfp_calibration_bundle_ci`
- `python3 tools/calibration_release_gate.py --bundle-dir tests/fixtures/tfp_calibration_bundle_ci` (same three steps as CI: schema, goldset, gate; `00_manifest.json` carries synthetic `tfp_signal_calibration` + `09_session_topology.json` for `main_engine_release_gate_v1`)

`11_calibration_release_gate.json` may be written by the gate CLI in CI (ephemeral workspace). It is gitignored here.

For real engine output, re-run `run_tfp_file_pipeline` and optionally set `HESPERIA_TFP_GOLD_BUNDLE_DIR` locally to compare against this goldset.
