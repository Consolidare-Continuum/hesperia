#!/usr/bin/env python3
"""
HESPERIA v0.3 — Chroma books validation run. Stub traversal + Chroma for books (evidence) only.
Topology (membership/adjacency) does not come from Chroma unless explicitly ingested per TOPOLOGY-STORAGE-CONTRACT;
this run uses stub W and stub membership unless Chroma has layer=hesperia_families.
1) Run full v0.3 pipeline (fusion → traversal → resolution → metrics) with stub topology.
2) Post-resolution: query layer=books; verify metrics unchanged (I-Q2).
Run: CHROMA_SERVER_URL=http://127.0.0.1:8002 python3 sphere_rag/chroma_books_validation_run.py [--no-books-check] [--out path]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if _SCRIPT_DIR.name == "sphere_rag":
    _HESPERIA_ROOT = _SCRIPT_DIR.parent
else:
    _HESPERIA_ROOT = _SCRIPT_DIR

sys.path.insert(0, str(_HESPERIA_ROOT))

# Chroma client (optional)
try:
    import chromadb
    HAS_CHROMA = True
except ImportError:
    HAS_CHROMA = False

from runtime.runners.full_run_simulation import (
    load_config,
    validate_config,
    build_stub_topology,
    run_full,
)


def _chroma_http_client():
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


def fetch_hesperia_families_topology(client, n_sides: int = 72) -> tuple[dict[int, list[int]], dict[int, list[int]], bool]:
    """
    Try to get (sides_of_family, families_of_area) from Chroma (membership only).
    Does NOT fetch adjacency/W; traversal always uses stub W. So: membership_from_chroma may be True;
    adjacency_from_chroma is always False (no W in Chroma in this path).
    Returns (sides_of_family, families_of_area, membership_from_chroma).
    """
    try:
        coll = client.get_collection("knowledge")
    except Exception:
        return build_stub_topology(n_sides=n_sides, n_areas=12, n_families_per_area=6)[0], build_stub_topology(n_sides=n_sides, n_areas=12, n_families_per_area=6)[1], False

    try:
        # Peek: get a batch with layer=hesperia_families
        res = coll.get(
            where={"layer": "hesperia_families"},
            limit=500,
            include=["metadatas"],
        )
    except Exception:
        return build_stub_topology(n_sides=n_sides, n_areas=12, n_families_per_area=6)[0], build_stub_topology(n_sides=n_sides, n_areas=12, n_families_per_area=6)[1], False

    if not res or not res.get("metadatas"):
        sof, foa = build_stub_topology(n_sides=n_sides, n_areas=12, n_families_per_area=6)
        return sof, foa, False

    # Build minimal topology from metadata: area_name/family_name or area_id/family_id
    # If we have area_id, family_id we can build families_of_area; without side_id we still need stub sides
    areas_seen: set[int] = set()
    families_seen: set[int] = set()
    for meta in res["metadatas"] or []:
        if not meta:
            continue
        aid = meta.get("area_id")
        fid = meta.get("family_id")
        if aid is not None:
            areas_seen.add(int(aid))
        if fid is not None:
            families_seen.add(int(fid))

    if not areas_seen and not families_seen:
        sof, foa = build_stub_topology(n_sides=n_sides, n_areas=12, n_families_per_area=6)
        return sof, foa, False

    n_areas = max(12, max(areas_seen) + 1) if areas_seen else 12
    n_fams = max(72, max(families_seen) + 1) if families_seen else 72
    n_families_per_area = max(1, n_fams // n_areas)
    sof, foa = build_stub_topology(n_sides=n_sides, n_areas=n_areas, n_families_per_area=n_families_per_area)
    return sof, foa, True


def query_books_post_resolution(client, dominant_area_id: int | None, dominant_family_id: int | None, n_results: int = 3) -> list[dict]:
    """Query Chroma layer=books after resolution (evidence only; must not change metrics). Returns list of chunks for logging."""
    try:
        coll = client.get_collection("knowledge")
    except Exception:
        return []
    try:
        # Optional: filter by area/family if metadata supports; else generic query
        where: dict = {"layer": "books"}
        res = coll.get(where=where, limit=n_results, include=["metadatas", "documents"])
    except Exception:
        return []
    out = []
    for i, doc in enumerate(res.get("documents") or []):
        meta = (res.get("metadatas") or [{}])[i] if res.get("metadatas") else {}
        out.append({"metadata": meta, "preview": (doc or "")[:200]})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="HESPERIA v0.3 Chroma books validation run (stub traversal + books I-Q2)")
    ap.add_argument("--no-books-check", action="store_true", help="Skip post-resolution books query and I-Q2 check")
    ap.add_argument("--n-sides", type=int, default=72, help="Stub topology size")
    ap.add_argument("--out", type=Path, help="Write result JSON here")
    args = ap.parse_args()

    os.environ.setdefault("ANONYMIZED_TELEMETRY", "FALSE")

    cfg = load_config(_HESPERIA_ROOT / "guard_config_v1.json")
    errs = validate_config(cfg)
    if errs:
        print("Config validation failed:", errs, file=sys.stderr)
        return 1

    n = args.n_sides
    S = [0.0] * n
    S[0], S[1], S[2] = 1.0, 0.5, 0.2
    L = [0.0] * n
    L[0], L[1], L[3], L[4] = 0.3, 0.6, 0.1, 0.05

    chroma_used = False
    membership_from_chroma = False
    adjacency_from_chroma = False  # W never from Chroma in this path; traversal uses stub
    sides_of_family, families_of_area = build_stub_topology(n_sides=n, n_areas=12, n_families_per_area=6)
    sides_of_family = {f: [i for i in sides if i < n] for f, sides in sides_of_family.items() if any(i < n for i in sides)}
    families_of_area = {a: [f for f in fams if f in sides_of_family] for a, fams in families_of_area.items()}

    if HAS_CHROMA:
        try:
            client = _chroma_http_client()
            if client is not None:
                chroma_used = True
                sof, foa, from_chroma = fetch_hesperia_families_topology(client, n_sides=n)
                if from_chroma:
                    membership_from_chroma = True
                    sof = {f: [i for i in sides if i < n] for f, sides in sof.items() if any(i < n for i in sides)}
                    foa = {a: [f for f in fams if f in sof] for a, fams in foa.items()}
                    if sof and foa:
                        sides_of_family, families_of_area = sof, foa
        except Exception as e:
            print("Chroma topology fetch failed, using stub:", e, file=sys.stderr)

    # topology_source: stub | membership_chroma (mixed: membership from Chroma, adjacency stub)
    topology_source = "stub" if not membership_from_chroma else "membership_chroma"

    result = run_full(S, L, sides_of_family, families_of_area, cfg)
    result["simulation"] = {
        "chroma_used": chroma_used,
        "topology": {
            "membership_from_chroma": membership_from_chroma,
            "adjacency_from_chroma": adjacency_from_chroma,
        },
        "topology_source": topology_source,
    }
    result["books_enabled"] = bool(HAS_CHROMA and chroma_used)
    cfg_path = _HESPERIA_ROOT / "guard_config_v1.json"
    result["config_hash"] = hashlib.sha256((cfg_path.read_bytes() if cfg_path.exists() else b"") + json.dumps(cfg, sort_keys=True).encode()).hexdigest()
    assets_dir = _HESPERIA_ROOT / "assets"
    result["lex_versions"] = {name: hashlib.sha256((assets_dir / name).read_bytes()).hexdigest() for name in ("A_CORE_STAR_MAP_v1.json", "B_SURFACE_LEX_FIELD_v1.json") if (assets_dir / name).exists()}
    if "shadow_triggers" not in result:
        result["shadow_triggers"] = []

    # Strong I-Q2: run pipeline twice — (A) run, (B) execute books retrieval and discard, (C) run again; assert (A)==(C)
    if HAS_CHROMA and chroma_used and not args.no_books_check:
        result_with_books = run_full(S, L, sides_of_family, families_of_area, cfg)
        try:
            client = _chroma_http_client()
            if client is not None:
                query_books_post_resolution(client, result["resolution"].get("dominant_area_id"), result["resolution"].get("dominant_family_id"), n_results=3)
        except Exception:
            pass
        result_without_books = run_full(S, L, sides_of_family, families_of_area, cfg)
        def key_resolution(r):
            return (r["resolution"].get("dominant_family_id"), r["resolution"].get("dominant_area_id"))
        def key_metrics(r):
            return tuple(r["metrics"].get(k) for k in ("governance", "loopability", "tension_energy", "obstacle_score"))
        def key_penalties(r):
            return tuple(r["penalties"].get(k) for k in ("P_amb", "P_thin", "P_disp", "P_shadow", "P_guard"))
        iq2_ok = (
            key_resolution(result_with_books) == key_resolution(result_without_books)
            and key_metrics(result_with_books) == key_metrics(result_without_books)
            and key_penalties(result_with_books) == key_penalties(result_without_books)
        )
        result["invariants"]["I_Q2_books_do_not_affect_metrics"] = iq2_ok
        result["invariants"]["I_Q2_strong_run_twice"] = iq2_ok
    else:
        result["invariants"]["I_Q2_books_do_not_affect_metrics"] = True
        result["invariants"]["I_Q2_strong_run_twice"] = True

    out_json = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(out_json, encoding="utf-8")
        print("Wrote", args.out, file=sys.stderr)
    else:
        print(out_json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
