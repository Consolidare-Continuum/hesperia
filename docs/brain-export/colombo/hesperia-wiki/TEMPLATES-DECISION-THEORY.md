# Template — Decision / theory narrative (Class A / Class B)

**ID:** HWIKI-DEC-01  
**Owners:** Ethan (+ Colombo fills theory body)  
**Use:** One short narrative page (or generator `notes`/`origin` block) per Class A/B branch decision.  
**Architecture ref:** [HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md](../HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md) §2c · charter [HWIKI-CHARTER-RATIFY-2026-07-23.md](../../../governance/HWIKI-CHARTER-RATIFY-2026-07-23.md)

---

## When to use

- Documenting **why** a science/symbol binds to **core** (Class A) vs stays on **TFP / MRT / COBALT** (Class B)
- Recording REJECTED / DEAD_ALGO_SURVIVED / BEYOND decisions that are **architectural**, not only formula-level
- Hub pages that answer: “which theories bind which branch?”

Do **not** use this template for raw symbol registers — use `generate_wiki.py` `add(...)` + code-cite template.

---

## Required fields (fill all)

```markdown
# <Decision title> — Class <A|B>

**Class:** A (cored / universal plumbing) | B (non-cored / branch-persistent)
**Branch / module:** core | TFP | MRT | COBALT | <other>
**Status vocabulary:** LIVE_FULL | LIVE_SUCCESSOR | PARTIAL | DEAD | DEAD_ALGO_SURVIVED | BEYOND | REJECTED | UNVERIFIED
**Wiki symbols touched:** [[Symbol1]], [[Symbol2]], …
**Code anchors:** `path/to/module.py` · call sites: `path:line` (≥1)

## What (one paragraph)

Plain-language: what decision or theory binding this page records.

## Where (placement)

- **Class A path:** branch experiment → proven generic → consolidate to `hesperia/modules/` + alias
- **Class B path:** branch MVP → register (alias / envelope / flag) → **stay branch-owned**; do not fold into sealed `/analyze`

## Why (legitimate reasoning)

Checkable rationale — cite module, spec, or audit. Not vibe.
- If REJECTED: what was tried, what broke, what survives elsewhere (if anything)
- If Class B: which specificity (psy / IT / attribution / corpus) forbids coring

## Theory lineage

- Author(s) + year (or “structural analogy only”)
- Extent: full | structural analogy | rejected-with-reason

## Relations

- **produced_from / inputs:** …
- **needed_by / consumers:** …
- **Cross-links:** related decision pages, Coverage-Ledger deferrals

## Exit note for this page

- [ ] Regen via `generate_wiki.py` if symbol pages changed
- [ ] HWIKI-03 re-ingest after material batch
```

---

## Class cheat-sheet (do not invent)

| Class | Means | Examples |
|-------|--------|----------|
| **A** | Universal engine plumbing — safe to consolidate into core | `dict_a`/`dict_b`, topology, nlp, metrics |
| **B** | Domain / theme / attribution — register only | TFP (psy), MRT (IT), COBALT (semantic attribution) |

**Agent rule:** Ask “universal plumbing or domain specificity?” before proposing a core merge.

---

## Mini examples (shape only — not new claims)

### Class A — shared fusion weight (shape)

- **Class:** A · **Branch:** core  
- **Why:** Centroid / fusion plumbing is domain-agnostic measurement  
- **Relations:** link α / E_cap / η wiki pages + `core/math` call sites  

### Class B — TFP clinical iteration labels (shape)

- **Class:** B · **Branch:** TFP  
- **Why:** Practitioner/session semantics must not pollute sealed `/analyze`  
- **Relations:** register envelope slot; do not merge clinical vocab into core metrics  

---

SIGNED: Spec (Ethan) | Class A/B decision-theory template | 2026-07-23 | HWIKI-DEC-01
