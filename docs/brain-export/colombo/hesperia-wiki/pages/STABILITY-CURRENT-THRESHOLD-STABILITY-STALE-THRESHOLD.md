# STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `sphere/fpf_bridge/constants.py + evidence_mapper.py`  
**Value / default:** 0.7 / 0.3

## Yields (formula)

Stability→freshness map: ≥CURRENT_THRESHOLD → CURRENT; ≥STALE else EXPIRED below STALE.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- *sphere/fpf_bridge/evidence_mapper.py*

## Origin

parameter_catalog.md §5

## Notes

**HWIKI-CAT-02:** FGR freshness numeric pair from CAT-01 delta.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md)
