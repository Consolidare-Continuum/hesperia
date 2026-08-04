# energy_conservation_tolerance

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py -> DEFAULT_CONFIG["energy_conservation_tolerance"]; check_conservation_pre_decay`  
**Value / default:** 1e-6 (must be < 1e-3)

## In plain words

how much drift the pre-decay energy-conservation check allows before rejecting the step.

## Definition

- **Receives:** [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- **Does:** Tolerance the pre-[decay](../pages/decay.md) energy-conservation check allows before rejecting a step as physically invalid.
- **Outputs:** `1e-6 (must be < 1e-3)` → *check_conservation_pre_decay*
- **Exists for:** tolerance twin of [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md)

## Yields (formula)

Tolerance the pre-[decay](../pages/decay.md) energy-conservation check allows before rejecting a step as physically invalid.

## Produced from (inputs)

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)

## Needed by (consumers)

- *check_conservation_pre_decay*

## See also

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- [E_cap](../pages/E-cap.md)
- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md)

## Origin

Hesperia-native Core Math Contract constant — no Java prototype ancestor — Theory Explainer: plain_lang: how much drift the pre-decay energy-conservation check allows before rejecting the step. author: Hesperia wiki (core/math/core_math.py -> DEFAULT_CONFIG["energy_conservation_tolerance"]; check_cons. extent: full. reasoning: tolerance twin of [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md). application: *check_conservation_pre_decay*.

## Notes

**HWIKI-WIRE:** attached to category anchor [alpha (fusion weight)](../pages/alpha-fusion-weight.md). **HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-CROSSCHECK (2026-08-04):** Last genuine gap found in a full parameter_catalog.md-vs-wiki cross-check after the HWIKI-CATALOG wave — every other §3/§4 constant (k_amb, tau_core, k_thin, k_disp, k_guard, k_shadow, delta_gap, max_shadow_hops, w_decay/w_guard_obs/w_shadow_obs, severe_curvature_threshold, severe_jump_rate_threshold) turned out already covered inside the P_amb/P_disp/P_guard/P_shadow/P_thin penalty pages or the paired curvature/jump_rate threshold pages, just not under their own bare name. This one genuinely had no page.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
