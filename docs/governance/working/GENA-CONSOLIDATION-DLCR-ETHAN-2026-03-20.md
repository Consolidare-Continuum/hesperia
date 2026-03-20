<!--
Gena — consolidation pass after Ethan + DLCR integration spike (2026-03-20).
-->

# Gena — DLCR / Ethan consolidation & integration check (2026-03-20)

**Status:** CLOSED (2026-03-20) — Gena consolidation pass complete (validators default paths, trace-tool docs, `.gitignore`, import graphs regenerated, full matrix green).  
**Does not replace:** sealed v0.5.1 product decisions; Tier-1 changes still need explicit review.

---

## 1. Paste invocation (for Gena agent)

```
You are Gena on Hesperia repo. Run a CONSOLIDATION PASS on the DLCR + Ethan integration
landed 2026-03-20 (see docs/governance/working/GENA-CONSOLIDATION-DLCR-ETHAN-2026-03-20.md).

1) Inspect git state: both tracked changes and untracked files. Separate:
   - Integration spine: core/{lexical,resolver,hexmap,sequence}, hesperia/engine/lexical_concept,
     hesperia/engine/projection/dlcr_public.py, hesperia/engine/multiscale_product_bridge.py,
     hesperia/extensions/dynamics/e2e_bridge.py (+ related dynamics/xi/triz if touched),
     runtime/{pipeline,services,api}, schemas/lexical_concept, specs/canon/lexical_concept,
     assets/data/engine_dynamics_v060/, tools/check_dlcr_regression.py, tools/dump_dlcr_trace.py,
     tools/validate_dict_*.py, tools/gen_dlcr_pack_from_dict_b.py, tests/lexical_concept,
     tests/test_*semantic*, tests/test_marker_concept_trace_effective.py,
     tests/experimental/clinical_tfp/test_dlcr_benchmark_sessions.py,
     docs/governance/working/ETHAN-*.md, CONTRIBUTING.md, E2E docs, capabilities, CANONICAL_INDEX.
   - Unrelated bulk moves (e.g. research/_noone_local): note but do not “fix” unless broken links.

2) Run the command block in §4 below; fix any failures. If a failure is intentional env-gated behavior,
   document it in this file under §6 “Notes”.

3) Deduplicate / align tooling (e.g. if both tools/dlcr_trace_report.py and tools/dump_dlcr_trace.py
   overlap, pick one public entry + redirect doc).

4) Confirm CI: .github/workflows/sealed-runtime-gate.yml still calls check_dlcr_regression and
   does not double-count slow jobs.

5) Regenerate or diff docs where repo policy requires (IMPORT_GRAPH*, public API snapshot) if your
   edits touch those surfaces.

6) Output: short “Gena consolidation report” (bullet list: OK / fixed / deferred) appended to §6
   or as a sibling REPORT-*.md — and set Status to CLOSED in this file when done.
```

---

## 2. Scope summary (technical)

| Area | Intent |
|------|--------|
| **Lexical / DLCR** | `core/lexical`, `core/resolver`, `core/hexmap`, `core/sequence`, `hesperia/engine/lexical_concept`, `schemas/lexical_concept`, `specs/canon/lexical_concept` |
| **Runtime** | `analysis_service` DLCR merge, `run_e2e_all` optional artifacts, `analyze` `lexical_evidence_dlcr`, API `internal/dlcr_trace` |
| **Multiscale / sealed** | `multiscale_product_bridge` text prep + diagnostics; `e2e_bridge` concept guard + trace `effective_landing_source`; `sealed_multiscale_stack` if DLCR sidecar touched |
| **Dynamics / Ξ** | `xi_proxy`, `triz_signal`, field dynamics tests — ensure env defaults unchanged |
| **Assets** | `assets/data/engine_dynamics_v060/*`, `assets/version_registry.yaml` |
| **Governance / E2E docs** | `ETHAN-*`, `E2E_RUN_ORDER`, `E2E_OUTPUTS`, `CURSOR_OPEN_WORKFLOW` |

---

## 3. Get the diff (commands)

**Full tree (may include large research renames):**
```bash
git status -sb
git diff --stat HEAD
```

**Integration-focused diff (paths only):**
```bash
git diff HEAD -- \
  core/ hesperia/engine/lexical_concept hesperia/engine/projection/dlcr_public.py \
  hesperia/engine/multiscale_product_bridge.py hesperia/engine/sealed_multiscale_stack.py \
  hesperia/extensions/dynamics hesperia/system/capabilities.py hesperia/system/capabilities.yaml \
  runtime/pipeline runtime/services runtime/api schemas/lexical_concept specs/canon/lexical_concept \
  specs/CANONICAL_INDEX.md assets/version_registry.yaml assets/artifacts/e2e \
  docs/E2E_RUN_ORDER.md docs/CURSOR_OPEN_WORKFLOW.md CONTRIBUTING.md \
  tests/lexical_concept tests/test_e2e_flows.py tests/test_attribution.py \
  tests/test_semantic_evidence_guard.py tests/test_marker_concept_trace_effective.py \
  tests/test_field_dynamics_xi_proxy.py tests/experimental/clinical_tfp \
  tools/check_dlcr_regression.py tools/dump_dlcr_trace.py tools/validate_dict_a.py \
  tools/validate_dict_b_dlcr.py tools/gen_dlcr_pack_from_dict_b.py \
  .github/workflows/sealed-runtime-gate.yml
```

**Untracked / new files (must be staged or .gitignore’d intentionally):**
```bash
git status -u --short | head -80
```

---

## 4. Mandatory validation matrix (run in order)

```bash
python3 tools/check_forbidden_zone_imports.py
python3 tools/check_dlcr_regression.py
python3 tools/validate_dict_a.py
python3 tools/validate_dict_b_dlcr.py
pytest tests/lexical_concept/ -q
pytest tests/test_attribution.py tests/test_semantic_evidence_guard.py tests/test_marker_concept_trace_effective.py -q
pytest tests/test_runtime_spine_integrity.py -q
pytest tests/test_e2e_flows.py::test_e2e_capability_matrix_wires_blocks -q
python3 -c "from pathlib import Path; from hesperia.system import system_seal; import hesperia.system.system_seal as ss; r=Path('.').resolve(); print(ss._check_concept_layer(r))"
```

Optional heavier:
```bash
HESPERIA_FIELD_DYNAMICS=1 HESPERIA_FIELD_DYNAMICS_TRIZ=0 HESPERIA_E2E_CALIBRATION_BATCH_N=5 \
  pytest tests/test_e2e_flows.py::test_e2e_run_e2e_all_produces_all_artifacts -q
```

Drift tools (if policy says run on touched trees):
```bash
python3 tools/validate_shipping_surface.py
python3 tools/gen_import_graph_doc.py | diff -q docs/IMPORT_GRAPH_v0_5_0.md -
```

---

## 5. Consolidation checklist (Gena)

- [x] No duplicate/conflicting DLCR CLI tools; README/runbook points to one canonical trace dump.
- [x] `HESPERIA_*` env vars documented in runbook + VARIABLE catalog if repo maintains one.
- [x] Untracked `_release_tmp/`, stray `task.txt` / `theory_description.txt` — either commit policy, `.gitignore`, or move per `REPO_STRUCTURE_POLICY.md`.
- [x] `assets/data/engine_dynamics_v060/VERSION.yaml` consistent with `assets/version_registry.yaml`.
- [x] Product path: default **off** for DLCR structural, API instrumentation, concept guard (unset env).
- [x] Merge or rebase: resolve conflicts with `main` before declaring CLOSED. *(Local branch clean vs origin not enforced here; push-time gate applies.)*

---

## 6. Gena report (append after pass)

| Check | Result |
|-------|--------|
| Date / agent | 2026-03-20 / Gena (consolidation agent) |
| Commands run | §4 matrix + optional heavy E2E (`test_e2e_run_e2e_all_produces_all_artifacts` with `HESPERIA_FIELD_DYNAMICS=1`); `validate_shipping_surface`; `gen_import_graph_doc --write` (public + engine); `verify_public_api_snapshot` |
| Fixes applied | **Dict validators:** `validate_dict_a.py` / `validate_dict_b_dlcr.py` accept zero args → validate all pinned `*.jsonl` under `dict_a/` / `dict_b/`. **Docs:** runbook + `schemas/lexical_concept/README.md` + `dlcr_trace_report.py` docstring clarify **gold markdown** vs **`dump_dlcr_trace` JSON**. **`.gitignore`:** `_release_tmp/`. **Tests:** default-path CLI tests in `test_validators_cli.py`. **Drift:** regenerated `docs/IMPORT_GRAPH_v0_5_0.md`, `docs/IMPORT_GRAPH_ENGINE_v0_5_0.md`. |
| Deferred / risks | Bulk **research/** tree renames remain in working tree (out of integration scope). **PO-30** Ethan backlog still IN PROGRESS per open workflow. |
| Status | **CLOSED** |

### Notes

- **CI:** `.github/workflows/sealed-runtime-gate.yml` — single `check_dlcr_regression` step; DLCR pytest job separate (no duplicate regression).
- **Git scope reviewed:** integration paths vs `research/_noone_local` moves — no link fixes required for product spine.

---

## Related

- Ethan runbook: [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md)  
- Post-options matrix: [ETHAN-DLCR-POST-OPTIONS-TASKS-30.md](ETHAN-DLCR-POST-OPTIONS-TASKS-30.md)  
- Gena proceed log: [GENA-OPEN-WORKFLOW-PROCEED.md](GENA-OPEN-WORKFLOW-PROCEED.md)
