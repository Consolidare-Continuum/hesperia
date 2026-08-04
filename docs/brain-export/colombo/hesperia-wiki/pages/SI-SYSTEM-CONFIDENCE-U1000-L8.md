# SI_SYSTEM_CONFIDENCE_U1000 (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Scaled indicator  
**Responsible (module):** `core/layers/layer_8.py:50`  
**Value / default:** 0–1000

## Yields (formula)

SI_SYSTEM_CONFIDENCE_U1000 = _ratio_to_u1000(l7[SYSTEM_CONFIDENCE_SCORE]) — publishes L7 confidence (which already folded GLOBAL_STABILITY).

## Produced from (inputs)

- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)

## Origin

41_SPEC Layer-8

## Notes

**HWIKI-L8-01:** Indirect consumer chain L6→L7→L8.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md)
