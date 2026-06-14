---
task_id: "hesperia|ksi|operator-inspect"
active_md_anchor: "| KSI-16 |"
---

# SCRIPT-RUNBOOK — Hesperia KSI operator inspection (stub)

**Id**: `hesperia-ksi-inspection`  
**Purpose**: Operator procedure to review **Kolmogorov Semantic Inspection (KSI)** incidents, inspect Teacher packets (structure only, no clinical text), and route proposals through Acceptance Gate + Sandbox — per [SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md](../governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md).  
**Owner**: Marcus (KSI-16) · **Status**: VERIFIED 2026-06-14 (KSI-P0..P3 on alunel).  
**Data boundary**: [H62-064-KSI-DATA-BOUNDARY.md](../operational/assignments/reports/H62-064-KSI-DATA-BOUNDARY.md)

---

## Preconditions

- Hesperia **0.6.1-final** sealed — **Python** `/analyze` at `/data/hesperia/hesperia` (`:18880` on alunel).
- `HESPERIA_KSI_ENABLED=1` (when wired, KSI-09).
- Writable dirs: `/data/hesperia/ksi`, `/data/hesperia/reflection` (HSPR-11 / Abelard).
- Brain spec: `governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md`.

---

## 1. Locate KSI output

```bash
# From alunel — Hesperia product repo
cd /data/hesperia/hesperia
# Bundle run with ksi block (when present)
ls -lt assets/artifacts/tfp_pipeline_runs/ | head -5
# Standalone KSI packet drops (Abelard paths)
ls -la /data/hesperia/ksi/
```

Expect: `ksi` block in invariant_activation / bundle JSON, or `teacher_packet_*.json` under `/data/hesperia/ksi/` (naming TBD by KSI-11).

---

## 2. Review incidents (deterministic)

1. Open bundle or packet JSON.
2. Confirm **no** `input_text`, `raw_text`, or clinical prose (H62-064).
3. For each incident: note `incident_type`, `concept_id`, `Residual_j`, `Expected_j`, `Observed_j`.
4. Check `missing_bridges[]` ranked list — ids and scores only.

**Stop** if clinical text or PII appears → file under KSI-15 / H62-070; do not forward to LLM Teacher.

---

## 3. Acceptance Gate (0.6.2 — schema only)

When `proposals[]` exist (0.7.0+ live Teacher):

| Check | Operator action |
|-------|-----------------|
| Schema valid | Discard if JSON schema fails (KSI-12). |
| `confidence < τ_teacher` | Discard (default τ_teacher = 0.65). |
| `add_concept` / `remove_edge` | **PAUSE** — require igareosh approval. |
| Cycle / W_e range | Auto-discard per spec §13. |

In **0.6.2**: validate Teacher **packet** schema only (H62-052); no live proposals.

---

## 4. Sandbox (0.7.0)

Replay gold fixtures with one accepted proposal at a time (KSI-13). Operator triggers from Hesperia tooling when available.

---

## 5. Failure modes

| Symptom | Action |
|---------|--------|
| Empty `ksi` block | Confirm `HESPERIA_KSI_ENABLED`; check KSI-01..05 blockers. |
| Packet fails schema | Gena/Felix — serializer KSI-11 / schema KSI-04. |
| Clinical text in packet | Sophia boundary breach — halt, redact, fix serializer. |
| No write under `/data/hesperia/ksi` | Abelard — permissions on alunel (HSPR-12). |

---

## 6. References

- KSI spec §12–14, §18 phased delivery  
- [HES-62-2026-REGISTER.md](../governance/HES-62-2026-REGISTER.md) — H62-031..052  
- [SCRIPT-RUNBOOK-hesperia-tfp-bundle-inspection.md](SCRIPT-RUNBOOK-hesperia-tfp-bundle-inspection.md) — floor-6 bundle sanity  

---

SIGNED: Operator (Marcus) | KSI inspection runbook stub | 2026-06-14 | KSI-16 / H62 operator path
