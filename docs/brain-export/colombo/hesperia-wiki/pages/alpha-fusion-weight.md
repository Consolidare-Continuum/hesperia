# alpha (fusion weight)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (default constant)  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** 0.65

## In plain words

blend two evidence maps into one energy field; α=0.65 leans toward Dict A (surface).

## Definition

- **Receives:** *S vector (Dict A)*, *L vector (Dict B)*
- **Does:** E0[i] = clamp(alpha·S'[i] + (1-alpha)·L'[i], 0, [E_cap](../pages/E-cap.md)) — 65/35 surface-biased weighted fusion of two normalized evidence vectors S (Dict A) and L (Dict B).
- **Outputs:** `0.65` → *centroid indices (activation)*, *E0 (fused energy)*, [eta (centroid threshold)](../pages/eta-centroid-threshold.md), [E_cap](../pages/E-cap.md), [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md), [energy_conservation_tolerance](../pages/energy-conservation-tolerance.md)
- **Exists for:** first stage of evidence fusion before centroid/η and diffusion

## Yields (formula)

E0[i] = clamp(alpha·S'[i] + (1-alpha)·L'[i], 0, [E_cap](../pages/E-cap.md)) — 65/35 surface-biased weighted fusion of two normalized evidence vectors S (Dict A) and L (Dict B).

## Produced from (inputs)

- *S vector (Dict A)*
- *L vector (Dict B)*

## Needed by (consumers)

- *centroid indices (activation)*
- *E0 (fused energy)*
- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- [E_cap](../pages/E-cap.md)
- [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md)
- [energy_conservation_tolerance](../pages/energy-conservation-tolerance.md)

## See also

- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- [E_cap](../pages/E-cap.md)
- [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md)
- [energy_conservation_tolerance](../pages/energy-conservation-tolerance.md)

## Origin

22_SPEC Core Math Contract v1.0 §3 — Theory Explainer: plain_lang: blend two evidence maps into one energy field; α=0.65 leans toward Dict A (surface). author: convex combination / linear scalarization (ops research pattern; not a single eponym paper). extent: full. reasoning: first stage of evidence fusion before centroid/η and diffusion. application: [E_cap](../pages/E-cap.md), [eta (centroid threshold)](../pages/eta-centroid-threshold.md), [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md); contrast dead [KL divergence](../pages/KL-divergence.md).

## Notes

**HWIKI-DOC-25 (fusion trio):** With [E_cap](../pages/E-cap.md) and [eta (centroid threshold)](../pages/eta-centroid-threshold.md) this is the LIVE fusion spine. Distinct from diffusion α / [Wiener feedback on alpha (k_s / k_j)](../pages/Wiener-feedback-on-alpha-k-s-k-j.md).

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
