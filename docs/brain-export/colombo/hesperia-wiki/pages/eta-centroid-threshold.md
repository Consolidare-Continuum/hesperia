# eta (centroid threshold)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py — centroid_indices()`  
**Value / default:** 0.02

## In plain words

ignore near-zero energy cells when picking the 'active' centroid set.

## Definition

- **Receives:** [alpha (fusion weight)](../pages/alpha-fusion-weight.md), [E_cap](../pages/E-cap.md)
- **Does:** active = [i for i in range(len(E0)) if E0[i] > eta] — sparse centroid selection floor.
- **Outputs:** `0.02` → [K_max](../pages/K-max.md), [KL divergence](../pages/KL-divergence.md)
- **Exists for:** sparse activation; **structural reason [KL divergence](../pages/KL-divergence.md) is REJECTED** (zeros in q)

## Yields (formula)

active = [i for i in range(len(E0)) if E0[i] > eta] — sparse centroid selection floor.

## Produced from (inputs)

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- [E_cap](../pages/E-cap.md)

## Needed by (consumers)

- [K_max](../pages/K-max.md)
- [KL divergence](../pages/KL-divergence.md)

## See also

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- [E_cap](../pages/E-cap.md)
- [K_max](../pages/K-max.md)
- [KL divergence](../pages/KL-divergence.md)
- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md)
- [energy_conservation_tolerance](../pages/energy-conservation-tolerance.md)

## Origin

22_SPEC §4 — Theory Explainer: plain_lang: ignore near-zero energy cells when picking the 'active' centroid set. author: 22_SPEC Core Math Contract. extent: full. reasoning: sparse activation; **structural reason [KL divergence](../pages/KL-divergence.md) is REJECTED** (zeros in q). application: [K_max](../pages/K-max.md), contrast [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md).

## Notes

**HWIKI-DOC-25:** With [E_cap](../pages/E-cap.md) + clamp, η is why centroid selection kills KL — not taste.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
