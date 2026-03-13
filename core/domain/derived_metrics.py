# HESPERIA — Legacy re-export. Canonical: hesperia.engine.kme.derived
# Copyright © 2026 igareosh.com. All rights reserved.

"""Re-export KME derived. Prefer: from hesperia.engine.kme.derived import ..."""

from hesperia.engine.kme.derived.calculator import (
    clamp01,
    compute,
    compute_derived_metrics,
    full_fingerprint,
    safe_div,
    to_derived_vector,
    to_full_fingerprint,
    vector,
    zero_derived_metrics,
)

__all__ = [
    "clamp01",
    "compute",
    "compute_derived_metrics",
    "full_fingerprint",
    "to_derived_vector",
    "to_full_fingerprint",
    "vector",
    "zero_derived_metrics",
    "safe_div",
]
