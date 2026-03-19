<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Prolog Fact Schema (Frozen)

## Input facts (from pipeline)

Allowed only:

- `dominant_area`
- `entropy_drop`
- `tension_increase`
- `dominance_transition`
- `propagation_spread`

Optional diagnostic facts:

- `low_entropy`
- `high_entropy`
- `stable_structure`

## Derived facts

- `structural_focus`
- `transition_risk`
- `elevated_risk`
- `structural_instability`
- `propagation_wave`

## Naming rules

- Lowercase `snake_case`.
- No parameters (boolean facts only).
- No synonyms.

## Fact order

Facts are sorted lexicographically before inference to guarantee deterministic order.

## Rule trace schema (frozen)

Every rule trace entry is structured as follows. No free text.

```json
{
  "rule": "transition_risk_rule",
  "premises": ["dominance_transition"],
  "derived": "transition_risk",
  "iteration": 2
}
```

- `rule`: Rule name (snake_case, suffix `_rule`).
- `premises`: List of predicate names that matched (input facts).
- `derived`: Single derived predicate name (no parameters).
- `iteration`: 1-based iteration index when the rule fired.
