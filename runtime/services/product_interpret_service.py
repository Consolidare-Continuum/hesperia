# HESPERIA — Product /interpret service (FPF-V7-12).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Build router envelope + structural interpretation from sealed /analyze path."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Literal

from sphere.router.pre_llm_compiler import compile_router_envelope

InterpretMode = Literal["deterministic", "llm"]
RouterMode = Literal["observe", "warn", "strict"]

_SCHEMA_ID = "hesperia.product_interpret.v0_1"


def _router_mode() -> RouterMode:
    raw = os.environ.get("HESPERIA_ROUTER_MODE", "observe").strip().lower()
    if raw in ("observe", "warn", "strict"):
        return raw  # type: ignore[return-value]
    return "observe"


def _apply_router_governance(
    out: dict[str, Any],
    mode: RouterMode,
) -> dict[str, Any]:
    decision = out.get("router_decision", {}).get("decision", "ALLOW")
    out["router_mode"] = mode
    out["governed_decision"] = decision

    if mode == "observe":
        return out

    if mode == "warn" and decision in ("WARN", "REVIEW_REQUIRED", "BLOCK"):
        out["governance_warning"] = (
            f"Router decision: {decision}. Output served with flag."
        )

    if mode == "strict" and decision in ("REVIEW_REQUIRED", "BLOCK"):
        out.pop("llm", None)
        out["interpretation"] = {
            "mode": "blocked",
            "structural_summary": f"Output suppressed — router decision: {decision}.",
            "router_fingerprint": out.get("router_envelope", {}).get("router_fingerprint"),
        }
        out["governance_block"] = True

    return out


def _deterministic_interpretation(
    engine: dict[str, Any],
    envelope: dict[str, Any],
) -> dict[str, Any]:
    trace = engine.get("trace") or []
    top = max(trace, key=lambda s: float(s.get("activation") or 0.0)) if trace else {}
    return {
        "mode": "deterministic",
        "structural_summary": (
            f"Dominant area {engine.get('dominant_area_id')} / "
            f"family {engine.get('dominant_family_id')} "
            f"with governance {engine.get('governance')}."
        ),
        "dominant_activation": top.get("activation"),
        "dominant_label": top.get("label"),
        "router_fingerprint": envelope.get("router_fingerprint"),
        "trace_steps": len(trace),
    }


def run_product_interpret(
    text: str,
    assets_root: Path | None = None,
    *,
    mode: InterpretMode = "deterministic",
    context_packet: dict[str, Any] | None = None,
    thinking_map_outcome: dict[str, Any] | None = None,
    overlay_hint: dict[str, Any] | None = None,
    temp_relation_overlay: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """FPF-V7-12: sealed analyze → router envelope → interpretation."""
    envelope = compile_router_envelope(
        text,
        assets_root,
        context_packet=context_packet,
        thinking_map_outcome=thinking_map_outcome,
        overlay_hint=overlay_hint,
        temp_relation_overlay=temp_relation_overlay,
    )
    engine = envelope.get("engine_trace") or {}
    mode_gov = _router_mode()
    out: dict[str, Any] = {
        "schema": _SCHEMA_ID,
        "mode": mode,
        "router_envelope": envelope,
        "interpretation": _deterministic_interpretation(engine, envelope),
        "engine_trace_hash": engine.get("trace_content_hash"),
        "router_fingerprint": envelope.get("router_fingerprint"),
        "evidence_ids": {
            "input_hash": envelope.get("input_hash"),
            "corpus_snapshot_id": envelope.get("corpus_snapshot_id"),
            "policy_snapshot_id": envelope.get("policy_snapshot_id"),
        },
    }
    if mode == "llm":
        from sphere.router.audit import audit_router_output
        from sphere.router.llm_interpret import LlmInterpretConfig, MockLlmClient, interpret_router_envelope

        provider = os.environ.get("HESPERIA_LLM_PROVIDER", "mock").strip().lower()
        if provider not in ("openai", "anthropic"):
            provider = "mock"
        llm_result = interpret_router_envelope(
            envelope,
            cfg=LlmInterpretConfig(provider=provider),  # type: ignore[arg-type]
            client=MockLlmClient() if provider == "mock" else None,
        )
        out["llm"] = llm_result
        out["prompt_envelope"] = llm_result.get("prompt_envelope")
        audit_bundle = audit_router_output(envelope, llm_result, assets_root=assets_root)
        out["router_output_audit"] = audit_bundle["audit"]
        out["router_decision"] = audit_bundle["router_decision"]
        out["decision"] = audit_bundle["router_decision"].get("decision")
        out["evidence_ids"]["output_hash"] = audit_bundle["audit"].get("output_hash")
        out = _apply_router_governance(out, mode_gov)
    else:
        out["decision"] = "ALLOW"
        out["router_mode"] = mode_gov
    return out
