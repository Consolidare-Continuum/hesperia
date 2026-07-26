# Hesperia 0.6.2 — release exit criteria (ratification)

**Task**: H62-063 (Ethan)  
**Date**: 2026-06-14  
**Status**: RATIFIED (governance doc) — product seal requires H62-072 Grace sign-off  
**Register**: [HES-62-2026-REGISTER.md](HES-62-2026-REGISTER.md)  
**Analysis**: [GRACE-HESPERIA-6-1-6-2-FULL-ANALYSIS-2026-06-14.md](../operational/assignments/GRACE-HESPERIA-6-1-6-2-FULL-ANALYSIS-2026-06-14.md)  
**KSI spec**: [SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md](SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md)

---

## 1. Scope of 0.6.2

**0.6.2** delivers the **KSI inspection layer** (KSI-P0..P3): Φ_e engine, expected/observed residuals, typed incidents, missing-bridge scoring, **LLM Teacher packet** (JSON, schema-validated), Acceptance Gate + Sandbox **schema** — **without** live LLM Teacher call (KSI-P4 → **0.7.0**).

Builds on **0.6.1** sealed runtime; does not replace Floor 6 propagation.

---

## 2. Exit gates (all required)

| # | Gate | Evidence |
|---|------|----------|
| G1 | **KSI-01..18** parent rows **DONE** in active.md (each closes when H62 children complete) | Workflow heartbeat + register |
| G2 | **H62-001..071** execution rows **DONE** (except PAUSED KSI-19 / 0.7.x UI) | [HES-62-2026-REGISTER.md](HES-62-2026-REGISTER.md) |
| G3 | **H62-072** Grace 0.6.2 wave sign-off report | operational/assignments/reports |
| G4 | Deterministic **pytest** (hesperia + ksi): **0 failures**; live smokes PASS or documented SKIP | CI / local alunel |
| G5 | Product artifacts committed: `assets/data/ksi/*`, `schemas/ksi_*`, `tersagor_agent/hesperia/ksi/` on `igareosh/tersagor` | Git tags / commits |
| G6 | **Data boundary** for Teacher packet ratified | [H62-064-KSI-DATA-BOUNDARY.md](../operational/assignments/reports/H62-064-KSI-DATA-BOUNDARY.md) |
| G7 | Operator runbook stub present | [SCRIPT-RUNBOOK-hesperia-ksi-inspection.md](../scripts/SCRIPT-RUNBOOK-hesperia-ksi-inspection.md) |
| G8 | **6.1-final** prerequisite: **Python** `/analyze` at `/data/hesperia/hesperia` implements [ENGINE-ANALYZE-CONTRACT-REFERENCE.md](../operational/assignments/ENGINE-ANALYZE-CONTRACT-REFERENCE.md) | HES-61-01..10 |

**G8 live evidence (HINS-12, 2026-06-14):** Governance seal ratified with workflow DONE rows; **prod `hesperia-api` was disabled** at inspection. HINS wave restored `:9005` shipping API + Django :8010. Re-verify after each prod deploy: `verify-hesperia-prod-https.sh`.

---

## 3. Explicitly out of 0.6.2

- Live `HESPERIA_KSI_LLM_TEACHER` API call (0.7.0 / KSI-P4).
- Sandbox repair **apply** to production graph (replay validation only in 0.6.2 scope per spec §14).
- Session Inspector Pane 2 (KSI-19 / KSI-P5).

---

## 4. Phased delivery map (spec §18)

| Phase | Release tag | 0.6.2 role |
|-------|-------------|------------|
| KSI-P0 | 0.6.2-alpha | Φ_e + unit tests |
| KSI-P1 | 0.6.2-beta | Residuals + incidents |
| KSI-P2 | 0.6.2-rc | Mirror + bridges |
| KSI-P3 | **0.6.2 sealed** | Teacher packet + gate schema |

---

## 5. CHANGE-LOG row (template)

When G1–G8 satisfied and H62-072 signed:

```
## 0.6.2 — KSI layer (sealed)
- KSI-P0..P3 complete per 24_SPEC__Kolmogorov_Semantic_Inspection_v0_1
- Teacher packet: structure + relations JSON; no live LLM in this release
- See governance/HESPERIA-0-6-2-EXIT-CRITERIA.md
```

---

## 6. Ratification

Ethan ratifies **this document** as the authoritative 0.6.2 exit definition. Product **sealed** status: **0.6.2 KSI-P0..P3 complete** per Grace H62-072 sign-off 2026-06-14.

## CHANGE-LOG

```
## 0.6.2 — KSI layer (sealed) — 2026-06-14
- KSI-P0..P3 complete per SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1
- Teacher packet: structure + relations JSON; no live LLM in this release
- Python engine /analyze contract; tersagor ksi/ + 49 pytest
- See governance/HESPERIA-0-6-2-EXIT-CRITERIA.md
```

---

SIGNED: Team lead (Ethan) | 0.6.2 exit criteria ratification | 2026-06-14 | H62-063
