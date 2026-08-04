# DOMINANT_FAMILY_ID

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 -> result["DOMINANT_FAMILY_ID"]`  
**Value / default:** int [0,287]

## In plain words

Which family had the most hits this run.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- **Does:** argmax(hits), first index on ties
- **Outputs:** `int [0,287]` → *no named wiki consumer yet*
- **Exists for:** L1 census field — first pipeline layer every later layer reads

## Yields (formula)

argmax(hits), first index on ties

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
- [DOMINANT_AREA_ID](../pages/DOMINANT-AREA-ID.md)
- [DOMINANCE_RATIO](../pages/DOMINANCE-RATIO.md)

## Origin

Hesperia-native `34_SPEC` L1 instrumentation — no Java prototype ancestor for the L1-L9 layer pipeline as a whole — Theory Explainer: plain_lang: Which family had the most hits this run.. author: Hesperia L1 (34_SPEC / output_catalog §1). extent: full. reasoning: L1 census field — first pipeline layer every later layer reads. application: [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), L2–L9.

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** Which family had the most hits this run. Source: `docs/foundations/output_catalog.md` §1, re-verified against `compute_L1` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
