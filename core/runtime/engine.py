"""Single runtime entrypoint for canonical execution."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from core.guards.determinism import guard_determinism
from core.output.result_builder import build_result
from hesperia.engine.runner import run_orchestration
from hesperia.engine.language import (
    FAMILY_SCORES,
    METRICS,
    TFP_CONFLICTS,
)


def analyze_engine(text: str) -> dict[str, Any]:
    repo_root = Path(__file__).resolve().parents[2]
    ctx = run_orchestration(text, repo_root=repo_root)
    metrics = dict(ctx.get(METRICS) or {})
    area_vector = list(metrics.get("area_vector") or [])
    family_vector = list(metrics.get("family_vector") or [])
    area_activation = {f"A{i+1}": float(v) for i, v in enumerate(area_vector)}
    family_activation = {f"F{i+1}": float(v) for i, v in enumerate(family_vector)}
    trajectory = {
        "segment_count": 1,
        "transition_count": 0,
        "stability_window": float(metrics.get("stability", 1.0)),
        "jump_distance": 0.0,
    }
    _ = ctx.get(FAMILY_SCORES)  # main engine language binding in runtime
    failure_flags = list(ctx.get(TFP_CONFLICTS) or [])
    result = build_result(
        area_activation=area_activation,
        family_activation=family_activation,
        trajectory=trajectory,
        segment_drifts=[0.0],
        failure_flags=failure_flags,
    )
    guard_determinism(result)
    return result


def analyze(text: str) -> dict[str, Any]:
    return analyze_engine(text)

