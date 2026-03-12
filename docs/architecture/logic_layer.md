<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Logic Layer (Layer-9) — Architecture

## Role

Layer-9 evaluates **deterministic structural rules** on the stable signals produced by Layer-8 (shadow correction) and Layer-7 (propagation). It detects structural events and produces logic_metrics for downstream interpretation (e.g. L10).

## Position in Pipeline

```
propagation (L7) → shadow (L8) → logic (L9) → interpretation (L10, future)
```

- **Inputs:** shadow_metrics (corrected_area_vector, corrected_family_counts, shadow_diagnostics), propagation_metrics (propagation_diagnostics), dynamism_metrics (stability_index, jump_rate, curvature). Optional: previous_pipeline_state for dominance transition.
- **Outputs:** logic_metrics (triggered_rules, dominance_events, entropy_events, tension_events, anomaly_flags, logic_diagnostics).

## Rule Model

- Rules are **deterministic structural predicates**. They do not implement math; they call **core/math** when needed (e.g. `detect_dominant_area` for share checks).
- Rule categories: dominant area, entropy drop, tension increase, propagation spread, dominance transition.
- Events are typed (dominant_area, entropy_drop, tension_increase, propagation_spread, dominance_transition) and carry minimal payload (area_id, share, delta_entropy, etc.).

## Modules

- **rule_types.py** — Event type constants and thresholds.
- **rule_registry.py** — List of rule functions; each returns event dict or None.
- **rule_evaluator.py** — Evaluates all rules, groups events by type.
- **rule_engine.py** — `compute_logic_metrics(shadow_metrics, propagation_metrics, dynamism_metrics, previous_state=None)` builds state, runs evaluator, builds logic_diagnostics.
- **diagnostics.py** — `build_logic_diagnostics(...)` for rules_evaluated_count, rules_triggered_count, dominant_area, entropy_after_shadow, tension_after_shadow, propagation_spread.

## Dependency Rule

- **sphere/logic** may call **core/math** (e.g. vector_ops.detect_dominant_area). It must not implement numeric formulas itself.
