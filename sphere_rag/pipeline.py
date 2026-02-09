from dataclasses import dataclass
from typing import Any, Dict, Protocol

from .attribution import AttributionService
from .geometry import GeometryService
from .governance import GovernanceDecision, GovernanceService
from .traversal import TraversalMetrics, TraversalService


class Retriever(Protocol):
    """
    Abstract retrieval interface.

    Implement this against any vector DB or search backend.
    """

    def retrieve(self, query: str, *, top_k: int = 8) -> Dict[str, Any]:
        ...


@dataclass
class SphereRAGResult:
    decision: GovernanceDecision
    traversal: TraversalMetrics
    raw_retrieval: Dict[str, Any]


class SphereRAGPipeline:
    """
    End-to-end RAG + governance pipeline built on Sphere.

    Steps:
    - Attribute user query
    - Retrieve candidate evidence using an arbitrary backend
    - Place into geometry, run traversal (prototype: placement uses only the query attribution)
    - Emit a clear decision for a downstream generator (LLM adapter).
    """

    def __init__(
        self,
        retriever: Retriever,
        attribution: AttributionService | None = None,
        geometry: GeometryService | None = None,
        traversal: TraversalService | None = None,
        governance: GovernanceService | None = None,
    ) -> None:
        self.retriever = retriever
        self.attribution = attribution or AttributionService()
        self.geometry = geometry or GeometryService()
        self.traversal = traversal or TraversalService()
        self.governance = governance or GovernanceService()

    def run(self, query: str, *, top_k: int = 8) -> SphereRAGResult:
        # 1) Attribute query to StatementAttribution
        stmt = self.attribution.attribute_statement(query)

        # 2) Retrieve external knowledge (prototype: returned but not yet placed into the region)
        raw_retrieval = self.retriever.retrieve(query, top_k=top_k)

        # 3) Map statement into geometry and build region
        seed_side = self.geometry.locate_statement(stmt.area, stmt.family)
        region = self.geometry.build_region(seed_side)

        # 4) Run semantic traversal
        traversal = self.traversal.run_traversal(region)

        # 5) Governance decision
        decision = self.governance.decide_for_query(traversal)

        return SphereRAGResult(
            decision=decision,
            traversal=traversal,
            raw_retrieval=raw_retrieval,
        )

