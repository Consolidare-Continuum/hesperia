# HESPERIA — Runtime service façades.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Runtime service façades. Structural analysis entry point; calls sphere + core."""

from runtime.services.analysis_service import run_structural_analysis, run_structural_analysis_batch

__all__ = [
    "run_structural_analysis",
    "run_structural_analysis_batch",
]
