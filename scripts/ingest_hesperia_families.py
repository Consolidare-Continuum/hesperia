#!/usr/bin/env python3
"""Ingest hesperia families table into Chroma (layer=hesperia_families).
Main mandatory source: CSV (hex_sphere_areas_families_ideal_proportions.csv).
Coordinates from CSV: number → global_id, area → area_name + area_id, family → family_name.
Books from 50_DATA joined by area. Schema: governance/HESPERIA-FAMILIES-CHROMA-SCHEMA.md.
Run from repo root: python cluster/chroma-server/ingest_hesperia_families.py
Data paths: CLIENTS/hesperia/ (or HESPERIA_DATA_DIR). Mass ingest = Abelard per CHROMA-USAGE-POLICY.
"""

from __future__ import annotations

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

# Data under repo
DEFAULT_DATA = REPO_ROOT / "CLIENTS" / "hesperia"

# Main mandatory CSV (coordinates source)
FAMILIES_CSV = "v0.1/hex_sphere_areas_families_ideal_proportions.csv"


def _area_id_map() -> dict[str, int]:
    """Canonical order of areas (0..11) for matrix coordinates."""
    areas = [
        "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
        "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
    ]
    return {a: i for i, a in enumerate(areas)}


def load_csv(data_dir: Path) -> list[tuple[int, str, str]]:
    """Load main mandatory CSV: (number, area, family). Returns list of (global_id, area_name, family_name)."""
    path = data_dir / FAMILIES_CSV
    if not path.exists():
        raise FileNotFoundError(f"CSV not found (main mandatory): {path}")
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if len(row) < 3:
                continue
            try:
                num = int(row[0].strip())
            except ValueError:
                continue
            area_name = row[1].strip()
            family_name = row[2].strip()
            if not area_name or not family_name:
                continue
            rows.append((num, area_name, family_name))
    return rows


def load_50(data_dir: Path) -> dict[str, list[str]]:
    """Load 50_DATA: Area -> list of 'Author — Title'. Handles quoted multiline fields."""
    path = data_dir / "50_DATA__120_books_authors_raw.txt"
    if not path.exists():
        return {}
    area_to_books: dict[str, list[str]] = {}
    with open(path, "r", encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t", quotechar='"')
        next(r, None)  # header
        for row in r:
            if len(row) < 3:
                continue
            area_name = row[0].strip()
            author = row[1].strip()
            title = row[2].strip().replace("\n", " ")
            ref = f"{author} — {title}"
            area_to_books.setdefault(area_name, []).append(ref)
    return area_to_books


def main() -> None:
    data_dir = Path(os.environ.get("HESPERIA_DATA_DIR", str(DEFAULT_DATA)))
    if not data_dir.is_dir():
        print(f"Data dir not found: {data_dir}", file=sys.stderr)
        sys.exit(2)

    area_ids = _area_id_map()
    families = load_csv(data_dir)
    books_by_area = load_50(data_dir)

    from agent_mcp_knowledge.store import get_client, get_collection

    client = get_client()
    coll = get_collection(client)

    layer = "hesperia_families"
    source = "hex_sphere_areas_families_ideal_proportions.csv"

    # Optional: delete existing hesperia_families (Abelard may run full replace)
    existing = coll.get(where={"layer": layer}, include=[], limit=500)
    if existing["ids"]:
        coll.delete(ids=existing["ids"])
        print(f"Deleted {len(existing['ids'])} existing {layer} rows", file=sys.stderr)

    ids = []
    documents = []
    metadatas = []

    for global_id, area_name, family_name in families:
        area_id = area_ids.get(area_name, -1)
        concept = f"Family {family_name} in area {area_name}."
        book_list = books_by_area.get(area_name, [])
        book_refs = json.dumps(book_list)

        doc_id = f"hfam_{global_id}"
        doc_text = f"{area_name} {family_name}: {concept}"

        ids.append(doc_id)
        documents.append(doc_text)
        metadatas.append({
            "source": source,
            "layer": layer,
            "area_name": area_name,
            "family_name": family_name,
            "global_id": global_id,
            "area_id": area_id,
            "concept": concept,
            "book_refs": book_refs,
        })

    # Add in batches (Chroma default embedding batch)
    batch_size = 50
    for start in range(0, len(ids), batch_size):
        end = start + batch_size
        coll.add(
            ids=ids[start:end],
            documents=documents[start:end],
            metadatas=metadatas[start:end],
        )
    print(f"Added {len(ids)} rows to layer={layer}", file=sys.stderr)


if __name__ == "__main__":
    main()
