# Energy conservation epsilon

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Invariant (constant)  
**Responsible (module):** `core/math/core_math.py — check_conservation_pre_decay, check_shadow_non_creation`  
**Value / default:** 1e-6

## Yields (formula)

Total energy must be conserved within epsilon after diffusion (E·W), before decay; shadow output must not exceed shadow input.

## Produced from (inputs)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [shadow_step](../pages/shadow-step.md)

## Origin

22_SPEC — physics-style invariant

## Notes

Row-stochastic W preserves total mass by construction before decay — this check verifies that construction holds at runtime.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md)
