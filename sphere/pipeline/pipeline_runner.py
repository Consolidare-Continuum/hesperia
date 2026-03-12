"""
Full L1–L10 pipeline runner. Single canonical entrypoint; strict order; contract and isolation validation.
Orchestrates core layers and sphere modules; produces USF. No layer logic here.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from core.attribution.structural import (
    attribute,
    load_dict_a,
    load_dict_b,
    normalize,
    tokenize,
)
from core.contracts.layer_contract import LayerInput
from core.layers import build_canonical_stub_adjacency, load_defaults
from core.stability import run_stability
from core.policy.interpretation_policy import apply_interpretation_policy

from runtime.pipeline.layer_registry import LAYERS
from runtime.pipeline.pipeline_state import PipelineState

from . import contract_validation, isolation_validation


def _validate_config(config: dict[str, Any]) -> None:
    if not config:
        raise ValueError("config must be non-empty")
    if "pipeline_version" not in config:
        raise ValueError("config must include pipeline_version")
    if config.get("deterministic") is not True:
        raise ValueError("config.deterministic must be True for canonical pipeline")


def _input_hash(raw_text: str, document_id: str | None) -> str:
    h = hashlib.sha256()
    h.update(raw_text.encode("utf-8"))
    if document_id:
        h.update(document_id.encode("utf-8"))
    return "sha256:" + h.hexdigest()


def run_pipeline(
    raw_text: str,
    config: dict[str, Any],
    source_metadata: dict[str, Any] | None = None,
    document_id: str | None = None,
) -> dict[str, Any]:
    """
    Execute full L1–L10 pipeline in strict order. Validate contracts after each layer;
    verify isolation (no upstream mutation). Produce canonical USF.
    """
    if not raw_text or not raw_text.strip():
        raise ValueError("raw_text must be non-empty")
    _validate_config(config)

    document_id = document_id or "unknown"
    source_metadata = source_metadata or {}
    assets_root = config.get("assets_root") or Path(__file__).resolve().parents[2] / "lexicon" / "curated"
    defaults = config.get("defaults")
    if defaults is None:
        defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))

    # Attribution
    dict_a = load_dict_a(assets_root=assets_root) or {}
    dict_b = load_dict_b() or {}
    tokens = tokenize(normalize(raw_text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adjacency = build_canonical_stub_adjacency(F, A)

    metadata = {
        "F": F,
        "A": A,
        "eps": float(defaults.get("eps", 1e-9)),
        "defaults": defaults,
        "matched": matched,
        "hits": hits,
        "adjacency": adjacency,
        "MAX_ALLOWED_DEPTH": D,
    }

    state = PipelineState()
    input_data = LayerInput(text=raw_text, tokens=tokens, metadata=metadata)
    snapshots: dict[int, dict[str, Any]] = {}

    # L1–L9 in order
    for layer_id, layer_module in LAYERS:
        input_data.metadata["layers"] = dict(state.layers)
        if layer_id >= 2 and 2 in state.layers:
            input_data.metadata["visited_B"] = set(state.layers[2].get("VISITED_IDS", []))
        if layer_id == 7 and "stability" not in input_data.metadata:
            stability_out = run_stability(state.layers)
            state.diagnostics["stability"] = stability_out
            input_data.metadata["stability"] = stability_out
        if layer_id == 8:
            policy_mode = config.get("interpretation_policy_mode") or defaults.get("interpretation_policy_mode") or "STRUCTURE_PLUS_CONTEXT"
            policy = apply_interpretation_policy(state, policy_mode)
            input_data.metadata["policy"] = policy

        for prev_id in range(1, layer_id):
            if prev_id in state.layers:
                snapshots[prev_id] = isolation_validation.snapshot_layer_output(state.layers[prev_id])

        output = layer_module.run(input_data)
        state.layers[layer_id] = output.result
        state.diagnostics[str(layer_id)] = output.diagnostics

        for prev_id in list(snapshots.keys()):
            if prev_id in state.layers:
                isolation_validation.validate_no_upstream_mutation(
                    snapshots[prev_id], state.layers[prev_id], f"layer_{prev_id}"
                )
        snapshots.clear()

    # Build layer_outputs for contract check and USF
    layer_outputs: dict[str, Any] = {}
    for i in range(1, 10):
        layer_outputs[f"layer_{i}"] = dict(state.layers.get(i, {}))
    layer_outputs["layer_1"].setdefault("normalized_tokens", tokens)

    # Sphere dynamism: area_sequence from matched token order
    family_sequence = [int(f) for f, _ in matched]
    area_sequence = [f // 24 for f in family_sequence]
    if not area_sequence:
        area_sequence = [0]

    try:
        from sphere.topology.topology_loader import load_area_adjacency
        adj_matrix = load_area_adjacency(config.get("topology_data_root"))
    except Exception:
        import numpy as np
        adj_matrix = np.zeros((12, 12), dtype=np.int64)
        for i in range(12):
            adj_matrix[i, (i - 1) % 12] = 1
            adj_matrix[i, (i + 1) % 12] = 1

    try:
        from sphere.dynamism import compute_dynamism
        dynamism_out = compute_dynamism(family_sequence, area_sequence, adj_matrix)
    except Exception:
        dynamism_out = {
            "trajectory": {"raw": [], "compressed": []},
            "transition_matrix": [[0] * 12 for _ in range(12)],
            "curvature": 0.0,
            "jump_rate": {"jump_count": 0, "jump_rate": 0.0},
            "stability_index": 0.0,
        }

    # Sphere logic: facts from L1 + dynamism
    L1 = state.layers.get(1, {})
    facts = {
        "dominant_area": int(L1.get("DOMINANT_AREA_ID", 0)),
        "dominant_family": int(L1.get("DOMINANT_FAMILY_ID", 0)),
        "entropy": float(L1.get("NORMALIZED_FAMILY_ENTROPY", 0.0)),
        "coverage": float(L1.get("COVERAGE_RATIO", 0.0)),
        "curvature": float(dynamism_out.get("curvature", 0.0)),
        "stability_index": float(dynamism_out.get("stability_index", 0.0)),
        "governance_area": 0.0,
    }
    try:
        from sphere.logic import evaluate_rules
        rule_path = config.get("logic_rules_path")
        logic_out = evaluate_rules(facts, rule_spec_path=rule_path)
    except Exception:
        logic_out = {
            "triggered_rules": [],
            "structural_diagnostics": [],
            "rule_trigger_registry": {"triggered_rule_ids": [], "count": 0, "by_severity": {}, "by_code": {}},
        }

    # L10 placeholder
    allow_l10_placeholder = config.get("allow_placeholder_layer10", True)
    layer_outputs["layer_10"] = {
        "analysis_report": None,
        "interpretation": None,
        "explanation": None,
        "_placeholder": allow_l10_placeholder,
    }

    contract_validation.validate_pipeline_contracts(layer_outputs)
    isolation_validation.validate_layer_isolation(layer_outputs)

    # Area vector from hits (12 areas)
    area_vector = [0.0] * 12
    total_hits = sum(hits)
    for f in range(F):
        a = f // 24
        if a < 12:
            area_vector[a] += hits[f]
    if total_hits > 0:
        area_vector = [x / total_hits for x in area_vector]

    # USF assembly
    try:
        from sphere.metrics import (
            detect_dominant_area,
            detect_dominant_family,
            detect_family_peaks,
            compute_structural_tension,
            compute_loopability,
            compute_entropy,
            compute_family_coverage,
        )
        import numpy as np
        fc = np.array(hits, dtype=np.float64)
        av = np.array(area_vector, dtype=np.float64)
        dominant_area = detect_dominant_area(av)
        dominant_family = detect_dominant_family(fc)
        family_peaks = detect_family_peaks(fc, k=5)
        tension = compute_structural_tension(av)
        loopability = compute_loopability(area_sequence)
        entropy = compute_entropy(av)
        coverage = compute_family_coverage(fc)
    except Exception:
        dominant_area = int(L1.get("DOMINANT_AREA_ID", 0))
        dominant_family = int(L1.get("DOMINANT_FAMILY_ID", 0))
        family_peaks = []
        tension = 0.0
        loopability = 0.0
        entropy = float(L1.get("NORMALIZED_FAMILY_ENTROPY", 0.0))
        coverage = float(L1.get("COVERAGE_RATIO", 0.0))

    raw_metrics = {
        "area_vector": area_vector,
        "family_counts": list(hits),
        "family_peaks": family_peaks,
        "dominant_area": dominant_area,
        "dominant_family": dominant_family,
        "entropy": entropy,
        "tension": tension,
        "loopability": loopability,
        "coverage": coverage,
    }
    dynamism_metrics = {
        "trajectory": dynamism_out.get("trajectory", {}),
        "transition_matrix": dynamism_out.get("transition_matrix", []),
        "curvature": dynamism_out.get("curvature", 0.0),
        "jump_rate": dynamism_out.get("jump_rate", 0.0),
        "stability_index": dynamism_out.get("stability_index", 0.0),
    }
    propagation_metrics = {
        "propagated_area_vector": list(area_vector),
        "propagated_family_counts": [float(x) for x in hits],
    }
    logic_outputs = {
        "triggered_rules": logic_out.get("triggered_rules", []),
        "logic_flags": [r.get("diagnostic_code", "") for r in logic_out.get("triggered_rules", []) if r.get("diagnostic_code")],
        "structural_diagnostics": logic_out.get("structural_diagnostics", []),
    }
    provenance = {
        "created_at": config.get("created_at", ""),
        "pipeline_version": str(config.get("pipeline_version", "v1")),
        "input_hash": _input_hash(raw_text, document_id),
        "deterministic": True,
    }

    try:
        from sphere.usf import generate_usf
        usf = generate_usf(
            document_id=document_id,
            source_metadata=source_metadata,
            raw_metrics=raw_metrics,
            dynamism_metrics=dynamism_metrics,
            propagation_metrics=propagation_metrics,
            logic_outputs=logic_outputs,
            provenance=provenance,
            usf_version="1.0",
        )
    except Exception as e:
        usf = {"_usf_error": str(e), "document_id": document_id}

    pipeline_metadata = {
        "pipeline_version": str(config.get("pipeline_version", "v1")),
        "deterministic": True,
        "executed_layers": list(range(1, 11)),
        "allow_placeholder_layer10": allow_l10_placeholder,
        "input_hash": _input_hash(raw_text, document_id),
        "contract_validation_passed": True,
        "isolation_validation_passed": True,
    }

    result = {
        "document_id": document_id,
        "layer_outputs": layer_outputs,
        "usf": usf,
        "pipeline_metadata": pipeline_metadata,
    }

    try:
        from sphere.guards import run_all_guards
        runtime_meta = dict(pipeline_metadata)
        runtime_meta.setdefault("area_sequence", area_sequence)
        runtime_meta.setdefault("usf", usf)
        result["guards"] = run_all_guards(
            result,
            layer_outputs,
            runtime_meta,
            config,
        )
    except Exception:
        result["guards"] = {
            "sigma": {"passed": False, "failed_checks": [{"invariant_id": "GUARD_RUN_ERROR", "message": "run_all_guards failed"}], "passed_checks": []},
            "gamma": {"passed": False, "failed_checks": [], "passed_checks": []},
            "theta": {"approved": False, "status": "quarantined", "violations": [], "warnings": [], "governance_flags": ["NON_CANONICAL_OUTPUT"]},
        }

    return result
