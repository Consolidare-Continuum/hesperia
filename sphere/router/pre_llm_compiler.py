# HESPERIA — Pre-LLM router compiler (HSR-V7-06).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Compose /analyze + optional context_rag + thinking-map into RouterInputEnvelope."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Any

from sphere.router.envelope_v0_1 import RouterInputEnvelope, envelope_to_dict
from sphere.router.thinking_map_bridge import (
    logic_mapping_from_thinking_map,
    policy_block_from_thinking_map,
)

_DEFAULT_CORPUS_SNAPSHOT = "corpus-unset"
_DEFAULT_POLICY_SNAPSHOT = "HSR-V7-01"


def _input_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _logic_from_engine(engine: dict[str, Any]) -> dict[str, Any]:
    return {
        "dominant_area_id": engine.get("dominant_area_id"),
        "dominant_family_id": engine.get("dominant_family_id"),
        "dominant_concept_id": engine.get("dominant_concept_id"),
        "trace_content_hash": engine.get("trace_content_hash"),
        "source": "engine_analyze",
    }


def _policy_from_engine(engine: dict[str, Any]) -> dict[str, Any]:
    gov = float(engine.get("governance") or 0.0)
    risk = "normal" if gov >= 0.35 else "elevated" if gov >= 0.2 else "high"
    return {
        "risk_level": risk,
        "governance": engine.get("governance"),
        "loopability": engine.get("loopability"),
        "tension_energy": engine.get("tension_energy"),
        "obstacle_score": engine.get("obstacle_score"),
        "source": "engine_analyze",
    }


def compile_router_envelope(
    text: str,
    assets_root: Path | None = None,
    *,
    context_packet: dict[str, Any] | None = None,
    thinking_map_outcome: dict[str, Any] | None = None,
    overlay_hint: dict[str, Any] | None = None,
    temp_relation_overlay: list[dict[str, Any]] | None = None,
    corpus_snapshot_id: str | None = None,
) -> dict[str, Any]:
    """HSR-V7-06: single inspectable routed envelope before LLM."""
    from runtime.services.engine_analyze_contract import run_engine_analyze

    engine = run_engine_analyze(
        text,
        assets_root=assets_root,
        overlay_hint=overlay_hint,
        temp_relation_overlay=temp_relation_overlay,
    )
    ctx = context_packet or {}
    corpus_id = (
        corpus_snapshot_id
        or ctx.get("corpus_snapshot_id")
        or os.environ.get("HESPERIA_CORPUS_SNAPSHOT_ID", _DEFAULT_CORPUS_SNAPSHOT)
    )
    if thinking_map_outcome:
        logic_mapping = logic_mapping_from_thinking_map(thinking_map_outcome)
        policy_block = policy_block_from_thinking_map(thinking_map_outcome)
    else:
        logic_mapping = _logic_from_engine(engine)
        policy_block = _policy_from_engine(engine)

    preview = text if len(text) <= 2000 else text[:2000] + "…"
    env = RouterInputEnvelope(
        router_version="v7-router-0.1",
        input_hash=_input_hash(text),
        input_text=preview,
        engine_trace=engine,
        logic_mapping=logic_mapping,
        retrieval_context=ctx.get("retrieval") or ctx.get("retrieval_context") or {},
        relation_context=ctx.get("relation_context") or {},
        policy_block=policy_block,
        corpus_snapshot_id=str(corpus_id),
        policy_snapshot_id=_DEFAULT_POLICY_SNAPSHOT,
        enabled_modules=["core", "router"],
        calculable=ctx.get("calculable"),
        coherence_hints=ctx.get("coherence_hints"),
        observability=ctx.get("observability"),
    ).finalize()
    return envelope_to_dict(env)
