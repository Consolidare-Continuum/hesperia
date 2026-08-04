# NEG_AREA_MATCH_RATIO

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_5.py::compute_L5 -> result["NEG_AREA_MATCH_RATIO"]`  
**Value / default:** float [0,1]

## In plain words

How much of the counter-evidence still lands in the dominant area — high values here weaken the 'genuine contradiction' read.

## Definition

- **Receives:** [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- **Does:** count(counter-evidence in dominant area) / [RETRIEVED_COUNT_NEG](../pages/RETRIEVED-COUNT-NEG.md)
- **Outputs:** `float [0,1]` → *no named wiki consumer yet*
- **Exists for:** L5 counter-evidence field — pressure against the dominant read

## Yields (formula)

count(counter-evidence in dominant area) / [RETRIEVED_COUNT_NEG](../pages/RETRIEVED-COUNT-NEG.md)

## Produced from (inputs)

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)

## See also

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- [ANTI_REGION_SIZE](../pages/ANTI-REGION-SIZE.md)
- [RETRIEVED_COUNT_NEG](../pages/RETRIEVED-COUNT-NEG.md)
- [NEG_SHORTFALL](../pages/NEG-SHORTFALL.md)
- [NEG_UNIQUE_BOOKS](../pages/NEG-UNIQUE-BOOKS.md)
- [NEG_DUPLICATE_BOOK_RATIO](../pages/NEG-DUPLICATE-BOOK-RATIO.md)
- [POS_NEG_BOOKSET_JACCARD](../pages/POS-NEG-BOOKSET-JACCARD.md)
- [POS_NEG_CHUNK_JACCARD](../pages/POS-NEG-CHUNK-JACCARD.md)
- [POS_SUPPORT_INDEX](../pages/POS-SUPPORT-INDEX.md)
- [NEG_SUPPORT_INDEX](../pages/NEG-SUPPORT-INDEX.md)
- [CONTRADICTION_PRESSURE_SCORE](../pages/CONTRADICTION-PRESSURE-SCORE.md)
- [REALITY_GATE_COUNTER_EVIDENCE](../pages/REALITY-GATE-COUNTER-EVIDENCE.md)

## Origin

Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: How much of the counter-evidence still lands in the dominant area — high values here weaken the 'genuine contradiction' read.. author: Hesperia L5 (38_SPEC / output_catalog §5). extent: full. reasoning: L5 counter-evidence field — pressure against the dominant read. application: [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md), L7.

## Notes

**HWIKI-CATALOG-L5 / HWIKI-PLAIN:** How much of the counter-evidence still lands in the dominant area — high values here weaken the 'genuine contradiction' read. Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
