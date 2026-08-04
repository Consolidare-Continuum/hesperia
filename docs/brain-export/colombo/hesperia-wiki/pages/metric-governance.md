# metric_governance

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Composite metric  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** —

## In plain words

five independent taxes (ambiguity, thin-core, dispersion, guard, shadow) sum and invert into one 0–1 health score.

## Definition

- **Receives:** [P_amb (ambiguity penalty)](../pages/P-amb-ambiguity-penalty.md), [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md), [P_disp (dispersion penalty)](../pages/P-disp-dispersion-penalty.md), [P_guard (guard penalty)](../pages/P-guard-guard-penalty.md), [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)
- **Does:** metric_governance = clamp(1 − (P_amb+P_thin+P_shadow+P_disp+P_guard), 0, 1) — single health number.
- **Outputs:** `—` → *no named wiki consumer yet*
- **Exists for:** preferred over Java multiplicative integrity powers — each penalty CI-testable alone

## Yields (formula)

metric_governance = clamp(1 − (P_amb+P_thin+P_shadow+P_disp+P_guard), 0, 1) — single health number.

## Produced from (inputs)

- [P_amb (ambiguity penalty)](../pages/P-amb-ambiguity-penalty.md)
- [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md)
- [P_disp (dispersion penalty)](../pages/P-disp-dispersion-penalty.md)
- [P_guard (guard penalty)](../pages/P-guard-guard-penalty.md)
- [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)

## See also

- [P_amb (ambiguity penalty)](../pages/P-amb-ambiguity-penalty.md)
- [P_thin (thin-core penalty)](../pages/P-thin-thin-core-penalty.md)
- [P_disp (dispersion penalty)](../pages/P-disp-dispersion-penalty.md)
- [P_guard (guard penalty)](../pages/P-guard-guard-penalty.md)
- [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)
- [ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)](../pages/ALPHA-BETA-GAMMA-DELTA-integrity-quartet-Java.md)
- [metric_obstacle_score](../pages/metric-obstacle-score.md)

## Origin

22_SPEC §12 — Theory Explainer: plain_lang: five independent taxes (ambiguity, thin-core, dispersion, guard, shadow) sum and invert into one 0–1 health score. author: 22_SPEC Core Math Contract (additive penalty-governance pattern). extent: full (suite as one explainable system). reasoning: preferred over Java multiplicative integrity powers — each penalty CI-testable alone. application: governance consumers; pattern reused by [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md); contrast dead [ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)](../pages/ALPHA-BETA-GAMMA-DELTA-integrity-quartet-Java.md).

## Notes

**HWIKI-DOC-23:** Hub for the penalty suite P_amb/thin/disp/guard/shadow. Clearest 'combine independent criteria into one thresholdable number' example in the repo.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
