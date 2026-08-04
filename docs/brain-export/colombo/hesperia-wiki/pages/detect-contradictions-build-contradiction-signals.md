# detect_contradictions / build_contradiction_signals

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Function  
**Responsible (module):** `hesperia/extensions/triz/contradiction_engine.py`  
**Value / default:** —

## In plain words

Core contradiction detection + ContradictionSignal construction / pattern classify.

## Definition

- **Receives:** [TRIZ contradiction core hub](../pages/TRIZ-contradiction-core-hub.md), *models.ContradictionSignal*
- **Does:** Core contradiction detection + ContradictionSignal construction / pattern classify.
- **Outputs:** `—` → *triz_classifier.classify_contradiction*, *family_contradiction.py*, [classify_contradiction(s) principle table](../pages/classify-contradiction-s-principle-table.md)
- **Exists for:** **HWIKI-TRIZ-02 / TRIZ-03 pin:** engine core — inventory role: core contradiction

## Yields (formula)

Core contradiction detection + ContradictionSignal construction / pattern classify.

## Produced from (inputs)

- [TRIZ contradiction core hub](../pages/TRIZ-contradiction-core-hub.md)
- *models.ContradictionSignal*

## Needed by (consumers)

- *triz_classifier.classify_contradiction*
- *family_contradiction.py*
- [classify_contradiction(s) principle table](../pages/classify-contradiction-s-principle-table.md)

## See also

- [TRIZ contradiction core hub](../pages/TRIZ-contradiction-core-hub.md)
- [classify_contradiction(s) principle table](../pages/classify-contradiction-s-principle-table.md)
- [run_triz_layer / run_triz_analysis_complete](../pages/run-triz-layer-run-triz-analysis-complete.md)
- [contradiction_contract (canonical fields)](../pages/contradiction-contract-canonical-fields.md)

## Origin

extensions/triz/contradiction_engine.py — Theory Explainer: plain_lang: Core contradiction detection + ContradictionSignal construction / pattern classify. author: Hesperia wiki (hesperia/extensions/triz/contradiction_engine.py). extent: full. reasoning: **HWIKI-TRIZ-02 / TRIZ-03 pin:** engine core — inventory role: core contradiction. application: *triz_classifier.classify_contradiction*, *family_contradiction.py*.

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-TRIZ-02 / TRIZ-03 pin:** engine core — inventory role: core contradiction.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
