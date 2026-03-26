# HESPERIA — KME canonical execution flow surface
# Copyright © 2026 igareosh.com. All rights reserved.

"""Canonical import surface for KME execution flow APIs."""

from __future__ import annotations

# Compatibility re-export from legacy module path.
from hesperia.engine.kme.pipeline import (  # noqa: F401
    HesperiaPipelineRunner,
    export_metric_report_json,
    metric_report_to_dict,
    run_corpus,
    run_document,
    run_pipeline,
)

__all__ = [
    "HesperiaPipelineRunner",
    "export_metric_report_json",
    "metric_report_to_dict",
    "run_corpus",
    "run_document",
    "run_pipeline",
]
