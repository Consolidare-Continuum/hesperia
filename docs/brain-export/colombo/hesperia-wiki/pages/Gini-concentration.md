# Gini concentration

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Entropy and Information Theory](../categories/Entropy-and-Information-Theory.md)  
**Type:** Formula / function  
**Responsible (module):** `core/layers/layer_1.py:_compute_gini (GINI_COEFFICIENT); also layer_4._gini`  
**Value / default:** —

## Yields (formula)

Sorted-array Gini coefficient — concentration alongside entropy (the two can disagree in direction on the same distribution).

## Needed by (consumers)

- [entropy_threshold (monotony)](../pages/entropy-threshold-monotony.md)
- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## Origin

Corrado Gini (1912), *Variabilità e mutabilità* — Theory Explainer: plain_lang: how unevenly hits/activation are piled onto a few families versus spread evenly — inequality as concentration. author: Corrado Gini (1912). extent: full (verbatim sorted-array Gini). reasoning: SCIENCE.md L1; independent concentration measure alongside Shannon. application: L1 `GINI_COEFFICIENT`, L3 `GINI_DELTA`, L4 `EVIDENCE_GINI_BASELINE`; pairs with [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md).

## Notes

**HWIKI-DOC-14:** Concentration alongside entropy — not a Shannon substitute.

---
[← back to category](../categories/Entropy-and-Information-Theory.md) · [wiki home](../index.md)
