# ROUNDING_POLICY (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/layers/layer_8.py::compute_L8 -> result[...]`  
**Value / default:** "DECIMALS_RATIO=6,DECIMALS_PCT=2,DECIMALS_U1000=0"

## In plain words

Documents the rounding precision applied per unit family.

## Definition

- **Receives:** [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Does:** Fixed reference constant, identical every run.
- **Outputs:** `"DECIMALS_RATIO=6,DECIMALS_PCT=2,DECIMALS_U1000=0"` → *no named wiki consumer yet*
- **Exists for:** L8 unit-policy constant — documents how SI_* values are tagged and scaled

## Yields (formula)

Fixed reference constant, identical every run.

## Produced from (inputs)

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## See also

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- [UNIT_TYPE_ENUM (L8)](../pages/UNIT-TYPE-ENUM-L8.md)
- [SCALE_POLICY_ENUM (L8)](../pages/SCALE-POLICY-ENUM-L8.md)
- [EPSILON_POLICY (L8)](../pages/EPSILON-POLICY-L8.md)
- [CLAMP_POLICY (L8)](../pages/CLAMP-POLICY-L8.md)
- [SI_TOTAL_TOKENS_COUNT (L8)](../pages/SI-TOTAL-TOKENS-COUNT-L8.md)
- [SI_COVERAGE_PCT (L8)](../pages/SI-COVERAGE-PCT-L8.md)
- [SI_COVERAGE_U1000 (L8)](../pages/SI-COVERAGE-U1000-L8.md)
- [SI_DOMINANCE_PCT (L8)](../pages/SI-DOMINANCE-PCT-L8.md)
- [SI_DOMINANCE_U1000 (L8)](../pages/SI-DOMINANCE-U1000-L8.md)
- [SI_ENTROPY_U1000 (L8)](../pages/SI-ENTROPY-U1000-L8.md)
- [SI_ENTROPY_PCT (L8)](../pages/SI-ENTROPY-PCT-L8.md)

## Origin

Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Documents the rounding precision applied per unit family.. author: Hesperia L8 (41_SPEC / output_catalog §8). extent: full. reasoning: L8 unit-policy constant — documents how SI_* values are tagged and scaled. application: [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md), L9.

## Notes

**HWIKI-CATALOG-L8 / HWIKI-PLAIN:** Documents the rounding precision applied per unit family. Source: `docs/foundations/output_catalog.md` §8.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
