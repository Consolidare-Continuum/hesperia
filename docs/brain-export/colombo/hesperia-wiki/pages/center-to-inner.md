# center_to_inner

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Parameter (YAML weight)  
**Responsible (module):** `assets/specs/canon/propagation_weights.yaml`  
**Value / default:** 0.25

## In plain words

how strongly energy at the center ring leaks into the first neighborhood ring.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Strongest local spread into the final area vector.
- **Outputs:** `0.25` → [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md), [bridge_weight](../pages/bridge-weight.md)
- **Exists for:** distance-sensitive diffusion intuition on the icosahedral neighborhoods

## Yields (formula)

Strongest local spread into the final area vector.

## Needed by (consumers)

- [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md)
- [bridge_weight](../pages/bridge-weight.md)

## See also

- [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md)
- [bridge_weight](../pages/bridge-weight.md)

## Origin

Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: how strongly energy at the center ring leaks into the first neighborhood ring. author: Hesperia propagation YAML (no single classical paper). extent: full (load-bearing weight). reasoning: distance-sensitive diffusion intuition on the icosahedral neighborhoods. application: [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md), [bridge_weight](../pages/bridge-weight.md), [lambda (lazy step)](../pages/lambda-lazy-step.md).

## Notes

**HWIKI-DOC-24:** Strongest local spread weight in the center→inner→middle→outer ladder.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
