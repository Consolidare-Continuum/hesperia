# FAMILIES_PER_AREA

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `gcs_lookup, core/topology/`  
**Value / default:** 24

## In plain words

fixed ontology grain — each of the 12 areas owns exactly this many families (24).

## Definition

- **Receives:** [AREAS](../pages/AREAS.md)
- **Does:** Families per area, fixed ontology grain.
- **Outputs:** `24` → [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md), [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)
- **Exists for:** partner of AREAS and [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)

## Yields (formula)

Families per area, fixed ontology grain.

## Produced from (inputs)

- [AREAS](../pages/AREAS.md)

## Needed by (consumers)

- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)

## See also

- [AREAS](../pages/AREAS.md)
- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)
- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Origin

Java 20_GEOMETRY — Theory Explainer: plain_lang: fixed ontology grain — each of the 12 areas owns exactly this many families (24). author: Hesperia wiki (gcs_lookup, core/topology/). extent: full. reasoning: partner of AREAS and [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md). application: [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
