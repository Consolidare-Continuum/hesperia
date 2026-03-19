---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CORE-AREA-AGG
---

# Area aggregation (family → area) — canonical

**Prerequisite:** Family activations **F** are defined by [family_aggregation.md](family_aggregation.md) (from hex microphysics or direct injection per [system_architecture.md](system_architecture.md)).

## Equation

For **Nf = 288** families partitioned into **Na = 12** areas with **24** families per operational area (10+2 geometry per `docs/TOPOLOGY_INVARIANTS.md`):

\[
A_{\text{area},a} = \sum_{m : \mathcal{A}(m) = a} F_m
\]

where \(\mathcal{A}(m)\) maps family index **m** to area index **a** (0-based implementation convention).

## Constraints

1. **Non-negative:** \(F_m \ge 0\) ⇒ \(A_{\text{area},a} \ge 0\).
2. **Deterministic:** fixed family→area map → unique **A_area** for given **F**.
3. **Public projection:** customer-facing outputs may expose **10** operational areas; full **12-node** internal graph is invariant per topology spec.

## Code

`hesperia.extensions.dynamics.equations.aggregate_family_to_area` and pipeline projection layers.

## Related

- [hex_microphysics_canon.md](hex_microphysics_canon.md)  
- [semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md) §3.2 area projection  
