# Calibration profiles — comparison (v1)

Profiles live in **`assets/config/calibration_profiles_v1.json`**. They are **presentation-only** in scope: precision, top-N, suppression floor, visibility of fallback flags.

| Profile | Precision | Top-N families | Suppression floor | Fallback flags |
|---------|-----------|----------------|-------------------|----------------|
| `strict_raw` | 8 | 96 | 0 | yes |
| `balanced_readable` | 4 | 48 | 1e-6 | yes |
| `ui_executive` | 2 | 12 | 1e-4 | no |
| `diagnostic_dense` | 6 | 288 | 0 | yes |

**Deterministic replay:** `tools/apply_output_calibration_profile.py` is a **stub** until frozen intermediate bundles exist; golden tests will pin `profile` + `profile_hash` + `calibration_version` on replay output.
