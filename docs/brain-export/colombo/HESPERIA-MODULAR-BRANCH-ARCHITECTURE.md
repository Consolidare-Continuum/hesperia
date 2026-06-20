# Hesperia — modular branch architecture (canonical)

**Updated:** 2026-06-20  
**Owner:** Colombo (research framing) · operator-confirmed direction  
**Audience:** Agents, Ethan, Felix, Gena, Grace — any Hesperia context  
**Branch inventory:** [HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md](HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md)

---

## 1. One sentence

**Hesperia is a runtime semantic engine at the core; we now build it through modular MVP branches that search, research, and ship independently — then consolidate into one systemic platform with a wider range of purposes.**

---

## 2. What Hesperia is (stable core)

**Since the engine was sealed** (0.6.x sealed `/analyze`, deterministic trace on grid), **all new purpose and understanding branches outward** — into modules, sibling repos, and research — **without reopening core physics**.

| Layer | Role | Status |
|-------|------|--------|
| **Runtime semantic engine (core)** | Sealed `/analyze` — hex geometry, dict_a/dict_b, trace on grid | **Prod** @ `e9eaa07` |
| **Modular engine kernel** | `hesperia/engine/`, `hesperia/modules/registry.py`, pipeline YAML | Dev · Spine A |
| **Runtime envelope** | IRC Teacher, hybrid retrieve, MCP/OpenAI paths | Prod 0.6.3 |
| **Ontology product geometry** | 12×24×250×6 (288 families) | Long-lived reference |

The core answers one question only: *where does this text land on the semantic grid, deterministically?*

**Modules and branches** answer different questions: *what result-oriented output does this purpose slice need?* (clinical session report, FPF structural read, library citations, inspection packet, …).

---

## 2a. Core + modules → scoped, result-oriented outputs

| Piece | Delivers | Scope |
|-------|----------|--------|
| **Core** | Engine trace, grid coordinates, sealed measurement | Universal input → grid |
| **Module / branch** | **Result-oriented artifact** for a domain | Explicitly scoped purpose |
| **Envelope** | Composes core + enabled module packets | One run, many scoped outputs |

Examples already in tree:

| Module / branch | Scoped output (result-oriented) |
|-----------------|--------------------------------|
| `hesperia.modules.tfp` | Clinical iteration roadmap, annotated transcript, TFP corpus compose |
| `hesperia.modules.core.dict_a/b` | Lexical → sparse family activations |
| **MRT** (`hesperia_mrt`) | 96-fam FPF structural interpretation, `sphere_rag` L1–L9 |
| **COBALT** (spec) | `cobalt_retrieval` — library evidence packet |
| Research (KSI, Nash, …) | Inspection / formalization drafts → future modules |

**Rule:** A module **must** declare its scope and its output shape. It **must not** redefine core measurement.

---

## 2c. Two module classes — cored vs non-cored

Not every module belongs in **core**. Not every branch module **should** fold back into sealed physics.

### Class A — **Core modules** (consolidated in core)

Universal engine plumbing. Proven on a branch → **merged back** into `hesperia/modules/` and `module_aliases.py` because they serve **all** inputs and domains.

| Module | Why cored |
|--------|-----------|
| `dict_a` / `dict_b` | Lexical → grid calculus — domain-agnostic |
| `topology` | Phase/geometry processing — shared |
| `nlp` | Baseline tokenization — shared |
| `metrics` | Measurement hooks — shared |

**Path:** branch experiments → generic mechanism proven → **consolidate to core** → registered alias, optional in pipeline YAML.

### Class B — **Non-cored modules** (branch-persistent)

**Intentionally not folded into core** — domain, theme, or attribution specificity would pollute universal measurement.

| Module / branch | Why **not** cored | Examples of specificity |
|-----------------|-------------------|-------------------------|
| **TFP** (`tfp`) | Clinical / **psy** — practitioner sessions, RU specialized texts | TFP iteration labels, session roadmaps |
| **MRT** (`hesperia_mrt`) | **IT** / tech — FPF, 96-fam grid, structural tech read | L1–L9 `sphere_rag`, FPF signatures |
| **COBALT** | **Semantic attribution** — library chunk bounding, Papra themes | `concept_id`, `area_name`, CHROMA-2 facets |
| Future domain branches | Legal, edu, org-specific themes | Own corpus, own output contract |

**Obvious reasons to stay non-cored:**

1. **Semantic attribution** — chunk/document bounding is corpus-specific, not engine physics.
2. **Theme / domain packs** — IT, psy, clinical, legal vocabularies and result shapes differ.
3. **Grid slices** — MRT 96-fam ≠ prod 288-fam; forcing merge breaks both.
4. **Corpus lifecycle** — library/clinical corpora evolve independently of sealed assets.

**Path:** branch MVP → **register** with core (alias, envelope slot, feature flag) → **stay branch-owned** — compose with core at runtime, **do not** ingest into sealed `/analyze`.

```text
                    SEALED CORE
                    dict_a/b · topology · nlp · metrics
                    universal measurement only
                           │
           ┌───────────────┴───────────────┐
           │                               │
    CONSOLIDATE BACK                 STAY NON-CORED
    (Class A)                        (Class B)
    generic plumbing                 domain / theme / attribution
           │                               │
    improved dict hook               TFP (psy)
    shared envelope pattern          MRT (IT)
                                     COBALT (attribution)
                                     future: legal, edu, …
                           │
                    RUNTIME COMPOSES
                    core trace + enabled branch packets
```

**Agent rule:** Ask *“Is this universal engine plumbing or domain/theme/attribution?”* — first → core consolidation candidate; second → **non-cored branch module**, register only.

---

## 2b. Whole-world scope → we separate on purpose

Hesperia can **realistically aim to encompass the whole world** of text and meaning — clinical, technical, legal, library, conversational, agentic — **only if we separate**:

1. **One sealed core** (shared measurement truth).
2. **Many scoped branches** (corpus, grid slice, output contract each).
3. **Independent completion** (MVP per branch; no monolith gate).
4. **Consolidation later** (register proven modules; shared dict pipeline where grids align).

Without separation, scope collapses into undeliverable monolith. **Branching is the realistic path to systemic coverage**, not a temporary compromise.

```text
  WHOLE WORLD (aim)
       │
       ├── core engine          ← one physics, all inputs
       ├── TFP branch           ← clinical results
       ├── MRT branch           ← tech/FPF results
       ├── COBALT branch        ← library RAG results
       ├── future branches …    ← each scoped, each shippable
       └── consolidation        ← systemic runtime, wider purposes
```

Everything else — clinical sessions, tech corpus, library RAG, thesis research — attaches as **branches**, not as replacements for the engine.

---

## 3. What changed (2026-06): modular branch approach

We **no longer treat Hesperia as a single monolithic product line** that must absorb every purpose before ship.

**New practice:**

1. **Search** — identify a purpose slice (clinical TFP, tech/FPF MRT, library COBALT, thesis threads).
2. **Research** — formalize in Colombo threads; spec module contract (Ethan).
3. **Build** — MVP branch on shared core; own corpus, repo optional, own exit criteria.
4. **Complete** — branch reaches its MVP gate **without blocking** siblings.
5. **Consolidate** — **Class A only:** proven universal plumbing merges to core; **Class B** registers at runtime, stays branch-owned.

```text
                    RUNTIME SEMANTIC ENGINE (core)
                    sealed /analyze · dict calculus · envelopes
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
    SEARCH / RESEARCH           BUILD MVP                  CONSOLIDATE
    (Colombo, specs)            (branches)            Class A → core
         │                          │                 Class B → register only
    TFP (psy)                 hesperia.modules.tfp    non-cored · envelope
    MRT (IT)                  hesperia_mrt            non-cored · sibling repo
    COBALT (attribution)      runtime/cobalt          non-cored · CHROMA-2
    Nash · Bell · KSI …       research → candidates   promote or stay branch
```

**Branches do not block each other.** TFP does not wait on COBALT. MRT does not wait on TFP. Core prod stays stable while branches advance.

---

## 4. Confirmed MVP branches (building now)

| Branch | Purpose slice | Build status |
|--------|---------------|--------------|
| **TFP** | Clinical — real practitioner, RU sessions, specialized texts | **Live module** on prod repo |
| **MRT** | Tech corpus — Matrix Reasoner, FPF, 96-family grid, `sphere_rag` | **Live repo** `hesperia_mrt` |
| **COBALT** | Library RAG — CHROMA-2 into runtime/MCP after corpus attribution | **Spec** → module on dev repo |

Detail: [HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md](HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md).

---

## 5. Research threads (search → future branches)

Colombo formalization threads are **not prod** — they **search** mechanisms that may become modules later:

| Thread | Searches for |
|--------|--------------|
| Nash | Semantic equilibrium, shadow dynamics |
| Bell (BCI-HP) | Consistency over hex paths |
| KAM | Perturbation stability |
| KAN / KSI | Kolmogorov-style semantic inspection |
| HSPR_discovery | Path / corpus-path discovery (thesis — not proven) |

Entry: [README.md](README.md) § Active threads.

**Rule:** Research stays in `colombo_research/` until Ethan + operator promote to branch or module spec.

---

## 6. Consolidation vision (systemic software, wider purposes)

**Goal:** At some point, mature branches merge into **one systemic Hesperia runtime** — same sealed semantic engine, **more registered modules**, **more corpora and consumers**, **wider purpose range** (clinical, technical, library, agentic MCP, academia).

**Not:**

- One big-bang rewrite.
- Merging family grids (96 vs 288) without explicit Ethan policy.
- Bypassing sealed `/analyze` for any branch.

**Yes:**

- **Class A:** Shared **dict_a → dict_b** pipeline improvements → core when grid-universal.
- **Class B:** Register non-cored modules — envelope slot, feature flag, MCP — **without** sealed asset merge.
- Envelope composition: engine trace + branch packets (`cobalt_retrieval`, TFP corpus, KSI gather, …).
- Each branch proves value **before** registration gate.

```text
Today                          Consolidation (target)
─────                          ──────────────────────
Core engine (prod)      →      Core engine (unchanged physics)
+ core modules          →      + consolidated Class A plumbing
+ TFP (psy, non-cored)  →      + registered clinical module (not in sealed stack)
+ MRT (IT, non-cored)   →      + registered tech branch / sibling repo
+ COBALT (attribution)  →      + registered library module (not in sealed stack)
+ research threads      →      + promoted inspectors or stay branch
                               = systemic runtime semantic platform
                                 core measurement + composed domain modules
```

---

## 7. Agent rules (clean context)

| Do | Don't |
|----|-------|
| Name the **branch** when discussing TFP, MRT, COBALT | Treat every Hesperia task as "the whole product" |
| Point to **core** for `/analyze` and sealed stack | Put branch corpus work inside sealed physics |
| Use this doc + branch model as **architecture SOT** | Duplicate branch tables in random chat/docs |
| Route implementation → Felix/Gena; spec → Ethan; research → Colombo | Block TFP on COBALT corpus or vice versa |
| Say **runtime semantic engine** for core; **branch/module** for slices | Call COBALT or MRT "the main engine" |
| Ask **Class A vs Class B** before merging to core | Fold psy/IT/attribution modules into sealed stack |

---

## 8. Where to read

| Need | Open |
|------|------|
| **This architecture (start here)** | This file |
| Branch inventory + repos | [HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md](HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md) |
| COBALT module spec | [COBALT/COBALT_research_FORMALIZATION-v0_1.md](COBALT/COBALT_research_FORMALIZATION-v0_1.md) |
| Brain pointers | [CLIENTS/hesperia/README.md](cursor repo CLIENTS/hesperia/README.md) |
| Repos / hosts | [cluster/HESPERIA-REPOS-AND-HOSTS.md](cursor cluster/HESPERIA-REPOS-AND-HOSTS.md) |
| Ethan COBALT task | [governance/TASK-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md](cursor governance/TASK-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md) |

---

## NEXT

| # | Action | Owner |
|---|--------|-------|
| 1 | Ethan ratify COBALT spec; publish branch register | Ethan |
| 2 | ~~Promote architecture into `igareosh/hesperia`~~ | **DONE** 2026-06-20 — `docs/brain-export/colombo/` + `docs/specs/HESPERIA-CORE-MODULES-AND-BRANCHES.md` |
| 3 | Grace triage branch model acknowledgment row (optional) | Grace |

---

`SIGNED: Researcher (Colombo) | Hesperia modular branch architecture | 2026-06-20 | canonical context`
