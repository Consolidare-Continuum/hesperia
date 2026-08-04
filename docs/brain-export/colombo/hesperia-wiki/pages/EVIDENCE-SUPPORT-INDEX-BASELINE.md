# EVIDENCE_SUPPORT_INDEX_BASELINE

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_4.py::compute_L4 -> result["EVIDENCE_SUPPORT_INDEX_BASELINE"]`  
**Value / default:** float [0,1]

## In plain words

L4's single most load-bearing output — the composite read on how well retrieved evidence actually supports what was structurally measured. Traces through L7/L8 rescale to L9 PILLAR_EVIDENCE_U1000 (see output_catalog.md's worked 'Trust' example).

## Definition

- **Receives:** [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- **Does:** 0.45*FAMILY_MATCH_RATIO + 0.35*AREA_MATCH_RATIO + 0.20*HIT_EVIDENCE_OVERLAP
- **Outputs:** `float [0,1]` → *no named wiki consumer yet*
- **Exists for:** L4 evidence-retrieval field — how well retrieved text backs structural measures

## Yields (formula)

0.45*FAMILY_MATCH_RATIO + 0.35*AREA_MATCH_RATIO + 0.20*HIT_EVIDENCE_OVERLAP

## Produced from (inputs)

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## See also

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [ENTROPY_DROP_SIGNIFICANT](../pages/ENTROPY-DROP-SIGNIFICANT.md)
- [RETRIEVAL_MODE_ID](../pages/RETRIEVAL-MODE-ID.md)
- [TOP_K](../pages/TOP-K.md)
- [RETRIEVED_COUNT_BASELINE](../pages/RETRIEVED-COUNT-BASELINE.md)
- [RETRIEVED_COUNT_SHADOW](../pages/RETRIEVED-COUNT-SHADOW.md)
- [RETRIEVAL_SHORTFALL_BASELINE](../pages/RETRIEVAL-SHORTFALL-BASELINE.md)
- [RETRIEVAL_SHORTFALL_SHADOW](../pages/RETRIEVAL-SHORTFALL-SHADOW.md)
- [UNIQUE_BOOKS_BASELINE](../pages/UNIQUE-BOOKS-BASELINE.md)
- [UNIQUE_BOOKS_SHADOW](../pages/UNIQUE-BOOKS-SHADOW.md)
- [DUPLICATE_BOOK_RATIO_BASELINE](../pages/DUPLICATE-BOOK-RATIO-BASELINE.md)
- [DUPLICATE_BOOK_RATIO_SHADOW](../pages/DUPLICATE-BOOK-RATIO-SHADOW.md)

## Origin

Hesperia-native `37_SPEC` L4 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: L4's single most load-bearing output — the composite read on how well retrieved evidence actually supports what was structurally measured. Traces through L7/L8 rescale to L9 PILLAR_EVIDENCE_U1000 (see output_catalog.md's worked 'Trust' example).. author: Hesperia L4 (37_SPEC / output_catalog §4). extent: full. reasoning: L4 evidence-retrieval field — how well retrieved text backs structural measures. application: [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), L5–L9.

## Notes

**HWIKI-CATALOG-L4 / HWIKI-PLAIN:** L4's single most load-bearing output — the composite read on how well retrieved evidence actually supports what was structurally measured. Traces through L7/L8 rescale to L9 PILLAR_EVIDENCE_U1000 (see output_catalog.md's worked 'Trust' example). Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
