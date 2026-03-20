<!--
Gena team10 — MCP workflow plan for DLCR-HP v0.6.0.
-->

# Gena team10 — MCP workflow (DLCR-HP v0.6.0)

Status: CLOSED  
Owner: Gena team10  
Scope: `DLCR-001`..`DLCR-020` from `task_gena_v0_6_0.md`  
Execution mode: Cursor + MCP-assisted workflow

---

## 1) MCP workflow contract

This workflow runs the DLCR implementation in tracked stages with explicit artifacts and handoff points.

- **Primary board:** `task_gena_v0_6_0.md`
- **Execution tracker:** this file (update checkboxes + notes)
- **Progress updates:** `docs/governance/working/GENA-OPEN-WORKFLOW-PROCEED.md`
- **System queue reference:** `docs/CURSOR_OPEN_WORKFLOW.md`

Each task must record:
- ticket id
- owner
- status (`todo`/`in_progress`/`done`/`blocked`)
- artifact paths
- validation command(s)
- result note

---

## 2) Team10 run model

Use 4 execution lanes in parallel where dependencies allow:

- **Lane A (Spec/Schema):** `DLCR-001`..`DLCR-008`
- **Lane B (Core Semantics):** `DLCR-009`..`DLCR-014`
- **Lane C (Data/Hex):** `DLCR-015`..`DLCR-018`
- **Lane D (Gates/Release):** `DLCR-019`..`DLCR-020`

Suggested role split:
- **T10-S1:** Specs/index contracts
- **T10-S2:** Schema validators + tests
- **T10-E1:** Normalization/matcher/resolver
- **T10-E2:** Hex projection/dynamics/aggregation
- **T10-QA:** Regression gate + release wiring

---

## 3) MCP stage gates

### Gate G0 — kickoff complete
- `DLCR-001`, `DLCR-002` done.
- Canon index points to DLCR spec pack.

### Gate G1 — schemas green
- `DLCR-003`..`DLCR-008` done.
- Dict A/B + resolver output schemas validate.

### Gate G2 — deterministic semantics green
- `DLCR-009`..`DLCR-014` done.
- Golden tests stable.
- Resolver trace conforms to schema.

### Gate G3 — hex path green
- `DLCR-015`..`DLCR-018` done.
- Concept->hex->family/area path deterministic.

### Gate G4 — release-ready green
- `DLCR-019`, `DLCR-020` done.
- Fallback is explicit and non-default.
- Regression drift gate active in CI.

---

## 4) Task tracker (20)

Use this table as the MCP workflow source of truth.

| Ticket | Status | Owner | Depends | Key artifacts |
|---|---|---|---|---|
| DLCR-001 | done | T10-S1 | - | `specs/canon/lexical_concept/SPEC__DLCR_HP_Master_v0_6_0.md` |
| DLCR-002 | done | T10-S1 | 001 | `specs/CANONICAL_INDEX.md` |
| DLCR-003 | done | T10-S2 | 001 | `schemas/lexical_concept/dict_a.schema.json` |
| DLCR-004 | done | T10-S2 | 003 | `tools/validate_dict_a.py`, `tests/lexical_concept/test_dict_a_schema.py`, `tests/lexical_concept/test_validators_cli.py` |
| DLCR-005 | done | T10-S2 | 001 | `schemas/lexical_concept/dict_b.schema.json` |
| DLCR-006 | done | T10-S2 | 005 | `tools/validate_dict_b_dlcr.py`, `tests/lexical_concept/test_dict_b_schema.py`, `tests/lexical_concept/test_validators_cli.py` |
| DLCR-007 | done | T10-S2 | 001 | `schemas/lexical_concept/resolver_output.schema.json` |
| DLCR-008 | done | T10-S2 | 007 | `schemas/lexical_concept/run_metadata.schema.json` |
| DLCR-009 | done | T10-E1 | 001 | `core/lexical/normalization.py`, `core/lexical/__init__.py` |
| DLCR-010 | done | T10-QA | 009 | `tests/lexical_concept/test_normalization.py`, `assets/data/engine_dynamics_v060/baselines/normalization_golden.json` |
| DLCR-011 | done | T10-E1 | 003,009 | `core/lexical/matcher.py` |
| DLCR-012 | done | T10-QA | 011 | `tests/lexical_concept/test_matcher.py` |
| DLCR-013 | done | T10-E1 | 005,011 | `core/resolver/resolver.py`, `core/resolver/score_rules.py`, `core/resolver/tiebreaks.py` |
| DLCR-014 | done | T10-QA | 007,013 | `tests/lexical_concept/test_resolver.py`, `tests/lexical_concept/test_resolver_output_schema.py` |
| DLCR-015 | done | T10-E2 | 004,006 | `assets/data/engine_dynamics_v060/dict_a/dict_a_seed.jsonl`, `assets/data/engine_dynamics_v060/dict_b/dict_b_seed.jsonl`, `assets/data/engine_dynamics_v060/corpora/gold_spans.jsonl` |
| DLCR-016 | done | T10-E2 | 013,015 | `core/hexmap/anchor_registry.py`, `core/hexmap/projection.py`, `assets/data/engine_dynamics_v060/anchors/concept_hex_anchors.json` |
| DLCR-017 | done | T10-E2 | 016 | `core/hexmap/dynamics.py`, `tests/lexical_concept/test_hex_dynamics.py` |
| DLCR-018 | done | T10-E2 | 017 | `core/hexmap/aggregate.py`, `tests/lexical_concept/test_aggregation.py` |
| DLCR-019 | done | T10-QA | 018 | `runtime/services/dlcr_service.py`, `tests/lexical_concept/test_fallback_mode.py` |
| DLCR-020 | done | T10-QA | 010,014,018,019 | `tools/check_dlcr_regression.py`, `tools/dlcr_trace_report.py`, `.github/workflows/sealed-runtime-gate.yml` |

---

## 5) Standard validation commands per ticket

Run minimally:

- Schema lane:
  - `python3 tools/validate_dict_a.py <path>`
  - `python3 tools/validate_dict_b_dlcr.py <path>`
- Test lane:
  - `pytest tests/lexical_concept -q`
- Smoke:
  - `python3 -m pytest tests/ -q --tb=no -x`

If release gate touched:
- run relevant release audit/check scripts in current release policy.

---

## 6) Required MCP progress update format

For every ticket transition, append one log line in `GENA-OPEN-WORKFLOW-PROCEED.md`:

`[YYYY-MM-DD] team10 DLCR-XYZ status=<todo|in_progress|done|blocked> artifacts=<paths> note=<one line>`

This keeps queue state visible to all Cursor operators.

---

## 7) Exit criteria (team10)

Team10 closes this workflow only when all are true:

- all `DLCR-001`..`DLCR-020` are `done`
- G0..G4 gates are green
- no default raw word->family path remains
- regression drift gate is active in CI

