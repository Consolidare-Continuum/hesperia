"""Single runtime entrypoint for canonical execution."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from core.guards.determinism import guard_determinism
from core.output.result_builder import build_result
from hesperia.engine.core import HesperiaEngine


def analyze_engine(text: str) -> dict[str, Any]:
    repo_root = Path(__file__).resolve().parents[2]
    config_path = repo_root / "configs" / "pipeline.yaml"
    engine = HesperiaEngine()
    engine.load_from_config(config_path)
    ctx = engine.run(text)
    metrics = dict(ctx.get("metrics") or {})
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
    failure_flags = list(ctx.get("tfp_conflicts") or [])
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

