# AREA_CONTAINMENT_U1000 (L9)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_9.py::compute_L9 -> result[...]`  
**Value / default:** int [0,1000]

## In plain words

Reframes L8 area leakage into containment (good when high) for geometry pillar scoring.

## Definition

- **Receives:** [SI_AREA_LEAKAGE_PCT (L8)](../pages/SI-AREA-LEAKAGE-PCT-L8.md)
- **Does:** 1000 - L8 SI_AREA_LEAKAGE_U1000
- **Outputs:** `int [0,1000]` → [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md)
- **Exists for:** directionalize leakage→containment so pillars stay 'higher is better'

## Yields (formula)

1000 - L8 SI_AREA_LEAKAGE_U1000

## Produced from (inputs)

- [SI_AREA_LEAKAGE_PCT (L8)](../pages/SI-AREA-LEAKAGE-PCT-L8.md)

## Needed by (consumers)

- [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md)

## See also

- [SI_AREA_LEAKAGE_PCT (L8)](../pages/SI-AREA-LEAKAGE-PCT-L8.md)
- [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md)

## Origin

Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Reframes L8 area leakage into containment (good when high) for geometry pillar scoring. author: Hesperia L9 (42_SPEC item 9). extent: full. reasoning: directionalize leakage→containment so pillars stay 'higher is better'. application: [PILLAR_GEOMETRY_U1000 (L9)](../pages/PILLAR-GEOMETRY-U1000-L9.md).

## Notes

**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Spec item 9 — reframes leakage into containment; feeds PILLAR_GEOMETRY_U1000. Source: `docs/foundations/output_catalog.md` §9.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
