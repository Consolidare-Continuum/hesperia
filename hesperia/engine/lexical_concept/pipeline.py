# HESPERIA — RAD. DLCR L0→L6 single entry for integration (Ethan INT-010).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from core.hexmap.aggregate import aggregate_hex_state, cross_family_relation_sketch
from core.hexmap.analytics import l1_drift, persistence_score
from core.hexmap.dynamics import apply_decay, concentration_index, dispersion_index, smooth_toward_mean
from core.hexmap.projection import project_concepts_to_hex
from core.lexical.analysis_input import prepare_structural_analysis_text
from core.lexical.cooccurrence import pair_counts_from_canonical
from core.lexical.matcher import match_dict_a
from core.lexical.normalization import normalize_text
from core.lexical.policy import load_dlcr_policy
from core.resolver.resolver import resolve_hit
from core.sequence.segmentation import segment_by_newlines
from core.sequence.trajectory import trajectory_over_segments


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    out: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def _merge_dict_b(paths: list[Path]) -> list[dict[str, Any]]:
    by_id: dict[str, dict[str, Any]] = {}
    for p in paths:
        for row in _load_jsonl(p):
            cid = row.get("concept_id")
            if cid and cid not in by_id:
                by_id[str(cid)] = row
    return [by_id[k] for k in sorted(by_id)]


def _merge_dict_a(paths: list[Path]) -> list[dict[str, Any]]:
    """
    Merge Dict A files in path order. Non-negative rows dedupe on ``normalized_form``
    (first file wins) so curated RU layers override legacy ``dict_a_tfp`` collisions.
    Negative-pattern rows always append (unique phrases).
    """
    rows: list[dict[str, Any]] = []
    seen_nf: set[str] = set()
    for p in paths:
        for row in _load_jsonl(p):
            if row.get("negative_patterns"):
                rows.append(row)
                continue
            nf = row.get("normalized_form")
            if not nf:
                continue
            if nf in seen_nf:
                continue
            seen_nf.add(nf)
            rows.append(row)
    return rows


def _family_slot_index(area: str, family: str) -> int | None:
    if not area.startswith("A") or not family.startswith("F"):
        return None
    try:
        an = int(area[1:])
        fn = int(family[1:])
    except ValueError:
        return None
    if not (1 <= an <= 12 and 1 <= fn <= 24):
        return None
    return (an - 1) * 24 + (fn - 1)


def _concept_weights_from_resolutions(resolved: list[dict[str, Any]]) -> dict[str, float]:
    w: dict[str, float] = {}
    for r in resolved:
        cid = r.get("winning_concept_id")
        if not cid:
            continue
        w[str(cid)] = w.get(str(cid), 0.0) + 1.0
    return w


def _load_version_pins(repo: Path) -> dict[str, Any]:
    p = repo / "assets" / "data" / "engine_dynamics_v060" / "VERSION.yaml"
    if not p.exists():
        return {}
    try:
        import yaml  # type: ignore[import-untyped]

        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def run_dlcr_pipeline(
    text: str,
    *,
    repo_root: Path | None = None,
    dict_a_paths: list[Path] | None = None,
    dict_b_paths: list[Path] | None = None,
    anchors_path: Path | None = None,
    mode: str = "clinical_speech",
) -> dict[str, Any]:
    """
    Run DLCR path: normalize → match Dict A → resolve Dict B → project hex → dynamics → aggregate.

    Default assets: merged seed + TFP packs under ``assets/data/engine_dynamics_v060/``.
    """
    repo = repo_root or _repo_root()
    base = repo / "assets" / "data" / "engine_dynamics_v060"
    # Legacy ``dict_a_tfp`` before stack layers so ``gold_tfp_ru`` B_A10 winners stay stable;
    # stack rows add non-colliding ``normalized_form`` keys (first path wins per form).
    da_paths = dict_a_paths or [
        base / "dict_a" / "dict_a_seed.jsonl",
        base / "dict_a" / "dict_a_tfp.jsonl",
        base / "dict_a" / "dict_a_tfp_ru_core.jsonl",
        base / "dict_a" / "dict_a_tfp_ru_variants.jsonl",
        base / "dict_a" / "dict_a_tfp_ru_speech.jsonl",
        base / "dict_a" / "dict_a_tfp_ru_negative.jsonl",
    ]
    db_paths = dict_b_paths or [
        base / "dict_b" / "dict_b_seed.jsonl",
        base / "dict_b" / "dict_b_tfp_ru_v060.jsonl",
        base / "dict_b" / "dict_b_tfp.jsonl",
    ]
    anch = anchors_path or base / "anchors" / "concept_hex_anchors_tfp.json"
    if not anch.exists():
        anch = base / "anchors" / "concept_hex_anchors.json"

    dict_a = _merge_dict_a(da_paths)
    dict_b_rows = _merge_dict_b(db_paths)
    concept_index = {row["concept_id"]: row for row in dict_b_rows}
    anchor_registry = json.loads(anch.read_text(encoding="utf-8")) if anch.exists() else {}

    pins = _load_version_pins(repo)
    pol = load_dlcr_policy(repo)
    max_acc: int | None
    raw_max = pol.get("dict_a_max_accepted")
    env_max = os.environ.get("HESPERIA_DICT_A_MAX_ACCEPTED", "").strip()
    if env_max.isdigit():
        max_acc = int(env_max)
    elif raw_max is not None and str(raw_max).strip().lstrip("-").isdigit():
        max_acc = int(raw_max)
    else:
        max_acc = None
    smooth_alpha = float(pol.get("hex_smooth_alpha") or 0.0)
    ctx_win = int(pol.get("resolver_context_window") or 48)
    seq_w = float(pol.get("sequential_association_weight") or 0.04)
    cooc_window = int(pol.get("cooc_window") or 4)

    canonical, prep_meta = prepare_structural_analysis_text(text, policy_mode=mode)
    norm = normalize_text(canonical)
    pair_counts = pair_counts_from_canonical(norm["canonical_text"], window=cooc_window)
    top_pairs = sorted(pair_counts.items(), key=lambda x: (-x[1], x[0]))[:24]

    hits, rejected = match_dict_a(norm["canonical_text"], dict_a, max_accepted=max_acc)
    span_outputs: list[dict[str, Any]] = []
    recent_winners: list[str] = []
    for hit in hits:
        ab: dict[str, float] = {}
        if seq_w > 0 and recent_winners:
            for cid in hit.candidate_concept_ids:
                boost = 0.0
                for prev in recent_winners[-3:]:
                    if prev == str(cid):
                        continue
                    boost += seq_w
                if boost > 0:
                    ab[str(cid)] = boost
        r = resolve_hit(
            hit,
            concept_index,
            mode=mode,
            version="v0.6.0",
            canonical_text=norm["canonical_text"],
            context_window=ctx_win,
            association_boost=ab or None,
        )
        span_outputs.append(r)
        w = r.get("winning_concept_id")
        if w:
            recent_winners.append(str(w))

    cw = _concept_weights_from_resolutions(span_outputs)
    hex_state, deg_proj = project_concepts_to_hex(cw, anchor_registry)
    hex_decayed = apply_decay(hex_state, decay=0.05)
    if smooth_alpha > 0:
        hex_decayed = smooth_toward_mean(hex_decayed, alpha=min(1.0, smooth_alpha))
    conc = concentration_index(hex_decayed)
    disp = dispersion_index(hex_decayed)
    fam_d, area_d = aggregate_hex_state(cw, concept_index)
    cross_fam = cross_family_relation_sketch(fam_d, top_k=8)

    hits_288 = [0.0] * 288
    for cid, weight in cw.items():
        meta = concept_index.get(cid) or {}
        for fid in meta.get("family_ids") or []:
            for aid in meta.get("area_ids") or []:
                idx = _family_slot_index(str(aid), str(fid))
                if idx is not None and 0 <= idx < 288:
                    hits_288[idx] += float(weight)

    # Segment trajectory + hex geometry per segment (PO-14 / PO-18)
    seg_summaries: list[dict[str, Any]] = []
    seg_drifts: list[float] = []
    seg_persist: list[float] = []
    prev_map: dict[str, float] = {}
    for _s, _e, seg in segment_by_newlines(text):
        sn = normalize_text(seg)
        sh, _ = match_dict_a(sn["canonical_text"], dict_a, max_accepted=max_acc)
        seg_cw: dict[str, float] = {}
        for hit in sh:
            r = resolve_hit(
                hit,
                concept_index,
                mode=mode,
                version="v0.6.0",
                canonical_text=sn["canonical_text"],
                context_window=ctx_win,
            )
            cid = r.get("winning_concept_id")
            if cid:
                seg_cw[str(cid)] = seg_cw.get(str(cid), 0.0) + 1.0
        hs, _ = project_concepts_to_hex(seg_cw, anchor_registry)
        hs_dec = apply_decay(hs, decay=0.05)
        if smooth_alpha > 0:
            hs_dec = smooth_toward_mean(hs_dec, alpha=min(1.0, smooth_alpha))
        seg_drifts.append(l1_drift(prev_map, hs_dec))
        seg_persist.append(persistence_score(prev_map, hs_dec))
        prev_map = dict(hs_dec)
        dom_slot = None
        mass = 0.0
        if hs:
            dom_sym = max(hs, key=lambda k: hs[k])
            mass = float(hs[dom_sym])
            try:
                from core.hexmap.topology import load_hex_index_map

                mp = load_hex_index_map(base / "anchors" / "hex_index_map.json")
                dom_slot = mp.get(dom_sym)
            except Exception:
                dom_slot = None
        seg_summaries.append({"dominant_slot": dom_slot, "mass": mass})
    traj = trajectory_over_segments(seg_summaries)

    return {
        "run": "dlcr_pipeline_v1",
        "mode": mode,
        "preprocess_meta": prep_meta,
        "policy_applied": {
            "dict_a_max_accepted": max_acc,
            "hex_smooth_alpha": smooth_alpha,
            "resolver_context_window": ctx_win,
            "sequential_association_weight": seq_w,
            "cooc_window": cooc_window,
        },
        "cooccurrence_token_pairs_top": [{"pair": list(p), "count": c} for p, c in top_pairs],
        "cross_family_sketch": cross_fam,
        "segment_hex_geometry": {
            "l1_drifts": [round(x, 6) for x in seg_drifts],
            "persistence_scores": [round(float(x), 6) for x in seg_persist],
        },
        "resource_versions": {
            "dict_a": str(pins.get("dict_a", "merged")),
            "dict_b": str(pins.get("dict_b", "merged")),
            "normalization": str(pins.get("normalization", "v0.6.0")),
            "resolver_rules": str(pins.get("resolver_rules", "v0.6.0")),
            "hex_topology": str(pins.get("hex_topology", "bounded_hx_map_v1")),
            "aggregation": str(pins.get("aggregation", "v0.6.0")),
        },
        "canonical_text": norm["canonical_text"],
        "lexical_hits_accepted": len(hits),
        "lexical_hits_rejected": len(rejected),
        "span_resolutions": span_outputs,
        "concept_weights": {k: round(v, 6) for k, v in sorted(cw.items())},
        "hex_activation": {k: round(v, 6) for k, v in sorted(hex_decayed.items())},
        "hex_concentration": round(conc, 6),
        "hex_dispersion": round(disp, 6),
        "family_activation": {k: round(v, 6) for k, v in sorted(fam_d.items())},
        "area_activation": {k: round(v, 6) for k, v in sorted(area_d.items())},
        "family_hits_288": [round(x, 6) for x in hits_288],
        "degradation_flags": list(deg_proj),
        "segment_trajectory": traj,
    }
