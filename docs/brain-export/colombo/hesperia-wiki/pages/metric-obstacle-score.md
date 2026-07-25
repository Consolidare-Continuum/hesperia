# metric_obstacle_score

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Composite metric  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** w_decay=0.50, w_guard_obs=0.30, w_shadow_obs=0.20 (CI-enforced sum = 1.0 ± 1e-6)

## Yields (formula)

obstacle_score = w_decay·Loss + w_guard_obs·clamp(GuardCount,0,1) + w_shadow_obs·(shadow_hops/max_shadow_hops)

## Produced from (inputs)

- [decay](../pages/decay.md)
- [P_guard (guard penalty)](../pages/P-guard-guard-penalty.md)
- [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)

## Origin

22_SPEC §12 / validate_config §16

## Notes

Weights encode a judgment (half from decay loss) — building a config where these three don't sum to 1 fails CI.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md)
