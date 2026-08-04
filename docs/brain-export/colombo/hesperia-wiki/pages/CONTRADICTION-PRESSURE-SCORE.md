# CONTRADICTION_PRESSURE_SCORE

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_5.py::compute_L5 -> result["CONTRADICTION_PRESSURE_SCORE"]`  
**Value / default:** float

## In plain words

L5A's single composite read on how much genuine contradicting evidence exists — feeds L9 CONSISTENCY_U1000.

## Definition

- **Receives:** [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- **Does:** 0.55*neg_support + 0.25*(1-pos_support) + 0.20*bookset_jaccard
- **Outputs:** `float` → *no named wiki consumer yet*
- **Exists for:** L5 counter-evidence field — pressure against the dominant read

## Yields (formula)

0.55*neg_support + 0.25*(1-pos_support) + 0.20*bookset_jaccard

## Produced from (inputs)

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)

## See also

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
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
- [REALITY_GATE_COUNTER_EVIDENCE](../pages/REALITY-GATE-COUNTER-EVIDENCE.md)

## Origin

Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: L5A's single composite read on how much genuine contradicting evidence exists — feeds L9 CONSISTENCY_U1000.. author: Hesperia L5 (38_SPEC / output_catalog §5). extent: full. reasoning: L5 counter-evidence field — pressure against the dominant read. application: [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md), L7.

## Notes

**HWIKI-CATALOG-L5 / HWIKI-PLAIN:** L5A's single composite read on how much genuine contradicting evidence exists — feeds L9 CONSISTENCY_U1000. Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
