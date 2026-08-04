# Energy conservation epsilon

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Invariant (constant)  
**Responsible (module):** `core/math/core_math.py — check_conservation_pre_decay, check_shadow_non_creation`  
**Value / default:** 1e-6

## In plain words

after diffusion, total energy must match the pre-diffusion total within this tiny epsilon (before [decay](../pages/decay.md)) — catches broken stochastic matrices.

## Definition

- **Receives:** [lambda (lazy step)](../pages/lambda-lazy-step.md), [shadow_step](../pages/shadow-step.md)
- **Does:** Total energy must be conserved within epsilon after diffusion (E·W), before [decay](../pages/decay.md); shadow output must not exceed shadow input.
- **Outputs:** `1e-6` → *no named wiki consumer yet*
- **Exists for:** conservation check on E·W before decay

## Yields (formula)

Total energy must be conserved within epsilon after diffusion (E·W), before [decay](../pages/decay.md); shadow output must not exceed shadow input.

## Produced from (inputs)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [shadow_step](../pages/shadow-step.md)

## See also

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [shadow_step](../pages/shadow-step.md)
- [decay](../pages/decay.md)
- [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)

## Origin

22_SPEC — physics-style invariant — Theory Explainer: plain_lang: after diffusion, total energy must match the pre-diffusion total within this tiny epsilon (before [decay](../pages/decay.md)) — catches broken stochastic matrices. author: Hesperia wiki (core/math/core_math.py — check_conservation_pre_decay, check_shadow_non_creation). extent: full. reasoning: conservation check on E·W before decay. application: [lambda (lazy step)](../pages/lambda-lazy-step.md), [shadow_step](../pages/shadow-step.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Row-stochastic W preserves total mass by construction before [decay](../pages/decay.md) — this check verifies that construction holds at runtime.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
