```python
# ============================================================
# gamma_guard.py
# HESPERIA — Γ (Gamma) Dynamic Invariant Guard
# Physical guard #2. ΣΓ implemented as final phase inside Γ.
#
# Design intent (per your architecture):
#  - Σ module enforces static structure/topology/schema.
#  - Γ module enforces runtime dynamics + ΣΓ relational coherence.
#  - No third runtime component.
#
# Γ checks (dynamic):
#  - Ring instability (oscillation growth)
#  - Fragmentation escalation
#  - Exploration collapse
#  - Polarization divergence
#  - Drift acceleration
#
# ΣΓ checks (relational):
#  - STRUCTURE_UNDERUTILIZED
#  - GEOMETRIC_INCOHERENCE
#  - AXIS_DIVERGENCE
#  - SEMANTIC_ENGINE_DRIFT
#  - CAPACITY_ASYMMETRY
#
# Notes:
#  - Γ does NOT re-check Σ invariants. If Σ fails, you stop earlier.
#  - Γ assumes ring order / antipodes / borders are canonical (Σ locked).
# ============================================================

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Dict
import math


# -----------------------------
# Failure types
# -----------------------------

class GammaFailMode(str, Enum):
    HALT = "halt"           # stop traversal now
    ROLLBACK = "rollback"   # rollback last step (if supported)
    CORRECT = "correct"     # trigger correction routine (if supported)


class GammaViolation(Exception):
    def __init__(self, code: str, mode: GammaFailMode = GammaFailMode.HALT, detail: str = ""):
        super().__init__(f"{code}{'::' + detail if detail else ''}")
        self.code = code
        self.mode = mode
        self.detail = detail


# -----------------------------
# State snapshot (runtime metrics)
# -----------------------------
@dataclass(frozen=True)
class GammaState:
    # Core structural metrics on current Region R (computed elsewhere)
    frag_index: float        # fragmentation index (K/active)
    coherence: float         # C(R) = L/active
    area_entropy: float      # entropy over Areas
    coverage_phi: float      # fraction of Areas hit in traversal
    loopability: float       # productivity of traversal
    obstacle_score: float    # O_obstacle in [0,1]

    # Area vector / polarization and drift
    tension_energy: float    # tensionEnergy(bipolarAxes(A_vec))
    drift: float             # cumulative drift [0..1] or comparable

    # Capacity / growth shape
    vertical_depth: float    # "vertical" deepening indicator [0..1]
    horizontal_growth: float # "horizontal" expansion indicator [0..1]


# -----------------------------
# Γ Guard
# -----------------------------
class GammaGuard:
    """
    Dynamic + relational guard.
    Call record(state) each step, then evaluate() to decide if traversal continues.
    """

    def __init__(
        self,
        history_size: int = 6,
        # ---- dynamic thresholds (conservative defaults; tune later) ----
        max_obstacle: float = 0.85,
        min_loopability: float = 0.05,
        max_frag_index: float = 0.65,
        min_coherence: float = 0.35,
        max_tension: float = 0.75,
        max_drift: float = 0.75,

        # slopes (growth across window)
        frag_slope_limit: float = 0.18,
        tension_slope_limit: float = 0.20,
        drift_slope_limit: float = 0.22,
        entropy_slope_limit: float = -0.18,     # entropy collapsing (negative slope)

        # ---- ΣΓ relational thresholds ----
        underutil_cov_limit: float = 0.30,
        underutil_coh_min: float = 0.80,
        axis_div_tension_min: float = 0.60,
        axis_div_entropy_max: float = 0.40,
        capacity_asym_depth_min: float = 0.80,
        capacity_asym_cov_max: float = 0.20,
        semantic_drift_hard: float = 0.80,
    ):
        self.history_size = history_size
        self.H: List[GammaState] = []

        # dynamic
        self.max_obstacle = max_obstacle
        self.min_loopability = min_loopability
        self.max_frag_index = max_frag_index
        self.min_coherence = min_coherence
        self.max_tension = max_tension
        self.max_drift = max_drift

        self.frag_slope_limit = frag_slope_limit
        self.tension_slope_limit = tension_slope_limit
        self.drift_slope_limit = drift_slope_limit
        self.entropy_slope_limit = entropy_slope_limit

        # relational ΣΓ
        self.underutil_cov_limit = underutil_cov_limit
        self.underutil_coh_min = underutil_coh_min
        self.axis_div_tension_min = axis_div_tension_min
        self.axis_div_entropy_max = axis_div_entropy_max
        self.capacity_asym_depth_min = capacity_asym_depth_min
        self.capacity_asym_cov_max = capacity_asym_cov_max
        self.semantic_drift_hard = semantic_drift_hard


    # --------------------------------------------------------
    # Public API
    # --------------------------------------------------------

    def reset(self) -> None:
        self.H.clear()


    def record(self, state: GammaState) -> None:
        self.H.append(state)
        if len(self.H) > self.history_size:
            self.H.pop(0)


    def evaluate(self) -> None:
        """
        Run Γ checks then ΣΓ checks.
        Raises GammaViolation on failure.
        """
        if not self.H:
            return

        # Γ: immediate state bounds
        self._gamma_bounds()

        # Γ: trend / persistence if enough history
        if len(self.H) >= 3:
            self._gamma_trends()

        # ΣΓ: structure–dynamics coherence checks (final phase)
        self._sigmagamma_relational()


    # --------------------------------------------------------
    # Γ: Immediate bounds
    # --------------------------------------------------------

    def _gamma_bounds(self) -> None:
        s = self.H[-1]

        if s.obstacle_score >= self.max_obstacle:
            raise GammaViolation("OBSTACLE_HARD_STOP", GammaFailMode.HALT, f"{s.obstacle_score:.3f}")

        if s.loopability < self.min_loopability:
            raise GammaViolation("EXPLORATION_COLLAPSE", GammaFailMode.HALT, f"{s.loopability:.3f}")

        if s.frag_index > self.max_frag_index:
            raise GammaViolation("FRAGMENTATION_TOO_HIGH", GammaFailMode.HALT, f"{s.frag_index:.3f}")

        if s.coherence < self.min_coherence:
            raise GammaViolation("COHERENCE_TOO_LOW", GammaFailMode.HALT, f"{s.coherence:.3f}")

        if s.tension_energy > self.max_tension:
            raise GammaViolation("POLARIZATION_TOO_HIGH", GammaFailMode.HALT, f"{s.tension_energy:.3f}")

        if s.drift > self.max_drift:
            raise GammaViolation("DRIFT_TOO_HIGH", GammaFailMode.HALT, f"{s.drift:.3f}")


    # --------------------------------------------------------
    # Γ: Trend checks (slope / persistence)
    # --------------------------------------------------------

    def _slope(self, attr: str) -> float:
        a0 = getattr(self.H[0], attr)
        a1 = getattr(self.H[-1], attr)
        return a1 - a0


    def _gamma_trends(self) -> None:
        frag_slope = self._slope("frag_index")
        if frag_slope > self.frag_slope_limit:
            raise GammaViolation("FRAGMENTATION_ESCALATION", GammaFailMode.HALT, f"slope={frag_slope:.3f}")

        tension_slope = self._slope("tension_energy")
        if tension_slope > self.tension_slope_limit:
            raise GammaViolation("POLARIZATION_RUNAWAY", GammaFailMode.HALT, f"slope={tension_slope:.3f}")

        drift_slope = self._slope("drift")
        if drift_slope > self.drift_slope_limit:
            raise GammaViolation("DRIFT_ACCELERATION", GammaFailMode.HALT, f"slope={drift_slope:.3f}")

        ent_slope = self._slope("area_entropy")
        # if entropy is collapsing sharply (negative slope), it's a narrowing attractor
        if ent_slope < self.entropy_slope_limit:
            raise GammaViolation("ENTROPY_COLLAPSE", GammaFailMode.HALT, f"slope={ent_slope:.3f}")


    # --------------------------------------------------------
    # ΣΓ: Relational (structure ↔ dynamics coherence)
    # --------------------------------------------------------

    def _sigmagamma_relational(self) -> None:
        """
        This is where we tie runtime behavior to the static lattice Σ froze.
        It's not a "bug flag"; it's a misalignment detector.
        """
        s = self.H[-1]

        # 1) STRUCTURE_UNDERUTILIZED
        # Coherent region, low fragmentation, but ring coverage stays narrow.
        if (s.coverage_phi < self.underutil_cov_limit) and (s.coherence >= self.underutil_coh_min):
            # Optional: require persistence (avoid one-off)
            if self._persistent("coverage_phi", lambda x: x < self.underutil_cov_limit, k=3):
                raise GammaViolation("STRUCTURE_UNDERUTILIZED", GammaFailMode.CORRECT)

        # 2) GEOMETRIC_INCOHERENCE
        # Coherence low + fragmentation high (region lattice not holding together)
        if (s.coherence < 0.40) and (s.frag_index > 0.50):
            raise GammaViolation("GEOMETRIC_INCOHERENCE", GammaFailMode.ROLLBACK)

        # 3) AXIS_DIVERGENCE
        # Tension high but entropy low => polarization with narrow activation
        if (s.tension_energy >= self.axis_div_tension_min) and (s.area_entropy <= self.axis_div_entropy_max):
            if self._persistent("tension_energy", lambda x: x >= self.axis_div_tension_min, k=3):
                raise GammaViolation("AXIS_DIVERGENCE", GammaFailMode.HALT)

        # 4) SEMANTIC_ENGINE_DRIFT
        # Drift crosses hard threshold: semantics are moving too fast relative to lattice.
        if s.drift >= self.semantic_drift_hard:
            raise GammaViolation("SEMANTIC_ENGINE_DRIFT", GammaFailMode.HALT)

        # 5) CAPACITY_ASYMMETRY
        # Vertical deepening without horizontal expansion (scalability constraint)
        if (s.vertical_depth >= self.capacity_asym_depth_min) and (s.coverage_phi <= self.capacity_asym_cov_max):
            if self._persistent("vertical_depth", lambda x: x >= self.capacity_asym_depth_min, k=3):
                raise GammaViolation("CAPACITY_ASYMMETRY", GammaFailMode.CORRECT)


    # --------------------------------------------------------
    # Helpers
    # --------------------------------------------------------

    def _persistent(self, attr: str, pred, k: int = 3) -> bool:
        """
        True if predicate holds for last k states (or as many as available).
        """
        if not self.H:
            return False
        window = self.H[-k:] if len(self.H) >= k else self.H[:]
        for s in window:
            if not pred(getattr(s, attr)):
                return False
        return True


# -----------------------------
# Minimal integration example
# -----------------------------
def gamma_step(gamma: GammaGuard, state: GammaState) -> Optional[GammaViolation]:
    """
    Convenience wrapper: record + evaluate, return violation (or None).
    """
    gamma.record(state)
    try:
        gamma.evaluate()
        return None
    except GammaViolation as e:
        return e
```
