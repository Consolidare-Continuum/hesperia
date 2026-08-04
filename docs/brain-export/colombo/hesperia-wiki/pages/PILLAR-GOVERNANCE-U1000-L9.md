# PILLAR_GOVERNANCE_U1000 (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** int [0,1000]

## In plain words

The one pillar keyed directly off L7's gate-chain outcome rather than an SI_* rescale — a clean pass scores 1000, each unit of failure code linearly costs 10 points.

## Definition

- **Receives:** [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- **Does:** 1000 if [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md)==0 else clamp(1000-10*code, 0, 1000)
- **Outputs:** `int [0,1000]` → [BRAND_WORD_TRUST (L9)](../pages/BRAND-WORD-TRUST-L9.md)
- **Exists for:** mid-level aggregation between L8 SI_* rescales and L9 brand words

## Yields (formula)

1000 if [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md)==0 else clamp(1000-10*code, 0, 1000)

## Produced from (inputs)

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)

## Needed by (consumers)

- [BRAND_WORD_TRUST (L9)](../pages/BRAND-WORD-TRUST-L9.md)

## See also

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [BRAND_WORD_TRUST (L9)](../pages/BRAND-WORD-TRUST-L9.md)
- [BAND_0_CRITICAL (L9)](../pages/BAND-0-CRITICAL-L9.md)
- [BAND_1_POOR (L9)](../pages/BAND-1-POOR-L9.md)
- [BAND_2_FAIR (L9)](../pages/BAND-2-FAIR-L9.md)
- [BAND_3_GOOD (L9)](../pages/BAND-3-GOOD-L9.md)
- [BAND_4_VERY_GOOD (L9)](../pages/BAND-4-VERY-GOOD-L9.md)
- [BAND_5_EXCELLENT (L9)](../pages/BAND-5-EXCELLENT-L9.md)
- [DIRECTIONALIZE_HIGH_IS_GOOD (L9)](../pages/DIRECTIONALIZE-HIGH-IS-GOOD-L9.md)
- [DIRECTIONALIZE_LOW_IS_GOOD (L9)](../pages/DIRECTIONALIZE-LOW-IS-GOOD-L9.md)
- [PILLAR_INPUT_QUALITY_U1000 (L9)](../pages/PILLAR-INPUT-QUALITY-U1000-L9.md)
- [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: The one pillar keyed directly off L7's gate-chain outcome rather than an SI_* rescale — a clean pass scores 1000, each unit of failure code linearly costs 10 points.. author: Hesperia L9 pillar (42_SPEC). extent: full. reasoning: mid-level aggregation between L8 SI_* rescales and L9 brand words. application: [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md).

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** The one pillar keyed directly off L7's gate-chain outcome rather than an SI_* rescale — a clean pass scores 1000, each unit of failure code linearly costs 10 points. One of six pillar scores. Source: `docs/foundations/output_catalog.md` §9.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
