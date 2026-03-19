# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.
#
# Canonical semantic field equations engine. L_F, R_F, C must be supplied explicitly
# from registry/config/topology — no hidden defaults in this module.

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

import numpy as np

ArrayLike = np.ndarray


def _as_float_array(x: Sequence[float] | np.ndarray, *, ndim: int, name: str) -> np.ndarray:
    arr = np.asarray(x, dtype=float)
    if arr.ndim != ndim:
        raise ValueError(f"{name} must have ndim={ndim}, got shape={arr.shape}")
    return arr


def _ensure_square_matrix(x: Sequence[Sequence[float]] | np.ndarray, *, name: str) -> np.ndarray:
    arr = _as_float_array(x, ndim=2, name=name)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError(f"{name} must be square, got shape={arr.shape}")
    return arr


def _ensure_vector_length(x: Sequence[float] | np.ndarray, *, n: int, name: str) -> np.ndarray:
    arr = _as_float_array(x, ndim=1, name=name)
    if arr.shape[0] != n:
        raise ValueError(f"{name} length mismatch: expected {n}, got {arr.shape[0]}")
    return arr


def _clip01(x: np.ndarray) -> np.ndarray:
    return np.clip(x, 0.0, 1.0)


def _round_list(x: np.ndarray, digits: int = 6) -> List[float]:
    return np.round(np.asarray(x, dtype=float), digits).tolist()


def _round_scalar(x: float, digits: int = 6) -> float:
    return round(float(x), digits)


@dataclass(frozen=True)
class SemanticFieldParams:
    alpha: float
    beta: float
    gamma: float
    delta: float
    mu: float = 0.0
    dt: float = 1.0
    epsilon: float = 1e-6
    tau: float = 1e-6
    clip_mode: bool = True

    def validate(self) -> None:
        for name in ("alpha", "beta", "gamma", "delta", "mu", "dt", "epsilon", "tau"):
            value = getattr(self, name)
            if value < 0:
                raise ValueError(f"{name} must be >= 0, got {value}")
        if self.dt == 0:
            raise ValueError("dt must be > 0")


@dataclass(frozen=True)
class FieldStepResult:
    field_prev: np.ndarray
    field_next: np.ndarray
    source_vector: np.ndarray
    pressure_vector: np.ndarray
    delta_vector: np.ndarray
    energy_prev: float
    energy_next: float
    converged_numerical: bool
    converged_contradiction: bool
    observables: Dict[str, float]

    def to_json_dict(self, *, digits: int = 6) -> Dict[str, Any]:
        return {
            "field_prev": _round_list(self.field_prev, digits),
            "field_next": _round_list(self.field_next, digits),
            "source_vector": _round_list(self.source_vector, digits),
            "pressure_vector": _round_list(self.pressure_vector, digits),
            "delta_vector": _round_list(self.delta_vector, digits),
            "energy_prev": _round_scalar(self.energy_prev, digits),
            "energy_next": _round_scalar(self.energy_next, digits),
            "converged_numerical": self.converged_numerical,
            "converged_contradiction": self.converged_contradiction,
            "observables": {k: _round_scalar(v, digits) for k, v in self.observables.items()},
        }


@dataclass(frozen=True)
class TimelineStep:
    step_index: int
    result: FieldStepResult

    def to_json_dict(self, *, digits: int = 6) -> Dict[str, Any]:
        payload = self.result.to_json_dict(digits=digits)
        payload["step_index"] = self.step_index
        return payload


def build_family_laplacian(
    adjacency_matrix: Sequence[Sequence[float]] | np.ndarray,
    *,
    symmetrize: bool = True,
    zero_diagonal: bool = True,
) -> np.ndarray:
    """
    Build the canonical graph Laplacian L = D - W from a family adjacency matrix.

    Rules:
    - adjacency must be square
    - weights must be non-negative
    - diagonal is zeroed by default
    - matrix is symmetrized by default
    """
    w = _ensure_square_matrix(adjacency_matrix, name="adjacency_matrix").astype(float)

    if np.any(w < 0):
        raise ValueError("adjacency_matrix must be non-negative")

    if zero_diagonal:
        np.fill_diagonal(w, 0.0)

    if symmetrize:
        w = 0.5 * (w + w.T)

    degrees = np.sum(w, axis=1)
    d = np.diag(degrees)
    l = d - w
    return l


def build_resistance_matrix(
    resistance_values: Sequence[float] | np.ndarray,
) -> np.ndarray:
    """
    Build diagonal resistance matrix R from per-family resistance values.
    """
    r = _as_float_array(resistance_values, ndim=1, name="resistance_values")
    if np.any(r < 0):
        raise ValueError("resistance_values must be non-negative")
    return np.diag(r)


def build_contradiction_matrix(
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
    *,
    symmetrize: bool = True,
    zero_diagonal: bool = True,
) -> np.ndarray:
    """
    Build contradiction matrix C.

    Rules:
    - must be square
    - must be non-negative
    - diagonal zero by default
    - symmetric by default
    """
    c = _ensure_square_matrix(contradiction_matrix, name="contradiction_matrix").astype(float)

    if np.any(c < 0):
        raise ValueError("contradiction_matrix must be non-negative")

    if zero_diagonal:
        np.fill_diagonal(c, 0.0)

    if symmetrize:
        c = 0.5 * (c + c.T)

    return c


def build_source_vector(
    documents: Sequence[Mapping[str, Any]],
    *,
    family_count: int,
    now_t: Optional[float] = None,
    use_temporal_decay: bool = True,
) -> np.ndarray:
    """
    Aggregate document source vectors into a single family source vector.

    Each document item may contain:
    - "source_vector": length-N vector
    - "weight": base scalar weight (default 1.0)
    - "quality": optional scalar quality/trust (default 1.0)
    - "timestamp": optional numeric time
    - "mass": optional scalar multiplier (default 1.0)

    Temporal decay:
        w_d(t) = weight * quality * mass * exp(-mu * (now_t - timestamp))

    Note:
    - This function only aggregates weighted sources.
    - Decay coefficient mu is applied later in `aggregate_sources_with_params`
      because it belongs to the parameter set.
    """
    if family_count <= 0:
        raise ValueError("family_count must be > 0")

    total = np.zeros(family_count, dtype=float)

    for idx, doc in enumerate(documents):
        if "source_vector" not in doc:
            raise ValueError(f"document[{idx}] missing required field: source_vector")

        vec = _ensure_vector_length(doc["source_vector"], n=family_count, name=f"document[{idx}].source_vector")
        if np.any(vec < 0):
            raise ValueError(f"document[{idx}].source_vector must be non-negative in v1")

        weight = float(doc.get("weight", 1.0))
        quality = float(doc.get("quality", 1.0))
        mass = float(doc.get("mass", 1.0))

        if weight < 0 or quality < 0 or mass < 0:
            raise ValueError(f"document[{idx}] weight/quality/mass must be non-negative")

        scalar = weight * quality * mass
        total += scalar * vec

    return total


def aggregate_sources_with_params(
    documents: Sequence[Mapping[str, Any]],
    *,
    family_count: int,
    params: SemanticFieldParams,
    now_t: Optional[float] = None,
) -> np.ndarray:
    """
    Aggregate weighted source vectors with optional exponential temporal decay.

    Expected per-document fields:
    - source_vector
    - weight (optional)
    - quality (optional)
    - mass (optional)
    - timestamp (optional)
    """
    if family_count <= 0:
        raise ValueError("family_count must be > 0")

    total = np.zeros(family_count, dtype=float)

    for idx, doc in enumerate(documents):
        if "source_vector" not in doc:
            raise ValueError(f"document[{idx}] missing required field: source_vector")

        vec = _ensure_vector_length(doc["source_vector"], n=family_count, name=f"document[{idx}].source_vector")
        if np.any(vec < 0):
            raise ValueError(f"document[{idx}].source_vector must be non-negative in v1")

        weight = float(doc.get("weight", 1.0))
        quality = float(doc.get("quality", 1.0))
        mass = float(doc.get("mass", 1.0))

        if weight < 0 or quality < 0 or mass < 0:
            raise ValueError(f"document[{idx}] weight/quality/mass must be non-negative")

        scalar = weight * quality * mass

        if now_t is not None and params.mu > 0.0 and "timestamp" in doc:
            timestamp = float(doc["timestamp"])
            age = max(0.0, now_t - timestamp)
            scalar *= float(np.exp(-params.mu * age))

        total += scalar * vec

    return total


def compute_pressure_vector(
    field_t: Sequence[float] | np.ndarray,
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
) -> np.ndarray:
    """
    Nonlinear contradiction pressure:
        P(F) = F ⊙ (C F)
    """
    f = _as_float_array(field_t, ndim=1, name="field_t")
    c = _ensure_square_matrix(contradiction_matrix, name="contradiction_matrix")
    if c.shape[0] != f.shape[0]:
        raise ValueError(f"shape mismatch: contradiction_matrix={c.shape}, field_t={f.shape}")

    cf = c @ f
    return f * cf


def compute_energy(
    field_t: Sequence[float] | np.ndarray,
    source_t: Sequence[float] | np.ndarray,
    laplacian: Sequence[Sequence[float]] | np.ndarray,
    resistance_matrix: Sequence[Sequence[float]] | np.ndarray,
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
    params: SemanticFieldParams,
) -> float:
    """
    Canonical linearized energy:
        E(F) = (alpha/2) F^T L F + (beta/2) F^T R F + (gamma/2) F^T C F - delta S^T F
    """
    params.validate()

    f = _as_float_array(field_t, ndim=1, name="field_t")
    s = _ensure_vector_length(source_t, n=f.shape[0], name="source_t")
    l = _ensure_square_matrix(laplacian, name="laplacian")
    r = _ensure_square_matrix(resistance_matrix, name="resistance_matrix")
    c = _ensure_square_matrix(contradiction_matrix, name="contradiction_matrix")

    n = f.shape[0]
    for name, mat in (("laplacian", l), ("resistance_matrix", r), ("contradiction_matrix", c)):
        if mat.shape != (n, n):
            raise ValueError(f"{name} shape mismatch: expected {(n, n)}, got {mat.shape}")

    energy = (
        0.5 * params.alpha * float(f.T @ l @ f)
        + 0.5 * params.beta * float(f.T @ r @ f)
        + 0.5 * params.gamma * float(f.T @ c @ f)
        - params.delta * float(s.T @ f)
    )
    return float(energy)


def compute_observables(
    field_prev: Sequence[float] | np.ndarray,
    field_next: Sequence[float] | np.ndarray,
    source_t: Sequence[float] | np.ndarray,
    laplacian: Sequence[Sequence[float]] | np.ndarray,
    resistance_matrix: Sequence[Sequence[float]] | np.ndarray,
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
    params: SemanticFieldParams,
) -> Dict[str, float]:
    """
    Canonical observables:
    - propagation_velocity
    - contradiction_load
    - diffusion_load
    - resistance_load
    - source_alignment
    - stability_score
    - delta_norm_l2
    - pressure_norm_l1
    """
    params.validate()

    f_prev = _as_float_array(field_prev, ndim=1, name="field_prev")
    f_next = _ensure_vector_length(field_next, n=f_prev.shape[0], name="field_next")
    s = _ensure_vector_length(source_t, n=f_prev.shape[0], name="source_t")
    l = _ensure_square_matrix(laplacian, name="laplacian")
    r = _ensure_square_matrix(resistance_matrix, name="resistance_matrix")
    c = _ensure_square_matrix(contradiction_matrix, name="contradiction_matrix")

    delta = f_next - f_prev
    delta_norm_l2 = float(np.linalg.norm(delta, ord=2))
    propagation_velocity = delta_norm_l2 / float(params.dt)

    contradiction_load = float(f_next.T @ c @ f_next)
    diffusion_load = float(f_next.T @ l @ f_next)
    resistance_load = float(f_next.T @ r @ f_next)
    source_alignment = float(s.T @ f_next)

    pressure = compute_pressure_vector(f_next, c)
    pressure_norm_l1 = float(np.linalg.norm(pressure, ord=1))

    stability_score = 1.0 / (1.0 + delta_norm_l2)

    return {
        "propagation_velocity": propagation_velocity,
        "contradiction_load": contradiction_load,
        "diffusion_load": diffusion_load,
        "resistance_load": resistance_load,
        "source_alignment": source_alignment,
        "stability_score": stability_score,
        "delta_norm_l2": delta_norm_l2,
        "pressure_norm_l1": pressure_norm_l1,
    }


def compute_convergence_metrics(
    field_prev: Sequence[float] | np.ndarray,
    field_next: Sequence[float] | np.ndarray,
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
    params: SemanticFieldParams,
) -> Dict[str, Any]:
    """
    Two convergence notions:
    - numerical: ||F_{t+1} - F_t||_2 < epsilon
    - contradiction: ||P(F_{t+1})||_1 < tau
    """
    params.validate()

    f_prev = _as_float_array(field_prev, ndim=1, name="field_prev")
    f_next = _ensure_vector_length(field_next, n=f_prev.shape[0], name="field_next")
    c = _ensure_square_matrix(contradiction_matrix, name="contradiction_matrix")
    if c.shape != (f_prev.shape[0], f_prev.shape[0]):
        raise ValueError(f"contradiction_matrix shape mismatch: expected {(f_prev.shape[0], f_prev.shape[0])}, got {c.shape}")

    delta_norm_l2 = float(np.linalg.norm(f_next - f_prev, ord=2))
    pressure = compute_pressure_vector(f_next, c)
    pressure_norm_l1 = float(np.linalg.norm(pressure, ord=1))

    return {
        "delta_norm_l2": delta_norm_l2,
        "pressure_norm_l1": pressure_norm_l1,
        "converged_numerical": delta_norm_l2 < params.epsilon,
        "converged_contradiction": pressure_norm_l1 < params.tau,
    }


def step_field(
    field_t: Sequence[float] | np.ndarray,
    source_t: Sequence[float] | np.ndarray,
    laplacian: Sequence[Sequence[float]] | np.ndarray,
    resistance_matrix: Sequence[Sequence[float]] | np.ndarray,
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
    params: SemanticFieldParams,
) -> FieldStepResult:
    """
    Single explicit Euler field step:

        F_{t+1} = F_t + dt * [
            -alpha L F_t
            -beta R F_t
            -gamma (F_t ⊙ (C F_t))
            +delta S_t
        ]

    Production-safe mode clips to [0, 1].
    """
    params.validate()

    f_t = _as_float_array(field_t, ndim=1, name="field_t")
    n = f_t.shape[0]
    s_t = _ensure_vector_length(source_t, n=n, name="source_t")
    l = _ensure_square_matrix(laplacian, name="laplacian")
    r = _ensure_square_matrix(resistance_matrix, name="resistance_matrix")
    c = _ensure_square_matrix(contradiction_matrix, name="contradiction_matrix")

    for name, mat in (("laplacian", l), ("resistance_matrix", r), ("contradiction_matrix", c)):
        if mat.shape != (n, n):
            raise ValueError(f"{name} shape mismatch: expected {(n, n)}, got {mat.shape}")

    diffusion_term = -params.alpha * (l @ f_t)
    resistance_term = -params.beta * (r @ f_t)
    pressure_vector = compute_pressure_vector(f_t, c)
    contradiction_term = -params.gamma * pressure_vector
    source_term = params.delta * s_t

    delta_vector = params.dt * (diffusion_term + resistance_term + contradiction_term + source_term)
    f_next = f_t + delta_vector

    if params.clip_mode:
        f_next = _clip01(f_next)

    energy_prev = compute_energy(f_t, s_t, l, r, c, params)
    energy_next = compute_energy(f_next, s_t, l, r, c, params)
    observables = compute_observables(f_t, f_next, s_t, l, r, c, params)
    convergence = compute_convergence_metrics(f_t, f_next, c, params)

    return FieldStepResult(
        field_prev=f_t.copy(),
        field_next=f_next.copy(),
        source_vector=s_t.copy(),
        pressure_vector=pressure_vector.copy(),
        delta_vector=delta_vector.copy(),
        energy_prev=energy_prev,
        energy_next=energy_next,
        converged_numerical=bool(convergence["converged_numerical"]),
        converged_contradiction=bool(convergence["converged_contradiction"]),
        observables=observables,
    )


def run_until_convergence(
    field_init: Sequence[float] | np.ndarray,
    source_t: Sequence[float] | np.ndarray,
    laplacian: Sequence[Sequence[float]] | np.ndarray,
    resistance_matrix: Sequence[Sequence[float]] | np.ndarray,
    contradiction_matrix: Sequence[Sequence[float]] | np.ndarray,
    params: SemanticFieldParams,
    *,
    max_steps: int = 100,
) -> Tuple[np.ndarray, List[TimelineStep]]:
    """
    Iteratively step the field until both convergence conditions hold,
    or max_steps is reached.
    """
    if max_steps <= 0:
        raise ValueError("max_steps must be > 0")

    f = _as_float_array(field_init, ndim=1, name="field_init").copy()
    timeline: List[TimelineStep] = []

    for step_idx in range(max_steps):
        result = step_field(
            field_t=f,
            source_t=source_t,
            laplacian=laplacian,
            resistance_matrix=resistance_matrix,
            contradiction_matrix=contradiction_matrix,
            params=params,
        )
        timeline.append(TimelineStep(step_index=step_idx, result=result))
        f = result.field_next.copy()

        if result.converged_numerical and result.converged_contradiction:
            break

    return f, timeline


def aggregate_family_to_area(
    family_field: Sequence[float] | np.ndarray,
    family_to_area: Sequence[int] | np.ndarray,
    *,
    area_count: int = 12,
) -> np.ndarray:
    """
    Deterministically aggregate family-level field to area-level field.

    family_to_area is a length-N vector of integer area indices.
    Supports either:
    - 0-based indices in [0, area_count-1]
    - 1-based indices in [1, area_count]
    """
    f = _as_float_array(family_field, ndim=1, name="family_field")
    mapping = np.asarray(family_to_area)

    if mapping.ndim != 1 or mapping.shape[0] != f.shape[0]:
        raise ValueError(
            f"family_to_area length mismatch: expected {f.shape[0]}, got shape={mapping.shape}"
        )

    if area_count <= 0:
        raise ValueError("area_count must be > 0")

    mapping = mapping.astype(int)

    if np.min(mapping) >= 1 and np.max(mapping) <= area_count:
        mapping = mapping - 1
    elif np.min(mapping) >= 0 and np.max(mapping) < area_count:
        pass
    else:
        raise ValueError(
            f"family_to_area must be all in [0,{area_count-1}] or [1,{area_count}], got min={mapping.min()}, max={mapping.max()}"
        )

    area_field = np.zeros(area_count, dtype=float)
    for idx, area_idx in enumerate(mapping):
        area_field[area_idx] += f[idx]
    return area_field


def build_identity_family_mapping(*, family_count: int, families_per_area: int = 24, area_count: int = 12) -> np.ndarray:
    """
    Convenience helper for canonical 288 = 12 * 24 layout.
    Returns 0-based family_to_area mapping.
    """
    if family_count != area_count * families_per_area:
        raise ValueError(
            f"family_count must equal area_count * families_per_area, got {family_count} != {area_count} * {families_per_area}"
        )

    mapping = np.repeat(np.arange(area_count, dtype=int), families_per_area)
    return mapping


__all__ = [
    "SemanticFieldParams",
    "FieldStepResult",
    "TimelineStep",
    "build_family_laplacian",
    "build_resistance_matrix",
    "build_contradiction_matrix",
    "build_source_vector",
    "aggregate_sources_with_params",
    "compute_pressure_vector",
    "compute_energy",
    "compute_observables",
    "compute_convergence_metrics",
    "step_field",
    "run_until_convergence",
    "aggregate_family_to_area",
    "build_identity_family_mapping",
]
