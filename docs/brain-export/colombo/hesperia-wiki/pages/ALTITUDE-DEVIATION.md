# ALTITUDE_DEVIATION

**Status:** 🟡 PARTIAL — present in a narrow slice/tool, not the full contract  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 -> result["ALTITUDE_DEVIATION"] (doubly-conditional)`  
**Value / default:** float

## In plain words

Distance from the profile's altitude band/target.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- **Does:** See notes — only computed when both a profile is supplied and the profile sets the specific field this key checks.
- **Outputs:** `float` → *no named wiki consumer yet*
- **Exists for:** only when profile has `ALT_BAND`/`ALT_TARGET`

## Yields (formula)

See notes — only computed when both a profile is supplied and the profile sets the specific field this key checks.

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

Hesperia-native `34_SPEC N1` profile-conformance extension — no Java prototype ancestor — Theory Explainer: plain_lang: Distance from the profile's altitude band/target.. author: Hesperia L1 profile extension (34_SPEC N1). extent: partial. reasoning: only when profile has `ALT_BAND`/`ALT_TARGET`. application: [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md).

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** Distance from the profile's altitude band/target. Narrower than the other 6 profile keys: only appears when profile has `ALT_BAND`/`ALT_TARGET`, not merely when a profile is supplied at all. Source: `docs/foundations/output_catalog.md` §1.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
