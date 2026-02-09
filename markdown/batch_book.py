import argparse
import json
import os
from pathlib import Path
from typing import Dict, List

from openai import OpenAI


API_KEY = os.getenv("OPENAI_API_KEY", "")
client = OpenAI(api_key=API_KEY or None)


def load_markdown(path: Path) -> str:
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def split_into_chunks(text: str, max_chars: int = 7000) -> List[str]:
    """
    Produce raw text chunks from the input text.

    Target size is ~1500–2000 tokens per chunk. We approximate this
    via a character cap (max_chars), since 1 token is roughly 3–4
    characters for English prose. With the default of 7000 characters
    you should land in the requested token range.
    """
    chunks: List[str] = []
    i = 0
    n = len(text)

    while i < n:
        # Tentative end of chunk
        end = min(i + max_chars, n)

        # Try to break on a natural boundary (double newline, then single newline, then space)
        break_pos = -1
        window = text[i:end]

        for sep in ["\n\n", "\n", " "]:
            idx = window.rfind(sep)
            if idx != -1:
                break_pos = i + idx + len(sep)
                break

        if break_pos == -1 or break_pos <= i:
            # Fallback: hard cut at max_chars
            break_pos = end

        chunk_text = text[i:break_pos]
        chunks.append(chunk_text)
        i = break_pos

    return chunks


def save_batched_json(path: Path, book: str, author: str, chunks: List[Dict]) -> None:
    data = {
        "book": book,
        "author": author,
        "chunks": chunks,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create a batched JSON structure for a markdown book, "
            "matching the shape of existing files in ./batched."
        )
    )
    parser.add_argument(
        "--input-md",
        required=True,
        help="Path to the source markdown book.",
    )
    parser.add_argument(
        "--output-json",
        help="Output JSON path (default: batched/<basename>.json).",
    )
    parser.add_argument(
        "--book",
        required=True,
        help="Book title to store in the JSON.",
    )
    parser.add_argument(
        "--author",
        required=True,
        help="Author name to store in the JSON.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=7000,
        help=(
            "Approximate maximum characters per chunk. "
            "7000 chars ≈ 1500–2000 tokens for typical prose."
        ),
    )

    args = parser.parse_args()

    input_path = Path(args.input_md)
    if not input_path.exists():
        raise SystemExit(f"Input markdown not found: {input_path}")

    if args.output_json:
        output_path = Path(args.output_json)
    else:
        base = input_path.stem
        output_path = Path("batched") / f"{base}.json"

    # Load and normalize source text (only newline normalization; content is otherwise untouched).
    raw_text = load_markdown(input_path)
    normalized = raw_text.replace("\r\n", "\n").replace("\r", "\n")

    batched: Dict = {
        "book": args.book,
        "author": args.author,
        "chunks": [],
    }
    start_offset = 0
    next_id = 1

    if output_path.exists():
        try:
            with output_path.open("r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception as e:
            print(f"Error reading existing batched file {output_path}: {e}", flush=True)
            raise SystemExit(1)

        existing_chunks = existing.get("chunks", [])
        existing_text = "".join(c.get("text", "") for c in existing_chunks)

        if existing_text:
            if not normalized.startswith(existing_text):
                print(
                    "Existing batched file does not match the start of the source text; "
                    "refusing to resume.",
                    flush=True,
                )
                raise SystemExit(1)

            batched["book"] = existing.get("book", args.book)
            batched["author"] = existing.get("author", args.author)
            batched["chunks"] = existing_chunks
            start_offset = len(existing_text)
            next_id = len(existing_chunks) + 1
            print(
                f"Resuming from existing file {output_path}: "
                f"{len(existing_chunks)} chunks, offset {start_offset}",
                flush=True,
            )

    # Always ensure the directory exists and write at least the header + any existing chunks.
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(batched, f, ensure_ascii=False)

    if start_offset >= len(normalized):
        print("No new text to batch; source fully processed.", flush=True)
        return

    remaining = normalized[start_offset:]
    new_chunk_texts = split_into_chunks(remaining, max_chars=args.max_chars)

    for chunk_text in new_chunk_texts:
        cid = next_id
        next_id += 1
        batched["chunks"].append({"id": cid, "text": chunk_text})

        # Persist after every chunk so that progress is never lost.
        try:
            with output_path.open("w", encoding="utf-8") as f:
                json.dump(batched, f, ensure_ascii=False)
        except Exception as e:
            print(f"Error writing chunk {cid} to {output_path}: {e}", flush=True)
            raise SystemExit(1)

        print(f"Wrote chunk {cid} to {output_path}", flush=True)

    print(
        f"Completed batching. Total chunks: {len(batched['chunks'])} "
        f"({len(new_chunk_texts)} new).",
        flush=True,
    )


if __name__ == "__main__":
    main()
