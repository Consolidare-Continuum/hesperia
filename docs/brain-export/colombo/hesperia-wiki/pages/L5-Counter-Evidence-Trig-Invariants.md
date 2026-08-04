# L5 — Counter-Evidence & Trig Invariants

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_5.py::compute_L5 (38_SPEC)`  
**Value / default:** 25 (12 counter-evidence + 13 trig)

## In plain words

two unrelated jobs sharing one layer — 5A retrieves and scores evidence AGAINST the dominant read (contradiction pressure); 5B self-tests the vector-space math itself (dot product, norm, angle axioms) as a sanity gate, not a content measurement.

## Definition

- **Receives:** [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- **Does:** Hub: two unrelated jobs sharing one layer — 5A retrieves and scores evidence AGAINST the dominant read (contradiction pressure); 5B self-tests the vector-space math itself (dot product, norm, angle axioms) as a sanity gate, not a content measurement.
- **Outputs:** `25 (12 counter-evidence + 13 trig)` → [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md), [ANTI_REGION_SIZE](../pages/ANTI-REGION-SIZE.md), [RETRIEVED_COUNT_NEG](../pages/RETRIEVED-COUNT-NEG.md), [NEG_SHORTFALL](../pages/NEG-SHORTFALL.md), [NEG_UNIQUE_BOOKS](../pages/NEG-UNIQUE-BOOKS.md), [NEG_DUPLICATE_BOOK_RATIO](../pages/NEG-DUPLICATE-BOOK-RATIO.md), [NEG_AREA_MATCH_RATIO](../pages/NEG-AREA-MATCH-RATIO.md), [POS_NEG_BOOKSET_JACCARD](../pages/POS-NEG-BOOKSET-JACCARD.md), [POS_NEG_CHUNK_JACCARD](../pages/POS-NEG-CHUNK-JACCARD.md), [POS_SUPPORT_INDEX](../pages/POS-SUPPORT-INDEX.md), [NEG_SUPPORT_INDEX](../pages/NEG-SUPPORT-INDEX.md), [CONTRADICTION_PRESSURE_SCORE](../pages/CONTRADICTION-PRESSURE-SCORE.md), [REALITY_GATE_COUNTER_EVIDENCE](../pages/REALITY-GATE-COUNTER-EVIDENCE.md), [DOT_SYMMETRY_RESIDUAL](../pages/DOT-SYMMETRY-RESIDUAL.md), [DOT_SELF_NONNEG_RESIDUAL](../pages/DOT-SELF-NONNEG-RESIDUAL.md), [NORM_CONSISTENCY_RESIDUAL](../pages/NORM-CONSISTENCY-RESIDUAL.md), [COSI_CLAMP_VIOLATION_COUNT](../pages/COSI-CLAMP-VIOLATION-COUNT.md), [ANGLE_RANGE_VIOLATION_COUNT](../pages/ANGLE-RANGE-VIOLATION-COUNT.md), [LAW_OF_COSINES_RESIDUAL](../pages/LAW-OF-COSINES-RESIDUAL.md), [SIN_COS_IDENTITY_RESIDUAL](../pages/SIN-COS-IDENTITY-RESIDUAL.md), [ROTATION_NORM_PRESERVATION_RESIDUAL](../pages/ROTATION-NORM-PRESERVATION-RESIDUAL.md), [ORTHONORMALITY_RESIDUAL_FROBENIUS](../pages/ORTHONORMALITY-RESIDUAL-FROBENIUS.md), [TRIANGLE_INEQUALITY_VIOLATION_COUNT](../pages/TRIANGLE-INEQUALITY-VIOLATION-COUNT.md), [METRIC_SYMMETRY_RESIDUAL](../pages/METRIC-SYMMETRY-RESIDUAL.md), [METRIC_IDENTITY_RESIDUAL](../pages/METRIC-IDENTITY-RESIDUAL.md), [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Exists for:** **HWIKI-CATALOG-L5:** Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04

## Yields (formula)

Hub: two unrelated jobs sharing one layer — 5A retrieves and scores evidence AGAINST the dominant read (contradiction pressure); 5B self-tests the vector-space math itself (dot product, norm, angle axioms) as a sanity gate, not a content measurement.

## Produced from (inputs)

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## Needed by (consumers)

- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [ANTI_REGION_SIZE](../pages/ANTI-REGION-SIZE.md)
- [RETRIEVED_COUNT_NEG](../pages/RETRIEVED-COUNT-NEG.md)
- [NEG_SHORTFALL](../pages/NEG-SHORTFALL.md)
- [NEG_UNIQUE_BOOKS](../pages/NEG-UNIQUE-BOOKS.md)
- [NEG_DUPLICATE_BOOK_RATIO](../pages/NEG-DUPLICATE-BOOK-RATIO.md)
- [NEG_AREA_MATCH_RATIO](../pages/NEG-AREA-MATCH-RATIO.md)
- [POS_NEG_BOOKSET_JACCARD](../pages/POS-NEG-BOOKSET-JACCARD.md)
- [POS_NEG_CHUNK_JACCARD](../pages/POS-NEG-CHUNK-JACCARD.md)
- [POS_SUPPORT_INDEX](../pages/POS-SUPPORT-INDEX.md)
- [NEG_SUPPORT_INDEX](../pages/NEG-SUPPORT-INDEX.md)
- [CONTRADICTION_PRESSURE_SCORE](../pages/CONTRADICTION-PRESSURE-SCORE.md)
- [REALITY_GATE_COUNTER_EVIDENCE](../pages/REALITY-GATE-COUNTER-EVIDENCE.md)
- [DOT_SYMMETRY_RESIDUAL](../pages/DOT-SYMMETRY-RESIDUAL.md)
- [DOT_SELF_NONNEG_RESIDUAL](../pages/DOT-SELF-NONNEG-RESIDUAL.md)
- [NORM_CONSISTENCY_RESIDUAL](../pages/NORM-CONSISTENCY-RESIDUAL.md)
- [COSI_CLAMP_VIOLATION_COUNT](../pages/COSI-CLAMP-VIOLATION-COUNT.md)
- [ANGLE_RANGE_VIOLATION_COUNT](../pages/ANGLE-RANGE-VIOLATION-COUNT.md)
- [LAW_OF_COSINES_RESIDUAL](../pages/LAW-OF-COSINES-RESIDUAL.md)
- [SIN_COS_IDENTITY_RESIDUAL](../pages/SIN-COS-IDENTITY-RESIDUAL.md)
- [ROTATION_NORM_PRESERVATION_RESIDUAL](../pages/ROTATION-NORM-PRESERVATION-RESIDUAL.md)
- [ORTHONORMALITY_RESIDUAL_FROBENIUS](../pages/ORTHONORMALITY-RESIDUAL-FROBENIUS.md)
- [TRIANGLE_INEQUALITY_VIOLATION_COUNT](../pages/TRIANGLE-INEQUALITY-VIOLATION-COUNT.md)
- [METRIC_SYMMETRY_RESIDUAL](../pages/METRIC-SYMMETRY-RESIDUAL.md)
- [METRIC_IDENTITY_RESIDUAL](../pages/METRIC-IDENTITY-RESIDUAL.md)
- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## See also

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [ANTI_REGION_SIZE](../pages/ANTI-REGION-SIZE.md)
- [RETRIEVED_COUNT_NEG](../pages/RETRIEVED-COUNT-NEG.md)
- [NEG_SHORTFALL](../pages/NEG-SHORTFALL.md)
- [NEG_UNIQUE_BOOKS](../pages/NEG-UNIQUE-BOOKS.md)
- [NEG_DUPLICATE_BOOK_RATIO](../pages/NEG-DUPLICATE-BOOK-RATIO.md)
- [NEG_AREA_MATCH_RATIO](../pages/NEG-AREA-MATCH-RATIO.md)
- [POS_NEG_BOOKSET_JACCARD](../pages/POS-NEG-BOOKSET-JACCARD.md)
- [POS_NEG_CHUNK_JACCARD](../pages/POS-NEG-CHUNK-JACCARD.md)
- [POS_SUPPORT_INDEX](../pages/POS-SUPPORT-INDEX.md)
- [NEG_SUPPORT_INDEX](../pages/NEG-SUPPORT-INDEX.md)

## Origin

Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: two unrelated jobs sharing one layer — 5A retrieves and scores evidence AGAINST the dominant read (contradiction pressure); 5B self-tests the vector-space math itself (dot product, norm, angle axioms) as a sanity gate, not a content measurement. author: Hesperia wiki (core/layers/layer_5.py::compute_L5 (38_SPEC)). extent: full. reasoning: **HWIKI-CATALOG-L5:** Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04. application: [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L5:** Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
