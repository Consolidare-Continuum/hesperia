# STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `sphere/fpf_bridge/constants.py + evidence_mapper.py`  
**Value / default:** 0.7 / 0.3

## In plain words

Stability→freshness map: ≥CURRENT_THRESHOLD → CURRENT; ≥STALE else EXPIRED below STALE.

## Definition

- **Receives:** [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- **Does:** Stability→freshness map: ≥CURRENT_THRESHOLD → CURRENT; ≥STALE else EXPIRED below STALE.
- **Outputs:** `0.7 / 0.3` → *sphere/fpf_bridge/evidence_mapper.py*
- **Exists for:** **HWIKI-CAT-02:** FGR freshness numeric pair from CAT-01 delta

## Yields (formula)

Stability→freshness map: ≥CURRENT_THRESHOLD → CURRENT; ≥STALE else EXPIRED below STALE.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- *sphere/fpf_bridge/evidence_mapper.py*

## See also

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)

## Origin

parameter_catalog.md §5 — Theory Explainer: plain_lang: Stability→freshness map: ≥CURRENT_THRESHOLD → CURRENT; ≥STALE else EXPIRED below STALE. author: Hesperia wiki (sphere/fpf_bridge/constants.py + evidence_mapper.py). extent: full. reasoning: **HWIKI-CAT-02:** FGR freshness numeric pair from CAT-01 delta. application: *sphere/fpf_bridge/evidence_mapper.py*.

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CAT-02:** FGR freshness numeric pair from CAT-01 delta.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
