# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""Service façades. Public runtime talks to sealed core only through these narrow interfaces."""

from core.services.analysis_service import run_structural_analysis, run_structural_analysis_batch
from core.services.report_service import build_public_report, export_public_artifacts

__all__ = [
    "run_structural_analysis",
    "run_structural_analysis_batch",
    "build_public_report",
    "export_public_artifacts",
]
