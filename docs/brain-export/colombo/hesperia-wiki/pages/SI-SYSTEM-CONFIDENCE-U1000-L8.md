# SI_SYSTEM_CONFIDENCE_U1000 (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Scaled indicator  
**Responsible (module):** `core/layers/layer_8.py:50`  
**Value / default:** 0–1000

## In plain words

publish L7's system confidence on the 0–1000 scale — the confidence number L9 bands and brand words read.

## Definition

- **Receives:** [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- **Does:** SI_SYSTEM_CONFIDENCE_U1000 = _ratio_to_u1000(l7[SYSTEM_CONFIDENCE_SCORE]) — publishes L7 confidence (which already folded GLOBAL_STABILITY).
- **Outputs:** `0–1000` → [BAND_0_CRITICAL (L9)](../pages/BAND-0-CRITICAL-L9.md), [BAND_1_POOR (L9)](../pages/BAND-1-POOR-L9.md), [BAND_2_FAIR (L9)](../pages/BAND-2-FAIR-L9.md), [BAND_3_GOOD (L9)](../pages/BAND-3-GOOD-L9.md), [BAND_4_VERY_GOOD (L9)](../pages/BAND-4-VERY-GOOD-L9.md), [BAND_5_EXCELLENT (L9)](../pages/BAND-5-EXCELLENT-L9.md)
- **Exists for:** L8 rescale of SYSTEM_CONFIDENCE_SCORE (L6→L7→L8 chain)

## Yields (formula)

SI_SYSTEM_CONFIDENCE_U1000 = _ratio_to_u1000(l7[SYSTEM_CONFIDENCE_SCORE]) — publishes L7 confidence (which already folded GLOBAL_STABILITY).

## Produced from (inputs)

- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)

## Needed by (consumers)

- [BAND_0_CRITICAL (L9)](../pages/BAND-0-CRITICAL-L9.md)
- [BAND_1_POOR (L9)](../pages/BAND-1-POOR-L9.md)
- [BAND_2_FAIR (L9)](../pages/BAND-2-FAIR-L9.md)
- [BAND_3_GOOD (L9)](../pages/BAND-3-GOOD-L9.md)
- [BAND_4_VERY_GOOD (L9)](../pages/BAND-4-VERY-GOOD-L9.md)
- [BAND_5_EXCELLENT (L9)](../pages/BAND-5-EXCELLENT-L9.md)

## See also

- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [BAND_0_CRITICAL (L9)](../pages/BAND-0-CRITICAL-L9.md)
- [BAND_1_POOR (L9)](../pages/BAND-1-POOR-L9.md)
- [BAND_2_FAIR (L9)](../pages/BAND-2-FAIR-L9.md)
- [BAND_3_GOOD (L9)](../pages/BAND-3-GOOD-L9.md)
- [BAND_4_VERY_GOOD (L9)](../pages/BAND-4-VERY-GOOD-L9.md)
- [BAND_5_EXCELLENT (L9)](../pages/BAND-5-EXCELLENT-L9.md)

## Origin

41_SPEC Layer-8 — Theory Explainer: plain_lang: publish L7's system confidence on the 0–1000 scale — the confidence number L9 bands and brand words read. author: Hesperia wiki (core/layers/layer_8.py:50). extent: full. reasoning: L8 rescale of SYSTEM_CONFIDENCE_SCORE (L6→L7→L8 chain). application: [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L8-01:** Indirect consumer chain L6→L7→L8.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
