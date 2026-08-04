# BRAND_WORD_TRUST (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** string enum

## In plain words

The single headline trust label — checks the gate-chain outcome first, then bands SI_SYSTEM_CONFIDENCE_U1000.

## Definition

- **Receives:** [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- **Does:** "BLOCKED" if code!=0 else "TRUSTED">=850 else "USABLE">=650 else "TENTATIVE">=450 else "FRAGILE"
- **Outputs:** `string enum` → *no named wiki consumer yet*
- **Exists for:** human-readable terminus label from U1000 / gate thresholds

## Yields (formula)

"BLOCKED" if code!=0 else "TRUSTED">=850 else "USABLE">=650 else "TENTATIVE">=450 else "FRAGILE"

## Produced from (inputs)

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)

## See also

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [PILLAR_INPUT_QUALITY_U1000 (L9)](../pages/PILLAR-INPUT-QUALITY-U1000-L9.md)
- [PILLAR_EVIDENCE_U1000 (L9)](../pages/PILLAR-EVIDENCE-U1000-L9.md)
- [PILLAR_CONSISTENCY_U1000 (L9)](../pages/PILLAR-CONSISTENCY-U1000-L9.md)
- [PILLAR_STABILITY_U1000 (L9)](../pages/PILLAR-STABILITY-U1000-L9.md)
- [PILLAR_GOVERNANCE_U1000 (L9)](../pages/PILLAR-GOVERNANCE-U1000-L9.md)
- [BAND_0_CRITICAL (L9)](../pages/BAND-0-CRITICAL-L9.md)
- [BAND_1_POOR (L9)](../pages/BAND-1-POOR-L9.md)
- [BAND_2_FAIR (L9)](../pages/BAND-2-FAIR-L9.md)
- [BAND_3_GOOD (L9)](../pages/BAND-3-GOOD-L9.md)
- [BAND_4_VERY_GOOD (L9)](../pages/BAND-4-VERY-GOOD-L9.md)
- [BAND_5_EXCELLENT (L9)](../pages/BAND-5-EXCELLENT-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: The single headline trust label — checks the gate-chain outcome first, then bands SI_SYSTEM_CONFIDENCE_U1000.. author: Hesperia L9 brand word (42_SPEC). extent: full. reasoning: human-readable terminus label from U1000 / gate thresholds. application: [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md).

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** The single headline trust label — checks the gate-chain outcome first, then bands SI_SYSTEM_CONFIDENCE_U1000. Source: `docs/foundations/output_catalog.md` §9, thresholds re-verified against `layer_9.py` 2026-08-04.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
