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
    ) -> "MetricReport":
        """Run pipeline and return full metric report (primitives, derived, fingerprint)."""
        from hesperia.engine.kme.models import MetricReport

        fp = self.run_pipeline(source_id, hits, relations, domain_release)
        return MetricReport(
            source_id=source_id,
            primitive_map=fp.primitive_map,
            derived_map=fp.derived_map,
            fingerprint=fp,
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
) -> "MetricReport":
    """One-shot: domain + document inputs → MetricReport."""
    runner = HesperiaPipelineRunner(domain_graph, domain_constants)
    return runner.run_document(source_id, hits, relations, domain_release)


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
            )
        else:
            raise TypeError("Each document must be DocumentInput")
        results.append(r)
    return results


def metric_report_to_dict(report: "MetricReport") -> dict:
    """Return JSON-serializable dict: sourceId, primitives, derived, fingerprint (stable for deterministic export)."""
    return {
        "sourceId": report.source_id,
        "primitives": report.primitive_map,
        "derived": report.derived_map,
        "fingerprint": report.fingerprint.to_dict(),
    }


def export_metric_report_json(path: str | Path, report: "MetricReport") -> None:
    """Write MetricReport to JSON file with deterministic key order and formatting."""
    from core.math.io_deterministic_json import write_json_deterministic

    write_json_deterministic(Path(path), metric_report_to_dict(report))
