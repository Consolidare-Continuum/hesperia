# Jaccard overlaps

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Similarity and Retrieval](../categories/Similarity-and-Retrieval.md)  
**Type:** Formula / function  
**Responsible (module):** `core/layers/layer_3.py (VISITED_JACCARD_SIMILARITY); layer_4._jaccard`  
**Value / default:** —

## Yields (formula)

Set overlap |A∩B|/|A∪B| — HIT/VISITED/evidence/bookset overlap variables.

## Needed by (consumers)

- [BM25 retrieval](../pages/BM25-retrieval.md)
- [cosine_similarity](../pages/cosine-similarity.md)

## Origin

Paul Jaccard (1901) — Theory Explainer: plain_lang: of the union of two sets, what fraction is shared — overlap without caring about order. author: Paul Jaccard (1901). extent: full (verbatim). reasoning: SCIENCE.md L3/L4 lineage table. application: VISITED_JACCARD_SIMILARITY, HIT_EVIDENCE_OVERLAP_*, EVIDENCE_JACCARD_BS, BOOKSET_JACCARD_BS.

## Notes

**HWIKI-DOC-16:** Product overlap applications across L3/L4.

---
[← back to category](../categories/Similarity-and-Retrieval.md) · [wiki home](../index.md)
