# FAMILY_HIT_VECTOR_L2

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 -> result["FAMILY_HIT_VECTOR_L2"]`  
**Value / default:** float

## In plain words

L2 norm of the family hit vector — how concentrated the hit distribution is (higher relative to L1 norm = fewer families carrying more weight each).

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- **Does:** sqrt(sum(h*h for h in hits))
- **Outputs:** `float` → *no named wiki consumer yet*
- **Exists for:** L1 census field — first pipeline layer every later layer reads

## Yields (formula)

sqrt(sum(h*h for h in hits))

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
- [MAX_FAMILY_HITS](../pages/MAX-FAMILY-HITS.md)
- [DOMINANT_FAMILY_ID](../pages/DOMINANT-FAMILY-ID.md)
- [DOMINANT_AREA_ID](../pages/DOMINANT-AREA-ID.md)
- [DOMINANCE_RATIO](../pages/DOMINANCE-RATIO.md)

## Origin

Hesperia-native `34_SPEC` L1 instrumentation — no Java prototype ancestor for the L1-L9 layer pipeline as a whole — Theory Explainer: plain_lang: L2 norm of the family hit vector — how concentrated the hit distribution is (higher relative to L1 norm = fewer families carrying more weight each).. author: Hesperia L1 (34_SPEC / output_catalog §1). extent: full. reasoning: L1 census field — first pipeline layer every later layer reads. application: [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), L2–L9.

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** L2 norm of the family hit vector — how concentrated the hit distribution is (higher relative to L1 norm = fewer families carrying more weight each). Source: `docs/foundations/output_catalog.md` §1, re-verified against `compute_L1` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
