import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

from openai import OpenAI

# Set your API key here or via the OPENAI_API_KEY environment variable.
API_KEY = os.getenv("OPENAI_API_KEY", "")

client = OpenAI(api_key=API_KEY or None)


SYSTEM_PROMPT = """You are a structured data–extraction assistant for the Sphere Project.

Sphere is a semantic geometry for knowledge processing:

12 Areas (GOOD, HARM, TRUTH, DECEIT, ORDER, CHAOS, FREEDOM, CONTROL, CARE, INDIFFERENCE, CREATION, DESTRUCTION)

24 Families per Area.

Books are assigned to one Area and one Family.

Your job is to extract atomic statements for placement into the Sphere’s 432,000 truth slots.

Extraction rules:
- From each chunk, extract 20–40 grounded factual statements.
- Each statement must be 1–2 sentences.
- Every statement must be explicitly supported by the text in the chunk.
- No speculation, interpretation, or external knowledge.
- Keep statements atomic: one claim per statement.
- Do not prepend phrases like \"The text says\"; just output blunt factual statements.
- Do not validate or judge the truth of the statements; only require that they come from the text.

Output rules:
- Always return clean JSON only, with no extra commentary.
- Shape:
  {
    \"chunk_id\": <ID>,
    \"statements\": [
      { \"sid\": \"<ID>-1\", \"text\": \"...\" },
      { \"sid\": \"<ID>-2\", \"text\": \"...\" }
    ]
  }
- If fewer than 20 valid statements exist, return all that are valid.
- If more than 40 exist, return the most direct factual ones.
"""


def load_chunks(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_existing_output(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_output(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def call_model(model: str, chunk_id: int, chunk_text: str) -> str:
    user_prompt = {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    f"Chunk id: {chunk_id}\n\n"
                    "Chunk text:\n"
                    "--------------------\n"
                    f"{chunk_text}\n"
                    "--------------------\n\n"
                    "Follow the Sphere extraction rules and return JSON only."
                ),
            }
        ],
    }

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            user_prompt,
        ],
        temperature=0,
    )

    content = response.choices[0].message.content or ""
    return content


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract Sphere statements from chunks of 'The Theory of Moral Sentiments'."
    )
    parser.add_argument(
        "--input",
        default="The Theory of Moral Sentiments - Adam Smith.json",
        help="Input chunks JSON file.",
    )
    parser.add_argument(
        "--output",
        default="statements_The Theory of Moral Sentiments - Adam Smith.json",
        help="Output statements JSON file.",
    )
    parser.add_argument(
        "--model",
        default="gpt-4.1-mini",
        help="OpenAI chat model to use.",
    )
    parser.add_argument(
        "--book-number-file",
        type=int,
        default=2,
        help="Numeric book identifier to store as 'book_number_file'.",
    )
    parser.add_argument(
        "--start-id",
        type=int,
        default=34,
        help="First chunk id to process.",
    )
    parser.add_argument(
        "--end-id",
        type=int,
        default=None,
        help="Optional last chunk id to process (inclusive).",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    print(f"Loading chunks from: {input_path}", flush=True)
    book_data = load_chunks(input_path)
    chunks: List[Dict[str, Any]] = book_data.get("chunks", [])

    existing = load_existing_output(output_path)

    out: Dict[str, Any] = {
        "book_number_file": args.book_number_file,
        "book": book_data.get("book"),
        "author": book_data.get("author"),
        "chunks": [],
    }
    if existing:
        out.update({k: v for k, v in existing.items() if k != "chunks"})
        existing_chunks = {c["chunk_id"] for c in existing.get("chunks", [])}
        print(f"Loaded existing output with {len(existing_chunks)} chunks from: {output_path}", flush=True)
        out["chunks"] = list(existing.get("chunks", []))
    else:
        existing_chunks = set()
        print("No existing output found, starting fresh.", flush=True)

    # Ensure there is always at least a stub output file on disk.
    save_output(output_path, out)

    for ch in chunks:
        cid = ch.get("id")
        if cid is None:
            continue
        if cid < args.start_id:
            # Skip chunks before the requested start id.
            continue
        if args.end_id is not None and cid > args.end_id:
            # Stop once we've passed the requested end id.
            break
        if cid in existing_chunks:
            print(f"Skipping already processed chunk {cid}", flush=True)
            continue

        chunk_text = ch.get("text", "")
        print(f"Processing chunk {cid}...", flush=True)
        raw_content = ""
        try:
            raw_content = call_model(args.model, cid, chunk_text)
            result = json.loads(raw_content)
        except Exception as e:
            # Record the failure but continue with subsequent chunks.
            print(f"Error processing chunk {cid}: {e}", flush=True)
            # Keep a simple log of failed chunks in the output JSON.
            failed = out.setdefault("failed_chunks", [])
            failed.append(
                {
                    "chunk_id": cid,
                    "error": str(e),
                    "raw_preview": raw_content[:200],
                }
            )
            save_output(output_path, out)
            print(f"Recorded failure for chunk {cid} and saved current progress to {output_path}", flush=True)
            continue

        chunk_id = result.get("chunk_id", cid)
        statements = result.get("statements", [])
        out["chunks"].append(
            {
                "chunk_id": chunk_id,
                "statements": statements,
            }
        )

        save_output(output_path, out)
        print(f"Saved chunk {cid} to {output_path}", flush=True)

    print("Processing complete.", flush=True)


if __name__ == "__main__":
    main()
