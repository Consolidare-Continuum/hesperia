# LAW_OF_COSINES_RESIDUAL

**Status:** 🟡 PARTIAL — present in a narrow slice/tool, not the full contract  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Derived variable (self-test)  
**Responsible (module):** `core/layers/layer_5.py::compute_L5 -> result["LAW_OF_COSINES_RESIDUAL"]`  
**Value / default:** float/int, near-zero expected

## In plain words

Reserved for a future non-deterministic-input mode — not a live computation today. The code sets this literal 0.0, explicitly flagged as reserved, not silently omitted.

## Definition

- **Receives:** [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- **Does:** hardcoded 0.0
- **Outputs:** `float/int, near-zero expected` → [REALITY_GATE_TRIG](../pages/REALITY-GATE-TRIG.md)
- **Exists for:** vector-space axiom self-test — not a content measurement

## Yields (formula)

hardcoded 0.0

## Produced from (inputs)

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)

## Needed by (consumers)

- [REALITY_GATE_TRIG](../pages/REALITY-GATE-TRIG.md)

## See also

- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- [REALITY_GATE_TRIG](../pages/REALITY-GATE-TRIG.md)
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

Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Reserved for a future non-deterministic-input mode — not a live computation today. The code sets this literal 0.0, explicitly flagged as reserved, not silently omitted.. author: Hesperia L5 trig self-test (38_SPEC). extent: partial. reasoning: vector-space axiom self-test — not a content measurement. application: [REALITY_GATE_TRIG](../pages/REALITY-GATE-TRIG.md), L7 g8.

## Notes

**HWIKI-CATALOG-L5 / HWIKI-PLAIN:** Reserved for a future non-deterministic-input mode — not a live computation today. The code sets this literal 0.0, explicitly flagged as reserved, not silently omitted. Not a content measurement — a self-test that the vector-space math the rest of the engine relies on actually holds its own axioms. Source: `docs/foundations/output_catalog.md` §5.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
