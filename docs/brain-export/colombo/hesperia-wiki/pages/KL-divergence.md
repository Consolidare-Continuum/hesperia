# KL divergence

**Status:** 🔴 REJECTED — explicit, reasoned decision against, not an oversight  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a — zero matches for `kl_divergence`/`def kl(` in any `.py``  
**Value / default:** —

## Yields (formula)

kl(p,q) = Σ p_i·log(p_i/q_i) — Java 21_MATH proposed relative entropy between two distributions.

## Origin

Kullback & Leibler (1951) / Java 21_MATH `kl(p,q)` — Theory Explainer: plain_lang: how different distribution p is from q; blows up if q has a zero where p does not. author: Kullback–Leibler (1951) as the Java proposal's theory family. extent: rejected_with_reason. reasoning: [eta (centroid threshold)](../pages/eta-centroid-threshold.md) + [E_cap](../pages/E-cap.md) manufacture exact zeros → KL undefined; Shannon [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md) stays. application: contrast Shannon; FPD/APD L2 profile distance fills the comparison slot.

## Notes

**HWIKI-DOC-03:** Structural reason, not taste. Kolmogorov complexity was separately, explicitly rejected as uncomputable — same discipline, different item.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md)
