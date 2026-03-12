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

## Data locations

- Area adjacency: `data/topology/area_adjacency_matrix.json` (or configurable `topology_data_root`).
- Family → area mapping: `data/topology/family_to_area_map.json` (canonical order `family_001` … `family_288` → area index 0–11).

## Rules

- All topology loaders and propagation code must use these dimensions.
- Changing AREAS or FAMILIES or the adjacency shape requires a design review and update to this document.
