# TOP_K

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/layers/layer_4.py::compute_L4 -> result["TOP_K"]`  
**Value / default:** int

## In plain words

Target retrieval count — how many chunks the engine tries to return.

## Definition

- **Receives:** [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- **Does:** 20 (default)
- **Outputs:** `int` → *no named wiki consumer yet*
- **Exists for:** L4 evidence-retrieval field — how well retrieved text backs structural measures

## Yields (formula)

20 (default)

## Produced from (inputs)

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## See also

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [ENTROPY_DROP_SIGNIFICANT](../pages/ENTROPY-DROP-SIGNIFICANT.md)
- [RETRIEVAL_MODE_ID](../pages/RETRIEVAL-MODE-ID.md)
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

Hesperia-native `37_SPEC` L4 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Target retrieval count — how many chunks the engine tries to return.. author: Hesperia L4 (37_SPEC / output_catalog §4). extent: full. reasoning: L4 evidence-retrieval field — how well retrieved text backs structural measures. application: [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), L5–L9.

## Notes

**HWIKI-CATALOG-L4 / HWIKI-PLAIN:** Target retrieval count — how many chunks the engine tries to return. Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
