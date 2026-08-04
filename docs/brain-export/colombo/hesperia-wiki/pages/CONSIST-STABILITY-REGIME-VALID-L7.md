# CONSIST_STABILITY_REGIME_VALID (L7)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Layer gate  
**Responsible (module):** `core/layers/layer_7.py (g10)`  
**Value / default:** boolean gate

## Yields (formula)

CONSIST_STABILITY_REGIME_VALID (g10) — consistency gate that the L6 Lyapunov/stability regime is within MAX_CHAOS_LEVEL / MAX_LYAPUNOV bounds.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- *DECISION_STATUS_CODE*

## Origin

40_SPEC Layer-7

## Notes

**HWIKI-L7-01:** Gate sibling of SYSTEM_CONFIDENCE — Lyapunov/stability regime validity.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md)
