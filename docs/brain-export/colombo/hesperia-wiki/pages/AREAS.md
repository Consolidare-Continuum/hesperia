# AREAS

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `sphere/topology/, core/topology/ (invariants, dict_b)`  
**Value / default:** 12

## Yields (formula)

Fixed ontology grain — 12 areas = 12 icosahedron vertices.

## Needed by (consumers)

- [FAMILIES_PER_AREA](../pages/FAMILIES-PER-AREA.md)
- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- [compute_tension](../pages/compute-tension.md)

## Origin

Java 20_GEOMETRY (`final int AREAS = 12`); geometric root: regular icosahedron / Platonic solid

## Notes

Every area-activation vector has length 12. Sigma shape checks fail if this drifts.

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md)
