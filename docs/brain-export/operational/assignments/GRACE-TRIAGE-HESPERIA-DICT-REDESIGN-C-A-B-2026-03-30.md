# Grace triage — Hesperia dictionary role-separation refactor (C -> A -> B)

**Date:** 2026-03-30  
**Requested by:** igareosh (operator)  
**Target repo/workspace:** `/data/hesperia/hesperia`

## Directive

Triage and split team execution for full dictionary redesign:

- Runtime order must become `Dict C -> Dict A -> Links -> Dict B -> Families/Areas/Dynamics`.
- `Dict C` is phrase-first (2-3 tokens), `Dict A` is single-token residual fallback, `Dict B` is concept-only authority, links explicit `source_dict`.
- Deterministic runtime and downstream dynamics stay intact; lexical and activation distributions are expected to drift.

## Preservation guard (operator critical)

Do not lose API-calibrated Dict A effort. Treat frozen normalized/proposal artifacts as immutable inputs; redesign writes to new versioned outputs only.  
Reference freeze report: `operational/assignments/reports/ETHAN-HDR-A7-DICT-A-PRESERVATION-FREEZE-2026-03-30.md`.

## Scope accepted for triage

1. **Data/model refactor**
   - Persist and validate `dict_c.jsonl` (2-3 token phrases only).
   - Purge multi-token rows from `dict_a.jsonl`.
   - Rebuild `dict_b.jsonl` as concept-only rows.
   - Rebuild `links.jsonl` with explicit `A|C -> B` provenance and base weights.

2. **Runtime refactor**
   - Implement C-first matching with 2/3-gram candidates.
   - Longest-match-first overlap resolution in C.
   - Token blocking after accepted C spans.
   - A matching only on residual tokens.
   - Merge A/C evidence before concept aggregation.

3. **Audit and release gates**
   - Add structure gates for A/C/B/link integrity.
   - Add runtime phrase/token coverage metrics and blocking metrics.
   - Introduce report-only -> warn -> fail gate adoption path.

## Team split required (Grace to instantiate OPEN rows)

- **Gena (owner, code):** runtime matcher refactor + evidence merge path + link resolver updates.
- **Noah (owner, validation):** structural validators and purity/leakage metrics.
- **Olivia (owner, gates):** release gate extensions and staged severity mode.
- **Liam (owner, wiring):** runner order guarantees and no-bypass integration checks.
- **Marcus (owner, schema):** A/C/B/link schema contracts and deterministic rejection taxonomy.
- **Ava (owner, guardrails):** read-only mutation guards for lexical assets during runtime.
- **Grace (owner, orchestration):** triage rows, dependency ordering, collision checks, closure packet.
- **Ethan (owner, policy freeze):** freeze authoritative ordering and weight hierarchy contract in model/governance docs.

## Recheck against full redesign spec (2026-03-30)

After strict pass against the full operator spec, triage includes mandatory closure of three explicit items:

1. **Phase-0 baseline freeze task** (pre-redesign metrics/artifacts snapshot).
2. **Data migration artifact task** (`dict_c_draft.jsonl`, clean `dict_a.jsonl`, clean `dict_b.jsonl`, rebuilt `links.jsonl` with `source_dict`).
3. **Runtime evidence contract task** (standard A/C evidence objects with span/match/weight fields and deterministic tests).

These are not optional and must exist as executable rows, not implied subtasks.

## Mandatory acceptance baseline

1. `Dict A` contains only single-token entries.
2. `Dict C` persisted and contains only 2-3 token entries.
3. `Dict B` contains concept-only rows.
4. `Links` encode explicit source dictionary (`A` or `C`) and valid `concept_id`.
5. Runtime executes `C first, A second`, and C-covered spans cannot produce A evidence.
6. Audit artifacts include phrase-hit, token-hit, blocked-token, and concept-source ratios.
7. Release gates validate structure and runtime invariants.

## Workflow to follow

1. Grace creates OPEN rows from this packet with dependencies:
   - schema/contracts -> data extraction/migration -> runtime order refactor -> metrics/gates -> validation/closure.
2. Owners execute per row in `/data/hesperia/hesperia`.
3. Each completed row lands one report under `operational/assignments/reports/`.
4. Final Grace closure row verifies DoD and records drift deltas vs pre-redesign baseline.

---

`SIGNED: Cursor (workflow) | Grace triage packet for Hesperia dict redesign | 2026-03-30 | operational/assignments`
