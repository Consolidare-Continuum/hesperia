# decay

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py — base_step()`  
**Value / default:** 0.04

## Yields (formula)

E_next = clamp(D·(1-decay), 0, E_cap) — damped discrete-time attrition after each diffusion step.

## Produced from (inputs)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)

## Origin

22_SPEC §5

## Notes

Structural analogy to LIF self-decay (Lapicque 1907) noted in related H_self paths; not claimed as literal.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md)
