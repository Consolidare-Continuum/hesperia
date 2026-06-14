# Hesperia 0.6.3 — IRC Teacher application run

**Status:** SEALED 2026-06-14 (Ethan — `hesperia-0.6.3` tag, archive E2E PASS)  
**Scope:** Application-level run only — no graph apply (0.7.0).

## Exit gates (H063-02)

| Gate | Criterion |
|------|-----------|
| G1 | RU TFP statement → `engine_run_envelope.v063` with full operator JSON |
| G2 | IRC `#hesperia-teacher` receives RUN_START → ENGINE_ENVELOPE → TEACHER_* → RUN_DONE |
| G3 | OpenAI Teacher returns `teacher_response.v063` — proposals only, no prose |
| G4 | MySQL `hesperia` ledger stores run + snapshots + pending proposals |
| G5 | Gold tests pass; `justification` rejected by schema validator |

## Artifacts

- Spec: [ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](./ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md)
- Register: [H063-2026-REGISTER.md](./H063-2026-REGISTER.md)
- Schemas: `cluster/tersagor-h063/schemas/`
- Code: deployed to alunel `/data/workspaces/tersagor`
