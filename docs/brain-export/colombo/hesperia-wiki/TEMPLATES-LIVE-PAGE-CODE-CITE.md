# Template — LIVE page code cite (module path + call site)

**ID:** HWIKI-CODE-01  
**Owner:** Felix  
**Rule:** Every **LIVE** wiki page (`LIVE_FULL`, `LIVE_SUCCESSOR`, and shipped `BEYOND` used in production path) must cite **module path** + **≥1 call site**.  
**Hub:** [CLAUDE.md](CLAUDE.md) · charter [HWIKI-CHARTER-RATIFY-2026-07-23.md](../../../governance/HWIKI-CHARTER-RATIFY-2026-07-23.md) · linker `tools/link_symbol.py`

---

## Minimum cite block (put in `module` + `notes`)

In `generate_wiki.py` `add(...)`:

| Field | Pattern |
|-------|---------|
| **module** | Repo-relative path to definition, optional `:line` — e.g. `hesperia/extensions/triz/novelty_engine.py:121` |
| **notes** (or dedicated call-sites line) | At least one **importer / invoker** outside the definition line |

**Call site** = a real `grep`/`rg` hit where the symbol or function is **used** (import, call, test that exercises production API). Prefer production callers; tests allowed as second cite when production callers are thin.

### Shape in rendered page

```markdown
**Responsible (module):** `hesperia/extensions/triz/novelty_engine.py:121`

## Notes

**Call sites (≥1):**
- `hesperia/extensions/triz/novelty_engine.py:186` — `compute_innovation_clusters` → `detect_concept_clusters_louvain`
- `hesperia/extensions/triz/triz_pipeline.py` — imports novelty_engine cluster helpers
```

### Helper before authoring

```bash
python3 tools/link_symbol.py "<symbol or function>"
# fills module/call-sites from grep; status/formula still human judgment
```

---

## Gate (batch DONE check)

- [ ] Status is LIVE_* or production BEYOND  
- [ ] `module` is a real path under Hesperia checkout (not `n/a`, not vague “L2 traversal” without file)  
- [ ] ≥1 call site with path (line preferred)  
- [ ] DEAD / REJECTED pages: module may be `n/a` or last-known path; call-site rule **does not** apply  
- [ ] PARTIAL: module + call site still required for the narrow slice that exists  

---

## Worked example (verified 2026-07-23 on altitudine tree)

**Symbol:** Louvain communities (seed 42) — already wikified  

| Cite | Evidence |
|------|----------|
| **Module (def)** | `hesperia/extensions/triz/novelty_engine.py` — `LOUVAIN_SEED = 42`; `detect_concept_clusters_louvain` @ ~L121 |
| **Call site 1** | same file ~L186 — `compute_innovation_clusters` → `detect_concept_clusters_louvain` |
| **Call site 2** | `hesperia/extensions/triz/triz_pipeline.py` — imports from `novelty_engine` |
| **Test (optional extra)** | `tests/triz/test_triz_pipeline.py` — imports `detect_concept_clusters`, `score_innovation_clusters` |

Wave pages that only say “Responsible (module): L2 traversal” without a file path **fail** this template until upgraded.

---

SIGNED: Developer (Felix) | LIVE page code-cite pattern | 2026-07-23 | HWIKI-CODE-01
