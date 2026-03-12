# Structural diagnostics detectors: anomaly, monotony, instability.
from sphere.diagnostics.anomaly_detector import detect_structural_anomalies
from sphere.diagnostics.monotony_detector import (
    detect_structural_monotony,
    compute_dominant_area_share,
)
from sphere.diagnostics.instability_detector import detect_rhetorical_instability
from sphere.diagnostics.diagnostics_runtime import run_diagnostics

__all__ = [
    "detect_structural_anomalies",
    "detect_structural_monotony",
    "compute_dominant_area_share",
    "detect_rhetorical_instability",
    "run_diagnostics",
]
