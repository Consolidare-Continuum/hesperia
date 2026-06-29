# HESPERIA — Tool inquiry service facade.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

from pathlib import Path
from typing import Any

from sphere.router.tool_inquiry import build_tool_inquiry_packet, serialize_json_only


def run_tool_inquiry(
    text: str,
    assets_root: Path | None = None,
    *,
    context_packet: dict[str, Any] | None = None,
    thinking_map_outcome: dict[str, Any] | None = None,
) -> str:
    """Return JSON-only string for CLI/MCP surfaces."""
    packet = build_tool_inquiry_packet(
        text,
        assets_root,
        context_packet=context_packet,
        thinking_map_outcome=thinking_map_outcome,
    )
    return serialize_json_only(packet)
