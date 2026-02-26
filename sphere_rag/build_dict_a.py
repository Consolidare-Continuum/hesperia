#!/usr/bin/env python3
"""
HESPERIA v0.6 — Build Dict A as calibrated 288-dimensional semantic field.
Replaces v0.5 (failed). Build-time deterministic generation; runtime immutable artifact.
Pipeline: family anchors → embed tokens → raw similarity → family-wise calibration → temperature softmax → metrics.
Output: assets/v06/dict_a_v06.jsonl, family_prior_v06.json, dict_a_v06.sha256.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

TOTAL_FAMILIES = 288
TAU = 0.35
EPS_SIGMA = 1e-8
SUM_TOL = 1e-6
SIGMA_MIN = 1e-6  # fail if σ_f below this
TOP_K = 32
# Strong signal thresholds (spec)
MARGIN_STRONG = 0.06
MASS_TOP8_STRONG = 0.55
ENTROPY_STRONG = 3.6

MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
MODEL_REVISION = os.environ.get("HESPERIA_V06_MODEL_REVISION")  # fixed hash for freeze
FAMILY_SPEC_PATH = REPO / "hesperia_lex" / "curated" / "FAMILY_SPEC_v0_6.json"
OUT_DIR = REPO / "assets" / "v06"


def _normalize_l2(vec: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [x / n for x in vec]


def _cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _load_family_spec(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        spec = json.load(f)
    if not isinstance(spec, list) or len(spec) != TOTAL_FAMILIES:
        raise SystemExit(f"FAIL: family spec must be list of {TOTAL_FAMILIES} entries, got {type(spec).__name__} len={len(spec) if isinstance(spec, list) else 'N/A'}")
    return spec


def _anchor_text(entry: dict) -> str:
    label = entry.get("label", "")
    core = entry.get("core_definition", "")
    pos = entry.get("positive_axis", "")
    neg = entry.get("negative_axis", "")
    ex = entry.get("central_examples", "")
    if isinstance(ex, list):
        ex = ", ".join(str(x) for x in ex)
    return f"{label}. {core}. Positive: {pos}. Negative: {neg}. Examples: {ex}"


def _load_vocabulary(assets_root: Path, vocab_path: Path | None) -> list[str]:
    """Canonical vocabulary: from Dict A keys (existing pipeline) or explicit vocab file."""
    if vocab_path and vocab_path.exists():
        raw = vocab_path.read_text(encoding="utf-8")
        if vocab_path.suffix == ".json":
            data = json.loads(raw)
            tokens = data if isinstance(data, list) else list(data.keys())
        else:
            tokens = [line.strip() for line in raw.splitlines() if line.strip()]
        return sorted(set(tokens))
    # Fallback: Dict A v0.4 keys (try assets_root then hesperia_lex/frozen)
    from sphere_rag.attribution_shared import load_dict_a_v033
    for root in (assets_root, REPO / "hesperia_lex" / "frozen", REPO / "assets"):
        dict_a = load_dict_a_v033(assets_root=root)
        if dict_a:
            return sorted(dict_a.keys())
    raise SystemExit("FAIL: no vocabulary. Provide --vocab file or Dict A under assets/ or hesperia_lex/frozen/.")


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Build Dict A v0.6 — full 288-family field")
    ap.add_argument("--family-spec", type=Path, default=FAMILY_SPEC_PATH, help="Path to FAMILY_SPEC_v0_6.json")
    ap.add_argument("--vocab", type=Path, default=None, help="Canonical vocabulary (.txt or .json); default: Dict A keys")
    ap.add_argument("--assets", type=Path, default=REPO / "assets", help="Assets root for Dict A fallback")
    ap.add_argument("--out-dir", type=Path, default=OUT_DIR, help="Output directory")
    ap.add_argument("--save-calibration-stats", action="store_true", help="Write calibration_stats_v06.json (mu_f, sigma_f) for audit")
    ap.add_argument("--stability-guards", action="store_true", help="τ=0.5, ε=1e-6 for σ_f, clip z to [-10,10] (Phase 2 clean rebuild)")
    args = ap.parse_args()

    tau = 0.5 if args.stability_guards else TAU
    eps_sigma = 1e-6 if args.stability_guards else EPS_SIGMA

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Step 1 — Build family anchors
    spec = _load_family_spec(Path(args.family_spec))
    import sentence_transformers as st
    import numpy as np
    kwargs = {}
    if MODEL_REVISION:
        kwargs["revision"] = MODEL_REVISION
    model = st.SentenceTransformer(MODEL_NAME, **kwargs)
    model.eval()

    anchor_texts = [_anchor_text(entry) for entry in spec]
    anchors_emb = model.encode(anchor_texts, normalize_embeddings=True)
    if hasattr(anchors_emb, "numpy"):
        anchors_emb = anchors_emb.numpy()
    anchors_emb = np.asarray(anchors_emb, dtype=np.float64)
    norms = np.linalg.norm(anchors_emb, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    anchors_emb = anchors_emb / norms
    if len(anchors_emb) != TOTAL_FAMILIES:
        raise SystemExit(f"FAIL: expected {TOTAL_FAMILIES} anchors, got {len(anchors_emb)}")

    # Step 2 — Embed all tokens
    vocab = _load_vocabulary(Path(args.assets), args.vocab)
    if not vocab:
        raise SystemExit("FAIL: empty vocabulary")
    token_emb = model.encode(vocab, normalize_embeddings=True)
    if hasattr(token_emb, "numpy"):
        token_emb = token_emb.numpy()
    token_emb = np.asarray(token_emb, dtype=np.float64)
    tnorms = np.linalg.norm(token_emb, axis=1, keepdims=True)
    tnorms = np.where(tnorms == 0, 1.0, tnorms)
    token_emb = token_emb / tnorms

    # Step 3 — Raw similarity matrix [tokens x 288]
    sim = np.dot(token_emb, anchors_emb.T)  # (V, 288)

    # Step 4 — Family-wise calibration
    mu_f = np.mean(sim, axis=0)
    sigma_f = np.std(sim, axis=0) + eps_sigma
    if np.any(sigma_f < SIGMA_MIN):
        raise SystemExit("FAIL: σ_f collapse (some σ_f < SIGMA_MIN)")
    z = (sim - mu_f) / sigma_f  # (V, 288)
    if args.stability_guards:
        z = np.clip(z, -10.0, 10.0)

    # Step 5 — Temperature softmax
    z_scaled = z / tau
    z_max = np.max(z_scaled, axis=1, keepdims=True)
    exp_z = np.exp(z_scaled - z_max)
    w = exp_z / np.sum(exp_z, axis=1, keepdims=True)
    if np.any(np.isnan(w)):
        raise SystemExit("FAIL: NaN in weights after softmax")
    sums = np.sum(w, axis=1)
    if np.any(np.abs(sums - 1.0) > SUM_TOL):
        raise SystemExit(f"FAIL: weight sum deviation > {SUM_TOL}")

    # Step 6 — Strong signal metrics per token
    n_tokens = len(vocab)
    family_prior_counts = np.zeros(TOTAL_FAMILIES)
    jsonl_path = out_dir / "dict_a_v06.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for i, token in enumerate(vocab):
            weights = w[i].tolist()
            sorted_idx = np.argsort(weights)[::-1]
            topk = [{"family_id": int(j), "w": round(weights[j], 8)} for j in sorted_idx[:TOP_K]]
            w1, w2 = weights[sorted_idx[0]], weights[sorted_idx[1]]
            margin_1_2 = float(w1 - w2)
            mass_top8 = float(sum(weights[sorted_idx[k]] for k in range(min(8, len(sorted_idx)))))
            ent = 0.0
            for wf in weights:
                if wf > 0:
                    ent -= wf * math.log(wf)
            nw = len(weights)
            w_sorted = sorted(weights)
            gini = 1.0 - 2.0 * sum((nw - k - 0.5) / nw * w_sorted[k] for k in range(nw)) if nw else 0.0
            strong = margin_1_2 >= MARGIN_STRONG and mass_top8 >= MASS_TOP8_STRONG and ent <= ENTROPY_STRONG
            family_prior_counts[sorted_idx[0]] += 1
            rec = {
                "token": token,
                "topk": topk,
                "metrics": {
                    "margin_1_2": round(margin_1_2, 6),
                    "mass_top8": round(mass_top8, 6),
                    "entropy": round(ent, 6),
                    "gini": round(gini, 6),
                    "strong": strong,
                },
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Family prior (normalized)
    total = float(np.sum(family_prior_counts))
    family_prior = (family_prior_counts / total).tolist() if total > 0 else [1.0 / TOTAL_FAMILIES] * TOTAL_FAMILIES
    prior_path = out_dir / "family_prior_v06.json"
    with open(prior_path, "w", encoding="utf-8") as f:
        json.dump({"family_prior": [round(p, 8) for p in family_prior]}, f, separators=(",", ":"))

    # Calibration stats for audit (Phase 1)
    if args.save_calibration_stats:
        cal_path = out_dir / "calibration_stats_v06.json"
        with open(cal_path, "w", encoding="utf-8") as f:
            json.dump({
                "mu_f": [round(float(x), 8) for x in mu_f],
                "sigma_f": [round(float(x), 8) for x in sigma_f],
            }, f, separators=(",", ":"))
        print(f"Written: {cal_path}")

    # SHA256
    payload = jsonl_path.read_bytes()
    sha = hashlib.sha256(payload).hexdigest()
    sha_path = out_dir / "dict_a_v06.sha256"
    sha_path.write_text(sha + "  dict_a_v06.jsonl\n", encoding="utf-8")

    print(f"Written: {jsonl_path} ({n_tokens} tokens)")
    print(f"Written: {prior_path}")
    print(f"Written: {sha_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
