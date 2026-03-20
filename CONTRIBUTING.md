# Contributing (inspection & reference)

This repository is released under a **Restricted Research Disclosure** license. Most use is **inspection and reference only**. See [LEGAL_NOTICE.md](LEGAL_NOTICE.md).

## Before you open a PR or push

1. Read [AGENTS.md](AGENTS.md) for repository rules and command hygiene.
2. Run the **pre-push checklist** in [docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md](docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md).
3. For changes that touch a **sealed release** (`release/v0.5.1/` current, `release/v0.5.0/` historical), follow [docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md](docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md) and `release/v0.5.1/README.md`.
4. **Tasks 1–11 integration map:** [docs/ENGINE_TASKS_1_11_INTEGRATION.md](docs/ENGINE_TASKS_1_11_INTEGRATION.md) — how engine physics wiring maps to `system_seal.json` checks.

## Cursor / IDE

- Workspace root = repository root (where `VERSION.yaml` and `runtime/` live).
- Task queue for this repo: [docs/CURSOR_OPEN_WORKFLOW.md](docs/CURSOR_OPEN_WORKFLOW.md).

For any use beyond the license terms, contact the author.

## DLCR / Dict bumps (Ethan PO-29)

Changing ``assets/data/engine_dynamics_v060/dict_a`` or ``dict_b`` (or resolver scoring) requires
``python3 tools/check_dlcr_regression.py`` clean and, for release lines, a pinned note in the
change log or audit bundle. See [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](docs/governance/working/ETHAN-DLCR-INTEGRATION-RUNBOOK.md).
