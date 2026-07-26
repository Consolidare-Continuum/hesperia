# Ethan — Hesperia scope: founder inspection, repo structure, workflow observability

**Audience**: Operator (founder) + Ethan + Gena when assigned on Hesperia.  
**Purpose**: Lock **Ethan’s scope** for **personal / founder** use of Hesperia: inspect third-party or internal repos, recover **structure through Hesperia’s lens**, then **act on problems** in those repos and **feed improvements back into Hesperia**. **Non-goal**: replace product charter for team-wide Hesperia delivery; this is the **founder loop** and how we evolve the engine from real application.

---

## 1) Scope (in)

1. **Enhance Hesperia** so it remains the **inspection substrate** for founder-led work (modules, dicts, runners, visualization, gates — as already tracked in Hesperia tasks).
2. **Apply Hesperia to a target repo** (clone/mirror, docs, code, configs, history) to produce **structured views**: what the repo *is* in terms of risks, themes, gaps, and alignment signals — **vision by Hesperia**, not a generic summary.
3. **After inspection**, **address problems** in the **target repo** (fixes, refactors, missing docs, workflow alignment) and/or **enhance Hesperia** when the gap is in **our** pipeline (new module, ontology slice, exporter).
4. **Observe two layers** on every serious application:
   - **Outcomes**: artifacts produced (reports, vectors, matrices, decisions).
   - **Workflow in application**: which Hesperia path ran (e.g. C→A→B, module id, profile, gates), **inputs/outputs per step**, **determinism/hash** where applicable, **who/what executed** (human, Cursor, cron). This is **meta-observability**: we improve the **process of applying** Hesperia, not only the final slide or score.

---

## 2) Scope (out)

- **Not** claiming Hesperia replaces cluster ops, billing, or client delivery ownership.
- **Not** skipping governance: frozen team files unchanged by assistants; founder/Ethan packets live in **operational/** or **governance/** per existing rules.
- **Not** collapsing “workflow observation” into vanity metrics — log **concrete** run records (timestamped JSON or append-only run logs) tied to a **target repo id** and **Hesperia version/module set**.

---

## 3) Operating loop (founder)

```
Target repo (mirror) → Hesperia run (declared profile/module/config)
    → structured outputs + workflow trace
    → interpret gaps / problems
    → actions: target repo fixes OR Hesperia enhancement
    → re-run same profile → compare outcomes + workflow deltas
```

**PG-SA** ([ETHAN-PG-SA-PARAMETER-GOLF-PLAN-2026-04-03.md](ETHAN-PG-SA-PARAMETER-GOLF-PLAN-2026-04-03.md)) is **one instance**: Parameter Golf mirror + competition ontology + bounded experiment matrix; same loop applies.

---

## 4) Workflow observability — minimum contract (MVP)

For each founder inspection **batch**, retain:

| Field | Meaning |
|-------|---------|
| `hesperia_ref` | Commit or tag of Hesperia used |
| `target_repo` | URL or path + commit |
| `profile_or_module` | What was run (e.g. `pg_sa`, `tfp`, `llm_audit`) |
| `pipeline_trace` | Ordered steps with hashes or artifact paths |
| `outcome_artifacts` | Links/paths to reports, JSON, maps |
| `operator_notes` | What changed in target repo or in Hesperia next |

**Ethan**: treat absence of `pipeline_trace` as **incomplete** for founder runs intended to drive Hesperia product learning.

---

## 5) Handoffs

- **Implementation** in Hesperia codebase: **Gena** when assigned; paths per [CLIENTS.md](../../CLIENTS.md) and `CLIENTS/hesperia/`.
- **Infra** for mirrors, services, disk: **Abelard**.
- **Triage / active.md**: **Grace** when the operator wants tracked rows.

---

## 6) Success

- Founder can **see structure** of an unfamiliar repo through Hesperia outputs, not only a narrative blurb.
- Each cycle produces **both** improved **target** understanding/fixes **and** a **record of how Hesperia was applied**, so the next enhancement is evidence-based.

---

SIGNED: Governance (Ethan) | founder Hesperia inspection + workflow observability scope | 2026-04-03 | operational
