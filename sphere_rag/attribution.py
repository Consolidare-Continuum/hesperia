from dataclasses import dataclass
from typing import List

from .geometry import AREAS, TOTAL_FAMILIES


@dataclass
class SentenceAttribution:
    F_sentence: List[float]
    A_sentence: List[float]
    dominant_family: int
    dominant_area: int


@dataclass
class StatementAttribution:
    F_statement: List[float]
    A_statement: List[float]
    family: int
    area: int
    inward_vector: List[float]
    outward_vector: List[float]


class AttributionService:
    """
    Thin prototype for the semantic attribution engine.

    In production this would implement the 5-stage word pipeline and
    sentence/statement aggregation as described in `12_SPEC__Semantic_Engine_v0_4.txt`.
    """

    def attribute_statement(self, text: str) -> StatementAttribution:
        # Placeholder: classify everything to Area 0 / Family 0.
        F = [0.0] * TOTAL_FAMILIES
        A = [0.0] * AREAS
        F[0] = 1.0
        A[0] = 1.0
        inward = [0.0] * AREAS
        outward = [0.0] * AREAS
        inward[0] = 1.0
        return StatementAttribution(
            F_statement=F,
            A_statement=A,
            family=0,
            area=0,
            inward_vector=inward,
            outward_vector=outward,
        )
