# CONSISTENCY_U1000 (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** int [0,1000]

## In plain words

Reframes contradiction pressure into consistency (good when high) for pillar and brand labels.

## Definition

- **Receives:** [SI_CONTRADICTION_PRESSURE_PCT (L8)](../pages/SI-CONTRADICTION-PRESSURE-PCT-L8.md)
- **Does:** 1000 - L8 SI_CONTRADICTION_PRESSURE_U1000
- **Outputs:** `int [0,1000]` → [PILLAR_CONSISTENCY_U1000 (L9)](../pages/PILLAR-CONSISTENCY-U1000-L9.md), [BRAND_WORD_CONTRADICTION (L9)](../pages/BRAND-WORD-CONTRADICTION-L9.md)
- **Exists for:** directionalize pressure→consistency so pillars stay 'higher is better'

## Yields (formula)

1000 - L8 SI_CONTRADICTION_PRESSURE_U1000

## Produced from (inputs)

- [SI_CONTRADICTION_PRESSURE_PCT (L8)](../pages/SI-CONTRADICTION-PRESSURE-PCT-L8.md)

## Needed by (consumers)

- [PILLAR_CONSISTENCY_U1000 (L9)](../pages/PILLAR-CONSISTENCY-U1000-L9.md)
- [BRAND_WORD_CONTRADICTION (L9)](../pages/BRAND-WORD-CONTRADICTION-L9.md)

## See also

- [SI_CONTRADICTION_PRESSURE_PCT (L8)](../pages/SI-CONTRADICTION-PRESSURE-PCT-L8.md)
- [PILLAR_CONSISTENCY_U1000 (L9)](../pages/PILLAR-CONSISTENCY-U1000-L9.md)
- [BRAND_WORD_CONTRADICTION (L9)](../pages/BRAND-WORD-CONTRADICTION-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Reframes contradiction pressure into consistency (good when high) for pillar and brand labels. author: Hesperia L9 (42_SPEC item 10). extent: full. reasoning: directionalize pressure→consistency so pillars stay 'higher is better'. application: [PILLAR_CONSISTENCY_U1000 (L9)](../pages/PILLAR-CONSISTENCY-U1000-L9.md), [BRAND_WORD_CONTRADICTION (L9)](../pages/BRAND-WORD-CONTRADICTION-L9.md).

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Item 10 — reframes contradiction pressure into consistency. Source: `docs/foundations/output_catalog.md` §9.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
