# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

from openai import OpenAI


# API key can be supplied via environment variable or edited here.
API_KEY = os.getenv("OPENAI_API_KEY", "")

client = OpenAI(api_key=API_KEY or None)


SYSTEM_PROMPT = """You are a classification assistant for the Sphere Project.

Sphere has 12 Areas and 24 Families per Area.
Every statement must be assigned to exactly one Family within a single Area.

Your task:
- For each input statement, choose the single most appropriate Family from the provided list.
- Use only the provided Families; do not invent new Families or Areas.
- If several Families seem plausible, pick the closest fit.
- Base the choice only on the content of the statement text.

Output rules:
- Respond with clean JSON only, no commentary.
- Shape:
  {
    "chunk_id": <ID>,
    "statements": [
      { "sid": "<SID>", "family": "<FAMILY_NAME>" },
      ...
    ]
  }
"""


def load_families_by_area(path: Path) -> Dict[str, List[str]]:
    """Load families grouped by Area from families.txt (tab-separated)."""
    by_area: Dict[str, List[str]] = {}
    with path.open("r", encoding="utf-8") as f:
        header = True
        for line in f:
            if header:
                header = False
                continue
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            _, area, family = parts[0], parts[1].strip(), parts[2].strip()
            if not area or not family:
                continue
            by_area.setdefault(area, [])
            if family not in by_area[area]:
                by_area[area].append(family)
    return by_area


def load_statements(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_output(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def classify_chunk(
    model: str,
    chunk_id: int,
    statements: List[Dict[str, Any]],
    area: str,
    families: List[str],
) -> str:
    """Call the model once for all statements in a chunk, return raw content."""
    families_text = ", ".join(families)

    user_content = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    f"Area: {area}\n"
                    f"Families in this Area: {families_text}\n\n"
                    f"Classify each of the following statements from chunk {chunk_id} "
                    f"into exactly one Family within Area {area}:\n"
                    + json.dumps(
                        [
                            {"sid": s["sid"], "text": s["text"]}
                            for s in statements
                        ],
                        ensure_ascii=False,
                    )
                    + "\n\nReturn JSON only in the specified format."
                ),
            }
        ],
    }

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            user_content,
        ],
        temperature=0,
    )

    content = response.choices[0].message.content or ""
    return content


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classify Sphere statements into Families for a single Area."
    )
    parser.add_argument(
        "--statements",
        default="statements_The Theory of Moral Sentiments - Adam Smith.json",
        help="Input JSON file with extracted statements.",
    )
    parser.add_argument(
        "--families-file",
        default="families.txt",
        help="families.txt listing all Areas and Families.",
    )
    parser.add_argument(
        "--area",
        default="GOOD",
        help="Area name for this book (e.g., GOOD).",
    )
    parser.add_argument(
        "--output",
        default="classified_statements_The Theory of Moral Sentiments - Adam Smith.json",
        help="Output JSON file for classified statements.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4o",
        help="OpenAI chat model to use for classification (e.g., gpt-4o).",
    )

    args = parser.parse_args()

    families_path = Path(args.families_file)
    print(f"Loading families from: {families_path}", flush=True)
    by_area = load_families_by_area(families_path)
    if args.area not in by_area:
        raise ValueError(f"Area '{args.area}' not found in {families_path}")
    area_families = by_area[args.area]
    print(f"Area {args.area} has {len(area_families)} families.", flush=True)

    statements_path = Path(args.statements)
    print(f"Loading statements from: {statements_path}", flush=True)
    data = load_statements(statements_path)

    book_number_file = data.get("book_number_file")
    book = data.get("book")
    author = data.get("author")
    chunks = data.get("chunks", [])

    output_path = Path(args.output)

    classified: Dict[str, Any] = {
        "book_number_file": book_number_file,
        "book": book,
        "author": author,
        "area": args.area,
        "families": area_families,
        "chunks": [],
    }

    # Save initial stub so progress is never lost.
    save_output(output_path, classified)

    for ch in chunks:
        chunk_id = ch.get("chunk_id")
        if chunk_id is None:
            continue

        stmts = ch.get("statements", [])
        if not stmts:
            continue

        print(f"Classifying chunk {chunk_id} with {len(stmts)} statements...", flush=True)

        raw_content = ""
        try:
            raw_content = classify_chunk(args.model, chunk_id, stmts, args.area, area_families)
            result = json.loads(raw_content)
        except Exception as e:
            print(f"Error classifying chunk {chunk_id}: {e}", flush=True)
            failed = classified.setdefault("failed_chunks", [])
            failed.append(
                {
                    "chunk_id": chunk_id,
                    "error": str(e),
                    "raw_preview": raw_content[:200],
                }
            )
            save_output(output_path, classified)
            print(f"Recorded failure for chunk {chunk_id} and saved current progress to {output_path}", flush=True)
            continue

        # result["statements"] should contain sid, family.
        by_sid = {s["sid"]: s for s in stmts}
        enriched_statements: List[Dict[str, Any]] = []
        for rs in result.get("statements", []):
            sid = rs.get("sid")
            family = rs.get("family")
            original = by_sid.get(sid, {})
            enriched_statements.append(
                {
                    "sid": sid,
                    "text": original.get("text"),
                    "family": family,
                    "area": args.area,
                }
            )

        classified["chunks"].append(
            {
                "chunk_id": chunk_id,
                "statements": enriched_statements,
            }
        )

        save_output(output_path, classified)
        print(f"Saved classifications for chunk {chunk_id} to {output_path}", flush=True)

    print("Classification complete.", flush=True)


if __name__ == "__main__":
    main()

