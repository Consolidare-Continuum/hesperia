# Hesperia — confirmed MVP branches (inventory)

**Updated:** 2026-06-20  
**Owner:** Colombo (research) · operator-confirmed branch model  
**Architecture (canonical):** [HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md](HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md) — modular branch approach; consolidation into systemic runtime semantic engine.  
**Purpose:** Branch inventory — **core Hesperia** vs **MVP branches/modules** (TFP, COBALT, MRT).  
**Product pointers:** [CLIENTS/hesperia/README.md](../../CLIENTS/hesperia/README.md) · [cluster/HESPERIA-REPOS-AND-HOSTS.md](../../cluster/HESPERIA-REPOS-AND-HOSTS.md)

---

## 1. Core vs branches

**Core Hesperia** = **runtime semantic engine** (shared, long-lived): hex geometry, sealed `/analyze`, modular engine kernel (`hesperia/engine/`), IRC Teacher envelope pattern, dict_a/dict_b calculus, 12×24×250×6 product geometry (288 families), deploy on `Atomic-Commits-Team/hesperia`.

**MVP branches** = purpose slices we **search, research, and build** in parallel. Each uses **most of core**; each has **own corpus, completion criteria, and optional repo**. Branches **do not block** each other.

**Module classes:** **Class A** (cored) — universal plumbing consolidated into core. **Class B** (non-cored) — domain/theme/attribution (psy/TFP, IT/MRT, COBALT attribution) — register at runtime, **do not** merge into sealed stack. See [HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md](HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md) §2c.

| Branch | Codename | Role | Repo / path |
|--------|----------|------|-------------|
| **TFP** | `tfp` | Clinical MVP — real practitioner, real RU sessions, specialized texts | **`igareosh/hesperia`** + **`Atomic-Commits-Team/hesperia`** · module `hesperia.modules.tfp` |
| **MRT** | `mrt` | Tech-corpus MVP — **Matrix Reasoner for Tech**, 12×8=**96** families, FPF/structural loop, L1–L9 `sphere_rag` | **`igareosh/hesperia_mrt`** · package `HESPERIA_MRT/` |
| **COBALT** | `cobalt` | Library RAG enhancer module — CHROMA-2 retrieval into runtime/MCP/LLM | Spec / future `hesperia.modules.cobalt` or `runtime/cobalt/` on dev repo |

---

## 2. TFP branch (clinical)

**Status:** Confirmed MVP · **for real** (sessions documented) · still MVP · completes on its own timeline.

| Item | Where |
|------|--------|
| Module | `hesperia/modules/tfp/` — `v1.py`, `seal.py`, `math_v1.py` |
| Session exports | `hesperia/modules/tfp/data/tfp_v1/inspector_exports/` (e.g. `13_tfp_s001_*`, `13_1-11-09-2023_*`) |
| RU dict packs | `assets/data/engine_dynamics_v060/dict_a/dict_a_tfp_ru_*.jsonl` |
| CHROMA-1 corpus | layer `tfp_corpus_ru` (not Papra CHROMA-2) |
| Runtime path | IRC Teacher 0.6.3 · hybrid retrieve → envelope → OpenAI Teacher |
| Prod URL | https://hesperia.prichindel.com/inspector/… |

**CHROMA-2 / COBALT:** optional later — TFP does **not** wait on library attribution. Join when chunk bounding shares `TFP_*` concept_ids.

---

## 3. MRT branch (tech / FPF structural)

**Status:** Confirmed MVP · own repo · **12×8=96** family model (not production 12×24=288).

**Repo:** `git@github.com:igareosh/hesperia_mrt.git` · HEAD **`711330f`** (2026-02-28) at inventory.

**Definition (from repo):** *HESPERIA MRT — 12×8=96 Tech-Corpus Pipeline.* Separate fork for **Matrix Reasoner for Tech** — Dict A (token → 96-family sparse activations), Dict B (surface math on 96-dim vector), E2E via `sphere_rag` structural loop. Primary feed: **FPF** (`fpf/input/FPF-Spec.md`).

| Item | Path in `hesperia_mrt` |
|------|-------------------------|
| MRT package | `HESPERIA_MRT/` — `run_e2e_mrt.py`, `MVP.md`, `PIPELINE_OVERVIEW.md`, `dicts/` |
| Reference impl | `sphere_rag/` — L1–L9 layers, guards, `hesperia_v03_core_math.py`, `analyze.py` |
| FPF / Dict A builder | `fpf/`, `scripts/build_dict_a_from_fpf.py`, `docs/SPEC__Dict_A_Builder_MRT12_96_v1_0.md` |
| Specs (canonical set) | Root `10_MASTER_SPEC__*`, `20_GEOMETRY__*`, `30_FAMILIES__*`, `34–42_SPEC` (L1–L9) |
| Doc index | `DOC_INDEX.md`, `OPERATIONAL_INDEX_v0_6.md` |

**MVP intent (`HESPERIA_MRT/MVP.md`):** demonstration value — decompose FPF structurally, extract signature, interpret in neutral technical language; **use MRT for MVP**, not full 12×288 ontology expansion.

**Relation to core product:**

| | Production (`igareosh/hesperia`) | MRT branch (`hesperia_mrt`) |
|--|----------------------------------|-----------------------------|
| Families | 12 × **24** = **288** | 12 × **8** = **96** |
| Focus | Sealed runtime, TFP clinical, 0.6.x | Tech corpus, FPF, sphere_rag L1–L9 |
| Push policy | §1 allowed remotes (dev/prod/backup) | See §5 below |

**COBALT:** MRT dict/matrix work is the **dictionary-first** path COBALT needs on CHROMA-2 — concepts and families before library chunk tags.

---

## 4. COBALT branch (library RAG module)

**Status:** Confirmed MVP module · spec only · **0→hero on CHROMA-2** default path.

| Item | Note |
|------|------|
| Role | Post-analyze RAG enhancer — `cobalt_retrieval` block; not main engine |
| Primary store | CHROMA-2 Papra `documents` via `colombo-library` MCP |
| Prerequisite | Corpus attribution via **dict_a → dict_b → area/family/concept** — not hand `topics\|…` on 1.23M chunks |
| TFP integration | Optional filter when TFP concept_ids exist on chunks; **not assumed at start** |

Ref: [COBALT_research_FORMALIZATION-v0_1.md](COBALT/COBALT_research_FORMALIZATION-v0_1.md) · [SPEC-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md](../../governance/SPEC-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md) (Ethan ratification pending).

---

## 5. Git / policy reconciliation (MRT repo)

**Brain policy today:** [governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md](../../governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md) §2a marks **`hesperia_mrt`** as *historical MRT-line workflow — archived; not an allowed push remote* (disconnected 2026-04-06).

**Operator intent (2026-06-20):** **MRT remains a confirmed MVP branch** with repo **`igareosh/hesperia_mrt`** (repo **live** on GitHub).

**Agent practice until policy amended:**

- **Read / clone** `hesperia_mrt` for MRT branch specs, `sphere_rag`, FPF, Dict A builder.
- **Daily product push** for runnable 0.6.x → only the **three** allowed Hesperia remotes (§1).
- **MRT branch work** → commit to `hesperia_mrt` when operator directs; **Grace + Ethan** to ratify push policy if MRT becomes active delivery again.

---

## 6. Cross-branch dependencies

```text
                    ┌─────────────────────────┐
                    │   Core Hesperia engine   │
                    │ 12×24×250×6 · /analyze   │
                    └───────────┬─────────────┘
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
    ┌───────────┐         ┌───────────┐         ┌───────────┐
    │ TFP branch │         │ MRT branch │         │  COBALT   │
    │ clinical   │         │ 96-fam FPF │         │ CHROMA-2  │
    │ sessions   │         │ sphere_rag │         │ RAG module│
    └─────┬─────┘         └─────┬─────┘         └─────┬─────┘
          │                     │                     │
          │    dict_a/b rebuild ◄┴────────────────────►│
          │         (shared ontology work)            │
          └──────── optional join via concept_id ─────┘
```

| From → To | Relationship |
|-----------|--------------|
| MRT → COBALT | Dict/matrix builder pattern; 96 vs 288 — reconcile before unified CHROMA-2 bounding |
| TFP → COBALT | Optional when `TFP_*` concepts on library chunks |
| MRT → TFP | Independent MVP timelines; share core math ideas, different family grids |
| All → CHROMA-2 | Attribution pipeline before COBALT is real |

---

## 7. Where to read (quick)

| Need | Open |
|------|------|
| Prod / dev layout | [cluster/HESPERIA-REPOS-AND-HOSTS.md](../../cluster/HESPERIA-REPOS-AND-HOSTS.md) |
| TFP module (code) | `igareosh/hesperia` → `hesperia/modules/tfp/` |
| MRT MVP + e2e | `igareosh/hesperia_mrt` → `HESPERIA_MRT/README.md`, `MVP.md` |
| MRT sphere_rag | `igareosh/hesperia_mrt` → `sphere_rag/README.md` |
| COBALT + CHROMA-2 corpus gap | Colombo session 2026-06-20 (dict rebuild before tags) |
| Push policy | [ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md](../../governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md) |
| Research threads (thesis) | [colombo_research/hesperia/README.md](README.md) |

---

## NEXT

| # | Action | Owner |
|---|--------|-------|
| 1 | Grace triage — ratify branch model; optional policy §2a amend for MRT MVP | Grace |
| 2 | Ethan — clarify 96 (MRT) vs 288 (prod) mapping or explicit “never merge grids” rule | Ethan |
| 3 | Felix — document clone path for `hesperia_mrt` on altitudine dev VM | Felix |
| 4 | Colombo — MRT `DOC_INDEX.md` ↔ brain `CLIENTS/hesperia` pointer row | Colombo |

---

`SIGNED: Researcher (Colombo) | Hesperia branch model TFP·MRT·COBALT | 2026-06-20 | consolidation doc`
