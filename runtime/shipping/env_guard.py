# HESPERIA — Lock supported environment variables. Reject or warn on unknown HESPERIA_*.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Ensure runtime behavior cannot be altered by unknown env vars."""

from __future__ import annotations

import os

ALLOWED_HESPERIA_ENV = frozenset({
    "HESPERIA_LICENSE_SKIP",
    "HESPERIA_LICENSE_REQUIRED",
    "HESPERIA_LICENSE_TOKEN",
    "HESPERIA_LICENSE_EXPIRY",
    "HESPERIA_LICENSE_FILE",
    "HESPERIA_RATE_LIMIT",
    "HESPERIA_MACHINE_BINDING",
    "HESPERIA_MACHINE_ID",
    "HESPERIA_ASSETS_ROOT",
    "HESPERIA_API_HOST",
    "HESPERIA_API_PORT",
    "HESPERIA_RUNTIME_MODE",
    "HESPERIA_SCHEMA_SHA256",
})


def check_hesperia_env(*, strict: bool = False) -> None:
    """
    Check for unknown HESPERIA_* variables. If strict=True, raise ValueError.
    Otherwise log to stderr and continue.
    """
    unknown = [k for k in os.environ if k.startswith("HESPERIA_") and k not in ALLOWED_HESPERIA_ENV]
    if not unknown:
        return
    msg = f"Unknown HESPERIA_* variable(s): {', '.join(sorted(unknown))}. See RUNTIME_ENV_VARS_v1.md."
    if strict:
        raise ValueError(msg)
    import sys
    print(msg, file=sys.stderr)
