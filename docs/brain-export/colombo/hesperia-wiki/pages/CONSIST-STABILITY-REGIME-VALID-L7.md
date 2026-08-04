# CONSIST_STABILITY_REGIME_VALID (L7)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Layer gate  
**Responsible (module):** `core/layers/layer_7.py (g10)`  
**Value / default:** boolean gate

## In plain words

CONSIST_STABILITY_REGIME_VALID (g10) — consistency gate that the L6 Lyapunov/stability regime is within [MAX_CHAOS_LEVEL](../pages/MAX-CHAOS-LEVEL.md) / MAX_LYAPUNOV bounds.

## Definition

- **Receives:** [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- **Does:** CONSIST_STABILITY_REGIME_VALID (g10) — consistency gate that the L6 Lyapunov/stability regime is within [MAX_CHAOS_LEVEL](../pages/MAX-CHAOS-LEVEL.md) / MAX_LYAPUNOV bounds.
- **Outputs:** `boolean gate` → [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md), [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md)
- **Exists for:** **HWIKI-L7-01:** Gate sibling of SYSTEM_CONFIDENCE — Lyapunov/stability regime validity

## Yields (formula)

CONSIST_STABILITY_REGIME_VALID (g10) — consistency gate that the L6 Lyapunov/stability regime is within [MAX_CHAOS_LEVEL](../pages/MAX-CHAOS-LEVEL.md) / MAX_LYAPUNOV bounds.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md)

## See also

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)

## Origin

40_SPEC Layer-7 — Theory Explainer: plain_lang: CONSIST_STABILITY_REGIME_VALID (g10) — consistency gate that the L6 Lyapunov/stability regime is within [MAX_CHAOS_LEVEL](../pages/MAX-CHAOS-LEVEL.md) / MAX_LYAPUNOV bounds. author: Hesperia wiki (core/layers/layer_7.py (g10)). extent: full. reasoning: **HWIKI-L7-01:** Gate sibling of SYSTEM_CONFIDENCE — Lyapunov/stability regime validity. application: [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md), [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L7-01:** Gate sibling of SYSTEM_CONFIDENCE — Lyapunov/stability regime validity.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
