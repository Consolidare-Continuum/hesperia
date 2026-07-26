# SCRIPT-RUNBOOK — Hesperia reflection evolution ledger

**Id:** `hesperia-reflection-evolution`  
**Parent:** HSPR-17 (Marcus) · **Audit:** HFIX-28  
**Date:** 2026-06-14

## Preconditions

- Reflection paths: `/data/hesperia/reflection/` (JSONL ledger + epoch snapshots)
- `TERSAGOR_HESPERIA_REFLECTION_ENABLED=1` when using live learning loop

## Read ledger

```bash
tail -20 /data/hesperia/reflection/corpus_evolution.jsonl
ls -lt /data/hesperia/reflection/epochs/ | head -5
```

## Interpret proposals

| Field | Operator action |
|-------|-----------------|
| `rejection_rate` ≥ 0.60 | Review `EvolutionRestructuringProposal` — accept/dismiss |
| `open_restructuring_proposals` | Count in `ReflectionLoopResult` / audit record |
| `learning_outcome.reason` | `record_rejected` = normal; check acceptance thresholds |

## References

- `tersagor_agent/hesperia/reflection/corpus_evolution.py`
- HSPR-15 acceptance thresholds (ratified)

---

SIGNED: Operator (Marcus) | reflection evolution runbook | 2026-06-14 | HFIX-28
