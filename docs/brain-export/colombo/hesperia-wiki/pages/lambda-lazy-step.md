# lambda (lazy step)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py — base_step()`  
**Value / default:** 0.55

## Yields (formula)

D = (1-lambda)·E + lambda·(E·W) — lazy Markov chain step: a (1-lambda) fraction stays put, lambda actually transitions via W.

## Produced from (inputs)

- [E_cap](../pages/E-cap.md)
- [Transition matrix (W)](../pages/Transition-matrix-W.md)

## Needed by (consumers)

- [decay](../pages/decay.md)
- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)
- [Wiener feedback on alpha (k_s / k_j)](../pages/Wiener-feedback-on-alpha-k-s-k-j.md)
- [PageRank-shaped walk (structural analogy)](../pages/PageRank-shaped-walk-structural-analogy.md)

## Origin

Markov (1906) — Theory Explainer: plain_lang: each step keeps part of current energy and mixes in neighbor energy; λ is how much of the mix comes from the graph. author: A.A. Markov (1906) chain formalism; laziness = standard aperiodicity technique. extent: structural_analogy (hand-set weights, not fitted HMM). reasoning: 22_SPEC base_step; 'Markov-like' discipline in SCIENCE.md. application: [Transition matrix (W)](../pages/Transition-matrix-W.md), T_steps=8, [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md), [PageRank-shaped walk (structural analogy)](../pages/PageRank-shaped-walk-structural-analogy.md), diffusion α modulated by [Wiener feedback on alpha (k_s / k_j)](../pages/Wiener-feedback-on-alpha-k-s-k-j.md).

## Notes

**HWIKI-DOC-04 / DOC-08:** Iterated T_steps=8 times per run. Terminology discipline: 'Markov-like', never 'fitted Markov chain / HMM' — weights are hand-set, not learned. Same lazy form is the PageRank structural analogy (SCIENCE.md) — see [PageRank-shaped walk (structural analogy)](../pages/PageRank-shaped-walk-structural-analogy.md). Distinct from [Wiener feedback on alpha (k_s / k_j)](../pages/Wiener-feedback-on-alpha-k-s-k-j.md) which modulates *diffusion* α in `sphere/propagation/weighting.py`, not this fusion/lazy λ.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md)
