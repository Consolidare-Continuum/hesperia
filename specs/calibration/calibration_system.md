---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CAL-SYSTEM
---

# Calibration system — canonical law

## 1. Authority

This document defines **what may be tuned**, **how search is gated**, and **where parameters live**.  
**Numeric family-field stepping** is defined only in [../dynamics/semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md).  
**Ranking score for parameter sets** is [hspr_index.md](hspr_index.md) §2 (HCI).

## 2. Parameter classes (binding)

| Class | Meaning | Examples |
|-------|---------|----------|
| **A** | Fixed structural constants — **not** tuned | Area count, icosahedral adjacency, family→area membership, public projection rules (`docs/TOPOLOGY_INVARIANTS.md`) |
| **B** | Controlled dynamic knobs | Decays, gains, contradiction penalties, resistance diagonals — see `assets/calibration/dynamics_parameter_registry.yaml` |
| **C** | Derived observables — **outputs only**, never tuned as primary knobs | Tension, Ξ proxies, narrative metrics from field state |

## 3. Registry (binding location)

- **Class B registry:** `assets/calibration/dynamics_parameter_registry.yaml` (component path references must match `EXTENSION_STATUS.yaml` / `hesperia.extensions.dynamics`).
- **Semantic field v1 JSON:** `assets/calibration/semantic_field_equations_v1.json` — parameters for Euler step in §6 of [semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md).

## 4. Procedure (binding)

1. **Constraint-first:** discard candidates violating §3 hard checks in implementation (`calibrate_parameter_grid` and related).
2. **Deterministic search:** grid or enumerated search; same inputs → same ranking.
3. **Governance:** named profiles frozen by release process; automation proposes, humans accept.
4. **Scoring:** HCI in [hspr_index.md](hspr_index.md); **not** proof of domain truth.

## 5. Extended blueprint (non-binding equations)

Long-form scenario tables, worked examples, and Ethan L-layer mapping remain in [../dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) **for explanation only** — if that file disagrees with **Class A/B/C** here, **this file wins**.
