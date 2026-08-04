# BAND_3_GOOD (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** bool

## In plain words

One of six mutually-exclusive confidence bands on L8 SI_SYSTEM_CONFIDENCE_U1000 — exactly one True per run.

## Definition

- **Receives:** [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md), [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md)
- **Does:** 600 <= SI_SYSTEM_CONFIDENCE_U1000 < 800
- **Outputs:** `bool` → *no named wiki consumer yet*
- **Exists for:** terminus confidence banding for human-facing labels and actions

## Yields (formula)

600 <= SI_SYSTEM_CONFIDENCE_U1000 < 800

## Produced from (inputs)

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md)

## See also

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md)
- [BAND_0_CRITICAL (L9)](../pages/BAND-0-CRITICAL-L9.md)
- [BAND_1_POOR (L9)](../pages/BAND-1-POOR-L9.md)
- [BAND_2_FAIR (L9)](../pages/BAND-2-FAIR-L9.md)
- [BAND_4_VERY_GOOD (L9)](../pages/BAND-4-VERY-GOOD-L9.md)
- [BAND_5_EXCELLENT (L9)](../pages/BAND-5-EXCELLENT-L9.md)
- [DIRECTIONALIZE_HIGH_IS_GOOD (L9)](../pages/DIRECTIONALIZE-HIGH-IS-GOOD-L9.md)
- [DIRECTIONALIZE_LOW_IS_GOOD (L9)](../pages/DIRECTIONALIZE-LOW-IS-GOOD-L9.md)
- [PILLAR_INPUT_QUALITY_U1000 (L9)](../pages/PILLAR-INPUT-QUALITY-U1000-L9.md)
- [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md)
- [PILLAR_EVIDENCE_U1000 (L9)](../pages/PILLAR-EVIDENCE-U1000-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: One of six mutually-exclusive confidence bands on L8 SI_SYSTEM_CONFIDENCE_U1000 — exactly one True per run. author: Hesperia L9 (42_SPEC / output_catalog §9). extent: full. reasoning: terminus confidence banding for human-facing labels and actions. application: [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md), brand words / actions.

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** One of six mutually-exclusive confidence bands on L8's SI_SYSTEM_CONFIDENCE_U1000 — exactly one is True per run. Source: `docs/foundations/output_catalog.md` §9.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
