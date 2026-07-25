#!/usr/bin/env python3
"""HWIKI-MCP-04 — code<->wiki linker: symbol -> defs/usages in the Hesperia checkout -> fields
ready for generate_wiki.py's add(...). Gathers evidence only; does NOT decide LIVE/DEAD/status —
that judgment stays with Colombo (content) / Felix (code review), per wiki/CLAUDE.md ownership split.

Usage:
    python3 link_symbol.py <symbol> [--json] [--max-usages N] [--repo PATH]

Examples:
    python3 link_symbol.py compute_tension
    python3 link_symbol.py LOOP_COUNT --json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

_REPO_CANDIDATES = (
    os.environ.get("HESPERIA_REPO_ROOT", "").strip(),
    "/data/workspaces/atomic-commit-hesperia",
    "/data/hesperia/hesperia",
)

# Definition patterns, in priority order (first match wins as "primary" definition kind).
_DEF_PATTERNS = [
    ("function", r"^\s*def\s+{sym}\s*\("),
    ("class", r"^\s*class\s+{sym}\s*[:\(]"),
    ("constant", r"^\s*{sym}\s*(:\s*[\w\[\], .|]+)?\s*="),
]

_EXCLUDE_DIRS = {".git", ".venv", "__pycache__", "node_modules", ".pytest_cache"}


def hesperia_repo_root(explicit: str | None = None) -> Path | None:
    candidates = (explicit,) + _REPO_CANDIDATES if explicit else _REPO_CANDIDATES
    for c in candidates:
        if c and Path(c).is_dir():
            return Path(c)
    return None


def _grep_lines(repo: Path, pattern: str) -> list[tuple[str, int, str]]:
    """Run grep -rn -E for pattern under repo, excluding noise dirs. Returns (relpath, lineno, text)."""
    exclude_args = []
    for d in _EXCLUDE_DIRS:
        exclude_args += ["--exclude-dir", d]
    try:
        proc = subprocess.run(
            ["grep", "-rn", "-E", "--include=*.py", *exclude_args, pattern, "."],
            cwd=str(repo), capture_output=True, text=True, timeout=30,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []
    out: list[tuple[str, int, str]] = []
    for line in proc.stdout.splitlines():
        # format: ./relpath:lineno:text
        m = re.match(r"^(\./[^:]+):(\d+):(.*)$", line)
        if not m:
            continue
        relpath, lineno, text = m.group(1)[2:], int(m.group(2)), m.group(3)
        out.append((relpath, lineno, text.strip()))
    return out


def find_definitions(repo: Path, symbol: str) -> list[dict]:
    defs = []
    for kind, pat_tpl in _DEF_PATTERNS:
        pat = pat_tpl.format(sym=re.escape(symbol))
        for relpath, lineno, text in _grep_lines(repo, pat):
            defs.append({"kind": kind, "file": relpath, "line": lineno, "snippet": text})
    return defs


def find_usages(repo: Path, symbol: str, definitions: list[dict], max_usages: int) -> list[dict]:
    """Whole-word occurrences of symbol, excluding the definition lines themselves."""
    def_keys = {(d["file"], d["line"]) for d in definitions}
    pat = rf"\b{re.escape(symbol)}\b"
    hits = _grep_lines(repo, pat)
    usages = []
    seen_files: set[str] = set()
    for relpath, lineno, text in hits:
        if (relpath, lineno) in def_keys:
            continue
        usages.append({"file": relpath, "line": lineno, "snippet": text})
        seen_files.add(relpath)
        if len(usages) >= max_usages:
            break
    return usages


def suggest_add_snippet(symbol: str, definitions: list[dict], usages: list[dict], repo: Path) -> str:
    """Ready-to-paste (after human fills status/category/formula/notes) add(...) call for
    generate_wiki.py — module/origin pre-filled from real grep evidence, nothing invented."""
    if definitions:
        primary = definitions[0]
        module = f"{primary['file']}:{primary['line']}"
        kind_label = {"function": "Formula / function", "class": "Formula / function", "constant": "Parameter (constant)"}.get(primary["kind"], "Formula / function")
    else:
        module = "n/a — no definition found by link_symbol.py (grep may have missed a dynamic/generated name)"
        kind_label = "Formula / function"
    usage_note = ""
    if usages:
        sites = "; ".join(f"{u['file']}:{u['line']}" for u in usages[:5])
        usage_note = f" Call sites (first {min(5, len(usages))} of {len(usages)}): {sites}."
    return (
        f'add("{symbol}", CAT_TODO, "STATUS_TODO", "{kind_label}",\n'
        f'    "{module}", "VALUE_TODO",\n'
        f'    "FORMULA_TODO",\n'
        f'    [], [],\n'
        f'    "ORIGIN_TODO",\n'
        f'    "{usage_note.strip()}")'
    )


def link(symbol: str, repo: Path, max_usages: int = 15) -> dict:
    definitions = find_definitions(repo, symbol)
    usages = find_usages(repo, symbol, definitions, max_usages)
    return {
        "symbol": symbol,
        "repo_root": str(repo),
        "definitions": definitions,
        "usage_count_sampled": len(usages),
        "usages": usages,
        "suggested_add_snippet": suggest_add_snippet(symbol, definitions, usages, repo),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("symbol", help="Symbol name to link (function, class, or constant)")
    ap.add_argument("--json", action="store_true", help="Print raw JSON instead of the human-readable summary")
    ap.add_argument("--max-usages", type=int, default=15, help="Cap on sampled usage lines (default 15)")
    ap.add_argument("--repo", type=str, default=None, help="Override Hesperia repo root")
    args = ap.parse_args()

    repo = hesperia_repo_root(args.repo)
    if repo is None:
        print(f"ERROR: no Hesperia repo checkout found. Tried: {', '.join(c for c in _REPO_CANDIDATES if c)}", file=sys.stderr)
        return 1

    result = link(args.symbol, repo, args.max_usages)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0

    print(f"Symbol: {result['symbol']}  (repo: {result['repo_root']})")
    if not result["definitions"]:
        print("  DEFINITIONS: none found — check spelling, or it may be dynamically generated/renamed.")
    else:
        print(f"  DEFINITIONS ({len(result['definitions'])}):")
        for d in result["definitions"]:
            print(f"    [{d['kind']}] {d['file']}:{d['line']}  {d['snippet'][:100]}")
    print(f"  USAGES (sampled {result['usage_count_sampled']}, cap {args.max_usages}):")
    for u in result["usages"][:args.max_usages]:
        print(f"    {u['file']}:{u['line']}  {u['snippet'][:100]}")
    print()
    print("Suggested generate_wiki.py add(...) stub (fill *_TODO fields, verify before committing):")
    print(result["suggested_add_snippet"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
