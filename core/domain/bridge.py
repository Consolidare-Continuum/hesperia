# HESPERIA — Legacy re-export. Canonical: hesperia.engine.kme.bridge
# Copyright © 2026 igareosh.com. All rights reserved.

"""Re-export KME bridge. Prefer: from hesperia.engine.kme.bridge import ..."""

from hesperia.engine.kme.bridge import (
    pipeline_matched_to_hits_relations,
    synthetic_domain_graph_for_topology,
)

__all__ = [
    "pipeline_matched_to_hits_relations",
    "synthetic_domain_graph_for_topology",
]
