# ALTITUDE_VARIANCE_GLOBAL

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 -> result["ALTITUDE_VARIANCE_GLOBAL"]`  
**Value / default:** float

## In plain words

How much altitude varies across the families that were hit — low variance means a consistent depth of match everywhere.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- **Does:** hit-weighted variance of per-family mean altitude
- **Outputs:** `float` → *no named wiki consumer yet*
- **Exists for:** L1 census field — first pipeline layer every later layer reads

## Yields (formula)

hit-weighted variance of per-family mean altitude

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

Hesperia-native `34_SPEC` L1 instrumentation — no Java prototype ancestor for the L1-L9 layer pipeline as a whole — Theory Explainer: plain_lang: How much altitude varies across the families that were hit — low variance means a consistent depth of match everywhere.. author: Hesperia L1 (34_SPEC / output_catalog §1). extent: full. reasoning: L1 census field — first pipeline layer every later layer reads. application: [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), L2–L9.

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** How much altitude varies across the families that were hit — low variance means a consistent depth of match everywhere. Source: `docs/foundations/output_catalog.md` §1, re-verified against `compute_L1` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
