# TFP module v1 — schema freeze (artifacts)

**TFP-V1-08:** Module-facing **TFP calibration / file-pipeline** JSON artifacts for v1 are validated by frozen JSON Schemas under:

- `schemas/tfp_bundle/01_structural_batch.schema.json`
- `schemas/tfp_bundle/10_calibration_audit.schema.json`
- `schemas/tfp_bundle/11_calibration_release_gate.schema.json`

**Tool:** `python3 tools/validate_tfp_bundle_schemas.py --bundle-dir <bundle_dir>`

**CI fixture:** `tests/fixtures/tfp_calibration_bundle_ci/` (also exercised in `sealed-runtime-gate.yml`).

**Rule:** Bump schema version or filename only with governance row; keep validator `ARTIFACTS` list in `validate_tfp_bundle_schemas.py` in sync.

`SIGNED: Daniel (schema freeze) | TFP module v1 | 2026-03-28 | TFP-V1-08`
