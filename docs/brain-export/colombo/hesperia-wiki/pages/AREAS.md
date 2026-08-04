# AREAS

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `sphere/topology/, core/topology/ (invariants, dict_b)`  
**Value / default:** 12

## In plain words

fixed ontology grain — always 12 therapy areas, one per icosahedron vertex; area vectors must be length 12.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Fixed ontology grain — 12 areas = 12 icosahedron vertices.
- **Outputs:** `12` → [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md), [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md), [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md), [compute_tension](../pages/compute-tension.md)
- **Exists for:** geometry/ontology constant under Sigma shape checks

## Yields (formula)

Fixed ontology grain — 12 areas = 12 icosahedron vertices.

## Needed by (consumers)

- [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md)
- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- [compute_tension](../pages/compute-tension.md)

## See also

- [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md)
- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- [compute_tension](../pages/compute-tension.md)

## Origin

Java 20_GEOMETRY (`final int AREAS = 12`); geometric root: regular icosahedron / Platonic solid — Theory Explainer: plain_lang: fixed ontology grain — always 12 therapy areas, one per icosahedron vertex; area vectors must be length 12. author: Hesperia wiki (sphere/topology/, core/topology/ (invariants, dict_b)). extent: full. reasoning: geometry/ontology constant under Sigma shape checks. application: [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md), [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md), [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Every area-activation vector has length 12. Sigma shape checks fail if this drifts.

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
