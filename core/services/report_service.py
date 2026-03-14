# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Report service façade. Build and export public reports only; all output passes through projection.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from core.projection import apply_public_projection


def build_public_report(
    analysis_result: dict[str, Any],
    report_profile_id: str | None = None,
    public_metric_profile_id: str = "commercial",
) -> dict[str, Any]:
    """
    Build a public report from analysis result. Result must already be projected or will be projected here.
    Returns report dict with only public metric profile and public vocabulary.
    """
    out = apply_public_projection(analysis_result)
    out["report_profile_id"] = report_profile_id or ""
    out["public_metric_profile_id"] = public_metric_profile_id
    return out


def export_public_artifacts(
    report: dict[str, Any],
    output_path: Path | str,
) -> None:
    """
    Write report to output_path. All content is public-safe (projected).
    For audit manifest, use runtime.public_reports.public_manifest_writer.write_public_audit_manifest.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    import json
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
