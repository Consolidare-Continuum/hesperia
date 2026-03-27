# Grace — CD v1 triage (resolved)

- **Ordering**: CD work lands in **Hesperia** repo (`hesperia/engine/concept_dictionary`, `pipeline.py`, assets, tests, `docs/governance/cd_v1/`). Cursor `active.md` tracks completion.
- **Modularization**: CD is **post-T6** domain module–friendly — keep imports under `hesperia.engine.*`; no `core` → CD reverse imports.
- **CI**: Add optional job: `pytest tests/concept_dictionary/` + lexical tests with `HESPERIA_CD_ENABLED` unset (default path).
- **Lexical gate**: script lives in cursor repo `scripts/ci-check-cd-no-lexical.py` (see ETHAN packet) or duplicate under `hesperia/scripts/` when Hesperia CI owns it.

SIGNED: Triage (Grace) | CD-T01 | 2026-03-27
