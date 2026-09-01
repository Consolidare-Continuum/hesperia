# Hesperia commit provenance chain — three repositories

**Generated:** 2026-09-01 (UTC session)  
**Purpose:** Second proof pack — full commit chain by time and message across all Hesperia git homes.  
**Copyright holder (current):** CONSOLIDARE CONTINUUM S.R.L. (IDNO 1026023120076)  
**Document No.:** CC-HES-PROVENANCE-CHAIN-2026-09-01

## Repositories (lane model)

| Order | Remote | Role | Commits in this export | Tip (this export) |
|------:|--------|------|------------------------:|-------------------|
| 1 | `igareosh/hesperia` | Dev — daily push, full history | 549 | `47a03b4e3589` |
| 2 | `Atomic-Commits-Team/hesperia` | **Abandoned 2026-07-26** — prod/consulting line frozen on GitHub | 391 | `4ed89c6d044d` |
| 3 | `Consolidare-Continuum/hesperia` | SRL prod-of-record — **genesis commit 0**, tree-sync from dev | 31 | `560ac2c2f4ca` |

**Note:** Repos 1 and 2 share authorship history until Atomic abandon; repo 3 **does not inherit** git parentage — only tree snapshots + corporate overlay (see `HESPERIA-CORPORATE-INCEPTION.md`).

## Milestones (expanded)

| Date | Repo | SHA | Event |
|------|------|-----|-------|
| 2026-02-09 | `igareosh/hesperia` | `26f33c97` | Genesis — first commit |
| 2026-02-18 | `Atomic-Commits-Team/hesperia` | `(fork)` | Atomic prod remote created (shared root) |
| 2026-03-12 | `igareosh/hesperia` | `c6bcf14` | RAD fingerprint + tag HESPERIA_RAD_FREEZE + OpenTimestamps |
| 2026-07-25 | `Atomic-Commits-Team/hesperia` | `0fcbe899` | Seal system_version 0.7.0 (last product tip) |
| 2026-07-26 | `Atomic-Commits-Team/hesperia` | `4ed89c6` | Copyright transfer ack — Atomic abandoned |
| 2026-07-26 | `Consolidare-Continuum/hesperia` | `cc59e4c` | Commit 0 — SRL corporate inception genesis |
| 2026-07-26 | `Consolidare-Continuum/hesperia` | `d89057b` | Corporate inception seal + overlay |
| 2026-07-26 | `igareosh/hesperia` | `fbbb316` | Dev proprietary copyright overlay |
| 2026-09-01 | `igareosh/hesperia` | `47a03b4` | Tip — syzif corpus relocate |
| 2026-09-01 | `Consolidare-Continuum/hesperia` | `560ac2c` | RAD OpenTimestamps crypto proof filed |

## Related proofs (same flash / dossier)

| Proof | Location |
|-------|----------|
| Dual-MSign IP assignment | `docs/corporate/*.pdf` · MinIO `legal/2026/17_…` `18_…` |
| RAD OpenTimestamps | `docs/corporate/crypto-proof/` · MinIO `37_hesperia_rad_crypto_proof_2026-09-01/` |
| **This chain** | `00-MERGED-chronological-all-repos.tsv` + per-repo TSV |

## Machine-readable exports (companion files)

| File | Contents |
|------|----------|
| `00-MERGED-chronological-all-repos.tsv` | All 971 rows interleaved by author timestamp |
| `01-igareosh-hesperia-commits.tsv` | Dev repo only |
| `02-atomic-commits-team-hesperia-commits.tsv` | Atomic frozen line |
| `03-consolidare-continuum-hesperia-commits.tsv` | SRL repo only |

## Full commit lists (oldest → newest)

### igareosh/hesperia (549 commits)

| # | ISO datetime | SHA | Subject |
|---:|---|---|---|
| 1 | 2026-02-09T17:03:51-05:00 | `26f33c97030d` | Initial commit |
| 2 | 2026-02-09T17:15:58-05:00 | `72bf6ece3195` | first commit |
| 3 | 2026-02-09T17:21:53-05:00 | `a05a08234c08` | 123 |
| 4 | 2026-02-09T17:33:44-05:00 | `7f41a93178a5` | 3 |
| 5 | 2026-02-10T08:02:58-05:00 | `176a556b5967` | 3 |
| 6 | 2026-02-18T08:24:56-05:00 | `9a3b770f46a9` | Replace with CLIENTS/hesperia from cursor repo (canonical source) |
| 7 | 2026-02-18T11:48:02-05:00 | `fdba4e732096` | Add governance (waterline, tasks, schema), project/, scripts/ — full Hesperia team and today's work |
| 8 | 2026-02-18T12:29:21-05:00 | `8162bf7a7b68` | Add MIT license and concepts doc |
| 9 | 2026-02-18T12:34:05-05:00 | `11de49e20416` | Add Codex context assessment (2026-02-18) |
| 10 | 2026-02-19T10:22:27-05:00 | `50b29338c7af` | 3 |
| 11 | 2026-02-19T17:46:30+02:00 | `7481e4356940` | Add files via upload |
| 12 | 2026-02-20T08:41:48+02:00 | `e9224bfe9106` | Add ΣΓΘ guard layer spec and issue-001 closure docs |
| 13 | 2026-02-20T08:42:24+02:00 | `217e8a74b585` | Merge pull request #2 from Atomic-Commits-Team/codex/add-new-guard-layer-features-and-documentation |
| 14 | 2026-02-20T09:05:46+02:00 | `496e67a5ef3e` | Add comprehensive documentation for v0.2 release |
| 15 | 2026-02-20T09:27:49+02:00 | `13dc9358d7ce` | Initialize guards module |
| 16 | 2026-02-20T09:40:00+02:00 | `c0a91c3a9bec` | Create Hesperia v0.2 Release Invoker script |
| 17 | 2026-02-20T09:51:04+02:00 | `18624acc51f4` | Add unit tests for guards: sigma_guard, gamma_guard, and theta_guard |
| 18 | 2026-02-20T09:53:14+02:00 | `047f19d95115` | Release notes for Hesperia v0.2 |
| 19 | 2026-02-20T10:03:27+02:00 | `eea358ac57f6` | Merge pull request #5 from Atomic-Commits-Team/v0.2 |
| 20 | 2026-02-20T10:28:24+02:00 | `d7a05dfc3b1e` | Add Hesperia-mapped software engineering tutorial plan |
| 21 | 2026-02-20T10:29:13+02:00 | `aa5ee68ffdd3` | Merge pull request #6 from Atomic-Commits-Team/codex/create-detailed-.md-file-for-project-plan |
| 22 | 2026-02-20T10:43:07+02:00 | `dcebd8f86f6b` | docs: expand HESPERIA software engineering tutorial plan |
| 23 | 2026-02-20T10:43:27+02:00 | `d2286b2e143d` | Merge pull request #7 from Atomic-Commits-Team/codex/create-software-engineering-plan-document |
| 24 | 2026-02-20T11:37:17+02:00 | `5df386dff278` | Add files via upload |
| 25 | 2026-02-20T11:44:27+02:00 | `d333580f1a68` | Polish Romanian diacritics and clean text artifacts in tutorial |
| 26 | 2026-02-20T11:44:51+02:00 | `4764eecb2636` | Merge pull request #8 from Atomic-Commits-Team/codex/check-romanian-diacritics-and-text-artifacts |
| 27 | 2026-02-20T12:05:37+02:00 | `83a1df20a91f` | Revizuire ediție HESPERIA cu corecturi și detalii noi |
| 28 | 2026-02-20T12:12:43+02:00 | `bbdcd588c5a2` | Refine tutorial TXT layout for improved readability |
| 29 | 2026-02-20T12:12:54+02:00 | `cbc539b6facd` | Merge pull request #9 from Atomic-Commits-Team/codex/adjust-text-file-structure-for-readability |
| 30 | 2026-02-20T19:47:31+02:00 | `cbbadcc5b517` | Wire Sigma/Gamma/Theta guards into runtime flow |
| 31 | 2026-02-20T19:48:13+02:00 | `7c781d50a604` | 0.2.0.1 wired up |
| 32 | 2026-02-20T20:13:31+02:00 | `9e869989ec2b` | Reorganize root Python guards into scripts package |
| 33 | 2026-02-20T20:13:47+02:00 | `c8bc88a45fff` | Merge pull request #11 from Atomic-Commits-Team/codex/organize-python-files-and-rename-elements |
| 34 | 2026-02-20T20:15:46+02:00 | `529bd4315e78` | Add files via upload |
| 35 | 2026-02-20T20:16:54+02:00 | `50fcae20aac2` | Delete v0.2 directory |
| 36 | 2026-02-20T17:23:12-05:00 | `e4233167353c` | API: /hesperia/analyze, /health, /privacy; minimal JSON response; logging; CORS/OPTIONS; deploy + systemd |
| 37 | 2026-02-21T00:28:16+02:00 | `91f3962c7690` | Harden OpenAI Actions API responses and CORS behavior |
| 38 | 2026-02-21T00:29:03+02:00 | `6f1f1d95dcf5` | Merge pull request #12 from Atomic-Commits-Team/codex/debug-openai-gpt-aegle-script |
| 39 | 2026-02-22T14:16:57+02:00 | `51d4181a35bc` | Add files via upload |
| 40 | 2026-02-22T14:28:56+02:00 | `faec1f9927c2` | Add v0.2.1 semantic stability documentation set |
| 41 | 2026-02-22T14:29:07+02:00 | `4890dd50d8a4` | Merge pull request #13 from Atomic-Commits-Team/codex/implement-repository-hygiene-and-versioning-updates |
| 42 | 2026-02-22T14:37:53+02:00 | `178652948ef3` | Update 19_SPEC__Semantic_Stability_Control_v1_0.txt |
| 43 | 2026-02-22T14:45:39+02:00 | `959e4c520e54` | Add files via upload |
| 44 | 2026-02-22T14:47:00+02:00 | `47f59fbc161f` | Rename SPEC_18__Indexing_and_Coordinates_v1_0.txt to 18_SPEC__Indexing_and_Coordinates_v1_0.txt |
| 45 | 2026-02-22T14:59:24+02:00 | `b8d1f80c8951` | Expand VARIABLES.md to include spec and academic variable glossary |
| 46 | 2026-02-22T15:00:26+02:00 | `c2f993ca74ce` | Merge pull request #14 from Atomic-Commits-Team/codex/create-variables.md |
| 47 | 2026-02-22T08:23:43-05:00 | `351178c608ba` | consolidation (Gena): canonical refs, workspace, DOC_INDEX, fix double extension |
| 48 | 2026-02-22T08:47:22-05:00 | `ffc5371c27a5` | Full overwrite from cursor brain: present state (no books). Specs, sphere_rag (shadow_layer v1.0), docs, releases v0.2.1 |
| 49 | 2026-02-23T09:00:12+02:00 | `b6a8b5f222d7` | Add files via upload |
| 50 | 2026-02-23T09:22:29+02:00 | `87c435815e01` | Add files via upload |
| 51 | 2026-02-23T09:32:35+02:00 | `6879a68f279e` | Add files via upload |
| 52 | 2026-02-23T04:44:25-05:00 | `edeedd42c993` | v0.4.1 runnable: Dict B build, pre-test, full sphere_rag |
| 53 | 2026-02-23T04:47:13-05:00 | `d08631cf1588` | Sync from cursor: specs 22,25-27, README, release notes, docs, guard_config, hesperia_lex (scripts+curated), assets A/B |
| 54 | 2026-02-23T12:03:57+02:00 | `c9fda7450592` | Add v0.4.1 structural audit report against v0.3.3 baseline |
| 55 | 2026-02-23T12:04:24+02:00 | `60ee226eea86` | Merge pull request #15 from Atomic-Commits-Team/codex/perform-structural-audit-of-hesperia |
| 56 | 2026-02-23T15:50:53-05:00 | `93b5292f6cd2` | Dict A v0.4.1 deprecated (v0.4.1.1 default); v0.4.1.2 canonical families.yaml + builder + validator |
| 57 | 2026-02-23T23:01:57+02:00 | `a8e444d6dd61` | Add v0.4.1.3 semantic family canonicalization pipeline |
| 58 | 2026-02-23T23:02:14+02:00 | `20bf4374efd3` | Merge pull request #16 from Atomic-Commits-Team/codex/rewrite-families.yaml-for-semantic-canonicalization |
| 59 | 2026-02-24T00:33:42+02:00 | `dd0d107febb1` | v0.4.1.4 Dict B: formalize B0 fallback and scaffold hard-gated B1 |
| 60 | 2026-02-24T00:34:00+02:00 | `37e0f6f1185c` | Merge pull request #17 from Atomic-Commits-Team/codex/finalize-b0-token-fallback-and-add-b1-scaffolding |
| 61 | 2026-02-24T00:59:02+02:00 | `5fc762e6cfae` | Add deterministic v040 embedding build env and runner |
| 62 | 2026-02-24T00:59:19+02:00 | `9a672785f67d` | Merge pull request #18 from Atomic-Commits-Team/codex/unblock-v0.4.0-embedding-build |
| 63 | 2026-02-24T01:14:16+02:00 | `d68bab579013` | Harden v0.4.0 build outputs with deterministic hashing and provenance |
| 64 | 2026-02-24T01:14:29+02:00 | `fcf778bf57ef` | Merge pull request #19 from Atomic-Commits-Team/codex/implement-deterministic-json-output-and-checksum-gate |
| 65 | 2026-02-24T01:22:12+02:00 | `4901aaded49a` | Gate v0.4.0 surface build with model pinning and canonical checks |
| 66 | 2026-02-24T01:22:33+02:00 | `b51ef88849d8` | Merge pull request #20 from Atomic-Commits-Team/codex/finalize-surface-artifact-for-dict-b |
| 67 | 2026-02-23T18:48:08-05:00 | `d3fccae2b5fd` | Canonical surface: fix freeze file format; repeatability venv-agnostic |
| 68 | 2026-02-23T19:12:00-05:00 | `19d28a40a2ef` | Hesperia: Dict B B1 freeze, canonical procedures, topology truth, coverage |
| 69 | 2026-02-24T02:26:21+02:00 | `70dc4dd1db3b` | Add HESPERIA AI status and milestones technical report |
| 70 | 2026-02-24T02:26:36+02:00 | `065c2eb9349d` | Merge pull request #21 from Atomic-Commits-Team/codex/create-technical-report-on-hesperia-project |
| 71 | 2026-02-24T06:56:42-05:00 | `dcbb38b1dcc7` | v0.4.0: first full L1–L9 stack, release notes, layer_runs, RELEASE_NOTES__v0_4 |
| 72 | 2026-02-24T14:18:46+02:00 | `052e194cbcc6` | Add v0.4 MVP assessment narrative report |
| 73 | 2026-02-24T14:18:57+02:00 | `01f8c4898cee` | Merge pull request #22 from Atomic-Commits-Team/codex/create-narrative-report-on-v0.4-hesperia-mvp-status |
| 74 | 2026-02-19T10:48:24-05:00 | `411309514bfa` | 3 |
| 75 | 2026-02-26T17:17:55-05:00 | `61ead07f090a` | Team 10 adoption: single repo, deliverables to Atomic-Commits-Team/hesperia. OPERATIONAL.md, TEAM10-PROJECT.md, .gitigno |
| 76 | 2026-02-26T17:20:02-05:00 | `9d293787aea4` | Operational report: push succeeded, large-file note, single variant. |
| 77 | 2026-02-26T17:25:40-05:00 | `1fe3802875ca` | End of day: nuke summary, sync note, single variant. |
| 78 | 2026-02-27T03:15:12-05:00 | `d79d79713984` | L1 Normative Structure Profile Extension (34_SPEC N1) + Taxonomy v1.0 |
| 79 | 2026-02-27T06:28:03-05:00 | `d52498e8e020` | R1-R4 pipeline, e2e sentence script, dict_b/surface wiring, docs and governance |
| 80 | 2026-02-27T08:18:24-05:00 | `e6a871fe89f9` | R1-R4/E2E: token-offset segmentation, unit fixes, spec notes |
| 81 | 2026-02-28T17:44:56-05:00 | `6d5cb52da958` | ORDER: repo-wide naming (4 words + version), artifacts in subfolders, specs at root |
| 82 | 2026-02-28T17:48:23-05:00 | `7765737d5745` | ORDER: document mrt remote (hesperia_mrt fork repo) |
| 83 | 2026-03-07T19:32:44+02:00 | `a36433493367` | docs: add naming consistency audit and expand variables index |
| 84 | 2026-03-07T19:33:02+02:00 | `8c720dfebae0` | Merge pull request #23 from Atomic-Commits-Team/codex/check-repository-terminology-consistency |
| 85 | 2026-03-11T01:27:07-07:00 | `934a3f984446` | Consolidate v0.4 baseline boot path and fix attribution tests |
| 86 | 2026-03-11T01:29:18-07:00 | `1ddbb4b17b1f` | Merge pull request #24 from Atomic-Commits-Team/codex/consolidate-poc-repo-into-canonical-baseline |
| 87 | 2026-03-11T06:51:49-04:00 | `05fc6faf9739` | 3 |
| 88 | 2026-03-11T11:15:39-04:00 | `6b385b2f66a8` | 3 |
| 89 | 2026-03-11T15:29:08-04:00 | `0897549ff767` | Dossier system, batch runner, content-addressed artifacts, and pipeline refactor |
| 90 | 2026-03-12T06:02:37-04:00 | `dcb4695a79bb` | Add sphere layer stack: topology, dynamism, logic, metrics, USF, pipeline, guards |
| 91 | 2026-03-12T07:09:36-04:00 | `802efcf98099` | Add testing framework, interface layer, structural geometry, diagnostics |
| 92 | 2026-03-12T07:54:31-04:00 | `c6bcb11b4b97` | v0.5: strip versioning, structural attribution, e2e all, deprecations, README rewrite |
| 93 | 2026-03-12T13:16:56-04:00 | `63febce162eb` | Layer-10 interpretation, USF consolidation, Prolog L9b, multi-step propagation, fingerprint drift |
| 94 | 2026-03-12T14:20:32-04:00 | `c6bcf14c222b` | RAD: legal notice repo-wide, architecture fingerprint, boundaries, layer deps, .gitignore pytest cache |
| 95 | 2026-03-12T14:20:55-04:00 | `c1361131db36` | docs: add Git tag and SHA to ARCHITECTURE_FINGERPRINT proof |
| 96 | 2026-03-12T14:24:09-04:00 | `e23749e380ed` | docs: evidence chain in ARCHITECTURE_FINGERPRINT (document→commit→tag), optional OpenTimestamps note |
| 97 | 2026-03-12T14:25:50-04:00 | `b1e0feac4e1f` | docs: OpenTimestamps proof for HESPERIA_SYSTEM_SPEC_v1.md (.ots), update fingerprint |
| 98 | 2026-03-12T14:34:26-04:00 | `d3aab9a4d9d7` | docs: README capabilities and use sections, push sync |
| 99 | 2026-03-13T14:31:30-04:00 | `4d0314e4a0a6` | KME domain pipeline: Tasks 1-6 + E2E integration |
| 100 | 2026-03-14T14:23:12-04:00 | `5eef4a61bb1b` | quarantine: move docs/architecture and docs/boot to legacy/docs_archive |
| 101 | 2026-03-14T14:30:53-04:00 | `8e137b81a0b9` | Sealed runtime: release gate, CLI/API shipping, backup, governance and cleanup |
| 102 | 2026-03-14T14:41:51-04:00 | `5f64eef60f7b` | Sealing scan: restrict to public surface only; document legacy observation window |
| 103 | 2026-03-14T15:15:04-04:00 | `a1c82762c37c` | Remove legacy/ after sealed runtime gate PASS; add manifest-only build target |
| 104 | 2026-03-14T15:25:20-04:00 | `9a3a24c0787f` | Add push_mirrors.sh and mirror setup docs; document lifecycle and protection layers |
| 105 | 2026-03-14T15:43:14-04:00 | `d17ba52f55df` | Cleanup: archive specs history, remove duplicate A_CORE_STAR_MAP, add CLEANUP_PLAN |
| 106 | 2026-03-14T15:47:13-04:00 | `e1fd3eae211b` | Clean repo root: move guard and layer config out of root |
| 107 | 2026-03-14T15:47:41-04:00 | `22302ccdea8f` | Docs: note Phase 2b root cleanup in CLEANUP_PLAN |
| 108 | 2026-03-14T16:04:35-04:00 | `8e7dfe6004c0` | fix: e2e sealing + move analysis_service to runtime for layer boundary |
| 109 | 2026-03-14T16:05:21-04:00 | `9e2e0ca67517` | chore: add .dockerignore and release artifacts (checksums, manifest, schema_sha256) |
| 110 | 2026-03-14T16:12:33-04:00 | `80453a32cf0c` | docs: from-scratch memo in README + RUN/BUILD/DEPLOY from scratch guides |
| 111 | 2026-03-14T16:25:50-04:00 | `7722d013b4f0` | docs: 10+2 topology decision — 10 operational, 2 reserved service areas |
| 112 | 2026-03-15T11:34:51-04:00 | `e5eed2b672c7` | Remark: testing_tfp phase |
| 113 | 2026-03-15T17:08:07-04:00 | `4bb8a5c7ea6e` | TFP testing stack: speaker-aware, transference, temporal, operational analytics, normalization, negation, n-grams, calib |
| 114 | 2026-03-18T05:48:01-04:00 | `04936737c919` | TRIZ engine, KME integration, e2e consolidation (9 stages), product/eval/deploy |
| 115 | 2026-03-18T06:58:15-04:00 | `2435be03b6fc` | docs: Hesperia knowledge base — repo map, dependency graph, variable catalog, product lines/stack |
| 116 | 2026-03-18T12:24:39-04:00 | `6e3f4e154c4b` | E2E: commit canonical artifacts + calibration batch; track e2e outputs in repo |
| 117 | 2026-03-18T12:26:27-04:00 | `0e740022bb12` | Add field_dynamics engine (phase1-4, state, triz_signal, xi_proxy, e2e_bridge) + tests |
| 118 | 2026-03-18T12:27:27-04:00 | `0d20594ac0d3` | Docs sync: system awareness, dynamics/calibration specs, governance, triage, research; AGENTS/README; calibration assets |
| 119 | 2026-03-18T12:30:18-04:00 | `586acec2a5b0` | docs: EoD repo-wide snapshot 2026-03-18 |
| 120 | 2026-03-18T13:23:26-04:00 | `af41d9e88234` | feat: semantic field stack — equations, HCI calibration, ontology matrices, E2E |
| 121 | 2026-03-19T04:33:06-04:00 | `c6d59b50ca15` | release: Hesperia Engine Dynamics v0.5.0 seal sync |
| 122 | 2026-03-19T04:42:09-04:00 | `0ba8b734af9a` | fix(release): snapshot git dirty before writing release/v0.5.0 artifacts |
| 123 | 2026-03-19T04:47:11-04:00 | `d4671bd4bdad` | release(v0.5.0): sealed audit artifacts (full pytest, 2026-03-19T12:00:00Z) |
| 124 | 2026-03-19T04:54:20-04:00 | `b999798aaa34` | fix(ci): sealing scan — word-boundary 3D, skip v0.5.0 audit + triz_demo |
| 125 | 2026-03-19T09:39:11-04:00 | `531d6ff29eaa` | feat(engine): Tasks 1–11 integration — P_CH, energy, calibration, topology, physics validation, system seal, full E2E st |
| 126 | 2026-03-19T11:25:32-04:00 | `342f3f00467e` | release: Hesperia Engine Dynamics v0.5.1 (enforcement baseline) |
| 127 | 2026-03-19T11:31:25-04:00 | `f53569eef780` | release: v0.5.1 sealed audit bundle (final_gate sealed=true) |
| 128 | 2026-03-19T11:43:06-04:00 | `f4e33d79c42d` | fix(ci): install pytest for sealed-runtime-gate integrity step |
| 129 | 2026-03-19T13:17:05-04:00 | `4759cf7809d3` | hardening(release): seal-coupled v0.5.1 version lock + portable bundle |
| 130 | 2026-03-19T13:27:45-04:00 | `cfc30a9b0b0e` | hardening(release): build_release_bundle matches temp-copy spec |
| 131 | 2026-03-19T13:37:21-04:00 | `a1c1355baad9` | release: add bundle integrity + determinism guard |
| 132 | 2026-03-20T11:43:39-04:00 | `151dfa38647f` | feat(tfp): RU v060 corpus, DLCR stack, dynamics wiring; drop session transcripts |
| 133 | 2026-03-21T12:20:24-04:00 | `51db2352bbbc` | sync: TFP calibration pack + OpenAI tooling |
| 134 | 2026-03-22T06:19:16-04:00 | `ea591d7694a1` | OpenAI calibration: stderr progress, smoke check, batch runners |
| 135 | 2026-03-22T06:20:51-04:00 | `364101e220d2` | chore: ignore and untrack research/_noone_local (local-only corpus) |
| 136 | 2026-03-22T06:22:30-04:00 | `f0eb1f9c6476` | TFP calibration: engine, pipeline, schemas, tools, tests, small JSON data |
| 137 | 2026-03-22T06:25:43-04:00 | `94277a7db3d0` | docs: refresh IMPORT_GRAPH v0.5.0 (runtime + engine) |
| 138 | 2026-03-22T06:30:25-04:00 | `7eb524a2beb0` | chore: bump DEAD_WEIGHT RECORDED_COUNT to 67 (import BFS drift) |
| 139 | 2026-03-26T02:23:57-04:00 | `6e60b6b61110` | Ethan ML-07: neutral product docstring for analyze_session_speaker_aware (mainline, no TFP). |
| 140 | 2026-03-26T02:25:33-04:00 | `e6b9a228d6ce` | Ethan task H (H_total): mainline-pin h_total_concepts.json; add semantic_dynamics_operator_spec.md. |
| 141 | 2026-03-26T04:50:02-04:00 | `e1217ab65d00` | release: finalize v0.5.2 technical terminology propagation |
| 142 | 2026-03-26T04:50:55-04:00 | `296581f37553` | release: seal v0.5.2 technical audit bundle |
| 143 | 2026-03-26T07:40:02-04:00 | `5cf99055251c` | release: seal v0.5.3 modular tfp onboard |
| 144 | 2026-03-26T09:06:20-04:00 | `23f589aef2ce` | feat: complete modular kernel workflow gates T1-T10 |
| 145 | 2026-03-26T11:26:55-04:00 | `ab1905ddc1ac` | release: seal v0.5.4 deterministic modular pipeline system |
| 146 | 2026-03-26T13:04:44-04:00 | `9f5547882702` | feat(product): deliver T11-T20 productization workflow slice |
| 147 | 2026-03-26T14:16:04-04:00 | `ac872661facc` | feat(engine): wire versioned calibration dict loader |
| 148 | 2026-03-26T14:19:27-04:00 | `4479c5897638` | release: promote system to v0.5.5 |
| 149 | 2026-03-27T13:48:23-04:00 | `f52fd57ec687` | feat(cd): Concept Dictionary v1 Phase 1 — executor, asset, pipeline hook (opt-in) |
| 150 | 2026-03-27T16:47:44-04:00 | `25f220e53a43` | HC-WAVE1: control layer MVP — schemas, docs, hesperia_control module, tests (HC-01..HC-10). |
| 151 | 2026-03-27T17:03:29-04:00 | `4ae0cd4c73b6` | Add TFP module data mirror (README, sync script, docs) |
| 152 | 2026-03-27T17:10:55-04:00 | `a142a8827c55` | Dict calibration: default 4 workers, offline bundle, skip API key in mock |
| 153 | 2026-03-27T17:12:20-04:00 | `0082666f0db6` | docs(dict_calibration): Dict A API phase closed; do not re-run LLM stages unless intentional |
| 154 | 2026-03-27T17:16:17-04:00 | `1f0b677b3d02` | Add B+CD verification wave after green A (script + doc) |
| 155 | 2026-03-27T17:19:21-04:00 | `dbafd41a8844` | governance(Ethan): lock B-before-CD after green A (working + MODEL_CARD) |
| 156 | 2026-03-27T17:20:55-04:00 | `6ab6a05d1460` | docs(Ethan): 10 tasks to finish dicts and calibrate/check |
| 157 | 2026-03-27T17:25:16-04:00 | `294d0ee0d8ed` | docs(Ethan): dict/calibration framework rev.2 (H/S/V/Y + control laws) |
| 158 | 2026-03-27T17:30:30-04:00 | `c76aa0822fa3` | governance(Ethan): seal v0_6_0_clr_v052_1 dict A/norm/propose/anchor tree |
| 159 | 2026-03-27T17:39:15-04:00 | `bd85cbee489f` | dict/CD: Phase 2 co_occurs soft math, release gates script |
| 160 | 2026-03-27T17:50:51-04:00 | `2e1043d38f76` | docs: point E2E and entry commands at runtime.pipeline (not execution_flow) |
| 161 | 2026-03-27T17:57:12-04:00 | `cc9c49ae064b` | GAP-WIRE-01: expand env_guard allowlist; RUNTIME_ENV_VARS tiers; regen script |
| 162 | 2026-03-27T17:58:47-04:00 | `6c2893f0ab5c` | GAP-WIRE-02: document shipping vs dev API; T17 /product/*; OpenAPI bearer for /product/ |
| 163 | 2026-03-27T17:59:35-04:00 | `043b3fe67086` | GAP-WIRE-03: README quick start hesperia.run + dict gate runbooks |
| 164 | 2026-03-27T18:00:40-04:00 | `b668eebc162e` | GAP-WIRE-04: validate_version_consistency in sealed-runtime-gate; policy doc |
| 165 | 2026-03-27T18:01:08-04:00 | `4b8691558953` | GAP-WIRE-05: document CI pytest subset vs full tests/ in SHIPPING_PATH_POLICY |
| 166 | 2026-03-27T18:02:23-04:00 | `dcc16366b533` | GAP-WIRE-06/07: metric registry partial-coverage waiver; tools shell index |
| 167 | 2026-03-28T11:49:08-04:00 | `033d57d4c391` | calibration: v0_6_0_clr_v052_2 B-gap closure (DICT-CAL-02), TFP cluster hex anchors |
| 168 | 2026-03-28T12:11:51-04:00 | `94af72d9f437` | TFP-GATE-A0/A1: determinism env, VERSION calibration pin, wave artifact checks |
| 169 | 2026-03-28T12:14:52-04:00 | `4f7ec60fbab3` | TFP-GATE: phase C smoke script, mirror checksum verify, governance docs (B1/B2/A2A3/METRICS/INV/UNMAPPED/CD-DELTA), test |
| 170 | 2026-03-28T12:26:32-04:00 | `a2078889a1fd` | TFP-ENF-01..05: behavioral pytest (dominance, co_occurs, saturation, modifiers), CD delta bounds, unmapped fixture gate, |
| 171 | 2026-03-28T12:36:31-04:00 | `8e2e57522cc0` | TFP-REL-01..05: lexical unmapped token rate API, real corpus test, pipeline CD area delta, per_text_non_empty_ratio, lat |
| 172 | 2026-03-28T12:47:58-04:00 | `e25be822060a` | TFP-TIGHT-01..05: unmapped cap 0.65 + real dict corpus, relative CD delta bound, semantic stability test, min per-text a |
| 173 | 2026-03-28T13:03:21-04:00 | `63cda5905056` | TFP module v1: governance, seal hook, gold tests, CI path gate |
| 174 | 2026-03-28T13:12:28-04:00 | `aee3cbc069e0` | TFP-DATA-T01: Ethan charter — module tfp_v1 SSoT, research evicted for dict ops |
| 175 | 2026-03-28T13:14:10-04:00 | `dc0effea3c9d` | TFP-DATA-T02: research/_noone_local inventory JSON + index + regen tool |
| 176 | 2026-03-28T13:14:43-04:00 | `4fe89c7be464` | TFP-DATA-T03: TFP_V1_LAYOUT.md + data README pointer |
| 177 | 2026-03-28T13:27:19-04:00 | `ff73864fe591` | TFP-DATA-T04–T20: tfp_v1 module data tree, migration, sync, CI gates |
| 178 | 2026-03-28T13:28:13-04:00 | `1730dc56877f` | TFP-DATA-T20: mark active.md closure item done in checklist |
| 179 | 2026-03-28T13:33:12-04:00 | `30daa9b78560` | TFP-DATA-T07: mirror dict_calibration provenance into tfp_v1 runs + manifest |
| 180 | 2026-03-28T13:44:50-04:00 | `35a56db45c50` | Move clinical session corpus to tfp_v1/corpus/sessions (migrate + ingest paths) |
| 181 | 2026-03-28T14:07:44-04:00 | `990f7992e167` | E2E TFP smoke uses primary text; hesperia.tfp shim; NLP session_topology wrappers |
| 182 | 2026-03-28T14:27:59-04:00 | `3c34695f7d10` | R1-R4: tokenize_with_spans fixes RU clinical R1 partition (punct-stripped tokens) |
| 183 | 2026-03-28T14:36:45-04:00 | `01042303d847` | Add apocalyptic archive triage doc + workflows mirror script |
| 184 | 2026-03-28T14:39:41-04:00 | `36dcaa572853` | docs(governance): Ethan flash recovery bundle + workflows must-carry (no server) |
| 185 | 2026-03-28T14:47:08-04:00 | `5e4d02f243e1` | tools: mirror cursor brain into /data/hesperia + data root README template |
| 186 | 2026-03-29T15:41:11-04:00 | `5eb1d339c52d` | docs(reference): add Upcelerator2026 README index (Dreamups Phase 1 N.2) |
| 187 | 2026-03-29T15:41:11-04:00 | `7c5aa5fb4366` | docs(reference): Upcelerator2026 Assignment-1 motivation, vision, mission |
| 188 | 2026-03-29T15:41:12-04:00 | `50fb60d679f3` | docs(reference): Upcelerator2026 market definition, sizing, PESTLE (2B) |
| 189 | 2026-03-29T15:41:12-04:00 | `d65a720249e1` | docs(reference): Upcelerator2026 competitor analysis (2C) |
| 190 | 2026-03-29T15:41:12-04:00 | `333b00e70dd8` | docs(reference): Upcelerator2026 BMC and pitch deck (2A, 2D) |
| 191 | 2026-03-29T15:41:12-04:00 | `63983e1095fe` | docs(reference): Upcelerator2026 working assets (generators, templates, notes) |
| 192 | 2026-03-29T15:41:27-04:00 | `bec423580f68` | chore(governance): add cursor session mode artifact |
| 193 | 2026-03-29T15:41:27-04:00 | `22a20d2d19f4` | test: add calibration dict loader and TFP module main run tests |
| 194 | 2026-03-29T15:41:27-04:00 | `dcc4fd9f7828` | docs(tools): document Upcelerator2026 path in data root template |
| 195 | 2026-03-30T06:16:58-04:00 | `d26987cea6c8` | HPROM-R4: hprom_report_metrics and v6 REPORT eval (force-add ignored reports path). |
| 196 | 2026-03-30T06:31:02-04:00 | `0352a6282eb5` | STABILIZE v052_4: sealed calibration dir, stabilize script, hprom_04 tri-version REPORT. |
| 197 | 2026-03-30T06:40:44-04:00 | `93855686f012` | tools: extended RU natural corpus + REPORT runner for v052_4 validation (no dict edits) |
| 198 | 2026-03-30T06:42:47-04:00 | `2a23ff83e2cf` | artifacts: dict field value and status counts snapshot + summarize tool |
| 199 | 2026-03-30T06:45:19-04:00 | `4d59aa33bbc1` | tools: print dict_states snapshot JSON to stdout; --quiet for file-only |
| 200 | 2026-03-30T06:49:30-04:00 | `3b67968a7e7a` | lexical: text language heuristic + dict_c language layer analysis (Grace C-layer) |
| 201 | 2026-03-30T06:53:33-04:00 | `5b52a09eee4b` | calibration: v052_5 dict_c language retag (ru/en/mixed) + tools and REPORT artifacts |
| 202 | 2026-03-30T07:04:34-04:00 | `e54bb4213197` | fixtures: extended RU natural corpus v2 (Wikipedia batch) + fetch tool + language layer artifact |
| 203 | 2026-03-30T07:33:16-04:00 | `47a6babd9e50` | fixtures: session 11.09.2023 plain text for DLCR REPORT baseline |
| 204 | 2026-04-14T08:19:47-04:00 | `e29cb70d572c` | v0.5.8 task1: couple contradiction pressure into tfp area inhibition |
| 205 | 2026-04-14T08:22:51-04:00 | `20f42a5b0235` | fix(nlp): speaker label regex flags for Python 3.12 (import-safe hesperia.nlp) |
| 206 | 2026-04-14T08:27:49-04:00 | `32038085f30f` | v0.5.8 task2: wire contradictions from pipeline into tfp activation |
| 207 | 2026-04-14T08:32:53-04:00 | `5ddf364b168a` | v0.5.8 task3: couple contradictions into topology segment dynamics |
| 208 | 2026-04-14T08:38:59-04:00 | `6448bc70a1a6` | v0.5.8 task4: propagate contradiction package across dlcr multiscale and product |
| 209 | 2026-04-14T08:44:34-04:00 | `1327948fe29d` | v0.5.8 task5: couple contradiction with lexical and concept uncertainty |
| 210 | 2026-04-14T08:52:22-04:00 | `5465444600e6` | v0.5.8 task6: couple contradiction with negation and inhibition logic |
| 211 | 2026-04-14T09:00:05-04:00 | `084d08046fa2` | v0.5.8 task7: couple contradiction with family-level structure |
| 212 | 2026-04-14T09:08:22-04:00 | `1dedcc7e5e6b` | v0.5.8 task8: feed contradiction patterns into lexical and concept calibration diagnostics |
| 213 | 2026-04-14T09:13:20-04:00 | `888bbcc8ecd1` | v0.5.8 task9: add contradiction integrity release gating and promotion verdicts |
| 214 | 2026-04-14T09:22:43-04:00 | `904cf944d0cb` | v0.5.8 task10: formalize contradiction spec and artifact contract |
| 215 | 2026-04-14T09:55:15-04:00 | `b87ca97680de` | v0.5.8 task11: centralize contradiction calibration surface and profile |
| 216 | 2026-04-14T10:08:28-04:00 | `13e5ef8534b9` | docs+tools: v0.5.8 seal register (tasks 1-11), bundle --contradiction-calibration-json |
| 217 | 2026-04-14T10:08:36-04:00 | `562134599bad` | Merge branch 'ed-0.5.8-task11-contradiction-calibration-surface': Hesperia v0.5.8 contradiction track (tasks 1-11) seale |
| 218 | 2026-04-14T10:28:16-04:00 | `e135bc6d153f` | shipping: fix sealing scan surface for v0.5.2 audit bundle |
| 219 | 2026-04-14T10:47:48-04:00 | `2342898dcfa2` | docs: regenerate IMPORT_GRAPH for contradiction pipeline imports (v0.5.8 drift) |
| 220 | 2026-04-14T10:56:59-04:00 | `c84dff919642` | fix(tfp): satisfy noone path literal gate (docs, handoff, paths) |
| 221 | 2026-04-14T11:00:08-04:00 | `557a01237f23` | fix(tfp): track tfp_v1 dict_a/runtime and dict_b skeleton for CI layout test |
| 222 | 2026-04-14T11:15:34-04:00 | `dcec99f9aa00` | docs: rebaseline dead-weight budget for v0.5.8 module growth (91 unreferenced) |
| 223 | 2026-04-14T11:25:39-04:00 | `cbc1253f57e4` | refactor(engine): move module ALIASES to engine; fix core/modules boundary |
| 224 | 2026-04-14T11:30:27-04:00 | `2c84f16c67ef` | docs: regenerate IMPORT_GRAPH_ENGINE after module_aliases split |
| 225 | 2026-04-14T11:34:06-04:00 | `f3a77463772f` | tools: skip RAW dict_a corpus check in CI when gitignored asset absent |
| 226 | 2026-04-14T11:41:38-04:00 | `ed42d3c4e972` | test: expect contradiction_package on run_sealed_multiscale_stack signature |
| 227 | 2026-04-14T12:01:09-04:00 | `551fe81a75cd` | test(fixtures): commit CI TFP bundle manifest calibration + 09_session_topology for release gate |
| 228 | 2026-04-14T14:02:03-04:00 | `1d5061dded14` | docs(tfp): single bundle output folder rule (TFP_VALUES_LIST §0) |
| 229 | 2026-04-14T14:07:47-04:00 | `b0a8a9cc9bc8` | chore(outputs): standardize TFP dirs under outputs/tfp/ + default paths |
| 230 | 2026-04-14T14:31:01-04:00 | `f46479eafa2f` | test(tfp): track operator narrative fixture tests/fixtures/tfp/input.txt |
| 231 | 2026-04-15T11:54:28-04:00 | `6d9b83042b10` | feat(output_views): Vite hex matrix viewer + build script for browser deploy |
| 232 | 2026-04-15T12:28:16-04:00 | `9f89613d40ea` | feat(hex_matrix_viewer): semantic layout, isolated render modes, coherence, schema |
| 233 | 2026-04-15T13:01:37-04:00 | `abda11ec0cd6` | feat(hex_matrix_viewer): 12x24 F(s,b) lattice + flat/cylinder/sphere projections |
| 234 | 2026-04-15T13:17:11-04:00 | `8905a3034e97` | feat(hex_matrix_viewer): unified project(s,b,mode); spheroid + pole merge toggle |
| 235 | 2026-04-15T13:25:19-04:00 | `9894c8e04dcd` | feat(hex_matrix_viewer): diamond inspection layout (288 cells, band-centered) |
| 236 | 2026-04-20T06:28:30-04:00 | `35d388e453d8` | 123 |
| 237 | 2026-05-11T04:40:55-04:00 | `85e5d7f1222a` | feat(api): TFP-CHROMA-04 — /inspector/tfp-corpus/compose endpoint (spec §6) |
| 238 | 2026-05-11T04:45:32-04:00 | `965b9e003bc0` | feat(hex-matrix): TMX-10 — RelationsPanel + appear/disappear side panel |
| 239 | 2026-05-11T04:49:04-04:00 | `0e3b7971432f` | docs(specs): TMX-11 — T3 supervisor prompt pack + diff slots |
| 240 | 2026-05-11T04:50:20-04:00 | `d69df05689ab` | feat(i18n): TMX-14 — RU UX copy for matrix labels, T1-T3 tiers, tooltips |
| 241 | 2026-05-11T04:52:03-04:00 | `29fdb829fbd6` | test(hex-matrix): TMX-15 — gold fixture + snapshot tests + D3 smoke |
| 242 | 2026-05-11T04:53:17-04:00 | `8d090f1b28e3` | docs(chroma): TMX-16+17 — reference_literature ingest path + timeline layer query contract |
| 243 | 2026-05-11T04:57:27-04:00 | `0cec2ff6a0f9` | docs(tmx): TMX-18..24 — PII review, operator runbook, QA checklist, a11y, integration, design, closure |
| 244 | 2026-04-07T02:36:52-04:00 | `a5a17fbf6bcf` | output_views: iteration_segment_openai_v1 schema, segment package, Kernberg prompts, tests (Gena OUT-VIEW-01/02) |
| 245 | 2026-04-07T02:39:57-04:00 | `f14e6a6c9f8f` | output_views: Session Inspector MVP route, panes, deep links, T54/T55 docs (Gena OUT-VIEW-03) |
| 246 | 2026-04-07T02:43:09-04:00 | `fbb1e7e50b4a` | output_views: segment export.json, copy UI, optional OpenAI proxy, rate limit doc, make target (Gena OUT-VIEW-04) |
| 247 | 2026-04-07T02:45:45-04:00 | `22664d45d211` | output_views: PII export dialog, safety/license/flags/rollback docs (OUT-VIEW-05 Daniel epic) |
| 248 | 2026-04-07T03:10:28-04:00 | `8af5ab7c747e` | output_views: T02 build session_inspector_v1 from TFP pipeline dir (OUT-VIEW-FULL-01) |
| 249 | 2026-04-07T03:13:13-04:00 | `dc333b0ab7c5` | output_views: generate_inspector_fixture + Makefile; FULL-02 pipeline fixture docs |
| 250 | 2026-04-07T03:15:48-04:00 | `dfc54ed72d4c` | output_views: FULL-03 Pane C audit planes + relations strip; tests |
| 251 | 2026-05-18T14:18:05-04:00 | `dca9675975c3` | Restore Django output_views skeleton and deploy docs after cherry-pick. |
| 252 | 2026-05-18T14:18:33-04:00 | `2a69bcb38fab` | Add prichindel systemd unit and restore full hesperia nginx vhost. |
| 253 | 2026-05-18T15:51:33-04:00 | `f7324eede8a9` | merge: origin/main into prod main (keep OUT-VIEW + TMX; align +9 -60) |
| 254 | 2026-05-18T15:54:33-04:00 | `2aa1d43cb0e2` | prod(prichindel): deploy pins for Session Inspector + site root |
| 255 | 2026-05-18T15:59:59-04:00 | `ff55ef46810b` | draw-line(2026-05-18): rollback marker — README + ROLLBACK-LINE doc |
| 256 | 2026-05-18T16:12:25-04:00 | `3b31604fa22e` | chore(prod): remove docs/ (documentation on igareosh/hesperia) |
| 257 | 2026-05-18T16:12:25-04:00 | `ce5818d0c92d` | chore(prod): remove root team and planning markdown |
| 258 | 2026-05-18T16:12:25-04:00 | `dedc2987eb14` | chore(prod): remove governance/ narrative |
| 259 | 2026-05-18T16:12:25-04:00 | `137806d19273` | chore(prod): remove release narrative markdown |
| 260 | 2026-05-18T16:12:25-04:00 | `830e79e16737` | chore(prod): remove specs narrative markdown |
| 261 | 2026-05-18T16:12:25-04:00 | `b13d7f221857` | chore(prod): minimal README pointer to dev repo |
| 262 | 2026-05-18T16:16:41-04:00 | `d3260f910c6e` | ci(prod): prod-code-only workflow and verifier script |
| 263 | 2026-05-18T16:16:50-04:00 | `326c69697d97` | chore(prod): remove research/ (reference corpus on igareosh/hesperia) |
| 264 | 2026-05-18T16:16:50-04:00 | `c8f563399d16` | chore(prod): remove runtime and tools narrative markdown |
| 265 | 2026-05-18T16:16:50-04:00 | `594411f4a6d4` | chore(prod): gitignore and untrack outputs markdown |
| 266 | 2026-05-18T16:17:03-04:00 | `e93c6f550e02` | fix(prod): restore research Python; strip reference markdown to dev repo |
| 267 | 2026-05-18T16:17:11-04:00 | `627d461d9a44` | ci(prod): allow research Python; forbid research markdown only |
| 268 | 2026-05-18T17:34:14-04:00 | `00f099088c34` | chore(prod): remove legacy/ and specs/ (dev documentation on igareosh/hesperia) |
| 269 | 2026-05-18T17:34:15-04:00 | `12f07f956e04` | chore(prod): remove module and output_views dev markdown (corpus untouched) |
| 270 | 2026-05-18T17:34:15-04:00 | `f80cc87ed92a` | chore(prod): remove examples, release, assets narrative md (not corpus/dicts) |
| 271 | 2026-05-18T17:34:50-04:00 | `fa6f01ebcf28` | fix(prod): restore specs yaml/json config; strip specs markdown only (corpus untouched) |
| 272 | 2026-05-18T17:34:54-04:00 | `276ea704f3ef` | ci(prod): verifier corpus-safe — dev md/specs prose only |
| 273 | 2026-05-18T17:35:05-04:00 | `d7a88d172341` | chore(prod): remove dict/tools dev README (corpus yaml/json untouched) |
| 274 | 2026-05-18T17:35:05-04:00 | `12f931a706bb` | ci(prod): corpus-safe verifier (specs yaml allowed) |
| 275 | 2026-05-18T17:37:51-04:00 | `8cfb4841bcc7` | chore(prod): immaculate sweep — dev notes removed (backup on igareosh/hesperia) |
| 276 | 2026-05-18T17:40:56-04:00 | `56f5ac823335` | draw-line(2026-05-18): dev-ready — immaculate prod, docs on igareosh/hesperia |
| 277 | 2026-05-18T17:41:08-04:00 | `18178deb63c9` | ci(prod): allow DEV-READY-LINE marker on immaculate tree |
| 278 | 2026-05-18T22:47:37+00:00 | `235ea30dd7c5` | fix(prod): gunicorn, security settings, sessions view, nginx hardening |
| 279 | 2026-05-18T22:49:28+00:00 | `77810ff9ef1c` | fix(prod): sync hesperia-api.service to match deployed config |
| 280 | 2026-05-18T23:04:28+00:00 | `41e051369a6f` | chore(v0.6.0): Python compliance pass — version bump, API cleanup |
| 281 | 2026-05-18T23:28:32+00:00 | `d4f4f67b4b00` | chore: checked by Felix (Claude Code) 2026-05-20 — python compliance v0.6.0 sealed, prod repo |
| 282 | 2026-05-21T02:55:52-04:00 | `2e712184fccc` | feat(output_views): inspector nav link to hex-matrix viewer (TMX-22) |
| 283 | 2026-05-21T03:08:19-04:00 | `d313bfddc63c` | fix(output_views): STATIC_URL /static/ and require collectstatic for WhiteNoise |
| 284 | 2026-05-27T22:15:30+03:00 | `9848c16fbab4` | docs(brand): Hesperia logo canonical visual description v1 and v1.2 |
| 285 | 2026-05-27T20:13:29+00:00 | `297e40873b0e` | Grace: ingest Hesperia logo image drop from operator cache. |
| 286 | 2026-05-28T11:34:47+00:00 | `257d81eee446` | fix: align release version authority with v0.6.0 |
| 287 | 2026-05-28T11:34:47+00:00 | `e196fce0488b` | fix: validate prod tree from shipping context |
| 288 | 2026-05-28T11:44:24+00:00 | `fa923eee0cfe` | release: add sealed v0.6.0 baseline package |
| 289 | 2026-05-28T12:08:50+00:00 | `fc7c5cf71df1` | build: add checked docker bundle for v0.6.0 |
| 290 | 2026-05-28T12:14:22+00:00 | `c9e95570789f` | release: add 0.6.0 agentic install contract |
| 291 | 2026-05-28T13:33:06+00:00 | `6a13eb12bb7c` | release: publish atomic 0.6.0 on tag push |
| 292 | 2026-05-28T13:34:58+00:00 | `676dd1c9c899` | ci: trigger atomic 0.6.0 release publish on branch push |
| 293 | 2026-05-28T16:37:39+03:00 | `7311d600b46f` | Merge pull request #26 from Atomic-Commits-Team/hesperia-v0.6.0-release |
| 294 | 2026-05-28T13:40:31+00:00 | `a06c8289c7e5` | release: refine atomic 0.6.0 release notes |
| 295 | 2026-05-28T13:48:07+00:00 | `f695936ffa49` | release: sanitize 0.6.0 public release artifacts |
| 296 | 2026-05-28T14:07:19+00:00 | `ee78240a1458` | ci: drop dict payload gates from sealed runtime release repo |
| 297 | 2026-05-28T14:07:19+00:00 | `536323fe63c4` | ci: drop dict payload gates from sealed runtime release repo |
| 298 | 2026-05-28T13:48:07+00:00 | `87f5a5b62aea` | release: sanitize 0.6.0 public release artifacts |
| 299 | 2026-05-28T17:17:41+03:00 | `482c2525def4` | ci: drop docs-dependent gates from prod sealed runtime workflow |
| 300 | 2026-05-28T17:21:11+03:00 | `47c91cac8fe2` | ci: trigger sealed runtime gate on sanitized main |
| 301 | 2026-05-28T17:23:47+03:00 | `46f63cf589a7` | ci: add workflow_dispatch to sealed runtime gate |
| 302 | 2026-05-28T17:37:08+03:00 | `d06f6744f55f` | ci: sealed runtime gate on push to main only (not PR reruns) |
| 303 | 2026-05-28T17:40:47+03:00 | `6df2695e0682` | fix(tfp): restore tfp_v1/nlp skeleton dir for layout gate (TFP-DATA-T15) |
| 304 | 2026-05-28T17:45:23+03:00 | `3de9974fa1d0` | Merge pull request #27 from Atomic-Commits-Team/hesperia-v0.6.0-release |
| 305 | 2026-06-14T13:31:18+03:00 | `f87b2bb1eaef` | HES-61-01: Python /analyze engine_result contract envelope. |
| 306 | 2026-06-14T13:47:57+03:00 | `cc94b09d4b81` | Default OpenAI model gpt-4o-mini (env-driven, not gpt-5.2). |
| 307 | 2026-06-14T16:01:41+03:00 | `16286faaf04c` | Ethan: seal Hesperia 0.6.3 GitHub archive — E2E without prod dicts/corpus. |
| 308 | 2026-06-14T16:31:39+03:00 | `9bf0289da52b` | Ethan: 0.6.3 archive example outputs (envelope, Teacher, IRC trace, analyze). |
| 309 | 2026-06-14T16:59:44+03:00 | `122d45bfeb6d` | merge: reconcile 0.6.1 analyze line (cc94b09) with 0.6.3 archive seal (16286fa) |
| 310 | 2026-06-14T17:05:02+03:00 | `e9eaa0764db6` | Add runtime/irc_teacher/ — 0.6.3 IRC Teacher path in product repo. |
| 311 | 2026-06-14T23:02:55+03:00 | `b37a67629bfd` | docs(dev): brain-export wave2 Hesperia from cursor (2026-06-14T2002Z) |
| 312 | 2026-06-14T20:07:54+00:00 | `6f86a9620a6b` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 313 | 2026-06-14T20:09:34+00:00 | `bb276954592d` | docs(dev): archive operational/assignments brain tree (2026-06-14) |
| 314 | 2026-06-14T20:11:44+00:00 | `988eb336cabd` | docs(dev): archive brain scripts tree (2026-06-14) |
| 315 | 2026-06-14T20:16:43+00:00 | `11bce88a5868` | docs(dev): final Hesperia brain sweep (2026-06-14) |
| 316 | 2026-06-14T20:16:52+00:00 | `bc920b411ef2` | docs(dev): final Hesperia brain sweep (2026-06-14) |
| 317 | 2026-06-14T22:04:24+00:00 | `bd151586ca36` | docs(dev): brain-export wave2 Hesperia from cursor (2026-06-14T2204Z) |
| 318 | 2026-06-14T22:04:42+00:00 | `0c8c78cf51f1` | docs(dev): final Hesperia brain sweep (2026-06-14) |
| 319 | 2026-06-14T22:04:47+00:00 | `4ad33a59cbcd` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 320 | 2026-06-20T13:17:06+00:00 | `81fcae344f8a` | docs(colombo): modular core, scoped modules, and branch architecture |
| 321 | 2026-06-20T13:32:53+00:00 | `0fa762213843` | docs(colombo): Class A cored vs Class B non-cored modules |
| 322 | 2026-06-20T13:32:59+00:00 | `3b9001c15858` | docs(colombo): fix dev-export path references in architecture §8 |
| 323 | 2026-06-20T13:35:23+00:00 | `df77d59d920d` | docs(colombo): pointer to mandatory-read policy for dev agents |
| 324 | 2026-06-28T12:59:48+00:00 | `e36d6a560500` | Add HSR-V7 router envelope schema and fingerprint v0.1. |
| 325 | 2026-06-29T11:55:31+00:00 | `bd869e2d8b15` | HSR-V7: full router implementation — pre-LLM compiler, post-LLM audit, governance modes, /product/interpret |
| 326 | 2026-06-29T12:15:41+00:00 | `99e17a4b65bd` | FPF-V7-13: fpf-thinking-map governed OpenAI calibration calls. |
| 327 | 2026-06-29T12:19:43+00:00 | `c0f76a672a06` | HSR-V7-08/11: corpus policy mirror + router gold test matrix. |
| 328 | 2026-06-29T12:28:53+00:00 | `85c407a51bbf` | docs: HSR-V7 version bump plan 0.6.3→0.6.5→0.7.0 (A-08) |
| 329 | 2026-06-29T12:36:47+00:00 | `5a094b63fb01` | docs: Gate B Gena classifications B-08/13/14 |
| 330 | 2026-06-29T12:47:03+00:00 | `322ee0110f0c` | HSR-V7 Gate C: Class A drain verified, observability wired, fusion confirmed |
| 331 | 2026-06-29T12:53:36+00:00 | `30b632aaedaf` | HSR-V7-C-21: VERSION.yaml 0.6.5 fusion milestone |
| 332 | 2026-06-29T14:45:07+00:00 | `7ffb606a20da` | HSR-V7 Gate C/D: schema validation, gold fixtures, API decision tests. |
| 333 | 2026-06-29T14:48:08+00:00 | `31d487210928` | HSR-V7 Gate E: product copy, API docs, operator surface labels. |
| 334 | 2026-06-29T14:53:23+00:00 | `7f7c8d2e6018` | COBALT MVP adapter: CHROMA-2 retrieve, flag off, hooks. |
| 335 | 2026-06-29T15:19:41+00:00 | `b66b35cbe3e4` | COBALT G2 attribution tool, chromadb 1.5 fix, gold test. |
| 336 | 2026-06-29T15:20:51+00:00 | `06bf3346a778` | H070 sandbox apply: update_edge_weight gate chain G1-G9. |
| 337 | 2026-06-29T15:59:29+00:00 | `e9cc40677812` | H070 pre-SEAL: Inspector Pane 2, replay, gold tests, ledger. |
| 338 | 2026-06-29T16:15:32+00:00 | `7af214c360e9` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 339 | 2026-06-30T22:11:47+00:00 | `63a2295b3924` | docs/foundations: Phase 2 exhaustive scientific documentation (L1–L11, all corners, eras, parameters) |
| 340 | 2026-07-01T11:09:55+00:00 | `9e22af322add` | docs: ISO-grade LTS documentation program + restored per-layer specs |
| 341 | 2026-07-04T14:59:23+00:00 | `6596c6cf515a` | sync: METRIC wave v0.7.0 (anchor_map/GCS registry, 24_SPEC, ISO doc index) |
| 342 | 2026-07-04T14:59:44+00:00 | `df96723c2e5b` | sync: fpf_bridge Layer 11 baseline (v7.0 + this session's v7.2 Phase 1-4/v7.3 code) |
| 343 | 2026-07-04T15:00:05+00:00 | `707737b95e30` | feat: fpf_bridge v7.2/v7.3/v7.4 specs + agentic Cursor interface + COBALT scale-up prep |
| 344 | 2026-07-04T15:07:53+00:00 | `3b283a1eb5b4` | docs: repo-wide consistency pass for fpf_bridge v7.2-v7.4 + new AGENTS.md |
| 345 | 2026-07-04T15:14:31+00:00 | `eec627aceb32` | docs: era 8 file, output_catalog §12 evidence-surface update, ISO cross-ref |
| 346 | 2026-07-04T15:19:34+00:00 | `b811319b9106` | docs(iso): re-verify all built rows against era 8, per the matrix's own LTS rule |
| 347 | 2026-07-04T15:23:31+00:00 | `4efaf87bf600` | docs: verify and record that core/ was never touched across the entire era 8 wave |
| 348 | 2026-07-04T15:49:10+00:00 | `a8fdd9809dda` | docs: tighten Hesperia agentic orientation |
| 349 | 2026-07-04T15:51:21+00:00 | `48c3421e0faf` | docs: propagate Hesperia naming discipline |
| 350 | 2026-07-04T15:56:10+00:00 | `a9ae78fd8045` | docs: add Hesperia parameter rationale map |
| 351 | 2026-07-04T16:02:35+00:00 | `e594da61f395` | docs: add Upcelerator productization QA |
| 352 | 2026-07-04T16:03:46+00:00 | `4d053f4c3c08` | docs: spread Upcelerator product wording |
| 353 | 2026-07-04T16:08:53+00:00 | `6d536ed97673` | docs: connect product wording to evidence surfaces |
| 354 | 2026-07-04T16:14:04+00:00 | `d074600a43b3` | docs: ingest Upcelerator market and competition baseline |
| 355 | 2026-07-04T16:20:42+00:00 | `b24bc5981e8c` | docs: expose productization routes in indexes |
| 356 | 2026-07-04T17:04:13+00:00 | `d23c5fbc46bd` | docs: add Aurel stabilization rules for productization |
| 357 | 2026-07-06T06:41:54+00:00 | `aec32febaf7e` | hesperia: align version authority and calibration packs |
| 358 | 2026-07-06T06:42:00+00:00 | `3de85145d93f` | docs: consolidate HSR-V7 source of truth |
| 359 | 2026-07-06T06:43:15+00:00 | `403590d25fb8` | merge origin/main before HSR-V7 consolidation push |
| 360 | 2026-07-06T06:44:47+00:00 | `5778de194eb2` | hesperia: mirror merged version metadata |
| 361 | 2026-07-06T06:51:42+00:00 | `0fb1f17a15be` | docs: apply ISO-grade rename and archive consolidation |
| 362 | 2026-07-06T07:14:27+00:00 | `f216ab220cf2` | refactor: fuse core domain and runtime canon |
| 363 | 2026-07-06T07:26:20+00:00 | `b6452aa52709` | refactor: converge canonical core imports |
| 364 | 2026-07-06T07:31:29+00:00 | `67f9e6680273` | docs: converge source truth after core fusion |
| 365 | 2026-07-06T07:51:57+00:00 | `dbadc2017d2f` | hesperia: remove obsolete core-expulsion shims |
| 366 | 2026-07-06T08:08:14+00:00 | `4cea408c400f` | hesperia: converge core output wiring |
| 367 | 2026-07-19T11:56:10+00:00 | `b3b0c44b4fcf` | fix(shipping): route load_context_packet_json through service facade |
| 368 | 2026-07-19T11:56:25+00:00 | `31e70088c3b6` | fix(sealing-scan): close 13-day CI red on Sealed runtime gate |
| 369 | 2026-07-19T11:56:29+00:00 | `be7eea2aa377` | docs(iso): correct stale corners/*.md count in traceability matrix |
| 370 | 2026-07-19T12:22:04+00:00 | `f39265703488` | feat(gtp): GTP-01/02 — six-side logical+semantic operator registry + schema |
| 371 | 2026-07-19T12:22:11+00:00 | `3aeb2cea1cd0` | feat(gtp): GTP-03 — hex_rotation calibration + per-side match score |
| 372 | 2026-07-19T12:22:19+00:00 | `e49fbdaece7c` | feat(gtp): GTP-04 — PointZeroDelta broadcast + CoherenceField Psi |
| 373 | 2026-07-19T12:22:27+00:00 | `eb3488b7be6e` | feat(gtp): GTP-05 — GTPA next-hex selection over legal neighbors |
| 374 | 2026-07-19T12:22:34+00:00 | `9f794044235f` | feat(gtp): GTP-06 — ThoughtImprint + path-discovery pipeline + package exports |
| 375 | 2026-07-19T12:22:41+00:00 | `9da62413bfca` | feat(gtp): GTP-07 — wire gtp block into RouterInputEnvelope, flag-gated |
| 376 | 2026-07-19T12:22:46+00:00 | `3e1603973ff9` | test(gtp): GTP-08 — deterministic gold matrix |
| 377 | 2026-07-19T12:22:53+00:00 | `0e1389ddf25c` | docs(specs): promote 23_SPEC GTP formalization with implementation status |
| 378 | 2026-07-19T12:32:27+00:00 | `f035a0b41da7` | docs(specs): GTP invocation guide + forward-direction note |
| 379 | 2026-07-19T12:44:31+00:00 | `67a60a34832c` | docs(specs): resolve §0.3 forward-direction tension, cross-link Ethan draft |
| 380 | 2026-07-19T13:14:14+00:00 | `737e19e8dad9` | docs: Ethan ratify fpf_bridge v7.2/v7.3/v7.4 (Hesperia day run) |
| 381 | 2026-07-19T13:41:29+00:00 | `58377cc20054` | feat(router): FPF-HSR-13 — mandatory logical/weight/source_activation blocks |
| 382 | 2026-07-19T13:41:40+00:00 | `f87723260dda` | feat(api): FPF-HSR-11 — InterpretBody.context_packet on /product/interpret |
| 383 | 2026-07-19T13:41:49+00:00 | `fa24630a48a7` | feat(cli): FPF-HSR-12 support — thinking_map_outcome extraction in router-inquire |
| 384 | 2026-07-19T13:49:49+00:00 | `3b2653b10ed2` | feat(fpf_inspect): FPF-BUII bottom-up GapReport dig endoscope |
| 385 | 2026-07-19T14:22:41+00:00 | `ae39bcc4a822` | Ship pre-0.7 HAND wire: pin 1.5.0, Option B, ops map, GapReport flag, gold harness. |
| 386 | 2026-07-25T19:26:36+00:00 | `f76297325c59` | chore(pin): align fpf-thinking-map to 1.9.2 (ATM2-43) |
| 387 | 2026-07-25T19:34:34+00:00 | `d5b5c650f9a7` | docs(wiki): export Colombo Hesperia parameter wiki to brain-export |
| 388 | 2026-07-25T19:43:52+00:00 | `ddc7a6ca10b0` | fix(fpf): align FPF_PIN_EXPECTED to 1.9.2 for pre-seal wiring |
| 389 | 2026-07-25T22:13:58+00:00 | `fc7a761386b8` | fix(e2e): correct field_dynamics_enabled import source in run_e2e_all |
| 390 | 2026-07-25T22:45:11+00:00 | `0fcbe8993603` | release: seal Hesperia system_version 0.7.0 |
| 391 | 2026-07-26T11:56:55+00:00 | `b14db04b1476` | feat(dev-test): add hesperia-dev-test Class B diagnostic battery |
| 392 | 2026-07-26T13:22:21+00:00 | `f6d5dab9f1b0` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 393 | 2026-07-26T13:23:42+00:00 | `8def51645fa4` | docs: retire remaining Atomic-Commits-Team/hesperia references (abandoned 2026-07-26) |
| 394 | 2026-07-26T14:52:49+00:00 | `2629817feae4` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 395 | 2026-07-26T15:09:06+00:00 | `741a7442bbd1` | feat(dev-test): Bench-0 gold witness on hesperia-dev-test + bump fpf-thinking-map to 1.9.3 |
| 396 | 2026-07-30T09:34:01+00:00 | `8754c7897634` | docs(dev): archive operational/assignments brain tree (2026-07-30) |
| 397 | 2026-07-31T01:35:32+00:00 | `fbbb316eca84` | core: graduate module math to core, sever core from all extensions/modules, adopt sphereV genesis taxonomy |
| 398 | 2026-07-31T02:05:24+00:00 | `efc85269302c` | merge: reconcile session work (fbbb316e) with concurrent dev/brain-link commits from origin |
| 399 | 2026-07-31T03:58:47+00:00 | `5ae3a8799fd0` | test: fix two regressions surfaced by the core severance / v06 retirement |
| 400 | 2026-07-31T09:24:49+00:00 | `342b7aeade75` | core/sphere: close both RAD guard violations left from core severance |
| 401 | 2026-07-31T10:37:11+00:00 | `639d087fcd95` | core/engine: graduate generic orchestration+physics from hesperia/engine; relocate research/experimental code; root clea |
| 402 | 2026-07-31T11:34:24+00:00 | `f44b3454edeb` | core/math: hammer-and-anvil pass 1 — remove confirmed-dead legacy/duplicate math |
| 403 | 2026-07-31T12:40:37+00:00 | `ed5a2ff97f7b` | perf+fix: cache ontology loaders, isolate TFP from core test suite, fix 7 stale-path regressions |
| 404 | 2026-07-31T13:20:44+00:00 | `648a055428af` | chore: move deploy/ and benchmarks/ (TRIZ-only root dirs) into hesperia/extensions/triz/ |
| 405 | 2026-07-31T14:17:29+00:00 | `bc1ae3153e97` | chore: fold data/config folders into assets/, scripts/ into tools/ — root 22 -> 16 |
| 406 | 2026-07-31T17:45:23+00:00 | `2032d3e2eee0` | docs+guard: formalize root as a closed set — REPO_STRUCTURE_POLICY.md + CI lock |
| 407 | 2026-08-01T07:07:45+00:00 | `fbe4f9c311fc` | module: consolidate TFP math duplication — math_v1.py into engine/tfp_math.py |
| 408 | 2026-08-03T13:09:38+00:00 | `0e4793fa07b2` | core: remove orphaned output_contracts_compat.py, fix stale _deprecated README |
| 409 | 2026-08-03T13:09:44+00:00 | `8bcac49129fd` | test(gtp): fix transposed rotation/exit_side columns in gold matrix |
| 410 | 2026-08-03T13:09:52+00:00 | `b8f6e7a69f23` | test(tfp): fix DLCR run-id drop, renamed release-gate check keys, stale threshold |
| 411 | 2026-08-03T13:10:05+00:00 | `819399ee6587` | metric: wire meta.hesperia_metric at runtime boundary; xfail deferred v0.7.0 rows |
| 412 | 2026-08-03T13:10:11+00:00 | `225a69ac68d2` | fix(build): remove stale lexicon/ COPY from shipping/product Dockerfiles |
| 413 | 2026-08-03T13:23:59+00:00 | `1d7902b71baf` | fix(ci): allow core.projection in shipping surface — Sealed runtime gate has been red since 07-31 |
| 414 | 2026-08-03T13:24:08+00:00 | `6c895cd0b226` | fix(ci): stale lexicon/ path crashes prod-code-only gate; CLI help text drift |
| 415 | 2026-08-03T13:37:00+00:00 | `1de9150d5021` | security: bump torch/transformers/huggingface-hub to close dependabot CVEs |
| 416 | 2026-08-03T13:37:13+00:00 | `6b79d1e64754` | security: bump vite/postcss/esbuild/@babel-core to close dependabot CVEs |
| 417 | 2026-08-03T14:07:36+00:00 | `8b75b601237c` | security: coordinated sentence-transformers 2.7.0 -> 5.6.1 major bump, closes remaining CVEs |
| 418 | 2026-08-03T14:43:35+00:00 | `1eec707120ad` | chore: remove requirements/embedding.txt + build-embeddings.txt — orphaned duplicates of surface.txt |
| 419 | 2026-08-03T15:41:20+00:00 | `a74987e48dae` | release: seal Hesperia system_version 0.7.1 |
| 420 | 2026-08-03T18:00:09+00:00 | `857651455155` | docs: file two external research drops (dictionary schema proposal, market positioning) |
| 421 | 2026-08-04T05:57:43+00:00 | `f003066adc2c` | docs(wiki): re-export Colombo Hesperia parameter wiki from brain (2026-08-04) |
| 422 | 2026-08-04T05:59:08+00:00 | `264c1d62f34a` | docs(wiki): update EXPORT-NOTE — Atomic split is stale, note promote-onward path |
| 423 | 2026-08-04T06:14:51+00:00 | `898abc23ecf4` | docs(wiki): re-export — fix module citations stale after core/domain KME move |
| 424 | 2026-08-04T06:22:06+00:00 | `cb9657fd3620` | docs(wiki): re-export — close dict_b.py cluster (module-ownership reclassification) |
| 425 | 2026-08-04T08:08:16+00:00 | `a17b948b81a8` | core: move dict_a/dict_b/topology/metrics modules to hesperia/modules/default/ |
| 426 | 2026-08-04T08:08:38+00:00 | `a1940da0ab42` | docs(wiki): re-export — fix stale core/runtime path in tension_from_conflict note |
| 427 | 2026-08-04T14:57:06+00:00 | `2564c5022b9f` | docs: fix stale specs/canon/ paths in parameter_catalog.md + output_catalog.md |
| 428 | 2026-08-04T15:03:44+00:00 | `4f5fe2263483` | docs(wiki): re-export — HWIKI-CATALOG-L1 batch (36 new pages) |
| 429 | 2026-08-04T15:32:30+00:00 | `c27424f3a6fc` | docs(wiki): re-export — HWIKI-CATALOG wave complete (230 new pages, L1-L9 full census) |
| 430 | 2026-08-04T15:46:27+00:00 | `dd87e2ec4b9a` | docs(wiki): re-export — energy_conservation_tolerance, last crosscheck gap |
| 431 | 2026-08-04T15:52:04+00:00 | `6ac5c0b56ac6` | docs(wiki): re-export — L6 Group-IV stubs, last next-wave candidate closed (401 items) |
| 432 | 2026-08-04T16:03:38+00:00 | `7056953c628a` | core: drain KSI-Inspector from Tersagor vendored copy into core/domain/ksi/ |
| 433 | 2026-08-04T16:20:42+00:00 | `d1ad829c0d87` | core: drain GTP-schemas + full IPoV (METRIC-23) from Tersagor vendored copy |
| 434 | 2026-08-04T16:28:38+00:00 | `a9408e69ede3` | docs(wiki): re-export — structure hubs corrected, KSI/IPoV landing noted |
| 435 | 2026-08-04T16:40:27+00:00 | `1d89c146fef1` | release: seal Hesperia system_version 0.7.2 — module boundary + KSI/IPoV drain |
| 436 | 2026-08-05T09:16:24+00:00 | `81c260536aa8` | feat(math-behav): wire KSI-Inspector + KAM lens + L5/L6 stub fills |
| 437 | 2026-08-10T09:24:47+00:00 | `29c435038f4a` | feat(layer6): add flag-gated epsilon series |
| 438 | 2026-08-10T09:31:46+00:00 | `b4adcae62845` | feat(metric): expose flag-gated IPoV on analyze |
| 439 | 2026-08-10T10:04:55+00:00 | `4e9b2961d73c` | feat(l6): flag-gated /analyze perturbation producer + METRIC-24/25 path cost |
| 440 | 2026-08-10T12:29:41+00:00 | `7c9b516a89b6` | feat(testing): flag-gated testing_params envelope for LLM/agent yield |
| 441 | 2026-08-10T14:46:38+00:00 | `e0a8df5318d4` | fix(topology): default area grain is 12; isolate optional ten-area module |
| 442 | 2026-08-10T14:46:49+00:00 | `d85db8224a9b` | docs(topology): clarify 10+2 was historical packing, default grain is 12 |
| 443 | 2026-08-10T14:50:23+00:00 | `46f71170fe28` | feat(math): area-math grain classifier switch (12 default / 10 optional) |
| 444 | 2026-08-10T14:55:33+00:00 | `e25965a76da5` | feat(math): propagate area-math grain switch across projection/reserve paths |
| 445 | 2026-08-10T15:13:21+00:00 | `4b1d5bd9a86e` | feat(api): side-by-side TFP analyze profile (HESPERIA_ANALYZE_PROFILE) |
| 446 | 2026-08-10T15:27:09+00:00 | `1ea6ddb91848` | Make TFP Class B lane operational for analyze+interpret instructor. |
| 447 | 2026-08-10T15:44:18+00:00 | `63b22d287bf1` | Wire real OpenAI client for /product/interpret teacher path. |
| 448 | 2026-08-10T15:50:02+00:00 | `f1aecb912dea` | Load OpenAI key from CC tip openai_api_key.txt when env unset. |
| 449 | 2026-08-10T16:42:44+00:00 | `7c70d3411800` | Wire TFP Class B to CHROMA-2 retrieve and dual-face clients. |
| 450 | 2026-08-11T11:21:44+00:00 | `83a601995e5d` | docs(dev): archive brain EOD collect/blocker reports (2026-08-11) |
| 451 | 2026-08-13T14:17:15+00:00 | `c0de6e7093e4` | Add lexicon working tree for sync readiness. |
| 452 | 2026-08-13T14:18:14+00:00 | `caac3bb1ab25` | Wire TFP MVP context query_text through interpret/inquiry paths. |
| 453 | 2026-08-13T14:24:59+00:00 | `22d8d0f0adfd` | Archive brain operational/assignments slim 2026-08-13 (KEEP 54+). |
| 454 | 2026-08-13T14:34:07+00:00 | `68b5ce046c8a` | Archive brain operational/external and ops-method qa runs (2026-08-13). |
| 455 | 2026-08-17T07:23:37+00:00 | `9ecbf4d5a24d` | Add Chiron to Named-owner map: params/math/corpus calibration entity. |
| 456 | 2026-08-17T07:32:56+00:00 | `9b98843c2f28` | Expand Chiron: standing performance authority, recipes/README, doc index. |
| 457 | 2026-08-17T07:38:25+00:00 | `9cf30789e707` | Chiron: note full brain-repo/MCP awareness in Named-owner map. |
| 458 | 2026-08-17T07:58:32+00:00 | `b69f7c2d88a3` | Chiron: ratified (Accepted), Named-owner map + doc index updated. |
| 459 | 2026-08-17T08:07:01+00:00 | `3b9b4b9208dc` | Document the dev/train boundary: shared-zone mode marker with Chiron. |
| 460 | 2026-08-17T10:33:16+00:00 | `13efe6b8ba26` | Add addressable location for parameter-combination recipes |
| 461 | 2026-08-17T10:41:13+00:00 | `416af736b5a0` | Bump nanoid to clear Dependabot alert #59 |
| 462 | 2026-08-17T13:46:47+00:00 | `7d9052501761` | router: wire real DLCR concept resolution into engine_trace for TFP profile |
| 463 | 2026-08-17T15:16:55+00:00 | `3668bb0e942f` | tfp profile: auto-pin sealed ACB calibration pack v0_6_0_clr_v052_5 |
| 464 | 2026-08-17T15:33:06+00:00 | `c1a1085368e5` | tfp_calibration_audit: accept engine_invariant_activation_v2, matching the gate |
| 465 | 2026-08-18T07:53:39+00:00 | `eecf0d77c894` | Land PC-001: TFP DLCR structural dict pin (full-stack, not fallback) |
| 466 | 2026-08-18T08:37:52+00:00 | `c195ca3b7c47` | Document TFP dict-pin + TRIZ topology combos; warn on --with-topology w/o --with-triz |
| 467 | 2026-08-18T08:57:43+00:00 | `0369540d0e22` | Add tfp_param_sweep.py — batch parametric-combo comparison tool |
| 468 | 2026-08-18T12:05:54+00:00 | `66b1abeaef26` | Fix calibration_release_gate.py: gate all sessions, not just sessions[0] |
| 469 | 2026-08-18T13:12:28+00:00 | `1660c89f7db9` | Redesign contradiction-grounding gate to family/area grain, not concept ID |
| 470 | 2026-08-18T14:31:23+00:00 | `83b5dbebeb03` | Add tfp_corpus Postgres schema pack for the live ops-method-pg instance. |
| 471 | 2026-08-18T14:45:43+00:00 | `b91691a39a89` | Add tfp_corpus Phase 2 ingest script and run it |
| 472 | 2026-08-18T15:30:04+00:00 | `684b2cc5bd84` | Abelard: verify tfp_corpus Phase 0-2 live, add backup + doc updates |
| 473 | 2026-08-18T16:04:42+00:00 | `89b644e0ddc8` | Wire Postgres-backed truth-point score (S/W/T) into contradiction reconciliation |
| 474 | 2026-08-18T16:27:59+00:00 | `ab9312c8bd17` | Ship CHI-001: first Chiron-tweaks recipe (truth-point grounding) |
| 475 | 2026-08-18T16:32:51+00:00 | `5c88b80917ef` | Add chiron_tweaks backlog + document the gather-then-recalibrate cadence |
| 476 | 2026-08-18T17:01:37+00:00 | `6d94bc0d185c` | Plan tomorrow's session start in the backlog file |
| 477 | 2026-08-19T06:49:14+00:00 | `4f88ae617140` | Gather phase complete: run remaining 10/14 real TFP sessions, log evidence |
| 478 | 2026-08-19T07:07:00+00:00 | `fb73f698c8d8` | Root-cause the zero_lex_share gate failure: dict_a_max_accepted truncates by position |
| 479 | 2026-08-19T08:01:51+00:00 | `b0b640528ec1` | Fix dict_a_max_accepted family-diversity starvation: 11/11 real sessions now pass the gate |
| 480 | 2026-08-19T08:07:10+00:00 | `b3678c1a9960` | Strike dict_a_max_accepted from open candidates, now fixed |
| 481 | 2026-08-19T10:42:58+00:00 | `4eaa399e8b08` | Ingest the real normalized TFP corpus into Postgres, separately from documents |
| 482 | 2026-08-19T10:43:36+00:00 | `8f3d731a0e99` | Close out ru_2_cleaned/en_2_cleaned investigation, log normalized_sentence ingest + ACB next step |
| 483 | 2026-08-19T11:23:42+00:00 | `54d5588a42ab` | Wire corpus to TFP structure inside Postgres (concept_link), tag v0.6.9 |
| 484 | 2026-08-19T12:28:09+00:00 | `4ab11c0a677c` | Seal v0_6_9: real ACB alignment merged, live on hesperia-analyze-tfp |
| 485 | 2026-08-19T12:36:43+00:00 | `dca808f1ec7b` | Support gpt-5-family reasoning models in the calibration OpenAI client |
| 486 | 2026-08-19T12:41:54+00:00 | `7ed082c04de1` | Log gpt-5-mini ACB re-run in progress (Phase 4c), check back 2-3h |
| 487 | 2026-08-19T18:01:42+00:00 | `4ea3e0939ee9` | Checkpoint accumulated links after every ACB pass, not just summary counts |
| 488 | 2026-08-19T18:03:19+00:00 | `3dff7710a572` | Log gpt-5-mini attempt 1 killed by session teardown, real cost lost, relaunched |
| 489 | 2026-08-19T18:15:30+00:00 | `976420e8d674` | Add binding rule: every paid API call must survive a crash |
| 490 | 2026-08-20T05:29:41+00:00 | `c18265a1dc3a` | Merge gpt-5-mini ACB findings into v0_6_9: 187 -> 203/283 concepts |
| 491 | 2026-08-20T05:30:25+00:00 | `fb49d0d7e82b` | Update v0_6_9 provenance note: 203/283 concepts, full regression verified |
| 492 | 2026-08-20T06:05:48+00:00 | `33a4a07bc953` | Collapse aspect-2..5 taxonomy over-split in v0_6_9: 283 -> 204 concepts |
| 493 | 2026-08-20T06:06:34+00:00 | `87ec682a3f82` | Update v0_6_9 provenance: 203/204 concepts after aspect-taxonomy collapse |
| 494 | 2026-08-20T06:31:24+00:00 | `7c09393fcb7a` | Collapse TFP_CLUSTER_005 into TFP_CLUSTER_004: 204 -> 203 concepts |
| 495 | 2026-08-20T06:32:08+00:00 | `308db9595c97` | Update v0_6_9 provenance: 203/203 concepts, full coverage of current catalog |
| 496 | 2026-08-20T06:52:57+00:00 | `7abb2eb094f4` | Promote TFP to v2/0.7.0 milestone; fix two version-consistency drifts |
| 497 | 2026-08-20T06:53:35+00:00 | `1f1ad4ac5ec5` | Note TFP v2/0.7.0 milestone in the postgres README |
| 498 | 2026-08-20T15:28:15+00:00 | `1780b41494e6` | Disambiguate coincidental label collisions + dedupe dict_b.jsonl (TFP v0_6_9) |
| 499 | 2026-08-20T15:41:56+00:00 | `fd06f88b13e0` | Revert the 8 disambiguation renames from 1780b414 -- they broke live scoring |
| 500 | 2026-08-20T15:42:23+00:00 | `192d09395409` | Document the rename-revert correction in BACKLOG.md |
| 501 | 2026-08-20T15:45:45+00:00 | `b91373b9f941` | Declare psycopg2-binary as a real dependency (tfp_corpus Postgres access) |
| 502 | 2026-08-20T17:34:55+00:00 | `fd658ba6d0cd` | CHI-002 spec: TFP batch-pipeline KME grain default + marker_index gap |
| 503 | 2026-08-20T17:54:08+00:00 | `4fe53cad271a` | CHI-002-01: batch KME grain=10 default + explicit marker_index at call site |
| 504 | 2026-08-20T18:31:45+00:00 | `dd5d4abf3bc7` | CHI-003: A10-dominance investigation closed with real evidence, theory question to Colombo |
| 505 | 2026-08-20T18:32:14+00:00 | `8a8c74fea87c` | Close A10-dominance backlog item, pointer to CHI-003 |
| 506 | 2026-08-20T18:36:45+00:00 | `197786ee51ff` | CHI-004 spec: dlcr_alpha Field Dynamics blend is a dead-return-field no-op |
| 507 | 2026-08-20T18:56:37+00:00 | `02623ad6fea1` | CHI-003-02: dual-signal areas_working alongside areas_final in TFP batch KME |
| 508 | 2026-08-20T20:50:06+00:00 | `a75bc5b97b65` | CHI-004-01: surface family_hits_288 so Field Dynamics DLCR blend can activate |
| 509 | 2026-08-20T21:04:23+00:00 | `b782e24d0027` | Chiron: candidate registry — tiered master list beyond the closed 60 |
| 510 | 2026-08-21T05:49:45+00:00 | `31250d9b5a92` | Chiron: CHI-005 — B8 TRIZ relation weights reviewed, held at defaults |
| 511 | 2026-08-21T05:58:38+00:00 | `bd03aa2dc551` | Chiron: CHI-006 - B6 diagnostic thresholds traced unwired, not tunable |
| 512 | 2026-08-21T06:11:03+00:00 | `5c6dc4c56757` | Chiron: CHI-007 - B2 propagation weights reviewed, held; synergy-lane finding |
| 513 | 2026-08-21T06:17:49+00:00 | `570820919f28` | Chiron: CHI-008 - B5 obstacle-score weights reviewed, held; CI claim corrected |
| 514 | 2026-08-21T06:27:36+00:00 | `332dfd68087d` | Chiron: CHI-009 - B3 fusion/traversal physics reviewed, held |
| 515 | 2026-08-21T06:30:35+00:00 | `b2e66345cc8a` | Chiron: CHI-010 - B4 governance penalties reviewed, held |
| 516 | 2026-08-21T06:50:14+00:00 | `bd0540aada73` | Chiron: CHI-011 - B7 FGR/Freshness calibration reviewed, split finding |
| 517 | 2026-08-21T07:19:52+00:00 | `a901769d0195` | Chiron: CHI-012 - B1 activation floor disconnected from real gate; Tier B sweep closed |
| 518 | 2026-08-21T07:35:44+00:00 | `b29aab4fbb9b` | CHI-B16: wire B1 activation SoT; retire B6 diagnostics pack |
| 519 | 2026-08-21T07:57:51+00:00 | `1127b7e64e25` | Chiron: CHI-013 - Tier C reachability verified across all 6 packs |
| 520 | 2026-08-21T08:46:58+00:00 | `136905c24f44` | Registry: lock inventory 92/39/13/4 post CHI-B16 and CHI-013 |
| 521 | 2026-08-21T08:48:25+00:00 | `caccb7546a34` | Registry: Tier D is a hard stop, not a next move |
| 522 | 2026-08-21T08:49:07+00:00 | `2954577cbf23` | Chiron: add STATUS-SNAPSHOT-2026-08-21 - full 148-constant status list |
| 523 | 2026-08-21T08:49:40+00:00 | `177196b27a08` | Merge remote-tracking branch 'origin/main' |
| 524 | 2026-08-21T09:02:36+00:00 | `8d4e71d8e4cf` | CHI-014-02: remove unread hex_field_reference from profiles_v1 |
| 525 | 2026-08-21T10:14:03+00:00 | `a5d53dac4c5f` | TFP-POLES-01: full A1-A12 outcome surfaces + pole_cascade audit + RU name lock |
| 526 | 2026-08-21T10:33:12+00:00 | `2e616adba75c` | Chiron: STATUS-SNAPSHOT - detail retired reasons + rejected-options table |
| 527 | 2026-08-21T11:32:37+00:00 | `12155690ba06` | CHI-015: gated TFP Class B Field Dynamics consumer -- 34 params accommodated |
| 528 | 2026-08-21T11:36:04+00:00 | `38e846d34dcb` | Chiron: registry + snapshot honesty pass - CHI-015 accommodated, not operational |
| 529 | 2026-08-21T15:46:49+00:00 | `593da5679eda` | CHI-016 first-class return + TFP-POLES-01/03 + CHIRON-126 address map |
| 530 | 2026-08-31T09:47:10+00:00 | `8d3f1332faf4` | Chiron: recover syzif book/author corpus (121 books), reconstruct repair_text.py |
| 531 | 2026-08-31T09:52:54+00:00 | `04284f547ad7` | Chiron: syzif corpus - drop #2 (Adam Smith), Rumelt moves 121->2 |
| 532 | 2026-08-31T09:59:26+00:00 | `ef89c8d49a3d` | Chiron: mark syzif corpus canonical source for default/core taxonomy |
| 533 | 2026-08-31T10:02:34+00:00 | `97ac76c5eb58` | Chiron: note default-core Stage 2 (syzif corpus wiring) in backlog |
| 534 | 2026-08-31T11:09:33+00:00 | `0ff6d4c3eac4` | Chiron: syzif corpus second-pass grind — ligature joins, cid leaks, running headers, page numbers |
| 535 | 2026-08-31T11:12:00+00:00 | `fc38bcbef54b` | Chiron: notes on syzif grind pass + open OCR word-error item, ahead of second-pass inspection |
| 536 | 2026-08-31T11:29:23+00:00 | `0d276e24411c` | Chiron: OCR word-error auto-fix tried and rejected — report-only tool kept, nothing applied |
| 537 | 2026-08-31T16:48:43+00:00 | `8db1d00d4434` | Chiron: fix silent write-skip bug in clean_corpus_artifacts.py, add soft-hyphen join |
| 538 | 2026-08-31T17:43:40+00:00 | `84b4c21f196f` | Chiron: apply LLM short-token OCR word-fixes (24,887), sentence-context judgment |
| 539 | 2026-08-31T18:00:49+00:00 | `f6b77efdb520` | Chiron: apply long-run OCR fixes (3,079), redesigned prompt + two safety nets |
| 540 | 2026-08-31T18:02:07+00:00 | `f94ad77020c4` | Chiron: notes on the closed OCR word-error pass, corpus floor as of 4280864/11815b9 successor |
| 541 | 2026-08-31T18:33:08+00:00 | `f43aff8f8716` | Chiron: redo long-run OCR fixes with fixed alignment check + reinforced prompt (3,139 more) |
| 542 | 2026-08-31T18:34:15+00:00 | `771a04316e2e` | Chiron: notes on the long-run reclaim pass and hallucination-leak fix |
| 543 | 2026-08-31T18:48:47+00:00 | `4b1b834d8364` | Chiron: self-contained task brief for Cursor — syzif corpus residual cleanup |
| 544 | 2026-08-31T20:55:29+00:00 | `36e02ee6f1b9` | IDE residual OCR wording on syzif corpus (no new scripts). |
| 545 | 2026-08-31T21:05:57+00:00 | `315e78831dec` | Finish outside-MB short-token syzif residuals. |
| 546 | 2026-08-31T21:26:54+00:00 | `fe4d493bdc0f` | Chiron: flag 85 Moral Boundaries unreliable, rename, exclude from corpus-clean claims |
| 547 | 2026-08-31T21:34:54+00:00 | `dc2a6e1901cc` | Chiron: day-close summary — honest state + the mirror-sync orphan bug found tonight |
| 548 | 2026-09-01T12:33:31+03:00 | `3c4b343a5321` | 123 |
| 549 | 2026-09-01T12:38:24+00:00 | `47a03b4e3589` | chore(corpus): relocate syzif (120-book default/core corpus) to hesperia/modules/default/corpus/syzif |
### Atomic-Commits-Team/hesperia (391 commits)

| # | ISO datetime | SHA | Subject |
|---:|---|---|---|
| 1 | 2026-02-09T22:03:51Z | `26f33c97030d` | Initial commit |
| 2 | 2026-02-09T22:15:58Z | `72bf6ece3195` | first commit |
| 3 | 2026-02-09T22:21:53Z | `a05a08234c08` | 123 |
| 4 | 2026-02-09T22:33:44Z | `7f41a93178a5` | 3 |
| 5 | 2026-02-10T13:02:58Z | `176a556b5967` | 3 |
| 6 | 2026-02-18T13:24:56Z | `9a3b770f46a9` | Replace with CLIENTS/hesperia from cursor repo (canonical source) |
| 7 | 2026-02-18T16:48:02Z | `fdba4e732096` | Add governance (waterline, tasks, schema), project/, scripts/ — full Hesperia team and today's work |
| 8 | 2026-02-18T17:29:21Z | `8162bf7a7b68` | Add MIT license and concepts doc |
| 9 | 2026-02-18T17:34:05Z | `11de49e20416` | Add Codex context assessment (2026-02-18) |
| 10 | 2026-02-19T15:22:27Z | `50b29338c7af` | 3 |
| 11 | 2026-02-19T15:46:30Z | `7481e4356940` | Add files via upload |
| 12 | 2026-02-19T15:48:24Z | `411309514bfa` | 3 |
| 13 | 2026-02-20T06:41:48Z | `e9224bfe9106` | Add ΣΓΘ guard layer spec and issue-001 closure docs |
| 14 | 2026-02-20T06:42:24Z | `217e8a74b585` | Merge pull request #2 from Atomic-Commits-Team/codex/add-new-guard-layer-features-and-documentation |
| 15 | 2026-02-20T07:05:46Z | `496e67a5ef3e` | Add comprehensive documentation for v0.2 release |
| 16 | 2026-02-20T07:27:49Z | `13dc9358d7ce` | Initialize guards module |
| 17 | 2026-02-20T07:40:00Z | `c0a91c3a9bec` | Create Hesperia v0.2 Release Invoker script |
| 18 | 2026-02-20T07:51:04Z | `18624acc51f4` | Add unit tests for guards: sigma_guard, gamma_guard, and theta_guard |
| 19 | 2026-02-20T07:53:14Z | `047f19d95115` | Release notes for Hesperia v0.2 |
| 20 | 2026-02-20T08:03:27Z | `eea358ac57f6` | Merge pull request #5 from Atomic-Commits-Team/v0.2 |
| 21 | 2026-02-20T08:28:24Z | `d7a05dfc3b1e` | Add Hesperia-mapped software engineering tutorial plan |
| 22 | 2026-02-20T08:29:13Z | `aa5ee68ffdd3` | Merge pull request #6 from Atomic-Commits-Team/codex/create-detailed-.md-file-for-project-plan |
| 23 | 2026-02-20T08:43:07Z | `dcebd8f86f6b` | docs: expand HESPERIA software engineering tutorial plan |
| 24 | 2026-02-20T08:43:27Z | `d2286b2e143d` | Merge pull request #7 from Atomic-Commits-Team/codex/create-software-engineering-plan-document |
| 25 | 2026-02-20T09:37:17Z | `5df386dff278` | Add files via upload |
| 26 | 2026-02-20T09:44:27Z | `d333580f1a68` | Polish Romanian diacritics and clean text artifacts in tutorial |
| 27 | 2026-02-20T09:44:51Z | `4764eecb2636` | Merge pull request #8 from Atomic-Commits-Team/codex/check-romanian-diacritics-and-text-artifacts |
| 28 | 2026-02-20T10:05:37Z | `83a1df20a91f` | Revizuire ediție HESPERIA cu corecturi și detalii noi |
| 29 | 2026-02-20T10:12:43Z | `bbdcd588c5a2` | Refine tutorial TXT layout for improved readability |
| 30 | 2026-02-20T10:12:54Z | `cbc539b6facd` | Merge pull request #9 from Atomic-Commits-Team/codex/adjust-text-file-structure-for-readability |
| 31 | 2026-02-20T17:47:31Z | `cbbadcc5b517` | Wire Sigma/Gamma/Theta guards into runtime flow |
| 32 | 2026-02-20T17:48:13Z | `7c781d50a604` | 0.2.0.1 wired up  |
| 33 | 2026-02-20T18:13:31Z | `9e869989ec2b` | Reorganize root Python guards into scripts package |
| 34 | 2026-02-20T18:13:47Z | `c8bc88a45fff` | Merge pull request #11 from Atomic-Commits-Team/codex/organize-python-files-and-rename-elements |
| 35 | 2026-02-20T18:15:46Z | `529bd4315e78` | Add files via upload |
| 36 | 2026-02-20T18:16:54Z | `50fcae20aac2` | Delete v0.2 directory |
| 37 | 2026-02-20T22:23:12Z | `e4233167353c` | API: /hesperia/analyze, /health, /privacy; minimal JSON response; logging; CORS/OPTIONS; deploy + systemd |
| 38 | 2026-02-20T22:28:16Z | `91f3962c7690` | Harden OpenAI Actions API responses and CORS behavior |
| 39 | 2026-02-20T22:29:03Z | `6f1f1d95dcf5` | Merge pull request #12 from Atomic-Commits-Team/codex/debug-openai-gpt-aegle-script |
| 40 | 2026-02-22T12:16:57Z | `51d4181a35bc` | Add files via upload |
| 41 | 2026-02-22T12:28:56Z | `faec1f9927c2` | Add v0.2.1 semantic stability documentation set |
| 42 | 2026-02-22T12:29:07Z | `4890dd50d8a4` | Merge pull request #13 from Atomic-Commits-Team/codex/implement-repository-hygiene-and-versioning-updates |
| 43 | 2026-02-22T12:37:53Z | `178652948ef3` | Update 19_SPEC__Semantic_Stability_Control_v1_0.txt |
| 44 | 2026-02-22T12:45:39Z | `959e4c520e54` | Add files via upload |
| 45 | 2026-02-22T12:47:00Z | `47f59fbc161f` | Rename SPEC_18__Indexing_and_Coordinates_v1_0.txt to 18_SPEC__Indexing_and_Coordinates_v1_0.txt |
| 46 | 2026-02-22T12:59:24Z | `b8d1f80c8951` | Expand VARIABLES.md to include spec and academic variable glossary |
| 47 | 2026-02-22T13:00:26Z | `c2f993ca74ce` | Merge pull request #14 from Atomic-Commits-Team/codex/create-variables.md |
| 48 | 2026-02-22T13:23:43Z | `351178c608ba` | consolidation (Gena): canonical refs, workspace, DOC_INDEX, fix double extension |
| 49 | 2026-02-22T13:47:22Z | `ffc5371c27a5` | Full overwrite from cursor brain: present state (no books). Specs, sphere_rag (shadow_layer v1.0), docs, releases v0.2.1 |
| 50 | 2026-02-23T07:00:12Z | `b6a8b5f222d7` | Add files via upload |
| 51 | 2026-02-23T07:22:29Z | `87c435815e01` | Add files via upload |
| 52 | 2026-02-23T07:32:35Z | `6879a68f279e` | Add files via upload |
| 53 | 2026-02-23T09:44:25Z | `edeedd42c993` | v0.4.1 runnable: Dict B build, pre-test, full sphere_rag |
| 54 | 2026-02-23T09:47:13Z | `d08631cf1588` | Sync from cursor: specs 22,25-27, README, release notes, docs, guard_config, hesperia_lex (scripts+curated), assets A/B |
| 55 | 2026-02-23T10:03:57Z | `c9fda7450592` | Add v0.4.1 structural audit report against v0.3.3 baseline |
| 56 | 2026-02-23T10:04:24Z | `60ee226eea86` | Merge pull request #15 from Atomic-Commits-Team/codex/perform-structural-audit-of-hesperia |
| 57 | 2026-02-23T20:50:53Z | `93b5292f6cd2` | Dict A v0.4.1 deprecated (v0.4.1.1 default); v0.4.1.2 canonical families.yaml + builder + validator |
| 58 | 2026-02-23T21:01:57Z | `a8e444d6dd61` | Add v0.4.1.3 semantic family canonicalization pipeline |
| 59 | 2026-02-23T21:02:14Z | `20bf4374efd3` | Merge pull request #16 from Atomic-Commits-Team/codex/rewrite-families.yaml-for-semantic-canonicalization |
| 60 | 2026-02-23T22:33:42Z | `dd0d107febb1` | v0.4.1.4 Dict B: formalize B0 fallback and scaffold hard-gated B1 |
| 61 | 2026-02-23T22:34:00Z | `37e0f6f1185c` | Merge pull request #17 from Atomic-Commits-Team/codex/finalize-b0-token-fallback-and-add-b1-scaffolding |
| 62 | 2026-02-23T22:59:02Z | `5fc762e6cfae` | Add deterministic v040 embedding build env and runner |
| 63 | 2026-02-23T22:59:19Z | `9a672785f67d` | Merge pull request #18 from Atomic-Commits-Team/codex/unblock-v0.4.0-embedding-build |
| 64 | 2026-02-23T23:14:16Z | `d68bab579013` | Harden v0.4.0 build outputs with deterministic hashing and provenance |
| 65 | 2026-02-23T23:14:29Z | `fcf778bf57ef` | Merge pull request #19 from Atomic-Commits-Team/codex/implement-deterministic-json-output-and-checksum-gate |
| 66 | 2026-02-23T23:22:12Z | `4901aaded49a` | Gate v0.4.0 surface build with model pinning and canonical checks |
| 67 | 2026-02-23T23:22:33Z | `b51ef88849d8` | Merge pull request #20 from Atomic-Commits-Team/codex/finalize-surface-artifact-for-dict-b |
| 68 | 2026-02-23T23:48:08Z | `d3fccae2b5fd` | Canonical surface: fix freeze file format; repeatability venv-agnostic |
| 69 | 2026-02-24T00:12:00Z | `19d28a40a2ef` | Hesperia: Dict B B1 freeze, canonical procedures, topology truth, coverage |
| 70 | 2026-02-24T00:26:21Z | `70dc4dd1db3b` | Add HESPERIA AI status and milestones technical report |
| 71 | 2026-02-24T00:26:36Z | `065c2eb9349d` | Merge pull request #21 from Atomic-Commits-Team/codex/create-technical-report-on-hesperia-project |
| 72 | 2026-02-24T11:56:42Z | `dcbb38b1dcc7` | v0.4.0: first full L1–L9 stack, release notes, layer_runs, RELEASE_NOTES__v0_4 |
| 73 | 2026-02-24T12:18:46Z | `052e194cbcc6` | Add v0.4 MVP assessment narrative report |
| 74 | 2026-02-24T12:18:57Z | `01f8c4898cee` | Merge pull request #22 from Atomic-Commits-Team/codex/create-narrative-report-on-v0.4-hesperia-mvp-status |
| 75 | 2026-02-26T22:17:55Z | `61ead07f090a` | Team 10 adoption: single repo, deliverables to Atomic-Commits-Team/hesperia. OPERATIONAL.md, TEAM10-PROJECT.md, .gitigno |
| 76 | 2026-02-26T22:20:02Z | `9d293787aea4` | Operational report: push succeeded, large-file note, single variant. |
| 77 | 2026-02-26T22:25:40Z | `1fe3802875ca` | End of day: nuke summary, sync note, single variant. |
| 78 | 2026-02-27T08:15:12Z | `d79d79713984` | L1 Normative Structure Profile Extension (34_SPEC N1) + Taxonomy v1.0 |
| 79 | 2026-02-27T11:28:03Z | `d52498e8e020` | R1-R4 pipeline, e2e sentence script, dict_b/surface wiring, docs and governance |
| 80 | 2026-02-27T13:18:24Z | `e6a871fe89f9` | R1-R4/E2E: token-offset segmentation, unit fixes, spec notes |
| 81 | 2026-02-28T22:44:56Z | `6d5cb52da958` | ORDER: repo-wide naming (4 words + version), artifacts in subfolders, specs at root |
| 82 | 2026-02-28T22:48:23Z | `7765737d5745` | ORDER: document mrt remote (hesperia_mrt fork repo) |
| 83 | 2026-03-07T17:32:44Z | `a36433493367` | docs: add naming consistency audit and expand variables index |
| 84 | 2026-03-07T17:33:02Z | `8c720dfebae0` | Merge pull request #23 from Atomic-Commits-Team/codex/check-repository-terminology-consistency |
| 85 | 2026-03-11T08:27:07Z | `934a3f984446` | Consolidate v0.4 baseline boot path and fix attribution tests |
| 86 | 2026-03-11T08:29:18Z | `1ddbb4b17b1f` | Merge pull request #24 from Atomic-Commits-Team/codex/consolidate-poc-repo-into-canonical-baseline |
| 87 | 2026-03-11T10:51:49Z | `05fc6faf9739` | 3 |
| 88 | 2026-03-11T15:15:39Z | `6b385b2f66a8` | 3 |
| 89 | 2026-03-11T19:29:08Z | `0897549ff767` | Dossier system, batch runner, content-addressed artifacts, and pipeline refactor |
| 90 | 2026-03-12T10:02:37Z | `dcb4695a79bb` | Add sphere layer stack: topology, dynamism, logic, metrics, USF, pipeline, guards |
| 91 | 2026-03-12T11:09:36Z | `802efcf98099` | Add testing framework, interface layer, structural geometry, diagnostics |
| 92 | 2026-03-12T11:54:31Z | `c6bcb11b4b97` | v0.5: strip versioning, structural attribution, e2e all, deprecations, README rewrite |
| 93 | 2026-03-12T17:16:56Z | `63febce162eb` | Layer-10 interpretation, USF consolidation, Prolog L9b, multi-step propagation, fingerprint drift |
| 94 | 2026-03-12T18:20:32Z | `c6bcf14c222b` | RAD: legal notice repo-wide, architecture fingerprint, boundaries, layer deps, .gitignore pytest cache |
| 95 | 2026-03-12T18:20:55Z | `c1361131db36` | docs: add Git tag and SHA to ARCHITECTURE_FINGERPRINT proof |
| 96 | 2026-03-12T18:24:09Z | `e23749e380ed` | docs: evidence chain in ARCHITECTURE_FINGERPRINT (document→commit→tag), optional OpenTimestamps note |
| 97 | 2026-03-12T18:25:50Z | `b1e0feac4e1f` | docs: OpenTimestamps proof for HESPERIA_SYSTEM_SPEC_v1.md (.ots), update fingerprint |
| 98 | 2026-03-12T18:34:26Z | `d3aab9a4d9d7` | docs: README capabilities and use sections, push sync |
| 99 | 2026-03-13T18:31:30Z | `4d0314e4a0a6` | KME domain pipeline: Tasks 1-6 + E2E integration |
| 100 | 2026-03-14T18:23:12Z | `5eef4a61bb1b` | quarantine: move docs/architecture and docs/boot to legacy/docs_archive |
| 101 | 2026-03-14T18:30:53Z | `8e137b81a0b9` | Sealed runtime: release gate, CLI/API shipping, backup, governance and cleanup |
| 102 | 2026-03-14T18:41:51Z | `5f64eef60f7b` | Sealing scan: restrict to public surface only; document legacy observation window |
| 103 | 2026-03-14T19:15:04Z | `a1c82762c37c` | Remove legacy/ after sealed runtime gate PASS; add manifest-only build target |
| 104 | 2026-03-14T19:25:20Z | `9a3a24c0787f` | Add push_mirrors.sh and mirror setup docs; document lifecycle and protection layers |
| 105 | 2026-03-14T19:43:14Z | `d17ba52f55df` | Cleanup: archive specs history, remove duplicate A_CORE_STAR_MAP, add CLEANUP_PLAN |
| 106 | 2026-03-14T19:47:13Z | `e1fd3eae211b` | Clean repo root: move guard and layer config out of root |
| 107 | 2026-03-14T19:47:41Z | `22302ccdea8f` | Docs: note Phase 2b root cleanup in CLEANUP_PLAN |
| 108 | 2026-03-14T20:04:35Z | `8e7dfe6004c0` | fix: e2e sealing + move analysis_service to runtime for layer boundary |
| 109 | 2026-03-14T20:05:21Z | `9e2e0ca67517` | chore: add .dockerignore and release artifacts (checksums, manifest, schema_sha256) |
| 110 | 2026-03-14T20:12:33Z | `80453a32cf0c` | docs: from-scratch memo in README + RUN/BUILD/DEPLOY from scratch guides |
| 111 | 2026-03-14T20:25:50Z | `7722d013b4f0` | docs: 10+2 topology decision — 10 operational, 2 reserved service areas |
| 112 | 2026-03-15T15:34:51Z | `e5eed2b672c7` | Remark: testing_tfp phase |
| 113 | 2026-03-15T21:08:07Z | `4bb8a5c7ea6e` | TFP testing stack: speaker-aware, transference, temporal, operational analytics, normalization, negation, n-grams, calib |
| 114 | 2026-03-18T09:48:01Z | `04936737c919` | TRIZ engine, KME integration, e2e consolidation (9 stages), product/eval/deploy |
| 115 | 2026-03-18T10:58:15Z | `2435be03b6fc` | docs: Hesperia knowledge base — repo map, dependency graph, variable catalog, product lines/stack |
| 116 | 2026-03-18T16:24:39Z | `6e3f4e154c4b` | E2E: commit canonical artifacts + calibration batch; track e2e outputs in repo |
| 117 | 2026-03-18T16:26:27Z | `0e740022bb12` | Add field_dynamics engine (phase1-4, state, triz_signal, xi_proxy, e2e_bridge) + tests |
| 118 | 2026-03-18T16:27:27Z | `0d20594ac0d3` | Docs sync: system awareness, dynamics/calibration specs, governance, triage, research; AGENTS/README; calibration assets |
| 119 | 2026-03-18T16:30:18Z | `586acec2a5b0` | docs: EoD repo-wide snapshot 2026-03-18 |
| 120 | 2026-03-18T17:23:26Z | `af41d9e88234` | feat: semantic field stack — equations, HCI calibration, ontology matrices, E2E |
| 121 | 2026-03-19T08:33:06Z | `c6d59b50ca15` | release: Hesperia Engine Dynamics v0.5.0 seal sync |
| 122 | 2026-03-19T08:42:09Z | `0ba8b734af9a` | fix(release): snapshot git dirty before writing release/v0.5.0 artifacts |
| 123 | 2026-03-19T08:47:11Z | `d4671bd4bdad` | release(v0.5.0): sealed audit artifacts (full pytest, 2026-03-19T12:00:00Z) |
| 124 | 2026-03-19T08:54:20Z | `b999798aaa34` | fix(ci): sealing scan — word-boundary 3D, skip v0.5.0 audit + triz_demo |
| 125 | 2026-03-19T13:39:11Z | `531d6ff29eaa` | feat(engine): Tasks 1–11 integration — P_CH, energy, calibration, topology, physics validation, system seal, full E2E st |
| 126 | 2026-03-19T15:25:32Z | `342f3f00467e` | release: Hesperia Engine Dynamics v0.5.1 (enforcement baseline) |
| 127 | 2026-03-19T15:31:25Z | `f53569eef780` | release: v0.5.1 sealed audit bundle (final_gate sealed=true) |
| 128 | 2026-03-19T15:43:06Z | `f4e33d79c42d` | fix(ci): install pytest for sealed-runtime-gate integrity step |
| 129 | 2026-03-19T17:17:05Z | `4759cf7809d3` | hardening(release): seal-coupled v0.5.1 version lock + portable bundle |
| 130 | 2026-03-19T17:27:45Z | `cfc30a9b0b0e` | hardening(release): build_release_bundle matches temp-copy spec |
| 131 | 2026-03-19T17:37:21Z | `a1c1355baad9` | release: add bundle integrity + determinism guard |
| 132 | 2026-03-20T15:43:39Z | `151dfa38647f` | feat(tfp): RU v060 corpus, DLCR stack, dynamics wiring; drop session transcripts |
| 133 | 2026-03-21T16:20:24Z | `51db2352bbbc` | sync: TFP calibration pack + OpenAI tooling |
| 134 | 2026-03-22T10:19:16Z | `ea591d7694a1` | OpenAI calibration: stderr progress, smoke check, batch runners |
| 135 | 2026-03-22T10:20:51Z | `364101e220d2` | chore: ignore and untrack research/_noone_local (local-only corpus) |
| 136 | 2026-03-22T10:22:30Z | `f0eb1f9c6476` | TFP calibration: engine, pipeline, schemas, tools, tests, small JSON data |
| 137 | 2026-03-22T10:25:43Z | `94277a7db3d0` | docs: refresh IMPORT_GRAPH v0.5.0 (runtime + engine) |
| 138 | 2026-03-22T10:30:25Z | `7eb524a2beb0` | chore: bump DEAD_WEIGHT RECORDED_COUNT to 67 (import BFS drift) |
| 139 | 2026-03-26T06:23:57Z | `6e60b6b61110` | Ethan ML-07: neutral product docstring for analyze_session_speaker_aware (mainline, no TFP). |
| 140 | 2026-03-26T06:25:33Z | `e6b9a228d6ce` | Ethan task H (H_total): mainline-pin h_total_concepts.json; add semantic_dynamics_operator_spec.md. |
| 141 | 2026-03-26T08:50:02Z | `e1217ab65d00` | release: finalize v0.5.2 technical terminology propagation |
| 142 | 2026-03-26T08:50:55Z | `296581f37553` | release: seal v0.5.2 technical audit bundle |
| 143 | 2026-03-26T11:40:02Z | `5cf99055251c` | release: seal v0.5.3 modular tfp onboard |
| 144 | 2026-03-26T13:06:20Z | `23f589aef2ce` | feat: complete modular kernel workflow gates T1-T10 |
| 145 | 2026-03-26T15:26:55Z | `ab1905ddc1ac` | release: seal v0.5.4 deterministic modular pipeline system |
| 146 | 2026-03-26T17:04:44Z | `9f5547882702` | feat(product): deliver T11-T20 productization workflow slice |
| 147 | 2026-03-26T18:16:04Z | `ac872661facc` | feat(engine): wire versioned calibration dict loader |
| 148 | 2026-03-26T18:19:27Z | `4479c5897638` | release: promote system to v0.5.5 |
| 149 | 2026-03-27T17:48:23Z | `f52fd57ec687` | feat(cd): Concept Dictionary v1 Phase 1 — executor, asset, pipeline hook (opt-in) |
| 150 | 2026-03-27T20:47:44Z | `25f220e53a43` | HC-WAVE1: control layer MVP — schemas, docs, hesperia_control module, tests (HC-01..HC-10). |
| 151 | 2026-03-27T21:03:29Z | `4ae0cd4c73b6` | Add TFP module data mirror (README, sync script, docs) |
| 152 | 2026-03-27T21:10:55Z | `a142a8827c55` | Dict calibration: default 4 workers, offline bundle, skip API key in mock |
| 153 | 2026-03-27T21:12:20Z | `0082666f0db6` | docs(dict_calibration): Dict A API phase closed; do not re-run LLM stages unless intentional |
| 154 | 2026-03-27T21:16:17Z | `1f0b677b3d02` | Add B+CD verification wave after green A (script + doc) |
| 155 | 2026-03-27T21:19:21Z | `dbafd41a8844` | governance(Ethan): lock B-before-CD after green A (working + MODEL_CARD) |
| 156 | 2026-03-27T21:20:55Z | `6ab6a05d1460` | docs(Ethan): 10 tasks to finish dicts and calibrate/check |
| 157 | 2026-03-27T21:25:16Z | `294d0ee0d8ed` | docs(Ethan): dict/calibration framework rev.2 (H/S/V/Y + control laws) |
| 158 | 2026-03-27T21:30:30Z | `c76aa0822fa3` | governance(Ethan): seal v0_6_0_clr_v052_1 dict A/norm/propose/anchor tree |
| 159 | 2026-03-27T21:39:15Z | `bd85cbee489f` | dict/CD: Phase 2 co_occurs soft math, release gates script |
| 160 | 2026-03-27T21:50:51Z | `2e1043d38f76` | docs: point E2E and entry commands at runtime.pipeline (not execution_flow) |
| 161 | 2026-03-27T21:57:12Z | `cc9c49ae064b` | GAP-WIRE-01: expand env_guard allowlist; RUNTIME_ENV_VARS tiers; regen script |
| 162 | 2026-03-27T21:58:47Z | `6c2893f0ab5c` | GAP-WIRE-02: document shipping vs dev API; T17 /product/*; OpenAPI bearer for /product/ |
| 163 | 2026-03-27T21:59:35Z | `043b3fe67086` | GAP-WIRE-03: README quick start hesperia.run + dict gate runbooks |
| 164 | 2026-03-27T22:00:40Z | `b668eebc162e` | GAP-WIRE-04: validate_version_consistency in sealed-runtime-gate; policy doc |
| 165 | 2026-03-27T22:01:08Z | `4b8691558953` | GAP-WIRE-05: document CI pytest subset vs full tests/ in SHIPPING_PATH_POLICY |
| 166 | 2026-03-27T22:02:23Z | `dcc16366b533` | GAP-WIRE-06/07: metric registry partial-coverage waiver; tools shell index |
| 167 | 2026-03-28T15:49:08Z | `033d57d4c391` | calibration: v0_6_0_clr_v052_2 B-gap closure (DICT-CAL-02), TFP cluster hex anchors |
| 168 | 2026-03-28T16:11:51Z | `94af72d9f437` | TFP-GATE-A0/A1: determinism env, VERSION calibration pin, wave artifact checks |
| 169 | 2026-03-28T16:14:52Z | `4f7ec60fbab3` | TFP-GATE: phase C smoke script, mirror checksum verify, governance docs (B1/B2/A2A3/METRICS/INV/UNMAPPED/CD-DELTA), test |
| 170 | 2026-03-28T16:26:32Z | `a2078889a1fd` | TFP-ENF-01..05: behavioral pytest (dominance, co_occurs, saturation, modifiers), CD delta bounds, unmapped fixture gate, |
| 171 | 2026-03-28T16:36:31Z | `8e2e57522cc0` | TFP-REL-01..05: lexical unmapped token rate API, real corpus test, pipeline CD area delta, per_text_non_empty_ratio, lat |
| 172 | 2026-03-28T16:47:58Z | `e25be822060a` | TFP-TIGHT-01..05: unmapped cap 0.65 + real dict corpus, relative CD delta bound, semantic stability test, min per-text a |
| 173 | 2026-03-28T17:03:21Z | `63cda5905056` | TFP module v1: governance, seal hook, gold tests, CI path gate |
| 174 | 2026-03-28T17:12:28Z | `aee3cbc069e0` | TFP-DATA-T01: Ethan charter — module tfp_v1 SSoT, research evicted for dict ops |
| 175 | 2026-03-28T17:14:10Z | `dc0effea3c9d` | TFP-DATA-T02: research/_noone_local inventory JSON + index + regen tool |
| 176 | 2026-03-28T17:14:43Z | `4fe89c7be464` | TFP-DATA-T03: TFP_V1_LAYOUT.md + data README pointer |
| 177 | 2026-03-28T17:27:19Z | `ff73864fe591` | TFP-DATA-T04–T20: tfp_v1 module data tree, migration, sync, CI gates |
| 178 | 2026-03-28T17:28:13Z | `1730dc56877f` | TFP-DATA-T20: mark active.md closure item done in checklist |
| 179 | 2026-03-28T17:33:12Z | `30daa9b78560` | TFP-DATA-T07: mirror dict_calibration provenance into tfp_v1 runs + manifest |
| 180 | 2026-03-28T17:44:50Z | `35a56db45c50` | Move clinical session corpus to tfp_v1/corpus/sessions (migrate + ingest paths) |
| 181 | 2026-03-28T18:07:44Z | `990f7992e167` | E2E TFP smoke uses primary text; hesperia.tfp shim; NLP session_topology wrappers |
| 182 | 2026-03-28T18:27:59Z | `3c34695f7d10` | R1-R4: tokenize_with_spans fixes RU clinical R1 partition (punct-stripped tokens) |
| 183 | 2026-03-28T18:36:45Z | `01042303d847` | Add apocalyptic archive triage doc + workflows mirror script |
| 184 | 2026-03-28T18:39:41Z | `36dcaa572853` | docs(governance): Ethan flash recovery bundle + workflows must-carry (no server) |
| 185 | 2026-03-28T18:47:08Z | `5e4d02f243e1` | tools: mirror cursor brain into /data/hesperia + data root README template |
| 186 | 2026-03-29T19:41:11Z | `7c5aa5fb4366` | docs(reference): Upcelerator2026 Assignment-1 motivation, vision, mission |
| 187 | 2026-03-29T19:41:11Z | `5eb1d339c52d` | docs(reference): add Upcelerator2026 README index (Dreamups Phase 1 N.2) |
| 188 | 2026-03-29T19:41:12Z | `63983e1095fe` | docs(reference): Upcelerator2026 working assets (generators, templates, notes) |
| 189 | 2026-03-29T19:41:12Z | `333b00e70dd8` | docs(reference): Upcelerator2026 BMC and pitch deck (2A, 2D) |
| 190 | 2026-03-29T19:41:12Z | `d65a720249e1` | docs(reference): Upcelerator2026 competitor analysis (2C) |
| 191 | 2026-03-29T19:41:12Z | `50fb60d679f3` | docs(reference): Upcelerator2026 market definition, sizing, PESTLE (2B) |
| 192 | 2026-03-29T19:41:27Z | `dcc4fd9f7828` | docs(tools): document Upcelerator2026 path in data root template |
| 193 | 2026-03-29T19:41:27Z | `22a20d2d19f4` | test: add calibration dict loader and TFP module main run tests |
| 194 | 2026-03-29T19:41:27Z | `bec423580f68` | chore(governance): add cursor session mode artifact |
| 195 | 2026-03-30T10:16:58Z | `d26987cea6c8` | HPROM-R4: hprom_report_metrics and v6 REPORT eval (force-add ignored reports path). |
| 196 | 2026-03-30T10:31:02Z | `0352a6282eb5` | STABILIZE v052_4: sealed calibration dir, stabilize script, hprom_04 tri-version REPORT. |
| 197 | 2026-03-30T10:40:44Z | `93855686f012` | tools: extended RU natural corpus + REPORT runner for v052_4 validation (no dict edits) |
| 198 | 2026-03-30T10:42:47Z | `2a23ff83e2cf` | artifacts: dict field value and status counts snapshot + summarize tool |
| 199 | 2026-03-30T10:45:19Z | `4d59aa33bbc1` | tools: print dict_states snapshot JSON to stdout; --quiet for file-only |
| 200 | 2026-03-30T10:49:30Z | `3b67968a7e7a` | lexical: text language heuristic + dict_c language layer analysis (Grace C-layer) |
| 201 | 2026-03-30T10:53:33Z | `5b52a09eee4b` | calibration: v052_5 dict_c language retag (ru/en/mixed) + tools and REPORT artifacts |
| 202 | 2026-03-30T11:04:34Z | `e54bb4213197` | fixtures: extended RU natural corpus v2 (Wikipedia batch) + fetch tool + language layer artifact |
| 203 | 2026-03-30T11:33:16Z | `47a6babd9e50` | fixtures: session 11.09.2023 plain text for DLCR REPORT baseline |
| 204 | 2026-04-07T06:36:52Z | `a5a17fbf6bcf` | output_views: iteration_segment_openai_v1 schema, segment package, Kernberg prompts, tests (Gena OUT-VIEW-01/02) |
| 205 | 2026-04-07T06:39:57Z | `f14e6a6c9f8f` | output_views: Session Inspector MVP route, panes, deep links, T54/T55 docs (Gena OUT-VIEW-03) |
| 206 | 2026-04-07T06:43:09Z | `fbb1e7e50b4a` | output_views: segment export.json, copy UI, optional OpenAI proxy, rate limit doc, make target (Gena OUT-VIEW-04) |
| 207 | 2026-04-07T06:45:45Z | `22664d45d211` | output_views: PII export dialog, safety/license/flags/rollback docs (OUT-VIEW-05 Daniel epic) |
| 208 | 2026-04-07T07:10:28Z | `8af5ab7c747e` | output_views: T02 build session_inspector_v1 from TFP pipeline dir (OUT-VIEW-FULL-01) |
| 209 | 2026-04-07T07:13:13Z | `dc333b0ab7c5` | output_views: generate_inspector_fixture + Makefile; FULL-02 pipeline fixture docs |
| 210 | 2026-04-07T07:15:48Z | `dfc54ed72d4c` | output_views: FULL-03 Pane C audit planes + relations strip; tests |
| 211 | 2026-04-14T12:19:47Z | `e29cb70d572c` | v0.5.8 task1: couple contradiction pressure into tfp area inhibition |
| 212 | 2026-04-14T12:22:51Z | `20f42a5b0235` | fix(nlp): speaker label regex flags for Python 3.12 (import-safe hesperia.nlp) |
| 213 | 2026-04-14T12:27:49Z | `32038085f30f` | v0.5.8 task2: wire contradictions from pipeline into tfp activation |
| 214 | 2026-04-14T12:32:53Z | `5ddf364b168a` | v0.5.8 task3: couple contradictions into topology segment dynamics |
| 215 | 2026-04-14T12:38:59Z | `6448bc70a1a6` | v0.5.8 task4: propagate contradiction package across dlcr multiscale and product |
| 216 | 2026-04-14T12:44:34Z | `1327948fe29d` | v0.5.8 task5: couple contradiction with lexical and concept uncertainty |
| 217 | 2026-04-14T12:52:22Z | `5465444600e6` | v0.5.8 task6: couple contradiction with negation and inhibition logic |
| 218 | 2026-04-14T13:00:05Z | `084d08046fa2` | v0.5.8 task7: couple contradiction with family-level structure |
| 219 | 2026-04-14T13:08:22Z | `1dedcc7e5e6b` | v0.5.8 task8: feed contradiction patterns into lexical and concept calibration diagnostics |
| 220 | 2026-04-14T13:13:20Z | `888bbcc8ecd1` | v0.5.8 task9: add contradiction integrity release gating and promotion verdicts |
| 221 | 2026-04-14T13:22:43Z | `904cf944d0cb` | v0.5.8 task10: formalize contradiction spec and artifact contract |
| 222 | 2026-04-14T13:55:15Z | `b87ca97680de` | v0.5.8 task11: centralize contradiction calibration surface and profile |
| 223 | 2026-04-14T14:08:28Z | `13e5ef8534b9` | docs+tools: v0.5.8 seal register (tasks 1-11), bundle --contradiction-calibration-json |
| 224 | 2026-04-14T14:08:36Z | `562134599bad` | Merge branch 'ed-0.5.8-task11-contradiction-calibration-surface': Hesperia v0.5.8 contradiction track (tasks 1-11) seale |
| 225 | 2026-04-14T14:28:16Z | `e135bc6d153f` | shipping: fix sealing scan surface for v0.5.2 audit bundle |
| 226 | 2026-04-14T14:47:48Z | `2342898dcfa2` | docs: regenerate IMPORT_GRAPH for contradiction pipeline imports (v0.5.8 drift) |
| 227 | 2026-04-14T14:56:59Z | `c84dff919642` | fix(tfp): satisfy noone path literal gate (docs, handoff, paths) |
| 228 | 2026-04-14T15:00:08Z | `557a01237f23` | fix(tfp): track tfp_v1 dict_a/runtime and dict_b skeleton for CI layout test |
| 229 | 2026-04-14T15:15:34Z | `dcec99f9aa00` | docs: rebaseline dead-weight budget for v0.5.8 module growth (91 unreferenced) |
| 230 | 2026-04-14T15:25:39Z | `cbc1253f57e4` | refactor(engine): move module ALIASES to engine; fix core/modules boundary |
| 231 | 2026-04-14T15:30:27Z | `2c84f16c67ef` | docs: regenerate IMPORT_GRAPH_ENGINE after module_aliases split |
| 232 | 2026-04-14T15:34:06Z | `f3a77463772f` | tools: skip RAW dict_a corpus check in CI when gitignored asset absent |
| 233 | 2026-04-14T15:41:38Z | `ed42d3c4e972` | test: expect contradiction_package on run_sealed_multiscale_stack signature |
| 234 | 2026-04-14T16:01:09Z | `551fe81a75cd` | test(fixtures): commit CI TFP bundle manifest calibration + 09_session_topology for release gate |
| 235 | 2026-04-14T18:02:03Z | `1d5061dded14` | docs(tfp): single bundle output folder rule (TFP_VALUES_LIST §0) |
| 236 | 2026-04-14T18:07:47Z | `b0a8a9cc9bc8` | chore(outputs): standardize TFP dirs under outputs/tfp/ + default paths |
| 237 | 2026-04-14T18:31:01Z | `f46479eafa2f` | test(tfp): track operator narrative fixture tests/fixtures/tfp/input.txt |
| 238 | 2026-04-15T15:54:28Z | `6d9b83042b10` | feat(output_views): Vite hex matrix viewer + build script for browser deploy |
| 239 | 2026-04-15T16:28:16Z | `9f89613d40ea` | feat(hex_matrix_viewer): semantic layout, isolated render modes, coherence, schema |
| 240 | 2026-04-15T17:01:37Z | `abda11ec0cd6` | feat(hex_matrix_viewer): 12x24 F(s,b) lattice + flat/cylinder/sphere projections |
| 241 | 2026-04-15T17:17:11Z | `8905a3034e97` | feat(hex_matrix_viewer): unified project(s,b,mode); spheroid + pole merge toggle |
| 242 | 2026-04-15T17:25:19Z | `9894c8e04dcd` | feat(hex_matrix_viewer): diamond inspection layout (288 cells, band-centered) |
| 243 | 2026-04-20T10:28:30Z | `35d388e453d8` | 123 |
| 244 | 2026-05-11T08:40:55Z | `85e5d7f1222a` | feat(api): TFP-CHROMA-04 — /inspector/tfp-corpus/compose endpoint (spec §6) |
| 245 | 2026-05-11T08:45:32Z | `965b9e003bc0` | feat(hex-matrix): TMX-10 — RelationsPanel + appear/disappear side panel |
| 246 | 2026-05-11T08:49:04Z | `0e3b7971432f` | docs(specs): TMX-11 — T3 supervisor prompt pack + diff slots |
| 247 | 2026-05-11T08:50:20Z | `d69df05689ab` | feat(i18n): TMX-14 — RU UX copy for matrix labels, T1-T3 tiers, tooltips |
| 248 | 2026-05-11T08:52:03Z | `29fdb829fbd6` | test(hex-matrix): TMX-15 — gold fixture + snapshot tests + D3 smoke |
| 249 | 2026-05-11T08:53:17Z | `8d090f1b28e3` | docs(chroma): TMX-16+17 — reference_literature ingest path + timeline layer query contract |
| 250 | 2026-05-11T08:57:27Z | `0cec2ff6a0f9` | docs(tmx): TMX-18..24 — PII review, operator runbook, QA checklist, a11y, integration, design, closure |
| 251 | 2026-05-18T18:18:05Z | `dca9675975c3` | Restore Django output_views skeleton and deploy docs after cherry-pick. |
| 252 | 2026-05-18T18:18:33Z | `2a69bcb38fab` | Add prichindel systemd unit and restore full hesperia nginx vhost. |
| 253 | 2026-05-18T19:51:33Z | `f7324eede8a9` | merge: origin/main into prod main (keep OUT-VIEW + TMX; align +9 -60) |
| 254 | 2026-05-18T19:54:33Z | `2aa1d43cb0e2` | prod(prichindel): deploy pins for Session Inspector + site root |
| 255 | 2026-05-18T19:59:59Z | `ff55ef46810b` | draw-line(2026-05-18): rollback marker — README + ROLLBACK-LINE doc |
| 256 | 2026-05-18T20:12:25Z | `b13d7f221857` | chore(prod): minimal README pointer to dev repo |
| 257 | 2026-05-18T20:12:25Z | `830e79e16737` | chore(prod): remove specs narrative markdown |
| 258 | 2026-05-18T20:12:25Z | `137806d19273` | chore(prod): remove release narrative markdown |
| 259 | 2026-05-18T20:12:25Z | `dedc2987eb14` | chore(prod): remove governance/ narrative |
| 260 | 2026-05-18T20:12:25Z | `ce5818d0c92d` | chore(prod): remove root team and planning markdown |
| 261 | 2026-05-18T20:12:25Z | `3b31604fa22e` | chore(prod): remove docs/ (documentation on igareosh/hesperia) |
| 262 | 2026-05-18T20:16:41Z | `d3260f910c6e` | ci(prod): prod-code-only workflow and verifier script |
| 263 | 2026-05-18T20:16:50Z | `594411f4a6d4` | chore(prod): gitignore and untrack outputs markdown |
| 264 | 2026-05-18T20:16:50Z | `c8f563399d16` | chore(prod): remove runtime and tools narrative markdown |
| 265 | 2026-05-18T20:16:50Z | `326c69697d97` | chore(prod): remove research/ (reference corpus on igareosh/hesperia) |
| 266 | 2026-05-18T20:17:03Z | `e93c6f550e02` | fix(prod): restore research Python; strip reference markdown to dev repo |
| 267 | 2026-05-18T20:17:11Z | `627d461d9a44` | ci(prod): allow research Python; forbid research markdown only |
| 268 | 2026-05-18T21:34:14Z | `00f099088c34` | chore(prod): remove legacy/ and specs/ (dev documentation on igareosh/hesperia) |
| 269 | 2026-05-18T21:34:15Z | `f80cc87ed92a` | chore(prod): remove examples, release, assets narrative md (not corpus/dicts) |
| 270 | 2026-05-18T21:34:15Z | `12f07f956e04` | chore(prod): remove module and output_views dev markdown (corpus untouched) |
| 271 | 2026-05-18T21:34:50Z | `fa6f01ebcf28` | fix(prod): restore specs yaml/json config; strip specs markdown only (corpus untouched) |
| 272 | 2026-05-18T21:34:54Z | `276ea704f3ef` | ci(prod): verifier corpus-safe — dev md/specs prose only |
| 273 | 2026-05-18T21:35:05Z | `12f931a706bb` | ci(prod): corpus-safe verifier (specs yaml allowed) |
| 274 | 2026-05-18T21:35:05Z | `d7a88d172341` | chore(prod): remove dict/tools dev README (corpus yaml/json untouched) |
| 275 | 2026-05-18T21:37:51Z | `8cfb4841bcc7` | chore(prod): immaculate sweep — dev notes removed (backup on igareosh/hesperia) |
| 276 | 2026-05-18T21:40:56Z | `56f5ac823335` | draw-line(2026-05-18): dev-ready — immaculate prod, docs on igareosh/hesperia |
| 277 | 2026-05-18T21:41:08Z | `18178deb63c9` | ci(prod): allow DEV-READY-LINE marker on immaculate tree |
| 278 | 2026-05-18T22:47:37Z | `235ea30dd7c5` | fix(prod): gunicorn, security settings, sessions view, nginx hardening |
| 279 | 2026-05-18T22:49:28Z | `77810ff9ef1c` | fix(prod): sync hesperia-api.service to match deployed config |
| 280 | 2026-05-18T23:04:28Z | `41e051369a6f` | chore(v0.6.0): Python compliance pass — version bump, API cleanup |
| 281 | 2026-05-18T23:28:32Z | `d4f4f67b4b00` | chore: checked by Felix (Claude Code) 2026-05-20 — python compliance v0.6.0 sealed, prod repo |
| 282 | 2026-05-21T06:55:52Z | `2e712184fccc` | feat(output_views): inspector nav link to hex-matrix viewer (TMX-22) |
| 283 | 2026-05-21T07:08:19Z | `d313bfddc63c` | fix(output_views): STATIC_URL /static/ and require collectstatic for WhiteNoise |
| 284 | 2026-05-27T19:15:30Z | `9848c16fbab4` | docs(brand): Hesperia logo canonical visual description v1 and v1.2 |
| 285 | 2026-05-27T20:13:29Z | `297e40873b0e` | Grace: ingest Hesperia logo image drop from operator cache. |
| 286 | 2026-05-28T11:34:47Z | `e196fce0488b` | fix: validate prod tree from shipping context |
| 287 | 2026-05-28T11:34:47Z | `257d81eee446` | fix: align release version authority with v0.6.0 |
| 288 | 2026-05-28T11:44:24Z | `fa923eee0cfe` | release: add sealed v0.6.0 baseline package |
| 289 | 2026-05-28T12:08:50Z | `fc7c5cf71df1` | build: add checked docker bundle for v0.6.0 |
| 290 | 2026-05-28T12:14:22Z | `c9e95570789f` | release: add 0.6.0 agentic install contract |
| 291 | 2026-05-28T13:33:06Z | `6a13eb12bb7c` | release: publish atomic 0.6.0 on tag push |
| 292 | 2026-05-28T13:34:58Z | `676dd1c9c899` | ci: trigger atomic 0.6.0 release publish on branch push |
| 293 | 2026-05-28T13:37:39Z | `7311d600b46f` | Merge pull request #26 from Atomic-Commits-Team/hesperia-v0.6.0-release |
| 294 | 2026-05-28T13:40:31Z | `a06c8289c7e5` | release: refine atomic 0.6.0 release notes |
| 295 | 2026-05-28T13:48:07Z | `87f5a5b62aea` | release: sanitize 0.6.0 public release artifacts |
| 296 | 2026-05-28T13:48:07Z | `f695936ffa49` | release: sanitize 0.6.0 public release artifacts |
| 297 | 2026-05-28T14:07:19Z | `536323fe63c4` | ci: drop dict payload gates from sealed runtime release repo |
| 298 | 2026-05-28T14:07:19Z | `ee78240a1458` | ci: drop dict payload gates from sealed runtime release repo |
| 299 | 2026-05-28T14:17:41Z | `482c2525def4` | ci: drop docs-dependent gates from prod sealed runtime workflow |
| 300 | 2026-05-28T14:21:11Z | `47c91cac8fe2` | ci: trigger sealed runtime gate on sanitized main |
| 301 | 2026-05-28T14:23:47Z | `46f63cf589a7` | ci: add workflow_dispatch to sealed runtime gate |
| 302 | 2026-05-28T14:37:08Z | `d06f6744f55f` | ci: sealed runtime gate on push to main only (not PR reruns) |
| 303 | 2026-05-28T14:40:47Z | `6df2695e0682` | fix(tfp): restore tfp_v1/nlp skeleton dir for layout gate (TFP-DATA-T15) |
| 304 | 2026-05-28T14:45:23Z | `3de9974fa1d0` | Merge pull request #27 from Atomic-Commits-Team/hesperia-v0.6.0-release |
| 305 | 2026-06-14T10:31:18Z | `f87b2bb1eaef` | HES-61-01: Python /analyze engine_result contract envelope. |
| 306 | 2026-06-14T10:47:57Z | `cc94b09d4b81` | Default OpenAI model gpt-4o-mini (env-driven, not gpt-5.2). |
| 307 | 2026-06-14T13:01:41Z | `16286faaf04c` | Ethan: seal Hesperia 0.6.3 GitHub archive — E2E without prod dicts/corpus. |
| 308 | 2026-06-14T13:31:39Z | `9bf0289da52b` | Ethan: 0.6.3 archive example outputs (envelope, Teacher, IRC trace, analyze). |
| 309 | 2026-06-14T13:59:44Z | `122d45bfeb6d` | merge: reconcile 0.6.1 analyze line (cc94b09) with 0.6.3 archive seal (16286fa) |
| 310 | 2026-06-14T14:05:02Z | `e9eaa0764db6` | Add runtime/irc_teacher/ — 0.6.3 IRC Teacher path in product repo. |
| 311 | 2026-06-14T20:02:55Z | `b37a67629bfd` | docs(dev): brain-export wave2 Hesperia from cursor (2026-06-14T2002Z) |
| 312 | 2026-06-14T20:07:54Z | `6f86a9620a6b` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 313 | 2026-06-14T20:09:34Z | `bb276954592d` | docs(dev): archive operational/assignments brain tree (2026-06-14) |
| 314 | 2026-06-14T20:11:44Z | `988eb336cabd` | docs(dev): archive brain scripts tree (2026-06-14) |
| 315 | 2026-06-14T20:16:43Z | `11bce88a5868` | docs(dev): final Hesperia brain sweep (2026-06-14) |
| 316 | 2026-06-14T20:16:52Z | `bc920b411ef2` | docs(dev): final Hesperia brain sweep (2026-06-14) |
| 317 | 2026-06-14T22:04:24Z | `bd151586ca36` | docs(dev): brain-export wave2 Hesperia from cursor (2026-06-14T2204Z) |
| 318 | 2026-06-14T22:04:42Z | `0c8c78cf51f1` | docs(dev): final Hesperia brain sweep (2026-06-14) |
| 319 | 2026-06-14T22:04:47Z | `4ad33a59cbcd` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 320 | 2026-06-20T13:17:06Z | `81fcae344f8a` | docs(colombo): modular core, scoped modules, and branch architecture |
| 321 | 2026-06-20T13:32:53Z | `0fa762213843` | docs(colombo): Class A cored vs Class B non-cored modules |
| 322 | 2026-06-20T13:32:59Z | `3b9001c15858` | docs(colombo): fix dev-export path references in architecture §8 |
| 323 | 2026-06-20T13:35:23Z | `df77d59d920d` | docs(colombo): pointer to mandatory-read policy for dev agents |
| 324 | 2026-06-28T12:59:48Z | `e36d6a560500` | Add HSR-V7 router envelope schema and fingerprint v0.1. |
| 325 | 2026-06-29T11:55:31Z | `bd869e2d8b15` | HSR-V7: full router implementation — pre-LLM compiler, post-LLM audit, governance modes, /product/interpret |
| 326 | 2026-06-29T12:15:41Z | `99e17a4b65bd` | FPF-V7-13: fpf-thinking-map governed OpenAI calibration calls. |
| 327 | 2026-06-29T12:19:43Z | `c0f76a672a06` | HSR-V7-08/11: corpus policy mirror + router gold test matrix. |
| 328 | 2026-06-29T12:28:53Z | `85c407a51bbf` | docs: HSR-V7 version bump plan 0.6.3→0.6.5→0.7.0 (A-08) |
| 329 | 2026-06-29T12:36:47Z | `5a094b63fb01` | docs: Gate B Gena classifications B-08/13/14 |
| 330 | 2026-06-29T12:47:03Z | `322ee0110f0c` | HSR-V7 Gate C: Class A drain verified, observability wired, fusion confirmed |
| 331 | 2026-06-29T12:53:36Z | `30b632aaedaf` | HSR-V7-C-21: VERSION.yaml 0.6.5 fusion milestone |
| 332 | 2026-06-29T14:45:07Z | `7ffb606a20da` | HSR-V7 Gate C/D: schema validation, gold fixtures, API decision tests. |
| 333 | 2026-06-29T14:48:08Z | `31d487210928` | HSR-V7 Gate E: product copy, API docs, operator surface labels. |
| 334 | 2026-06-29T14:53:23Z | `7f7c8d2e6018` | COBALT MVP adapter: CHROMA-2 retrieve, flag off, hooks. |
| 335 | 2026-06-29T15:19:41Z | `b66b35cbe3e4` | COBALT G2 attribution tool, chromadb 1.5 fix, gold test. |
| 336 | 2026-06-29T15:20:51Z | `06bf3346a778` | H070 sandbox apply: update_edge_weight gate chain G1-G9. |
| 337 | 2026-06-29T15:59:29Z | `e9cc40677812` | H070 pre-SEAL: Inspector Pane 2, replay, gold tests, ledger. |
| 338 | 2026-06-29T16:15:32Z | `7af214c360e9` | docs(dev): brain-link manifest (pointers only, no brain ingest) |
| 339 | 2026-06-30T22:11:47Z | `63a2295b3924` | docs/foundations: Phase 2 exhaustive scientific documentation (L1–L11, all corners, eras, parameters) |
| 340 | 2026-07-01T11:09:55Z | `9e22af322add` | docs: ISO-grade LTS documentation program + restored per-layer specs |
| 341 | 2026-07-04T14:59:23Z | `6596c6cf515a` | sync: METRIC wave v0.7.0 (anchor_map/GCS registry, 24_SPEC, ISO doc index) |
| 342 | 2026-07-04T14:59:44Z | `df96723c2e5b` | sync: fpf_bridge Layer 11 baseline (v7.0 + this session's v7.2 Phase 1-4/v7.3 code) |
| 343 | 2026-07-04T15:00:05Z | `707737b95e30` | feat: fpf_bridge v7.2/v7.3/v7.4 specs + agentic Cursor interface + COBALT scale-up prep |
| 344 | 2026-07-04T15:07:53Z | `3b283a1eb5b4` | docs: repo-wide consistency pass for fpf_bridge v7.2-v7.4 + new AGENTS.md |
| 345 | 2026-07-04T15:14:31Z | `eec627aceb32` | docs: era 8 file, output_catalog §12 evidence-surface update, ISO cross-ref |
| 346 | 2026-07-04T15:19:34Z | `b811319b9106` | docs(iso): re-verify all built rows against era 8, per the matrix's own LTS rule |
| 347 | 2026-07-04T15:23:31Z | `4efaf87bf600` | docs: verify and record that core/ was never touched across the entire era 8 wave |
| 348 | 2026-07-04T15:49:10Z | `a8fdd9809dda` | docs: tighten Hesperia agentic orientation |
| 349 | 2026-07-04T15:51:21Z | `48c3421e0faf` | docs: propagate Hesperia naming discipline |
| 350 | 2026-07-04T15:56:10Z | `a9ae78fd8045` | docs: add Hesperia parameter rationale map |
| 351 | 2026-07-04T16:02:35Z | `e594da61f395` | docs: add Upcelerator productization QA |
| 352 | 2026-07-04T16:03:46Z | `4d053f4c3c08` | docs: spread Upcelerator product wording |
| 353 | 2026-07-04T16:08:53Z | `6d536ed97673` | docs: connect product wording to evidence surfaces |
| 354 | 2026-07-04T16:14:04Z | `d074600a43b3` | docs: ingest Upcelerator market and competition baseline |
| 355 | 2026-07-04T16:20:42Z | `b24bc5981e8c` | docs: expose productization routes in indexes |
| 356 | 2026-07-04T17:04:13Z | `d23c5fbc46bd` | docs: add Aurel stabilization rules for productization |
| 357 | 2026-07-06T06:41:54Z | `aec32febaf7e` | hesperia: align version authority and calibration packs |
| 358 | 2026-07-06T06:42:00Z | `3de85145d93f` | docs: consolidate HSR-V7 source of truth |
| 359 | 2026-07-06T06:43:15Z | `403590d25fb8` | merge origin/main before HSR-V7 consolidation push |
| 360 | 2026-07-06T06:44:47Z | `5778de194eb2` | hesperia: mirror merged version metadata |
| 361 | 2026-07-06T06:51:42Z | `0fb1f17a15be` | docs: apply ISO-grade rename and archive consolidation |
| 362 | 2026-07-06T07:14:27Z | `f216ab220cf2` | refactor: fuse core domain and runtime canon |
| 363 | 2026-07-06T07:26:20Z | `b6452aa52709` | refactor: converge canonical core imports |
| 364 | 2026-07-06T07:31:29Z | `67f9e6680273` | docs: converge source truth after core fusion |
| 365 | 2026-07-06T07:51:57Z | `dbadc2017d2f` | hesperia: remove obsolete core-expulsion shims |
| 366 | 2026-07-06T08:08:14Z | `4cea408c400f` | hesperia: converge core output wiring |
| 367 | 2026-07-19T11:56:10Z | `b3b0c44b4fcf` | fix(shipping): route load_context_packet_json through service facade |
| 368 | 2026-07-19T11:56:25Z | `31e70088c3b6` | fix(sealing-scan): close 13-day CI red on Sealed runtime gate |
| 369 | 2026-07-19T11:56:29Z | `be7eea2aa377` | docs(iso): correct stale corners/*.md count in traceability matrix |
| 370 | 2026-07-19T12:22:04Z | `f39265703488` | feat(gtp): GTP-01/02 — six-side logical+semantic operator registry + schema |
| 371 | 2026-07-19T12:22:11Z | `3aeb2cea1cd0` | feat(gtp): GTP-03 — hex_rotation calibration + per-side match score |
| 372 | 2026-07-19T12:22:19Z | `e49fbdaece7c` | feat(gtp): GTP-04 — PointZeroDelta broadcast + CoherenceField Psi |
| 373 | 2026-07-19T12:22:27Z | `eb3488b7be6e` | feat(gtp): GTP-05 — GTPA next-hex selection over legal neighbors |
| 374 | 2026-07-19T12:22:34Z | `9f794044235f` | feat(gtp): GTP-06 — ThoughtImprint + path-discovery pipeline + package exports |
| 375 | 2026-07-19T12:22:41Z | `9da62413bfca` | feat(gtp): GTP-07 — wire gtp block into RouterInputEnvelope, flag-gated |
| 376 | 2026-07-19T12:22:46Z | `3e1603973ff9` | test(gtp): GTP-08 — deterministic gold matrix |
| 377 | 2026-07-19T12:22:53Z | `0e1389ddf25c` | docs(specs): promote 23_SPEC GTP formalization with implementation status |
| 378 | 2026-07-19T12:32:27Z | `f035a0b41da7` | docs(specs): GTP invocation guide + forward-direction note |
| 379 | 2026-07-19T12:44:31Z | `67a60a34832c` | docs(specs): resolve §0.3 forward-direction tension, cross-link Ethan draft |
| 380 | 2026-07-19T13:14:14Z | `737e19e8dad9` | docs: Ethan ratify fpf_bridge v7.2/v7.3/v7.4 (Hesperia day run) |
| 381 | 2026-07-19T13:41:29Z | `58377cc20054` | feat(router): FPF-HSR-13 — mandatory logical/weight/source_activation blocks |
| 382 | 2026-07-19T13:41:40Z | `f87723260dda` | feat(api): FPF-HSR-11 — InterpretBody.context_packet on /product/interpret |
| 383 | 2026-07-19T13:41:49Z | `fa24630a48a7` | feat(cli): FPF-HSR-12 support — thinking_map_outcome extraction in router-inquire |
| 384 | 2026-07-19T13:49:49Z | `3b2653b10ed2` | feat(fpf_inspect): FPF-BUII bottom-up GapReport dig endoscope |
| 385 | 2026-07-19T14:22:41Z | `ae39bcc4a822` | Ship pre-0.7 HAND wire: pin 1.5.0, Option B, ops map, GapReport flag, gold harness. |
| 386 | 2026-07-25T19:26:36Z | `f76297325c59` | chore(pin): align fpf-thinking-map to 1.9.2 (ATM2-43) |
| 387 | 2026-07-25T19:34:34Z | `d5b5c650f9a7` | docs(wiki): export Colombo Hesperia parameter wiki to brain-export |
| 388 | 2026-07-25T19:43:52Z | `ddc7a6ca10b0` | fix(fpf): align FPF_PIN_EXPECTED to 1.9.2 for pre-seal wiring |
| 389 | 2026-07-25T22:13:58Z | `fc7a761386b8` | fix(e2e): correct field_dynamics_enabled import source in run_e2e_all |
| 390 | 2026-07-25T22:45:11Z | `0fcbe8993603` | release: seal Hesperia system_version 0.7.0 |
| 391 | 2026-07-26T11:20:07Z | `4ed89c6d044d` | docs: acknowledge copyright transfer; abandon cluster use |
### Consolidare-Continuum/hesperia (31 commits)

| # | ISO datetime | SHA | Subject |
|---:|---|---|---|
| 1 | 2026-07-26T11:01:18+00:00 | `cc59e4c39bf8` | 0 — Corporate inception of Hesperia under CONSOLIDARE CONTINUUM S.R.L. |
| 2 | 2026-07-26T11:01:24+00:00 | `d89057b21c1f` | seal: Hesperia corporate inception under CONSOLIDARE CONTINUUM S.R.L. |
| 3 | 2026-07-31T01:49:40+00:00 | `496f5892206e` | promote: dev session sync — genesis taxonomy, core/module severance, math graduation, copyright correction |
| 4 | 2026-07-31T04:00:33+00:00 | `b8baa0b9eab2` | test: fix two regressions surfaced by the core severance / v06 retirement |
| 5 | 2026-07-31T12:48:54+00:00 | `436021838baa` | sync: Atomic ed5a2ff9 tree onto CC corporate-inception root (no VERSION invent) |
| 6 | 2026-08-04T05:58:08+00:00 | `5f1b27695352` | sync: Atomic f003066a tree onto CC corporate-inception root (no VERSION invent) |
| 7 | 2026-08-04T06:17:18+00:00 | `c83f0d5a91f3` | sync: Atomic 898abc23 tree onto CC corporate-inception root (no VERSION invent) |
| 8 | 2026-08-04T07:21:18+00:00 | `c708320d0dfe` | sync: Atomic cb9657fd tree onto CC corporate-inception root (no VERSION invent) |
| 9 | 2026-08-04T08:45:17+00:00 | `136c8599d13f` | sync: Atomic a1940da0 tree onto CC corporate-inception root (no VERSION invent) |
| 10 | 2026-08-04T16:41:04+00:00 | `19d75066bc7a` | sync: Atomic 1d89c146 tree onto CC corporate-inception root (no VERSION invent) |
| 11 | 2026-08-05T09:48:02+00:00 | `38a055652c09` | sync: Atomic 81c26053 tree onto CC corporate-inception root (no VERSION invent) |
| 12 | 2026-08-10T09:40:49+00:00 | `473a3bbea10f` | sync: Atomic b4adcae6 tree onto CC corporate-inception root (no VERSION invent) |
| 13 | 2026-08-10T10:24:01+00:00 | `7231187d97c4` | sync: Atomic 4e9b2961 tree onto CC corporate-inception root (no VERSION invent) |
| 14 | 2026-08-10T15:45:27+00:00 | `893a1219b584` | Ignore local openai_api_key.txt in CC hesperia clone. |
| 15 | 2026-08-10T15:47:11+00:00 | `d9cc8d8a4fd0` | Add openai_api_key.txt at repo root for durable CC custody. |
| 16 | 2026-08-31T09:58:41+00:00 | `9a35e9914d49` | sync: Atomic 04284f54 tree onto CC corporate-inception root (no VERSION invent) |
| 17 | 2026-08-31T09:59:48+00:00 | `f60745aaead4` | sync: Atomic ef89c8d4 tree onto CC corporate-inception root (no VERSION invent) |
| 18 | 2026-08-31T11:10:58+00:00 | `6f11f13af10b` | sync: Atomic 0ff6d4c3 tree onto CC corporate-inception root (no VERSION invent) |
| 19 | 2026-08-31T11:12:26+00:00 | `ad437e7d20a8` | sync: Atomic fc38bcbe tree onto CC corporate-inception root (no VERSION invent) |
| 20 | 2026-08-31T11:29:48+00:00 | `d0041698d584` | sync: Atomic 0d276e24 tree onto CC corporate-inception root (no VERSION invent) |
| 21 | 2026-08-31T16:49:11+00:00 | `1fb144d0b069` | sync: Atomic 8db1d00d tree onto CC corporate-inception root (no VERSION invent) |
| 22 | 2026-08-31T17:44:22+00:00 | `42808644913b` | sync: Atomic 84b4c21f tree onto CC corporate-inception root (no VERSION invent) |
| 23 | 2026-08-31T18:01:25+00:00 | `11815b955b95` | sync: Atomic f6b77efd tree onto CC corporate-inception root (no VERSION invent) |
| 24 | 2026-08-31T18:02:32+00:00 | `4e8caf3e86a4` | sync: Atomic f94ad770 tree onto CC corporate-inception root (no VERSION invent) |
| 25 | 2026-08-31T18:33:42+00:00 | `51d25bd9a5d2` | sync: Atomic f43aff8f tree onto CC corporate-inception root (no VERSION invent) |
| 26 | 2026-08-31T18:34:42+00:00 | `18fb7ffe117c` | sync: Atomic 771a0431 tree onto CC corporate-inception root (no VERSION invent) |
| 27 | 2026-08-31T18:49:12+00:00 | `3f9d96db71f8` | sync: Atomic 4b1b834d tree onto CC corporate-inception root (no VERSION invent) |
| 28 | 2026-08-31T21:27:32+00:00 | `5d9149fef428` | sync: Atomic fe4d493b tree onto CC corporate-inception root (no VERSION invent) |
| 29 | 2026-08-31T21:35:18+00:00 | `5b3a3221d4c3` | sync: Atomic dc2a6e19 tree onto CC corporate-inception root (no VERSION invent) |
| 30 | 2026-09-01T12:53:53+00:00 | `47eff2d4cd97` | sync: Atomic 47a03b4e tree onto CC corporate-inception root (no VERSION invent) |
| 31 | 2026-09-01T19:58:44+00:00 | `560ac2c2f4ca` | docs(corporate): file RAD OpenTimestamps crypto proof chain |

## Verify (spot-check)

```bash
git -C /path/to/igareosh-hesperia log -1 --format='%H %aI %s'
wc -l 0*-*.tsv
sha256sum *.tsv *.md
```

SIGNED: Cursor | Hesperia three-repo commit provenance chain | 2026-09-01 | second proof pack
