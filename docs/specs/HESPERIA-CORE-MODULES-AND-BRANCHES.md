# Hesperia — core, modules, and scoped branches

**Canonical on dev repo:** `igareosh/hesperia` (this tree)  
**Updated:** 2026-06-20  
**Author:** Colombo (research) · operator-confirmed  
**Prod push:** `Atomic-Commits-Team/hesperia` — **docs only on dev** until Ethan release wave

---

## 1. Sealed core

The **runtime semantic engine** is **sealed**: `/analyze` + dict calculus + deterministic trace on the 12×24×250×6 grid.

- Code: `hesperia/engine/`, sealed assets under `assets/data/engine_dynamics_v060/`
- **No branch reopens core physics.** MRT, TFP, COBALT, and future work **branch understanding and outputs**, not measurement truth.

---

## 2. Modules in this repo (`hesperia/modules/`)

Registered aliases: `hesperia/engine/module_aliases.py`

| Alias | Module | Scoped result-oriented output |
|-------|--------|------------------------------|
| `dict_a` / `dict_b` | `hesperia.modules.core.*` | Token → sparse activations; surface math |
| `tfp` | `hesperia.modules.tfp.v1` | Clinical TFP: roadmaps, iterations, corpus compose |
| `topology` | `hesperia.modules.topology.core` | Topology-phase processing |
| `nlp` | `hesperia.modules.nlp.basic` | Baseline NLP |
| `metrics` | `hesperia.modules.metrics.base` | Metric hooks |

**Pattern:** core measures → module produces **purpose-scoped artifact** → envelope/MCP/LLM consumes.

Future on dev: `cobalt` → `runtime/cobalt/` or `hesperia.modules.cobalt.v1` (spec pending).

---

## 3. Sibling branches (separate repos / trees)

| Branch | Repo | Why separate |
|--------|------|--------------|
| **MRT** | `igareosh/hesperia_mrt` | 96-family tech/FPF grid; `sphere_rag`; not prod 288-fam |
| **COBALT** | spec → this dev repo | CHROMA-2 library RAG; corpus gate first |

Dev workspace on **altitudine:** `/data/workspaces/atomic-commit-hesperia` (this repo) · `/data/workspaces/hesperia_mrt` (MRT).

---

## 4. Whole-world aim → mandatory separation

We can realistically cover **many domains** (clinical, technical, library, agentic, academia) **only by separating**:

1. One **core** engine.
2. Many **scoped modules/branches**, each with own corpus and output contract.
3. **Independent MVP** completion per branch.
4. **Consolidation** when branches prove value — register modules, shared dict pipeline.

---

## 5. Read next

| Doc | Path |
|-----|------|
| Full architecture | [docs/brain-export/colombo/HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md](../brain-export/colombo/HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md) |
| Branch inventory | [docs/brain-export/colombo/HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md](../brain-export/colombo/HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md) |
| COBALT formalization | [docs/brain-export/colombo/COBALT_research_FORMALIZATION-v0_1.md](../brain-export/colombo/COBALT_research_FORMALIZATION-v0_1.md) |
| Brain pointers | cursor repo `CLIENTS/hesperia/README.md` |

---

`SIGNED: Researcher (Colombo) | dev repo core+modules+branches | 2026-06-20 | igareosh/hesperia`
