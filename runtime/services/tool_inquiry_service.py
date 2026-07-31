# HESPERIA — Tool inquiry service facade.
# Copyright © 2026 Societatea cu Răspundere Limitată "CONSOLIDARE CONTINUUM" (IDNO 1026023120076). See LEGAL_NOTICE.md.

from __future__ import annotations

from pathlib import Path
from typing import Any

from sphere.router.tool_inquiry import (
    build_tool_inquiry_packet,
    load_context_packet_json as _load_context_packet_json,
    serialize_json_only,
)


def load_context_packet_json(path: Path) -> dict[str, Any]:
    """Load optional context_rag JSON from file for inquiry augmentation."""
    return _load_context_packet_json(path)


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
