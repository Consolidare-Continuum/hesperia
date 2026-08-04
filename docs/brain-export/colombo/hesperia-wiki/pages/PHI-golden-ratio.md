# PHI (golden ratio)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `sphere/topology/embedding.py`  
**Value / default:** (1 + √5) / 2 ≈ 1.618033988749895

## In plain words

the golden ratio is the scale that appears when you build a regular icosahedron from unit coordinates; Hesperia uses it so the 12 area points sit on a true Platonic solid, not an arbitrary cloud.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Coordinate generator for the 12 icosahedron vertices (`ICOSAHEDRON_VERTICES_RAW`).
- **Outputs:** `(1 + √5) / 2 ≈ 1.618033988749895` → [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md), *angular_distance*, *geodesic_distance*
- **Exists for:** SCIENCE.md — 12 areas are geometrically forced by this construction

## Yields (formula)

Coordinate generator for the 12 icosahedron vertices (`ICOSAHEDRON_VERTICES_RAW`).

## Needed by (consumers)

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- *angular_distance*
- *geodesic_distance*

## See also

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Origin

Classical geometry (φ = (1+√5)/2) — Theory Explainer: plain_lang: the golden ratio is the scale that appears when you build a regular icosahedron from unit coordinates; Hesperia uses it so the 12 area points sit on a true Platonic solid, not an arbitrary cloud. author: classical Greek geometry / Euclidean solid construction (not a Hesperia-native invention). extent: full (verbatim φ in `ICOSAHEDRON_VERTICES_RAW`). reasoning: SCIENCE.md — 12 areas are geometrically forced by this construction. application: [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md), *angular_distance*, *geodesic_distance*.

## Notes

**HWIKI-DOC-09:** Verified in `embedding.py`. Java corpus stated [AREAS](../pages/AREAS.md)/FAMILIES as bare integers without embedding — φ is LIVE geometry, not a Java carry-over name.

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
