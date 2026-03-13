# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA Knowledge Metrics Engine (KME).
Deterministic computation of structural knowledge metrics and fingerprints for documents and domains.
Module path: hesperia.engine.kme
"""

from hesperia.engine.kme.models import (
    ActiveEdge,
    ActiveGraph,
    ActiveNode,
    ConceptHit,
    DerivedMetrics,
    DocumentInput,
    DomainConstants,
    DomainEdge,
    DomainFingerprint,
    DomainGraph,
    DomainNode,
    DomainProfile,
    MetricReport,
    PrimitiveMetrics,
    RelationCandidate,
)
from hesperia.engine.kme.active_graph import build_active_graph
from hesperia.engine.kme.derived.calculator import (
    compute,
    compute_derived_metrics,
    full_fingerprint,
    to_derived_vector,
    to_full_fingerprint,
    vector,
    zero_derived_metrics,
)
from hesperia.engine.kme.extractor import extract_constants
from hesperia.engine.kme.fingerprint.builder import (
    MARKETABLE_DERIVED_ORDER,
    build_fingerprint,
    cosine_similarity,
    euclidean_distance,
    fingerprint_cosine,
    fingerprint_euclidean,
    fingerprint_manhattan,
    marketable_derived_from_map,
    same_fingerprint,
    manhattan_distance,
)
from hesperia.engine.kme.loader import load_domain_graph_from_json, load_frozen_constants
from hesperia.engine.kme.pipeline import (
    HesperiaPipelineRunner,
    export_metric_report_json,
    metric_report_to_dict,
    run_corpus,
    run_document,
    run_pipeline,
)
from hesperia.engine.kme.primitives.calculator import compute_primitives
from hesperia.engine.kme.profiling.profiler import build_profile, classify_document, domain_distance

__all__ = [
    "ActiveEdge",
    "ActiveGraph",
    "ActiveNode",
    "ConceptHit",
    "DerivedMetrics",
    "DocumentInput",
    "DomainConstants",
    "DomainEdge",
    "DomainFingerprint",
    "DomainGraph",
    "DomainNode",
    "DomainProfile",
    "MetricReport",
    "PrimitiveMetrics",
    "RelationCandidate",
    "build_active_graph",
    "build_fingerprint",
    "build_profile",
    "classify_document",
    "compute",
    "compute_derived_metrics",
    "compute_primitives",
    "cosine_similarity",
    "domain_distance",
    "euclidean_distance",
    "export_metric_report_json",
    "extract_constants",
    "fingerprint_cosine",
    "fingerprint_euclidean",
    "fingerprint_manhattan",
    "full_fingerprint",
    "load_domain_graph_from_json",
    "load_frozen_constants",
    "MARKETABLE_DERIVED_ORDER",
    "manhattan_distance",
    "marketable_derived_from_map",
    "metric_report_to_dict",
    "run_corpus",
    "run_document",
    "run_pipeline",
    "same_fingerprint",
    "to_derived_vector",
    "to_full_fingerprint",
    "vector",
    "zero_derived_metrics",
    "HesperiaPipelineRunner",
]
