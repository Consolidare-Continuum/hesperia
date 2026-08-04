# decay_factor (propagation)

**Status:** 🟡 PARTIAL — present in a narrow slice/tool, not the full contract  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Parameter (YAML weight)  
**Responsible (module):** `assets/specs/canon/propagation_weights.yaml`  
**Value / default:** 1.0

## In plain words

reserved multi-hop attenuation knob; today it is identity (1.0) on single-hop paths.

## Definition

- **Receives:** [Transition matrix (W)](../pages/Transition-matrix-W.md)
- **Does:** Deferred multi-hop attenuation — currently a no-op on single-hop propagation.
- **Outputs:** `1.0` → *no named wiki consumer yet*
- **Exists for:** future multi-hop attenuation without breaking current YAML

## Yields (formula)

Deferred multi-hop attenuation — currently a no-op on single-hop propagation.

## Produced from (inputs)

- [Transition matrix (W)](../pages/Transition-matrix-W.md)

## See also

- [Transition matrix (W)](../pages/Transition-matrix-W.md)
- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)

## Origin

Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: reserved multi-hop attenuation knob; today it is identity (1.0) on single-hop paths. author: Hesperia propagation YAML. extent: partial (reserved slot). reasoning: future multi-hop attenuation without breaking current YAML. application: [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md).

## Notes

**HWIKI-WIRE:** attached to category anchor [Transition matrix (W)](../pages/Transition-matrix-W.md). **HWIKI-DOC-24:** Reserved slot, not yet load-bearing beyond identity.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
