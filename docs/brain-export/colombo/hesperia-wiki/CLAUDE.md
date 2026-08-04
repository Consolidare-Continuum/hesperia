# CLAUDE.md — Hesperia Parameter/Variable Wiki (read this first)

**Scope of this file:** only `colombo_research/hesperia/wiki/` and its rendered sibling `colombo_research/hesperia/wiki_site/`. Claude Code loads this automatically for any agent working in this directory, in addition to the repo-root [`CLAUDE.md`](../../../CLAUDE.md) — same convention, narrower scope. If you were pointed at this wiki and haven't read the root file yet, read that one first for entity identity (Felix/Colombo/Abelard/…); this file assumes it.

---

## What this is

A **wikipedia-style, interlinked register** of every Hesperia math variable/parameter this research thread has verified in `/data/hesperia/hesperia` — one page per item, LIVE and DEAD alike, each with: **status, type, responsible module, value, formula (yields), produced-from (inputs), needed-by (consumers), origin, notes**. Built bottom-up from a one-year Java-prototype-vs-shipped-code audit, not top-down from a spec — every claim traces to a `grep`/file-read done during that research, not to a memory of what should be true.

**Why it exists:** Colombo's research kept regenerating the same lookups (is X live? what replaced it? why did Y die?) across separate one-off `.md` audits. This wiki is the durable, navigable form of that research — the thing to open *before* re-deriving an answer that's already been found once.

**Operator mandate (2026-07-19):** all-encompassing grind — theory, decisions, science; per step / line of code what and where happens, for what reasons, relations interlinked. Expand via `HWIKI-*` wave. Do not treat Coverage-Ledger gaps as permanent silence.

## Structure

| Path | What |
|------|------|
| `index.md` | Home page — category list, status legend, full alphabetical page list |
| `structure/` | **System structure / how-it-works hubs @ sealed 0.7.0** (hand-authored; not ITEMS). Start: [SYSTEM-STRUCTURE-0.7.0.md](structure/SYSTEM-STRUCTURE-0.7.0.md), [HOW-IT-WORKS-0.7.0.md](structure/HOW-IT-WORKS-0.7.0.md). Wave: `HWIKI-STRUCT-*` |
| `categories/*.md` | 12 hub pages (Geometry, Core Math Contract, Tension, Propagation, Thresholds, Graph Metrics, Entropy, Stability, Similarity, Trust, Concept Dictionary, Dead/Rejected) — each a table of its member pages |
| `pages/*.md` | One page per variable/parameter/formula — the actual content |
| `Coverage-Ledger.md` | **Read before assuming completeness.** States explicitly what's *not* wikified yet (full L1–L11 layer variables, KME's 35 derived metrics individually, TRIZ internals, STRUCT depth) and open/unresolved questions carried over from the research passes |
| `tools/generate_wiki.py` | **Source of truth generator.** Parameter pages + 12 category hubs + `index.md` + `Coverage-Ledger.md` are rendered from the `ITEMS` list in this script — not hand-authored. Links to `structure/` hubs are emitted by the generator; hub bodies themselves are hand-authored |
| `tools/render_wiki_html.py` | Converts every `.md` in this folder to static HTML (via `pandoc`) into `../wiki_site/`, rewriting `.md` links to `.html` |
| `tools/serve.py` | Copy of the server actually running (canonical source; the live copy is `../wiki_site/serve.py`, colocated with what it serves) |
| `../wiki_site/` | Rendered HTML output + the running server. Not the source of truth — regenerated from this folder, don't hand-edit `.html` there |

## Where it's served

Systemd unit **`hesperia-wiki.service`** on the **altitudine** dev VM, always-on (`enabled`, survives reboot), threaded static server with reverse-DNS-lookup-on-request disabled (a known `http.server` stall cause — see `tools/serve.py`):

- LAN DNS: `http://wiki.hesperia.local/` (dnsmaster AdGuard → `192.168.100.65`; nginx `:80` → wiki `:8901`; also `wiki.hesperia`, `wiki.hesperia.prichindel.local`)
- LAN direct: `http://192.168.100.65:8901/index.html` (or `:80` via nginx)
- Tailnet: `http://100.89.236.59:8901/index.html` (or `:80` if using LAN DNS name over tailnet IP)

**Note:** bare `.local` is mDNS-reserved on Linux `systemd-resolved`. altitudine routes `~hesperia.local` → dnsmaster (`/etc/systemd/resolved.conf.d/20-hesperia-local.conf`). Prefer `wiki.hesperia.prichindel.local` on hosts that only route `prichindel.local`.

```bash
systemctl status hesperia-wiki.service      # check
sudo systemctl restart hesperia-wiki.service # after changing tools/serve.py (content-only changes don't need a restart)
sudo journalctl -u hesperia-wiki.service -f  # tail logs
```

`ufw` on this host allow-lists per service — port `8901/tcp` has explicit rules for `192.168.100.0/24` (LAN) and `100.64.0.0/10` (tailnet), tagged `hesperia-wiki` in `sudo ufw status`. If reachability breaks again, check there before assuming the app is at fault — that's what actually caused the first "it hangs" report on 2026-07-19.

## How to update this wiki

**Two ways, different durability:**

1. **Durable (do this for anything worth keeping):** edit `tools/generate_wiki.py` — add or modify an `add(name, category, status, kind, module, value, formula, produced_from, needed_by, origin, notes)` call, then regenerate:
   ```bash
   python3 tools/generate_wiki.py          # rewrites pages/, categories/, index.md, Coverage-Ledger.md
   python3 tools/render_wiki_html.py        # re-renders ../wiki_site/*.html from the updated .md
   ```
   No service restart needed — the running server just serves whatever is on disk.

2. **Quick, non-durable:** hand-edit a file directly in `pages/*.md`. Fine for a one-off correction someone needs to see *now*, but **the next `generate_wiki.py` run overwrites it** — anything worth keeping has to make it back into the generator's `ITEMS` list, or it's lost on the next regen.

**Adding cross-links:** `produced_from` / `needed_by` entries are plain strings; the generator auto-links any string that exactly matches another item's `name`, and renders anything else as plain italic text (an external input with no page). Inline `[[Page Name]]` or `[[Page Name|label]]` also works inside `formula`/`origin`/`notes` strings — same auto-link-or-italicize rule.

## Status vocabulary

| Code | Meaning |
|------|---------|
| 🟢 `LIVE_FULL` | Matches proposal (if any), running in production path |
| 🟢 `LIVE_SUCCESSOR` | Same idea, different name/formula than any Java ancestor |
| 🟡 `PARTIAL` | Present in a narrow slice/tool, not the full contract |
| 🔴 `DEAD` | No implementation under this name or a successor formula |
| 🔴/🟢 `DEAD_ALGO_SURVIVED` | Name dead, but the underlying algorithm runs elsewhere — see the linked live page (the `largest_component_size` ↔ Java `L(R)` case is the flagship example) |
| 🔵 `BEYOND` | Shipped in LIVE, not proposed in the Java corpus |
| ⚪ `UNVERIFIED` | Claimed in an earlier doc, did not re-confirm by direct `grep`/read — don't cite as fact without re-checking |
| 🔴 `REJECTED` | Explicit, reasoned decision against (e.g. KL divergence, DFT ring smoothness) — not an oversight |

## Source research (what this wiki was built from)

- [`COLOMBO-HESPERIA-JAVA-PROPOSED-VS-ACCOMPLISHED-AUDIT-2026-07-19.md`](../COLOMBO-HESPERIA-JAVA-PROPOSED-VS-ACCOMPLISHED-AUDIT-2026-07-19.md) — symbol-level DEAD/PARTIAL register (Colombo)
- [`COLOMBO-HESPERIA-MATH-PARAMS-THEORY-MAP-2026-07-19.md`](../COLOMBO-HESPERIA-MATH-PARAMS-THEORY-MAP-2026-07-19.md) — LIVE math register, provenance chains (Colombo)
- [`FELIX-HESPERIA-DEAD-PARTIAL-REIMPLEMENTATION-VIABILITY-2026-07-19.md`](../FELIX-HESPERIA-DEAD-PARTIAL-REIMPLEMENTATION-VIABILITY-2026-07-19.md) — engineering viability of reviving each DEAD/PARTIAL item (Felix)
- [`COLOMBO-HESPERIA-DEAD-SCIENCE-BOTTOM-UP-SURFACE-2026-07-19.md`](../COLOMBO-HESPERIA-DEAD-SCIENCE-BOTTOM-UP-SURFACE-2026-07-19.md) — discipline-level bottom-up trace of where the underlying science survived (Colombo)

If a wiki page's claim conflicts with one of these docs, the wiki should win *only if* it was independently re-verified — check the page's **Notes** section; several pages explicitly flag where a claim from an earlier doc did **not** re-confirm (e.g. `Wiener feedback on alpha (k_s / k_j)` — `UNVERIFIED`, contradicted by a direct grep). Don't silently trust older docs over the wiki, or the wiki over the docs — check what was actually re-run.

## MCP tooling (HWIKI-MCP wave, 2026-07-19)

Two complementary lookup paths — semantic recall vs. exact structured record:

| Path | Tool | When |
|------|------|------|
| **Semantic** | `query_knowledge(query=…, layer="hesperia_wiki")` (`chroma-knowledge` MCP) | Fuzzy recall across many pages; "what do we know about X area" |
| **Exact/structured** | `query_hesperia_wiki(query, top_k)`, `get_hesperia_wiki_page(name)` (`hesperia-wiki` MCP) | One named symbol, precise status/module/formula fields, no Chroma/ingest-lag dependency — reads `index.json` directly |

`hesperia-wiki` MCP server: `agent_mcp_hesperia_wiki/` (repo root), registered in `governance/mcp-config.json` → mirrored to `.mcp.json` / `.cursor/mcp.json` / VSCode via `scripts/deploy-mcp-config-global.sh`. Runs locally (`bash scripts/agent-mcp-hesperia-wiki.sh`) — no SSH, no Chroma, works even when prichindel/CHROMA-1 is unreachable. Third tool, `format_hesperia_wiki_science(name_or_query)`, returns the fixed citation block below directly.

**`index.json`** (sibling to `index.md`, same `tools/generate_wiki.py` regen step) is the structured mirror every tool above reads — `{name, status, module, formula, produced_from, needed_by, origin, notes, source_page, lan_url, tailnet_url}` per item. Never hand-edit it; it's derived, same rule as the `.md` pages.

**Context RAG**: `cluster/chroma-server/context_rag.py --query "…"` auto-includes `retrieval.wiki_hits` when the query matches a wiki item (or force with `--hesperia-wiki`) — schema: `governance/CONTEXT-RAG-PACKET-SCHEMA.md` §5.

**Code↔wiki linker** (`tools/link_symbol.py <symbol>`): grep-based evidence gatherer, not a status-decider — finds real definitions + call sites in the Hesperia checkout and prints a `generate_wiki.py` `add(...)` stub with `module`/call-sites pre-filled from actual grep hits and `STATUS_TODO`/`FORMULA_TODO` left for a human (status is a judgment call, never auto-assigned). Use this before writing a new page by hand.

**Science (wiki) citation block** — fixed format for agent/runbook responses that need to cite a wiki fact without re-deriving it:
```
**Science (wiki):** <name> — `<status>` · module: `<module>` · <why, from notes/formula/origin> · <LAN or tailnet URL>
```
Get it via `format_hesperia_wiki_science(name_or_query)` (MCP tool) or `python3 tools/science_citation.py "<name or query>"` (no-MCP-client CLI fallback, e.g. from a shell runbook step). Formatting logic lives once in `agent_mcp_hesperia_wiki/citation.py` — both callers use it, so the shape never drifts between them. On no match it says so explicitly ("no matching wiki record") — never invents a status.

## Ownership

**Content** (adding items, correcting status, re-verifying claims) — **Colombo** (research/formalization role). **Serving infrastructure + MCP tooling** (systemd unit, firewall, `agent_mcp_hesperia_wiki`, context-rag wiring, linker CLI) — **Felix**. **CHROMA-1 mirror** (`layer=hesperia_wiki`) — Abelard ingest after VECTOR-STORAGE-APPROVAL. Team policy: [HESPERIA-PARAMETER-WIKI-SOURCE.md](../../../governance/HESPERIA-PARAMETER-WIKI-SOURCE.md) · runbook `SCRIPT-RUNBOOK-hesperia-parameter-wiki`. Agents query via `query_knowledge(layer="hesperia_wiki")` (semantic) or `query_hesperia_wiki`/`get_hesperia_wiki_page` (exact) before re-deriving status. Report a broken link or a wrong status the same way any defect gets reported in this repo: **task Grace**.

---
SIGNED: Developer (Felix) + Research (Colombo) | wiki onboarding / operating doc | 2026-07-19 | HWIKI-MCP-01..05 tooling section added
