# Icosahedral Surface Graph

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Topology (structural fact)  
**Responsible (module):** `assets/topology/area_adjacency_matrix.json, sphere/topology/embedding.py`  
**Value / default:** 12 nodes, 30 edges, 5-regular (`degree_per_node: 5`)

## Yields (formula)

The 12 areas are literal icosahedron vertices; `validate_embedding_matches_topology` enforces that every graph edge has near-equal angular length and every non-edge is strictly longer.

## Produced from (inputs)

- [AREAS](../pages/AREAS.md)
- [PHI (golden ratio)](../pages/PHI-golden-ratio.md)

## Needed by (consumers)

- [compute_tension](../pages/compute-tension.md)
- *angular_distance*
- [DFT Ring Smoothness](../pages/DFT-Ring-Smoothness.md)

## Origin

Regular icosahedron (Platonic solid) — Theory Explainer: plain_lang: think of the 12 therapy areas as the corners of a 20-faced solid; each corner touches exactly five others (5-regular), so 'next area' is neighborhood on a sphere, not a circle. author: Platonic solid / icosahedron topology. extent: full (adjacency JSON + embedding validation). reasoning: this graph is the substrate for tension and for rejecting ring-DFT. application: [compute_tension](../pages/compute-tension.md), [OPPOSITE_OFFSET](../pages/OPPOSITE-OFFSET.md), contrast [DFT Ring Smoothness](../pages/DFT-Ring-Smoothness.md).

## Notes

**HWIKI-DOC-10:** **Decisive fact against DFT Ring Smoothness**: a meaningful ring-DFT needs a 2-regular cyclic graph (C₁₂); the built topology is 5-regular. See [DFT Ring Smoothness](../pages/DFT-Ring-Smoothness.md).

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md)
