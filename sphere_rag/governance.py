from dataclasses import dataclass

from .traversal import TraversalMetrics


@dataclass
class GovernanceDecision:
    allow: bool
    require_correction: bool
    forbid: bool
    score: float
    reason: str


class GovernanceService:
    """
    Takes traversal metrics and emits a clear, LLM-readable decision.

    This is the governance/policy layer that stands between retrieved
    evidence and any downstream text generation (LLM adapter).
    """

    def decide_for_query(self, metrics: TraversalMetrics) -> GovernanceDecision:
        if metrics.obstacle_score > 0.7:
            return GovernanceDecision(
                allow=False,
                require_correction=False,
                forbid=True,
                score=0.0,
                reason="High obstacle score in semantic region.",
            )
        if metrics.tension_energy > 0.7:
            return GovernanceDecision(
                allow=False,
                require_correction=True,
                forbid=False,
                score=0.3,
                reason="High polarization / tension; require clarification or correction.",
            )
        return GovernanceDecision(
            allow=True,
            require_correction=False,
            forbid=False,
            score=0.9,
            reason="Stable region with acceptable loopability and coverage.",
        )

