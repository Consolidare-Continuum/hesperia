# L1 — Structural Activation Census

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 (34_SPEC)`  
**Value / default:** 27 base + up to 6 profile

## In plain words

token-attribution census — the first of nine pipeline layers; everything downstream is built on this layer's family/area hit counts.

## Definition

- **Receives:** *ActiveGraph (KME concept graph)*
- **Does:** Hub: token-attribution census — the first of nine pipeline layers (L1-L9), everything downstream is built on this layer's family/area hit counts.
- **Outputs:** `27 base + up to 6 profile` → [STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md), [PROFILE_MODE_ACTIVE](../pages/PROFILE-MODE-ACTIVE.md), [TOTAL_TOKENS](../pages/TOTAL-TOKENS.md), [ATTRIBUTED_TOKENS](../pages/ATTRIBUTED-TOKENS.md), [COVERAGE_RATIO](../pages/COVERAGE-RATIO.md), [UNIQUE_FAMILIES_HIT](../pages/UNIQUE-FAMILIES-HIT.md), [FAMILY_ACTIVATION_DENSITY](../pages/FAMILY-ACTIVATION-DENSITY.md), [FAMILY_HIT_VECTOR_L1](../pages/FAMILY-HIT-VECTOR-L1.md), [FAMILY_HIT_VECTOR_L2](../pages/FAMILY-HIT-VECTOR-L2.md), [MAX_FAMILY_HITS](../pages/MAX-FAMILY-HITS.md), [DOMINANT_FAMILY_ID](../pages/DOMINANT-FAMILY-ID.md), [DOMINANT_AREA_ID](../pages/DOMINANT-AREA-ID.md), [DOMINANCE_RATIO](../pages/DOMINANCE-RATIO.md), [MEAN_ALTITUDE_GLOBAL](../pages/MEAN-ALTITUDE-GLOBAL.md), [MEAN_ALTITUDE_DOMINANT](../pages/MEAN-ALTITUDE-DOMINANT.md), [ALTITUDE_VARIANCE_GLOBAL](../pages/ALTITUDE-VARIANCE-GLOBAL.md), [FAMILY_ENTROPY](../pages/FAMILY-ENTROPY.md), [NORMALIZED_FAMILY_ENTROPY](../pages/NORMALIZED-FAMILY-ENTROPY.md), [UNIQUE_AREAS_HIT](../pages/UNIQUE-AREAS-HIT.md), [AREA_SPREAD](../pages/AREA-SPREAD.md), [AREA_DOMINANCE_RATIO](../pages/AREA-DOMINANCE-RATIO.md), [SECONDARY_FAMILY_RATIO](../pages/SECONDARY-FAMILY-RATIO.md), [SIGNAL_TO_NOISE_RATIO](../pages/SIGNAL-TO-NOISE-RATIO.md), [SPARSITY_INDEX](../pages/SPARSITY-INDEX.md), [TOKEN_REDUNDANCY_RATIO](../pages/TOKEN-REDUNDANCY-RATIO.md), [ALTITUDE_WEIGHTED_MASS](../pages/ALTITUDE-WEIGHTED-MASS.md), [PROFILE_ID](../pages/PROFILE-ID.md), [PROFILE_VERSION](../pages/PROFILE-VERSION.md), [PROFILE_CHECKSUM](../pages/PROFILE-CHECKSUM.md), [FAMILY_PROFILE_DEVIATION](../pages/FAMILY-PROFILE-DEVIATION.md), [AREA_PROFILE_DEVIATION](../pages/AREA-PROFILE-DEVIATION.md), [PROFILE_CONFORMANCE_SCORE](../pages/PROFILE-CONFORMANCE-SCORE.md), [FORBIDDEN_MASS_PENALTY](../pages/FORBIDDEN-MASS-PENALTY.md), [ALTITUDE_DEVIATION](../pages/ALTITUDE-DEVIATION.md), [BUDGET_VIOLATION_SCORE](../pages/BUDGET-VIOLATION-SCORE.md), [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md), [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md), [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Exists for:** foundation layer for L2–L9 structural and trust pipeline

## Yields (formula)

Hub: token-attribution census — the first of nine pipeline layers (L1-L9), everything downstream is built on this layer's family/area hit counts.

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [PROFILE_MODE_ACTIVE](../pages/PROFILE-MODE-ACTIVE.md)
- [TOTAL_TOKENS](../pages/TOTAL-TOKENS.md)
- [ATTRIBUTED_TOKENS](../pages/ATTRIBUTED-TOKENS.md)
- [COVERAGE_RATIO](../pages/COVERAGE-RATIO.md)
- [UNIQUE_FAMILIES_HIT](../pages/UNIQUE-FAMILIES-HIT.md)
- [FAMILY_ACTIVATION_DENSITY](../pages/FAMILY-ACTIVATION-DENSITY.md)
- [FAMILY_HIT_VECTOR_L1](../pages/FAMILY-HIT-VECTOR-L1.md)
- [FAMILY_HIT_VECTOR_L2](../pages/FAMILY-HIT-VECTOR-L2.md)
- [MAX_FAMILY_HITS](../pages/MAX-FAMILY-HITS.md)
- [DOMINANT_FAMILY_ID](../pages/DOMINANT-FAMILY-ID.md)
- [DOMINANT_AREA_ID](../pages/DOMINANT-AREA-ID.md)
- [DOMINANCE_RATIO](../pages/DOMINANCE-RATIO.md)
- [MEAN_ALTITUDE_GLOBAL](../pages/MEAN-ALTITUDE-GLOBAL.md)
- [MEAN_ALTITUDE_DOMINANT](../pages/MEAN-ALTITUDE-DOMINANT.md)
- [ALTITUDE_VARIANCE_GLOBAL](../pages/ALTITUDE-VARIANCE-GLOBAL.md)
- [FAMILY_ENTROPY](../pages/FAMILY-ENTROPY.md)
- [NORMALIZED_FAMILY_ENTROPY](../pages/NORMALIZED-FAMILY-ENTROPY.md)
- [UNIQUE_AREAS_HIT](../pages/UNIQUE-AREAS-HIT.md)
- [AREA_SPREAD](../pages/AREA-SPREAD.md)
- [AREA_DOMINANCE_RATIO](../pages/AREA-DOMINANCE-RATIO.md)
- [SECONDARY_FAMILY_RATIO](../pages/SECONDARY-FAMILY-RATIO.md)
- [SIGNAL_TO_NOISE_RATIO](../pages/SIGNAL-TO-NOISE-RATIO.md)
- [SPARSITY_INDEX](../pages/SPARSITY-INDEX.md)
- [TOKEN_REDUNDANCY_RATIO](../pages/TOKEN-REDUNDANCY-RATIO.md)
- [ALTITUDE_WEIGHTED_MASS](../pages/ALTITUDE-WEIGHTED-MASS.md)
- [PROFILE_ID](../pages/PROFILE-ID.md)
- [PROFILE_VERSION](../pages/PROFILE-VERSION.md)
- [PROFILE_CHECKSUM](../pages/PROFILE-CHECKSUM.md)
- [FAMILY_PROFILE_DEVIATION](../pages/FAMILY-PROFILE-DEVIATION.md)
- [AREA_PROFILE_DEVIATION](../pages/AREA-PROFILE-DEVIATION.md)
- [PROFILE_CONFORMANCE_SCORE](../pages/PROFILE-CONFORMANCE-SCORE.md)
- [FORBIDDEN_MASS_PENALTY](../pages/FORBIDDEN-MASS-PENALTY.md)
- [ALTITUDE_DEVIATION](../pages/ALTITUDE-DEVIATION.md)
- [BUDGET_VIOLATION_SCORE](../pages/BUDGET-VIOLATION-SCORE.md)
- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## See also

- [STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [PROFILE_MODE_ACTIVE](../pages/PROFILE-MODE-ACTIVE.md)
- [TOTAL_TOKENS](../pages/TOTAL-TOKENS.md)
- [ATTRIBUTED_TOKENS](../pages/ATTRIBUTED-TOKENS.md)
- [COVERAGE_RATIO](../pages/COVERAGE-RATIO.md)
- [UNIQUE_FAMILIES_HIT](../pages/UNIQUE-FAMILIES-HIT.md)
- [FAMILY_ACTIVATION_DENSITY](../pages/FAMILY-ACTIVATION-DENSITY.md)
- [FAMILY_HIT_VECTOR_L1](../pages/FAMILY-HIT-VECTOR-L1.md)
- [FAMILY_HIT_VECTOR_L2](../pages/FAMILY-HIT-VECTOR-L2.md)
- [MAX_FAMILY_HITS](../pages/MAX-FAMILY-HITS.md)
- [DOMINANT_FAMILY_ID](../pages/DOMINANT-FAMILY-ID.md)

## Origin

Hesperia-native `34_SPEC` L1 instrumentation — docstring claims 25 variables, actual base return dict has 27 keys (recovered-spec resolution: item 18 bundles two names into one spec entry; [PROFILE_MODE_ACTIVE](../pages/PROFILE-MODE-ACTIVE.md) is a code-only flag outside the spec's numbered list) — Theory Explainer: plain_lang: token-attribution census — the first of nine pipeline layers; everything downstream is built on this layer's family/area hit counts. author: Hesperia L1 hub (34_SPEC). extent: full. reasoning: foundation layer for L2–L9 structural and trust pipeline. application: [STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md).

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** `docs/foundations/output_catalog.md` §1 already did the source-verification — this hub + per-variable pages transcribe that research, re-verified against `compute_L1`.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
