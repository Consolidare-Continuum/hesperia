# HESPERIA — Legacy re-export. Canonical: hesperia.engine.kme.pipeline
# Copyright © 2026 igareosh.com. All rights reserved.

"""Re-export KME pipeline. Prefer: from hesperia.engine.kme.pipeline import ..."""

from hesperia.engine.kme.pipeline import (
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
