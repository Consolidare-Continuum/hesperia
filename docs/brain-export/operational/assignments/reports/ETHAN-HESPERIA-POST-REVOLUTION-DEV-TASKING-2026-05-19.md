# Ethan — Hesperia operational: further dev tasking (post repo revolution)

**Date:** 2026-05-19  
**Audience:** Operator (igareosh), Grace, Gena, Felix, Abelard, team  
**Context:** Repo revolution **complete** — dev/prod split, immaculate prod, dev-ready line, prod deploy @ `18178de`, OUT-VIEW question closed, HES-LINE deploy slice done, HES-LINE-03/04 **ABORT**.

**Purpose:** Lock **how we develop Hesperia from here** and **what is already taskable** vs **what needs new Grace triage**. Ethan does **not** add `active.md` rows — Grace triages operator picks.

---

## 1) Revolution complete — operational baseline

| Item | Truth |
|------|--------|
| **Product line** | Tag **`hesperia/dev-ready-line-20260518`** — proceed from here |
| **Prod** | `Atomic-Commits-Team/hesperia` @ **`18178de`** · `prichindel:/data/hesperia/hesperia` · deployed 2026-05-19 |
| **Dev** | `igareosh/hesperia` @ **`777c4ef3`** · `alunel:/data/workspaces/atomic-commit-hesperia` |
| **Brain** | Team/triage/deploy pointers only — no product tree ingest |
| **Policies (frozen)** | [ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md) · [ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md](../../../governance/ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md) |
| **Map** | [cluster/HESPERIA-REPOS-AND-HOSTS.md](../../../cluster/HESPERIA-REPOS-AND-HOSTS.md) |

**Closures (do not re-open without new governance row):**

- HES-SPLIT, HES-READY, HES-LINK, HES-POLICY, HES-DEBLOAT-10 — [GRACE-HESPERIA-DEBLOAT-CLOSURE-2026-05-19.md](GRACE-HESPERIA-DEBLOAT-CLOSURE-2026-05-19.md)
- OUT-VIEW T01–T65 + FULL-01..05 — historical `ed-0.5.6-calibration-baseline`; [GRACE-HESPERIA-OUT-VIEW-QUESTION-CLOSED-2026-05-19.md](GRACE-HESPERIA-OUT-VIEW-QUESTION-CLOSED-2026-05-19.md)
- HES-LINE-00..02 deploy — DONE; HES-LINE-03..04 — **ABORT**

---

## 2) Mandatory dev routing (every slice)

| Activity | Where | Who |
|----------|--------|-----|
| Documentation, specs prose, planning | **`igareosh/hesperia`** + brain `operational/` / `governance/` | Gena, Grace, Cursor |
| Code (py, schemas, corpus data commits) | **Dev first** → promote **`origin`** prod | Gena / Felix |
| Smoke (inspector, hex-matrix, tests) | **alunel dev clone only** | Gena / Felix |
| Deploy | **prichindel prod only** — `bash scripts/hesperia-prod-deploy.sh` | Abelard |
| Post-deploy gate | `verify-hesperia-prod-https.sh` | Abelard |

**Prod commit rule:** no narrative md / specs markdown / team residue on `Atomic-Commits-Team/hesperia` `main`. CI: `verify-hesperia-prod-code-only.sh`.

---

## 3) Out of scope (unchanged)

| Area | Rule |
|------|------|
| **Engine core** | Sealed — no mutation rows without explicit governance |
| **Parameter Golf** | **Suspended** — ARCHIVED in `active.md`; Grace reopens only on operator ask |
| **Engine promotion / apocalyptic archive** | Separate triage; not implied by dev-ready line |
| **Bulk reopen OUT-VIEW-01..09** | Forbidden — delivery closed April 2026 |

---

## 4) Open work already in `active.md` (authorized)

**Single live epic:** **Timeline matrix (TMX)** — triage [GRACE-TRIAGE-TIMELINE-MATRIX-SESSION-TFP-2026-04-08.md](../GRACE-TRIAGE-TIMELINE-MATRIX-SESSION-TFP-2026-04-08.md).

| Phase | IDs | Status |
|-------|-----|--------|
| Spec + scaffold | TMX-00..09, TMX-12..13 | **DONE** |
| Polish + ops + closure | TMX-10..11, TMX-14..24 | **OPEN** (14 rows) |

**Surfaces in scope:** `output_views` — Session Inspector (live), **timeline-matrix** route, hex-matrix static, interpretation blob / supervisor seed (TMX-12..13 done).

**Ethan recommendation — execution order for Grace (when operator says proceed TMX):**

1. **TMX-11** (Ethan) — prompt pack T3 / supervisor slots — unblocks copy and agent consumption  
2. **TMX-10** (Felix) — wire relations + appear_disappear into UI (tooltips / side panel)  
3. **TMX-14** (Olivia) — RU UX copy (depends on 10–11 stable labels)  
4. **TMX-15** (Noah) — gold fixture + snapshot — gate before closure  
5. **TMX-22** (Liam) — inspector ↔ matrix nav + deep links  
6. **TMX-23** (Ava) — design consistency with inspector  
7. **TMX-18** (Sophia) — PII parity review  
8. **TMX-19** (Marcus) + **TMX-20** (Daniel) — runbook + QA checklist  
9. **TMX-21** (Emma) — a11y  
10. **TMX-16..17** (Abelard) — Chroma path + query_knowledge docs (can parallel after 15 if corpus stable)  
11. **TMX-24** (Grace) — closure vs SPEC v1.1  

Set **one IN_PROGRESS** at a time per [AUTOMATION-SCRIPTING-TEAM-POLICY.md](../../../governance/AUTOMATION-SCRIPTING-TEAM-POLICY.md) §8 unless operator approves parallel Felix/Gena on disjoint paths.

---

## 5) Not yet taskable — Grace triage on operator ask

These were **HES-LINE-04** candidates; **ABORT** means no rows until explicit triage:

| Candidate epic | Ethan notes | Suggested owner |
|----------------|-------------|-----------------|
| **RU i18n wire** (inspector + matrix) | Partial stub from OUT-VIEW; full wire = new packet | Gena + Olivia |
| **Session index UX** (`/sessions/`) | Not in TMX; product UX slice | Gena |
| **HPROM / sealed promotion** | Was separate March track; do not auto-reopen | Grace + Ethan assess |
| **Dictionary C→A→B redesign** | Historical triage DONE; follow-on = new row | Gena / Ethan |
| **Founder inspection loop** | [ETHAN-HESPERIA-FOUNDER-SCOPE-INSPECTION-WORKFLOW-2026-04-03.md](ETHAN-HESPERIA-FOUNDER-SCOPE-INSPECTION-WORKFLOW-2026-04-03.md) — orthogonal to TMX | Operator-driven |

---

## 6) Definition of done — per code slice (post-revolution)

Every **code** merge toward prod must satisfy:

1. Commits on **`igareosh/hesperia`** first; smoke on alunel.  
2. Prod promotion: atomic commits on **`Atomic-Commits-Team/hesperia`**; `verify-hesperia-prod-code-only.sh` passes.  
3. Abelard deploy + `verify-hesperia-prod-https.sh`.  
4. Owner **`report_done`** when workflow step completes (brain MCP / API).  
5. No docs-on-prod regression.

**TMX wave closure:** TMX-24 + SPEC DoD checklist + optional Grace closure report (mirror OUT-VIEW-FULL pattern).

---

## 7) Live verification URLs (prod)

| Surface | URL |
|---------|-----|
| Session Inspector (baseline) | https://hesperia.prichindel.com/inspector/1-11-09-2023/ |
| Timeline matrix | https://hesperia.prichindel.com/inspector/1-11-09-2023/timeline-matrix/ |
| Hex matrix | https://hesperia.prichindel.com/hex-matrix/ |

---

## 8) Operator mode — **(C) idle** (2026-05-19)

**Operator choice:** **(C)** — no Hesperia execution until you have bandwidth in **your** brain. Product line stays frozen at **`hesperia/dev-ready-line-20260518`**; prod live @ deploy; **TMX-10..24** remain **OPEN** (not IN_PROGRESS).

**When you return (one line to team):**

- **TMX:** e.g. *“Grace, proceed TMX — start TMX-11”* or *“…start TMX-10”* → Grace sets **IN_PROGRESS** per §4 order.  
- **New epic:** e.g. *“Grace, triage RU i18n”* → §5 packet + new rows.  
- **Still idle:** no action.

**Re-entry card (human brain):**

| Question | Answer already locked |
|----------|------------------------|
| Where is code? | Dev: `alunel` → `igareosh/hesperia` · Prod: `prichindel` → `Atomic-Commits-Team/hesperia` |
| Where are docs? | Dev repo + brain — **not** prod |
| What’s live? | Inspector, timeline-matrix, hex-matrix @ `hesperia.prichindel.com` |
| What’s waiting? | **TMX-10..24** only (14 OPEN rows) |
| What’s forbidden? | Reopen OUT-VIEW bulk, Parameter Golf, engine core without new row |

No automation pickup on Hesperia while idle. Hotfix/deploy still Abelard if prod breaks — separate from feature idle.

---

## 9) Grace / team (when operator un-idles)

| Who | Action |
|-----|--------|
| **Operator** | **(C) now** — see §8 re-entry phrases |
| **Grace** | On unpause (A): set **TMX-11** or **TMX-10** **IN_PROGRESS**; on (B): triage packet → new rows |
| **Gena / Felix** | Code on dev clone; push `dev` then `origin` per slice |
| **Abelard** | Deploy only after prod `origin` updated |

---

## References

| Doc | Path |
|-----|------|
| Debloat closure | [GRACE-HESPERIA-DEBLOAT-CLOSURE-2026-05-19.md](GRACE-HESPERIA-DEBLOAT-CLOSURE-2026-05-19.md) |
| Dev-ready line | [HESPERIA-DEV-READY-LINE-2026-05-18.md](../HESPERIA-DEV-READY-LINE-2026-05-18.md) |
| TMX triage | [GRACE-TRIAGE-TIMELINE-MATRIX-SESSION-TFP-2026-04-08.md](../GRACE-TRIAGE-TIMELINE-MATRIX-SESSION-TFP-2026-04-08.md) |
| Rollback awareness | [GRACE-HESPERIA-ROLLBACK-LINE-AWARENESS-2026-05-18.md](GRACE-HESPERIA-ROLLBACK-LINE-AWARENESS-2026-05-18.md) |

`SIGNED: Ethan (team lead) | Hesperia post-revolution dev tasking | 2026-05-19 | operational`
