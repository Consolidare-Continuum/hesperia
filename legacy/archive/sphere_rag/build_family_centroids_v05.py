#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA v0.5 — Build-time family centroid freeze.
Load FAMILY_ANCHORS_v0_5.json, embed positive/negative anchors with all-mpnet-base-v2 (fixed revision),
compute normalized centroids per family, write FAMILY_CENTROIDS_v0_5.json + SHA256 freeze.
No runtime anchor embedding. CPU inference, deterministic.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

# Fixed model and revision for determinism. Set HESPERIA_V05_MODEL_REVISION for freeze.
MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
MODEL_REVISION = os.environ.get("HESPERIA_V05_MODEL_REVISION")  # e.g. commit hash; None = default branch
ANCHORS_PATH = REPO / "hesperia_lex" / "curated" / "FAMILY_ANCHORS_v0_5.json"
OUT_DIR = REPO / "hesperia_lex" / "frozen"
CENTROIDS_FILE = "FAMILY_CENTROIDS_v0_5.json"
SHA256_FILE = "FAMILY_CENTROIDS_v0_5.sha256"
TOTAL_FAMILIES = 288


def _normalize(vec: list[float]) -> list[float]:
    import math
    n = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [x / n for x in vec]


def main() -> int:
    if not ANCHORS_PATH.exists():
        print(f"Anchors not found: {ANCHORS_PATH}", file=sys.stderr)
        return 1
    with open(ANCHORS_PATH, encoding="utf-8") as f:
        anchors = json.load(f)
    if len(anchors) != TOTAL_FAMILIES:
        print(f"Expected {TOTAL_FAMILIES} families, got {len(anchors)}", file=sys.stderr)
        return 1

    import sentence_transformers as st
    import numpy as np
    kwargs = {}
    if MODEL_REVISION:
        kwargs["revision"] = MODEL_REVISION
    model = st.SentenceTransformer(MODEL_NAME, **kwargs)
    model.eval()

    centroids: dict[str, dict[str, list[float]]] = {}
    for key in sorted(anchors.keys(), key=int):
        fam = anchors[key]
        pos_texts = [t.strip() for t in fam["positive"] if t and isinstance(t, str)]
        neg_texts = [t.strip() for t in fam["negative"] if t and isinstance(t, str)]
        if not pos_texts or not neg_texts:
            print(f"Family {key}: need positive and negative anchors", file=sys.stderr)
            return 1
        pos_emb = model.encode(pos_texts, normalize_embeddings=True)
        neg_emb = model.encode(neg_texts, normalize_embeddings=True)
        pos_centroid = np.mean(pos_emb, axis=0)
        neg_centroid = np.mean(neg_emb, axis=0)
        pos_centroid = _normalize(pos_centroid.tolist())
        neg_centroid = _normalize(neg_centroid.tolist())
        centroids[key] = {"positive": pos_centroid, "negative": neg_centroid}

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / CENTROIDS_FILE
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(centroids, f, separators=(",", ":"))
    payload = out_path.read_bytes()
    sha = hashlib.sha256(payload).hexdigest()
    sha_path = OUT_DIR / SHA256_FILE
    sha_path.write_text(sha + "  " + CENTROIDS_FILE + "\n", encoding="utf-8")
    print(f"Written: {out_path}")
    print(f"SHA256:  {sha_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
