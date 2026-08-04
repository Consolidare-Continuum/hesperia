# PROFILE_ID

**Status:** 🟡 PARTIAL — present in a narrow slice/tool, not the full contract  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Parameter (flag)  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 -> result["PROFILE_ID"] (profile-conditional)`  
**Value / default:** str

## In plain words

Name/version string identifying the active profile.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- **Does:** See notes — profile-conformance formula, only computed when a StructureProfile is supplied.
- **Outputs:** `str` → *no named wiki consumer yet*
- **Exists for:** only present when a StructureProfile is supplied to compute_L1

## Yields (formula)

See notes — profile-conformance formula, only computed when a StructureProfile is supplied.

## Produced from (inputs)

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)

## See also

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
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

## Origin

Hesperia-native `34_SPEC N1` profile-conformance extension — no Java prototype ancestor — Theory Explainer: plain_lang: Name/version string identifying the active profile.. author: Hesperia L1 profile extension (34_SPEC N1). extent: partial. reasoning: only present when a StructureProfile is supplied to compute_L1. application: [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), L7 conformance gates.

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** Name/version string identifying the active profile. PARTIAL because these keys only appear in `compute_L1`'s return dict when a `profile` argument is supplied — absent on every unprofiled run. Source: `docs/foundations/output_catalog.md` §1.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
