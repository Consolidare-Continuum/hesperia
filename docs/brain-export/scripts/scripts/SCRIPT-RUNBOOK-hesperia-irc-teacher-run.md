# SCRIPT-RUNBOOK — Hesperia IRC Teacher run (0.6.3)

**Id:** `hesperia-irc-teacher-run`  
**Owner:** Liam  
**Trigger:** Operator sends RU TFP statement via Tersagor bot with `TERSAGOR_HESPERIA_IRC_TEACHER=1`

## Preconditions

- `HESPERIA_KSI_ENABLED=1`
- `HESPERIA_063_ENABLED=1`
- Optional live LLM: `HESPERIA_KSI_LLM_TEACHER=1` + `OPENAI_API_KEY`
- MySQL: `MYSQL_HESPERIA_DSN=mysql://user:pass@127.0.0.1:3306/hesperia`
- IRC audit: `HESPERIA_TEACHER_AUDIT_DIR=~/ergo/logs/hesperia-teacher`

## Steps

1. Enable flags in tersagor env (alunel).
2. Send RU scientific statement to bot; correlation_id logged.
3. Verify IRC trace file: `tail -f ~/ergo/logs/hesperia-teacher/irc-trace.jsonl`
4. Query ledger: `SELECT run_id, status, created_at FROM hesperia.hesperia_teacher_run ORDER BY created_at DESC LIMIT 5;`
5. Confirm proposals `status=pending` (no apply until 0.7.0).

## Rollback

Set `TERSAGOR_HESPERIA_IRC_TEACHER=0` — path disabled; 0.6.2 packet-only unchanged.

SIGNED: Liam | workflow runbook | 2026-06-14 | H063-31
