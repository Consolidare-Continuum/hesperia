# LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Formula / function  
**Responsible (module):** `core/layers/layer_6.py:76-77`  
**Value / default:** —

## In plain words

a single number claiming 'how stable is this read' from condition + a Lyapunov-named proxy.

## Definition

- **Receives:** [CONDITION_NUMBER (L6)](../pages/CONDITION-NUMBER-L6.md), [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md)
- **Does:** GLOBAL_STABILITY_SCORE = 1 / (1 + CONDITION_NUMBER + |LYAPUNOV_ESTIMATE|) — single-step perturbation-growth proxy.
- **Outputs:** `—` → [CONCEPTUAL_COHERENCE_INDEX (L6)](../pages/CONCEPTUAL-COHERENCE-INDEX-L6.md), *sphere/pipeline/contract_validation.py contract*, [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md), [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md), [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md), [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md), [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)
- **Exists for:** SCIENCE.md honesty — not a literal Lyapunov exponent

## Yields (formula)

GLOBAL_STABILITY_SCORE = 1 / (1 + CONDITION_NUMBER + |LYAPUNOV_ESTIMATE|) — single-step perturbation-growth proxy.

## Produced from (inputs)

- [CONDITION_NUMBER (L6)](../pages/CONDITION-NUMBER-L6.md)
- [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md)

## Needed by (consumers)

- [CONCEPTUAL_COHERENCE_INDEX (L6)](../pages/CONCEPTUAL-COHERENCE-INDEX-L6.md)
- *sphere/pipeline/contract_validation.py contract*
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)

## See also

- [CONDITION_NUMBER (L6)](../pages/CONDITION-NUMBER-L6.md)
- [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md)
- [CONCEPTUAL_COHERENCE_INDEX (L6)](../pages/CONCEPTUAL-COHERENCE-INDEX-L6.md)
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)
- [structural analogy (extent term)](../pages/structural-analogy-extent-term.md)

## Origin

Lyapunov (1892), *General Problem of the Stability of Motion* — Theory Explainer: plain_lang: a single number claiming 'how stable is this read' from condition + a Lyapunov-named proxy. author: A.M. Lyapunov (1892). extent: structural_analogy (proxy, not iterated exponent). reasoning: SCIENCE.md honesty — not a literal Lyapunov exponent. application: *GLOBAL_STABILITY_SCORE* path into L7/L8; [CONCEPTUAL_COHERENCE_INDEX (L6)](../pages/CONCEPTUAL-COHERENCE-INDEX-L6.md).

## Notes

**HWIKI-DOC-12 / L6:** Explicitly a conceptual proxy — no iterated perturbation, no divergence-rate over many steps. Same honesty discipline as Java [ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)](../pages/ALPHA-BETA-GAMMA-DELTA-integrity-quartet-Java.md). L6 neighbors: [CONDITION_NUMBER (L6)](../pages/CONDITION-NUMBER-L6.md), [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md), [SPECTRAL_GAP (L6)](../pages/SPECTRAL-GAP-L6.md).

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
