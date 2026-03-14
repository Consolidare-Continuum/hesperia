# HESPERIA — Shipping CLI. Single entry point; service façades only.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Shipping entry point. Exposes analyze, compare, batch-analyze. No internal API."""

from runtime.shipping.cli_main import main

__all__ = ["main"]
