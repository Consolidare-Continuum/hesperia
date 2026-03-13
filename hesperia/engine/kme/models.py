# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
KME — Data models for domain graph, constants, active graph, primitives, derived, fingerprint, profile.
Java-style machine-readable specification.
"""

from __future__ import annotations

from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Domain graph
# ---------------------------------------------------------------------------


@dataclass
class DomainNode:
    """Single node in the domain graph."""

    concept_id: str


@dataclass
class DomainEdge:
    """Directed edge; graph is treated as undirected for metrics."""

    source_concept_id: str
    target_concept_id: str
    relation_type: str


@dataclass
class DomainGraph:
    """
    Reference domain graph.
    Rules: undirected for metrics; self-loops ignored; duplicate edges removed during canonicalization.
    """

    nodes: dict[str, DomainNode]
    edges: list[DomainEdge]


@dataclass
class DomainConstants:
    """Frozen domain constants computed from the reference graph."""

    domain_node_count: int
    domain_degree_p95: float
    domain_distance_p95: float

    def to_dict(self) -> dict[str, int | float]:
        """JSON-serializable dict with snake_case keys."""
        return {
            "domain_node_count": self.domain_node_count,
            "domain_degree_p95": self.domain_degree_p95,
            "domain_distance_p95": self.domain_distance_p95,
        }


# ---------------------------------------------------------------------------
# Active graph inputs and output
# ---------------------------------------------------------------------------


@dataclass
class ConceptHit:
    """Concept occurrence from upstream NLP layer."""

    concept_id: str
    token_index: int


@dataclass
class RelationCandidate:
    """Detected co-occurrence or relation extraction."""

    concept_a: str
    concept_b: str
    relation_type: str


@dataclass
class ActiveNode:
    """Active domain concept with hit count."""

    concept_id: str
    hit_count: int


@dataclass
class ActiveEdge:
    """Active domain relation (canonical source ≤ target)."""

    source_concept_id: str
    target_concept_id: str
    relation_type: str


@dataclass
class ActiveGraph:
    """Text-activated semantic graph A = (V_A, E_A). V_A ⊆ V_R, E_A ⊆ E_R."""

    nodes: dict[str, ActiveNode]
    edges: list[ActiveEdge]

    def to_dict(self) -> dict[str, object]:
        """JSON-serializable dict; nodes by conceptId, edges sorted."""
        nodes_out = {
            cid: {"hitCount": n.hit_count}
            for cid, n in sorted(self.nodes.items())
        }
        edges_out = [
            {
                "source": e.source_concept_id,
                "target": e.target_concept_id,
                "type": e.relation_type,
            }
            for e in sorted(
                self.edges,
                key=lambda x: (x.source_concept_id, x.target_concept_id, x.relation_type),
            )
        ]
        return {"nodes": nodes_out, "edges": edges_out}


# ---------------------------------------------------------------------------
# Primitive metrics output
# ---------------------------------------------------------------------------


@dataclass
class PrimitiveMetrics:
    """Six primitive metrics from active graph + domain constants. All in [0, 1]."""

    LD: float   # LogicalDensity
    COH: float  # Coherence
    NC: float   # NodeCoverage
    PR: float   # PropagationRadius
    PV: float   # PropagationVolume
    CI: float   # ConcentrationIndex

    def to_dict(self) -> dict[str, float]:
        """Canonical serialization order: LD, COH, NC, PR, PV, CI."""
        return {
            "LD": self.LD,
            "COH": self.COH,
            "NC": self.NC,
            "PR": self.PR,
            "PV": self.PV,
            "CI": self.CI,
        }


# ---------------------------------------------------------------------------
# Derived metrics output (35 metrics, all in [0, 1])
# ---------------------------------------------------------------------------


@dataclass
class DerivedMetrics:
    """Thirty-five derived metrics from primitives. Strict bounded regime: clamp01, safeDiv."""

    KDI: float
    CSI: float
    SPI: float
    TDS: float
    SSS: float
    KCI: float
    CCI: float
    SPS: float
    DCI: float
    CSI2: float
    KEF: float
    ASS: float
    CDR: float
    KCR: float
    TCI: float
    PEI: float
    KE: float
    SCS: float
    CRI: float
    KNS: float
    CII: float
    TEP: float
    KSI: float
    CDD: float
    SSR: float
    TER: float
    CPC: float
    KBS: float
    TRI: float
    IDE: float
    KPS: float
    TBI: float
    KDI2: float
    CDI: float
    KVI: float

    def to_dict(self) -> dict[str, float]:
        """Canonical serialization order (frozen)."""
        return {
            "KDI": self.KDI,
            "CSI": self.CSI,
            "SPI": self.SPI,
            "TDS": self.TDS,
            "SSS": self.SSS,
            "KCI": self.KCI,
            "CCI": self.CCI,
            "SPS": self.SPS,
            "DCI": self.DCI,
            "CSI2": self.CSI2,
            "KEF": self.KEF,
            "ASS": self.ASS,
            "CDR": self.CDR,
            "KCR": self.KCR,
            "TCI": self.TCI,
            "PEI": self.PEI,
            "KE": self.KE,
            "SCS": self.SCS,
            "CRI": self.CRI,
            "KNS": self.KNS,
            "CII": self.CII,
            "TEP": self.TEP,
            "KSI": self.KSI,
            "CDD": self.CDD,
            "SSR": self.SSR,
            "TER": self.TER,
            "CPC": self.CPC,
            "KBS": self.KBS,
            "TRI": self.TRI,
            "IDE": self.IDE,
            "KPS": self.KPS,
            "TBI": self.TBI,
            "KDI2": self.KDI2,
            "CDI": self.CDI,
            "KVI": self.KVI,
        }


# ---------------------------------------------------------------------------
# Domain fingerprint output
# ---------------------------------------------------------------------------


@dataclass
class DomainFingerprint:
    """Deterministic fingerprint: ordered vector + metadata + vectorHash. Same metrics -> same bytes."""

    fingerprint_version: str
    domain_release: str
    source_id: str
    metric_names: list[str]
    metric_values: list[float]
    primitive_map: dict[str, float]
    derived_map: dict[str, float]
    vector_hash: str

    def to_dict(self) -> dict[str, object]:
        """Stable JSON field order."""
        return {
            "fingerprintVersion": self.fingerprint_version,
            "domainRelease": self.domain_release,
            "sourceId": self.source_id,
            "metricNames": self.metric_names,
            "metricValues": self.metric_values,
            "primitiveMap": self.primitive_map,
            "derivedMap": self.derived_map,
            "vectorHash": self.vector_hash,
        }


# ---------------------------------------------------------------------------
# E2E pipeline I/O
# ---------------------------------------------------------------------------


@dataclass
class DocumentInput:
    """Single-document input for the pipeline: source id, concept hits, relation candidates."""

    source_id: str
    hits: list[ConceptHit]
    relations: list[RelationCandidate]


@dataclass
class MetricReport:
    """Full pipeline output: 41 metrics, fingerprint vector, hash, and maps for JSON report."""

    source_id: str
    primitive_map: dict[str, float]
    derived_map: dict[str, float]
    fingerprint: DomainFingerprint


# ---------------------------------------------------------------------------
# Domain Profile — corpus-level structural signature
# ---------------------------------------------------------------------------


@dataclass
class DomainProfile:
    """Aggregated structural signature of a corpus: mean, std, median, p90 per dimension (41), profileHash."""

    domain_id: str
    document_count: int
    mean_vector: list[float]
    std_vector: list[float]
    median_vector: list[float]
    p90_vector: list[float]
    profile_hash: str

    def to_dict(self) -> dict[str, object]:
        """JSON-serializable; keys match spec."""
        return {
            "domainId": self.domain_id,
            "documentCount": self.document_count,
            "meanVector": self.mean_vector,
            "stdVector": self.std_vector,
            "medianVector": self.median_vector,
            "p90Vector": self.p90_vector,
            "profileHash": self.profile_hash,
        }
