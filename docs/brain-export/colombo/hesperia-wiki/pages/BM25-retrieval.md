# BM25 retrieval

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Similarity and Retrieval](../categories/Similarity-and-Retrieval.md)  
**Type:** Algorithm  
**Responsible (module):** `core/layers/layer_4.py + defaults RETRIEVAL_MODE_ID`  
**Value / default:** RETRIEVAL_MODE_ID=LEX_BM25_V1

## In plain words

classic search ranking that scores how well a query's terms match a document, with length normalization.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Standard BM25 ranking for L4 lexical evidence retrieval.
- **Outputs:** `RETRIEVAL_MODE_ID=LEX_BM25_V1` → [Jaccard overlaps](../pages/Jaccard-overlaps.md), [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- **Exists for:** SCIENCE.md L4; BEYOND Java corpus

## Yields (formula)

Standard BM25 ranking for L4 lexical evidence retrieval.

## Needed by (consumers)

- [Jaccard overlaps](../pages/Jaccard-overlaps.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## See also

- [Jaccard overlaps](../pages/Jaccard-overlaps.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## Origin

Robertson & Spärck Jones (1976) — Theory Explainer: plain_lang: classic search ranking that scores how well a query's terms match a document, with length normalization. author: Stephen Robertson & Karen Spärck Jones (1976), crystallized through TREC. extent: full (verbatim lexical retrieval function). reasoning: SCIENCE.md L4; BEYOND Java corpus. application: L4 evidence retrieval path; pairs with [Jaccard overlaps](../pages/Jaccard-overlaps.md) overlap diagnostics.

## Notes

**HWIKI-DOC-15:** Not proposed in the Java corpus — BEYOND retrieval path.

---
[← back to category](../categories/Similarity-and-Retrieval.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
