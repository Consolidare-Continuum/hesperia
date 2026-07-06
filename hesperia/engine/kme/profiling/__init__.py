# HESPERIA — KME profiling subpackage.
# Copyright © 2026 igareosh.com. All rights reserved.

"""KME — Domain profile layer (corpus-level aggregation)."""

from core.domain.profile import (
    build_profile,
    classify_document,
    domain_distance,
)

__all__ = [
    "build_profile",
    "classify_document",
    "domain_distance",
]
