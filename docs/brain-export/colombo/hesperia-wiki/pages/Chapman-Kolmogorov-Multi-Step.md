# Chapman-Kolmogorov Multi-Step

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Formula / function  
**Responsible (module):** `sphere/propagation/multi_step_diffusion.py:21-72 (`propagate_k_steps`, `iterative_diffusion`)`  
**Value / default:** —

## Yields (formula)

v_k = v @ W^k (np.linalg.matrix_power) or iterative current=(1-α)current+α(current@W).

## Produced from (inputs)

- [Transition matrix (W)](../pages/Transition-matrix-W.md)

## Needed by (consumers)

- [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)
- *cumulativeDrift*

## Origin

Chapman (1928) / Kolmogorov (1931) — Theory Explainer: plain_lang: instead of one hop, raise the transition matrix to the k-th power (or repeat the lazy step) to see mass after many hops. author: Chapman–Kolmogorov equation lineage. extent: full (verbatim matrix_power / iterative). reasoning: multi-step diffusion + mixing diagnostics. application: [Mixing Diagnostics](../pages/Mixing-Diagnostics.md), [lambda (lazy step)](../pages/lambda-lazy-step.md), contrast dead [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md).

## Notes

**HWIKI-DOC-06:** Verified in `propagate_k_steps` (pure power) and `iterative_diffusion` (lazy α loop calling `diffuse_step`).

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md)
