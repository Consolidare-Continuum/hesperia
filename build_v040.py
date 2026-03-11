#!/usr/bin/env python3
"""Historical build entrypoint retained for compatibility.

Historical reference (pre-refactor): v0.4.0 build flow was tied to legacy modules.
Active execution stack is runtime/core/lexicon; this wrapper is intentionally non-operational.
"""

from __future__ import annotations

import sys


if __name__ == "__main__":
    sys.stderr.write(
        "build_v040.py is a historical pre-refactor entrypoint. "
        "Use active runtime/lexicon tools instead.\n"
    )
    raise SystemExit(2)
