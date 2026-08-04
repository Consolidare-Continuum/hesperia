# RETRIEVAL_MODE_ID

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Parameter (flag)  
**Responsible (module):** `core/layers/layer_4.py::compute_L4 -> result["RETRIEVAL_MODE_ID"]`  
**Value / default:** string

## In plain words

Identifies which retrieval engine produced this layer's output — currently always the lexical BM25 implementation.

## Definition

- **Receives:** [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- **Does:** "LEX_BM25_V1"
- **Outputs:** `string` → *no named wiki consumer yet*
- **Exists for:** L4 evidence-retrieval field — how well retrieved text backs structural measures

## Yields (formula)

"LEX_BM25_V1"

## Produced from (inputs)

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## See also

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [ENTROPY_DROP_SIGNIFICANT](../pages/ENTROPY-DROP-SIGNIFICANT.md)
- [TOP_K](../pages/TOP-K.md)
- [RETRIEVED_COUNT_BASELINE](../pages/RETRIEVED-COUNT-BASELINE.md)
- [RETRIEVED_COUNT_SHADOW](../pages/RETRIEVED-COUNT-SHADOW.md)
- [RETRIEVAL_SHORTFALL_BASELINE](../pages/RETRIEVAL-SHORTFALL-BASELINE.md)
- [RETRIEVAL_SHORTFALL_SHADOW](../pages/RETRIEVAL-SHORTFALL-SHADOW.md)
- [UNIQUE_BOOKS_BASELINE](../pages/UNIQUE-BOOKS-BASELINE.md)
- [UNIQUE_BOOKS_SHADOW](../pages/UNIQUE-BOOKS-SHADOW.md)
- [DUPLICATE_BOOK_RATIO_BASELINE](../pages/DUPLICATE-BOOK-RATIO-BASELINE.md)
- [DUPLICATE_BOOK_RATIO_SHADOW](../pages/DUPLICATE-BOOK-RATIO-SHADOW.md)
- [FAMILY_MATCH_COUNT_BASELINE](../pages/FAMILY-MATCH-COUNT-BASELINE.md)

## Origin

Hesperia-native `37_SPEC` L4 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Identifies which retrieval engine produced this layer's output — currently always the lexical BM25 implementation.. author: Hesperia L4 (37_SPEC / output_catalog §4). extent: full. reasoning: L4 evidence-retrieval field — how well retrieved text backs structural measures. application: [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), L5–L9.

## Notes

**HWIKI-CATALOG-L4 / HWIKI-PLAIN:** Identifies which retrieval engine produced this layer's output — currently always the lexical BM25 implementation. Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
