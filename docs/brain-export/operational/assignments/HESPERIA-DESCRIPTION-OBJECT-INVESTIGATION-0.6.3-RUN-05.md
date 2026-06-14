# Hesperia Description Object Investigation — Run 05 of 05 (final)

**Title:** 0.6.3 IRC Teacher application run — end-to-end trace, KSI/geometry, MySQL, parameters, bibliography  
**Version:** Hesperia 0.6.3 (description object investigation)  
**Product SHA:** `e9eaa07` · **Archive tag:** `122d45b` · **Integration ref:** tersagor `0149120` (evolution tree)  
**Index:** [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md) · **Prior runs:** [01](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md)–[04](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-04.md)

---

## Abstract

Run 05 closes the **description object investigation** with the **0.6.3 application arc**: Russian TFP statement → hybrid retrieve → `engine_run_envelope.v063` → sanitized Teacher request → OpenAI proposals-only response → `reweight_preview` with **`applied=0`** → MySQL ledger → IRC JSONL audit. This run integrates Runs 01–04: sealed stack (03) feeds `/analyze` (04); IRC Teacher wraps that sidecar plus optional KSI/geometry from integration host. **Graph mutation is explicitly deferred to 0.7.0.**

---

## 1. Application run — linear state machine

### 1.1 Orchestrator

**Product entry:** `runtime/irc_teacher/run.py` → `run_irc_teacher_path(text_ru, correlation_id?, channel?)`  
**Integration mirror:** `tersagor_agent/hesperia/irc_teacher_run.py` (same step order; `hybrid_retriever.retrieve` may add KSI/geometry post-steps on deployed tersagor).

**Precondition:** `HESPERIA_IRC_TEACHER=1` or `TERSAGOR_HESPERIA_IRC_TEACHER=1`.

| Step | State label | Function / emit | Output parameters |
|------|-------------|-----------------|-------------------|
| T0 | `INIT` | `correlation_id`, `run_id` (UUID in envelope) | `cid`, pending envelope |
| T1 | `RETRIEVE` | `retrieve(HybridRetrieveInput)` | `HybridRetrieveOutput` |
| T2 | `ENVELOPE` | `build_engine_run_envelope` | `engine_run_envelope.v063` |
| T3 | `IRC_START` | `emit_run_start` | JSONL `RUN_START` |
| T4 | `IRC_ENGINE` | `emit_engine_envelope` | JSONL `ENGINE_ENVELOPE` (chunked) |
| T5 | `TEACHER_REQ` | `build_teacher_request_from_envelope` | KSI packet (no raw RU in OpenAI body) |
| T6 | `IRC_TREQ` | `emit_teacher_request` | JSONL `TEACHER_REQUEST` |
| T7 | `TEACHER_CALL` | `call_openai_teacher_v063` | `teacher_response.v063` |
| T8 | `IRC_TRESP` | `emit_teacher_response` | JSONL `TEACHER_RESPONSE` |
| T9 | `PREVIEW` | `compute_reweight_preview` | list `{parameter_key, value_before, value_after, applied:0}` |
| T10 | `IRC_PREVIEW` | `emit_reweight_preview` | JSONL `REWEIGHT_PREVIEW` |
| T11 | `PERSIST` | `persist_teach_run` | MySQL rows (if DSN set) |
| T12 | `DONE` | `emit_run_done` | JSONL `RUN_DONE` status=`stored` |

**No backward transitions** in product code — failure raises or returns empty proposals; no retry loop.

### 1.2 Concomitant subsystems (same request, ordered)

```
[HTTP /analyze]          ← analyze_adapter (inside retrieve)
[Envelope build]         ← sync Python
[OpenAI API]             ← blocking HTTP (if flags on)
[MySQL INSERT]           ← sync (if DSN)
[IRC JSONL append]       ← sync file I/O
```

Reflection audit and graph apply are **out of scope** for 0.6.3 (Ethan spec §2).

---

## 2. Stage T1 — hybrid retrieve

### 2.1 Product path (`runtime/irc_teacher/analyze_adapter.py`)

```python
engine_result = POST {HESPERIA_ENGINE_URL}/analyze
    body: {"text": query, "mode": "standard"}
```

**Extract:**

| Field | Source |
|-------|--------|
| `engine_result` | sidecar or top-level; must contain `trace` for envelope roads |
| `ksi` | `engine_result.get("ksi")` — **empty @ product-only `e9eaa07`** |
| `interior_pov`, `gtp_coherence` | same — populated when integration enriches |

**Default URL:** `http://127.0.0.1:18880` (`HESPERIA_ENGINE_URL` / prod `:9005`).

### 2.2 Integration path (tersagor — governance spec)

Ethan spec order when full stack deployed:

```
/analyze (engine_result)
  → geometry post (IPoV, GTP)
  → KSI (Φ_e, incidents, missing_bridges, phi_trace)
  → optional reflection (off default)
```

**Verified:** brain stub `cluster/tersagor-h063/` mirrors envelope/teacher/mysql modules; **`hybrid_retriever`** lives on deployed tersagor workspace, not duplicated in product `@ e9eaa07`.

**KSI block shape** (when present):

```json
{
  "version": "0.1",
  "incidents": [{"type": "...", "concept_id": "...", "incoming_edges": [...]}],
  "missing_bridges": [{"bridge_need_score": 0.8, ...}],
  "phi_trace": {"SRC->TGT": {"W_e": 0.1, "R_e": 0.2, "phi_sat": 0.9, "type": "activates"}}
}
```

Ref: [governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md](../../governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md).

---

## 3. Stage T2 — `engine_run_envelope.v063`

**File:** `runtime/irc_teacher/engine_run_envelope.py`

### 3.1 Builder block

```python
build_engine_run_envelope(
    text_ru=text_ru,
    correlation_id=cid,
    hybrid_output=hybrid_out,
    lang="ru",
    input_kind="tfp_scientific_statement",
)
```

### 3.2 Top-level schema

| Key | Content | Operator visibility |
|-----|---------|---------------------|
| `schema` | `hesperia.engine_run_envelope.v063` | yes |
| `lang` | `ru` | yes |
| `correlation_id` | IRC thread id | yes |
| `run_id` | UUID | yes — MySQL PK |
| `input.text_ru` | **full Russian statement** | yes on IRC; **excluded from Teacher** |
| `input.kind` | `tfp_scientific_statement` | yes |
| `engine` | activation summary | yes |
| `ksi` | inspection block | yes when wired |
| `parameters` | `W_e` list from `phi_trace`, config ref | yes |

### 3.3 `engine` sub-object

| Field | Populated from | Purpose |
|-------|----------------|---------|
| `hesperia_ref` | git short SHA product repo | provenance |
| `integration_host_ref` | `TERSAGOR_ROOT` git SHA | provenance |
| `propagation_trace` | `engine_result.propagation_trace` or `trace[]` mapping | roads / hops |
| `areas`, `families`, `tfp_vector` | engine_result if present | macro state |
| `invariant_activation` | engine_result | concept activations |
| `interior_pov` | hybrid_output | geometry (IPoV) |
| `gtp_coherence` | hybrid_output | GTP path ids |
| `corpus_activations` | derived from `invariant_activation.concepts` | id + observed/expected scalars |
| `roads` | trace steps + `gtp_path_ids` | ordered path for operator |

**Example fixture:** product `release/v0.6.3/examples/example_engine_run_envelope_v063.json`.

---

## 4. Stage T5–T7 — Teacher request and response

### 4.1 Sanitization — `build_teacher_request_from_envelope`

**File:** `runtime/irc_teacher/teacher_packet.py`

**Included:** `ksi_version`, `session_id` (= run_id), `iteration_id` (= correlation_id), `incidents[]`, `missing_bridges[]` (ranked by `bridge_need_score`).

**Excluded (H62-064):** `input.text_ru`, raw book text, ENGINE-ANALYZE full trace.

**Per-incident enrichment:** `incoming_edges[]` with `{source, type, W_e, R_e}`.

### 4.2 OpenAI call — `call_openai_teacher_v063`

**Gates:**

| Condition | Behavior |
|-----------|----------|
| `OPENAI_API_KEY` missing | empty `proposals: []` |
| `HESPERIA_KSI_LLM_TEACHER != 1` | empty proposals (dry run) |
| both set | OpenAI chat, `temperature=0`, JSON object mode |

**System prompt (RU):** return only `hesperia.teacher_response.v063`; proposals = actions + numeric values; no justification.

**Model:** `HESPERIA_KSI_TEACHER_MODEL` default `gpt-4o-mini`.

### 4.3 Response validation — `validate_teacher_response_v063`

| Rule | Enforcement |
|------|-------------|
| `schema == hesperia.teacher_response.v063` | raise |
| `lang == ru` | raise |
| `proposals` is array | raise |
| keys in `{justification, message, explanation, reasoning, comment}` | **forbidden** |
| unexpected string fields on proposals | raise (allowlist: action, source, target, type, concept_id, field) |

**Exit gate G5:** gold tests reject `justification` ([HESPERIA-0-6-3-EXIT-CRITERIA.md](../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md)).

### 4.4 Proposal actions (0.6.3)

| `action` | Payload fields | MySQL `target_type` |
|----------|----------------|---------------------|
| `update_edge_weight` | source, target, type?, W_e_current, W_e_proposed, confidence | `edge` |
| `update_cd_field` | concept_id, field, value_current, value_proposed, confidence | `cd_field` |
| `add_edge`, `remove_edge`, `add_concept` | schema-defined | edge / concept / bridge |

**0.7.0 only:** applying proposals to graph files — not executed here.

---

## 5. Stage T9 — reweight preview

**File:** `runtime/irc_teacher/teacher_v063.py` — `compute_reweight_preview`

```python
for each proposal:
    if update_edge_weight:
        parameter_key = f"W_e:{source}->{target}"
        value_before = W_e_current; value_after = W_e_proposed
    if update_cd_field:
        parameter_key = f"{concept_id}.{field}"
    applied = 0  # ALWAYS in 0.6.3
```

**Doctrine:** `applied=0` on every preview row — observe and store **pending**; sandbox apply is CELL 15 / v0.7.0.

**Example:** `release/v0.6.3/examples/example_reweight_preview.json`.

---

## 6. Stage T10–T11 — IRC audit and MySQL

### 6.1 IRC emitter

**File:** `runtime/irc_teacher/irc_teacher_emitter.py`

| Type | Payload |
|------|---------|
| `RUN_START` | correlation_id, run_id, lang |
| `ENGINE_ENVELOPE` | full envelope (chunks if >3800 chars) |
| `TEACHER_REQUEST` | sanitized packet |
| `TEACHER_RESPONSE` | proposals JSON |
| `REWEIGHT_PREVIEW` | preview list |
| `RUN_DONE` | correlation_id, run_id, status |

**Default channel:** `#hesperia-teacher`  
**Audit file:** `$HESPERIA_TEACHER_AUDIT_DIR/irc-trace.jsonl` (default `~/ergo/logs/hesperia-teacher/`)

**Example JSONL:** `release/v0.6.3/examples/example_irc_trace.jsonl`.

### 6.2 MySQL ledger

**File:** `runtime/irc_teacher/mysql_ledger.py`  
**DSN:** `MYSQL_HESPERIA_DSN` (e.g. `mysql://user:pass@host/hesperia`)  
**Host:** prichindel Docker `mysql_db` (Abelard deploy)

| Table | Rows written | Status |
|-------|--------------|--------|
| `hesperia_teacher_run` | 1 per run — full JSON blobs | `stored` |
| `hesperia_activation_snapshot` | 0..N from `corpus_activations` | — |
| `hesperia_edge_snapshot` | 0..N from `ksi.phi_trace` | — |
| `hesperia_proposal` | 1 per proposal | **`pending`** |
| `hesperia_reweight_event` | spec table; product `@ e9eaa07` may omit separate insert (preview IRC-only) |

**No-op:** if DSN unset, `persist_teach_run` returns `run_id` without DB.

Schema DDL: [governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md) §5.

---

## 7. Environment flags — 0.6.3 arc (parameter table)

| Variable | When `1` / set | Effect |
|----------|----------------|--------|
| `HESPERIA_IRC_TEACHER` / `TERSAGOR_HESPERIA_IRC_TEACHER` | required | enable `run_irc_teacher_path` |
| `HESPERIA_ENGINE_ENABLED` | default on | HTTP analyze in retrieve |
| `HESPERIA_ENGINE_URL` | prod URL | target `/analyze` |
| `HESPERIA_KSI_ENABLED` | Teacher run | set when `ksi_enabled()` |
| `HESPERIA_KSI_LLM_TEACHER` | live LLM | OpenAI call; else empty proposals |
| `OPENAI_API_KEY` | secret | Teacher API |
| `HESPERIA_KSI_TEACHER_MODEL` | optional | default gpt-4o-mini |
| `MYSQL_HESPERIA_DSN` | prod | persist ledger |
| `HESPERIA_TEACHER_AUDIT_DIR` | optional | IRC JSONL path |
| `HESPERIA_ROOT` / `TERSAGOR_ROOT` | paths | git SHA in envelope |

Broader runtime vars: brain [HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md](../../HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md).

---

## 8. Worked example — Russian TFP statement (full trace)

**Input (RU):**

> Агрессия в семейной системе снижает способность к саморегуляции и усиливает защитные механизмы при нарушении границ.

**Kind:** `tfp_scientific_statement` · **lang:** `ru`

### 8.1 Retrieve

1. `POST /analyze` → Run 04 dual pipeline executes sealed stack twice internally for summary+sidecar.
2. `engine_result.trace[]` — marker-attributed steps (family_042, shame/aggression lexicon hits depend on assets).
3. If tersagor KSI wired: incidents e.g. `{type: residual_high, concept_id: SHAME}`.

### 8.2 Envelope excerpt (conceptual)

```json
{
  "schema": "hesperia.engine_run_envelope.v063",
  "correlation_id": "cid-demo-063-001",
  "run_id": "550e8400-e29b-41d4-a716-446655440000",
  "input": {"text_ru": "Агрессия в семейной системе…", "kind": "tfp_scientific_statement"},
  "engine": {
    "propagation_trace": [
      {"hop": 0, "concept": "AGGRESSION", "area_id": "A09", "activation": 0.72},
      {"hop": 1, "concept": "SELF_REGULATION", "area_id": "A04", "activation": 0.31}
    ],
    "hesperia_ref": "e9eaa07"
  },
  "ksi": {"incidents": [{"type": "residual_high", "concept_id": "SHAME"}], "phi_trace": {}},
  "parameters": {"W_e": [], "ksi_config_ref": "assets/data/ksi/ksi_config_v01.json"}
}
```

(Fixture-aligned — see product `release/v0.6.3/examples/`.)

### 8.3 Teacher request (OpenAI user message)

```json
{
  "ksi_version": "0.1",
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "iteration_id": "cid-demo-063-001",
  "incidents": [{"type": "residual_high", "concept_id": "SHAME", "incoming_edges": []}],
  "missing_bridges": []
}
```

**Note:** no Russian prose in this JSON.

### 8.4 Teacher response

```json
{
  "schema": "hesperia.teacher_response.v063",
  "lang": "ru",
  "proposals": [
    {
      "action": "update_edge_weight",
      "source": "AGGRESSION",
      "target": "SELF_REGULATION",
      "W_e_current": 0.12,
      "W_e_proposed": 0.58,
      "confidence": 0.84
    }
  ]
}
```

### 8.5 Reweight preview → MySQL

Preview IRC message → `hesperia_proposal.status='pending'`, `applied=0` in preview objects.

**Operator query (Marcus runbook):**

```sql
SELECT run_id, correlation_id, status, created_at
FROM hesperia_teacher_run ORDER BY created_at DESC LIMIT 5;

SELECT action, confidence, status FROM hesperia_proposal
WHERE run_id = '550e8400-e29b-41d4-a716-446655440000';
```

---

## 9. Five-run synthesis — complete runtime map

| Run | Spine / layer | Question answered |
|-----|---------------|-------------------|
| **01** | Architecture | What are the three spines? Global iteration? Entry points? |
| **02** | Modular kernel | How do YAML modules phase through `ctx`? |
| **03** | Sealed multiscale | How does text become A_hex, F, HSPR? |
| **04** | Shipping HTTP | How does `/analyze` expose SUMMARY + `engine_result.trace[]`? |
| **05** | 0.6.3 application | How does IRC Teacher wrap analyze + KSI + OpenAI + MySQL? |

**Single-request 0.6.3 byte path:**

```
RU text
  → [Tersagor/TG] run_irc_teacher_path
  → HTTP analyze (×1 in retrieve; ×2 if counting Run 04 dual server design separately)
  → sealed multiscale (inside analyze)
  → engine_run_envelope (operator sees RU + engine + ksi)
  → teacher_packet (KSI only → OpenAI)
  → proposals (pending)
  → IRC + MySQL (applied=0)
```

**Intentional non-actions (0.6.3):**

- No graph file writes
- No `reweight_preview.applied=1`
- No Session Inspector Pane 2 (0.7.0)
- No raw operator text to OpenAI

---

## 10. File map — 0.6.3 surface

| File | Role |
|------|------|
| `runtime/irc_teacher/run.py` | Application orchestrator |
| `runtime/irc_teacher/analyze_adapter.py` | HTTP retrieve |
| `runtime/irc_teacher/engine_run_envelope.py` | v063 envelope + teacher req builder |
| `runtime/irc_teacher/teacher_packet.py` | KSI packet serializer |
| `runtime/irc_teacher/teacher_v063.py` | OpenAI + validation + preview |
| `runtime/irc_teacher/irc_teacher_emitter.py` | IRC JSONL |
| `runtime/irc_teacher/mysql_ledger.py` | Persistence |
| `runtime/irc_teacher/flags.py` | Feature flags |
| `release/v0.6.3/examples/*` | Gold fixtures |
| `docs/specs/0.6.3-IRC-TEACHER-RUN.md` | Product spec mirror |

---

## 11. Bibliography and verified sources

| ID | Source | Use in investigation |
|----|--------|----------------------|
| B1 | Product repo `igareosh/hesperia` @ `e9eaa07` (alunel) | All Python block citations |
| B2 | Tag `0.6.3` / `122d45b` | [governance/HESPERIA-VERSION-TAG-REGISTRY.md](../../governance/HESPERIA-VERSION-TAG-REGISTRY.md) |
| B3 | [governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md) | Envelope + MySQL + acceptance |
| B4 | [governance/HESPERIA-0-6-3-EXIT-CRITERIA.md](../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md) | Gates G1–G5 |
| B5 | [operational/assignments/ENGINE-ANALYZE-CONTRACT-REFERENCE.md](ENGINE-ANALYZE-CONTRACT-REFERENCE.md) | trace[] contract |
| B6 | [operational/assignments/reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt](reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt) | CELL 13 narrative |
| B7 | `release/v0.6.3/examples/` on product | Offline fixtures |
| B8 | [HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md](../../HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md) | Env allowlist |
| B9 | KAN PDF (brain `operational/assignments/reports/hesperia-0.6.x/`) | 0.6.0–0.6.3 reasoning context |
| B10 | [governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md](../../governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md) | KSI theory pack |

**Unverified / future work:** live prod curl trace with full KSI on prichindel `:9005`; Java ENGINE-ANALYZE parity (Gena HES-61-01).

---

## 12. Study completion statement

The **Hesperia Description Object Investigation v0.6.3** (Runs 01–05) documents:

- **Per-step iteration** at modular, hex, HTTP trace, and IRC application layers
- **All primary Python files** on the shipping and 0.6.3 paths with block-level roles
- **Formulas** for hex step, product signals, HSPR, ENGINE-ANALYZE mapping, reweight preview
- **States and scopes** (`ctx`, GuardedContext, sealed dict, envelope schemas, MySQL pending)
- **Outputs as parameters** wiring tables across runs
- **Concomitant** sequential subsystems (no closed-loop mutation in 0.6.3)

**Promotion path:** Grace triage → Felix/Gena for `docs/specs/` merge on dev repo if operator wants single canonical markdown beside existing `0.6.3-IRC-TEACHER-RUN.md`.

---

## NEXT (Colombo)

1. [ ] Operator review — promote investigation to dev `docs/specs/HESPERIA-RUNTIME-DESCRIPTION-OBJECT-v0.6.3.md` — owner: **Grace triage → Colombo/Felix**
2. [ ] Wire full KSI/geometry into product `engine_result` or document tersagor-only boundary — owner: **Felix**
3. [ ] 0.7.0 description object (sandbox apply) — separate study when CELL 15 opens — owner: **Colombo**

**Verified exists:** Runs 01–05 committed; product IRC modules + examples @ `e9eaa07`; exit criteria sealed 2026-06-14  
**Still unverified:** live OpenAI call on prod with operator RU statement in this session

---

SIGNED: Research (Colombo) | Hesperia description object investigation Run 05 (final) | 2026-06-14 | v0.6.3
