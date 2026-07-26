# RESEARCH — HESPERIA Method Mapping (external → product)

**SPEC ID:** HESPERIA-RESEARCH-KSI-RELATION-REPAIR-0.7.0  
**Date:** 2026-06-14  
**Author:** Colombo  
**Status:** Draft v0.1  

---

## Mapping table

| External concept | Source field | Meaning | HESPERIA equivalent (verified) | Can use now? | Needs 0.7.0? | Risk |
|------------------|--------------|---------|------------------------------|--------------|--------------|------|
| KAN edge activation | KAN / GKAN | Learnable Φ on edge | `Φ_e`, KSI `phi_trace`, optional `transfer_function` metadata on relation | Language only | Φ_e inspectable params | Medium — confuse with training |
| MLP fixed activation | Baseline DL | Fixed node nonlinearity | Static `W_e` only (current default) | Yes | — | Low |
| KG link prediction | LP surveys | Rank missing triples | `missing_bridges[]`, `bridge_need_score` | Yes (0.6.2+) | Ranking → apply | Low if replay-gated |
| KG completion | Completion | Add missing facts | Relation **candidate** → sandbox `add_edge` | Propose (0.6.3) | Apply | Medium |
| Triple confidence | Embedding models | Score ∈ [0,1] | **Not authoritative** — use replay delta instead | No as sole gate | 0.7.0 composite score | High if alone |
| Negative sampling | LP training | Contrast false triples | **Counterexample replay set** (benchmark statements) | Design now | 0.7.0 gate | Low |
| Ontology repair | Ontology eng. | Governed graph change | Proposal types + approval + git SHA graph | Schema partial | Apply executor | Medium |
| Ontology evolution | Versioning | Migrate ontology | Semantic migration + rollback artifact | Document | 0.7.0 | Medium |
| Human-in-the-loop KG | HITL papers | User validates query/graph | IRC operator + approval MCP + `applied=0`→`1` | Yes (0.6.3 observe) | 0.7.0 approve | Low |
| LLM KG construction | LLM+ontology papers | LLM builds graph | **Rejected** — Teacher numeric only | Forbidden | — | High |
| LLM numeric proposal | 0.6.3 Teacher | Values-only JSON | `hesperia.teacher_response.v063`, `update_edge_weight` | Yes | Sandbox test | Medium |
| Sandbox / counterfactual | ML ops | Try change in copy | CELL 15 — **not built** | No | **Yes** | Low if deterministic |
| Before/after eval | CI / benchmarks | Regression test | Deterministic **replay set** on analyze traces | Partial (pytest) | 0.7.0 gate | Low |
| Graph neural message pass | GNN | Learn on graph | Deterministic propagation (existing engine) | Yes | Do not replace | High if replaced |
| Spline edge function | KAN | Piecewise edge map | Approved **`transfer_function`** record (frozen knots) | No | 0.7.0 optional | Medium |
| Inspector explainability | UI/UX | Show why approve | KSI-19 Pane 2: diff + metrics + evidence IDs | No UI | 0.7.0 | Low |

---

## Proposal action mapping (0.6.3 Teacher → 0.7.0 apply)

| Teacher `action` (exists in code) | 0.6.3 behaviour | 0.7.0 recommendation | Score |
|-----------------------------------|-----------------|----------------------|-------|
| `update_edge_weight` | Preview only; `applied=0` | **First allowed apply type** | 3 |
| `update_cd_field` | Preview only | Defer or **manual-only** (higher blast radius) | 1–2 |
| (future) `add_edge` | Not in 0.6.3 Teacher schema yet | Second allowed apply type | 2–3 |
| `mark_rejected` / `mark_needs_human_review` | Metadata only | Gate states, no graph write | 3 |

---

## Decision matrix (spec §9)

| Candidate method | Determinism | Audit | Small surface | Fits graph | No big training | Replay | Human OK | Inspector | **Score** |
|------------------|-------------|-------|---------------|------------|-----------------|--------|----------|-----------|-----------|
| KAN full training | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | **0–1** |
| KAN-inspired Φ_e (frozen) | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **2–3** |
| GraphKAN dependency | 1 | 1 | 0 | 2 | 0 | 1 | 1 | 1 | **0–1** |
| KG LP terminology | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | **3** |
| Ontology repair discipline | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **3** |
| LLM free-form graph edit | 0 | 0 | — | 0 | — | 0 | 0 | 0 | **0** |
| LLM numeric proposals | 2 | 3 | 3 | 3 | 3 | 2 | 3 | 2 | **2–3** |
| Sandbox replay gate | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | **3** |

---

## Hypothesis (spec §10) — tested against inventory

**Confirmed:** HESPERIA should **not** become a KAN system. It should borrow:

- **Language** from KAN (edge transfer Φ_e)  
- **Science** from KG completion (missing/weak/false bridge)  
- **Discipline** from ontology repair (typed changes, rollback)  
- **Runtime** from existing deterministic engine + 0.6.3 Teacher ledger  

**Sharper:** KAN = metaphor for edge behaviour; KG completion = missing-edge science; ontology repair = safety; Hesperia = audit gate.

---

**SIGNED:** Research (Colombo) | Hesperia 0.7.0 method mapping | 2026-06-14 | v0.1
