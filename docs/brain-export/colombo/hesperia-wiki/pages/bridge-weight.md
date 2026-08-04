# bridge_weight

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Parameter (YAML weight)  
**Responsible (module):** `assets/specs/canon/propagation_weights.yaml`  
**Value / default:** 0.22

## Yields (formula)

Cross-area coupling — semantic bleed across areas.

## Produced from (inputs)

- [center_to_inner](../pages/center-to-inner.md)

## Needed by (consumers)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)

## Origin

Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: how much energy can jump across area bridges (semantic bleed), not only along rings. author: Hesperia propagation YAML. extent: full. reasoning: cross-area coupling complementary to radial weights. application: [center_to_inner](../pages/center-to-inner.md), [Transition matrix (W)](../pages/Transition-matrix-W.md).

## Notes

**HWIKI-DOC-24:** Cross-area coupling weight.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md)
