# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
KME — E2E Pipeline runner.
Text corpus → Active Graph → Primitive Metrics → Derived Metrics → Fingerprint → Export.
Target: < 15 ms per document.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hesperia.engine.kme.models import (
        DomainConstants,
        DomainFingerprint,
        DomainGraph,
        MetricReport,
    )


class HesperiaPipelineRunner:
    """Runs the full metric pipeline: hits + relations → ActiveGraph → Primitives → Derived → Fingerprint."""

    def __init__(self, domain_graph: "DomainGraph", domain_constants: "DomainConstants") -> None:
        self.domain_graph = domain_graph
        self.domain_constants = domain_constants

    def run_pipeline(
        self,
        source_id: str,
        hits: list,
        relations: list,
        domain_release: str = "",
    ) -> "DomainFingerprint":
        """Run pipeline for one document; return fingerprint (41 metrics + hash)."""
        from hesperia.engine.kme.active_graph import build_active_graph
        from hesperia.engine.kme.derived.calculator import compute_derived_metrics
        from hesperia.engine.kme.fingerprint.builder import build_fingerprint
        from hesperia.engine.kme.primitives.calculator import compute_primitives

        active_graph = build_active_graph(hits, relations, self.domain_graph)
        primitives = compute_primitives(active_graph, self.domain_constants)
        derived = compute_derived_metrics(primitives)
        fingerprint = build_fingerprint(
            primitives,
            derived,
            domain_release=domain_release,
            source_id=source_id,
        )
        return fingerprint

    def run_document(
        self,
        source_id: str,
        hits: list,
        relations: list,
        domain_release: str = "",
        *,
        concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    ) -> "MetricReport":
        """
        Run pipeline and return full metric report (primitives, derived, fingerprint, TRIZ signals).

        Optional ``concept_to_area_family`` (concept_id → (area, family) strings) feeds
        explainability ``build_activation_trace`` → topology for TRIZ binding and routes.
        """
        from hesperia.engine.explainability import build_activation_trace
        from hesperia.engine.kme.active_graph import build_active_graph
        from hesperia.engine.kme.derived.calculator import compute_derived_metrics
        from hesperia.engine.kme.fingerprint.builder import build_fingerprint
        from hesperia.engine.kme.models import MetricReport
        from hesperia.engine.kme.primitives.calculator import compute_primitives
        from hesperia.engine.triz.kme_bridge import (
            build_topology_from_activation_trace,
            run_triz_for_kme,
            topology_from_graph_coordinates,
        )

        active_graph = build_active_graph(hits, relations, self.domain_graph)
        primitives = compute_primitives(active_graph, self.domain_constants)
        derived = compute_derived_metrics(primitives)
        fingerprint = build_fingerprint(
            primitives,
            derived,
            domain_release=domain_release,
            source_id=source_id,
        )

        topo: dict | None = None
        if concept_to_area_family:
            markers = [(cid, float(n.hit_count)) for cid, n in sorted(active_graph.nodes.items())]
            trace = build_activation_trace(markers, concept_to_area_family)
            topo = build_topology_from_activation_trace(trace) or None
        elif active_graph.concept_coordinates:
            topo = topology_from_graph_coordinates(active_graph)

        # TRIZ: hesperia.engine.triz.triz_pipeline.run_triz_analysis (via run_triz_layer)
        triz_signals = run_triz_for_kme(active_graph, topo)

        return MetricReport(
            source_id=source_id,
            primitive_map=fingerprint.primitive_map,
            derived_map=fingerprint.derived_map,
            fingerprint=fingerprint,
            triz_signals=triz_signals,
        )


def run_pipeline(
    domain_graph: "DomainGraph",
    domain_constants: "DomainConstants",
    source_id: str,
    hits: list,
    relations: list,
    domain_release: str = "",
) -> "DomainFingerprint":
    """One-shot pipeline: domain + document inputs → DomainFingerprint."""
    runner = HesperiaPipelineRunner(domain_graph, domain_constants)
    return runner.run_pipeline(source_id, hits, relations, domain_release)


def run_document(
    domain_graph: "DomainGraph",
    domain_constants: "DomainConstants",
    source_id: str,
    hits: list,
    relations: list,
    domain_release: str = "",
    **kwargs: object,
) -> "MetricReport":
    """One-shot: domain + document inputs → MetricReport (optional ``concept_to_area_family`` for TRIZ topology)."""
    runner = HesperiaPipelineRunner(domain_graph, domain_constants)
    caf = kwargs.pop("concept_to_area_family", None)
    if kwargs:
        raise TypeError(f"run_document: unexpected kwargs {set(kwargs)}")
    return runner.run_document(
        source_id, hits, relations, domain_release, concept_to_area_family=caf
    )


def run_corpus(
    documents: list,
    domain_graph: "DomainGraph",
    domain_constants: "DomainConstants",
    domain_release: str = "",
) -> list["MetricReport"]:
    """Batch: run pipeline for each DocumentInput; return list of MetricReports."""
    from hesperia.engine.kme.models import DocumentInput, MetricReport

    runner = HesperiaPipelineRunner(domain_graph, domain_constants)
    results: list[MetricReport] = []
    for doc in documents:
        if isinstance(doc, DocumentInput):
            r = runner.run_document(
                doc.source_id,
                doc.hits,
                doc.relations,
                domain_release=domain_release,
                concept_to_area_family=doc.concept_to_area_family,
            )
        else:
            raise TypeError("Each document must be DocumentInput")
        results.append(r)
    return results


def metric_report_to_dict(report: "MetricReport") -> dict:
    """Return JSON-serializable dict: sourceId, primitives, derived, fingerprint, triz (optional)."""
    out = {
        "sourceId": report.source_id,
        "primitives": report.primitive_map,
        "derived": report.derived_map,
        "fingerprint": report.fingerprint.to_dict(),
    }
    if report.triz_signals is not None:
        out["triz"] = report.triz_signals.to_dict()
    return out


def export_metric_report_json(path: str | Path, report: "MetricReport") -> None:
    """Write MetricReport to JSON file with deterministic key order and formatting."""
    from core.math.io_deterministic_json import write_json_deterministic

    write_json_deterministic(Path(path), metric_report_to_dict(report))
