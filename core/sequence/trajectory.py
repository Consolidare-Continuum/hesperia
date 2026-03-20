"""Trajectory features over ordered segment outputs (e.g. dominant microcell per segment)."""

from __future__ import annotations

from typing import Any


def trajectory_over_segments(segment_summaries: list[dict[str, Any]]) -> dict[str, Any]:
    """
    ``segment_summaries``: one dict per segment with optional ``dominant_slot`` (int) and ``mass`` (float).
    Returns JSON-serializable trajectory stats.
    """
    slots: list[int | None] = []
    masses: list[float] = []
    for s in segment_summaries:
        ds = s.get("dominant_slot")
        slots.append(int(ds) if ds is not None else None)
        try:
            masses.append(float(s.get("mass") or 0.0))
        except (TypeError, ValueError):
            masses.append(0.0)
    moves = 0
    prev = None
    for s in slots:
        if s is None:
            continue
        if prev is not None and s != prev:
            moves += 1
        prev = s
    return {
        "segment_count": len(segment_summaries),
        "dominant_slots": slots,
        "transition_count": moves,
        "total_mass": round(sum(masses), 6),
    }
