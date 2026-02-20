from __future__ import annotations

from dataclasses import asdict

from sphere_rag.geometry import AREAS, FAMILIES_PER_AREA, TOTAL_FAMILIES

from scripts.gamma_guard import GammaState, StopReason, gamma_finish, gamma_tick
from scripts.sigma_guard import SigmaGuard
from scripts.theta_gate import theta_gate


def default_family_to_area() -> list[int]:
    return [idx // FAMILIES_PER_AREA for idx in range(TOTAL_FAMILIES)]


def default_area_ring_order() -> list[int]:
    return list(range(AREAS))


def run_sigma_preflight(*, strict: bool = True, tau: list[float] | None = None) -> dict:
    guard = SigmaGuard(strict=strict)
    status = guard.validate_all(
        family_to_area=default_family_to_area(),
        area_ring_order=default_area_ring_order(),
        tau=tau,
    )
    return asdict(status)


__all__ = [
    "GammaState",
    "SigmaGuard",
    "StopReason",
    "default_area_ring_order",
    "default_family_to_area",
    "gamma_finish",
    "gamma_tick",
    "run_sigma_preflight",
    "theta_gate",
]
