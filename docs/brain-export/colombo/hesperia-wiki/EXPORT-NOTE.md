# Hesperia parameter wiki — brain-export mirror

**Re-exported:** 2026-08-04 (previously 2026-07-25)  
**Role:** Published mirror for Hesperia **dev** (`igareosh/hesperia`), tree-synced onward to **prod-of-record** (`Consolidare-Continuum/hesperia`) on each gated promote per [SPEC-ETHAN-HESPERIA-REPO-STATE-MACHINE](https://github.com/igareosh/cursor/blob/main/governance/SPEC-ETHAN-HESPERIA-REPO-STATE-MACHINE.md) — the old Atomic-Commits-Team split this note originally described no longer applies (Atomic abandoned 2026-07-26).

## Canonical edit path (brain)

| Need | Path |
|------|------|
| Source of truth | brain `colombo_research/hesperia/wiki/` |
| Generator | `tools/generate_wiki.py` then regen |
| Live LAN | `http://wiki.hesperia.local/` (altitudine) |
| CHROMA-1 | `query_knowledge(layer="hesperia_wiki")` |

Durable edits happen on **brain**, then re-export here. Hand-edits under this export alone will drift until the next sync.

## This tree

| Path | Content |
|------|---------|
| `./` (this folder) | Markdown pages, categories, `index.json`, generator tools |
| `../hesperia-wiki_site/` | Rendered HTML sibling (static browse) |

`SIGNED: Developer (Felix) | wiki brain-export re-sync | 2026-08-04 | igareosh/hesperia → Consolidare-Continuum/hesperia (promoted)`
