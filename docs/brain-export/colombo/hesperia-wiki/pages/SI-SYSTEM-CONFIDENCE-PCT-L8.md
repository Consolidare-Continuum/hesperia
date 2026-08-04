# SI_SYSTEM_CONFIDENCE_PCT (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_8.py::compute_L8 -> result[...]`  
**Value / default:** float [0,100]

## In plain words

Percent-scale sibling of the already-wikified [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md) — same source value, feeds L9's confidence bands alongside the U1000 form.

## Definition

- **Receives:** [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Does:** L7 SYSTEM_CONFIDENCE_SCORE -> [0,100]
- **Outputs:** `float [0,100]` → *no named wiki consumer yet*
- **Exists for:** L8 SI_* rescale — fixed unit family so L9 never sees each layer's native scale

## Yields (formula)

L7 SYSTEM_CONFIDENCE_SCORE -> [0,100]

## Produced from (inputs)

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## See also

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- [UNIT_TYPE_ENUM (L8)](../pages/UNIT-TYPE-ENUM-L8.md)
- [SCALE_POLICY_ENUM (L8)](../pages/SCALE-POLICY-ENUM-L8.md)
- [EPSILON_POLICY (L8)](../pages/EPSILON-POLICY-L8.md)
- [CLAMP_POLICY (L8)](../pages/CLAMP-POLICY-L8.md)
- [ROUNDING_POLICY (L8)](../pages/ROUNDING-POLICY-L8.md)
- [SI_TOTAL_TOKENS_COUNT (L8)](../pages/SI-TOTAL-TOKENS-COUNT-L8.md)
- [SI_COVERAGE_PCT (L8)](../pages/SI-COVERAGE-PCT-L8.md)
- [SI_COVERAGE_U1000 (L8)](../pages/SI-COVERAGE-U1000-L8.md)
- [SI_DOMINANCE_PCT (L8)](../pages/SI-DOMINANCE-PCT-L8.md)

## Origin

Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Percent-scale sibling of the already-wikified [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md) — same source value, feeds L9's confidence bands alongside the U1000 form.. author: Hesperia L8 (41_SPEC / output_catalog §8). extent: full. reasoning: L8 SI_* rescale — fixed unit family so L9 never sees each layer's native scale. application: [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md), L9 pillars/bands.

## Notes

**HWIKI-CATALOG-L8 / HWIKI-PLAIN:** Percent-scale sibling of the already-wikified [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md) — same source value, feeds L9's confidence bands alongside the U1000 form. Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
