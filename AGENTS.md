# AGENT GUIDELINES — HESPERIA (HSPR) Repo

This file describes how automated agents (like LLM-based assistants)
should work with this repository.

## 1. Documentation Structure

- Prefer the numbered documentation files when seeking specs:
  - `10_MASTER_SPEC__HESPERIA_v1_0.txt` is the main semantic reference.
  - `11_BLUEPRINT__HESPERIA_v4_5_full.txt` is the integrated blueprint.
  - `12_SPEC__Semantic_Engine_v0_4.txt` and
    `13_SPEC__Indexing_and_Coordinates_v1_0.txt` define engine + indexing.
- Treat `legacy/` and files prefixed with `60_LEGACY__` or `61_LEGACY__`
  as historical drafts — do not base new designs on them without cross-checking
  against the latest numbered specs.

## 2. Naming and New Docs

- When adding new documentation:
  - Use the pattern: `NN_CATEGORY__Short_title_and_version.txt` (or `.md`).
  - Choose `NN` to keep logical ordering with existing docs.
  - Keep Java-style pseudocode when describing core math or geometry.
- When updating an existing spec:
  - Prefer adding a new versioned file (e.g. `v1_1`) instead of overwriting
    a stable, referenced version.

## 3. Code Conventions

- Keep Python code in `sphere_rag/` synchronized with the latest specs:
  - Geometry and indexing must follow `13_SPEC__Indexing_and_Coordinates_v1_0.txt`.
  - Semantic engine behavior should match `12_SPEC__Semantic_Engine_v0_4.txt`
    and the master/blueprint specs.
- For Java-like documentation:
  - Use clear, compilable-looking signatures but it does not need to be
    fully runnable.
  - Keep constants and formulas consistent with the master specs.


## 3a. Guard Layer Discipline (ΣΓΘ)

- Guard documentation is canonical in
  `42_POLICY__Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`.
- Treat guard layers as non-overlapping responsibilities:
  - **Σ**: static geometry/indexing invariants only.
  - **Γ**: runtime and structure-dynamics invariants only.
  - **Θ**: governance and publishability legitimacy only.
- For changes touching traversal, governance, or indexing, update guard-facing
  docs so reviewers can map behavior to Σ/Γ/Θ checks explicitly.
- Do not weaken a guard silently. If behavior changes, add versioned docs and
  note expected failure mode (`HALT`, `ROLLBACK`, `CORRECT`, or
  `REQUIRE_REVIEW`).

## 4. Safety and Secrets

- `openai_python.txt` and related files may contain API keys controlled
  externally. Do not copy these values into new files or logs.
- When writing example code that uses OpenAI or other APIs, reference
  environment variables or configuration files rather than hardcoding keys.

## 5a. R1–R4 and sphere_math — reason isolated, mitigated (usual mode)

**Background:** A Cursor decoding/formatting loop was tied to R1–R4 spec (table-fill) and large sphere_math output in context. Reason isolated; mitigations in place with common efforts (Ethan deliverable fix, Grace triage/tasking). See `docs/FINDINGS__Cursor_Decoding_Loop_2026-02-27.md`.

**When working with R1–R4 or sphere_math, follow the deliverable fix:**

- **R1–R4:** Pipeline outputs = **JSON per schema only** (Unit, BookProfile, SI_metrics). Do not ask the model to “output in this format” or “fill this table” from the spec; spec tables are reference only. Generate tables from JSON if needed (script/tool).
- **sphere_math 100-sentence run:** Do not attach the full ~28k-line output as context. Use `--limit N` (e.g. `--limit 5`), single-sentence run (`run_sphere_math_values`), or a summary artifact.

**Full rule:** `governance/ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md`. Team tasking: `governance/TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md`, `project/active.md`.

## 6. Scope for This AGENTS File

- These guidelines apply to the entire repository rooted at this directory.
- If nested directories later introduce their own `AGENTS.md`, those files
  may override or extend these rules for their subtrees.
