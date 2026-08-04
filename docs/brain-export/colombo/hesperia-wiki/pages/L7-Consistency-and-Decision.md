# L7 — Consistency and Decision

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_7.py::compute_L7 (40_SPEC)`  
**Value / default:** 25 base + up to 3 conditional

## In plain words

ten pass/fail consistency gates (g1-g10) plus alignment/confidence aggregation — the layer where L1-L6's separate measurements collapse into one trust tier and one decision code.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md), [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md), [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- **Does:** Hub: ten pass/fail consistency gates (g1-g10) plus alignment/confidence aggregation — the layer where L1-L6's separate measurements collapse into one trust tier and one decision code.
- **Outputs:** `25 base + up to 3 conditional` → [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md), [CONSIST_COVERAGE_MIN_GATE (L7, g1)](../pages/CONSIST-COVERAGE-MIN-GATE-L7-g1.md), [CONSIST_ATTRIBUTION_MASS_EQUALITY (L7, g2)](../pages/CONSIST-ATTRIBUTION-MASS-EQUALITY-L7-g2.md), [CONSIST_TRAVERSAL_NONEMPTY_WHEN_ATTRIBUTED (L7, g3)](../pages/CONSIST-TRAVERSAL-NONEMPTY-WHEN-ATTRIBUTED-L7-g3.md), [CONSIST_DOMINANT_FAMILY_IN_TRAVERSAL (L7, g4)](../pages/CONSIST-DOMINANT-FAMILY-IN-TRAVERSAL-L7-g4.md), [CONSIST_AREA_MAPPING (L7, g5)](../pages/CONSIST-AREA-MAPPING-L7-g5.md), [CONSIST_EVIDENCE_INTEGRITY_HARD (L7, g6)](../pages/CONSIST-EVIDENCE-INTEGRITY-HARD-L7-g6.md), [CONSIST_SHADOW_DELTA_ONLY_IF_SHADOW (L7, g7)](../pages/CONSIST-SHADOW-DELTA-ONLY-IF-SHADOW-L7-g7.md), [CONSIST_TRIG_REQUIRED_FOR_ANGLE_METRICS (L7, g8)](../pages/CONSIST-TRIG-REQUIRED-FOR-ANGLE-METRICS-L7-g8.md), [CONSIST_COUNTER_EVIDENCE_VALID (L7, g9)](../pages/CONSIST-COUNTER-EVIDENCE-VALID-L7-g9.md), [TRUST_TIER](../pages/TRUST-TIER.md), [MAX_ALLOWABLE_SHADOW_DEVIATION](../pages/MAX-ALLOWABLE-SHADOW-DEVIATION.md), [SHADOW_WITHIN_LIMITS](../pages/SHADOW-WITHIN-LIMITS.md), [MAX_ALLOWABLE_CONTRADICTION](../pages/MAX-ALLOWABLE-CONTRADICTION.md), [CONTRADICTION_WITHIN_LIMITS](../pages/CONTRADICTION-WITHIN-LIMITS.md), [MAX_AREA_LEAKAGE](../pages/MAX-AREA-LEAKAGE.md), [AREA_LEAKAGE_WITHIN_LIMITS](../pages/AREA-LEAKAGE-WITHIN-LIMITS.md), [MAX_CHAOS_LEVEL](../pages/MAX-CHAOS-LEVEL.md), [STRUCTURE_EVIDENCE_ALIGNMENT](../pages/STRUCTURE-EVIDENCE-ALIGNMENT.md), [SHADOW_EVIDENCE_ALIGNMENT_DELTA](../pages/SHADOW-EVIDENCE-ALIGNMENT-DELTA.md), [SHADOW_JUSTIFICATION_SCORE](../pages/SHADOW-JUSTIFICATION-SCORE.md), [CONTRADICTION_ADJUSTED_SUPPORT](../pages/CONTRADICTION-ADJUSTED-SUPPORT.md), [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md), [OUTPUT_TRUST_TAG](../pages/OUTPUT-TRUST-TAG.md), [CONSIST_PROFILE_CONFORMANCE (L7)](../pages/CONSIST-PROFILE-CONFORMANCE-L7.md), [PROFILE_CHECKSUM (L7)](../pages/PROFILE-CHECKSUM-L7.md), [STABILITY_ANOMALY_SCORE (L7)](../pages/STABILITY-ANOMALY-SCORE-L7.md), [SPECTRAL_GAP (L6)](../pages/SPECTRAL-GAP-L6.md), [POTENTIAL_GRADIENT (L6)](../pages/POTENTIAL-GRADIENT-L6.md)
- **Exists for:** **HWIKI-CATALOG-L7:** Source: `docs/foundations/output_catalog.md` §7, re-verified against `compute_L7` 2026-08-04

## Yields (formula)

Hub: ten pass/fail consistency gates (g1-g10) plus alignment/confidence aggregation — the layer where L1-L6's separate measurements collapse into one trust tier and one decision code.

## Produced from (inputs)

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)

## Needed by (consumers)

- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- [CONSIST_COVERAGE_MIN_GATE (L7, g1)](../pages/CONSIST-COVERAGE-MIN-GATE-L7-g1.md)
- [CONSIST_ATTRIBUTION_MASS_EQUALITY (L7, g2)](../pages/CONSIST-ATTRIBUTION-MASS-EQUALITY-L7-g2.md)
- [CONSIST_TRAVERSAL_NONEMPTY_WHEN_ATTRIBUTED (L7, g3)](../pages/CONSIST-TRAVERSAL-NONEMPTY-WHEN-ATTRIBUTED-L7-g3.md)
- [CONSIST_DOMINANT_FAMILY_IN_TRAVERSAL (L7, g4)](../pages/CONSIST-DOMINANT-FAMILY-IN-TRAVERSAL-L7-g4.md)
- [CONSIST_AREA_MAPPING (L7, g5)](../pages/CONSIST-AREA-MAPPING-L7-g5.md)
- [CONSIST_EVIDENCE_INTEGRITY_HARD (L7, g6)](../pages/CONSIST-EVIDENCE-INTEGRITY-HARD-L7-g6.md)
- [CONSIST_SHADOW_DELTA_ONLY_IF_SHADOW (L7, g7)](../pages/CONSIST-SHADOW-DELTA-ONLY-IF-SHADOW-L7-g7.md)
- [CONSIST_TRIG_REQUIRED_FOR_ANGLE_METRICS (L7, g8)](../pages/CONSIST-TRIG-REQUIRED-FOR-ANGLE-METRICS-L7-g8.md)
- [CONSIST_COUNTER_EVIDENCE_VALID (L7, g9)](../pages/CONSIST-COUNTER-EVIDENCE-VALID-L7-g9.md)
- [TRUST_TIER](../pages/TRUST-TIER.md)
- [MAX_ALLOWABLE_SHADOW_DEVIATION](../pages/MAX-ALLOWABLE-SHADOW-DEVIATION.md)
- [SHADOW_WITHIN_LIMITS](../pages/SHADOW-WITHIN-LIMITS.md)
- [MAX_ALLOWABLE_CONTRADICTION](../pages/MAX-ALLOWABLE-CONTRADICTION.md)
- [CONTRADICTION_WITHIN_LIMITS](../pages/CONTRADICTION-WITHIN-LIMITS.md)
- [MAX_AREA_LEAKAGE](../pages/MAX-AREA-LEAKAGE.md)
- [AREA_LEAKAGE_WITHIN_LIMITS](../pages/AREA-LEAKAGE-WITHIN-LIMITS.md)
- [MAX_CHAOS_LEVEL](../pages/MAX-CHAOS-LEVEL.md)
- [STRUCTURE_EVIDENCE_ALIGNMENT](../pages/STRUCTURE-EVIDENCE-ALIGNMENT.md)
- [SHADOW_EVIDENCE_ALIGNMENT_DELTA](../pages/SHADOW-EVIDENCE-ALIGNMENT-DELTA.md)
- [SHADOW_JUSTIFICATION_SCORE](../pages/SHADOW-JUSTIFICATION-SCORE.md)
- [CONTRADICTION_ADJUSTED_SUPPORT](../pages/CONTRADICTION-ADJUSTED-SUPPORT.md)
- [DECISION_STATUS_CODE](../pages/DECISION-STATUS-CODE.md)
- [OUTPUT_TRUST_TAG](../pages/OUTPUT-TRUST-TAG.md)
- [CONSIST_PROFILE_CONFORMANCE (L7)](../pages/CONSIST-PROFILE-CONFORMANCE-L7.md)
- [PROFILE_CHECKSUM (L7)](../pages/PROFILE-CHECKSUM-L7.md)
- [STABILITY_ANOMALY_SCORE (L7)](../pages/STABILITY-ANOMALY-SCORE-L7.md)
- [SPECTRAL_GAP (L6)](../pages/SPECTRAL-GAP-L6.md)
- [POTENTIAL_GRADIENT (L6)](../pages/POTENTIAL-GRADIENT-L6.md)

## See also

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- [CONSIST_COVERAGE_MIN_GATE (L7, g1)](../pages/CONSIST-COVERAGE-MIN-GATE-L7-g1.md)
- [CONSIST_ATTRIBUTION_MASS_EQUALITY (L7, g2)](../pages/CONSIST-ATTRIBUTION-MASS-EQUALITY-L7-g2.md)
- [CONSIST_TRAVERSAL_NONEMPTY_WHEN_ATTRIBUTED (L7, g3)](../pages/CONSIST-TRAVERSAL-NONEMPTY-WHEN-ATTRIBUTED-L7-g3.md)
- [CONSIST_DOMINANT_FAMILY_IN_TRAVERSAL (L7, g4)](../pages/CONSIST-DOMINANT-FAMILY-IN-TRAVERSAL-L7-g4.md)
- [CONSIST_AREA_MAPPING (L7, g5)](../pages/CONSIST-AREA-MAPPING-L7-g5.md)
- [CONSIST_EVIDENCE_INTEGRITY_HARD (L7, g6)](../pages/CONSIST-EVIDENCE-INTEGRITY-HARD-L7-g6.md)

## Origin

Hesperia-native `40_SPEC` L7 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: ten pass/fail consistency gates (g1-g10) plus alignment/confidence aggregation — the layer where L1-L6's separate measurements collapse into one trust tier and one decision code. author: Hesperia wiki (core/layers/layer_7.py::compute_L7 (40_SPEC)). extent: full. reasoning: **HWIKI-CATALOG-L7:** Source: `docs/foundations/output_catalog.md` §7, re-verified against `compute_L7` 2026-08-04. application: [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L7:** Source: `docs/foundations/output_catalog.md` §7, re-verified against `compute_L7` 2026-08-04. `docs/specs/history/40_SPEC` recovery confirmed `OUTPUT_TRUST_TAG` is spec item 25, correcting an earlier miscounted '24 base' claim.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
