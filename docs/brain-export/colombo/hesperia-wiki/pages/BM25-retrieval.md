# BM25 retrieval

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Similarity and Retrieval](../categories/Similarity-and-Retrieval.md)  
**Type:** Algorithm  
**Responsible (module):** `core/layers/layer_4.py + defaults RETRIEVAL_MODE_ID`  
**Value / default:** RETRIEVAL_MODE_ID=LEX_BM25_V1

## Yields (formula)

Standard BM25 ranking for L4 lexical evidence retrieval.

## Needed by (consumers)

- [Jaccard overlaps](../pages/Jaccard-overlaps.md)

## Origin

Robertson & Spärck Jones (1976) — Theory Explainer: plain_lang: classic search ranking that scores how well a query's terms match a document, with length normalization. author: Stephen Robertson & Karen Spärck Jones (1976), crystallized through TREC. extent: full (verbatim lexical retrieval function). reasoning: SCIENCE.md L4; BEYOND Java corpus. application: L4 evidence retrieval path; pairs with [Jaccard overlaps](../pages/Jaccard-overlaps.md) overlap diagnostics.

## Notes

**HWIKI-DOC-15:** Not proposed in the Java corpus — BEYOND retrieval path.

---
[← back to category](../categories/Similarity-and-Retrieval.md) · [wiki home](../index.md)
