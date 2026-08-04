# cumulativeDrift / turnCoherence

**Status:** 🔴 DEAD — no implementation under this name or a successor formula  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a`  
**Value / default:** —

## In plain words

Turn-to-turn coherence and cumulative drift via cosine similarity across a multi-turn session.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Turn-to-turn coherence and cumulative drift via cosine similarity across a multi-turn session.
- **Outputs:** `—` → [cosine_similarity](../pages/cosine-similarity.md), [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)
- **Exists for:** **Cleanest 'taken toward, wrong boundary' case in the register.** [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) already computes the same shape (consecutive L1 distance + entropy along a state sequence) for within-run diffusion steps; nobody has moved that machinery 

## Yields (formula)

Turn-to-turn coherence and cumulative drift via cosine similarity across a multi-turn session.

## Needed by (consumers)

- [cosine_similarity](../pages/cosine-similarity.md)
- [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)

## See also

- [cosine_similarity](../pages/cosine-similarity.md)
- [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)

## Origin

Java 21_MATH — Theory Explainer: plain_lang: Turn-to-turn coherence and cumulative drift via cosine similarity across a multi-turn session. author: Hesperia wiki (n/a). extent: dead. reasoning: **Cleanest 'taken toward, wrong boundary' case in the register.** [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) already computes the same shape (consecutive L1 distance + entropy along a state sequence) for within-run diffusion steps; nobody has moved that machinery . application: Dead and Rejected Science.

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **Cleanest 'taken toward, wrong boundary' case in the register.** [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) already computes the same shape (consecutive L1 distance + entropy along a state sequence) for within-run diffusion steps; nobody has moved that machinery to a turn-to-turn boundary yet. [cosine_similarity](../pages/cosine-similarity.md) (the other half of what this needed) already exists, repurposed for fingerprints.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
