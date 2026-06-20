# HESPERIA COBALT — research formalization v0.1

**Doc id:** `COBALT_research_FORMALIZATION-v0_1`  
**Codename:** `HESPERIA COBALT`  
**Status:** Research formalization (Colombo) — input to Ethan module-branch spec  
**Date:** 2026-06-20  
**Session source:** Colombo research chat (operator + Cursor), altitudine dev VM  
**Branch model:** [HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md](../HESPERIA-BRANCH-MODEL-TFP-COBALT-MRT.md)

---

## 0. INVENTORY — what exists (verified)

| Artifact | Status | Role re COBALT |
|----------|--------|----------------|
| Hesperia core `/analyze` (Spine B) | Prod `@ e9eaa07` | Measurement truth — **COBALT must not modify** |
| Modular engine (`hesperia/engine/`, `configs/pipeline.yaml`) | Dev repo | Spine A — optional `cobalt` module slot |
| Hybrid retrieve (`runtime/irc_teacher/analyze_adapter.py`) | Prod | Post-analyze hook pattern (same as KSI/IPoV) |
| `context_rag.py` + `cursor-context-rag` MCP | Brain / CHROMA-1 | Domain geometry + `hesperia_families` + `books` |
| `colombo-library` MCP + CHROMA-2 Papra | librarymaster · ~796/1010 docs · ~1.23M chunks | Library retrieval — **primary COBALT store** |
| TFP branch (`hesperia.modules.tfp`) | Confirmed MVP · real sessions | Optional consumer — not prerequisite |
| MRT branch (`igareosh/hesperia_mrt`) | Confirmed MVP · 12×8=96 | Dict-first path; grid differs from prod 288 |
| CHROMA-2 chunk metadata | **Misaligned** — `theme=general`, no Hesperia bounding | **Blocks useful COBALT until corpus pipeline** |
| COBALT code | **None** | Spec-only |

---

## 1. LOCATE — definitions

### 1.1 Branch placement

**COBALT** is a **confirmed Hesperia MVP branch** implemented as a **self-standing module**:

- **Not** the main engine.
- **Not** a replacement for TFP or MRT.
- **Enhancer:** optional read-only RAG layer piped into runtime envelopes, MCP, and OpenAI API paths (IRC Teacher, agents).

### 1.2 Formal definition

> **COBALT** (*Codename*) — a Hesperia **library RAG enhancer module** that composes a **`cobalt_retrieval`** packet from **CHROMA-2** (primary) and optionally **CHROMA-1** `context_rag`, bound to runtime context (user text, engine trace, optional branch filter), for downstream MCP/LLM consumption **without mutating sealed physics**.

### 1.3 Non-goals (v0.1 MVP)

- Graph mutation, Teacher `applied=1`, or sealed-stack changes.
- CHROMA-2 mass ingest or Papra librarian writes (Colombo/Abelard territory).
- Hand-tagging `topics|TFP|…` on 1.23M chunks.
- Mandatory TFP coupling at launch.

---

## 2. FORMALIZE — architecture

### 2.1 Integration modes (MVP stack)

| Mode | Mechanism | Consumer |
|------|-----------|----------|
| **A — Runtime adapter** | `runtime/cobalt/retrieve.py`; env `HESPERIA_COBALT_ENABLED=1` | IRC Teacher hybrid retrieve |
| **B — MCP** | `hesperia-cobalt` or extend `cursor-context-rag` | Cursor, tersagor OpenAI SDK |
| **C — Spine A module** | `cobalt` alias in `module_aliases.py`; `enabled: false` default | Research YAML only |

**Recommended MVP:** A + B. C deferred.

### 2.2 Query composition strategies

| Id | Input | Query | When |
|----|-------|-------|------|
| S0 | User text | literal | Baseline |
| S1 | `engine_result.trace` dominant concept/area/family | trace-bound string | **Primary when engine live** |
| S2 | TFP iteration labels + relational summary | composed (like `/inspector/tfp-corpus/compose`) | TFP branch only |
| S3 | S1 + `context_rag` families | dual-store fusion | Phase 2 |

### 2.3 Filter dimensions (post-attribution)

When CHROMA-2 chunks carry Hesperia bounding metadata:

- `concept_id`, `area_id`, `area_name`, `family_name`, `global_id`
- Optional `branch=tfp` → restrict to `TFP_*` concepts
- Optional `lang=ru|en`

Until attribution exists: semantic top-k only + manual post-filter (weak).

### 2.4 `cobalt_retrieval` packet (additive schema v0.1)

```yaml
cobalt_retrieval:
  version: "0.1-mvp"
  branch: null | tfp | mrt          # optional consumer hint
  store_primary: CHROMA-2
  query_composed: string
  strategy: S0 | S1 | S2 | S3
  filters: { lang, library_layer, concept_id, area_name, family_name }
  hits:
    - rank: int
      doc_id: string
      doc_name: string
      title: string
      creator: string
      chunk_index: int
      excerpt: string
      distance: float
      concept_id: string | null      # after attribution
      area_name: string | null
      family_name: string | null
      citation: string               # Papra/CHROMA-2 format
  retrieval_meta:
    top_k_requested: int
    hits_used: int
    max_chunks_per_doc: 2
    hybrid_rerank: false
  chroma2_status: ok | degraded | unavailable
  attribution_version: string | null
```

Failure: empty hits + `chroma2_status=degraded` — **Teacher unchanged** (same as empty KSI @ product-only).

### 2.5 Corpus prerequisite (critical finding)

**Embeddings ≠ alignment.** COBALT code without corpus work returns wrong hits (verified: RU TFP query → networking PDFs).

Required **before COBALT is real**:

1. Finish CHROMA-2 reindex (214 `OCR_req` policy).
2. **dict_a → dict_b → area/family/concept** batch attribution on chunks — not hand `papra_doc_meta` tags at scale.
3. Re-ingest with Hesperia-native metadata fields.
4. Eval set (50–200 Q→doc pairs) + QA template sign-off.
5. Reconcile **MRT 96-fam** vs **prod 288-fam** before unified bounding.

**Path B (default):** COBALT 0→hero on CHROMA-2 generic retrieval; TFP filter when attribution proves `TFP_*` on chunks.

---

## 3. DRAFT — outcomes by phase

### Phase 0 — Ethan spec + register (this handoff)

- Module-branch spec ratified.
- Grace triage register (`COBALT-00..n`) when Ethan/operator ready.
- Corpus gate documented as **hard dependency** for Phase 2+.

### Phase 1 — Corpus + attribution (parallel track)

| Outcome | Owner |
|---------|-------|
| Batch job: chunk text → dict_a/b → bounding JSONL | Felix/Gena |
| CHROMA-2 ingest writes `concept_id`, `area_name`, … | Abelard |
| Eval: TFP queries hit clinical docs | Colombo + Noah |

### Phase 2 — COBALT MVP module

| Outcome | Owner |
|---------|-------|
| `runtime/cobalt/retrieve.py` + feature flag | Felix |
| Extend `HybridRetrieveOutput` | Felix |
| MCP `get_cobalt_packet` | Felix |
| Smoke: envelope carries `cobalt_retrieval` | Felix |

### Phase 3 — Branch consumers

| Branch | COBALT use |
|--------|------------|
| **TFP** | S2 + `branch=tfp` filter when attribution ready |
| **MRT** | Shared dict pipeline; grid mapping spec first |
| **Core Teacher** | S1 trace-bound library citations in proposals context |

---

## 4. Relations to sibling branches

```text
Core Hesperia (/analyze)
    │
    ├── TFP branch ──────── clinical corpus, tfp_corpus_ru, sessions
    ├── MRT branch ──────── 96-fam dict builder (hesperia_mrt)
    └── COBALT branch ───── read-only CHROMA-2 RAG enhancer
              ▲
              │ requires attribution pipeline (dict/matrix)
              │
         CHROMA-2 Papra
```

| Relation | Rule |
|----------|------|
| COBALT → TFP | Optional; not blocking TFP completion |
| COBALT → MRT | MRT dict work feeds attribution design; grids must be reconciled |
| COBALT → core | Post-analyze only; never inside sealed `/analyze` |

---

## 5. Risks

| Risk | Mitigation |
|------|------------|
| Ship COBALT before corpus aligned | Phase gate: eval fail = module flag stays off |
| 96 vs 288 family grids | Ethan spec § grid policy |
| Policy: CHROMA-2 read-only | No Hesperia→CHROMA-2 ingest from runtime |
| OpenAI prompt leakage | Reuse Teacher sanitization; citations truncated |
| `hesperia_mrt` vs prod repo drift | MRT stays separate repo; COBALT reads CHROMA-2 only |

---

## NEXT

| # | Action | Owner |
|---|--------|-------|
| 1 | Ratify [TASK-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md](../../../governance/TASK-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md) → publish `SPEC-ETHAN-HESPERIA-COBALT-MODULE-BRANCH.md` | **Ethan** |
| 2 | Grace triage COBALT wave after Ethan spec (register + exit criteria) | Grace |
| 3 | Corpus attribution spike (dict pipeline on Papra sample) | Felix |
| 4 | 10-query TFP eval seed expansion | Colombo |

---

`SIGNED: Researcher (Colombo) | COBALT formalization v0.1 | 2026-06-20 | Hesperia branch research`
