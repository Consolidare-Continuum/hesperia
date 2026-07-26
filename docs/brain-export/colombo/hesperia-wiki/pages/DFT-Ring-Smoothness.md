# DFT Ring Smoothness

**Status:** 🔴 REJECTED — explicit, reasoned decision against, not an oversight  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a — zero matches for `np.fft`/`scipy.fft`/`ringSmoothness` in any `.py``  
**Value / default:** —

## Yields (formula)

Fourier/DFT-based smoothness measure over a proposed 12-area ring (`AREA_RING_ORDER`), plus a Java `Complex` class.

## Produced from (inputs)

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Origin

Java 21_MATH §10 / 23_PROTOTYPE — Theory Explainer: plain_lang: a ring Fourier smoothness score needs areas arranged on a circle (each has two neighbors); Hesperia's areas sit on an icosahedron where each has five neighbors — wrong topology for that DFT. author: Java proposal (DFT/ringSmoothness); rejection is Hesperia geometry decision. extent: rejected_with_reason. reasoning: [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md) is 5-regular (`degree_per_node: 5` in adjacency JSON); ring-DFT needs 2-regular C₁₂. application: contrast [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md) / dominance already covering 'smoothness-like' questions.

## Notes

**HWIKI-DOC-11:** Topology incompatibility — Felix verify degree: `data/topology/area_adjacency_matrix.json` `degree_per_node: 5`. Not an oversight.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md)
