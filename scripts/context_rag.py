#!/usr/bin/env python3
"""Context RAG: single entry point for context packet (calculable + optional retrieval + coherence hints).
Reuses matrix_run for calculable block; optional Chroma query for families (layer=hesperia_families).
Schema: governance/CONTEXT-RAG-PACKET-SCHEMA.md. Proposal: governance/HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md.
Run from repo root: python cluster/chroma-server/context_rag.py [--path] [--start N] [--direction 1|-1] [--steps N] [--query "..."] [--area_id N] [--family_name X] [--chroma] [--data-dir PATH]
Output: JSON context packet to stdout.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from sphere_rag.guards import run_sigma_preflight

# Canonical areas for coherence_hints (must match matrix_run)
CANONICAL_AREAS = [
    "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
    "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
]
DEFAULT_FAMILIES_LIMIT = 20
DEFAULT_BOOKS_CHUNKS_LIMIT = 10


def _run_matrix_run(start: int, direction: int, steps: int, chroma: bool, data_dir: str) -> dict | None:
    """Run matrix_run.py and return parsed JSON calculable block. Returns None on failure."""
    cmd = [
        sys.executable,
        str(SCRIPT_DIR / "matrix_run.py"),
        "--start", str(start),
        "--direction", str(direction),
        "--steps", str(steps),
    ]
    if chroma:
        cmd.append("--chroma")
    if data_dir:
        cmd.append("--data-dir")
        cmd.append(data_dir)
    env = os.environ.copy()
    env.setdefault("PYTHONPATH", str(REPO_ROOT))
    try:
        out = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=30,
            env=env,
        )
        if out.returncode != 0:
            return None
        return json.loads(out.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None


def _add_l_full_from_activation(loopability: dict, activation_path: str, geometry: dict) -> None:
    """When activation data file exists, compute L_full per 40_POLICY §11 and add to loopability.
    Activation JSON: {"G_F": N} -> L_full = N / STEPS_PER_PASS; or {"L_full": value} for direct value.
    """
    path = Path(activation_path)
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError):
        return
    steps_per_pass = int(geometry.get("STEPS_PER_PASS", 12)) or 12
    if "L_full" in data:
        try:
            loopability["L_full"] = float(data["L_full"])
        except (TypeError, ValueError):
            pass
    elif "G_F" in data:
        try:
            g_f = int(data["G_F"])
            loopability["L_full"] = round(g_f / steps_per_pass, 6)
        except (TypeError, ValueError):
            pass


def _build_coherence_hints(calculable: dict) -> dict:
    """Derive coherence_hints from calculable block."""
    road = calculable.get("road_coordinates", [])
    path_params = calculable.get("path_params", {})
    border_passings = calculable.get("border_passings", {})
    area_passings = border_passings.get("area_border_passings", [])
    family_passings = border_passings.get("family_border_passings", [])
    traversal_length = calculable.get("traversal_length", 0)
    is_loop = calculable.get("is_loop", False)
    direction = path_params.get("direction", 1)

    # Current position: last step on path
    current_area_id = road[-1]["area_id"] if road else path_params.get("start_area_id", 0)
    area_name = CANONICAL_AREAS[current_area_id] if 0 <= current_area_id < 12 else ""

    # Adjacent areas on ring (left = CCW, right = CW)
    left_id = (current_area_id - 1 + 12) % 12
    right_id = (current_area_id + 1) % 12
    suggested_adjacent_areas = [
        {"area_id": left_id, "area_name": CANONICAL_AREAS[left_id], "direction": "CCW"},
        {"area_id": right_id, "area_name": CANONICAL_AREAS[right_id], "direction": "CW"},
    ]

    if traversal_length == 12 and is_loop and direction == 1:
        traversal_summary = "one full ring CW"
    elif traversal_length == 12 and is_loop and direction == -1:
        traversal_summary = "one full ring CCW"
    else:
        start_area = path_params.get("start_area_id", 0)
        dir_label = "CW" if direction == 1 else "CCW"
        traversal_summary = f"{traversal_length} steps from area {start_area} ({CANONICAL_AREAS[start_area]}) {dir_label}"

    border_passings_count = {
        "area_border_passings": len(area_passings),
        "family_border_passings": len(family_passings),
    }

    return {
        "current_area_id": current_area_id,
        "current_area_name": area_name,
        "suggested_adjacent_areas": suggested_adjacent_areas,
        "traversal_summary": traversal_summary,
        "border_passings_count": border_passings_count,
    }


def _build_observability(calculable: dict, safeguard_events_count: int | None = None) -> dict:
    """Build observability block (v0.1): read-only telemetry; no engine modification.
    Ref: projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md.
    """
    road = calculable.get("road_coordinates", [])
    path_params = calculable.get("path_params", {})
    border_passings = calculable.get("border_passings", {})
    traversal_length = calculable.get("traversal_length", 0) or len(road)
    direction = path_params.get("direction", 1)

    # loopability_band: from L_full (calculable.loopability); classification only
    loopability = calculable.get("loopability", {})
    l_full = loopability.get("L_full")
    if l_full is None:
        loopability_band = "unknown"
    elif l_full >= 0.6:
        loopability_band = "stable"
    elif l_full > 0.4:
        loopability_band = "transitional"
    else:
        loopability_band = "unstable"

    # entropy_metric = unique_areas_visited / steps (report only)
    unique_areas = len({r["area_id"] for r in road}) if road else 0
    entropy_metric = round(unique_areas / traversal_length, 6) if traversal_length else 0.0

    # border_passings_count (same shape as coherence_hints)
    area_passings = border_passings.get("area_border_passings", [])
    family_passings = border_passings.get("family_border_passings", [])
    border_passings_count = {
        "area_border_passings": len(area_passings),
        "family_border_passings": len(family_passings),
    }

    # ring_distance_from_start: area units along ring from start to current
    start_area_id = path_params.get("start_area_id", 0)
    current_area_id = road[-1]["area_id"] if road else start_area_id
    ring_distance_from_start = ((current_area_id - start_area_id) * direction) % 12

    out = {
        "loopability_band": loopability_band,
        "entropy_metric": entropy_metric,
        "border_passings_count": border_passings_count,
        "direction": direction,
        "ring_distance_from_start": ring_distance_from_start,
        "safeguard_events_count": safeguard_events_count if safeguard_events_count is not None else 0,
    }
    return out


def _query_families_chroma(
    query_text: str | None,
    area_id: int | None,
    family_name: str | None,
    limit: int,
) -> list[dict]:
    """Query Chroma layer=hesperia_families. Returns list of {metadata + document text}."""
    try:
        from agent_mcp_knowledge.store import get_client, get_collection
        client = get_client()
        coll = get_collection(client)
        where: dict = {"layer": "hesperia_families"}
        if area_id is not None:
            where["area_id"] = area_id
        if family_name is not None:
            where["family_name"] = family_name

        if query_text and query_text.strip():
            res = coll.query(
                query_texts=[query_text.strip()],
                n_results=min(limit, 20),
                where=where,
                include=["metadatas", "documents"],
            )
            ids = res.get("ids", [[]])[0]
            metadatas = res.get("metadatas", [[]])[0]
            documents = res.get("documents", [[]])[0]
        else:
            got = coll.get(
                where=where,
                include=["metadatas", "documents"],
                limit=limit,
            )
            ids = got.get("ids", [])
            metadatas = got.get("metadatas", [])
            documents = got.get("documents", [])

        families = []
        for i, mid in enumerate(ids):
            meta = (metadatas[i] if i < len(metadatas) else {}) or {}
            doc = (documents[i] if i < len(documents) else "") or ""
            families.append({
                "id": mid,
                "area_id": meta.get("area_id"),
                "area_name": meta.get("area_name"),
                "family_name": meta.get("family_name"),
                "global_id": meta.get("global_id"),
                "concept": meta.get("concept"),
                "book_refs": meta.get("book_refs"),  # JSON array string "Author — Title"
                "document": doc[:500] if doc else None,
            })
        return families
    except Exception:
        return []


def _query_books_chunks(
    query_text: str,
    limit: int,
    bounding: dict,
) -> list[dict]:
    """Query Chroma layer=books; return chunks with bounding (area_name, family_name, concept)."""
    if not query_text or not query_text.strip():
        return []
    try:
        from agent_mcp_knowledge.store import query as store_query
        results = store_query(
            query_text=query_text.strip(),
            n_results=min(limit, 20),
            layer="books",
        )
        chunks = []
        for r in results:
            text = r.get("text", "")
            meta = r.get("metadata", {}) or {}
            chunks.append({
                "text": text[:2000] if text else None,
                "source": meta.get("source"),
                "area_name": bounding.get("area_name"),
                "family_name": bounding.get("family_name"),
                "concept": bounding.get("concept"),
            })
        return chunks
    except Exception:
        return []


def main() -> int:
    sigma_status = run_sigma_preflight(strict=True)
    ap = argparse.ArgumentParser(
        description="Context RAG: return context packet (calculable + optional retrieval + coherence hints)"
    )
    ap.add_argument("--path", action="store_true", help="Include path/calculable (default: always true)")
    ap.add_argument("--start", type=int, default=0, help="Start area_id 0..11 (default 0)")
    ap.add_argument("--direction", type=int, default=1, choices=[1, -1], help="1=CW, -1=CCW (default 1)")
    ap.add_argument("--steps", type=int, default=12, help="Number of steps (default 12)")
    ap.add_argument("--query", type=str, default="", help="Optional query for retrieval (Chroma families)")
    ap.add_argument("--area_id", type=int, default=None, help="Filter retrieval by area_id 0..11")
    ap.add_argument("--family_name", type=str, default=None, help="Filter retrieval by family_name")
    ap.add_argument("--chroma", action="store_true", help="Use Chroma for matrix and/or retrieval")
    ap.add_argument("--data-dir", type=str, default="", help="Override data dir for CSV")
    ap.add_argument("--families-limit", type=int, default=DEFAULT_FAMILIES_LIMIT, help="Max families in retrieval (default 20)")
    ap.add_argument("--books-chunks-limit", type=int, default=DEFAULT_BOOKS_CHUNKS_LIMIT, help="Max books chunks in retrieval (default 10)")
    ap.add_argument("--activation", type=str, default="", help="Path to activation data JSON (G_F or L_full per 40_POLICY §11); when present, add L_full to calculable.loopability")
    args = ap.parse_args()

    data_dir = args.data_dir or os.environ.get("HESPERIA_DATA_DIR", str(REPO_ROOT / "CLIENTS" / "hesperia"))
    start = max(0, min(11, args.start))
    steps = max(1, args.steps)

    # 1. Calculable block (always; from matrix_run)
    calculable_raw = _run_matrix_run(start, args.direction, steps, args.chroma, data_dir)
    if calculable_raw is None:
        # Fallback: try without chroma
        calculable_raw = _run_matrix_run(start, args.direction, steps, False, data_dir)
    if calculable_raw is None:
        print(json.dumps({"error": "matrix_run failed (CSV missing or Chroma down)"}, indent=2), file=sys.stderr)
        return 1

    matrix_source = calculable_raw.get("matrix_source", "csv")
    loopability = dict(calculable_raw.get("loopability", {}))
    # When activation data exists: add L_full per 40_POLICY §11 (L_full = G_F[p] / STEPS_PER_PASS)
    if args.activation:
        _add_l_full_from_activation(loopability, args.activation, calculable_raw.get("geometry", {}))
    calculable = {
        "geometry": calculable_raw.get("geometry", {}),
        "hex_unit": calculable_raw.get("hex_unit", {}),
        "truth_unit": calculable_raw.get("truth_unit", {}),
        "borders": calculable_raw.get("borders", {}),
        "path_params": calculable_raw.get("path_params", {}),
        "road_coordinates": calculable_raw.get("road_coordinates", []),
        "border_passings": calculable_raw.get("border_passings", {}),
        "traversal_length": calculable_raw.get("traversal_length", 0),
        "is_loop": calculable_raw.get("is_loop", False),
        "loopability": loopability,
    }

    # 2. Coherence hints (from calculable)
    coherence_hints = _build_coherence_hints(calculable_raw)

    # 2b. Observability extension v0.1 (read-only; wrapper only; ref HESPERIA_OBSERVABILITY_EXTENSION_v0_1)
    observability = _build_observability(calculable)

    # 3. Optional retrieval
    retrieval: dict | None = None
    if args.query or args.area_id is not None or args.family_name is not None:
        families = _query_families_chroma(
            args.query or None,
            args.area_id,
            args.family_name,
            args.families_limit,
        )
        # Books chunks with bounding from first family (books–families wiring un-paused)
        chunks: list[dict] = []
        if families:
            first = families[0]
            bounding = {
                "area_name": first.get("area_name"),
                "family_name": first.get("family_name"),
                "concept": first.get("concept"),
            }
            query_for_books = args.query or ""
            if not query_for_books and (bounding.get("area_name") or bounding.get("family_name") or bounding.get("concept")):
                query_for_books = " ".join(
                    str(x) for x in (bounding.get("area_name"), bounding.get("family_name"), bounding.get("concept")) if x
                )
            if query_for_books:
                chunks = _query_books_chunks(query_for_books, args.books_chunks_limit, bounding)
        retrieval = {
            "families": families,
            "chunks": chunks,
        }

    # 4. Assemble packet
    packet = {
        "matrix_source": matrix_source,
        "sigma_status": sigma_status,
        "calculable": calculable,
        "coherence_hints": coherence_hints,
        "observability": observability,
    }
    if retrieval is not None:
        packet["retrieval"] = retrieval

    print(json.dumps(packet, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
