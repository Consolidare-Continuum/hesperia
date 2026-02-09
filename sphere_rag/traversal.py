from dataclasses import dataclass
from typing import List

from .geometry import AREAS, SphereRegion


AREA_RING_ORDER = list(range(AREAS))


@dataclass
class TraversalMetrics:
    loopability: float
    coverage_phi: float
    tension_energy: float
    obstacle_score: float


class TraversalService:
    """
    Executes loop-based semantic traversal over the sphere.

    For the prototype we keep the math intentionally simple but return
    deterministic metrics in [0,1].
    """

    def run_traversal(self, region: SphereRegion) -> TraversalMetrics:
        area_vec = region.area_activation()
        # Simple placeholders for now:
        loopability = max(area_vec)
        coverage_phi = sum(1 for v in area_vec if v > 0) / AREAS
        tension_energy = 1.0 - loopability * coverage_phi
        obstacle_score = 0.0
        return TraversalMetrics(
            loopability=loopability,
            coverage_phi=coverage_phi,
            tension_energy=tension_energy,
            obstacle_score=obstacle_score,
        )


