# Output calibration migration notes (v1)

## Structural / sealed

- **New:** `diagnostics.calibration_status` on internal structural payload (pre-projection).
- **New:** `L1.CALIBRATION_FALLBACK_USED` when L1 is synthesized from sealed `family_activation_vector`.
- **New:** `concept_layer.marker_concept_mass`, `uniform_concept_prior_fallback_used`, `hex_upstream_fallback_used` in sealed stack output.

Downstream **public schema** consumers: unchanged required keys; optional keys may appear in extended diagnostics depending on projection policy.

## Hex microphysics

- **Behavior change:** Energy-controlled local step no longer accepts proposals that annihilate positive total hex mass. Regressions: any test that relied on η=1 → all-zero clip must be updated.

## Audit / tooling

- Run `python3 tools/tfp_calibration_audit.py --bundle-dir outputs/<run>` after file pipeline to emit `10_calibration_audit.json`.
