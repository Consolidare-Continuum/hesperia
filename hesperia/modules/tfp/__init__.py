"""TFP module package — v1 public surface.

Stable entrypoints: see ``ENTRYPOINTS.md`` in this directory.
"""

from __future__ import annotations

from hesperia.modules.tfp.module import create
from hesperia.modules.tfp.v1 import TFPModule, create as create_v1

__all__ = ["TFPModule", "create", "create_v1"]
