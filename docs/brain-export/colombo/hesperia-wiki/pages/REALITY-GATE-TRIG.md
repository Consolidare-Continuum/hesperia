# REALITY_GATE_TRIG

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_5.py::compute_L5 -> result["REALITY_GATE_TRIG"]`  
**Value / default:** bool

## In plain words

hard pass/fail: every trig/metric-space self-test residual must sit inside tolerance — if this fails, do not trust angle-based claims.

## Definition

- **Receives:** [DOT_SYMMETRY_RESIDUAL](../pages/DOT-SYMMETRY-RESIDUAL.md), [DOT_SELF_NONNEG_RESIDUAL](../pages/DOT-SELF-NONNEG-RESIDUAL.md), [NORM_CONSISTENCY_RESIDUAL](../pages/NORM-CONSISTENCY-RESIDUAL.md)
- **Does:** AND of all 13 trig/metric-space residual checks within tolerance
- **Outputs:** `bool` → *no named wiki consumer yet*
- **Exists for:** summary gate over the 13 L5 trig residuals

## Yields (formula)

AND of all 13 trig/metric-space residual checks within tolerance

## Produced from (inputs)

- [DOT_SYMMETRY_RESIDUAL](../pages/DOT-SYMMETRY-RESIDUAL.md)
- [DOT_SELF_NONNEG_RESIDUAL](../pages/DOT-SELF-NONNEG-RESIDUAL.md)
- [NORM_CONSISTENCY_RESIDUAL](../pages/NORM-CONSISTENCY-RESIDUAL.md)

## See also

- [DOT_SYMMETRY_RESIDUAL](../pages/DOT-SYMMETRY-RESIDUAL.md)
- [DOT_SELF_NONNEG_RESIDUAL](../pages/DOT-SELF-NONNEG-RESIDUAL.md)
- [NORM_CONSISTENCY_RESIDUAL](../pages/NORM-CONSISTENCY-RESIDUAL.md)
- [COSI_CLAMP_VIOLATION_COUNT](../pages/COSI-CLAMP-VIOLATION-COUNT.md)
- [ANGLE_RANGE_VIOLATION_COUNT](../pages/ANGLE-RANGE-VIOLATION-COUNT.md)
- [LAW_OF_COSINES_RESIDUAL](../pages/LAW-OF-COSINES-RESIDUAL.md)
- [SIN_COS_IDENTITY_RESIDUAL](../pages/SIN-COS-IDENTITY-RESIDUAL.md)
- [ROTATION_NORM_PRESERVATION_RESIDUAL](../pages/ROTATION-NORM-PRESERVATION-RESIDUAL.md)
- [ORTHONORMALITY_RESIDUAL_FROBENIUS](../pages/ORTHONORMALITY-RESIDUAL-FROBENIUS.md)
- [TRIANGLE_INEQUALITY_VIOLATION_COUNT](../pages/TRIANGLE-INEQUALITY-VIOLATION-COUNT.md)
- [METRIC_SYMMETRY_RESIDUAL](../pages/METRIC-SYMMETRY-RESIDUAL.md)
- [METRIC_IDENTITY_RESIDUAL](../pages/METRIC-IDENTITY-RESIDUAL.md)

## Origin

Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: hard pass/fail: every trig/metric-space self-test residual must sit inside tolerance — if this fails, do not trust angle-based claims. author: Hesperia wiki (core/layers/layer_5.py::compute_L5 -> result["REALITY_GATE_TRIG"]). extent: full. reasoning: summary gate over the 13 L5 trig residuals. application: [DOT_SYMMETRY_RESIDUAL](../pages/DOT-SYMMETRY-RESIDUAL.md), [DOT_SELF_NONNEG_RESIDUAL](../pages/DOT-SELF-NONNEG-RESIDUAL.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L5:** The single hard gate summarizing all 13 trig self-tests (5 live + 6 reserved-0.0 + itself) — gates L7's g8 guard and L9's ACTION_ALLOW_HUMAN_SUMMARY. Source: `docs/foundations/output_catalog.md` §5.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
