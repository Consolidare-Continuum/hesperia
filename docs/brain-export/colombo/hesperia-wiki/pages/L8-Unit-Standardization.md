# L8 — Unit Standardization

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_8.py::compute_L8 (41_SPEC)`  
**Value / default:** 30

## In plain words

takes every L1-L7 raw ratio/score and rescales it into fixed, documented unit families (PCT, U1000) so L9 and downstream consumers never have to know each upstream layer's native scale.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md), [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md), [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md), [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- **Does:** Hub: takes every L1-L7 raw ratio/score and rescales it into fixed, documented unit families (PCT, U1000) so L9 and downstream consumers never have to know each upstream layer's native scale.
- **Outputs:** `30` → [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md), [UNIT_TYPE_ENUM (L8)](../pages/UNIT-TYPE-ENUM-L8.md), [SCALE_POLICY_ENUM (L8)](../pages/SCALE-POLICY-ENUM-L8.md), [EPSILON_POLICY (L8)](../pages/EPSILON-POLICY-L8.md), [CLAMP_POLICY (L8)](../pages/CLAMP-POLICY-L8.md), [ROUNDING_POLICY (L8)](../pages/ROUNDING-POLICY-L8.md), [SI_TOTAL_TOKENS_COUNT (L8)](../pages/SI-TOTAL-TOKENS-COUNT-L8.md), [SI_COVERAGE_PCT (L8)](../pages/SI-COVERAGE-PCT-L8.md), [SI_COVERAGE_U1000 (L8)](../pages/SI-COVERAGE-U1000-L8.md), [SI_DOMINANCE_PCT (L8)](../pages/SI-DOMINANCE-PCT-L8.md), [SI_DOMINANCE_U1000 (L8)](../pages/SI-DOMINANCE-U1000-L8.md), [SI_ENTROPY_U1000 (L8)](../pages/SI-ENTROPY-U1000-L8.md), [SI_ENTROPY_PCT (L8)](../pages/SI-ENTROPY-PCT-L8.md), [SI_GEOMETRIC_STABILITY_U1000 (L8)](../pages/SI-GEOMETRIC-STABILITY-U1000-L8.md), [SI_GEOMETRIC_STABILITY_PCT (L8)](../pages/SI-GEOMETRIC-STABILITY-PCT-L8.md), [SI_AREA_LEAKAGE_PCT (L8)](../pages/SI-AREA-LEAKAGE-PCT-L8.md), [SI_AREA_LEAKAGE_U1000 (L8)](../pages/SI-AREA-LEAKAGE-U1000-L8.md), [SI_SHADOW_DEVIATION_U1000 (L8)](../pages/SI-SHADOW-DEVIATION-U1000-L8.md), [SI_SHADOW_DEVIATION_PCT (L8)](../pages/SI-SHADOW-DEVIATION-PCT-L8.md), [SI_EVIDENCE_SUPPORT_U1000 (L8)](../pages/SI-EVIDENCE-SUPPORT-U1000-L8.md), [SI_EVIDENCE_SUPPORT_PCT (L8)](../pages/SI-EVIDENCE-SUPPORT-PCT-L8.md), [SI_CONTRADICTION_PRESSURE_U1000 (L8)](../pages/SI-CONTRADICTION-PRESSURE-U1000-L8.md), [SI_CONTRADICTION_PRESSURE_PCT (L8)](../pages/SI-CONTRADICTION-PRESSURE-PCT-L8.md), [SI_TRIG_REALITY_FLAG (L8)](../pages/SI-TRIG-REALITY-FLAG-L8.md), [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md), [POLICY_MODE (L8)](../pages/POLICY-MODE-L8.md), [INTERPRETATION_CONSTRAINTS (L8)](../pages/INTERPRETATION-CONSTRAINTS-L8.md), [INTERPRETATION_SCOPE (L8)](../pages/INTERPRETATION-SCOPE-L8.md)
- **Exists for:** **HWIKI-CATALOG-L8:** Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04

## Yields (formula)

Hub: takes every L1-L7 raw ratio/score and rescales it into fixed, documented unit families (PCT, U1000) so L9 and downstream consumers never have to know each upstream layer's native scale.

## Produced from (inputs)

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)

## Needed by (consumers)

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [UNIT_TYPE_ENUM (L8)](../pages/UNIT-TYPE-ENUM-L8.md)
- [SCALE_POLICY_ENUM (L8)](../pages/SCALE-POLICY-ENUM-L8.md)
- [EPSILON_POLICY (L8)](../pages/EPSILON-POLICY-L8.md)
- [CLAMP_POLICY (L8)](../pages/CLAMP-POLICY-L8.md)
- [ROUNDING_POLICY (L8)](../pages/ROUNDING-POLICY-L8.md)
- [SI_TOTAL_TOKENS_COUNT (L8)](../pages/SI-TOTAL-TOKENS-COUNT-L8.md)
- [SI_COVERAGE_PCT (L8)](../pages/SI-COVERAGE-PCT-L8.md)
- [SI_COVERAGE_U1000 (L8)](../pages/SI-COVERAGE-U1000-L8.md)
- [SI_DOMINANCE_PCT (L8)](../pages/SI-DOMINANCE-PCT-L8.md)
- [SI_DOMINANCE_U1000 (L8)](../pages/SI-DOMINANCE-U1000-L8.md)
- [SI_ENTROPY_U1000 (L8)](../pages/SI-ENTROPY-U1000-L8.md)
- [SI_ENTROPY_PCT (L8)](../pages/SI-ENTROPY-PCT-L8.md)
- [SI_GEOMETRIC_STABILITY_U1000 (L8)](../pages/SI-GEOMETRIC-STABILITY-U1000-L8.md)
- [SI_GEOMETRIC_STABILITY_PCT (L8)](../pages/SI-GEOMETRIC-STABILITY-PCT-L8.md)
- [SI_AREA_LEAKAGE_PCT (L8)](../pages/SI-AREA-LEAKAGE-PCT-L8.md)
- [SI_AREA_LEAKAGE_U1000 (L8)](../pages/SI-AREA-LEAKAGE-U1000-L8.md)
- [SI_SHADOW_DEVIATION_U1000 (L8)](../pages/SI-SHADOW-DEVIATION-U1000-L8.md)
- [SI_SHADOW_DEVIATION_PCT (L8)](../pages/SI-SHADOW-DEVIATION-PCT-L8.md)
- [SI_EVIDENCE_SUPPORT_U1000 (L8)](../pages/SI-EVIDENCE-SUPPORT-U1000-L8.md)
- [SI_EVIDENCE_SUPPORT_PCT (L8)](../pages/SI-EVIDENCE-SUPPORT-PCT-L8.md)
- [SI_CONTRADICTION_PRESSURE_U1000 (L8)](../pages/SI-CONTRADICTION-PRESSURE-U1000-L8.md)
- [SI_CONTRADICTION_PRESSURE_PCT (L8)](../pages/SI-CONTRADICTION-PRESSURE-PCT-L8.md)
- [SI_TRIG_REALITY_FLAG (L8)](../pages/SI-TRIG-REALITY-FLAG-L8.md)
- [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md)
- [POLICY_MODE (L8)](../pages/POLICY-MODE-L8.md)
- [INTERPRETATION_CONSTRAINTS (L8)](../pages/INTERPRETATION-CONSTRAINTS-L8.md)
- [INTERPRETATION_SCOPE (L8)](../pages/INTERPRETATION-SCOPE-L8.md)

## See also

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L5 — Counter-Evidence & Trig Invariants](../pages/L5-Counter-Evidence-Trig-Invariants.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [UNIT_TYPE_ENUM (L8)](../pages/UNIT-TYPE-ENUM-L8.md)
- [SCALE_POLICY_ENUM (L8)](../pages/SCALE-POLICY-ENUM-L8.md)
- [EPSILON_POLICY (L8)](../pages/EPSILON-POLICY-L8.md)
- [CLAMP_POLICY (L8)](../pages/CLAMP-POLICY-L8.md)
- [ROUNDING_POLICY (L8)](../pages/ROUNDING-POLICY-L8.md)

## Origin

Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: takes every L1-L7 raw ratio/score and rescales it into fixed, documented unit families (PCT, U1000) so L9 and downstream consumers never have to know each upstream layer's native scale. author: Hesperia wiki (core/layers/layer_8.py::compute_L8 (41_SPEC)). extent: full. reasoning: **HWIKI-CATALOG-L8:** Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04. application: [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L8:** Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04. 5 policy/metadata constants (always identical text) + 22 SI_* metrics from `compute_L8` + 3 more (POLICY_MODE, INTERPRETATION_CONSTRAINTS, INTERPRETATION_SCOPE) always added by the `run()` wrapper regardless of whether a policy was supplied.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
