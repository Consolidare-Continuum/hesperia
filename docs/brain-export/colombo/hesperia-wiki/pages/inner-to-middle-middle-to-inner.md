# inner_to_middle / middle_to_inner

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Parameter (YAML weight)  
**Responsible (module):** `assets/specs/canon/propagation_weights.yaml`  
**Value / default:** 0.18

## In plain words

second-ring leak — weaker than [center_to_inner](../pages/center-to-inner.md) because farther from the activated core.

## Definition

- **Receives:** [center_to_inner](../pages/center-to-inner.md)
- **Does:** Second-ring leak, distance-sensitive diffusion.
- **Outputs:** `0.18` → [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md)
- **Exists for:** distance decay ladder

## Yields (formula)

Second-ring leak, distance-sensitive diffusion.

## Produced from (inputs)

- [center_to_inner](../pages/center-to-inner.md)

## Needed by (consumers)

- [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md)

## See also

- [center_to_inner](../pages/center-to-inner.md)
- [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md)
- [bridge_weight](../pages/bridge-weight.md)

## Origin

Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: second-ring leak — weaker than [center_to_inner](../pages/center-to-inner.md) because farther from the activated core. author: Hesperia propagation YAML. extent: full. reasoning: distance decay ladder. application: [center_to_inner](../pages/center-to-inner.md), [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md).

## Notes

**HWIKI-DOC-24:** Mid-ring bidirectional weight.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
