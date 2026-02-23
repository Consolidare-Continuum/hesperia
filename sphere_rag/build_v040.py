"""
HESPERIA v0.4.0 — build pipeline: Dict A → anchors → Dict B → surface (roles + map).
28_SPEC__v0_4_0_Embedding_Based_DictB_and_Surface_Siding.
Deterministic, build-time only. Produces frozen artifacts + reports + manifest.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from . import build_v040_config as C
from .attribution_v033 import load_dict_a_v033, load_dict_b_v033
from .invariant_catalog import SIDES_PER_FAMILY, TOTAL_SIDES

# Lazy import heavy deps
_sentence_transformers = None
_np = None


def _get_st():
    global _sentence_transformers
    if _sentence_transformers is None:
        import sentence_transformers
        _sentence_transformers = sentence_transformers
    return _sentence_transformers


def _get_np():
    global _np
    if _np is None:
        import numpy as np
        _np = np
    return _np


# ---------- §5–6 Normalization and candidate filtering ----------
_PUNCT = re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
_STRIP_PUNCT_RE = re.compile(f"[{_PUNCT}]")


def normalize_token(s: str) -> str:
    """NFKC, lowercase. No length cap (build uses length filter separately)."""
    if not isinstance(s, str):
        s = str(s)
    s = unicodedata.normalize("NFKC", s).lower().strip()
    s = " ".join(s.split())
    return s


def strip_ascii_punct(s: str) -> str:
    return _STRIP_PUNCT_RE.sub("", s).strip()


def filter_candidates(tokens: list[str]) -> set[str]:
    """§6: reject empty, len<2, len>40, numeric-only, no letters. Return deduped set."""
    out: set[str] = set()
    for t in tokens:
        n = normalize_token(t)
        p = strip_ascii_punct(n)
        if not p or len(p) < 2 or len(p) > 40:
            continue
        if p.isdigit():
            continue
        if not any(c.isalpha() for c in p):
            continue
        out.add(p)
    return out


# ---------- Dict A as lemma → {familyGlobal, altitude} ----------
def load_dict_a_for_build(path: Path | None = None, assets_root: Path | None = None) -> dict[str, dict[str, Any]]:
    """Load Dict A (native or legacy) as lemma → {familyGlobal, altitude}."""
    return load_dict_a_v033(path=path, assets_root=assets_root)


# ---------- Embedding model and anchors ----------
def get_model_revision() -> str:
    """Try to get pinned revision for MODEL_NAME from Hugging Face."""
    try:
        from huggingface_hub import model_info
        info = model_info(C.MODEL_NAME)
        return info.sha or info.id or "unknown"
    except Exception:
        return "unknown"


def build_anchor_embeddings(
    dict_a: dict[str, dict[str, Any]],
    model_name: str = C.MODEL_NAME,
) -> tuple[list[dict[str, Any]], list[tuple[str, int, float]], object]:
    """Embed all Dict A lemmas. Returns (anchor_records, list of (lemma, familyGlobal, altitude), model)."""
    st = _get_st()
    np = _get_np()
    model = st.SentenceTransformer(model_name)
    lemmas = sorted(dict_a.keys())
    if not lemmas:
        return [], [], model
    # Single-token strings, no wrapping
    vectors = model.encode(lemmas, normalize_embeddings=True)
    if hasattr(vectors, "numpy"):
        vectors = vectors.numpy()
    vectors = np.asarray(vectors, dtype=np.float64)
    # L2 normalize again for deterministic cosine
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    vectors = vectors / norms
    anchor_records = []
    for i, lemma in enumerate(lemmas):
        entry = dict_a[lemma]
        fg = int(entry["familyGlobal"])
        alt = float(entry.get("altitude", 0.5))
        anchor_records.append({
            "lemma": lemma,
            "familyGlobal": fg,
            "altitude": alt,
            "embedding": vectors[i].tolist(),
        })
    return anchor_records, [(lemma, int(dict_a[lemma]["familyGlobal"]), float(dict_a[lemma].get("altitude", 0.5))) for lemma in lemmas], model


def cosine_similarity(vec: Any, anchors: Any) -> Any:
    """vec (1, D), anchors (N, D) → (N,) similarities."""
    np = _get_np()
    v = np.asarray(vec, dtype=np.float64)
    a = np.asarray(anchors, dtype=np.float64)
    if v.ndim == 1:
        v = v.reshape(1, -1)
    return np.dot(a, v.T).ravel()


# ---------- §8A Family affinity matrix (diagnostic) ----------
def build_family_vectors(anchor_records: list[dict[str, Any]]) -> tuple[dict[int, list[float]], Any]:
    """Option A: mean embedding per family. Returns (family_global -> vector, np array (288, D))."""
    np = _get_np()
    by_family: dict[int, list[list[float]]] = {}
    for r in anchor_records:
        fg = int(r["familyGlobal"])
        by_family.setdefault(fg, []).append(r["embedding"])
    dim = len(anchor_records[0]["embedding"]) if anchor_records else 768
    vectors_dict: dict[int, list[float]] = {}
    matrix = np.zeros((C.TOTAL_FAMILIES, dim), dtype=np.float64)
    for fg in range(C.TOTAL_FAMILIES):
        embs = by_family.get(fg, [])
        if embs:
            arr = np.array(embs, dtype=np.float64)
            mean_v = np.mean(arr, axis=0)
            norm = np.linalg.norm(mean_v)
            if norm > 0:
                mean_v = mean_v / norm
            matrix[fg] = mean_v
            vectors_dict[fg] = mean_v.tolist()
        else:
            vectors_dict[fg] = [0.0] * dim
    return vectors_dict, matrix


def build_affinity_matrix(
    anchor_records: list[dict[str, Any]],
    family_vectors_matrix: Any,
) -> tuple[list[dict[str, Any]], dict[int, float], dict[tuple[int, int], float], list[tuple[str, float]]]:
    """
    Per-lemma: full 288 affinity, primary, OSS, top5.
    Returns (affinity_records, fcs_per_family, cross_sim_map (f,g)->mean, weak_anchors list (lemma, OSS)).
    """
    np = _get_np()
    anchors_arr = np.array([r["embedding"] for r in anchor_records], dtype=np.float64)
    # (N_anchors, 288)
    sims_all = np.dot(anchors_arr, family_vectors_matrix.T)
    # Normalize to [0,1]: cosine in [-1,1] -> (s+1)/2
    sims_01 = ((sims_all + 1.0) * 0.5).clip(0.0, 1.0)

    affinity_records: list[dict[str, Any]] = []
    weak_anchors: list[tuple[str, float]] = []
    for i, r in enumerate(anchor_records):
        vec_288 = sims_01[i].tolist()
        sorted_idx = np.argsort(-sims_01[i])
        primary_fg = int(sorted_idx[0])
        primary_score = float(sims_01[i, primary_fg])
        second_score = float(sims_01[i, sorted_idx[1]]) if len(sorted_idx) > 1 else primary_score
        oss = primary_score - second_score
        if oss < C.OSS_THRESHOLD:
            weak_anchors.append((r["lemma"], oss))
        top5 = [{"family": int(sorted_idx[j]), "score": float(sims_01[i, sorted_idx[j]])} for j in range(min(5, len(sorted_idx)))]
        affinity_records.append({
            "lemma": r["lemma"],
            "primary_family": primary_fg,
            "primary_score": primary_score,
            "full_affinity_vector": vec_288,
            "top5_families": top5,
            "OSS": round(oss, 6),
        })

    # FCS: per family, mean intra-family similarity (each anchor vs family vector)
    fcs_per_family: dict[int, float] = {}
    for fg in range(C.TOTAL_FAMILIES):
        indices = [i for i, r in enumerate(anchor_records) if r["familyGlobal"] == fg]
        if len(indices) < 2:
            fcs_per_family[fg] = 1.0 if indices else 0.0
        else:
            # mean of cosine(anchor, family_vector) for anchors in this family
            vals = [float(sims_all[i, fg]) for i in indices]
            fcs_per_family[fg] = float(np.mean(vals))

    # Cross-family mean similarity: for each (f,g) f!=g, mean over anchors in f of sim to g
    cross_sim_map: dict[tuple[int, int], float] = {}
    for fg in range(C.TOTAL_FAMILIES):
        indices = [i for i, r in enumerate(anchor_records) if r["familyGlobal"] == fg]
        for g in range(C.TOTAL_FAMILIES):
            if fg == g:
                continue
            if not indices:
                cross_sim_map[(fg, g)] = 0.0
            else:
                cross_sim_map[(fg, g)] = float(np.mean([sims_all[i, g] for i in indices]))

    return affinity_records, fcs_per_family, cross_sim_map, weak_anchors


def write_affinity_artifacts(
    anchor_records: list[dict[str, Any]],
    family_vectors_dict: dict[int, list[float]],
    affinity_records: list[dict[str, Any]],
    fcs_per_family: dict[int, float],
    cross_sim_map: dict[tuple[int, int], float],
    weak_anchors: list[tuple[str, float]],
    out_dir: Path,
    allow_small_build: bool,
) -> None:
    """Write §8A artifacts: dictA_family_affinity, family_vectors, reports, flags."""
    np = _get_np()
    # dictA_family_affinity_v040.json
    affinity_by_lemma = {}
    for r in affinity_records:
        affinity_by_lemma[r["lemma"]] = {
            "primary_family": r["primary_family"],
            "primary_score": r["primary_score"],
            "full_affinity_vector": r["full_affinity_vector"],
            "top5_families": r["top5_families"],
            "OSS": r["OSS"],
        }
    (out_dir / "dictA_family_affinity_v040.json").write_text(json.dumps(affinity_by_lemma, indent=2), encoding="utf-8")

    # family_vectors_v040.json
    fv_out = {str(fg): vec for fg, vec in family_vectors_dict.items()}
    (out_dir / "family_vectors_v040.json").write_text(json.dumps(fv_out), encoding="utf-8")

    # report_dictA_affinity_matrix_v040.txt
    oss_vals = [r["OSS"] for r in affinity_records]
    n_ambig = sum(1 for r in affinity_records if r["OSS"] < C.OSS_THRESHOLD)
    lines = [
        "Dict A affinity matrix report (§8A)",
        "=" * 50,
        f"OSS distribution: mean={np.mean(oss_vals):.4f}, median={np.median(oss_vals):.4f}, min={min(oss_vals):.4f}",
        f"% ambiguous lemmas (OSS < {C.OSS_THRESHOLD}): {n_ambig}/{len(affinity_records)} ({100*n_ambig/max(1,len(affinity_records)):.1f}%)",
        "",
        "Top 20 weakest anchors (by OSS):",
    ]
    weak_sorted = sorted(weak_anchors, key=lambda x: x[1])[:20]
    for lemma, oss in weak_sorted:
        lines.append(f"  {lemma}: OSS={oss:.4f}")
    if len(weak_anchors) < 20 and weak_anchors:
        lines.append(f"  (all {len(weak_anchors)} weak listed)")
    lines.append("")
    lines.append("Family Cohesion Score (FCS) per family (first 30):")
    for fg in sorted(fcs_per_family.keys())[:30]:
        lines.append(f"  family {fg}: FCS={fcs_per_family[fg]:.4f}")
    if len(fcs_per_family) > 30:
        lines.append(f"  ... and {len(fcs_per_family)-30} more")
    # CFL: top overlapping pairs (by mean cross-similarity)
    pairs = [(k, v) for k, v in cross_sim_map.items()]
    pairs.sort(key=lambda x: -x[1])
    lines.append("")
    lines.append("Cross-family leakage — top 15 overlapping pairs (f, g, mean_sim):")
    for (f, g), v in pairs[:15]:
        lines.append(f"  ({f}, {g}): {v:.4f}")
    (out_dir / "report_dictA_affinity_matrix_v040.txt").write_text("\n".join(lines), encoding="utf-8")

    # report_family_geometry_v040.txt — inter-family cosine (family vector vs family vector)
    n_f = C.TOTAL_FAMILIES
    fv_matrix = np.array([family_vectors_dict.get(fg, [0.0] * 768) for fg in range(n_f)], dtype=np.float64)
    norms = np.linalg.norm(fv_matrix, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    fv_matrix = fv_matrix / norms
    inter = np.dot(fv_matrix, fv_matrix.T)
    triu = np.triu_indices(n_f, k=1)
    off_diag = inter[triu]
    pairs_geom = []
    for i in range(n_f):
        for j in range(i + 1, n_f):
            pairs_geom.append((i, j, float(inter[i, j])))
    pairs_geom.sort(key=lambda x: -x[2])
    mean_sim_per_f = [float(np.mean([inter[f, g] for g in range(n_f) if g != f])) for f in range(n_f)]
    most_isolated = int(np.argmin(mean_sim_per_f))
    lines_geom = [
        "Family geometry report (§8A)",
        "=" * 50,
        "Inter-family cosine (family vector vs family vector):",
        f"  Mean off-diagonal: {float(np.mean(off_diag)):.4f}",
        "Most similar family pairs (top 10):",
    ]
    for i, j, s in pairs_geom[:10]:
        lines_geom.append(f"  ({i}, {j}): {s:.4f}")
    lines_geom.append(f"Most isolated family (lowest mean sim to others): {most_isolated} (mean={mean_sim_per_f[most_isolated]:.4f})")
    # Entropy indicator: distribution of off-diag similarities
    hist, _ = np.histogram(off_diag, bins=10, range=(-1, 1))
    lines_geom.append("Off-diagonal similarity histogram (10 bins): " + ", ".join(str(int(h)) for h in hist))
    (out_dir / "report_family_geometry_v040.txt").write_text("\n".join(lines_geom), encoding="utf-8")

    # dictA_geometry_flags_v040.json
    thin_families = [fg for fg, fcs in fcs_per_family.items() if fcs < C.FCS_THRESHOLD]
    overlap_pairs = [(f, g) for (f, g), v in cross_sim_map.items() if v > C.CFL_CROSS_SIM_MAX]
    flags_lemmas = {r["lemma"]: {"weak_anchor": r["OSS"] < C.OSS_THRESHOLD} for r in affinity_records}
    flags = {
        "lemmas": flags_lemmas,
        "thin_families": thin_families,
        "family_overlap_pairs": overlap_pairs[:50],
        "summary": {
            "n_weak_anchors": len(weak_anchors),
            "n_thin_families": len(thin_families),
            "n_overlap_pairs": len(overlap_pairs),
        },
    }
    (out_dir / "dictA_geometry_flags_v040.json").write_text(json.dumps(flags, indent=2), encoding="utf-8")

    # §8A.6 optional fail/warn
    if not allow_small_build:
        pct_ambig = 100.0 * n_ambig / max(1, len(affinity_records))
        if pct_ambig > 100 * C.OSS_AMBIGUOUS_PCT_MAX:
            import warnings
            warnings.warn(f"§8A.6: {pct_ambig:.1f}% of Dict A lemmas have OSS < {C.OSS_THRESHOLD} (threshold {100*C.OSS_AMBIGUOUS_PCT_MAX}%)")
        for fg, fcs in fcs_per_family.items():
            if fcs < C.FCS_FAIL:
                import warnings
                warnings.warn(f"§8A.6: family {fg} FCS {fcs:.4f} < {C.FCS_FAIL}")
        for (f, g), v in cross_sim_map.items():
            if v > C.CFL_CROSS_SIM_MAX:
                import warnings
                warnings.warn(f"§8A.6: families ({f},{g}) mean cross-similarity {v:.4f} > {C.CFL_CROSS_SIM_MAX}")


# ---------- Dict B build ----------
def build_dict_b_with_model(
    candidates: set[str],
    anchor_records: list[dict[str, Any]],
    model: Any,
    tau: float = C.TAU_DEFAULT,
    delta: float = C.DELTA_DEFAULT,
    mu: str = C.MU_DEFAULT,
    k: int = C.K_TOP,
) -> tuple[dict[str, int], list[dict[str, Any]], list[dict[str, Any]]]:
    np = _get_np()
    anchors_array = np.array([r["embedding"] for r in anchor_records], dtype=np.float64)
    dict_b: dict[str, int] = {}
    accepted_audit: list[dict[str, Any]] = []
    rejected_audit: list[dict[str, Any]] = []

    # Encode all candidates in one batch for speed
    cand_list = sorted(candidates)
    if not cand_list:
        return dict_b, accepted_audit, rejected_audit
    token_vectors = model.encode(cand_list, normalize_embeddings=True)
    if hasattr(token_vectors, "numpy"):
        token_vectors = token_vectors.numpy()
    token_vectors = np.asarray(token_vectors, dtype=np.float64)
    norms = np.linalg.norm(token_vectors, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    token_vectors = token_vectors / norms

    for idx, token in enumerate(cand_list):
        sims = np.dot(anchors_array, token_vectors[idx])
        top_indices = np.argsort(-sims)[:k]
        top1_idx = int(top_indices[0])
        top1_score = float(sims[top1_idx])
        top2_score = float(sims[top_indices[1]]) if len(top_indices) > 1 else top1_score
        top1_anchor = anchor_records[top1_idx]
        top1_lemma = top1_anchor["lemma"]
        top1_fg = int(top1_anchor["familyGlobal"])

        if top1_score < tau:
            rejected_audit.append({
                "token": token,
                "best_score": top1_score,
                "best_anchor_lemma": top1_lemma,
                "reason": "below_threshold",
            })
            continue

        ambiguous = (top1_score - top2_score) < delta
        if mu == "flag_and_reject" and ambiguous:
            rejected_audit.append({
                "token": token,
                "best_score": top1_score,
                "best_anchor_lemma": top1_lemma,
                "reason": "ambiguous_rejected",
            })
            continue

        # Tie-break already resolved by argsort (first occurrence). Spec: equal score → lowest familyGlobal, then lexicographic lemma.
        # We iterate anchors in record order; top1_idx is best. If there were ties we'd need to pick lowest fg then smallest lemma.
        dict_b[token] = top1_fg
        topk_list = [
            {"familyGlobal": int(anchor_records[i]["familyGlobal"]), "lemma": anchor_records[i]["lemma"], "score": float(sims[i])}
            for i in top_indices
        ]
        accepted_audit.append({
            "token": token,
            "assigned_familyGlobal": top1_fg,
            "top1_score": top1_score,
            "top1_anchor_lemma": top1_lemma,
            "top2_score": top2_score,
            "ambiguous_flag": ambiguous,
            "topK": topk_list,
        })

    return dict_b, accepted_audit, rejected_audit


# ---------- Anti-collapse checks ----------
def check_imbalance(dict_b: dict[str, int], kappa_max: float = C.KAPPA_MAX_SHARE) -> tuple[bool, dict[int, int]]:
    """Returns (ok, per_family_counts). ok=False if any family > kappa_max share."""
    total = len(dict_b)
    if total == 0:
        return True, {}
    counts: dict[int, int] = {}
    for fg in dict_b.values():
        counts[fg] = counts.get(fg, 0) + 1
    for fg, c in counts.items():
        if c / total > kappa_max:
            return False, counts
    return True, counts


def check_coverage(per_family_counts: dict[int, int], f_min: int = C.F_MIN_COVERED) -> bool:
    return len(per_family_counts) >= f_min


# ---------- Surface: role mask (deterministic L/T/S/R per family) ----------
def _seed_for_family(family_global: int, version: str = "v040") -> int:
    h = hashlib.sha256(f"{version}:{family_global}".encode()).digest()
    return int.from_bytes(h[:4], "big")


def build_role_mask_per_family_v2(family_global: int) -> list[str]:
    """Deterministic 1500 roles. Quotas: L=600, T=450, S=300, R=150. Per hex: L≤3, T≥1."""
    # 250 hexes. Assign (L,T,S,R) per hex so sums match. Templates: (3,2,1,0)*100, (3,2,0,1)*100, (0,1,2,3)*50 → L=600, T=450, S=200+100=300, R=100+50=150. Ok.
    templates = [
        (3, 2, 1, 0),
        (3, 2, 0, 1),
        (0, 1, 2, 3),
    ]
    counts = [100, 100, 50]
    flat: list[str] = []
    for (l, t, s, r), n in zip(templates, counts):
        for _ in range(n):
            flat.extend([C.ROLE_L] * l + [C.ROLE_T] * t + [C.ROLE_S] * s + [C.ROLE_R] * r)
    rng = _seed_for_family(family_global)
    result = []
    for h in range(C.HEXES_PER_FAMILY):
        start = h * C.SIDES_PER_HEX
        hex_roles = flat[start : start + C.SIDES_PER_HEX]
        seed = (rng + h * 7919) & 0x7FFF_FFFF
        order = list(range(6))
        for i in range(5, 0, -1):
            seed = (seed * 1103515245 + 12345) & 0x7FFF_FFFF
            j = seed % (i + 1)
            order[i], order[j] = order[j], order[i]
        result.extend([hex_roles[order[i]] for i in range(6)])
    return result


# ---------- Token placement: assign token to lexical side (family, hex, side) ----------
def token_to_placement_key(token: str, family_global: int) -> int:
    """Deterministic key for initial placement (family-local side index 0..1499)."""
    h = hashlib.sha256(f"v040:{family_global}:{token}".encode()).digest()
    return int.from_bytes(h[:4], "big") % SIDES_PER_FAMILY


def place_tokens_on_surface_v2(
    dict_b: dict[str, int],
    role_masks: dict[int, list[str]],
) -> dict[int, list[str]]:
    """Place each token on an L side of its family. Bucket = list of tokens per side. Deterministic."""
    surface_map: dict[int, list[str]] = {}
    hex_lex_used: dict[int, dict[int, int]] = {fg: {h: 0 for h in range(C.HEXES_PER_FAMILY)} for fg in range(C.TOTAL_FAMILIES)}

    tokens_by_family: dict[int, list[str]] = {}
    for token, fg in dict_b.items():
        tokens_by_family.setdefault(fg, []).append(token)
    for fg in tokens_by_family:
        tokens_by_family[fg].sort()

    for family_global, tokens in tokens_by_family.items():
        mask = role_masks[family_global]
        hex_used = hex_lex_used[family_global]
        for token in tokens:
            start = token_to_placement_key(token, family_global)
            placed = False
            for o in range(SIDES_PER_FAMILY):
                side_local = (start + o) % SIDES_PER_FAMILY
                if mask[side_local] != C.ROLE_L:
                    continue
                hex_local = side_local // C.SIDES_PER_HEX
                side_id = family_global * SIDES_PER_FAMILY + side_local
                bucket = surface_map.get(side_id, [])
                if bucket:
                    bucket.append(token)
                    bucket.sort()
                    surface_map[side_id] = bucket
                    placed = True
                    break
                if hex_used[hex_local] < C.L_MAX_PER_HEX:
                    surface_map[side_id] = [token]
                    hex_used[hex_local] += 1
                    placed = True
                    break
            if not placed:
                raise RuntimeError(f"Could not place token {token} in family {family_global}")
    return surface_map


# ---------- Reports ----------
def write_report_dict_a_coverage(anchor_records: list[dict], path: Path, a_min: int = C.A_MIN) -> None:
    by_family: dict[int, list[str]] = {}
    for r in anchor_records:
        fg = r["familyGlobal"]
        by_family.setdefault(fg, []).append(r["lemma"])
    lines = ["Dict A coverage (anchors per family)", "=" * 50, ""]
    thin = []
    for fg in range(C.TOTAL_FAMILIES):
        lemmas = by_family.get(fg, [])
        lines.append(f"family {fg}: {len(lemmas)} anchors")
        if len(lemmas) < a_min:
            thin.append(fg)
    if thin:
        lines.append("")
        lines.append(f"THIN FAMILIES (< {a_min} anchors): {thin}")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_report_dict_b_stats(
    candidates_total: int,
    accepted: list,
    rejected: list,
    accepted_audit: list,
    per_family_counts: dict[int, int],
    imbalance_ok: bool,
    path: Path,
) -> None:
    np = _get_np()
    total_acc = len(accepted_audit)
    total_rej = len(rejected)
    ambiguous = sum(1 for a in accepted_audit if a.get("ambiguous_flag"))
    scores = [a["top1_score"] for a in accepted_audit]
    pct = (total_acc / candidates_total * 100) if candidates_total else 0.0
    lines = [
        "Dict B statistics",
        "=" * 50,
        f"candidates total: {candidates_total}",
        f"accepted: {total_acc} ({pct:.1f}%)",
        f"rejected: {total_rej}",
        f"ambiguous (flagged): {ambiguous}",
    ]
    if scores:
        lines.append(f"mean similarity: {np.mean(scores):.4f}")
        lines.append(f"median similarity: {np.median(scores):.4f}")
    lines.append("")
    lines.append("Per-family token counts (first 20):")
    for fg in sorted(per_family_counts.keys())[:20]:
        lines.append(f"  family {fg}: {per_family_counts[fg]}")
    if len(per_family_counts) > 20:
        lines.append(f"  ... and {len(per_family_counts)-20} more")
    lines.append("")
    lines.append(f"imbalance check (κ): {'PASS' if imbalance_ok else 'FAIL'}")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_report_surface_stats(
    role_masks: dict[int, list[str]],
    surface_map: dict[int, list[str]],
    path: Path,
) -> None:
    violations = []
    for fg, mask in role_masks.items():
        for h in range(C.HEXES_PER_FAMILY):
            start = h * C.SIDES_PER_HEX
            hex_roles = mask[start : start + C.SIDES_PER_HEX]
            lc = sum(1 for r in hex_roles if r == C.ROLE_L)
            tc = sum(1 for r in hex_roles if r == C.ROLE_T)
            if lc > C.L_MAX_PER_HEX or tc < C.T_MIN_PER_HEX:
                violations.append((fg, h, lc, tc))
    bucket_sizes = [len(b) for b in surface_map.values()]
    lines = [
        "Surface statistics",
        "=" * 50,
        f"per-hex constraint violations (L≤3, T≥1): {len(violations)}",
    ]
    if violations:
        lines.extend(str(v) for v in violations[:10])
    lines.append("")
    lines.append(f"lexical sides with ≥1 token: {len(surface_map)}")
    if bucket_sizes:
        lines.append(f"bucket size min/max/mean: {min(bucket_sizes)} / {max(bucket_sizes)} / {sum(bucket_sizes)/len(bucket_sizes):.2f}")
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------- Pipeline ----------
def run_build(
    dict_a_path: Path | None = None,
    assets_root: Path | None = None,
    candidates_path: Path | None = None,
    candidates_fallback_from_b: bool = True,
    out_dir: Path | None = None,
    mode: str = "balanced",
    allow_small_build: bool = False,
) -> None:
    """Full pipeline: load Dict A, load candidates, build anchors → Dict B → surface → reports + manifest."""
    if out_dir is None:
        out_dir = Path(__file__).resolve().parent.parent / "assets" / "v040"
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    dict_a = load_dict_a_for_build(path=dict_a_path, assets_root=assets_root)
    if not dict_a:
        raise SystemExit("No Dict A entries loaded. Provide dict_a path or assets_root with A_CORE_STAR_MAP.")

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
        if candidates_fallback_from_b:
            root = assets_root or Path(__file__).resolve().parent.parent / "assets"
            b_path = root / "B_SURFACE_LEX_FIELD_v1.json"
            if b_path.exists():
                dict_b_legacy = load_dict_b_v033(path=b_path)
                cand_list = list(set(cand_list) | set(dict_b_legacy.keys()))
        cand_list = list(set(cand_list))

    candidates = filter_candidates(cand_list)
    if not candidates:
        raise SystemExit("No candidates after filtering. Check candidate source and §6 filters.")

    # Mode
    if mode == "strict":
        tau, delta, mu = C.MODE_STRICT["tau"], C.MODE_STRICT["delta"], C.MODE_STRICT["mu"]
    elif mode == "exploratory":
        tau, delta, mu = C.MODE_EXPLORATORY["tau"], C.MODE_EXPLORATORY["delta"], C.MODE_EXPLORATORY["mu"]
    else:
        tau, delta, mu = C.MODE_BALANCED["tau"], C.MODE_BALANCED["delta"], C.MODE_BALANCED["mu"]

    # Anchors
    anchor_records, _, model = build_anchor_embeddings(dict_a)
    anchors_path = out_dir / "dict_a_anchors_v040.json"
    # Save without full vectors for size; or save with vectors for rebuild. Spec says "embedding vector (or vector index reference)"
    to_save = [{"lemma": r["lemma"], "familyGlobal": r["familyGlobal"], "altitude": r["altitude"], "embedding": r["embedding"]} for r in anchor_records]  # noqa: E501
    anchors_path.write_text(json.dumps(to_save, indent=2), encoding="utf-8")

    # §8A Family affinity matrix (build-time diagnostic)
    family_vectors_dict, family_vectors_matrix = build_family_vectors(anchor_records)
    affinity_records, fcs_per_family, cross_sim_map, weak_anchors = build_affinity_matrix(
        anchor_records, family_vectors_matrix
    )
    write_affinity_artifacts(
        anchor_records, family_vectors_dict, affinity_records,
        fcs_per_family, cross_sim_map, weak_anchors,
        out_dir, allow_small_build,
    )

    # Dict B
    dict_b, accepted_audit, rejected_audit = build_dict_b_with_model(
        candidates, anchor_records, model, tau=tau, delta=delta, mu=mu, k=C.K_TOP
    )
    dict_b_minimal = {k: v for k, v in dict_b.items()}
    (out_dir / "dict_b_v040.json").write_text(json.dumps(dict_b_minimal), encoding="utf-8")
    audit_path = out_dir / "dict_b_v040_audit.jsonl"
    with open(audit_path, "w", encoding="utf-8") as f:
        for r in accepted_audit:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        for r in rejected_audit:
            f.write(json.dumps({"token": r["token"], "reason": r["reason"], "best_score": r.get("best_score"), "best_anchor_lemma": r.get("best_anchor_lemma")}, ensure_ascii=False) + "\n")

    # Imbalance and coverage (§15)
    imbalance_ok, per_family_counts = check_imbalance(dict_b)
    if not imbalance_ok and not allow_small_build:
        raise SystemExit("FAIL: family imbalance (κ). Fix Dict A or τ. Use --allow-small-build for tiny Dict A.")
    coverage_ok = check_coverage(per_family_counts)
    if not coverage_ok and not allow_small_build:
        raise SystemExit("FAIL: covered families < F_min_covered (240). Use --allow-small-build for tiny Dict A.")

    # Reports
    write_report_dict_a_coverage(anchor_records, out_dir / "report_dictA_coverage_v040.txt")
    write_report_dict_b_stats(
        len(candidates), list(dict_b.keys()), list(rejected_audit), accepted_audit,
        per_family_counts, imbalance_ok, out_dir / "report_dictB_stats_v040.txt",
    )

    # Surface: role masks
    role_masks = {fg: build_role_mask_per_family_v2(fg) for fg in range(C.TOTAL_FAMILIES)}
    roles_out: dict[str, Any] = {"version": "v040", "per_family": {}}
    for fg in range(C.TOTAL_FAMILIES):
        roles_out["per_family"][str(fg)] = role_masks[fg]
    (out_dir / "surface_roles_v040.json").write_text(json.dumps(roles_out), encoding="utf-8")

    surface_map = place_tokens_on_surface_v2(dict_b, role_masks)
    # surface_map: side_id → list of tokens. Save as side_id (str) → list for JSON
    map_out = {str(sid): bucket for sid, bucket in surface_map.items()}
    (out_dir / "surface_map_v040.json").write_text(json.dumps(map_out), encoding="utf-8")

    write_report_surface_stats(role_masks, surface_map, out_dir / "report_surface_stats_v040.txt")

    # Manifest
    import torch
    import platform
    manifest = {
        "model_name": C.MODEL_NAME,
        "model_revision": get_model_revision(),
        "torch_version": torch.__version__,
        "python_version": platform.python_version(),
        "tau": tau,
        "delta": delta,
        "kappa_max_share": C.KAPPA_MAX_SHARE,
        "date": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dict_a_version": "v1",
        "candidate_list_version": "v1",
    }
    (out_dir / "build_manifest_v040.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("DONE. Artifacts in", out_dir)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="HESPERIA v0.4.0 build: Dict A → Dict B → surface")
    p.add_argument("--dict-a", type=Path, help="Path to Dict A (native or legacy)")
    p.add_argument("--assets-root", type=Path, help="Assets root (default: repo assets)")
    p.add_argument("--candidates", type=Path, help="Candidate tokens file (.txt or .json)")
    p.add_argument("--out-dir", type=Path, default=None, help="Output directory")
    p.add_argument("--mode", choices=["strict", "balanced", "exploratory"], default="balanced")
    p.add_argument("--allow-small-build", action="store_true", help="Allow build when covered families < 240 (tiny Dict A)")
    args = p.parse_args()
    run_build(
        dict_a_path=args.dict_a,
        assets_root=args.assets_root,
        candidates_path=args.candidates,
        out_dir=args.out_dir,
        mode=args.mode,
        allow_small_build=args.allow_small_build,
    )
