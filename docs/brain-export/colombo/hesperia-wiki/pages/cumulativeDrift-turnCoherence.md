# cumulativeDrift / turnCoherence

**Status:** 🔴 DEAD — no implementation under this name or a successor formula  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a`  
**Value / default:** —

## Yields (formula)

Turn-to-turn coherence and cumulative drift via cosine similarity across a multi-turn session.

## Origin

Java 21_MATH

## Notes

**Cleanest 'taken toward, wrong boundary' case in the register.** [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) already computes the same shape (consecutive L1 distance + entropy along a state sequence) for within-run diffusion steps; nobody has moved that machinery to a turn-to-turn boundary yet. [cosine_similarity](../pages/cosine-similarity.md) (the other half of what this needed) already exists, repurposed for fingerprints.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md)
