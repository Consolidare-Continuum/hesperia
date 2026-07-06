# Hesperia — core, modules, and scoped branches

**Canonical on dev repo:** `igareosh/hesperia` (this tree)  
**Updated:** 2026-06-20  
**Author:** Colombo (research) · operator-confirmed  
**Prod push:** `Atomic-Commits-Team/hesperia` — **docs only on dev** until Ethan release wave

---

## 1. Sealed core

The **runtime semantic engine** is **sealed**: `/analyze` + dict calculus + deterministic trace on the 12×24×250×6 grid.

- Code: `hesperia/engine/`, sealed assets under `assets/data/engine_dynamics_v060/`
- Deterministic structural computation is canonical under `core/`, with `core.domain` owning shared
  KME/domain measurement logic and `core.runtime` owning generic runtime modules.
- `hesperia.engine.kme` remains only as a narrowed compatibility package surface where explicitly
  protected legacy behavior still matters.
- Former `hesperia.modules.core` / `metrics.base` / `topology.core` shim files were removed once
  live code and tests converged to canonical `core.runtime.*`.
- **No branch reopens core physics.** MRT, TFP, COBALT, and future work **branch understanding and outputs**, not measurement truth.

---

## 2. Module classes — cored vs non-cored

### Class A — Core modules (consolidated in core)

Universal plumbing is consolidated under `core/runtime/`. Branch work that proves **domain-agnostic** value merges back here.

| Alias | Module | Cored because |
|-------|--------|---------------|
| `dict_a` / `dict_b` | `core.runtime.dict_*_module` | Lexical → grid calculus — all domains |
| `topology` | `core.runtime.topology_module` | Shared geometry phase |
| `nlp` | `hesperia.modules.nlp.basic` | Baseline tokenization |
| `metrics` | `core.runtime.metrics_module` | Shared measurement hooks |

### Class B — Non-cored modules (branch-persistent)

**Not folded into sealed core** — semantic attribution, theme, or domain specificity (IT, psy, clinical, library, …).

| Module / branch | Location | Why non-cored |
|-----------------|----------|---------------|
| **TFP** | `hesperia.modules.tfp` | **Psy / clinical** — sessions, RU specialized outputs |
| **MRT** | `igareosh/hesperia_mrt` | **IT / tech** — FPF, 96-fam, `sphere_rag` |
| **COBALT** | spec → `runtime/cobalt/` | **Semantic attribution** — CHROMA-2 bounding, themes |

**Non-cored modules register** with core (alias, envelope slot, flag) but **do not** enter sealed `/analyze` assets.

**Decision test:** *Universal engine plumbing?* → Class A, consolidate. *Domain / theme / attribution?* → Class B, stay branch.

---

## 3. Modules in this repo (registry)

Registered aliases: `hesperia/engine/module_aliases.py`

| Alias | Class | Scoped result-oriented output |
|-------|-------|------------------------------|
| `dict_a` / `dict_b` | **A** | Token → sparse activations; surface math |
| `topology`, `nlp`, `metrics` | **A** | Shared engine plumbing |
| `tfp` | **B** | Clinical TFP: roadmaps, iterations, corpus compose |

Future: `cobalt` → Class **B** (attribution / library).

**Pattern:** core measures → enabled modules produce **scoped artifacts** → envelope/MCP/LLM composes.

---

## 4. Sibling branches (separate repos / trees)

| Branch | Repo | Why separate |
|--------|------|--------------|
| **MRT** | `igareosh/hesperia_mrt` | 96-family tech/FPF grid; `sphere_rag`; not prod 288-fam |
| **COBALT** | spec → this dev repo | CHROMA-2 library RAG; corpus gate first |

Dev workspace on **altitudine:** `/data/workspaces/atomic-commit-hesperia` (this repo) · `/data/workspaces/hesperia_mrt` (MRT).

---

## 5. Whole-world aim → mandatory separation

We can realistically cover **many domains** only by separating:

1. One **sealed core** (Class A modules).
2. Many **non-cored branch modules** (Class B — IT, psy, attribution, …).
3. **Independent MVP** per branch.
4. **Consolidation** for Class A only; Class B **registers**, does not merge into sealed stack.

---

## 6. Read next

| Doc | Path |
|-----|------|
| **Mandatory read policy (dev agents)** | cursor brain `governance/HESPERIA-MODULAR-ARCHITECTURE-MANDATORY-READ.md` |
| Full architecture | [docs/brain-export/colombo/HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md](../brain-export/colombo/HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md) |
| Branch inventory | [docs/brain-export/colombo/HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md](../brain-export/colombo/HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md) |
| COBALT formalization | [docs/brain-export/colombo/COBALT_research_FORMALIZATION-v0_1.md](../brain-export/colombo/COBALT_research_FORMALIZATION-v0_1.md) |
| Brain pointers | cursor repo `CLIENTS/hesperia/README.md` |

---

`SIGNED: Researcher (Colombo) | dev repo core+modules+branches | 2026-06-20 | igareosh/hesperia`
