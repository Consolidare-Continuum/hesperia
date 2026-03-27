# Marcus — CD v1 review checklist

- [ ] CD rows never contain natural-language marker strings (only IDs, enums, numbers).
- [ ] `requires` / `excludes` cardinality ≤ 2 per MVP guardrail (validator enforced).
- [ ] Overconstraint: pipeline can return empty `concept_weights` — classify as `CD_EMPTY_ACTIVE_SET` in failure taxonomy when product surfaces it.
- [ ] `HESPERIA_CD_ENABLED` default off — no silent behavior change until profile enables CD.
- [ ] Determinism: double-run hash test in CI.

SIGNED: Review (Marcus) | CD checklist | 2026-03-27
