# Grace triage — Hesperia execution gaps (post–first-triage remediation)

**Date (UTC):** 2026-06-14  
**Triage:** Grace  
**Invoker:** igareosh — issues encountered in workflow execution session; missing from HSPR/HES-61/H62 first triage  
**Register:** [governance/HFIX-2026-REGISTER.md](../../governance/HFIX-2026-REGISTER.md)  
**Rows:** **HFIX-01..28** on [active.md](../../active.md)

---

## 1. Why this wave

First triage (HSPR-00..19, HES-61, H62-001..072) assumed clean execution paths. **Live workflow run** exposed:

| Issue | Encountered | First triage gap |
|-------|-------------|------------------|
| HSPR-08..10 live smokes passed; rows stayed OPEN | MCP `report_done` drift / no formal pytest | No closure + test files |
| HSPR-12 paths created; post-boot hook missing | Abelard partial | No `alunel-post-boot-fixups.sh` row |
| HSPR-16 boundary doc absent | Sophia not tasked after H62-064 | Duplicate boundary scope |
| HES-61-01 labeled Java; engine is Python | Gena subagent discovery | Wrong stack in row text |
| `engine_result` sidecar not parsed | Bridge smoke failed until fix | No parse-contract doc |
| `hesperia-analyze-dev` not in boot docs | Manual systemd install | No runbook / post-boot |
| Full `retrieve()` E2E failed on Chroma | chromadb connection | No CHROMA-1 live E2E row |
| Heartbeat stale after report_done | prichindel `workflow_heartbeat.txt` | No recounter task |
| prichindel `git reset --hard` risk | Sync during drain | No policy row |
| tersagor git commit identity | rebase failures on alunel | No repo-local identity |
| KSI bundle empty stub with engine on | H62-022 stub only | No live Observed_j populate |
| OpenAI model was gpt-5.2 / gpt-4o | User correction | Env + code default row |
| `context_rag` live packet incomplete | HES-61-09 OPEN | No HFIX row |

---

## 2. Wave structure (28 tasks)

| Band | IDs | Owner focus |
|------|-----|-------------|
| **W0 Meta + sync** | HFIX-01..02 | Grace |
| **W1 HSPR closure** | HFIX-03..08 | Felix, Abelard, Sophia |
| **W2 6.1 contract/docs** | HFIX-09..12 | Gena, Felix |
| **W3 Ops + workflow** | HFIX-13..17 | Abelard, Grace |
| **W4 Seal + KSI live** | HFIX-18..26 | Ethan, Grace, Gena, Felix, Noah |
| **W5 Runbooks** | HFIX-27..28 | Liam, Marcus |

---

## 3. Dependency order

1. **HFIX-01** meta → rows live  
2. **HFIX-06, 27** — analyze service durable on boot  
3. **HFIX-03..05** — formal OpenAI pytest → close HSPR-08..10 via **HFIX-02**  
4. **HFIX-09..10** — contract docs before **HFIX-22** live KSI  
5. **HFIX-18..19** — 6.1-final seal after HFIX-03..12 subset  

---

## 4. Maps to parent rows

| HFIX | Closes / unblocks |
|------|-------------------|
| HFIX-02..05 | HSPR-08, 09, 10 |
| HFIX-06, 12 | HSPR-12, HES-61-09 |
| HFIX-07..08 | HSPR-16 |
| HFIX-09..11 | HES-61-01..10 doc accuracy |
| HFIX-18..19 | HES-61-11, 12 |
| HFIX-20..22 | H62-002, 008, 022 |
| HFIX-25..26 | KSI-14, 17 |

---

## 5. Inbox footer

**Triage outcome:** PROJECT-CREATED — 2026-06-14 — [active.md](../../active.md) **HFIX-01..28**; register [HFIX-2026-REGISTER.md](../../governance/HFIX-2026-REGISTER.md).

---

SIGNED: Triage (Grace) | execution-gap remediation wave | 2026-06-14 | 28 tasks from session issues
