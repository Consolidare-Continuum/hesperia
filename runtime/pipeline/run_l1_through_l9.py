#!/usr/bin/env python3
"""Run L1..L9 via layer contract: attribution → LayerInput → L1→…→L9. State in PipelineState. Usage: python3 -m runtime.pipeline.run_l1_through_l9 [--out path.json]"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parents[1]
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))

from core.attribution.structural import (
    attribute,
    load_dict_a,
    load_dict_b,
    normalize,
    tokenize,
)
from core.contracts.layer_contract import LayerInput
from core.layers import build_canonical_stub_adjacency, load_defaults, load_structure_profile
from core.policy import apply_interpretation_policy
from core.stability import run_stability
from runtime.dossier import validate_dossier_schema, write_dossier_json
from runtime.dossier.index_manager import update_dossier_index
from runtime.provenance import build_run_manifest, get_engine_provenance

from .layer_registry import LAYERS
from .pipeline_state import PipelineState


def run_pipeline_for_text(
    text: str,
    assets_root: Path | None = None,
    defaults: dict | None = None,
    profile_id: str | None = None,
    profile: dict | None = None,
    policy_mode: str | None = None,
) -> dict:
    """
    Run L1→L9 + Δ stability layer on a single text. Returns full pipeline output dict
    (L1..L9, diagnostics) for use by multiscale or other callers.
    """
    assets = assets_root if assets_root is not None else _HESPERIA / "lexicon" / "curated"
    if defaults is None:
        from core.layers import load_defaults
        defaults = load_defaults()
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
        "F": F,
        "A": A,
        "eps": eps,
        "defaults": defaults,
        "matched": matched,
        "hits": hits,
        "adjacency": adjacency,
        "profile_id": profile_id,
        "profile": profile,
        "MAX_ALLOWED_DEPTH": D,
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
            mode = policy_mode or (defaults.get("interpretation_policy_mode") if isinstance(defaults, dict) else None) or "STRUCTURE_PLUS_CONTEXT"
            policy = apply_interpretation_policy(state, mode)
            input_data.metadata["policy"] = policy
        output = layer_module.run(input_data)
        state.layers[layer_id] = output.result
        state.diagnostics[str(layer_id)] = output.diagnostics

    return {
        "run": "L1_through_L9",
        "text_preview": text[:80],
        "L1": state.layers[1],
        "L2": state.layers[2],
        "L3": state.layers[3],
        "L4": state.layers[4],
        "L5": state.layers[5],
        "L6": state.layers[6],
        "L7": state.layers[7],
        "L8": state.layers[8],
        "L9": state.layers[9],
        "diagnostics": state.diagnostics,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default="justice lie fairness truth good order harm freedom")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument(
        "--profile",
        type=Path,
        default=None,
        help="Path to STRUCTURE_PROFILE__*.json (L1 profile mode)",
    )
    ap.add_argument(
        "--policy-mode",
        dest="policy_mode",
        default=None,
        choices=("STRUCTURE_ONLY", "STRUCTURE_PLUS_CONTEXT", "FULL_INTERPRETATION"),
        help="Π interpretation policy mode (default: from defaults or STRUCTURE_PLUS_CONTEXT)",
    )
    ap.add_argument(
        "--write-dossier",
        type=Path,
        default=None,
        metavar="PATH",
        help="Write deterministic dossier artifact (HSD) with checksum to PATH",
    )
    ap.add_argument(
        "--validate-dossier",
        action="store_true",
        help="Validate dossier schema before writing (when used with --write-dossier)",
    )
    args = ap.parse_args()

    assets = _HESPERIA / "lexicon" / "curated"
    dict_a = load_dict_a(assets_root=assets) or {}
    dict_b = load_dict_b()
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))

    profile_id = None
    profile = None
    if args.profile and args.profile.exists():
        profile, _ = load_structure_profile(args.profile, F=F, A=A)
        profile_id = profile.get("profile_name") or profile.get("profile_version") or args.profile.stem

    policy_mode = getattr(args, "policy_mode", None) or defaults.get("interpretation_policy_mode")
    out = run_pipeline_for_text(
        args.text,
        assets_root=assets,
        defaults=defaults,
        profile_id=profile_id,
        profile=profile,
        policy_mode=policy_mode,
    )
    L7 = out["L7"]
    L9 = out["L9"]
    if getattr(args, "validate_dossier", False):
        try:
            validate_dossier_schema(out)
            print("Dossier schema validation passed.", file=sys.stderr)
        except ValueError as e:
            print("Dossier schema validation failed:", e, file=sys.stderr)
            sys.exit(1)
    if getattr(args, "write_dossier", None):
        dossier_payload = dict(out)
        meta = dict(dossier_payload.get("meta", {}))
        meta.update(get_engine_provenance())
        meta["run_manifest"] = build_run_manifest(args, defaults, profile_id, profile, assets)
        dossier_payload["meta"] = meta
        write_dossier_json(dossier_payload, args.write_dossier)
        update_dossier_index(args.write_dossier)
        print("Dossier written to", args.write_dossier, file=sys.stderr)
    j = json.dumps(out, indent=2)
    if args.out:
        args.out.write_text(j, encoding="utf-8")
        print("Output written to", args.out, file=sys.stderr)
    print(j)
    print(
        "--- reportable --- L7 DECISION_STATUS_CODE:",
        L7["DECISION_STATUS_CODE"],
        "OUTPUT_TRUST_TAG:",
        L7["OUTPUT_TRUST_TAG"],
        "L9 BRAND_WORD_TRUST:",
        L9["BRAND_WORD_TRUST"],
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
