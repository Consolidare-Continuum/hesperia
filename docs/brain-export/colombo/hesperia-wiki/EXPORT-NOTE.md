# Hesperia parameter wiki — brain-export mirror

**Promoted:** 2026-07-25  
**Role:** Published mirror for Hesperia **dev** (`igareosh/hesperia`).  
**Not** for Atomic prod (`Atomic-Commits-Team/hesperia`) — docs stay off prod per [ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT](https://github.com/igareosh/cursor/blob/main/governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md).

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

`SIGNED: Researcher (Colombo) | wiki brain-export | 2026-07-25 | docs only → igareosh/hesperia`
