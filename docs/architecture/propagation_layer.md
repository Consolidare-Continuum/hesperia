# Propagation Layer (Layer-7) — Architecture

## Principles

1. **Layer-7 is behavior, not math infrastructure.**  
   Propagation orchestrates topology and dynamism; it does not implement numeric primitives. All math (diffusion step, row normalization, conservation checks) lives in `core/math`.

2. **Topology constrains propagation.**  
   Mass flows only along edges of the area adjacency graph. No adjacency → no diffusion. The propagation matrix is built from the topology (and optional edge weights) and is row-stochastic.

3. **core/math performs numeric operations.**  
   Single-step diffusion `(1 - α)*v + α*(v @ W)`, L1 normalization, and mass-conservation checks are implemented in `core/math`. `sphere/propagation` calls these and composes behavior (weighting, diagnostics, family projection).

4. **Family propagation is area-derived (Option A).**  
   We first propagate at area level (12 areas over the adjacency graph), then project the propagated area vector back to 288 families using the family→area mapping. Family counts are not copied from input; they are derived from propagated areas.

5. **Conservation and normalization policy.**  
   - Without normalization: total area mass is conserved within a small tolerance (diffusion is a convex combination).  
   - With normalization (default): output area and family vectors are L1-normalized to sum 1; diagnostics record `normalization_applied` and `mass_before` / `mass_after`.

## Architecture Diagram

```
Layer-4 Topology  ──┐
                    ├─→ Layer-7 Propagation ─→ propagated_area_vector
Layer-5 Math      ──┤                          propagated_family_counts
                    │                          propagation_diagnostics
Layer-6 Dynamism  ──┘
```

- **Layer-4 / sphere/topology:** supplies area adjacency matrix and family→area mapping.  
- **Layer-5 / core/math:** supplies diffusion step, normalization, matrix row-normalize, conservation check.  
- **Layer-6 / sphere/dynamism:** supplies optional stability_index and jump_rate for modulating the diffusion coefficient.  
- **Layer-7 / sphere/propagation:** builds edge weights from topology, applies modulation, runs area diffusion, projects to families, and produces diagnostics.

## Dependency Direction

- `sphere/propagation` → `sphere/topology` (adjacency, family_to_area)
- `sphere/propagation` → `core/math` (diffusion, normalization, matrix_utils, conservation)
- `sphere/pipeline` → `sphere/propagation` (calls `compute_propagation` only; no inline propagation logic)

## Outputs

- **propagated_area_vector:** length 12; from topology-driven area diffusion.  
- **propagated_family_counts:** length 288; from area→family projection.  
- **propagation_diagnostics:** diffusion coefficient used, stability/jump modulation flags, mass before/after, conservation and normalization flags, active edge count.
