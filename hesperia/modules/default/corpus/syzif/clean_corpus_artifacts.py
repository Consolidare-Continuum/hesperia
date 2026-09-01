#!/usr/bin/env python3
"""Second-stage grind for syzif corpus .md files: strip machine-reading friction
that survives repair_text.py — running headers/footers, ligature-space breaks,
PDF glyph-ID leaks, standalone page numbers, HTML-nav leftovers.

Run repair_text.py first (encoding/hyphen-join). This pass is line-structure and
frequency based, so it needs the final line layout repair_text.py produces.

Does not touch back matter (Notes/Bibliography/References/Index) — chapter-level
notes often carry real argument, not just citations, so trimming that needs a
per-book judgment call, not a blind regex. Use --backmatter-report to locate
candidates instead.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# --- ligature-space breaks (PDF fi/fl/ffi/ffl glyph extracted with a stray space) ---
# Verified against the corpus: no English word ends bare in "fi"/"fl"/"ffi"/"ffl",
# so this fires only on the corrupted case, lowercase and sentence-initial Title-case.
_LIG_LOWER = re.compile(r"(ffi|ffl|fi|fl) (?=[a-z])")
_LIG_TITLE = re.compile(r"(Ffi|Ffl|Fi|Fl) (?=[a-z])")

# --- soft/Unicode hyphen line-wrap breaks — repair_text.py's hyphen-join only
# matches ASCII "-"; these are different codepoints from the same PDF->text
# conversion, same failure mode: word split across a line-wrap, joined with a
# hyphen-like character instead of nothing. Found via real inspection (21,307
# occurrences, 19/120 files) — "chal\xad\nlenge" for "challenge" was the case
# that surfaced it.
_SOFT_HYPHEN_JOIN = re.compile(r"([a-zA-Z])[­‐‑]\n?([a-z])")

# --- PDF glyph-ID leak: font ToUnicode map failed, literal (cid:NN) survived ---
_CID = re.compile(r"\(cid:\d+\)\s*")

# --- HTML/CD-ROM navigation leftovers (seen in Peirce Collected Papers) ---
_NAV = re.compile(r"^\s*\[(Click here[^\]]*|Top|Back|Home|Next|Previous)\]?\s*$", re.I)

# --- standalone page numbers ---
_PAGE_DIGIT = re.compile(r"^\s*\d{1,4}\s*$")
_PAGE_ROMAN = re.compile(r"^[IVXLCDM]{1,6}$")  # uppercase only — real prose is never a bare uppercase roman-looking token alone on a line

# --- back-matter heading candidates (report only, not stripped) ---
_BACKMATTER_HEAD = re.compile(
    r"^\s*(NOTES?|BIBLIOGRAPHY|REFERENCES|INDEX|APPENDIX(ES)?|ENDNOTES?|WORKS CITED)\s*$",
    re.I,
)

RUNNING_HEADER_MIN_REPEATS = 5
RUNNING_HEADER_MIN_LEN = 4
RUNNING_HEADER_MAX_LEN = 100


def fix_ligature_spacing(text: str, stats: Counter) -> str:
    text, n1 = _LIG_LOWER.subn(r"\1", text)
    text, n2 = _LIG_TITLE.subn(r"\1", text)
    stats["ligature_joins"] += n1 + n2
    return text


def fix_soft_hyphen_joins(text: str, stats: Counter) -> str:
    text, n = _SOFT_HYPHEN_JOIN.subn(r"\1\2", text)
    stats["soft_hyphen_joins"] += n
    return text


def strip_cid_artifacts(text: str, stats: Counter) -> str:
    text, n = _CID.subn("", text)
    stats["cid_glyph_leaks_removed"] += n
    return text


def strip_nav_lines(lines: list[str], stats: Counter) -> list[str]:
    out = []
    for ln in lines:
        if _NAV.match(ln):
            stats["nav_lines_removed"] += 1
            continue
        out.append(ln)
    return out


def strip_page_number_lines(lines: list[str], stats: Counter) -> list[str]:
    out = []
    for ln in lines:
        s = ln.strip()
        if _PAGE_DIGIT.match(s) or (s and _PAGE_ROMAN.match(s)):
            stats["page_number_lines_removed"] += 1
            continue
        out.append(ln)
    return out


def strip_running_headers(lines: list[str], stats: Counter) -> list[str]:
    """Remove lines that repeat verbatim >= threshold times and look like a
    running header/footer (short, no sentence-ending punctuation, not a
    markdown heading). Keeps the first occurrence as a structural trace."""
    candidates = Counter()
    for ln in lines:
        s = ln.strip()
        if not (RUNNING_HEADER_MIN_LEN <= len(s) <= RUNNING_HEADER_MAX_LEN):
            continue
        if s.startswith("#"):
            continue
        if s[-1:] in ".?!,;:":
            continue
        candidates[s] += 1

    headers = {s for s, n in candidates.items() if n >= RUNNING_HEADER_MIN_REPEATS}
    if not headers:
        return lines

    seen_once: set[str] = set()
    out = []
    for ln in lines:
        s = ln.strip()
        if s in headers:
            if s not in seen_once:
                seen_once.add(s)
                out.append(ln)
            else:
                stats["running_header_lines_removed"] += 1
            continue
        out.append(ln)
    return out


def find_backmatter_candidates(lines: list[str]) -> list[dict]:
    n = len(lines)
    if n == 0:
        return []
    found = []
    for i, ln in enumerate(lines):
        if _BACKMATTER_HEAD.match(ln.strip()):
            found.append(
                {
                    "line": i + 1,
                    "text": ln.strip(),
                    "position_pct": round(100 * i / n, 1),
                }
            )
    return found


def clean_file(path: Path) -> tuple[Counter, list[dict]]:
    stats: Counter = Counter()
    original = path.read_text(encoding="utf-8", errors="replace")

    text = fix_ligature_spacing(original, stats)
    text = fix_soft_hyphen_joins(text, stats)
    text = strip_cid_artifacts(text, stats)

    lines = text.split("\n")
    backmatter = find_backmatter_candidates(lines)
    lines = strip_nav_lines(lines, stats)
    lines = strip_page_number_lines(lines, stats)
    lines = strip_running_headers(lines, stats)

    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = cleaned.strip() + "\n"

    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
    return stats, backmatter


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", help="specific .md files; default = all *.md in this dir")
    ap.add_argument("--dry-run", action="store_true", help="report only, no writes")
    ap.add_argument("--json", action="store_true", help="emit machine-readable summary")
    args = ap.parse_args(argv)

    targets = [Path(f) for f in args.files] if args.files else sorted(ROOT.glob("*.md"))
    if not targets:
        print("no .md files found", file=sys.stderr)
        return 1

    total = Counter()
    per_file = []
    all_backmatter = {}

    for path in targets:
        if args.dry_run:
            text = path.read_text(encoding="utf-8", errors="replace")
            stats: Counter = Counter()
            tmp = fix_ligature_spacing(text, stats)
            tmp = fix_soft_hyphen_joins(tmp, stats)
            tmp = strip_cid_artifacts(tmp, stats)
            lines = tmp.split("\n")
            backmatter = find_backmatter_candidates(lines)
            lines2 = strip_nav_lines(lines, stats)
            lines2 = strip_page_number_lines(lines2, stats)
            lines2 = strip_running_headers(lines2, stats)
        else:
            stats, backmatter = clean_file(path)

        total.update(stats)
        if stats:
            per_file.append({"file": path.name, **dict(stats)})
        if backmatter:
            all_backmatter[path.name] = backmatter

    if args.json:
        print(json.dumps({"total": dict(total), "per_file": per_file, "backmatter": all_backmatter}, indent=2, ensure_ascii=False))
    else:
        print(f"files scanned: {len(targets)}  (dry_run={args.dry_run})")
        for k, v in total.items():
            print(f"  {k}: {v}")
        print(f"files touched: {len(per_file)}")
        print(f"files with backmatter candidates: {len(all_backmatter)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
