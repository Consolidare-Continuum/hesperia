# KL divergence

**Status:** 🔴 REJECTED — explicit, reasoned decision against, not an oversight  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a — zero matches for `kl_divergence`/`def kl(` in any `.py``  
**Value / default:** —

## In plain words

how different distribution p is from q; blows up if q has a zero where p does not.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** kl(p,q) = Σ p_i·log(p_i/q_i) — Java 21_MATH proposed relative entropy between two distributions.
- **Outputs:** `—` → [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md), [eta (centroid threshold)](../pages/eta-centroid-threshold.md), [E_cap](../pages/E-cap.md), [S=T·C·X_A / S′ composite (Java)](../pages/S-T-C-X-A-S-composite-Java.md), [meanTau/varTau/stdTau/fillingRate/adjacencyCorrelation (Java)](../pages/meanTau-varTau-stdTau-fillingRate-adjacencyCorrelation-Java.md), [expectedTimeToObstacle (Java)](../pages/expectedTimeToObstacle-Java.md), [utility / strategicScore / actionScore (Java)](../pages/utility-strategicScore-actionScore-Java.md), [causalCoherence / decisionIntegrity / temporalStability (Java)](../pages/causalCoherence-decisionIntegrity-temporalStability-Java.md), [IPS / QCS (Java)](../pages/IPS-QCS-Java.md), [domainFit / scaleConsistency / compatibilityScore (Java)](../pages/domainFit-scaleConsistency-compatibilityScore-Java.md), [runLoop / shouldBreak (Java)](../pages/runLoop-shouldBreak-Java.md), [summaryFidelity / compressionRatio (Java)](../pages/summaryFidelity-compressionRatio-Java.md), [Sentence capacity 3-5/side (Java)](../pages/Sentence-capacity-3-5-side-Java.md), [tau_s per-side truth (Java)](../pages/tau-s-per-side-truth-Java.md)
- **Exists for:** [eta (centroid threshold)](../pages/eta-centroid-threshold.md) + [E_cap](../pages/E-cap.md) manufacture exact zeros → KL undefined; Shannon [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md) stays

## Yields (formula)

kl(p,q) = Σ p_i·log(p_i/q_i) — Java 21_MATH proposed relative entropy between two distributions.

## Needed by (consumers)

- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- [E_cap](../pages/E-cap.md)
- [S=T·C·X_A / S′ composite (Java)](../pages/S-T-C-X-A-S-composite-Java.md)
- [meanTau/varTau/stdTau/fillingRate/adjacencyCorrelation (Java)](../pages/meanTau-varTau-stdTau-fillingRate-adjacencyCorrelation-Java.md)
- [expectedTimeToObstacle (Java)](../pages/expectedTimeToObstacle-Java.md)
- [utility / strategicScore / actionScore (Java)](../pages/utility-strategicScore-actionScore-Java.md)
- [causalCoherence / decisionIntegrity / temporalStability (Java)](../pages/causalCoherence-decisionIntegrity-temporalStability-Java.md)
- [IPS / QCS (Java)](../pages/IPS-QCS-Java.md)
- [domainFit / scaleConsistency / compatibilityScore (Java)](../pages/domainFit-scaleConsistency-compatibilityScore-Java.md)
- [runLoop / shouldBreak (Java)](../pages/runLoop-shouldBreak-Java.md)
- [summaryFidelity / compressionRatio (Java)](../pages/summaryFidelity-compressionRatio-Java.md)
- [Sentence capacity 3-5/side (Java)](../pages/Sentence-capacity-3-5-side-Java.md)
- [tau_s per-side truth (Java)](../pages/tau-s-per-side-truth-Java.md)

## See also

- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- [E_cap](../pages/E-cap.md)
- [S=T·C·X_A / S′ composite (Java)](../pages/S-T-C-X-A-S-composite-Java.md)
- [meanTau/varTau/stdTau/fillingRate/adjacencyCorrelation (Java)](../pages/meanTau-varTau-stdTau-fillingRate-adjacencyCorrelation-Java.md)
- [expectedTimeToObstacle (Java)](../pages/expectedTimeToObstacle-Java.md)
- [utility / strategicScore / actionScore (Java)](../pages/utility-strategicScore-actionScore-Java.md)
- [causalCoherence / decisionIntegrity / temporalStability (Java)](../pages/causalCoherence-decisionIntegrity-temporalStability-Java.md)
- [IPS / QCS (Java)](../pages/IPS-QCS-Java.md)
- [domainFit / scaleConsistency / compatibilityScore (Java)](../pages/domainFit-scaleConsistency-compatibilityScore-Java.md)
- [runLoop / shouldBreak (Java)](../pages/runLoop-shouldBreak-Java.md)
- [summaryFidelity / compressionRatio (Java)](../pages/summaryFidelity-compressionRatio-Java.md)

## Origin

Kullback & Leibler (1951) / Java 21_MATH `kl(p,q)` — Theory Explainer: plain_lang: how different distribution p is from q; blows up if q has a zero where p does not. author: Kullback–Leibler (1951) as the Java proposal's theory family. extent: rejected_with_reason. reasoning: [eta (centroid threshold)](../pages/eta-centroid-threshold.md) + [E_cap](../pages/E-cap.md) manufacture exact zeros → KL undefined; Shannon [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md) stays. application: contrast Shannon; FPD/APD L2 profile distance fills the comparison slot.

## Notes

**HWIKI-DOC-03:** Structural reason, not taste. Kolmogorov complexity was separately, explicitly rejected as uncomputable — same discipline, different item.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
