# Hesperia Control Layer v1 — Ethan tasking packet (merged spec)

**Date:** 2026-03-27  
**Role:** Ethan (architect)  
**Status:** **TASKING LIVE** — `active.md` rows **HC-*** OPEN; execution host **`/data/hesperia/hesperia`**; tracking **cursor** repo.

## Intent

Operationalize the operator’s **HESPERIA CONTROL SPEC v1.0** **after Ethan validation**: no parallel “second constitution.” Work **merges into** CD v1, existing resolver/DLCR contracts, `MODEL_CARD` hook order, and release gates. Ref: prior Ethan reply (merge rules, Tier 1/2/3, non-viable items struck).

## Non-negotiables (frozen)

1. **Single owner per control mechanism** — no duplicate competition math (CD `co_occurs` / excludes **vs** separate `concept_competition.py` without ADR).
2. **Pipeline truth** — `A → B → CD → C_agg → Topology` per `docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md`; any new stage = **documented hook** + **versioned config**.
3. **Modifier order** — **Ethan HC-ETHAN-01** locks **pre-CD lexical** vs **CD-internal**; HC-03 (Gena) starts **after** that freeze.
4. **No hot-path corpus prevalence** until offline calibration artifact + `cd_calibration_vN` (concept normalization slice deferred).
5. **Cross-plane agreement** — release/audit metric only until each plane exposes **comparable** schema (Olivia HC-09).

## Dependency graph (summary)

```text
HC-GRACE-01 (triage) ─┬─► HC-ETHAN-01 (freeze appendix + modifier order)
                      │
HC-ETHAN-01 ──────────┼─► HC-03 (Gena modifiers), HC-04 (Liam hooks)
                      │
HC-01 (Noah) ─────────┴─► independent Tier-1 track (provenance)
HC-02 (Marcus) ─────────► CD Phase 2 competition math (after HC-ETHAN-01 for scope)
HC-05 (Gena dominance) ──► after C_agg contract clear (Olivia may reference CD-T11 extensions)
HC-06–HC-07 ───────────► fixtures + CI after HC-01/HC-05 produce stable traces
HC-08 (Gena) ──────────► parallel diagnostic track
HC-09 (Olivia) ────────► gate contract (parallel)
HC-10 (Ava) ───────────► guard in same PR train as HC-03/HC-05 or first touch
```

## Task table (executable)

| ID | Owner | Task | Acceptance (short) |
|----|--------|------|---------------------|
| **HC-GRACE-01** | Grace | Triage this packet: confirm HC-* rows in `active.md`, resolve owner collisions, order START after CD-T01–T20 closure (DONE). | OPEN rows visible; no duplicate HC owner conflict; note blockers in Link column if any. |
| **HC-ETHAN-01** | Ethan | Freeze **HESPERIA_CONTROL_MERGED_v1** appendix in cursor: execution order vs `lexical_concept/pipeline.py` + MODEL_CARD; **modifier placement** decision; anti-duplication matrix vs CD v1 fields. | One markdown under `operational/assignments/` or `docs/governance/working/` + link from this packet §Implementation log. |
| **HC-01** | Noah | **B↔A provenance + validation envelope** — align to existing resolver / DLCR output schema; per-activation trace: token ids, match types, support scores, `is_valid`, rejection reason; no orphan JSON parallel to `resolver_output`. | Example run manifest + ≥3 gold segments; deterministic fields documented. |
| **HC-02** | Marcus | **Unified competition policy** for CD Phase 2 — merge “concept competition” with `co_occurs` / winner policy; **single** suppression function + tie-break + determinism proof (extends CD-T16 spirit). | ADR or `docs/governance/cd_v1/` appendix; Marcus review sign-off. |
| **HC-03** | Gena | **Modifier MVP** — after HC-ETHAN-01: one binding path only; **negation + one damping class**; deterministic binding rules; tests. | Unit + fixture; no full taxonomy until entity/span contract extended. |
| **HC-04** | Liam | **Runner hook order** — document and implement wire order per HC-ETHAN-01 + MODEL_CARD (no prod bypass); feature flag if needed. | Integration test; `HESPERIA_CD_*` / adjacent env documented. |
| **HC-05** | Gena | **Strict dominance** — segment-level policy on **declared** aggregation output (areas or public projection per product contract); versioned thresholds; outcome class enum. | Config + tests; does not break hex-causal product path claims. |
| **HC-06** | Noah | **Fixtures** — golden + perturbation (length, boilerplate, negation flip) for HC-01 + HC-05 traces; hash or structured diff harness. | `tests/` paths in Hesperia; README slice. |
| **HC-07** | Daniel | **CI gates** — extend determinism/dominance/length smoke as applicable; no flaky network. | Workflow green; documented in CI README or runbook. |
| **HC-08** | Gena | **Unmapped token diagnostic engine** — ranked reports only; **no** dictionary mutation in pipeline. | CLI or module + sample report artifact in repo or test fixtures. |
| **HC-09** | Olivia | **Cross-plane agreement** — define **comparable** plane output schema subset + pass/warn/fail policy for release gate (not fake numeric agreement). | Contract doc + example JSON; links to existing calibration_release_gate / audit. |
| **HC-10** | Ava | **Read-only guard** — new control modules must not mutate A/B lexical or ontology resources (extend CD-T10 pattern if needed). | Conformance test or static check; documented. |

## Deferred (explicit — not OPEN until Ethan+Grace reopen)

- **Concept normalization** Layer B/C (corpus prevalence, family density offline) — calibration bundle + batch job.
- **Interaction compilation** full four-artifact set — **CD Phase 3** single compiler track (no parallel `interaction_compiler.py` stack).
- **Full modifier taxonomy** (temporal/scope/…) — blocked on CD-T19 / entity = span | turn | clause.

## Implementation log

| Date | Note |
|------|------|
| 2026-03-27 | Ethan issued packet; `active.md` HC-GRACE-01 … HC-10 OPEN rows added (P1 hesperia). |
| 2026-03-27 | **Grace HC-GRACE-01 PASS:** 12 HC rows present; CD-T01–T20 **DONE** — no dependency conflict; owners unique (Grace, Ethan, Noah×2, Marcus, Gena×3, Liam, Daniel, Olivia, Ava); HC-03/HC-04 blocked on **HC-ETHAN-01** per packet; no row merge required. |
| 2026-03-27 | **Ethan HC-ETHAN-01 DONE:** Frozen appendix [HESPERIA_CONTROL_MERGED_v1_APPENDIX-2026-03-27.md](HESPERIA_CONTROL_MERGED_v1_APPENDIX-2026-03-27.md) — hook bands, modifier pre-CD MVP + CD precedence, anti-duplication matrix, §11 reorder. |
| 2026-03-27 | **HC-WAVE1 Cursor drain:** HC-01…HC-10 → **DONE**; Hesperia **`25f220e`**; report [reports/HC-WAVE1-CURSOR-DELIVERY-2026-03-27.md](reports/HC-WAVE1-CURSOR-DELIVERY-2026-03-27.md); `active.md` OPEN=0; workflow driver **No OPEN tasks**. |

---

`SIGNED: Architect (Ethan) | Hesperia Control Layer v1 tasking | 2026-03-27 | cursor operational`
