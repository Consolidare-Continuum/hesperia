# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Task 2 — LLM collapse of noisy surface strings to stable lexical forms."""

from __future__ import annotations

from typing import Any

from .openai_json import chat_json


SYSTEM = """You normalize clinical / psychodynamic surface text to compact lexical phrases.
Rules: aggressive removal of fillers; preserve psychological meaning; lower-case output;
no diagnosis labels; output strict JSON only."""

USER_TEMPLATE = """Given items (pattern_type + text), return JSON object with key "items" array.
Each element: {{"source_text": str, "normalized": str, "variants": [str, ...]}}
Merge paraphrases to one normalized form; variants lists surface alternates (max 8).
Input:
{payload}
"""


def normalize_batch(rows: list[dict[str, Any]], *, batch_size: int = 24) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for i in range(0, len(rows), batch_size):
        chunk = rows[i : i + batch_size]
        payload = [
            {"pattern_type": r.get("pattern_type"), "text": r.get("text"), "freq": r.get("freq")}
            for r in chunk
        ]
        import json as _json

        raw = chat_json(system=SYSTEM, user=USER_TEMPLATE.format(payload=_json.dumps(payload, ensure_ascii=False)))
        items = raw.get("items") if isinstance(raw, dict) else None
        if not isinstance(items, list):
            raise ValueError("normalize_batch: expected {items: [...]}")
        by_src = {str(x.get("source_text", "")): x for x in items if isinstance(x, dict)}
        for r in chunk:
            st = str(r.get("text", ""))
            hit = by_src.get(st) or {}
            norm = str(hit.get("normalized") or st).strip()
            vars_ = hit.get("variants") if isinstance(hit.get("variants"), list) else []
            vars_clean = [str(v).strip() for v in vars_ if str(v).strip()][:12]
            rec = dict(r)
            rec["normalized"] = norm
            rec["variants"] = vars_clean
            out.append(rec)
    return out
