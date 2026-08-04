# Template — Plain-language parameter definition (HWIKI-PLAIN)

**ID:** HWIKI-PLAIN-01  
**Owner:** Colombo (content) · Felix (renderer / export to `Consolidare-Continuum/hesperia`)  
**Live:** [http://wiki.hesperia.local/](http://wiki.hesperia.local/) · brain SOT `tools/generate_wiki.py` · prod mirror `docs/brain-export/colombo/hesperia-wiki/`  
**Charter:** [HWIKI-CHARTER-RATIFY-2026-07-23.md](../../../governance/HWIKI-CHARTER-RATIFY-2026-07-23.md)

---

## Mandate (operator 2026-08-04)

Every wiki parameter / variable / term page must be readable by a human who is not grepping code. Each page answers four questions in plain words **and** keeps the formula:

| Question | Page field | Meaning |
|----------|------------|---------|
| **What does it receive?** | Produced from (inputs) | Upstream values, vectors, flags, layer hubs |
| **What does it do?** | Yields (formula) + In plain words | Math / rule in symbols **and** one sentence in ordinary language |
| **What does it output?** | Value / default + Needed by | Type/range **and** who consumes it |
| **Why does it exist?** | Theory Explainer `plain_lang` + `reasoning` | Purpose in the product — not only ancestry |

Terms (status vocabulary, hubs, REJECTED science) use the same four questions; “formula” may be a definition sentence.

---

## Durable shape in `generate_wiki.py`

Put plain language in **origin** via Theory Explainer (survives regen):

```text
… — Theory Explainer: plain_lang: <one clear sentence>. author: <source>. extent: full|partial|structural_analogy|rejected_with_reason. reasoning: <why it exists here>. application: [[Related]].
```

Helper: `theory_explainer(plain, author, extent=..., reasoning=..., application=...)`.

Catalog batches that already store `_meaning` **must** promote `_meaning` into `plain_lang` (do not leave meaning only in Notes).

---

## Rendered page order (after HWIKI-PLAIN)

1. Header (status, category, type, module, value)  
2. **In plain words** — extracted `plain_lang` (or pending marker)  
3. **Definition** — Receives / Does / Outputs / Exists for  
4. Yields (formula)  
5. Produced from / Needed by  
6. Origin / Notes  

---

## Gate (batch DONE)

- [ ] `plain_lang` present for every LIVE_* / BEYOND / PARTIAL page in the batch  
- [ ] Formula still exact (no “vibes only”)  
- [ ] Inputs and consumers linked where pages exist  
- [ ] Regen: `python3 tools/generate_wiki.py && python3 tools/render_wiki_html.py`  
- [ ] Export / promote to prod-of-record when batch is material (Felix + Grace lane for CC repo)

DEAD / REJECTED: still require plain_lang explaining *why dead/rejected* (not silence).

---

SIGNED: Research (Colombo) | HWIKI-PLAIN definition contract | 2026-08-04 | wiki
