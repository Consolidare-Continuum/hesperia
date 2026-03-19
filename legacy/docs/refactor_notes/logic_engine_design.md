<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Logic Engine Design (Layer-9)

## Rule model

- Rules are **simple functions** `(state, previous_state) -> event_dict | None`.
- **State** is built from shadow_metrics, propagation_metrics, dynamism_metrics (corrected_area_vector, shadow_diagnostics, propagation_diagnostics, dominant_area_id, etc.).
- When a rule needs a numeric quantity (e.g. dominant area index or share), it uses **core/math** (e.g. `detect_dominant_area`) or reads from state (engine precomputes dominant_area_id).

## Why rules are deterministic

- All inputs (corrected vectors, diagnostics) are deterministic outputs of L7/L8.
- Thresholds are fixed constants (e.g. 0.35 for dominant share, 0.15 for entropy drop).
- No randomness; same inputs always yield same triggered_rules and events.

## Why math stays in core/math

- Share comparison uses the dominant area index and the value at that index (already in state or from core.math).
- No new formulas (entropy, tension, etc.) are implemented in sphere/logic; they are read from shadow_diagnostics and propagation_diagnostics produced by layers that use core/math.

## Rule list

1. **Dominant area** — dominant_area_share ≥ 0.35 → event with area_id, share.
2. **Entropy drop** — entropy_before_shadow − entropy_after_shadow ≥ 0.15 → event with delta_entropy.
3. **Tension increase** — tension_after − tension_before ≥ 0.10 → event with delta_tension.
4. **Propagation spread** — active_edges_count or changed_areas_count ≥ 2 → event with areas_affected.
5. **Dominance transition** — previous_dominant_area != current_dominant_area → event with from, to.

## Future extension path

- Add rules via rule_registry (append to STRUCTURAL_RULES).
- Optional rule_spec (YAML) for configurable thresholds while keeping evaluation deterministic.
- Layer-10 interpretation can consume logic_metrics.triggered_rules and *_events for explanations and UI.
