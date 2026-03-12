# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA v0.5 — Deterministic 288-family dense projection engine.
project_token(token) -> list of 288 floats. Uses frozen FAMILY_CENTROIDS_v0_5.json; embeds token only.
v0.5.1: temperature_sharpen() — softmax over |v| with sign preserved; reduces entropy, increases contrast.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
from typing import Any

# v0.5.1 temperature sharpening: default T=0.15; override via HESPERIA_TEMPERATURE
DEFAULT_TEMPERATURE = 0.15
EXP_CAP = 50.0  # cap m_f/T before exp to prevent overflow
# v0.5.2 contrast: gamma on magnitudes before softmax (m_f = |v_f|^gamma); default 2.0 for target band
DEFAULT_GAMMA = 2.0
GAMMA_MIN, GAMMA_MAX = 1.0, 3.0
# topK: 0 = off; 12–25 suggested for structural sparsity
DEFAULT_TOP_K = 0
TOP_K_MIN, TOP_K_MAX = 0, 288

try:
    from .invariant_catalog import TOTAL_FAMILIES
except ImportError:
    TOTAL_FAMILIES = 288

# Default centroid path (frozen artifact)
_DEFAULT_CENTROIDS_PATH = Path(__file__).resolve().parent.parent / "hesperia_lex" / "frozen" / "FAMILY_CENTROIDS_v0_5.json"
_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
_model: Any = None
_centroids: dict[str, dict[str, list[float]]] | None = None


def _get_model():
    global _model
    if _model is None:
        import sentence_transformers as st
        _model = st.SentenceTransformer(_MODEL_NAME)
        _model.eval()
    return _model


def load_centroids(centroids_path: Path | None = None) -> dict[str, dict[str, list[float]]]:
    global _centroids
    path = centroids_path or _DEFAULT_CENTROIDS_PATH
    if _centroids is None:
        with open(path, encoding="utf-8") as f:
            _centroids = json.load(f)
    return _centroids


def _cosine(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5 or 1.0
    nb = sum(y * y for y in b) ** 0.5 or 1.0
    return dot / (na * nb)


def _normalize(vec: list[float]) -> list[float]:
    n = sum(x * x for x in vec) ** 0.5 or 1.0
    return [x / n for x in vec]


def project_token(
    token: str,
    centroids_path: Path | None = None,
    clamp: bool = True,
) -> list[float]:
    """
    Embed token, normalize; for each family compute pos_sim - neg_sim; optional clamp to [-1, 1].
    Returns 288-dimensional attribution vector.
    """
    centroids = load_centroids(centroids_path)
    model = _get_model()
    # Single token: encode returns (1, dim) or (dim,)
    emb = model.encode([token.strip().lower() or " "], normalize_embeddings=True)
    if hasattr(emb, "tolist"):
        token_vec = emb[0].tolist() if emb.ndim > 1 else emb.tolist()
    else:
        token_vec = list(emb[0]) if len(emb) else [0.0] * 768
    token_vec = _normalize(token_vec)
    out: list[float] = []
    for key in sorted(centroids.keys(), key=int):
        pos_c = centroids[key]["positive"]
        neg_c = centroids[key]["negative"]
        pos_sim = _cosine(token_vec, pos_c)
        neg_sim = _cosine(token_vec, neg_c)
        value = pos_sim - neg_sim
        if clamp:
            value = max(-1.0, min(1.0, value))
        out.append(value)
    return out


def get_dim() -> int:
    return TOTAL_FAMILIES


def get_temperature() -> float:
    """T for sharpening; from HESPERIA_TEMPERATURE or default. Deterministic."""
    s = os.environ.get("HESPERIA_TEMPERATURE", "").strip()
    if not s:
        return DEFAULT_TEMPERATURE
    try:
        t = float(s)
        return max(1e-6, min(10.0, t))
    except ValueError:
        return DEFAULT_TEMPERATURE


def get_gamma() -> float:
    """Power amplification before softmax: m_f = |v_f|^gamma. From HESPERIA_GAMMA. Deterministic."""
    s = os.environ.get("HESPERIA_GAMMA", "").strip()
    if not s:
        return DEFAULT_GAMMA
    try:
        g = float(s)
        return max(GAMMA_MIN, min(GAMMA_MAX, g))
    except ValueError:
        return DEFAULT_GAMMA


def get_top_k() -> int:
    """After sharpening, keep only top K families (0 = off). From HESPERIA_TOP_K. Deterministic."""
    s = os.environ.get("HESPERIA_TOP_K", "").strip()
    if not s:
        return DEFAULT_TOP_K
    try:
        k = int(s)
        return max(TOP_K_MIN, min(TOP_K_MAX, k))
    except ValueError:
        return DEFAULT_TOP_K


def temperature_sharpen(v: list[float], T: float | None = None, gamma: float | None = None) -> list[float]:
    """
    Temperature-scaled softmax over absolute magnitudes; sign preserved. Deterministic.
    Step 1: v_f already clamped [-1,1]. Step 2: m_f = |v_f|^gamma, s_f = sign(v_f).
    Step 3: w_f = exp(min(m_f/T, EXP_CAP)) / sum(exp(...)). Step 4: v_f_sharp = s_f * w_f.
    Smaller T = sharper; gamma > 1 = more contrast without extreme T collapse.
    """
    if not v:
        return v[:]
    T = T if T is not None and T > 0 else get_temperature()
    g = gamma if gamma is not None and gamma >= 1.0 else get_gamma()
    n = len(v)
    m = [abs(x) for x in v]
    if g != 1.0:
        m = [x ** g for x in m]
    s = [1.0 if x >= 0 else -1.0 for x in v]
    scaled = [min(m[i] / T, EXP_CAP) for i in range(n)]
    exp_vals = [math.exp(scaled[i]) for i in range(n)]
    total = sum(exp_vals) or 1.0
    w = [exp_vals[i] / total for i in range(n)]
    return [s[i] * w[i] for i in range(n)]


def top_k_truncate(v: list[float], K: int | None = None) -> list[float]:
    """
    Keep only top K families by |value|; zero the rest. Deterministic (tie-break by index).
    K from get_top_k() if None. If K <= 0 or K >= len(v), return v unchanged.
    """
    if not v:
        return v[:]
    k = K if K is not None else get_top_k()
    if k <= 0 or k >= len(v):
        return v[:]
    indexed = [(i, abs(v[i]), v[i]) for i in range(len(v))]
    indexed.sort(key=lambda x: (-x[1], x[0]))
    out = [0.0] * len(v)
    for i in range(k):
        idx, _, val = indexed[i]
        out[idx] = val
    return out
