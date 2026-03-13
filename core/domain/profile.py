# HESPERIA — Legacy re-export. Canonical: hesperia.engine.kme.profiling
# Copyright © 2026 igareosh.com. All rights reserved.

"""Re-export KME profiling. Prefer: from hesperia.engine.kme.profiling import ..."""

from hesperia.engine.kme.profiling.profiler import (
    build_profile,
    classify_document,
    domain_distance,
)

__all__ = [
    "build_profile",
    "classify_document",
    "domain_distance",
]
