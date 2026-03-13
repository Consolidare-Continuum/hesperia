# HESPERIA — Legacy re-export. Canonical: hesperia.engine.kme.primitives
# Copyright © 2026 igareosh.com. All rights reserved.

"""Re-export KME primitives. Prefer: from hesperia.engine.kme.primitives import ..."""

from hesperia.engine.kme.primitives.calculator import (
    build_adjacency,
    clamp01,
    compute_ci,
    compute_coh,
    compute_ld,
    compute_nc,
    compute_pr,
    compute_primitives,
    compute_pv,
    count_connected_triplets,
    count_triangles,
    largest_component_size,
    multi_source_distances,
    positive_or_one,
    select_anchor_ids,
    sorted_node_ids,
)

__all__ = [
    "build_adjacency",
    "clamp01",
    "compute_ci",
    "compute_coh",
    "compute_ld",
    "compute_nc",
    "compute_pr",
    "compute_primitives",
    "compute_pv",
    "count_connected_triplets",
    "count_triangles",
    "largest_component_size",
    "multi_source_distances",
    "positive_or_one",
    "select_anchor_ids",
    "sorted_node_ids",
]
