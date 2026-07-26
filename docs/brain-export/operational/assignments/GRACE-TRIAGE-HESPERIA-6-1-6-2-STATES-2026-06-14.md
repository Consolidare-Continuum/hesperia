# Grace triage — Hesperia 6.1 / 6.2 release states

**Date (UTC):** 2026-06-14  
**Triage:** Grace  
**Invoker:** igareosh — formalize states, gaps, expected next tasking  
**Refs:** [GRACE-HESPERIA-6-1-PRE-RELEASE-CLOSURE-2026-06-11.md](GRACE-HESPERIA-6-1-PRE-RELEASE-CLOSURE-2026-06-11.md), [governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md](../../governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md)

---

## 1. Release state model (formal)

| State ID | Name | Meaning | Status |
|----------|------|---------|--------|
| **6.1-ground** | Pre-release Python ground | HSPR + IPoV + GTP libraries in `tersagor`; specs promoted; **393** deterministic tests pass; `HybridRetrieveOutput` optional fields defined | **ACHIEVED** 2026-06-11 |
| **6.1-final** | Live runtime wire | Java engine implements `/analyze` contract; traversal emits live `interior_pov` + `gtp_coherence`; reflection smoke path on live engine | **IN PROGRESS** — gap rows **HES-61-01..03** + open **HSPR** |
| **6.2-spec** | KSI formalization | Brain draft `24_SPEC__Kolmogorov_Semantic_Inspection_v0_1`; task decomposition §19 | **ACHIEVED** 2026-06-13 |
| **6.2-ground** | KSI P0–P1 code | Φ_e engine, config/schemas, forward Expected_j, residuals, incident bundle | **BLOCKED** until **6.1-final** (needs live `Observed_j`) |
| **6.2-beta** | KSI P2 | Mirror cause, bridge need, MIRROR_DEFICIT incidents | After 6.2-ground |
| **6.2-rc** | KSI P3 | Teacher packet + acceptance gate schema (no live LLM) | After 6.2-beta |
| **6.2** | Release tag | KSI-P3 complete; gold tests green | Target after **KSI-01..18** |

**Rule:** Do not start **KSI-05+** until **6.1-final** exit criteria pass (live propagation observable).

---

## 2. State 6.1 — gap analysis

### 2.1 Achieved (6.1-ground)

| Area | Evidence |
|------|----------|
| Engine contract doc | `tersagor/docs/ENGINE-ANALYZE-CONTRACT.md` — HSPR-01/02 DONE |
| Reflection/Vigil Python | HSPR-04..07, 11, 13, 14 DONE — 33+ unit tests |
| IPoV | IPoV-01..07 DONE — 62 gold tests |
| GTP | GTP-01..08 DONE — 37 gold tests |
| Schema hooks | `interior_pov`, `gtp_coherence` on `HybridRetrieveOutput` |

### 2.2 Gaps (6.1 → 6.1-final)

| Gap | Blocker for | Owner | Row |
|-----|-------------|-------|-----|
| **Java `/analyze` does not yet implement contract** | HSPR-03, HSPR-19, live IPoV/GTP | Gena | **HES-61-01** |
| **IPoV/GTP not wired in live traversal pipeline** | Product surface, context_rag live packet | Gena | **HES-61-02** |
| **No E2E live bundle smoke** | Release sign-off | Felix | **HES-61-03** |
| Reflection storage paths | HSPR-10 persistence on disk | Abelard | **HSPR-12** (existing) |
| OpenAI smoke/integration | HSPR-08..10 | Felix | **HSPR-08..10** (existing; after 61-01) |
| Governance / ops | HSPR-15..18 | Ethan/Sophia/Marcus/Noah | existing P2 rows |

### 2.3 Exit criteria — 6.1-final DONE when

1. **HES-61-01** DONE — live engine returns contract-compliant `/analyze` JSON.
2. **HES-61-02** DONE — one live `HybridRetrieveOutput` includes populated `interior_pov` + `gtp_coherence`.
3. **HES-61-03** DONE — Felix gold: static input → live bundle asserts both blocks + HSPR-03 snapshot fields.
4. **HSPR-03** DONE — `HesperiaEngineBridge` smoke on live engine.

---

## 3. State 6.2 — gap analysis

### 3.1 Achieved (6.2-spec)

- KSI v0.1 spec in brain (`governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md`).
- Phased delivery KSI-P0..P5 mapped to releases.
- Task IDs **KSI-01..19** decomposed (§19).

### 3.2 Entry gate

| Prerequisite | Why |
|--------------|-----|
| **6.1-final** | KSI compares Expected vs **Observed** from live `invariant_activation` / `propagation_trace` |
| **Ethan** promotion of spec to `igareosh/hesperia` `docs/specs/` | Product repo SSOT |
| **HES-62-00** Grace wave meta | Rows live, inbox footer |

### 3.3 Execution order (6.2-ground → 6.2)

```
KSI-01 → KSI-02 → KSI-05 → KSI-06
         ↓ parallel
KSI-03, KSI-04 (Felix schemas/config)
         ↓
KSI-07, KSI-08 (mirror + bridge)
         ↓
KSI-09, KSI-10 (Felix bundle wire)
         ↓
KSI-11..13 (teacher packet, gate, sandbox)
         ↓
KSI-14..18 (fixtures, risk, runbook, env, gold tests)
```

**KSI-19** (Ava inspector UI) — **PAUSED** until 6.2 stable (KSI-P5 / 0.7.x).

---

## 4. active.md rows (this triage)

### Wave HES-61 (6.1-final)

| ID | Owner | Priority |
|----|-------|----------|
| HES-61-00 | Grace | P1 — wave meta |
| HES-61-01 | Gena | P1 — **blocker** |
| HES-61-02 | Gena | P1 — **blocker** |
| HES-61-03 | Felix | P1 — after 61-01/02 |

Existing **HSPR-03..19** remain; mapped to 6.1-final in §2.2.

### Wave HES-62 (6.2 / KSI)

| ID | Owner | Priority |
|----|-------|----------|
| HES-62-00 | Grace | P1 — wave meta (blocked until 6.1-final exit) |
| KSI-01..18 | per §19 | P1 blockers: 01,02,05; else P2 |
| KSI-19 | Ava | P2 **PAUSED** |

---

## 5. Expected tasking next (driver order)

| Order | Step | Owner | Why |
|-------|------|-------|-----|
| 1 | **HES-61-01** | Gena | Unblocks all live-engine work |
| 2 | **HES-61-02** | Gena | Product surface for IPoV/GTP |
| 3 | **HSPR-03** | Felix | First smoke on live wire |
| 4 | **HES-61-03** | Felix | 6.1-final exit bundle |
| 5 | **HSPR-08..10** | Felix | OpenAI path (parallel ok) |
| 6 | **HSPR-12** | Abelard | Storage paths |
| — | **HES-62-00** triage unlock | Grace | After 6.1-final exit |
| 7 | **KSI-01** | Gena | Start 6.2-ground |

**Current driver** should prefer **HES-61-01** once rows are live (supersedes HSPR-03 until engine exists).

---

## 6. Inbox footer

**Triage outcome:** PROJECT-CREATED — 2026-06-14 — [active.md](../../active.md) **HES-61-00..03**, **HES-62-00**, **KSI-01..19**.

---

SIGNED: Triage (Grace) | Hesperia 6.1/6.2 state formalization | 2026-06-14 | gap closure + KSI tasking
