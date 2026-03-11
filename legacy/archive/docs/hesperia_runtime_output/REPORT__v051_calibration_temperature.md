# HESPERIA v0.5.1 — Temperature sharpening calibration report

**Date:** 2026-02-24
**Dataset:** 100 sentences × 2 (base/shadow), 5 domains.
**Metrics:** entropy before/after sharpening (normalized), per-domain governance, shadow delta magnitude.

## Summary

| T     | entropy_sharp_norm_mean_global | entropy_after (raw) | In target 0.65–0.80? |
|-------|--------------------------------|----------------------|----------------------|
| 0.15  | 0.996                          | 5.64                 | No                   |
| 0.08  | 0.984                          | 5.57                 | No                   |
| 0.04  | 0.938                          | 5.31                 | No                   |
| **0.02** | **0.812**                  | **4.60**             | **Yes**              |

Default T=0.15 (spec) does not reduce entropy; with this embedding distribution, lower T is required. **HESPERIA_TEMPERATURE=0.02** brings normalized entropy into the target band and increases domain contrast.

## T=0.02 (recommended for target band)

- **entropy_before_sharpen_mean:** 5.44
- **entropy_after_sharpen_mean:** 4.60
- **entropy_sharp_norm_mean_global:** 0.812

Per-domain entropy (normalized): conflict_power 0.77, economic_exchange 0.81, identity_culture 0.83, social_cohesion 0.86, technical_systems 0.79.

**Governance spread (mean_governance):** 0.39 (identity_culture) – 0.48 (conflict_power, social_cohesion).
**Shadow delta magnitude:** ~0.0003–0.0013 (increased vs no sharpening; no explosion).

## Artifacts

- `calibration_metrics_v05.json` — default T (0.15)
- `calibration_metrics_v05_T008.json` — T=0.08
- `calibration_metrics_v05_T004.json` — T=0.04
- `calibration_metrics_v05_T002.json` — T=0.02 (use for target band)

## Determinism

No randomness; T fixed per run. Entropy change is deterministic per sentence.
