# CONSIST_AREA_MAPPING (L7, g5)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_7.py::compute_L7 -> out[...]`  
**Value / default:** bool

## In plain words

Sanity check that the dominant area was derived correctly from the dominant family, not independently computed and possibly inconsistent.

## Definition

- **Receives:** [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- **Does:** L1 DOMINANT_AREA_ID == [DOMINANT_FAMILY_ID](../pages/DOMINANT-FAMILY-ID.md) // FAMILIES_PER_AREA
- **Outputs:** `bool` → *no named wiki consumer yet*
- **Exists for:** L7 consistency/decision field — collapses L1–L6 into trust tier and decision code

## Yields (formula)

L1 DOMINANT_AREA_ID == [DOMINANT_FAMILY_ID](../pages/DOMINANT-FAMILY-ID.md) // FAMILIES_PER_AREA

## Produced from (inputs)

- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)

## See also

- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [SPECTRAL_GAP (L6)](../pages/SPECTRAL-GAP-L6.md)
- [POTENTIAL_GRADIENT (L6)](../pages/POTENTIAL-GRADIENT-L6.md)
- [CONSIST_COVERAGE_MIN_GATE (L7, g1)](../pages/CONSIST-COVERAGE-MIN-GATE-L7-g1.md)
- [CONSIST_ATTRIBUTION_MASS_EQUALITY (L7, g2)](../pages/CONSIST-ATTRIBUTION-MASS-EQUALITY-L7-g2.md)
- [CONSIST_TRAVERSAL_NONEMPTY_WHEN_ATTRIBUTED (L7, g3)](../pages/CONSIST-TRAVERSAL-NONEMPTY-WHEN-ATTRIBUTED-L7-g3.md)
- [CONSIST_DOMINANT_FAMILY_IN_TRAVERSAL (L7, g4)](../pages/CONSIST-DOMINANT-FAMILY-IN-TRAVERSAL-L7-g4.md)
- [CONSIST_EVIDENCE_INTEGRITY_HARD (L7, g6)](../pages/CONSIST-EVIDENCE-INTEGRITY-HARD-L7-g6.md)
- [CONSIST_SHADOW_DELTA_ONLY_IF_SHADOW (L7, g7)](../pages/CONSIST-SHADOW-DELTA-ONLY-IF-SHADOW-L7-g7.md)
- [CONSIST_TRIG_REQUIRED_FOR_ANGLE_METRICS (L7, g8)](../pages/CONSIST-TRIG-REQUIRED-FOR-ANGLE-METRICS-L7-g8.md)
- [CONSIST_COUNTER_EVIDENCE_VALID (L7, g9)](../pages/CONSIST-COUNTER-EVIDENCE-VALID-L7-g9.md)
- [TRUST_TIER](../pages/TRUST-TIER.md)

## Origin

Hesperia-native `40_SPEC` L7 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Sanity check that the dominant area was derived correctly from the dominant family, not independently computed and possibly inconsistent.. author: Hesperia L7 (40_SPEC / output_catalog §7). extent: full. reasoning: L7 consistency/decision field — collapses L1–L6 into trust tier and decision code. application: [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md), L8–L9.

## Notes

**HWIKI-CATALOG-L7 / HWIKI-PLAIN:** Sanity check that the dominant area was derived correctly from the dominant family, not independently computed and possibly inconsistent. Source: `docs/foundations/output_catalog.md` §7, re-verified against `compute_L7` 2026-08-04.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
