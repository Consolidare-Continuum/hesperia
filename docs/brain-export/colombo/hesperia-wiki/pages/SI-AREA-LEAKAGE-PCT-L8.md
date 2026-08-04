# SI_AREA_LEAKAGE_PCT (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_8.py::compute_L8 -> result[...]`  
**Value / default:** float [0,100]

## In plain words

L2's cross-area spillover, rescaled to a percent.

## Definition

- **Receives:** [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Does:** L2 [CROSS_AREA_RATIO](../pages/CROSS-AREA-RATIO.md) -> [0,100]
- **Outputs:** `float [0,100]` → [AREA_CONTAINMENT_U1000 (L9)](../pages/AREA-CONTAINMENT-U1000-L9.md)
- **Exists for:** L8 SI_* rescale — fixed unit family so L9 never sees each layer's native scale

## Yields (formula)

L2 [CROSS_AREA_RATIO](../pages/CROSS-AREA-RATIO.md) -> [0,100]

## Produced from (inputs)

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## Needed by (consumers)

- [AREA_CONTAINMENT_U1000 (L9)](../pages/AREA-CONTAINMENT-U1000-L9.md)

## See also

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- [AREA_CONTAINMENT_U1000 (L9)](../pages/AREA-CONTAINMENT-U1000-L9.md)
- [UNIT_TYPE_ENUM (L8)](../pages/UNIT-TYPE-ENUM-L8.md)
- [SCALE_POLICY_ENUM (L8)](../pages/SCALE-POLICY-ENUM-L8.md)
- [EPSILON_POLICY (L8)](../pages/EPSILON-POLICY-L8.md)
- [CLAMP_POLICY (L8)](../pages/CLAMP-POLICY-L8.md)
- [ROUNDING_POLICY (L8)](../pages/ROUNDING-POLICY-L8.md)
- [SI_TOTAL_TOKENS_COUNT (L8)](../pages/SI-TOTAL-TOKENS-COUNT-L8.md)
- [SI_COVERAGE_PCT (L8)](../pages/SI-COVERAGE-PCT-L8.md)
- [SI_COVERAGE_U1000 (L8)](../pages/SI-COVERAGE-U1000-L8.md)
- [SI_DOMINANCE_PCT (L8)](../pages/SI-DOMINANCE-PCT-L8.md)
- [SI_DOMINANCE_U1000 (L8)](../pages/SI-DOMINANCE-U1000-L8.md)

## Origin

Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: L2's cross-area spillover, rescaled to a percent.. author: Hesperia L8 (41_SPEC / output_catalog §8). extent: full. reasoning: L8 SI_* rescale — fixed unit family so L9 never sees each layer's native scale. application: [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md), L9 pillars/bands.

## Notes

**HWIKI-CATALOG-L8 / HWIKI-PLAIN:** L2's cross-area spillover, rescaled to a percent. Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
