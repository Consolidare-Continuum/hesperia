from __future__ import annotations

from dataclasses import dataclass, field

EXPECTED_AREAS = 12
EXPECTED_FAMILIES_PER_AREA = 24
EXPECTED_TOTAL_FAMILIES = EXPECTED_AREAS * EXPECTED_FAMILIES_PER_AREA


@dataclass(frozen=True, slots=True)
class SigmaStatus:
    ok: bool
    strict: bool
    checks: dict[str, bool]
    details: list[str] = field(default_factory=list)


class SigmaGuard:
    def __init__(self, strict: bool = True) -> None:
        self.strict = strict

    def validate_all(
        self,
        *,
        family_to_area: list[int] | None = None,
        area_ring_order: list[int] | None = None,
        tau: list[float] | None = None,
    ) -> SigmaStatus:
        checks: dict[str, bool] = {}
        details: list[str] = []

        if family_to_area is not None:
            c_len = len(family_to_area) == EXPECTED_TOTAL_FAMILIES
            c_range = all(0 <= a < EXPECTED_AREAS for a in family_to_area)
            c_partition = all(
                family_to_area[idx] == (idx // EXPECTED_FAMILIES_PER_AREA) for idx in range(len(family_to_area))
            )
            checks["family_to_area_len_288"] = c_len
            checks["family_to_area_area_range"] = c_range
            checks["family_to_area_partition"] = c_partition
            if not c_len:
                details.append(f"family_to_area length must be 288, got {len(family_to_area)}")
            if not c_range:
                details.append("family_to_area contains invalid area ids")
            if not c_partition:
                details.append("family_to_area does not match canonical 24-families-per-area layout")

        if area_ring_order is not None:
            c_ring = len(area_ring_order) == EXPECTED_AREAS and sorted(area_ring_order) == list(range(EXPECTED_AREAS))
            checks["area_ring_order_canonical"] = c_ring
            if not c_ring:
                details.append("area_ring_order must be a permutation of 0..11")

        if tau is not None:
            c_tau = all((v is None) or (0.0 <= float(v) <= 1.0) for v in tau)
            checks["tau_in_range_0_1"] = c_tau
            if not c_tau:
                details.append("tau values must be in [0, 1]")

        ok = all(checks.values()) if checks else True
        if self.strict and not ok:
            raise ValueError("SigmaGuard preflight failed: " + "; ".join(details or ["unknown error"]))
        return SigmaStatus(ok=ok, strict=self.strict, checks=checks, details=details)
