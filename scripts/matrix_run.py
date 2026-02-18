#!/usr/bin/env python3
"""Matrix run for agents context: address matrix, return calculable-for-model results.
Uses CSV (CLIENTS/hesperia/v0.1/hex_sphere_areas_families_ideal_proportions.csv) by default;
optional Chroma layer=hesperia_families when available.
Schema: governance/HESPERIA-FAMILIES-CHROMA-SCHEMA.md §6.
Run from repo root: python cluster/chroma-server/matrix_run.py [--start N] [--direction 1|-1] [--steps N] [--chroma]
Output: JSON to stdout (geometry, path, road_coordinates, border_passings, traversal_length, is_loop, etc.).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT_DIR = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# Geometry constants per schema §6.1 (20_GEOMETRY, 13_SPEC)
AREA_COUNT = 12
FAMILIES_PER_AREA = 24
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6
TOTAL_FAMILIES = AREA_COUNT * FAMILIES_PER_AREA
TOTAL_HEXES = TOTAL_FAMILIES * HEXES_PER_FAMILY
TOTAL_SIDES = TOTAL_HEXES * SIDES_PER_HEX
STEPS_PER_PASS = AREA_COUNT

CANONICAL_AREAS = [
    "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
    "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
]
DEFAULT_CSV = "CLIENTS/hesperia/v0.1/hex_sphere_areas_families_ideal_proportions.csv"


def area_left(area_id: int) -> int:
    return (area_id - 1 + AREA_COUNT) % AREA_COUNT


def area_right(area_id: int) -> int:
    return (area_id + 1) % AREA_COUNT


def area_at_step(start_area_id: int, direction: int, step: int) -> int:
    """Ring step per 40_POLICY §4.3."""
    return (start_area_id + direction * step + AREA_COUNT) % AREA_COUNT


def load_matrix_from_csv(csv_full: Path) -> list[tuple[int, str, str]]:
    """Load (global_id, area_name, family_name). global_id from CSV 'number' (1-based)."""
    if not csv_full.exists():
        alt = REPO_ROOT / DEFAULT_CSV
        csv_full = alt if alt.exists() else csv_full
    if not csv_full.exists():
        raise FileNotFoundError(f"CSV not found: {csv_full}")
    path = csv_full
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            if len(row) < 3:
                continue
            try:
                num = int(row[0].strip())
            except ValueError:
                continue
            area_name = row[1].strip()
            family_name = row[2].strip()
            if area_name and family_name:
                rows.append((num, area_name, family_name))
    return rows


def build_area_to_families(
    rows: list[tuple[int, str, str]],
) -> tuple[dict[int, list[tuple[int, str, str]]], dict[str, int]]:
    """Map area_id -> [(global_id, area_name, family_name), ...]; area_name -> area_id."""
    name_to_id = {a: i for i, a in enumerate(CANONICAL_AREAS)}
    by_area: dict[int, list[tuple[int, str, str]]] = {i: [] for i in range(AREA_COUNT)}
    for global_id, area_name, family_name in rows:
        aid = name_to_id.get(area_name, -1)
        if aid >= 0:
            by_area[aid].append((global_id, area_name, family_name))
    return by_area, name_to_id


def run_traversal(
    start_area_id: int,
    direction: int,
    steps: int,
    area_to_families: dict[int, list[tuple[int, str, str]]],
) -> tuple[list[dict], list[dict], list[dict]]:
    """Build path as list of (area_id, global_id, area_name, family_name).
    Returns (road_coordinates, area_border_passings, family_border_passings).
    """
    road = []
    area_passings = []
    family_passings = []
    prev_area, prev_global = None, None
    for step in range(steps):
        a_id = area_at_step(start_area_id, direction, step)
        fams = area_to_families.get(a_id, [])
        global_id, area_name, family_name = fams[0] if fams else (0, CANONICAL_AREAS[a_id], "")
        road.append({
            "step": step,
            "area_id": a_id,
            "global_id": global_id,
            "area_name": area_name,
            "family_name": family_name,
        })
        if prev_area is not None:
            if prev_area != a_id:
                area_passings.append({
                    "from_area_id": prev_area,
                    "to_area_id": a_id,
                    "from_area_name": CANONICAL_AREAS[prev_area],
                    "to_area_name": area_name,
                })
            if prev_global is not None and prev_global != global_id:
                family_passings.append({
                    "from_global_id": prev_global,
                    "to_global_id": global_id,
                    "from_area_id": prev_area,
                    "to_area_id": a_id,
                })
        prev_area, prev_global = a_id, global_id
    return road, area_passings, family_passings


def main() -> int:
    ap = argparse.ArgumentParser(description="Matrix run: return calculable-for-model results")
    ap.add_argument("--start", type=int, default=0, help="Start area_id 0..11 (default 0)")
    ap.add_argument("--direction", type=int, default=1, choices=[1, -1], help="1=CW, -1=CCW (default 1)")
    ap.add_argument("--steps", type=int, default=12, help="Number of steps (default 12 = one ring)")
    ap.add_argument("--chroma", action="store_true", help="Try Chroma first (fallback to CSV)")
    ap.add_argument("--data-dir", type=str, default="", help="Override data dir for CSV")
    args = ap.parse_args()

    data_dir = Path(args.data_dir) if args.data_dir else Path(os.environ.get("HESPERIA_DATA_DIR", str(REPO_ROOT / "CLIENTS" / "hesperia")))
    if not data_dir.is_absolute():
        data_dir = REPO_ROOT / data_dir
    csv_path = Path(DEFAULT_CSV)
    csv_full = data_dir / "v0.1" / csv_path.name if (data_dir / "v0.1").exists() else data_dir / csv_path

    matrix_source = "csv"
    rows: list[tuple[int, str, str]] = []

    if args.chroma:
        try:
            from agent_mcp_knowledge.store import get_client, get_collection
            client = get_client()
            coll = get_collection(client)
            got = coll.get(where={"layer": "hesperia_families"}, include=["metadatas"], limit=500)
            if got["ids"] and got["metadatas"]:
                matrix_source = "chroma"
                for mid, meta in zip(got["ids"], got["metadatas"]):
                    g = meta.get("global_id")
                    a = meta.get("area_name", "")
                    f = meta.get("family_name", "")
                    if g is not None and a and f:
                        rows.append((int(g), a, f))
                rows.sort(key=lambda x: x[0])
        except Exception:
            rows = load_matrix_from_csv(csv_full)
    else:
        rows = load_matrix_from_csv(csv_full)

    area_to_families, _ = build_area_to_families(rows)

    # Geometry constants
    geometry = {
        "AREA_COUNT": AREA_COUNT,
        "FAMILIES_PER_AREA": FAMILIES_PER_AREA,
        "HEXES_PER_FAMILY": HEXES_PER_FAMILY,
        "SIDES_PER_HEX": SIDES_PER_HEX,
        "TOTAL_FAMILIES": TOTAL_FAMILIES,
        "TOTAL_HEXES": TOTAL_HEXES,
        "TOTAL_SIDES": TOTAL_SIDES,
        "STEPS_PER_PASS": STEPS_PER_PASS,
    }

    # Hex unit / truth unit capacity
    hex_unit = {
        "count_per_family": HEXES_PER_FAMILY,
        "total_hexes": TOTAL_HEXES,
    }
    truth_unit = {
        "sides_per_hex": SIDES_PER_HEX,
        "total_sides": TOTAL_SIDES,
        "side_id_range": [0, TOTAL_SIDES - 1],
    }

    # Borders (adjacency)
    borders = {
        "area_ring": [
            {"area_id": i, "area_name": CANONICAL_AREAS[i], "left_area_id": area_left(i), "right_area_id": area_right(i)}
            for i in range(AREA_COUNT)
        ],
    }

    # Path and road traversal
    start = max(0, min(11, args.start))
    steps = max(1, args.steps)
    direction = args.direction
    road, area_passings, family_passings = run_traversal(start, direction, steps, area_to_families)
    traversal_length = len(road)
    is_loop = traversal_length > 1 and road[0]["area_id"] == road[-1]["area_id"] and (traversal_length % AREA_COUNT == 0)

    out = {
        "matrix_source": matrix_source,
        "geometry": geometry,
        "hex_unit": hex_unit,
        "truth_unit": truth_unit,
        "borders": borders,
        "path_params": {"start_area_id": start, "direction": direction, "steps": steps},
        "road_coordinates": road,
        "border_passings": {
            "area_border_passings": area_passings,
            "family_border_passings": family_passings,
        },
        "traversal_length": traversal_length,
        "is_loop": is_loop,
        "loopability": {
            "formula_ref": "L_full = G_F[p] / STEPS_PER_PASS (40_POLICY §11)",
            "requires_activation_data": True,
            "note": "Compute when per-family activation and TAU_FAMILY threshold are available.",
        },
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
