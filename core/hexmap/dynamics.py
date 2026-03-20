"""Deterministic hex-state dynamics primitives."""

from __future__ import annotations


def apply_decay(hex_state: dict[str, float], decay: float = 0.05) -> dict[str, float]:
    return {k: max(0.0, v * (1.0 - decay)) for k, v in hex_state.items()}


def concentration_index(hex_state: dict[str, float]) -> float:
    total = sum(hex_state.values())
    if total <= 0:
        return 0.0
    peak = max(hex_state.values())
    return peak / total


def dispersion_index(hex_state: dict[str, float]) -> float:
    total = sum(hex_state.values())
    if total <= 0:
        return 0.0
    active = sum(1 for value in hex_state.values() if value > 0)
    return active / max(1, len(hex_state))


def smooth_toward_mean(hex_state: dict[str, float], alpha: float = 0.12) -> dict[str, float]:
    """
    Deterministic denoising: blend each mass with global mean (Ethan PO-17).

    ``alpha`` in [0,1]; 0 returns input unchanged.
    """
    if alpha <= 0 or not hex_state:
        return dict(hex_state)
    total = sum(hex_state.values())
    n = max(1, len(hex_state))
    mean = total / n
    return {k: (1.0 - alpha) * float(v) + alpha * mean for k, v in hex_state.items()}

