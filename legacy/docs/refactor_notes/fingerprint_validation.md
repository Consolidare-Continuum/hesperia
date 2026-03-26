<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Fingerprint Validation

## Why fingerprint stability matters

The USF **fingerprint** is the canonical structural summary used for comparison, deduplication, and drift detection. It is derived deterministically from interpretation_metrics (Layer-10). If the same raw_text always produced a different fingerprint, downstream consumers could not reliably compare runs or detect meaningful change.

- **Determinism:** Identical text and config must produce the same fingerprint. This is enforced by deterministic Layer-9 and Layer-10 and by fixed-point inference in the execution_flow.
- **Stability:** Small lexical or formatting changes should not cause large fingerprint changes unless they alter structural attribution (e.g. dominant area or event set).
- **Sensitivity:** Large semantic or structural changes should be reflected in the fingerprint (e.g. different structural_state or active_events).

## How drift is measured

Drift is measured by comparing two fingerprints (e.g. from two execution_flow runs).

### Frozen drift formula

```
drift_score = (state_delta * 0.6) + (event_delta * 0.4)
```

Definitions:

- `state_delta` = number of changed state keys / total state keys (e.g. structural_state, dominant_area_id, entropy_state, tension_state, propagation_state). If both fingerprints have the same keys, count how many values differ; divide by total keys.
- `event_delta` = |events₁ △ events₂| / max(|events₁ ∪ events₂|, 1) (symmetric difference of active_events over union size), or equivalently event_difference / total_events when comparing two runs.

### Thresholds

- `minor_change_threshold` = 0.15
- `major_change_threshold` = 0.40

### Interpretation

| Score        | Meaning           |
|-------------|-------------------|
| &lt; 0.15    | Stable fingerprint |
| 0.15 – 0.40 | Moderate drift     |
| &gt; 0.40    | Semantic shift     |

## Test thresholds

- **Determinism:** For the same (text, config, document_id), `usf["fingerprint"]` must be byte-identical (or dict-equal) across runs.
- **Limited drift (minor lexical):** For small wording changes (e.g. adding a word or synonym), `event_delta` should be bounded (e.g. ≤ 10) and often `state_changed == 0`. Exact thresholds are project-specific.
- **Larger drift (major semantic):** For very different texts, we allow and expect that `state_changed` or `event_delta` can be larger; tests should not require that they always differ, only that the comparison is well-defined and that the fingerprint reflects structural meaning.

Tests live under `tests/fingerprint/`: determinism and drift assertions as above.
