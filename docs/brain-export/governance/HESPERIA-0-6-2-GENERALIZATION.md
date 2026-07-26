# Hesperia 0.6.2 — implementation generalization

**Date:** 2026-06-14  
**Status:** **SEALED** — active.md **OPEN: 0** for hesperia 6.1/6.2 wave

---

## Stack (canonical)

| Layer | Location | Notes |
|-------|----------|-------|
| **Engine** | `/data/hesperia/hesperia` Python shipping API `:18880` | `ENGINE-ANALYZE-CONTRACT.md` |
| **Bridge** | `tersagor` `HesperiaEngineBridge` + `engine_result` sidecar | `docs/ENGINE-RESULT-SIDECAR.md` |
| **Post-retrieve** | `attach_post_retrieve_geometry()` | `interior_pov` + `gtp_coherence` |
| **KSI** | `tersagor_agent/hesperia/ksi/` | Φ_e, residuals, teacher packet, gate, sandbox |
| **Reflection** | `tersagor_agent/hesperia/reflection/` | OpenAI smokes; learning loop on `:18880` |

## Pipeline order

`retrieve` → geometry → KSI (env) → reflection (env) — see `docs/HYBRID-RETRIEVE-PIPELINE.md`

## Test baseline (alunel)

```bash
cd /data/workspaces/tersagor
set -a && source .env && set +a
PYTHONPATH=src .venv/bin/python -m pytest tests/test_ksi_*.py tests/test_hesperia_engine_bridge.py -q
```

**49 KSI + 28 reflection/engine tests PASS** (2026-06-14).

## Env gates

| Var | Default | Purpose |
|-----|---------|---------|
| `HESPERIA_KSI_ENABLED` | 0 | KSI bundle block |
| `TERSAGOR_HESPERIA_REFLECTION_ENABLED` | 0 | Post-analyze reflection |
| `OPENAI_MODEL` | gpt-4o-mini | Reflection client |

KSI vars in `hesperia/runtime/shipping/env_guard.py` ALLOWED list.

## Out of 0.6.2 (0.7.0)

- Live `HESPERIA_KSI_LLM_TEACHER` call
- Sandbox repair apply to production graph
- KSI Inspector UI (KSI-19)

## Governance

- Exit: [HESPERIA-0-6-2-EXIT-CRITERIA.md](HESPERIA-0-6-2-EXIT-CRITERIA.md)
- Register: [HES-62-2026-REGISTER.md](HES-62-2026-REGISTER.md)
- Wave close: [HES-62-WAVE-CLOSE-2026-06-14.md](../operational/assignments/reports/HES-62-WAVE-CLOSE-2026-06-14.md)
- **Agent orientation (Grace):** [GRACE-WRAP-UP-HESPERIA-0-6-1-0-6-2-2026-06-14.md](../operational/assignments/GRACE-WRAP-UP-HESPERIA-0-6-1-0-6-2-2026-06-14.md) — 5 bundles, what/where/why
- **Post-seal inspection (Ethan):** [ETHAN-HESPERIA-FULL-INSPECTION-2026-06-14.md](../operational/assignments/reports/ETHAN-HESPERIA-FULL-INSPECTION-2026-06-14.md) · [HINS-2026-REGISTER.md](HINS-2026-REGISTER.md) — live prod/venv gaps

---

SIGNED: Cursor | 0.6.2 generalization | 2026-06-14
