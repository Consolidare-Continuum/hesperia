# DIRECTIONALIZE_LOW_IS_GOOD (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** "1000-clamp(u,0,1000)"

## In plain words

Counterpart convention for metrics where lower U1000 means better (leakage/pressure before containment/consistency reframes).

## Definition

- **Receives:** [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- **Does:** Fixed formula string, not a value.
- **Outputs:** `"1000-clamp(u,0,1000)"` → *no named wiki consumer yet*
- **Exists for:** shared directionalize convention for inverted 'bad-when-high' metrics

## Yields (formula)

Fixed formula string, not a value.

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
- [PILLAR_INPUT_QUALITY_U1000 (L9)](../pages/PILLAR-INPUT-QUALITY-U1000-L9.md)
- [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md)
- [PILLAR_EVIDENCE_U1000 (L9)](../pages/PILLAR-EVIDENCE-U1000-L9.md)
- [PILLAR_CONSISTENCY_U1000 (L9)](../pages/PILLAR-CONSISTENCY-U1000-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Counterpart convention for metrics where lower U1000 means better (leakage/pressure before containment/consistency reframes). author: Hesperia L9 (42_SPEC). extent: full. reasoning: shared directionalize convention for inverted 'bad-when-high' metrics. application: [AREA_CONTAINMENT_U1000 (L9)](../pages/AREA-CONTAINMENT-U1000-L9.md), [CONSISTENCY_U1000 (L9)](../pages/CONSISTENCY-U1000-L9.md).

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Counterpart to [DIRECTIONALIZE_HIGH_IS_GOOD (L9)](../pages/DIRECTIONALIZE-HIGH-IS-GOOD-L9.md) for metrics where lower U1000 means better — a reference string, not itself computed per-run. Source: `docs/foundations/output_catalog.md` §9.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
