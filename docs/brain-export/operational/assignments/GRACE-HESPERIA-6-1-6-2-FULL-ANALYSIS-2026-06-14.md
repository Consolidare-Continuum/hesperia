# Grace — Hesperia 0.6.1 / 0.6.2 full analysis

**Date (UTC):** 2026-06-14  
**Triage:** Grace  
**Invoker:** igareosh — destination, sealed runtime, LLM teaching of structure/relations, full integration  
**Register:** [governance/HES-62-2026-REGISTER.md](../../governance/HES-62-2026-REGISTER.md) (**H62-001..072** + **HES-61-04..12**)

---

## 1. Destination (what “done” means)

| Release | Destination | Sealed when |
|---------|-------------|-------------|
| **0.6.1** | **Geometry-safe semantic traversal kernel** at runtime — live engine, live bundle, IPoV + GTP on `HybridRetrieveOutput`, reflection path optional | **6.1-final sealed**: HES-61-01..12 + HSPR-03 DONE; 393 + new live smokes green |
| **0.6.2** | **KSI inspection layer** on Floor 6 — Φ_e, Expected/Observed residuals, typed incidents, missing-bridge scoring, **LLM Teacher packet** (structure + relations on concepts), Acceptance Gate + Sandbox schema | **0.6.2 sealed**: KSI-P0..P3 complete per spec §18; H62-001..071 DONE; **no live LLM call** (that is **0.7.0** KSI-P4) |

**Full integration** = one live `HybridRetrieveOutput` / audit bundle carries: `trace`, `interior_pov`, `gtp_coherence`, optional `reflection_*`, optional `ksi` block — all env-gated, deterministic core, additive fields only.

---

## 2. Existing tested states (inventory)

### 2.1 DONE and tested (do not rework)

| Wave | IDs | Tests | Runtime |
|------|-----|-------|---------|
| HSPR Python | 01–02 doc, 04–07, 11, 13–14 | 33+ reflection unit | Standalone libs |
| IPoV | 01–07 | 62 gold | Standalone; schema hook on output |
| GTP | 01–08 | 37 gold | Standalone; schema hook on output |
| **Total deterministic** | — | **393 pass** | No live engine/OpenAI |

### 2.2 OPEN — mapped to destination

| Bucket | Rows | Blocks |
|--------|------|--------|
| **6.1-final wire** | HES-61-01..03, HES-61-04..12, HSPR-03,08–10,12,19 | Live Java engine, OpenAI key, alunel paths |
| **6.1 governance** | HSPR-15..18 | Ratification, boundary, runbook, Chroma |
| **6.2 epic** | KSI-01..18 | Parent anchors; execution = **H62-001..072** |
| **6.2 UI** | KSI-19 | PAUSED → 0.7.x |

---

## 3. Runtime architecture (sealed bundle)

```
Input text
    → Floor 0–6 (Java engine + Python hybrid_retriever)     [6.1-final]
    → interior_pov (IPoW step)                              [HES-61-02/07/08]
    → gtp_coherence (Ψ, GTPA)                               [HES-61-02/07/08]
    → reflection loop (optional, HSPR)                      [HSPR-08..10, env flag]
    → KSI layer (optional, HESPERIA_KSI_ENABLED)            [H62-020..022]
         Φ_e → Expected_j → Residual_j → incidents
         → mirror + bridge → Teacher packet (JSON, no LLM in 0.6.2)
         → Acceptance Gate → Sandbox schema (replay in 0.6.2)
    → HesperiaAuditRecord + context_rag packet
```

**LLM teaching (0.6.2 scope):** structured **Teacher packet** teaches graph **structure** (areas, families, active concepts) and **relations** (edge types, W_e, R_e, incoming_edges, missing_bridges). Packet is serialized and schema-validated; **live LLM Teacher call** = KSI-P4 / **0.7.0** (H62-033 templates ready in 0.6.2).

---

## 4. Expected test matrix (sealed runtime)

| Layer | Test type | Owner rows | Pass criterion |
|-------|-----------|------------|----------------|
| 6.1 contract | Engine bridge smoke | HSPR-03, HES-61-03, HES-61-06 | Live `/analyze` JSON matches contract |
| 6.1 wire | IPoV/GTP on output | HES-61-07/08, HES-61-09 | `interior_pov` + `gtp_coherence` populated live |
| 6.1 reflection | OpenAI smokes + loop | HSPR-08..10 | Schema-strict LLM JSON; full loop one input |
| 6.1 relations | Overlay ping-pong | HSPR-19, HES-61-10 | Trace hash differs with/without overlay |
| KSI P0 | φ_e gold | H62-006..008, H62-049 | Deterministic Φ_e on fixtures |
| KSI P1 | Expected/residual | H62-050..051, H62-057 | Known Expected_j, incident type |
| KSI P2 | Mirror/bridge | H62-052, H62-025..028 | MISSING_BRIDGE, MIRROR_DEFICIT |
| KSI P3 | Teacher/gate | H62-053..055 | Packet validates; gate accept/reject |
| Regression | Full suite | H62-059 | 393 + all new ksi tests green |
| Integration | Env gates | H62-056..057 | KSI off → no block; on → populated |

---

## 5. Parallel execution lanes (today)

| Lane | Who | Can start now | Delivers |
|------|-----|---------------|----------|
| **A** | Gena | **Yes** | HES-61-01/02, H62-001..008 (R_e + φ_e — no live engine) |
| **B** | Felix | **Yes** | H62-009..012 schemas, H62-019..021 models, H62-049..055 gold scaffolds |
| **C** | Gena+Felix | After A partial | H62-013..022 bundle wire, HES-61-03/07/08 |
| **D** | Team gov | **Yes** | H62-063..071, HSPR-15..18 |
| **E** | Abelard | **Yes** | HSPR-12, H62-069 paths |

**Hard dependency:** KSI **Observed_j** from live propagation (H62-013+, H62-046) requires **HES-61-01** engine trace. P0 (φ_e, assets) and P3 schemas run **in parallel** today.

---

## 6. 0.6.2 close criteria (Grace)

**0.6.2 DONE** when:

1. All **KSI-01..18** parent rows DONE (each closes when its H62 children DONE).
2. **H62-072** Grace wave sign-off.
3. **Ethan H62-064** ratifies 0.6.2 exit in CHANGE-LOG.
4. `pytest` ksi + hesperia: **0 failures** on deterministic suite; live smokes documented PASS or SKIP with reason.
5. Product repo: `assets/data/ksi/*`, `schemas/ksi_*`, `tersagor_agent/hesperia/ksi/` committed on `igareosh/tersagor`.

**Out of 0.6.2 (0.7.0):** live `HESPERIA_KSI_LLM_TEACHER` call, sandbox repair loop apply, Inspector Pane 2 (KSI-19).

---

## 7. Tasking summary

| Set | Count | IDs |
|-----|-------|-----|
| 6.1-final expansion | 9 | HES-61-04..12 |
| 0.6.2 granular execution | 72 | **H62-001..072** |
| Epic parents (existing) | 18 | KSI-01..18 |
| **New rows this triage** | **81** | above HSPR coarse set |

**Live rows:** [active.md](../../active.md) · **Register:** [HES-62-2026-REGISTER.md](../../governance/HES-62-2026-REGISTER.md)

---

## 8. Inbox footer

**Triage outcome:** PROJECT-CREATED — 2026-06-14 — [active.md](../../active.md) **HES-61-04..12**, **H62-001..072**; register [HES-62-2026-REGISTER.md](../../governance/HES-62-2026-REGISTER.md).

---

SIGNED: Triage (Grace) | Hesperia 0.6.1/0.6.2 full analysis + 81-task wave | 2026-06-14 | destination + sealed runtime + LLM teaching packet scope
