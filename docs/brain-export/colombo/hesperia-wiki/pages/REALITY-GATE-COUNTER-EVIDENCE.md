# REALITY_GATE_COUNTER_EVIDENCE

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_5.py::compute_L5 -> result["REALITY_GATE_COUNTER_EVIDENCE"]`  
**Value / default:** bool

## In plain words

Hard pass/fail gate on the counter-evidence half — gates L7's g9 guard.

## Definition

- **Receives:** [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- **Does:** integrity, shortfall, and pressure all within policy caps
- **Outputs:** `bool` → *no named wiki consumer yet*
- **Exists for:** L5 counter-evidence field — pressure against the dominant read

## Yields (formula)

integrity, shortfall, and pressure all within policy caps

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
- [CONTRADICTION_PRESSURE_SCORE](../pages/CONTRADICTION-PRESSURE-SCORE.md)

## Origin

Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Hard pass/fail gate on the counter-evidence half — gates L7's g9 guard.. author: Hesperia L5 (38_SPEC / output_catalog §5). extent: full. reasoning: L5 counter-evidence field — pressure against the dominant read. application: [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md), L7.

## Notes

**HWIKI-CATALOG-L5 / HWIKI-PLAIN:** Hard pass/fail gate on the counter-evidence half — gates L7's g9 guard. Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
