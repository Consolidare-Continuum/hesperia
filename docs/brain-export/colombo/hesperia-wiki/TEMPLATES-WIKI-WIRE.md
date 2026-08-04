# Template — Wiki wire / interlinking (HWIKI-WIRE)

**ID:** HWIKI-WIRE-01  
**Owner:** Colombo  
**Live:** [http://wiki.hesperia.local/](http://wiki.hesperia.local/)  
**Map:** [Wiki Wire Map](pages/Wiki-Wire-Map.md) (generated)

---

## Mandate

Every parameter, concept, and term page must be **reachable by links** from related pages — not an island of prose. Formula stays exact; wiring is the navigation spine.

## Edge kinds

| Edge | Field | Meaning |
|------|-------|---------|
| **Receives** | `produced_from` | Upstream inputs / parent hubs |
| **Feeds** | `needed_by` | Downstream consumers |
| **Mentions** | `[[Page Name]]` in formula / origin / notes / plain | Inline term links |
| **See also** | rendered section | Parents + children + inbound + category anchor |

## Generator passes (durable)

1. `wire_bidirectional()` — if A lists B in `produced_from`, B lists A in `needed_by`
2. `wire_orphans_and_successors()` — attach orphan pages to category anchors; DEAD→LIVE successor edges
3. `autolink_known_names()` — wrap first exact name hit in each text field with `[[…]]` (longest-first; skip self; protect code/`[[`])
4. `render_page` — **See also** block + Definition I/O links
5. `Wiki Wire Map` page — hub membership counts + orphans remaining

## Do not

- Invent scientific relations that audits did not verify
- Autolink inside protected `code` or existing `[[wikilinks]]`
- Dump entire category as See also (cap ~12)

SIGNED: Research (Colombo) | HWIKI-WIRE interlinking | 2026-08-04 | wiki
