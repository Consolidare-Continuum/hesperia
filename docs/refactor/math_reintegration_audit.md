# Math Reintegration Audit

**Scope:** `sphere/dynamism/`, `sphere/metrics/`, `sphere/pipeline/`  
**Rule:** Math is infrastructure → lives only in `core/math`. Sphere layers orchestrate only; they must import math primitives and must not implement math.

---

## Audit Table

| Function | Location | Type | Action |
|----------|----------|------|--------|
| `compute_curvature` | sphere/dynamism/curvature.py | curvature metrics | MOVE → core/math/curvature_metrics.py |
| `compute_stability_index` | sphere/dynamism/stability.py | stability metrics | MOVE → core/math/stability_metrics.py |
| `compute_transition_matrix` | sphere/dynamism/transition_matrix.py | transition matrix | MOVE → core/math/transition_matrix.py |
| `compute_transition_probabilities` | sphere/dynamism/transition_matrix.py | transition matrix / normalization | MOVE → core/math/transition_matrix.py |
| `build_trajectory` | sphere/dynamism/trajectory.py | sequence/vector ops | MOVE → core/math/sequence_utils.py |
| `compress_trajectory` | sphere/dynamism/trajectory.py | sequence ops | MOVE → core/math/sequence_utils.py |
| `compute_jump_rate` | sphere/dynamism/jump_rate.py | curvature/jump metrics | MOVE → core/math/curvature_metrics.py (or jump_metrics) |
| `compute_entropy` | sphere/metrics/entropy.py | entropy | MOVE → core/math/entropy_metrics.py |
| `compute_normalized_entropy` | sphere/metrics/entropy.py | entropy / normalization | MOVE → core/math/entropy_metrics.py |
| `compute_structural_tension` | sphere/metrics/tension.py | stability/tension metric | MOVE → core/math/stability_metrics.py |
| `detect_dominant_area` | sphere/metrics/dominance.py | argmax / dominance | MOVE → core/math/vector_ops.py or dominance.py |
| `detect_dominant_family` | sphere/metrics/dominance.py | argmax / dominance | MOVE → core/math/vector_ops.py or dominance.py |
| `detect_family_peaks` | sphere/metrics/dominance.py | top-k / ranking | MOVE → core/math/vector_ops.py or dominance.py |
| `compute_family_coverage` | sphere/metrics/coverage.py | coverage fraction | MOVE → core/math/coverage.py |
| `compute_area_coverage` | sphere/metrics/coverage.py | coverage fraction | MOVE → core/math/coverage.py |
| `compute_loopability` | sphere/metrics/loopability.py | structural metric (counts) | MOVE → core/math/sequence_metrics.py |

**Pipeline:** `sphere/pipeline/contract_validation.py`, `sphere/pipeline/isolation_validation.py` — no mathematical logic; no changes.

**Dynamism engine:** `sphere/dynamism/dynamism_engine.py` — orchestration only (calls curvature, stability, trajectory, transition_matrix, jump_rate). After migration it will import from `core.math` and call same APIs.

---

## Summary by Target Module

| core/math module | Functions moved from sphere |
|------------------|----------------------------|
| curvature_metrics.py | compute_curvature, compute_jump_rate |
| stability_metrics.py | compute_stability_index, compute_structural_tension |
| transition_matrix.py | compute_transition_matrix, compute_transition_probabilities |
| entropy_metrics.py | compute_entropy, compute_normalized_entropy |
| vector_ops.py | detect_dominant_area, detect_dominant_family, detect_family_peaks (argmax/top-k) |
| coverage.py | compute_family_coverage, compute_area_coverage |
| sequence_utils.py | build_trajectory, compress_trajectory |
| sequence_metrics.py | compute_loopability |

---

## Dependency Direction (Enforced)

- **Allowed:** `sphere/*` → `core/math`
- **Forbidden:** `sphere/*` implementing math internally (numpy formulas, log, matrix ops, etc.)
