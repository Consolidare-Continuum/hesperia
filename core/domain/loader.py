# HESPERIA — Legacy re-export. Canonical: hesperia.engine.kme.loader
# Copyright © 2026 igareosh.com. All rights reserved.

"""Re-export KME loader. Prefer: from hesperia.engine.kme.loader import ..."""

from hesperia.engine.kme.loader import (
    load_domain_graph_from_json,
    load_frozen_constants,
)

__all__ = [
    "load_domain_graph_from_json",
    "load_frozen_constants",
]
