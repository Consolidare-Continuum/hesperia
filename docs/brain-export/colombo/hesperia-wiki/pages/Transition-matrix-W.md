# Transition matrix (W)

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Data structure / formula  
**Responsible (module):** `core/math/transition_matrix.py`  
**Value / default:** —

## Yields (formula)

Transition counts a_t -> a_{t+1}, row-normalized to a stochastic matrix.

## Needed by (consumers)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)

## Origin

Markov (1906) finite-state formalism — Theory Explainer: plain_lang: a table of 'from this area, probability of next area' built from counted moves, then normalized so each row sums to 1. author: Markov finite-state chain. extent: full construction (counts→probabilities). reasoning: BEYOND Java; supports lazy step and multi-step diffusion. application: [lambda (lazy step)](../pages/lambda-lazy-step.md), [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md), [Mixing Diagnostics](../pages/Mixing-Diagnostics.md).

## Notes

**HWIKI-DOC-05:** Full construction (counts -> probabilities); not proposed in the Java corpus, built later for L6 dynamism.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md)
