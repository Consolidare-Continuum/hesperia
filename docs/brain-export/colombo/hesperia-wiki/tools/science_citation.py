#!/usr/bin/env python3
"""HWIKI-MCP-05 — standalone CLI for the fixed 'Science (wiki)' citation block.
Same formatting logic as the format_hesperia_wiki_science MCP tool
(agent_mcp_hesperia_wiki/citation.py) — this is the no-MCP-client fallback for a runbook,
a script, or an agent response_contract that just needs one clean citation line/block.

Usage:
    python3 science_citation.py "<name or query>" [--link lan|tailnet|none]

Examples:
    python3 science_citation.py "KL divergence"
    python3 science_citation.py "compute_tension" --link tailnet
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agent_mcp_hesperia_wiki.citation import format_science_block_multi  # noqa: E402
from agent_mcp_hesperia_wiki.store import get_page, search  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name_or_query", help="Exact wiki page name, or a keyword search")
    ap.add_argument("--link", choices=["lan", "tailnet", "none"], default="lan", help="Which URL to include (default lan)")
    ap.add_argument("--top-k", type=int, default=5, help="Max records when name_or_query is a search, not an exact hit (default 5)")
    args = ap.parse_args()

    record, suggestions = get_page(args.name_or_query)
    if record is not None:
        print(format_science_block_multi([record], link=args.link))
        return 0

    results = search(args.name_or_query, top_k=args.top_k)
    if results:
        print(format_science_block_multi(results, link=args.link))
        return 0

    if suggestions:
        print(f"**Science (wiki):** no exact match for '{args.name_or_query}'. Did you mean: {', '.join(suggestions)}?", file=sys.stderr)
    else:
        print(format_science_block_multi([], link=args.link))
    return 1


if __name__ == "__main__":
    sys.exit(main())
