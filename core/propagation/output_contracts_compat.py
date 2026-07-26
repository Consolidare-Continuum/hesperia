# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
DEPRECATED — Do not use in new code. Use core.propagation.output_contracts instead.
Re-exports for backward compatibility only; RAD: no version in filename.
"""
from __future__ import annotations

from core.propagation.output_contracts import (
    make_error_result,
    to_minimal_operational_result,
)

__all__ = ["make_error_result", "to_minimal_operational_result"]
