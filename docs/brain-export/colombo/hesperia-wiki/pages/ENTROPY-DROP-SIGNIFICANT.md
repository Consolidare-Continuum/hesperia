# ENTROPY_DROP_SIGNIFICANT

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `sphere/fpf_bridge/constants.py + sphere/interpretation/state_classifier.py`  
**Value / default:** 0.15

## In plain words

Cutoff for when an entropy drop upgrades FGR / trust tier vs mild fluctuation.

## Definition

- **Receives:** [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- **Does:** Cutoff for when an entropy drop upgrades FGR / trust tier vs mild fluctuation.
- **Outputs:** `0.15` → *sphere/fpf_bridge/evidence_mapper.py*, *state_classifier.py*
- **Exists for:** **HWIKI-CAT-02:** FGR freshness numeric — entropy-drop significance

## Yields (formula)

Cutoff for when an entropy drop upgrades FGR / trust tier vs mild fluctuation.

## Produced from (inputs)

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)

## Needed by (consumers)

- *sphere/fpf_bridge/evidence_mapper.py*
- *state_classifier.py*

## See also

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
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

## Origin

parameter_catalog.md §5 / synergies — Theory Explainer: plain_lang: Cutoff for when an entropy drop upgrades FGR / trust tier vs mild fluctuation. author: Hesperia wiki (sphere/fpf_bridge/constants.py + sphere/interpretation/state_classifier.py). extent: full. reasoning: **HWIKI-CAT-02:** FGR freshness numeric — entropy-drop significance. application: *sphere/fpf_bridge/evidence_mapper.py*, *state_classifier.py*.

## Notes

**HWIKI-WIRE:** attached to category anchor [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md). **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CAT-02:** FGR freshness numeric — entropy-drop significance.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
