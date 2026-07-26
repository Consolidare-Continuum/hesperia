# compute_entropy (Shannon)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Entropy and Information Theory](../categories/Entropy-and-Information-Theory.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/entropy_metrics.py`  
**Value / default:** —

## Yields (formula)

H = −Σ p·log(p); compute_normalized_entropy divides by ln(M).

## Produced from (inputs)

- *E (energy vector)*

## Needed by (consumers)

- [P_disp (dispersion penalty)](../pages/P-disp-dispersion-penalty.md)
- [entropy_threshold (monotony)](../pages/entropy-threshold-monotony.md)
- [Mixing Diagnostics](../pages/Mixing-Diagnostics.md)

## Origin

Shannon (1948), *A Mathematical Theory of Communication* — Theory Explainer: plain_lang: how spread-out / unpredictable a distribution is; high entropy = energy smeared across many sides, low = concentrated. author: Claude Shannon (1948). extent: full (canonical H and H/ln(M)). reasoning: reused as the system's information primitive rather than inventing a second entropy. application: [P_disp (dispersion penalty)](../pages/P-disp-dispersion-penalty.md), [entropy_threshold (monotony)](../pages/entropy-threshold-monotony.md), [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) (`compute_normalized_entropy`).

## Notes

**HWIKI-DOC-02:** The single most-reused mathematical primitive in the whole system — canonical, not tool-local. Contrast [KL divergence](../pages/KL-divergence.md) (REJECTED) and tool-local [area_entropy (tool-local)](../pages/area-entropy-tool-local.md).

---
[← back to category](../categories/Entropy-and-Information-Theory.md) · [wiki home](../index.md)
