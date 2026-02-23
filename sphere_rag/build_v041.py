"""
HESPERIA v0.4.1 — Dict B build per 29_SPEC.
Token → { preferred, possible_relaxed } via similarity vs family vectors.
Build-time only; runtime loads only dict_b_v041.json.
"""
from __future__ import annotations

import json
import unicodedata
import re
from pathlib import Path
from typing import Any

from . import build_v041_config as C041
from .build_v040 import (
    filter_candidates,
    load_dict_a_for_build,
    _get_st,
)

# Lazy heavy deps
_np = None

def _get_np_():
    global _np
    if _np is None:
        import numpy as np
        _np = np
    return _np


def load_family_vectors(path: Path) -> Any:
    """Load family_vectors_v040.json → (288, D) matrix, float64, L2-normalized."""
    np = _get_np_()
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    vecs = []
    for i in range(C041.TOTAL_FAMILIES):
        vecs.append(data.get(str(i), [0.0] * 768))
    arr = np.array(vecs, dtype=np.float64)
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    arr = arr / norms
    return arr


def compute_fcs_from_anchors(anchor_records: list[dict], family_vectors: Any) -> dict[int, float]:
    """FCS(f) = mean(cosine(anchor_emb, family_vector_f)) for anchors in family f."""
    np = _get_np_()
    by_family: dict[int, list[int]] = {}  # fg -> list of indices in anchor_records
    for i, r in enumerate(anchor_records):
        fg = int(r["familyGlobal"])
        by_family.setdefault(fg, []).append(i)
    anchors_arr = np.array([r["embedding"] for r in anchor_records], dtype=np.float64)
    fcs = {}
    for fg in range(C041.TOTAL_FAMILIES):
        idx = by_family.get(fg, [])
        if not idx:
            fcs[fg] = 0.0
            continue
        # cosine(anchor, family_vec_fg)
        sims = np.dot(anchors_arr[idx], family_vectors[fg])
        fcs[fg] = float(np.mean(sims))
    return fcs


def load_weak_anchor_families(flags_path: Path) -> set[int]:
    """Families that contain at least one weak_anchor lemma. From dictA_geometry_flags or affinity."""
    if not flags_path.exists():
        return set()
    with open(flags_path, encoding="utf-8") as f:
        data = json.load(f)
    weak_lemmas = {k for k, v in data.get("lemmas", {}).items() if v.get("weak_anchor")}
    if not weak_lemmas:
        return set()
    # Need to map lemma → family. Load dict_a or use affinity.
    # dictA_family_affinity has lemma → primary_family. Use that.
    affinity_path = flags_path.parent / "dictA_family_affinity_v040.json"
    if not affinity_path.exists():
        return set()
    with open(affinity_path, encoding="utf-8") as f:
        affinity = json.load(f)
    return {int(affinity[lemma]["primary_family"]) for lemma in weak_lemmas if lemma in affinity}


def run_build_v041(
    dict_a_path: Path | None = None,
    assets_root: Path | None = None,
    anchors_v040_path: Path | None = None,
    family_vectors_v040_path: Path | None = None,
    candidates_path: Path | None = None,
    out_dir: Path | None = None,
    allow_small_build: bool = False,
) -> None:
    """Full Dict B v0.4.1 build: load inputs, classify vs family vectors, write artifacts."""
    np = _get_np_()
    st = _get_st()
    repo = Path(__file__).resolve().parent.parent
    assets_dir = Path(assets_root) if assets_root else repo / "assets"
    root = assets_dir / "v040"  # v040 artifacts (anchors, family_vectors, flags)
    out_dir = Path(out_dir or assets_dir / "v041")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Inputs
    dict_a = load_dict_a_for_build(path=dict_a_path, assets_root=assets_dir if assets_dir.exists() else repo)
    if not dict_a:
        raise SystemExit("No Dict A loaded.")

    anchors_path = anchors_v040_path or root / "dict_a_anchors_v040.json"
    fv_path = family_vectors_v040_path or root / "family_vectors_v040.json"
    if not anchors_path.exists():
        raise SystemExit(f"Missing {anchors_path}")
    if not fv_path.exists():
        raise SystemExit(f"Missing {fv_path}")

    with open(anchors_path, encoding="utf-8") as f:
        anchor_records = json.load(f)
    family_vectors = load_family_vectors(fv_path)
    fcs_per_family = compute_fcs_from_anchors(anchor_records, family_vectors)

    # Inter-family cosine for overlap cap
    inter_family_cos = np.dot(family_vectors, family_vectors.T)

    weak_families = load_weak_anchor_families(root / "dictA_geometry_flags_v040.json")

    # Candidates
    if candidates_path and candidates_path.exists():
        raw = candidates_path.read_text(encoding="utf-8")
        if candidates_path.suffix == ".json":
            data = json.loads(raw)
            cand_list = data if isinstance(data, list) else list(data.keys())
        else:
            cand_list = [line.strip() for line in raw.splitlines() if line.strip()]
    else:
        cand_list = list(dict_a.keys())
        b_path = assets_dir / "B_SURFACE_LEX_FIELD_v1.json"
        if not b_path.exists():
            b_path = repo / "hesperia_lex" / "curated" / "B_SURFACE_LEX_FIELD_v1.json"
        if b_path.exists():
            from .attribution_v033 import load_dict_b_v033
            legacy_b = load_dict_b_v033(path=b_path)
            cand_list = list(set(cand_list) | set(legacy_b.keys()))
    candidates = filter_candidates(cand_list)
    if not candidates:
        raise SystemExit("No candidates after filtering.")

    # Encode candidates
    model = st.SentenceTransformer(C041.MODEL_NAME)
    cand_sorted = sorted(candidates)
    token_vectors = model.encode(cand_sorted, normalize_embeddings=True)
    if hasattr(token_vectors, "numpy"):
        token_vectors = token_vectors.numpy()
    token_vectors = np.asarray(token_vectors, dtype=np.float64)
    norms = np.linalg.norm(token_vectors, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    token_vectors = token_vectors / norms

    # Similarity vs 288 family vectors: (N, 288)
    sims_all = np.dot(token_vectors, family_vectors.T)
    n_cand = len(cand_sorted)

    dict_b: dict[str, dict[str, Any]] = {}
    accepted_audit: list[dict[str, Any]] = []
    rejected_audit: list[dict[str, Any]] = []
    primary_count: dict[int, int] = {f: 0 for f in range(C041.TOTAL_FAMILIES)}
    secondary_count: dict[int, int] = {f: 0 for f in range(C041.TOTAL_FAMILIES)}
    family_secondary_matrix: dict[int, dict[int, int]] = {f: {g: 0 for g in range(C041.TOTAL_FAMILIES)} for f in range(C041.TOTAL_FAMILIES)}
    n_ambiguous_reject = 0
    n_weak_anchor_assigned = 0

    for idx, token in enumerate(cand_sorted):
        sims = sims_all[idx]
        top2 = np.argsort(-sims)[:2]
        F1, F2 = int(top2[0]), int(top2[1])
        S1, S2 = float(sims[F1]), float(sims[F2])
        margin = S1 - S2

        # §6.1 Preferred
        if S1 < C041.TAU or margin < C041.DELTA_MIN_PRIMARY or fcs_per_family.get(F1, 0) < C041.FCS_MIN:
            reason = "below_tau" if S1 < C041.TAU else ("margin" if margin < C041.DELTA_MIN_PRIMARY else "cohesion")
            if margin < C041.DELTA_MIN_PRIMARY:
                n_ambiguous_reject += 1
            rejected_audit.append({
                "token": token, "S1": S1, "S2": S2, "F1": F1, "F2": F2,
                "FCS_F1": fcs_per_family.get(F1), "rejection_reason": reason,
            })
            continue

        preferred = F1
        primary_count[F1] = primary_count.get(F1, 0) + 1
        if F1 in weak_families:
            n_weak_anchor_assigned += 1

        # §6.2 Possible_relaxed
        possible_relaxed: int | None = None
        if (S2 >= C041.TAU_RELAXED and margin <= C041.DELTA_MAX_SECONDARY and
            float(inter_family_cos[F1, F2]) <= C041.FAMILY_OVERLAP_CAP and
            fcs_per_family.get(F2, 0) >= C041.FCS_MIN):
            possible_relaxed = F2
            secondary_count[F2] = secondary_count.get(F2, 0) + 1
            family_secondary_matrix[F1][F2] = family_secondary_matrix[F1].get(F2, 0) + 1

        dict_b[token] = {"preferred": preferred, "possible_relaxed": possible_relaxed}
        accepted_audit.append({
            "token": token, "preferred": preferred, "possible_relaxed": possible_relaxed,
            "S1": S1, "S2": S2, "F1": F1, "F2": F2, "FCS_F1": fcs_per_family.get(F1),
            "ambiguous_flag": margin < C041.DELTA_MIN_PRIMARY,
        })

    n_accepted = len(dict_b)
    n_rejected = len(rejected_audit)
    total = n_cand
    n_with_secondary = sum(1 for v in dict_b.values() if v.get("possible_relaxed") is not None)

    # §8 §9 Failure conditions
    failures: list[str] = []
    if total > 0 and (n_ambiguous_reject / total) > C041.AMBIGUOUS_PCT_MAX:
        failures.append(f"Ambiguous tokens {n_ambiguous_reject}/{total} ({100*n_ambiguous_reject/total:.1f}%) > {100*C041.AMBIGUOUS_PCT_MAX}%")
    if n_accepted > 0 and (n_weak_anchor_assigned / n_accepted) > C041.WEAK_ANCHOR_PCT_MAX:
        failures.append(f"Weak anchor assigned {n_weak_anchor_assigned}/{n_accepted} > {100*C041.WEAK_ANCHOR_PCT_MAX}%")
    for fg, c in primary_count.items():
        if c > 0 and (c / n_accepted) > C041.KAPPA_MAX_SHARE:
            failures.append(f"Family {fg} primary share {c/n_accepted:.2%} > κ {C041.KAPPA_MAX_SHARE}")
    if n_accepted > 0 and (n_with_secondary / n_accepted) > C041.MAX_SECONDARY_RATIO_GLOBAL:
        failures.append(f"Secondary global ratio {n_with_secondary/n_accepted:.2%} > {C041.MAX_SECONDARY_RATIO_GLOBAL}")
    for fg in range(C041.TOTAL_FAMILIES):
        prim = primary_count.get(fg, 0)
        sec = secondary_count.get(fg, 0)
        if prim > 0 and sec > C041.SECONDARY_PER_FAMILY_RATIO * prim:
            failures.append(f"Family {fg} secondary {sec} > 0.5*primary {prim}")
        if prim + sec > C041.LEXICAL_SLOTS_PER_FAMILY:
            failures.append(f"Family {fg} total lexical {prim+sec} > {C041.LEXICAL_SLOTS_PER_FAMILY}")

    if failures and not allow_small_build:
        fail_path = out_dir / "build_failures_v041.txt"
        fail_path.write_text("\n".join(["Dict B v0.4.1 build FAILED", ""] + failures), encoding="utf-8")
        raise SystemExit("Build failed: " + "; ".join(failures[:3]))

    # Write artifacts
    (out_dir / "dict_b_v041.json").write_text(json.dumps(dict_b), encoding="utf-8")
    with open(out_dir / "dict_b_v041_audit.jsonl", "w", encoding="utf-8") as f:
        for r in accepted_audit:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        for r in rejected_audit:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # family_secondary_matrix: family_i → { family_j: count }
    matrix_out = {str(i): {str(j): v for j, v in row.items() if v > 0} for i, row in family_secondary_matrix.items()}
    (out_dir / "family_secondary_matrix_v041.json").write_text(json.dumps(matrix_out), encoding="utf-8")

    # report_dictB_stats_v041.txt
    lines = [
        "Dict B v0.4.1 statistics",
        "=" * 50,
        f"candidate count: {total}",
        f"accepted: {n_accepted} ({100*n_accepted/max(1,total):.1f}%)",
        f"rejected: {n_rejected}",
        f"ambiguity (rejected margin): {n_ambiguous_reject}",
        f"mean S1 (accepted): {np.mean([a['S1'] for a in accepted_audit]):.4f}" if accepted_audit else "",
        "Per-family primary distribution (non-zero):",
    ]
    for fg in sorted(primary_count.keys()):
        if primary_count[fg] > 0:
            lines.append(f"  family {fg}: {primary_count[fg]}")
    lines.append(f"κ_max_share check: max primary share = {max((c/n_accepted for c in primary_count.values() if n_accepted), default=0):.2%} (cap {C041.KAPPA_MAX_SHARE})")
    (out_dir / "report_dictB_stats_v041.txt").write_text("\n".join(filter(None, lines)), encoding="utf-8")

    # report_secondary_affinity_v041.txt
    lines2 = [
        "Secondary affinity report v0.4.1",
        "=" * 50,
        f"% tokens with possible_relaxed: {n_with_secondary}/{n_accepted} ({100*n_with_secondary/max(1,n_accepted):.1f}%)",
        "Secondary count per family (non-zero):",
    ]
    for fg in sorted(secondary_count.keys()):
        if secondary_count[fg] > 0:
            lines2.append(f"  family {fg}: {secondary_count[fg]}")
    margins = [a["S1"] - a["S2"] for a in accepted_audit]
    if margins:
        lines2.append(f"Margin (S1-S2) distribution: min={min(margins):.4f}, max={max(margins):.4f}, mean={np.mean(margins):.4f}")
    (out_dir / "report_secondary_affinity_v041.txt").write_text("\n".join(lines2), encoding="utf-8")

    # build_manifest_v041.json
    import platform
    import torch
    try:
        from huggingface_hub import model_info
        rev = (model_info(C041.MODEL_NAME).sha or model_info(C041.MODEL_NAME).id or "unknown")
    except Exception:
        rev = "unknown"
    manifest = {
        "model_name": C041.MODEL_NAME,
        "model_revision_hash": rev,
        "torch_version": torch.__version__,
        "python_version": platform.python_version(),
        "tau": C041.TAU,
        "delta_min_primary": C041.DELTA_MIN_PRIMARY,
        "tau_relaxed": C041.TAU_RELAXED,
        "delta_max_secondary": C041.DELTA_MAX_SECONDARY,
        "kappa_max_share": C041.KAPPA_MAX_SHARE,
        "FCS_min": C041.FCS_MIN,
        "date": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dict_a_version": "v1",
        "candidate_list_version": "v1",
    }
    (out_dir / "build_manifest_v041.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("DONE. Dict B v0.4.1 artifacts in", out_dir)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="HESPERIA v0.4.1 Dict B build (29_SPEC)")
    p.add_argument("--dict-a", type=Path)
    p.add_argument("--assets-root", type=Path, help="Directory containing v040 artifacts (anchors, family_vectors)")
    p.add_argument("--anchors", type=Path, help="dict_a_anchors_v040.json")
    p.add_argument("--family-vectors", type=Path, help="family_vectors_v040.json")
    p.add_argument("--candidates", type=Path)
    p.add_argument("--out-dir", type=Path)
    p.add_argument("--allow-small-build", action="store_true")
    args = p.parse_args()
    run_build_v041(
        dict_a_path=args.dict_a,
        assets_root=args.assets_root,
        anchors_v040_path=args.anchors,
        family_vectors_v040_path=args.family_vectors,
        candidates_path=args.candidates,
        out_dir=args.out_dir,
        allow_small_build=args.allow_small_build,
    )
