# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Analysis service façade. Public runtime must not orchestrate internal math/pipeline step by step.
Single entry into structural analysis; supports single-text, reduced stages (L1+L2, L1+L2+L3), and optional profile.
Lives in runtime so dependency is runtime → sphere → core (no core → sphere).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def run_structural_analysis(
    text: str,
    assets_root: Path | None = None,
    calibration_profile_id: str | None = None,
    report_profile_id: str | None = None,
    policy_mode: str | None = None,
    profile_path: Path | None = None,
    profile_id: str | None = None,
    profile: dict | None = None,
    stages: str = "full",
    enable_domain_metrics: bool = False,
    domain_constants_path: str | Path | None = None,
) -> dict[str, Any]:
    """
    Run structural analysis on text. Returns public-safe result only (projected).
    stages: "full" | "L1_L2" | "L1_L2_L3". When "full", runs full pipeline; otherwise only the given stages.
    When profile_path or profile is provided, uses profile-based path; otherwise sphere pipeline.
    """
    from core.projection import apply_public_projection

    assets = assets_root or Path(__file__).resolve().parents[2] / "lexicon" / "curated"
    if stages == "L1_L2":
        raw = _run_l1_l2(text, assets)
    elif stages == "L1_L2_L3":
        raw = _run_l1_l2_l3(text, assets)
    else:
        raw = _run_full(text, assets, profile_path, profile_id, profile, policy_mode, enable_domain_metrics, domain_constants_path)
    return apply_public_projection(raw)


def run_structural_analysis_batch(
    texts: list[str],
    assets_root: Path | None = None,
    policy_mode: str | None = None,
) -> list[dict[str, Any]]:
    """Run structural analysis on each text. Returns list of public-safe projected results."""
    from core.projection import apply_public_projection
    from core.layers import load_defaults
    from sphere.pipeline.pipeline_runner import run_pipeline

    assets = assets_root or Path(__file__).resolve().parents[2] / "lexicon" / "curated"
    defaults = load_defaults()
    config = {
        "pipeline_version": "v1",
        "deterministic": True,
        "assets_root": assets,
        "defaults": defaults,
    }
    if policy_mode:
        config["interpretation_policy_mode"] = policy_mode
    results = []
    for i, text in enumerate(texts):
        result = run_pipeline(text, config, document_id=f"batch_{i}")
        layer_outputs = result.get("layer_outputs", {})
        raw = {
            "run": "structural_analysis",
            "text_preview": text[:80],
            "L1": layer_outputs.get("layer_1", {}),
            "L2": layer_outputs.get("layer_2", {}),
            "L3": layer_outputs.get("layer_3", {}),
            "L4": layer_outputs.get("layer_4", {}),
            "L5": layer_outputs.get("layer_5", {}),
            "L6": layer_outputs.get("layer_6", {}),
            "L7": layer_outputs.get("layer_7", {}),
            "L8": layer_outputs.get("layer_8", {}),
            "L9": layer_outputs.get("layer_9", {}),
        }
        results.append(apply_public_projection(raw))
    return results


def _run_full(
    text: str,
    assets: Path,
    profile_path: Path | None,
    profile_id: str | None,
    profile: dict | None,
    policy_mode: str | None,
    enable_domain_metrics: bool = False,
    domain_constants_path: str | Path | None = None,
) -> dict[str, Any]:
    from core.layers import load_defaults
    from sphere.pipeline.pipeline_runner import run_pipeline

    defaults = load_defaults()
    if profile_path and profile_path.exists():
        from core.layers import load_structure_profile
        profile_obj, _ = load_structure_profile(profile_path, F=int(defaults.get("F", 288)), A=int(defaults.get("A", 12)))
        profile_id = profile_id or profile_obj.get("profile_name") or profile_path.stem
        profile = profile_obj
    if profile_id is not None or profile is not None:
        return _run_full_with_profile(text, assets, defaults, profile_id, profile, policy_mode)
    config = {
        "pipeline_version": "v1",
        "deterministic": True,
        "assets_root": assets,
        "defaults": defaults,
    }
    if policy_mode:
        config["interpretation_policy_mode"] = policy_mode
    if enable_domain_metrics:
        config["enable_domain_metrics"] = True
        if domain_constants_path is not None:
            config["domain_constants_path"] = str(domain_constants_path)
    result = run_pipeline(text, config, document_id="analysis_service")
    layer_outputs = result.get("layer_outputs", {})
    raw = {
        "run": "structural_analysis",
        "text_preview": text[:80],
        "L1": layer_outputs.get("layer_1", {}),
        "L2": layer_outputs.get("layer_2", {}),
        "L3": layer_outputs.get("layer_3", {}),
        "L4": layer_outputs.get("layer_4", {}),
        "L5": layer_outputs.get("layer_5", {}),
        "L6": layer_outputs.get("layer_6", {}),
        "L7": layer_outputs.get("layer_7", {}),
        "L8": layer_outputs.get("layer_8", {}),
        "L9": layer_outputs.get("layer_9", {}),
        "usf": result.get("usf"),
        "interpretation_metrics": result.get("interpretation_metrics"),
        "diagnostics": result.get("diagnostics", {}),
    }
    if enable_domain_metrics and result.get("domain_metrics") is not None:
        raw["domain_metrics"] = result["domain_metrics"]
    return raw


def _run_full_with_profile(
    text: str,
    assets: Path,
    defaults: dict,
    profile_id: str | None,
    profile: dict | None,
    policy_mode: str | None,
) -> dict[str, Any]:
    from core.attribution.structural import attribute, load_dict_a, load_dict_b, normalize, tokenize
    from core.contracts.layer_contract import LayerInput
    from core.layers import build_canonical_stub_adjacency
    from core.policy import apply_interpretation_policy
    from core.stability import run_stability
    from sphere.pipeline.layer_registry import LAYERS
    from sphere.pipeline.pipeline_state import PipelineState

    dict_a = load_dict_a(assets_root=assets) or {}
    dict_b = load_dict_b()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))
    tokens = tokenize(normalize(text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adjacency = build_canonical_stub_adjacency(F, A)
    state = PipelineState()
    metadata = {
        "F": F, "A": A, "eps": eps, "defaults": defaults,
        "matched": matched, "hits": hits, "adjacency": adjacency,
        "profile_id": profile_id, "profile": profile, "MAX_ALLOWED_DEPTH": D,
    }
    input_data = LayerInput(text=text, tokens=tokens, metadata=metadata)
    for layer_id, layer_module in LAYERS:
        input_data.metadata["layers"] = dict(state.layers)
        if layer_id >= 2 and 2 in state.layers:
            input_data.metadata["visited_B"] = set(state.layers[2].get("VISITED_IDS", []))
        if layer_id == 7 and "stability" not in input_data.metadata:
            stability_out = run_stability(state.layers)
            state.diagnostics["stability"] = stability_out
            input_data.metadata["stability"] = stability_out
        if layer_id == 8:
            mode = policy_mode or (defaults.get("interpretation_policy_mode") or "STRUCTURE_PLUS_CONTEXT")
            policy = apply_interpretation_policy(state, mode)
            input_data.metadata["policy"] = policy
        output = layer_module.run(input_data)
        state.layers[layer_id] = output.result
        state.diagnostics[str(layer_id)] = output.diagnostics
    return {
        "run": "structural_analysis",
        "text_preview": text[:80],
        "L1": state.layers[1], "L2": state.layers[2], "L3": state.layers[3],
        "L4": state.layers[4], "L5": state.layers[5], "L6": state.layers[6],
        "L7": state.layers[7], "L8": state.layers[8], "L9": state.layers[9],
        "diagnostics": state.diagnostics,
    }


def _run_l1_l2(text: str, assets: Path) -> dict[str, Any]:
    from core.attribution.structural import attribute, load_dict_a, load_dict_b, normalize, tokenize
    from core.layers import build_canonical_stub_adjacency, compute_L1, compute_L2, load_defaults

    dict_a = load_dict_a(assets_root=assets) or {}
    dict_b = load_dict_b()
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))
    tokens = tokenize(normalize(text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adj = build_canonical_stub_adjacency(F, A)
    L1 = compute_L1(len(tokens), matched, F=F, A=A, eps=eps)
    L2 = compute_L2(L1, hits, adjacency=adj, F=F, A=A, MAX_ALLOWED_DEPTH=D, eps=eps)
    return {
        "run": "L1_L2",
        "text_preview": text[:80],
        "L1": L1,
        "L2": L2,
    }


def _run_l1_l2_l3(text: str, assets: Path) -> dict[str, Any]:
    from core.attribution.structural import attribute, load_dict_a, load_dict_b, normalize, tokenize
    from core.layers import build_canonical_stub_adjacency, compute_L1, compute_L2, compute_L3, load_defaults

    dict_a = load_dict_a(assets_root=assets) or {}
    dict_b = load_dict_b()
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))
    tokens = tokenize(normalize(text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adj = build_canonical_stub_adjacency(F, A)
    L1 = compute_L1(len(tokens), matched, F=F, A=A, eps=eps)
    L2 = compute_L2(L1, hits, adjacency=adj, F=F, A=A, MAX_ALLOWED_DEPTH=D, eps=eps)
    L1_S, L2_S, hits_S = L1, L2, hits[:]
    L3 = compute_L3(L1, L2, hits, L1_S, L2_S, hits_S, F=F, A=A, eps=1e-12, **{
        k: defaults.get(k) for k in ("SHADOW_MAX_DEVIATION", "SHADOW_MAX_CROSS_AREA_DELTA", "SHADOW_ALLOW_AREA_FLIP", "TOP_K") if k in defaults
    })
    return {
        "run": "L1_L2_L3",
        "text_preview": text[:80],
        "text_s_preview": text[:80],
        "L1_B": L1, "L2_B": L2, "L1_S": L1_S, "L2_S": L2_S, "L3": L3,
    }
