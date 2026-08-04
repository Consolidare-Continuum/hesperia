# PageRank-shaped walk (structural analogy)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Concept Dictionary](../categories/Concept-Dictionary.md)  
**Type:** Concept / theory term  
**Responsible (module):** `docs/publication/SCIENCE.md lineage table; core/math/core_math.py base_step`  
**Value / default:** v' = (1−λ)v + λ·vW (lazy form)

## In plain words

PageRank spreads importance by repeatedly mixing 'stay put' with 'follow a link'; Hesperia reuses that *shape* for energy diffusion on areas, not ranking web pages.

## Definition

- **Receives:** [lambda (lazy step)](../pages/lambda-lazy-step.md), [Transition matrix (W)](../pages/Transition-matrix-W.md)
- **Does:** Structural analogy only: the lazy-random-walk mixing form matches PageRank's damping walk; Hesperia's W is semantic adjacency, not a web-link graph, and no eigenvector-convergence claim is made.
- **Outputs:** `v' = (1−λ)v + λ·vW (lazy form)` → [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md), [Mixing Diagnostics](../pages/Mixing-Diagnostics.md), [structural analogy (extent term)](../pages/structural-analogy-extent-term.md)
- **Exists for:** SCIENCE.md cites the form explicitly; do not claim PageRank product semantics

## Yields (formula)

Structural analogy only: the lazy-random-walk mixing form matches PageRank's damping walk; Hesperia's W is semantic adjacency, not a web-link graph, and no eigenvector-convergence claim is made.

## Produced from (inputs)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [Transition matrix (W)](../pages/Transition-matrix-W.md)

## Needed by (consumers)

- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)
- [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)
- [structural analogy (extent term)](../pages/structural-analogy-extent-term.md)

## See also

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [Transition matrix (W)](../pages/Transition-matrix-W.md)
- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)
- [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)
- [structural analogy (extent term)](../pages/structural-analogy-extent-term.md)
- [Markov-like (term)](../pages/Markov-like-term.md)

## Origin

Brin & Page (1998), 'The Anatomy of a Large-Scale Hypertextual Web Search Engine' — Theory Explainer: plain_lang: PageRank spreads importance by repeatedly mixing 'stay put' with 'follow a link'; Hesperia reuses that *shape* for energy diffusion on areas, not ranking web pages. author: Sergey Brin & Larry Page (1998). extent: structural_analogy only. reasoning: SCIENCE.md cites the form explicitly; do not claim PageRank product semantics. application: [lambda (lazy step)](../pages/lambda-lazy-step.md), [Transition matrix (W)](../pages/Transition-matrix-W.md), [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md).

## Notes

**HWIKI-DOC-08:** Cite SCIENCE.md — structural analogy only; never claim Hesperia runs PageRank.

---
[← back to category](../categories/Concept-Dictionary.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
