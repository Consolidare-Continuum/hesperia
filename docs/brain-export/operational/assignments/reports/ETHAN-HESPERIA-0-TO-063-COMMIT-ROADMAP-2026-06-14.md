# Ethan — Hesperia 0 → 0.6.3 commit roadmap (three repos)

**Date:** 2026-06-14  
**Entity:** Ethan (product governance)  
**Audience:** igareosh, Grace, team archive  
**Method:** Full `git log --reverse` on all three trees; tag mapping; cross-repo reasoning on what shipped where.

---

## Repo map (authoritative)

| Tree | GitHub | Path | Commits | HEAD (2026-06-14) | Role |
|------|--------|------|---------|-------------------|------|
| **Dev** | `igareosh/hesperia` | `alunel:/data/workspaces/atomic-commit-hesperia` | **302** | `9bf0289` · tag **`hesperia-0.6.3`** → `16286fa` | Docs + full product history + archive seal |
| **Prod** | `Atomic-Commits-Team/hesperia` | `prichindel:/data/hesperia/hesperia` | **283** | **`d313bfd`** | Runnable product on prod disk — **code + sealed assets only** |
| **Brain** | `igareosh/cursor` | `/data/altitudine/prichindel.com` | **1598** total · **108** hesperia-scoped path filter | (brain tip) | Governance, deploy, triage, specs — **not product source** |

**Critical divergence:** Prod **stopped at May 21** (`d313bfd`). Dev continued through **0.6.0 release (May 28)** and **0.6.3 archive seal (Jun 14)**. Prod has **no** `0.6.0` or `hesperia-0.6.3` tags fetched. Live prod `/analyze` SHA per HINS doc = **`d313bfd`**.

**0.6.3 live Teacher path** is **not** wholly in these three repos — runtime modules sit on **`igareosh/tersagor`** commit **`0149120`** (tersagor VM). This roadmap notes that at **v0.6.3** only.

---

## How to read this document

- **Version** = release tag when it exists; otherwise **`Ref-X.Y.Z`** reference id for a commit array.
- Each row: **what changed**, **which repo(s)**, **anchor SHAs** (short).
- Dev and prod share origin through **May 18**; they **fork in purpose** after the prod debloat (dev keeps docs, prod keeps code).

---

## Phase 0 — Genesis and brain bootstrap

### Ref-0.0 · 2026-02-09 → 2026-02-18 · Project birth

| Repo | Commits (array) | What happened |
|------|-----------------|---------------|
| **Prod/Dev** | `26f33c9` … `fdba4e7` (≈12 commits) | Empty repo → mirror **`CLIENTS/hesperia`** from brain; add governance/, project/, scripts/, MIT license, Codex assessment. Hesperia becomes a **standalone product repo** split from cursor brain. |
| **Brain** | `15400db`, `f2629e4`, `63a9d25` | Hesperia **project bootstrap** in brain: V1 fixed point, observability/capacity governance, GitHub remote wiring. |

**Reasoning:** Before v0.2, the product lived inside brain (`CLIENTS/hesperia`). This phase **extracts** Hesperia into Atomic-Commits-Team/hesperia while brain retains client governance and infra pointers only.

---

## v0.2 · 2026-02-20 · ΣΓΘ guard layer

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | tag **`hesperia-v0.2-20260220`** → `eea358a` | Guard layer spec (ΣΓΘ), guards module, unit tests, release invoker, v0.2 release notes; merge PR #5. Wired into runtime (`0.2.0.1`). |
| **Dev/Prod** | `e423316` | **First HTTP API**: `/hesperia/analyze`, `/health`, `/privacy`; CORS; deploy + systemd stub. |
| **Brain** | `52b25a9`, `7636ccd` | **hesperia.prichindel.com** nginx, tunnel script, infra runbook — prod surface planning parallel to API land. |

**Reasoning:** v0.2 is the first **named release** with executable guards + minimal analyze API. Brain tracks **how** it reaches the internet; product repo holds **what** runs.

---

## Ref-0.2.1 · 2026-02-22 · Semantic stability + brain sync

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | `faec1f9`, `4890dd5` | v0.2.1 semantic stability doc set; VARIABLES.md glossary; spec renames (18_INDEXING, 19_SEMANTIC_STABILITY). |
| **Dev/Prod** | `ffc5371` | **Full overwrite from cursor brain** — specs, sphere_rag (shadow_layer v1.0), releases v0.2.1 (tag path toward v0.3.0). |
| **Brain** | `916372d`, `8039483` | Switch product remote to **Atomic-Commits-Team/hesperia**; **Hesperia → CLIENTS/ only** — remove duplicate hesperia trees from brain root. |

**Reasoning:** Consolidation wave — one product remote, brain stops being a second source of product bytes.

---

## v0.3.0 – v0.3.3 · 2026-02-22 → 2026-02-23 · Math contract + guards in pipeline

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | tag **`hesperia-v0.3.0`** → `ffc5371` | Core math contract, lexical stack, release gate. |
| **Dev/Prod** | (array) | v0.3.1 guards in pipeline; **v0.3.3** `serve_v033`, single pipeline + shadow flag, legacy Dict A tests. |
| **Brain** | `5474c7b` … `bb76480` | Mirror commits documenting v0.3.0/v0.3.1/v0.3.3 seals in brain README/governance. |

**Reasoning:** First **versioned math contract** with ΣΓΘ in the execution path — foundation for all later TFP/engine work.

---

## v0.4.0 + Ref-0.4.1.x · 2026-02-23 → 2026-02-24 · L1–L9 stack + Dict A/B

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | tag **`hesperia-v0.4.0`** → `dcbb38b` / `d9abcbf` | **First full L1–L9 stack**; RELEASE_NOTES v0.4; layer_runs; MVP assessment. |
| **Dev/Prod** | `edeedd4`, `d08631c` | v0.4.1 runnable: Dict B build, pre-test, sphere_rag; sync specs 22,25–27 from brain. |
| **Dev/Prod** | `93b5292` … `b51ef88` | Dict A deprecation chain v0.4.1.1→1.4; B0/B1 scaffolding; deterministic embedding build; surface artifact gates. |
| **Dev/Prod** | `19d28a4`, `d3fccae` | Dict B B1 freeze; canonical surface repeatability. |
| **Brain** | `354336e` … `6ca43da` | Parallel brain commits: L1–L9 frozen report, RELEASE_NOTES, RUNNABLE declaration, v0.4.0 tag link. |

**Reasoning:** **v0.4.0** = first end-to-end **layer stack** product. Ref-0.4.1.x = dictionary calibration sub-wave still on the v0.4 train.

---

## Ref-0.4-v06-pivot · 2026-02-24 · Archive v04/v05, pivot naming to v0.6 ops layout

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | `b84dc6d` … `89bc563` | Drop v05/dense; archive deprecated scripts; **rename tree to v06** (`analyze.py`, assets/v06); wire `analyze.analyze()`; FREEZE docs. |
| **Brain** | same SHAs mirrored | Brain carries same pivot commits under CLIENTS/hesperia path filter. |

**Reasoning:** Major **line rename** — operational “v0.6” layout appears before the later **sealed runtime v0.6.0** (May 2026). Two different “0.6” meanings: **architecture generation** (Feb) vs **release tag** (May).

---

## Ref-0.5.0-precursor · 2026-02-26 → 2026-03-14 · Team-10 repo + sphere stack + sealed runtime

| Repo | Commit array (high level) | What happened |
|------|---------------------------|---------------|
| **Dev/Prod** | `61ead07` … `d17ba52` | Team-10 adoption; ORDER naming; dossier system; **sphere layer stack**; **v0.5 strip**; RAD legal/fingerprint; **sealed runtime** (release gate, CLI/API shipping); legacy removal after gate PASS; mirror scripts. |
| **Dev/Prod** | `8e137b8` | **Sealed runtime: release gate, CLI/API shipping** — birth of `runtime/shipping/` surface. |
| **Brain** | (sparse) | Brain focuses on cluster/ops; product moves fast in Atomic repo. |

**Reasoning:** Transforms Hesperia from layer POC into **shippable runtime** with sealing discipline — direct ancestor of v0.6.0 prod gate.

---

## v0.5.0 · 2026-03-19 · Engine Dynamics seal

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | tag **`v0.5.0`** → `d4671bd` / `6c2216b` | Tasks 1–11 integration (P_CH, energy, calibration, topology, physics validation, system seal); **full pytest sealed audit**; Engine Dynamics v0.5.0 seal sync. |

**Reasoning:** First **dynamics**-named major seal after sphere/TFP testing stack land (Mar 15–18).

---

## Ref-0.5.1 → v0.5.5 · 2026-03-19 → 2026-03-26 · Release chain + productization

| Version | Anchor | What happened |
|---------|--------|---------------|
| **v0.5.1** | `f53569e` | Enforcement baseline; sealed audit bundle `sealed=true`. |
| **v0.5.2** | `296581f` | Technical terminology propagation seal. |
| **v0.5.3** | `5cf9905` | Modular TFP onboard seal. |
| **v0.5.4** | `ab1905d` | Deterministic modular pipeline (T1–T10 gates). |
| **v0.5.5** | `4479c58` | T11–T20 productization slice; versioned calibration dict loader. |

**Reasoning:** Rapid **patch train** hardening shipping, TFP modularity, and product workflow gates — each tag = audit artifact + CI coupling.

---

## Ref-0.5.6 · 2026-03-27 → 2026-03-30 · Control layer, dict calibration, D3 viewer

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | `25f220e`, `c76aa08` | **HC-WAVE1** control layer MVP; **v0_6_0_clr_v052_1** dict tree seal; B-before-CD governance. |
| **Dev/Prod** | `63cda59` … `ff73864` | **TFP module v1** SSoT; tfp_v1 data tree; migration; CI gates. |
| **Dev/Prod** | `0352a62`, `5b52a09` | STABILIZE v052_4/v052_5 calibration; language layer. |
| **Dev/Prod** | `f9c7024`, `b315268` (brain) | **HESPERIA-D3-VIEWER** v0.5.6 read-only inspection UI; Abelard LAN :8765 viewer. |
| **Brain** | `f197273` … `b37b97b` | Ethan **Control Layer v1** tasking; HC-01..10 workflow; `/data/hesperia` cold root packet. |

**Reasoning:** Bridge from engine seals to **operator-visible inspection** — D3 viewer and control schemas precede Django Session Inspector.

---

## v0.5.8 · 2026-04-14 · Contradiction track (11 tasks)

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | tag **`v0.5.8`** → `5621345` / `42cc7e1` | Tasks 1–11: contradiction pressure through TFP, topology, DLCR, lexical/concept, negation, family structure, calibration diagnostics, **integrity release gating**; seal register + bundle flag. |
| **Brain** | `c07b8d1`, `abc4d23` | Grace release notes payload; TFP bundle folder §0 governance. |

**Reasoning:** Last **major engine feature seal** before UI/output_views dominate — contradiction as first-class calibration signal.

---

## Ref-0.5.9-ui · 2026-04-07 → 2026-05-11 · Session Inspector + Hex Matrix + TMX

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev/Prod** | `a5a17fb` … `dfc54ed` | **OUT-VIEW epic**: Django `output_views`, Session Inspector MVP, Kernberg OpenAI segment schema, PII export, pipeline fixtures (Gena/Felix/Daniel). |
| **Dev/Prod** | `6d9b830` … `9894c8e` | **Hex matrix viewer** (Vite): 12×24 lattice, projections, diamond 288-cell layout. |
| **Dev/Prod** | `85e5d7f` … `0cec2ff` | **TMX-10..24**: RelationsPanel, RU i18n, gold tests, Chroma reference_literature contract, operator runbook. |
| **Brain** | `fec2701` … `551d63f` | Ethan specs: Django output views, Session Inspector panes, **45-task Grace wave**; alunel systemd :8010. |
| **Brain** | `1796ed2`, `d93a390` | nginx `/hex-matrix/` static deploy template. |

**Reasoning:** Hesperia becomes **browser-operable** — inspector + hex matrix are the prod surfaces today at hesperia.prichindel.com.

---

## Ref-20260518 · 2026-05-18 · Prod/dev split (“immaculate prod”)

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Prod** | `ff55ef4` → `18178de` (array ≈20 commits) | **Rollback line** then **debloat**: strip docs/, governance/, specs markdown, release narrative; **prod-code-only CI**; corpus-safe verifier; tag **`hesperia/dev-ready-line-20260518`**. |
| **Dev** | same commits + keeps docs on `igareosh/hesperia` | Dev remote retains full narrative; prod = runnable only. |
| **Prod** | `41e0513`, `d4f4f67` | **v0.6.0 Python compliance** pass; Felix seal note on prod repo. |
| **Brain** | `48494da`, `d8a7285`, `f06736b`, `6b10b3d` | Rollback line pointers; **dev-ready** policy; brain↔dev links only; nginx template sync; **post-0.6.0 topology** governance. |

**Reasoning:** Architectural inflection — **2×2 model** ([cluster/HESPERIA-REPOS-AND-HOSTS.md](../../../cluster/HESPERIA-REPOS-AND-HOSTS.md)): docs on dev, code on prod, brain = pointers.

---

## v0.6.0 · 2026-05-28 · Sealed runtime baseline (dev repo)

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev** | tag **`0.6.0`** → `d06f674` | Sanitized public release artifacts; docker bundle; agentic install contract; **atomic 0.6.0 publish on tag push**; CI sealed-runtime gate on main; `6df2695` TFP layout fix. |
| **Prod** | `d313bfd` (**no 0.6.0 tag on disk**) | Prod disk **did not pull** May 28 release chain — remains at May 21 inspector static fix. Compliance commits `41e0513`/`d4f4f67` are in history but HEAD is behind dev. |
| **Brain** | `a89e158`, `9988c3e` | Ethan **post-0.6.0 topology** + Felix dev authority policy. |

**Reasoning:** **v0.6.0** tag marks **sealed runtime product** for GitHub/archive consumers on **dev**. Prod deployment SHA is **older** — intentional lag until Abelard promote (HINS-12 found API down; fixed separately).

---

## Ref-0.6.1 · 2026-06-11 → 2026-06-14 · 6.1-final engine contract (workflow-heavy)

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Brain** | `7f39836` | Close **25 task rows** + 6.1 pre-release report. |
| **Brain** | `8f88955`, active.md **HES-61-01..12** | Grace triage: **6.1-final** — Python `/analyze` contract, IPoV/GTP live wire, E2E smoke, seal ratification. |
| **Prod** | (no dedicated tag) | Implementation = prod tree `@ d313bfd` + alunel mirror `@ cc94b09` per HINS; **hesperia-analyze-dev** :18880. |
| **Dev** | (no 0.6.1 tag) | No separate git tag; work validated against runtime + workflow rows. |

**Reasoning:** **0.6.1** is primarily a **contract seal** (ENGINE-ANALYZE, hybrid retrieve, context_rag blocks) executed via workflow, not a product-repo tag. Brain is the audit trail.

---

## v0.6.2 · 2026-06-13 → 2026-06-14 · KSI inspection layer (governance seal)

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Brain** | `2b93b4b` | **KSI v0.1 spec** — Kolmogorov Semantic Inspection for 0.6.2. |
| **Brain** | `a67f1f3`, `4d4e3e4`, `4ea9b71` | Grace **81-task wave** H62-001..072; exit criteria; H62-064 data boundary; workflow execution report. |
| **Brain** | [HESPERIA-0-6-2-EXIT-CRITERIA.md](../../../governance/HESPERIA-0-6-2-EXIT-CRITERIA.md) | **KSI-P0..P3 sealed** — Φ_e, residuals, Teacher **packet** serializer, gate/sandbox schemas; **no live LLM** (deferred). |
| **Dev/Prod** | (no `0.6.2` tag) | KSI implementation rows marked DONE in workflow; bytes may span prod runtime + tests — **no separate product tag**. |

**Reasoning:** **0.6.2** = **inspection layer contract** ratified in brain. Differs from 0.6.3 which adds **live Teacher application run**.

---

## Ref-HINS · 2026-06-14 · Prod hygiene remediation (pre-0.6.3)

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Brain** | HINS-00..16 registers + reports | Prod API was down; venvs broken; env_guard KSI vars drifted; **16 remediation tasks DONE** before H063. |
| **Prod** | Abelard deploy | `hesperia-api` :9005, inspector :8010, verify-hesperia-prod-https.sh PASS. |

**Reasoning:** Not a version bump — **trust gate** so 0.6.3 operator run claims match live prod.

---

## v0.6.3 · 2026-06-14 · IRC Teacher archive seal (dev) + tersagor runtime

| Repo | Anchor | What happened |
|------|--------|---------------|
| **Dev** | tag **`hesperia-0.6.3`** → `16286fa`, `9bf0289` | Archive E2E gate PASS; `VERSION.yaml` 0.6.3; `release/v0.6.3/examples/`; `docs/specs/0.6.3-IRC-TEACHER-RUN.md`; `dist/hesperia-0.6.3-archive.zip`; minimal offline dict pin (no prod corpus in zip). |
| **Prod** | (unchanged `d313bfd`) | Prod analyze engine SHA unchanged; live Teacher path wired via **tersagor**, not prod tag bump. |
| **Brain** | H063-00..49, `ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md`, `GRACE-0.6.3-PRE-RELEASE-PACKAGE-NARRATIVE` | Application spec: RU TFP → envelope → IRC trace → OpenAI Teacher (numeric proposals only) → MySQL pending ledger; **no graph write**. |
| **tersagor** | `0149120` (fourth repo — runtime) | Felix modules: `engine_run_envelope`, `teacher_v063`, `irc_teacher_*`, `mysql_ledger`; 465 pytest pass. |

**Reasoning:** **0.6.3** splits across **archive product** (dev tag), **live integration** (tersagor + prichindel MySQL), and **governance** (brain). Prod Atomic repo intentionally **not** bumped to 0.6.3 tag yet.

---

## Tag index (dev repo — canonical release markers)

| Tag | SHA (short) | Date |
|-----|-------------|------|
| `hesperia-v0.2-20260220` | `eea358a` | 2026-02-20 |
| `hesperia-v0.3.0` | `ffc5371` | 2026-02-22 |
| `hesperia-v0.4.0` | `d9abcbf` | 2026-02-24 |
| `v0.5.0` | `6c2216b` | 2026-03-19 |
| `v0.5.8` | `42cc7e1` | 2026-04-14 |
| `hesperia/rollback-line-20260518` | `ff55ef4` | 2026-05-18 |
| `hesperia/dev-ready-line-20260518` | `d9a7cdf` | 2026-05-19 |
| `0.6.0` | `d06f674` | 2026-05-28 |
| **`hesperia-0.6.3`** | **`16286fa`** | **2026-06-14** |

Prod repo tags match through **dev-ready-line**; **missing `0.6.0` and `hesperia-0.6.3`** on prichindel disk at inspection time.

---

## Brain hesperia-scoped commit waves (108 commits, by era)

| Era | Count (approx) | Themes |
|-----|----------------|--------|
| Feb 16–24 | 35 | Bootstrap, v0.3–v0.4 mirrors, Dict A/B, L1–L9, v06 pivot |
| Mar 6–30 | 40 | Control layer, TFP gates, PG-SA, D3 viewer, cold root |
| Apr 4–15 | 15 | Push policy, output_views specs, 45-task wave, TFP runbook, v0.5.8 notes |
| May 5–28 | 10 | Authentik wall, CHROMA-1, rollback/dev-ready, 0.6.0 topology |
| Jun 1–14 | 8 | 0.6.1 close, KSI spec, 0.6.2 triage, H063 post-impl report |

Full filter: `git log -- 'CLIENTS/hesperia/**' 'governance/*HESPERIA*' 'governance/H0*' 'cluster/HESPERIA*' 'operational/**/*HESPERIA*' 'scripts/*hesperia*'`

---

## Road summary (hero arc)

```text
Ref-0.0 genesis (brain CLIENTS → product repo)
  → v0.2 guards + API
  → v0.3 math contract
  → v0.4 L1–L9 + Dict A/B
  → Ref-v06-pivot (Feb architecture generation)
  → Ref-0.5 sealed runtime + TFP module
  → v0.5.0 dynamics seal → v0.5.5 productization
  → v0.5.8 contradiction
  → Ref-0.5.9 Session Inspector + Hex Matrix
  → Ref-20260518 prod/dev split
  → v0.6.0 sealed runtime (dev tag; prod lag)
  → Ref-0.6.1 analyze contract (workflow)
  → v0.6.2 KSI layer (brain seal)
  → Ref-HINS prod trust
  → v0.6.3 IRC Teacher archive (dev tag) + tersagor live
```

---

## Artifact placement cheat sheet (today)

| Artifact type | Canonical repo |
|---------------|----------------|
| Runnable Python/shipping/API | **Prod** `Atomic-Commits-Team/hesperia` (promoted from dev) |
| Specs, release notes, tutorials | **Dev** `igareosh/hesperia` |
| Exit criteria, registers, runbooks, nginx/systemd templates | **Brain** |
| IRC Teacher runtime (0.6.3 live) | **tersagor** (outside this three-repo list) |
| GitHub archive zip 0.6.3 | **Dev** tag `hesperia-0.6.3` → `dist/hesperia-0.6.3-archive.zip` |

---

## NEXT (Ethan)

1. ~~**Promote decision**~~ **DONE 2026-06-14:** prod fast-forwarded to **`122d45b`**; dev+prod unified.
2. ~~**Tag gap**~~ **DONE:** `hesperia-0.6.1`→`f87b2bb`, `hesperia-0.6.2`→`cc94b09`, `0.6.3`/`hesperia-0.6.3`→`122d45b`. Registry: [governance/HESPERIA-VERSION-TAG-REGISTRY.md](../governance/HESPERIA-VERSION-TAG-REGISTRY.md).
3. **Operator:** redeploy prod services from **`122d45b`** if live SHA still **`d313bfd`** (`hesperia-prod-deploy.sh` + verify).
4. **Abelard:** confirm tersagor `0149120` Teacher path against reconciled `/analyze` contract.

### Reconcile (2026-06-14)

Branches diverged after `d06f674`: Atomic `main` carried **6.1** (`f87b2bb`→`cc94b09`); dev carried **0.6.3 archive** (`16286fa`). Tag **`0.6.3`** on Atomic incorrectly pointed at **`cc94b09`**. **Fixed:** merge → **`122d45b`**; tags aligned; both remotes pushed; prod disk pulled.

SIGNED: Team lead (Ethan) | Hesperia 0→0.6.3 commit roadmap | 2026-06-14 | three-repo full-tree analysis
