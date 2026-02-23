"""Minimal landing explain helper for Dict A/B0/B1 resolution."""

from __future__ import annotations

from typing import Any


def explain_landing(
    token: str,
    dict_a: dict[str, dict[str, Any]],
    b0: dict[str, int],
    b1_optional: dict[str, int] | None,
    token_to_side_id: dict[str, int] | None = None,
    b0_anchor_map: dict[str, str] | None = None,
) -> dict[str, Any]:
    t = token.strip().lower()
    if t in dict_a:
        e = dict_a[t]
        return {
            "landing_source": "A",
            "familyGlobal": int(e.get("familyGlobal", -1)),
            "anchor_key": t,
        }

    if b1_optional and token_to_side_id and t in token_to_side_id:
        side_id = int(token_to_side_id[t])
        family = b1_optional.get(str(side_id))
        if family is not None:
            return {
                "landing_source": "B1",
                "familyGlobal": int(family),
                "side_id": side_id,
            }

    if t in b0:
        out = {
            "landing_source": "B0",
            "familyGlobal": int(b0[t]),
        }
        if b0_anchor_map and t in b0_anchor_map:
            out["anchor_key"] = b0_anchor_map[t]
        return out

    return {"landing_source": "NONE", "familyGlobal": None}
