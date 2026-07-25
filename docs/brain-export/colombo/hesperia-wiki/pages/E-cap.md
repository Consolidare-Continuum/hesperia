# E_cap

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** 1.0

## Yields (formula)

Clamp ceiling applied after fusion and after every diffusion step.

## Produced from (inputs)

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)

## Needed by (consumers)

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)

## Origin

22_SPEC §3 — Theory Explainer: plain_lang: no activation cell may exceed 1.0; the field stays a bounded probability-like surface. author: 22_SPEC Core Math Contract. extent: full. reasoning: normalized bounded field + with η manufactures exact zeros that kill KL. application: [alpha (fusion weight)](../pages/alpha-fusion-weight.md), [lambda (lazy step)](../pages/lambda-lazy-step.md), [KL divergence](../pages/KL-divergence.md) (REJECTED).

## Notes

**HWIKI-DOC-25:** Clamp after fusion and diffusion — partner of [eta (centroid threshold)](../pages/eta-centroid-threshold.md) in the structural-zero story.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md)
