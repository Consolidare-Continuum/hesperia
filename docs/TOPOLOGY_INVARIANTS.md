<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA RAD — Topology Invariants

This document is the **single source of truth** for topology geometry. Any change to these constants must be reflected here and reviewed.

## Topology type: icosahedral surface graph

The area topology is a **closed spheroid surface graph** with icosahedral adjacency:

- **Nodes:** 12 (A1–A12, indices 0–11).
- **Edges:** 30.
- **Degree:** every node has exactly 5 neighbors.
- **Structure:** skeleton of a regular icosahedron (12 vertices, 20 triangular faces).

Validation (enforced at load time):

- `degree(node) == 5` for every node.
- `total_edges == 30`.
- Graph is a single connected component.

## Meta reference nodes (A6, A12)

- **A6** (index 5) and **A12** (index 11) are **meta reference nodes** (semantic control anchors).
- They remain **fully connected** in the graph (same 5 neighbors each); no geometric links are removed.
- **Propagation:** `propagation_weight` is **reduced** on edges incident to meta nodes (default scale 0.5). They receive propagation normally but emit filtered propagation; they may act as calibration references.

## Invariants

| Constant | Value | Description |
|----------|--------|-------------|
| **AREAS** | 12 | Number of topological areas (indices 0–11). |
| **FAMILIES** | 288 | Number of families (indices 0–287). |
| **ADJACENCY** | 12×12 symmetric, binary | Icosahedral: degree 5 per node, 30 edges, connected. |
| **ICOSAHEDRAL_DEGREE** | 5 | Every node has exactly 5 neighbors. |
| **ICOSAHEDRAL_EDGES** | 30 | Total edge count. |

## Public vs reserved (10+2) — project-wide decision

**Operational (public):** 10 areas, 240 families, 60 000 hexes, 360 000 sides. All propagation, metrics, and public outputs use only these. Indices: areas 0–9, families 0–239, hexes/sides in the non-reserved ranges.

**Reserved (service areas):** 2 areas (internal indices 10, 11), 48 families (global 240–287), 12 000 hexes, 72 000 sides. Space reserved for special purposes; not exposed in public ontology or outputs. Loaded from `assets/reserve/` (reserved_areas.json, reserved_families_registry.json, reserved_hex_registry.json). The projection layer and schema guard ensure no reserved indices appear in responses or exports.

**Math and propagation:** The two reserved areas are **stateless** for now (no population, no semantic values). Propagation and core math operate over the full 12-area geometry; reserved regions are excluded only at output and from population. No change to propagation formulas or invariants.

| Tier | Internal (total) | Public (operational) | Reserved (service) |
|------|------------------|----------------------|--------------------|
| Areas | 12 | 10 | 2 |
| Families | 288 | 240 | 48 |
| Hexes | 72 000 | 60 000 | 12 000 |
| Sides | 432 000 | 360 000 | 72 000 |

## Icosahedral adjacency (canonical)

Canonical adjacency equals the **geometric icosahedron** (unit-sphere embedding). Each node has exactly 5 neighbors (A1=0 … A12=11):

- A1 → A2, A6, A8, A11, A12
- A2 → A1, A6, A8, A9, A10
- A3 → A4, A5, A7, A11, A12
- A4 → A3, A5, A7, A9, A10
- A5 → A3, A4, A6, A10, A12
- A6 (meta) → A1, A2, A5, A10, A12
- A7 → A3, A4, A8, A9, A11
- A8 → A1, A2, A7, A9, A11
- A9 → A2, A4, A7, A8, A10
- A10 → A2, A4, A5, A6, A9
- A11 → A1, A3, A7, A8, A12
- A12 (meta) → A1, A3, A5, A6, A11

## 3-D embedding (aligned)

The 3-D unit-sphere embedding is **canonically aligned** to the topology graph via deterministic graph isomorphism (see `sphere/topology/embedding_alignment.py`). All exported coordinates and Graphviz layout use this aligned mapping. Topology and embedding describe the same labeled icosahedron; all graph edges have near-equal angular length (strict validation with tolerance 0.05).

## Family embedding (two-scale geometry)

Families are **not** placed directly on the icosahedron. The correct model is hierarchical:

- **Icosahedron vertex** → **Area** (area-to-area topology).
- **Inside each area** → **Local family lattice** (24 families: 1 center + 6 inner + 8 middle + 9 outer).
- **Inside each family** → Concepts / hexes.

Cross-area traversal uses **bridge families** only (see `specs/canon/family_embedding_tfp.yaml` and `docs/specs/FAMILY_EMBEDDING.md`). Loader: `sphere.topology.family_embedding`.

## Data locations

- Area adjacency: `data/topology/area_adjacency_matrix.json` (or configurable `topology_data_root`). Must satisfy icosahedral invariants (degree 5, 30 edges, connected).
- Family → area mapping: `data/topology/family_to_area_map.json` (canonical order `family_001` … `family_288` → area index 0–11).
- Family embedding (local lattices + bridges): `specs/canon/family_embedding_tfp.yaml`.
- Reserved (service) areas and families: `assets/reserve/reserved_areas.json`, `reserved_families_registry.json`, `reserved_hex_registry.json`. See **Public vs reserved (10+2)** above.

## Rules

- All topology loaders and propagation code must use these dimensions.
- Public outputs and schemas expose only 10 areas, 240 families (no reserved indices). Use `core.projection` and `core.topology.reserve_loader` to enforce.
- Changing AREAS or FAMILIES or the adjacency shape requires a design review and update to this document.
