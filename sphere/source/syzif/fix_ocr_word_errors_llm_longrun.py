#!/usr/bin/env python3
"""Re-address the long/glued-run class fix_ocr_word_errors_llm.py's first pass
left unresolved (see docs/recipes/chiron_tweaks/BACKLOG.md).

That first pass used one prompt for every flagged token regardless of shape.
It worked well for short single-word typos (applied, 84b4c21f) but was
unreliable on long glued/duplicated multi-word runs (e.g. "our society
society of women and others" concatenated with no spaces, sometimes with
words doubled): the model sometimes fully reconstructed them correctly
("Hismothermotherisisbedridden" -> "His mother is bedridden") but often
collapsed a long run to 1-2 words, silently dropping real content
("HistoryooffInsanity" -> "History", losing "of Insanity").

Two changes here, not one — a better prompt alone isn't trustworthy enough
after seeing that failure mode, so this adds an independent, deterministic
check that doesn't depend on the model self-reporting honestly:

1. Prompt: explicit reconstruction task, not a single-word fix. States the
   input is letters-only run-together text (spaces lost, and duplicated
   words are a known artifact of this exact conversion pipeline — collapse
   an exact repeat like "society society" to one "society", but every
   letter run that is NOT a repeat must appear in the output). Reject
   (not partial-fix) if it cannot confidently recover the full content.
2. Verification, independent of the model: after a "fix" verdict, compute
   the letter-bag (lowercase, letters only) of the original flagged token
   and of the proposed correction with spaces/hyphens stripped and any
   single duplicated word collapsed once. If the correction's letter-bag
   does not cover >=85% of the original's letters (by count, allowing
   for the legitimate de-duplication case), the verdict is downgraded to
   "reject_content_loss" here in the script, regardless of what the model
   claimed — never trust the self-report alone for this failure mode.

Separate progress file (ocr_llm_longrun_progress.jsonl) and separate suspect
set (>= LONG_MIN_LEN chars, re-evaluated fresh — the first pass's verdicts on
these tokens used the old prompt and are not reused).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fix_ocr_word_errors_llm import (  # noqa: E402
    ROOT,
    apply_case,
    find_suspects,
    load_api_key,
)

MODEL = os.environ.get("OCR_WORD_FIX_MODEL", "gpt-4o-mini")
BATCH_SIZE = int(os.environ.get("OCR_WORD_FIX_BATCH", "15"))  # smaller — longer per-item context
CONF_THRESHOLD = float(os.environ.get("OCR_WORD_FIX_CONF", "0.70"))
COVERAGE_THRESHOLD = float(os.environ.get("OCR_WORD_FIX_COVERAGE", "0.85"))
LONG_MIN_LEN = int(os.environ.get("OCR_WORD_FIX_LONG_MIN", "15"))

SYSTEM_PROMPT = """You reconstruct a single flagged run of letters extracted from a printed book, \
where the text-extraction pipeline lost the spaces between words and, in this specific corpus, \
sometimes duplicates a word (e.g. "societysociety" for "society", "isis" for "is"). The flagged \
run is one long letters-only blob with no spaces, e.g. "historyoofinsanity" for "history of \
insanity", or "wranglingisisapoorpoorsubstitute" for "wrangling is a poor substitute".

You will receive a batch of items: book title, author, a short context, and ONE flagged run \
(marked in the context with **run**).

Your job: reconstruct the FULL original wording of the flagged run — every distinct word it \
contains, in order, with spaces restored. Rules:

1. If a word is clearly duplicated back-to-back in the run (e.g. "poorpoor" -> "poor", "isis" -> \
"is"), collapse it to ONE occurrence — that is not content loss, it's undoing the duplication \
artifact.
2. Do NOT drop, summarize, or omit any part of the run that is not an exact duplicate. If the run \
is "wranglingisisapoorpoorsubstitute", the correct output is "wrangling is a poor substitute" — \
ALL five distinct words, not just "substitute". Losing real words is a serious error, worse than \
rejecting.
3. If you cannot confidently reconstruct the ENTIRE run this way — some part is genuinely unclear, \
not just unfamiliar — reject rather than guess or give a partial/incomplete reconstruction. A \
confident partial answer is not acceptable; it must be the whole run or a rejection.
4. Only reject for genuine uncertainty about the *content* of the run, not because it is long — \
length alone is not a reason to reject.
5. Confidence reflects how sure you are the reconstruction is complete and correct, not just \
plausible.

Return ONLY valid JSON: {"results": [{"i": <item index, int>, "verdict": "fix"|"reject", \
"correction": "<full reconstructed phrase with spaces, or null>", "confidence": <0.0-1.0>}, ...]} \
— one entry per item, same order, no omissions, no extra commentary."""


def letter_bag(s: str) -> Counter:
    return Counter(ch.lower() for ch in s if ch.isalpha())


def collapse_immediate_dupes(bag_source: str) -> str:
    """For coverage checking only: collapse a word immediately repeated in the
    ORIGINAL flagged token (case-insensitive) to one instance, so a legitimate
    de-duplication doesn't look like content loss when measuring coverage."""
    import re

    return re.sub(r"\b(\w+)(\1)\b", r"\1", bag_source, flags=re.IGNORECASE)


def coverage_ratio(original: str, correction: str) -> float:
    orig_for_coverage = collapse_immediate_dupes(original)
    orig_bag = letter_bag(orig_for_coverage)
    corr_bag = letter_bag(correction)
    total = sum(orig_bag.values())
    if total == 0:
        return 1.0
    overlap = sum((orig_bag & corr_bag).values())
    return overlap / total


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
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--progress", type=Path, default=ROOT / "ocr_llm_longrun_progress.jsonl")
    args = ap.parse_args(argv)

    targets = [Path(f) for f in args.files] if args.files else sorted(ROOT.glob("*.md"))
    if not targets:
        print("no .md files found", file=sys.stderr)
        return 1

    print("scanning for suspects...", flush=True)
    all_suspects = find_suspects(targets)
    suspects = [s for s in all_suspects if len(s["word"]) >= LONG_MIN_LEN]
    if args.limit:
        suspects = suspects[: args.limit]
    print(f"long-run suspects (>={LONG_MIN_LEN} chars): {len(suspects)}  model={MODEL}  batch={BATCH_SIZE}", flush=True)

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

    batches = [pending[bi : bi + BATCH_SIZE] for bi in range(0, len(pending), BATCH_SIZE)]
    n_batches = len(batches)
    workers = int(os.environ.get("OCR_WORD_FIX_WORKERS", "6"))
    completed = 0
    content_loss_downgrades = 0

    with args.progress.open("a", encoding="utf-8") as prog:
        from concurrent.futures import ThreadPoolExecutor, as_completed

        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(call_batch, client, b): b for b in batches}
            for fut in as_completed(futures):
                batch = futures[fut]
                results = fut.result()
                for s, r in zip(batch, results):
                    verdict = r.get("verdict", "reject")
                    correction = r.get("correction")
                    confidence = r.get("confidence", 0.0)
                    cov = None
                    if verdict == "fix" and correction:
                        cov = coverage_ratio(s["word"], correction)
                        if cov < COVERAGE_THRESHOLD:
                            verdict = "reject_content_loss"
                            content_loss_downgrades += 1
                    row = {
                        "file": s["file"],
                        "start": s["start"],
                        "end": s["end"],
                        "word": s["word"],
                        "verdict": verdict,
                        "correction": correction,
                        "confidence": confidence,
                        "coverage": cov,
                    }
                    prog.write(json.dumps(row, ensure_ascii=False) + "\n")
                    done[f"{s['file']}:{s['start']}"] = row
                prog.flush()
                completed += 1
                print(f"  batch {completed}/{n_batches} done", flush=True)

    def letters(s: str) -> int:
        return sum(1 for c in s if c.isalpha())

    over_completion = 0

    def not_over_complete(v: dict) -> bool:
        nonlocal over_completion
        if letters(v["correction"]) > letters(v["word"]) * 1.3 + 5:
            over_completion += 1
            return False
        return True

    fixed = {
        k: v
        for k, v in done.items()
        if v["verdict"] == "fix"
        and v.get("confidence", 0) >= CONF_THRESHOLD
        and v.get("correction")
        and v["word"].lower() != (v.get("correction") or "").lower()
        and not_over_complete(v)
    }
    print(
        f"fix verdicts >= {CONF_THRESHOLD} conf, coverage >= {COVERAGE_THRESHOLD}, not over-complete: {len(fixed)} / {len(suspects)}",
        flush=True,
    )
    print(f"content-loss downgrades (model said fix, coverage check disagreed): {content_loss_downgrades}", flush=True)
    print(f"over-completion exclusions (correction hallucinated content beyond the flagged span): {over_completion}", flush=True)

    if not args.apply:
        print("report-only (pass --apply to write). Sample fixes:", flush=True)
        for row in list(fixed.values())[:20]:
            print(f"  {row['word']} -> {row['correction']}  (conf {row['confidence']}, cov {row['coverage']})")
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
