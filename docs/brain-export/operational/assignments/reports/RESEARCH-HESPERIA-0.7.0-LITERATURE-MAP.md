# RESEARCH — HESPERIA 0.7.0 Literature Map

**SPEC ID:** HESPERIA-RESEARCH-KSI-RELATION-REPAIR-0.7.0  
**Date:** 2026-06-14  
**Author:** Colombo (research)  
**Status:** Draft v0.1 — discussion/research only; no code  
**Scope:** Informs 0.7.0; does not change 0.6.3  

---

## 0. Inventory (what we actually used)

| Source | Role in this map |
|--------|------------------|
| Evolution tree pass 4 | CELL 11–15 boundaries, `applied=0`, contracts |
| [governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md) | Teacher JSON doctrine, MySQL ledger |
| Product payload `teacher_v063.py` | `update_edge_weight`, `update_cd_field`, `applied: 0` |
| CHROMA-1 `layer=books` | Ontology graph / KG modelling (KnowledgeSeeker, Wang & Li) |
| CHROMA-2 Papra (`documents`, ~9666 chunks) | General ML / complexity; **no KAN-titled papers indexed by name yet** |
| Operator spec arXiv links | KAN, GKAN, n-ary KG survey, HITL KG, LLM ontology (primary external anchors) |

---

## 1. KAN / GraphKAN / KANG

### Core papers (starter set — spec anchors)

| Paper | arXiv | Mechanism (extract, not hype) |
|-------|-------|-------------------------------|
| **KAN** (Kolmogorov–Arnold Networks) | [2404.19756](https://arxiv.org/abs/2404.19756) | Replace fixed activations on nodes with **learnable univariate functions on edges** (splines); interpretability claim = you can read Φ on each edge |
| **GKAN** (Graph Kolmogorov–Arnold Networks) | [2406.06470](https://arxiv.org/abs/2406.06470) | Transplant KAN edge functions into **graph** message passing |
| **KANG** (survey line) | (see GKAN citations) | Spline-based **edge activations** in GNN setting; same design axis as GKAN |

### Mechanisms relevant to HESPERIA

- **Static weight** `W_e` ≈ MLP linear edge weight.  
- **Transfer function** `Φ_e(x)` ≈ KAN edge activation: maps propagated signal along relation `e`.  
- **Minimum useful form for HESPERIA (research answer A2):** piecewise-linear or low-knot spline on **bounded domain**, with **saturation_limit** and **approval-frozen coefficients** — not online training loop.  
- **Full KAN training (score 0–1):** violates determinism + audit unless training happens **offline** and only **approved** Φ_e lands in prod graph.

### Rejected for HESPERIA 0.7.0

- End-to-end GraphKAN dependency as runtime library.  
- Stochastic gradient updates on canonical graph.  
- “KAN branding” in market copy.

### Terms safely borrowed

`edge activation`, `univariate transfer`, `spline knot`, `interpretable edge function`, `Φ_e residual` (Hesperia already uses Φ_e in KSI).

---

## 2. Knowledge graph completion / link prediction

### Core surveys (starter set)

| Topic | Anchor | Mechanism |
|-------|--------|-----------|
| **Link prediction in n-ary KGs** | [2506.08970](https://arxiv.org/html/2506.08970v1) | Predict **missing elements** in facts; ranking metrics; n-ary generalization beyond binary triples |
| Classical LP | TransE, RotatE, ComplEx (via surveys) | **Score candidate triples**; rank; threshold — embedding confidence, not prose |

### Mechanisms relevant to HESPERIA

| External | HESPERIA (verified 0.6.x) |
|----------|---------------------------|
| Missing relation | `missing_bridges[]`, `bridge_need_score` (KSI / envelope) |
| Weak relation | Low `W_e`, high Φ_e residual, incident flags |
| False bridge | Contradiction / replay failure after sandbox apply |
| Candidate ranking | Teacher proposals + deterministic replay score |
| Negative sampling | **Counterexample replay set** (benchmark statements that must not break) |

### Rejected

- Pure embedding confidence as **sole** approval gate (non-auditable on hex graph).  
- Auto-add top-k predicted edges without sandbox.

### Terms safely borrowed

`link prediction`, `completion`, `candidate edge`, `ranking metric`, `false positive edge`.

---

## 3. Ontology repair / ontology evolution

### Sources used

- CHROMA-1 books: *Knowledge Seeker* (Lim, Liu, Lee) — Ontology Graph, concept units, relations, versioning of learned ontology.  
- CHROMA-1 books: *Knowledge Engineering and Management* (Wang, Li) — ontology → **weighted concept network**, hierarchical vs non-hierarchical edges.

### Mechanisms relevant to HESPERIA

HESPERIA is closer to a **governed semantic graph / ontology** than to a free neural net:

| Ontology discipline | HESPERIA 0.7.0 translation |
|---------------------|----------------------------|
| Safe change types | Narrow allowlist: `add_edge`, `update_edge_weight`, `mark_rejected`, `mark_needs_human_review` |
| Consistency check | Deterministic replay + damage metrics |
| Versioning | Git SHA on graph + MySQL proposal ledger + rollback artifact |
| Migration | **Semantic migration** spec (like DB migration): proposal batch → sandbox apply → diff → approve → canonical bump |

### Rejected for first apply

- `split_concept`, `merge_concept`, `add_concept` (spec: chaos risk).  
- `update_cd_field` in **automatic** apply path (already in Teacher schema — **human-gated only** or defer to 0.7.1).

### Terms safely borrowed

`ontology evolution`, `refinement`, `consistency checking`, `change transaction`, `rollback`.

---

## 4. LLM-assisted KG / ontology construction

### Core papers (starter set)

| Paper | arXiv | Mechanism |
|-------|-------|-----------|
| Human-in-the-loop LLM + KG | [2602.05512](https://arxiv.org/abs/2602.05512) | User refines queries; **human preserves semantic rigor** |
| LLM from expert material | [2403.08345](https://arxiv.org/abs/2403.08345) | LLM builds ontology/KG from text — **more aggressive** than HESPERIA should allow at 0.7.0 |

### HESPERIA 0.6.3 doctrine (verified code)

- Teacher returns **numeric proposals only**; `FORBIDDEN_KEYS`: justification, reasoning, comment.  
- `compute_reweight_preview`: **`applied: 0` always** in 0.6.3.  
- IRC carries full envelope; OpenAI sees **sanitized teacher_packet** only.

### Allowed vs forbidden (Track D)

| Allowed around proposal | Forbidden in Teacher JSON |
|-------------------------|---------------------------|
| `incident_id`, `source_edge_id`, replay benchmark IDs | Prose justification |
| Before/after metric deltas (machine-readable) | Hidden chain-of-thought |
| `correlation_id`, `run_id`, MySQL foreign keys | Free narrative |

### Terms safely borrowed

`human-in-the-loop`, `proposal vs authority`, `suggestion layer`, `gate`.

---

## 5. Human-in-the-loop graph governance

Synthesis of §4 + evolution tree CELL 13:

```text
LLM role (0.6.3–0.7.0): numeric proposal generator only
Gate role: schema validation → sandbox → replay → score → human/approval MCP → mutate
Inspector role (0.7.0): show diff + scores + evidence handles, not LLM prose
```

---

## 6. Methods rejected for HESPERIA

| Method | Score | Why |
|--------|-------|-----|
| Full KAN/GNN training on live graph | 0 | Nondeterministic; opaque |
| GraphKAN as runtime dependency | 0–1 | Heavy; wrong organism |
| LLM free-form graph edit | 0 | Breaks audit |
| Embedding-only link prediction auto-apply | 0–1 | No deterministic replay |
| Concept split/merge in 0.7.0 | 0 | Scope chaos |
| Prose in Teacher JSON | 0 | Already forbidden |

---

## 7. Terms we can safely borrow (stable vocabulary)

Use spec §6 vocabulary in all 0.7.0 docs:

`semantic incident`, `missing bridge`, `weak bridge`, `false bridge`, `relation candidate`, `edge transfer function`, `Φ_e residual`, `activation mismatch`, `sandbox apply`, `replay set`, `semantic damage`, `approval gate`, `rollback contract`.

Avoid: understands, learns automatically, self-improves, AI fixes the graph.

---

**SIGNED:** Research (Colombo) | Hesperia 0.7.0 relation repair | 2026-06-14 | literature map v0.1
