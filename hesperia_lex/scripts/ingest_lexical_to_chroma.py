#!/usr/bin/env python3
"""
Ingest Dict A and Dict B into Chroma for agent query.

Recommended: use a dedicated collection hesperia_lex (Dict A/B only) to avoid mixing
with books or topology. If using a single collection (e.g. knowledge), enforce
hard filter by layer in every query; CI must ensure books retrieval cannot see
layer=hesperia_lex and lex queries cannot see layer=books.

Run from repo root: CHROMA_SERVER_URL=http://127.0.0.1:8002 python3 CLIENTS/hesperia/hesperia_lex/scripts/ingest_lexical_to_chroma.py
Abelard: run when lexical stack is updated; mass ingest = Abelard only.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

LEX_ROOT = Path(__file__).resolve().parent.parent
CURATED = LEX_ROOT / "curated"
os.environ.setdefault("ANONYMIZED_TELEMETRY", "FALSE")

def _parse_args():
    import argparse
    ap = argparse.ArgumentParser(description="Ingest Dict A/B into Chroma")
    ap.add_argument("--strict", action="store_true", help="Fail non-zero if Chroma unreachable or chromadb missing (CI/prod)")
    return ap.parse_args()

try:
    import chromadb
    from chromadb.utils import embedding_functions
except ImportError:
    chromadb = None

def _http_client():
    if chromadb is None:
        return None
    url = os.environ.get("CHROMA_SERVER_URL", "").strip()
    if not url:
        return None
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    parts = url.split(":", 1)
    host = parts[0] or "127.0.0.1"
    port = int(parts[1]) if len(parts) > 1 else 8002
    return chromadb.HttpClient(host=host, port=port)


def main() -> int:
    args = _parse_args()
    strict = getattr(args, "strict", False)

    if chromadb is None:
        if strict:
            print("chromadb not installed; --strict: fail.", file=sys.stderr)
            return 1
        print("chromadb not installed; skip Chroma ingest.", file=sys.stderr)
        return 0

    client = _http_client()
    if client is None:
        if strict:
            print("CHROMA_SERVER_URL not set; --strict: fail.", file=sys.stderr)
            return 1
        print("CHROMA_SERVER_URL not set; skip ingest.", file=sys.stderr)
        return 0

    a_path = CURATED / "A_CORE_STAR_MAP_v0_4_1_1.json"
    if not a_path.exists():
        a_path = CURATED / "A_CORE_STAR_MAP_v1.json"
    b_path = CURATED / "B_SURFACE_LEX_FIELD_v1.json"
    if not a_path.exists() or not b_path.exists():
        print("Curated A/B not found (default A: A_CORE_STAR_MAP_v0_4_1_1.json); run validation first.", file=sys.stderr)
        return 1

    with open(a_path, encoding="utf-8") as f:
        dict_a = json.load(f)
    with open(b_path, encoding="utf-8") as f:
        dict_b = json.load(f)

    dict_a = {k: v for k, v in dict_a.items() if not k.startswith("_") and isinstance(v, list)}
    dict_b = {k: v for k, v in dict_b.items() if not k.startswith("_") and isinstance(v, dict)}

    try:
        coll = client.get_or_create_collection("knowledge", metadata={"description": "Knowledge + lexical"})
    except Exception:
        coll = client.create_collection("knowledge")

    # Build documents for Dict A: one per lemma
    ids_a = []
    docs_a = []
    meta_a = []
    for lemma, entries in dict_a.items():
        ids_a.append(f"lex_a_{lemma}")
        docs_a.append(f"lemma {lemma} maps to side_ids: " + ", ".join(str(e.get("side_id")) for e in entries))
        meta_a.append({"layer": "hesperia_lex", "dict": "A", "lemma": lemma})

    # Build documents for Dict B: one per side_id
    ids_b = []
    docs_b = []
    meta_b = []
    for side_id, obj in dict_b.items():
        canonical = obj.get("canonical_lemma", "")
        aliases = obj.get("aliases", [])
        al_str = ", ".join(a.get("alias", a) if isinstance(a, dict) else a for a in aliases)
        ids_b.append(f"lex_b_{side_id}")
        docs_b.append(f"side_id {side_id} canonical {canonical} aliases: {al_str}")
        meta_b.append({"layer": "hesperia_lex", "dict": "B", "side_id": str(side_id), "canonical_lemma": canonical})

    # Upsert in batches (Chroma may require embedding; if collection has embedding_fn we need to add with embeddings or let it embed)
    all_ids = ids_a + ids_b
    all_docs = docs_a + docs_b
    all_meta = meta_a + meta_b
    if not all_ids:
        print("No lexical data to ingest.", file=sys.stderr)
        return 0
    try:
        coll.upsert(ids=all_ids, documents=all_docs, metadatas=all_meta)
        print("Ingested", len(ids_a), "Dict A chunks,", len(ids_b), "Dict B chunks into Chroma (layer=hesperia_lex).")
    except Exception as e:
        print("Chroma upsert failed (collection may use embedding):", e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
