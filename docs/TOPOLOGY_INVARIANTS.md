<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA RAD — Topology Invariants

This document is the **single source of truth** for topology geometry. Any change to these constants must be reflected here and reviewed.

## Invariants

| Constant | Value | Description |
|----------|--------|-------------|
| **AREAS** | 12 | Number of topological areas (indices 0–11). |
| **FAMILIES** | 288 | Number of families (indices 0–287). |
| **ADJACENCY** | 12×12 symmetric matrix | Area adjacency: binary, symmetric, diagonal 0. No isolated nodes; graph connected. |

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

## Data locations

- Area adjacency: `data/topology/area_adjacency_matrix.json` (or configurable `topology_data_root`).
- Family → area mapping: `data/topology/family_to_area_map.json` (canonical order `family_001` … `family_288` → area index 0–11).
- Reserved (service) areas and families: `assets/reserve/reserved_areas.json`, `reserved_families_registry.json`, `reserved_hex_registry.json`. See **Public vs reserved (10+2)** above.

## Rules

- All topology loaders and propagation code must use these dimensions.
- Public outputs and schemas expose only 10 areas, 240 families (no reserved indices). Use `core.projection` and `core.topology.reserve_loader` to enforce.
- Changing AREAS or FAMILIES or the adjacency shape requires a design review and update to this document.
