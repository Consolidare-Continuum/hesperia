#!/usr/bin/env python3
"""Third-stage grind, LLM version: character-level OCR misreads that survive
repair_text.py (mechanical) and clean_corpus_artifacts.py (structural/layout).

The two non-LLM attempts (dictionary edit-distance, OCR confusion-table — see
docs/recipes/chiron_tweaks/BACKLOG.md, 2026-08-31 3rd-pass entry) both failed:
neither has sentence context, so neither can tell a garbled word from a real
rare name/acronym/term. This does — sends book title, author, the sentence
around the flagged word, and the word itself, and asks the model to either
fix it (>=70% confidence) or reject it (leave untouched). No normalization:
the model is told to judge that one word only, never rewrite anything else,
and the script only ever substitutes the exact single matched span.

Suspect detection stays the same fast/safe filter as before: token not in
system dictionary, and appears exactly once in the whole 120-book corpus
(real recurring vocabulary — technical terms, author names used repeatedly —
is protected by definition; true one-off OCR noise is, structurally, a
one-off). 75,358 such tokens across the corpus as of 2026-08-31.

Checkpointed (progress.jsonl per batch) — safe to kill and resume.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SYSTEM_DICT = Path("/usr/share/dict/american-english")
KEYFILE = Path(os.environ.get("HESPERIA_OPENAI_KEYFILE", "/data/consolidare-continuum/hesperia/openai_api_key.txt"))
MODEL = os.environ.get("OCR_WORD_FIX_MODEL", "gpt-4o-mini")
BATCH_SIZE = int(os.environ.get("OCR_WORD_FIX_BATCH", "25"))
CONF_THRESHOLD = float(os.environ.get("OCR_WORD_FIX_CONF", "0.70"))
CONTEXT_CHARS = 200  # each side of the flagged word

_TOKEN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
_TITLE_AUTHOR = re.compile(r"^\d+\s+(.+?)\s*-\s*([^-]+)$")  # "NN Title - Author"

SYSTEM_PROMPT = """You correct a single flagged word in text extracted from a printed book \
(PDF/epub -> text conversion, so occasional OCR-style character misreads happen — wrong or \
merged letters, e.g. "Bditors" for "Editors", "Ulliversity" for "University").

You will receive a batch of items. For EACH item: book title, author, a short sentence-level \
context, and ONE flagged word from that context (marked in the context with **word**).

Decide, using the context: is the flagged word a corrupted form of some other real word, or is \
it already correct as printed (a real word, a proper name, an acronym, a technical/foreign term, \
a citation fragment)?

Rules:
1. Only propose a fix if you are genuinely >=70% confident of the exact correct word. If you are \
less confident, or the word is plausibly a real name/acronym/term as printed, reject it — do not \
guess.
2. Never invent a fix just because the word looks unusual — proper nouns, foreign words, and \
technical jargon are common and correct in this corpus and must be rejected, not "corrected".
3. Fix ONLY the flagged word itself. Do not comment on or suggest changes to anything else in the \
sentence.
4. Preserve the flagged word's capitalization pattern in your correction (all-caps stays all-caps, \
capitalized stays capitalized, etc.) — but return the correction in its natural case; the caller \
re-applies casing.

Return ONLY valid JSON: {"results": [{"i": <item index, int>, "verdict": "fix"|"reject", \
"correction": "<word or null>", "confidence": <0.0-1.0>}, ...]} — one entry per item, same order, \
no omissions, no extra commentary."""


def load_api_key() -> str:
    raw = KEYFILE.read_text(encoding="utf-8")
    for ln in raw.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        if "=" in ln and "KEY" in ln.upper():
            return ln.split("=", 1)[1].strip().strip('"').strip("'")
        return ln
    raise SystemExit(f"No API key in {KEYFILE}")


def load_system_dict() -> set[str]:
    words = set()
    for line in SYSTEM_DICT.read_text(encoding="utf-8", errors="replace").splitlines():
        w = line.strip()
        if len(w) >= 2 and w.isalpha():
            words.add(w.lower())
    return words


def parse_title_author(stem: str) -> tuple[str, str]:
    m = _TITLE_AUTHOR.match(stem)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return stem, "unknown"


def apply_case(source: str, candidate: str) -> str:
    if source.isupper():
        return candidate.upper()
    if source[:1].isupper():
        return candidate[:1].upper() + candidate[1:]
    return candidate


def build_corpus_frequency(files: list[Path]) -> dict[str, list[tuple[Path, int, int]]]:
    """token(lower) -> list of (file, match_start, match_end), only kept while count==1."""
    locations: dict[str, list[tuple[Path, int, int]]] = {}
    dropped: set[str] = set()
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in _TOKEN.finditer(text):
            low = m.group(0).lower()
            if low in dropped:
                continue
            if low in locations:
                dropped.add(low)
                del locations[low]
                continue
            locations[low] = [(path, m.start(), m.end())]
    return locations


def find_suspects(files: list[Path]) -> list[dict]:
    sysdict = load_system_dict()
    locations = build_corpus_frequency(files)
    corpus_recur = Counter()  # not needed separately: singleton-by-construction above

    file_text_cache: dict[Path, str] = {}
    suspects = []
    for low, locs in locations.items():
        if len(low) < 4 or low in sysdict:
            continue
        path, start, end = locs[0]
        if path not in file_text_cache:
            file_text_cache[path] = path.read_text(encoding="utf-8", errors="replace")
        text = file_text_cache[path]
        original = text[start:end]
        ctx_start = max(0, start - CONTEXT_CHARS)
        ctx_end = min(len(text), end + CONTEXT_CHARS)
        context = text[ctx_start:start] + "**" + original + "**" + text[end:ctx_end]
        context = context.replace("\n", " ").strip()
        title, author = parse_title_author(path.stem)
        suspects.append(
            {
                "file": path.name,
                "start": start,
                "end": end,
                "word": original,
                "context": context,
                "title": title,
                "author": author,
            }
        )
    return suspects


def call_batch(client, batch: list[dict]) -> list[dict]:
    items_blob = "\n".join(
        f'{i}. Book: "{s["title"]}" by {s["author"]}. Context: {s["context"]}'
        for i, s in enumerate(batch)
    )
    for attempt in range(1, 6):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                temperature=0,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": items_blob},
                ],
            )
            data = json.loads(resp.choices[0].message.content or "{}")
            results = data.get("results", [])
            if isinstance(results, list) and len(results) == len(batch):
                return results
            print(f"  warn: result count mismatch ({len(results)} vs {len(batch)}), retrying", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001
            print(f"  warn: batch call failed ({exc}), retry {attempt}/5", file=sys.stderr)
            time.sleep(min(2 ** attempt, 30))
    return [{"i": i, "verdict": "reject", "correction": None, "confidence": 0.0} for i in range(len(batch))]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--apply", action="store_true", help="write fixes (default: report only)")
    ap.add_argument("--limit", type=int, default=0, help="cap total suspects processed (0 = all)")
    ap.add_argument("--progress", type=Path, default=ROOT / "ocr_llm_progress.jsonl")
    args = ap.parse_args(argv)

    targets = [Path(f) for f in args.files] if args.files else sorted(ROOT.glob("*.md"))
    if not targets:
        print("no .md files found", file=sys.stderr)
        return 1

    print("scanning for suspects...", flush=True)
    suspects = find_suspects(targets)
    if args.limit:
        suspects = suspects[: args.limit]
    print(f"suspects: {len(suspects)}  model={MODEL}  batch={BATCH_SIZE}", flush=True)

    done: dict[str, dict] = {}
    if args.progress.exists():
        for ln in args.progress.read_text(encoding="utf-8").splitlines():
            if not ln.strip():
                continue
            try:
                row = json.loads(ln)
            except json.JSONDecodeError:
                continue
            done[f"{row['file']}:{row['start']}"] = row

    from openai import OpenAI

    client = OpenAI(api_key=load_api_key())

    pending = [s for s in suspects if f"{s['file']}:{s['start']}" not in done]
    print(f"already done: {len(suspects) - len(pending)}  pending: {len(pending)}", flush=True)

    with args.progress.open("a", encoding="utf-8") as prog:
        for bi in range(0, len(pending), BATCH_SIZE):
            batch = pending[bi : bi + BATCH_SIZE]
            results = call_batch(client, batch)
            for s, r in zip(batch, results):
                row = {
                    "file": s["file"],
                    "start": s["start"],
                    "end": s["end"],
                    "word": s["word"],
                    "verdict": r.get("verdict", "reject"),
                    "correction": r.get("correction"),
                    "confidence": r.get("confidence", 0.0),
                }
                prog.write(json.dumps(row, ensure_ascii=False) + "\n")
                done[f"{s['file']}:{s['start']}"] = row
            prog.flush()
            print(f"  batch {bi // BATCH_SIZE + 1}/{(len(pending) - 1) // BATCH_SIZE + 1} done", flush=True)

    fixed = {k: v for k, v in done.items() if v["verdict"] == "fix" and v.get("confidence", 0) >= CONF_THRESHOLD and v.get("correction")}
    print(f"total fix verdicts >= {CONF_THRESHOLD} confidence: {len(fixed)} / {len(suspects)} suspects", flush=True)

    if not args.apply:
        print("report-only (pass --apply to write). Sample fixes:", flush=True)
        for row in list(fixed.values())[:20]:
            print(f"  {row['word']} -> {row['correction']}  (conf {row['confidence']})")
        return 0

    by_file: dict[str, list[dict]] = {}
    for k, row in fixed.items():
        by_file.setdefault(row["file"], []).append(row)

    applied = 0
    for fname, rows in by_file.items():
        path = ROOT / fname
        text = path.read_text(encoding="utf-8", errors="replace")
        rows.sort(key=lambda r: -r["start"])
        for row in rows:
            orig = text[row["start"] : row["end"]]
            if orig != row["word"]:
                print(f"  skip stale offset: {fname} @ {row['start']} ({orig!r} != {row['word']!r})", file=sys.stderr)
                continue
            corrected = apply_case(orig, row["correction"])
            text = text[: row["start"]] + corrected + text[row["end"] :]
            applied += 1
        path.write_text(text, encoding="utf-8")

    print(f"applied: {applied}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
