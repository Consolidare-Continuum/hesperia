# Mixing Diagnostics

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Formula / function  
**Responsible (module):** `sphere/propagation/multi_step_diffusion.py:75-103 (`propagation_depth_metric`)`  
**Value / default:** —

## In plain words

measures how fast a walk sequence spreads (L1 step sizes) and how disordered each snapshot is (normalized Shannon).

## Definition

- **Receives:** [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md), [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- **Does:** propagation_depth_metric(seq): consecutive_l1[i]=Σ|s[i+1]-s[i]| (via vector_sum abs); entropy_sequence[i]=compute_normalized_entropy(s[i]); depth=len(seq)-1.
- **Outputs:** `—` → *cumulativeDrift*
- **Exists for:** shipped for multi-step diffusion diagnostics, not turn boundaries

## Yields (formula)

propagation_depth_metric(seq): consecutive_l1[i]=Σ|s[i+1]-s[i]| (via vector_sum abs); entropy_sequence[i]=compute_normalized_entropy(s[i]); depth=len(seq)-1.

## Produced from (inputs)

- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)
- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)

## Needed by (consumers)

- *cumulativeDrift*

## See also

- [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md)
- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- [PageRank-shaped walk (structural analogy)](../pages/PageRank-shaped-walk-structural-analogy.md)
- [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md)

## Origin

Markov-chain mixing characterization (applied) — Theory Explainer: plain_lang: measures how fast a walk sequence spreads (L1 step sizes) and how disordered each snapshot is (normalized Shannon). author: applied mixing / information theory (no single eponym; entropy via Shannon 1948). extent: full (within-run). reasoning: shipped for multi-step diffusion diagnostics, not turn boundaries. application: [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md), [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md), contrast dead [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md).

## Notes

**HWIKI-OPEN-03 / DOC-07 re-read 2026-07-23 (line-by-line):** function is `propagation_depth_metric` — returns dict keys `depth`, `consecutive_l1`, `entropy_sequence`. Entropy calls `core.math.entropy_metrics.compute_normalized_entropy` (canonical Shannon path), not a local copy. Empty/short/mismatched sequences return zeros. **Confidence lifted** — no longer UNVERIFIED companion-doc paraphrase. Structurally same shape as dead [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md), different boundary (within-run steps vs turn-to-turn).

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
