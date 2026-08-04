# ACTION_REQUIRE_MORE_INPUT (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** bool

## In plain words

Fires when too little of the input actually got attributed to trust any read from it.

## Definition

- **Receives:** [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- **Does:** SI_COVERAGE_U1000 < 500
- **Outputs:** `bool` → *no named wiki consumer yet*
- **Exists for:** terminus action flag — what the product may ask a human or allow next

## Yields (formula)

SI_COVERAGE_U1000 < 500

## Produced from (inputs)

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)

## See also

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
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
- [PILLAR_EVIDENCE_U1000 (L9)](../pages/PILLAR-EVIDENCE-U1000-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Fires when too little of the input actually got attributed to trust any read from it.. author: Hesperia L9 action trigger (42_SPEC). extent: full. reasoning: terminus action flag — what the product may ask a human or allow next. application: [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md).

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Fires when too little of the input actually got attributed to trust any read from it. Source: `docs/foundations/output_catalog.md` §9.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
