# bridge_weight

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Parameter (YAML weight)  
**Responsible (module):** `assets/specs/canon/propagation_weights.yaml`  
**Value / default:** 0.22

## In plain words

how much energy can jump across area bridges (semantic bleed), not only along rings.

## Definition

- **Receives:** [center_to_inner](../pages/center-to-inner.md)
- **Does:** Cross-area coupling — semantic bleed across areas.
- **Outputs:** `0.22` → [lambda (lazy step)](../pages/lambda-lazy-step.md)
- **Exists for:** cross-area coupling complementary to radial weights

## Yields (formula)

Cross-area coupling — semantic bleed across areas.

## Produced from (inputs)

- [center_to_inner](../pages/center-to-inner.md)

## Needed by (consumers)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)

## See also

- [center_to_inner](../pages/center-to-inner.md)
- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md)
- [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md)

## Origin

Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: how much energy can jump across area bridges (semantic bleed), not only along rings. author: Hesperia propagation YAML. extent: full. reasoning: cross-area coupling complementary to radial weights. application: [center_to_inner](../pages/center-to-inner.md), [Transition matrix (W)](../pages/Transition-matrix-W.md).

## Notes

**HWIKI-DOC-24:** Cross-area coupling weight.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
