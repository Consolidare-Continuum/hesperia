<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Topology Graph Weights Specification

**Layer-4 Topology Graph — propagation weights.** Deterministic and reproducible.

## Scope

This specification defines the **propagation weights** used when computing influence between areas on the Layer-4 topology graph. The graph is an **icosahedral surface graph** (12 areas, 30 edges, degree 5 per node); adjacency from `data/topology/area_adjacency_matrix.json` (must satisfy icosahedral invariants). Meta nodes A6, A12 (indices 5, 11) use reduced propagation weight on incident edges.

## Weight Constants

| Constant               | Value | Description                          |
|------------------------|-------|--------------------------------------|
| `self_weight`          | 1.0   | Weight for the area’s own contribution. |
| `adjacent_weight`      | 0.25  | Weight for each adjacent area’s contribution. |
| `non_adjacent_weight`  | 0     | Weight for non-adjacent areas (no propagation). |

All values are fixed. No runtime or configuration overrides for reproducibility.

## Propagation Rule

Let `area_vector` be a length-12 vector of non-negative values (e.g. aggregated family counts per area). Let `adjacent(i)` be the set of area indices adjacent to area `i` (from the area adjacency matrix).

**Influence at area *i*:**

```
influence(area_i) =
    area_vector[i] * self_weight
  + Σ(adjacent areas j) area_vector[j] * adjacent_weight
```

Equivalently, for each area index `i` in `0..11`:

- **Self term:** `area_vector[i] * 1.0`
- **Adjacent terms:** for each `j` in `adjacent(i)`, add `area_vector[j] * 0.25`
- **Non-adjacent:** no contribution (weight 0)

## Determinism and Reproducibility

- Weights are fixed in this spec; implementations must use exactly these values unless a future spec version explicitly changes them.
- Adjacency is defined solely by `data/topology/area_adjacency_matrix.json` (symmetric, diagonal 0).
- Order of areas is deterministic (indices 0–11); family→area mapping is from `data/topology/family_to_area_map.json`.

## References

- Layer-4 responsibilities: areas aggregation + adjacency graph (Reference Architecture).
- Data: `data/topology/area_adjacency_matrix.json`, `data/topology/family_to_area_map.json`.
- Loader: `sphere/topology/topology_loader.py`.
