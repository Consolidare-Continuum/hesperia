# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.

"""Noise reduction and threshold constants for TRIZ layer."""

from __future__ import annotations

import math

# Task 6.2 — threshold filters
MIN_CONTRADICTION_SCORE = 0.15
MIN_CLUSTER_SIZE = 3
MIN_PROPAGATION_STEPS = 2


def exponential_smoothing(series: list[float], alpha: float = 0.3) -> list[float]:
    """EWMA; alpha in (0,1]. First value seeds the smooth."""
    if not series:
        return []
    a = min(1.0, max(1e-9, alpha))
    out = [series[0]]
    for x in series[1:]:
        out.append(a * x + (1.0 - a) * out[-1])
    return out


def moving_average(series: list[float], window: int = 3) -> list[float]:
    """Simple causal moving average; window >= 1."""
    if not series or window < 1:
        return list(series)
    w = min(window, len(series))
    out: list[float] = []
    for i in range(len(series)):
        lo = max(0, i - w + 1)
        chunk = series[lo : i + 1]
        out.append(sum(chunk) / float(len(chunk)))
    return out


def z_score_normalize(series: list[float], eps: float = 1e-9) -> list[float]:
    """Per-sequence z-score; deterministic; empty → []."""
    if not series:
        return []
    mu = sum(series) / float(len(series))
    var = sum((x - mu) ** 2 for x in series) / float(len(series))
    sd = math.sqrt(var + eps)
    return [(x - mu) / sd for x in series]
