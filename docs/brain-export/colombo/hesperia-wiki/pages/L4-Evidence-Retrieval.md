# L4 — Evidence Retrieval

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_4.py::compute_L4 (37_SPEC)`  
**Value / default:** 25

## In plain words

retrieves supporting text chunks (BM25) for both baseline and shadow runs, then scores how well retrieval actually backs up what L1/L2 measured structurally.

## Definition

- **Receives:** [BM25 retrieval](../pages/BM25-retrieval.md), [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- **Does:** Hub: retrieves supporting text chunks (BM25) for both baseline and shadow runs, then scores how well retrieval actually backs up what L1/L2 measured structurally.
- **Outputs:** `25` → [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md), [RETRIEVAL_MODE_ID](../pages/RETRIEVAL-MODE-ID.md), [TOP_K](../pages/TOP-K.md), [RETRIEVED_COUNT_BASELINE](../pages/RETRIEVED-COUNT-BASELINE.md), [RETRIEVED_COUNT_SHADOW](../pages/RETRIEVED-COUNT-SHADOW.md), [RETRIEVAL_SHORTFALL_BASELINE](../pages/RETRIEVAL-SHORTFALL-BASELINE.md), [RETRIEVAL_SHORTFALL_SHADOW](../pages/RETRIEVAL-SHORTFALL-SHADOW.md), [UNIQUE_BOOKS_BASELINE](../pages/UNIQUE-BOOKS-BASELINE.md), [UNIQUE_BOOKS_SHADOW](../pages/UNIQUE-BOOKS-SHADOW.md), [DUPLICATE_BOOK_RATIO_BASELINE](../pages/DUPLICATE-BOOK-RATIO-BASELINE.md), [DUPLICATE_BOOK_RATIO_SHADOW](../pages/DUPLICATE-BOOK-RATIO-SHADOW.md), [FAMILY_MATCH_COUNT_BASELINE](../pages/FAMILY-MATCH-COUNT-BASELINE.md), [FAMILY_MATCH_RATIO_BASELINE](../pages/FAMILY-MATCH-RATIO-BASELINE.md), [AREA_MATCH_RATIO_BASELINE](../pages/AREA-MATCH-RATIO-BASELINE.md), [TOP_K_FAMILY_COVERAGE_BASELINE](../pages/TOP-K-FAMILY-COVERAGE-BASELINE.md), [EVIDENCE_ENTROPY_BASELINE](../pages/EVIDENCE-ENTROPY-BASELINE.md), [EVIDENCE_GINI_BASELINE](../pages/EVIDENCE-GINI-BASELINE.md), [RANK_WEIGHTED_ALIGNMENT_BASELINE](../pages/RANK-WEIGHTED-ALIGNMENT-BASELINE.md), [HIT_EVIDENCE_OVERLAP_BASELINE](../pages/HIT-EVIDENCE-OVERLAP-BASELINE.md), [HIT_EVIDENCE_OVERLAP_SHADOW](../pages/HIT-EVIDENCE-OVERLAP-SHADOW.md), [EVIDENCE_JACCARD_BS](../pages/EVIDENCE-JACCARD-BS.md), [BOOKSET_JACCARD_BS](../pages/BOOKSET-JACCARD-BS.md), [EVIDENCE_SHIFT_SCORE](../pages/EVIDENCE-SHIFT-SCORE.md), [INTEGRITY_CHECK_PASS_RATIO](../pages/INTEGRITY-CHECK-PASS-RATIO.md), [EVIDENCE_SUPPORT_INDEX_BASELINE](../pages/EVIDENCE-SUPPORT-INDEX-BASELINE.md), [EVIDENCE_ACCEPTABILITY_GATE](../pages/EVIDENCE-ACCEPTABILITY-GATE.md), [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md), [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md), [ENTROPY_DROP_SIGNIFICANT](../pages/ENTROPY-DROP-SIGNIFICANT.md)
- **Exists for:** **HWIKI-CATALOG-L4:** Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04

## Yields (formula)

Hub: retrieves supporting text chunks (BM25) for both baseline and shadow runs, then scores how well retrieval actually backs up what L1/L2 measured structurally.

## Produced from (inputs)

- [BM25 retrieval](../pages/BM25-retrieval.md)
- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## Needed by (consumers)

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
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
- [FAMILY_MATCH_COUNT_BASELINE](../pages/FAMILY-MATCH-COUNT-BASELINE.md)
- [FAMILY_MATCH_RATIO_BASELINE](../pages/FAMILY-MATCH-RATIO-BASELINE.md)
- [AREA_MATCH_RATIO_BASELINE](../pages/AREA-MATCH-RATIO-BASELINE.md)
- [TOP_K_FAMILY_COVERAGE_BASELINE](../pages/TOP-K-FAMILY-COVERAGE-BASELINE.md)
- [EVIDENCE_ENTROPY_BASELINE](../pages/EVIDENCE-ENTROPY-BASELINE.md)
- [EVIDENCE_GINI_BASELINE](../pages/EVIDENCE-GINI-BASELINE.md)
- [RANK_WEIGHTED_ALIGNMENT_BASELINE](../pages/RANK-WEIGHTED-ALIGNMENT-BASELINE.md)
- [HIT_EVIDENCE_OVERLAP_BASELINE](../pages/HIT-EVIDENCE-OVERLAP-BASELINE.md)
- [HIT_EVIDENCE_OVERLAP_SHADOW](../pages/HIT-EVIDENCE-OVERLAP-SHADOW.md)
- [EVIDENCE_JACCARD_BS](../pages/EVIDENCE-JACCARD-BS.md)
- [BOOKSET_JACCARD_BS](../pages/BOOKSET-JACCARD-BS.md)
- [EVIDENCE_SHIFT_SCORE](../pages/EVIDENCE-SHIFT-SCORE.md)
- [INTEGRITY_CHECK_PASS_RATIO](../pages/INTEGRITY-CHECK-PASS-RATIO.md)
- [EVIDENCE_SUPPORT_INDEX_BASELINE](../pages/EVIDENCE-SUPPORT-INDEX-BASELINE.md)
- [EVIDENCE_ACCEPTABILITY_GATE](../pages/EVIDENCE-ACCEPTABILITY-GATE.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- [ENTROPY_DROP_SIGNIFICANT](../pages/ENTROPY-DROP-SIGNIFICANT.md)

## See also

- [BM25 retrieval](../pages/BM25-retrieval.md)
- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- [RETRIEVAL_MODE_ID](../pages/RETRIEVAL-MODE-ID.md)
- [TOP_K](../pages/TOP-K.md)
- [RETRIEVED_COUNT_BASELINE](../pages/RETRIEVED-COUNT-BASELINE.md)
- [RETRIEVED_COUNT_SHADOW](../pages/RETRIEVED-COUNT-SHADOW.md)
- [RETRIEVAL_SHORTFALL_BASELINE](../pages/RETRIEVAL-SHORTFALL-BASELINE.md)
- [RETRIEVAL_SHORTFALL_SHADOW](../pages/RETRIEVAL-SHORTFALL-SHADOW.md)
- [UNIQUE_BOOKS_BASELINE](../pages/UNIQUE-BOOKS-BASELINE.md)
- [UNIQUE_BOOKS_SHADOW](../pages/UNIQUE-BOOKS-SHADOW.md)

## Origin

Hesperia-native `37_SPEC` L4 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: retrieves supporting text chunks (BM25) for both baseline and shadow runs, then scores how well retrieval actually backs up what L1/L2 measured structurally. author: Hesperia wiki (core/layers/layer_4.py::compute_L4 (37_SPEC)). extent: full. reasoning: **HWIKI-CATALOG-L4:** Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04. application: [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L4:** Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
