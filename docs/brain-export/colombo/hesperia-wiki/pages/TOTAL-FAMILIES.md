# TOTAL_FAMILIES

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Derived variable  
**Responsible (module):** `throughout core/`  
**Value / default:** 288

## In plain words

size of the family vector — always 12 areas × 24 families per area = 288 slots Sigma shape-checks against.

## Definition

- **Receives:** [AREAS](../pages/AREAS.md), [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md)
- **Does:** TOTAL_FAMILIES = AREAS × [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md) = 12 × 24
- **Outputs:** `288` → *F_vec[288]*, *detect_dominant_family*, [TOTAL_HEXES](../pages/TOTAL-HEXES.md)
- **Exists for:** fixed ontology grain for family-activation vectors

## Yields (formula)

TOTAL_FAMILIES = AREAS × [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md) = 12 × 24

## Produced from (inputs)

- [AREAS](../pages/AREAS.md)
- [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md)

## Needed by (consumers)

- *F_vec[288]*
- *detect_dominant_family*
- [TOTAL_HEXES](../pages/TOTAL-HEXES.md)

## See also

- [AREAS](../pages/AREAS.md)
- [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md)
- [TOTAL_HEXES](../pages/TOTAL-HEXES.md)
- [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)
- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Origin

Java 20_GEOMETRY (product) — Theory Explainer: plain_lang: size of the family vector — always 12 areas × 24 families per area = 288 slots Sigma shape-checks against. author: Hesperia wiki (throughout core/). extent: full. reasoning: fixed ontology grain for family-activation vectors. application: *F_vec[288*], *detect_dominant_family*.

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Family-activation vector length; Sigma shape check.

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
