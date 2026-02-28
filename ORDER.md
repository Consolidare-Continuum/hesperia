# Repo-wide ORDER — HESPERIA

**One place for each kind of thing. Human-readable names. Versions on everything. No parliament.**

---

## 1. File naming (repo-wide)

- **Human-readable:** Up to **4 words** (underscore-separated), plus version.
- **Pattern:** `[NN_]Word1_Word2_[Word3]_[Word4]_vX_Y.ext`
  - Optional leading `NN_` for ordering (e.g. `10_`, `42_`).
  - Version always: `_vX_Y` (e.g. `_v1_0`, `_v0_4`).
- **Examples (good):**  
  `Master_Spec_Hesperia_v1_0.txt`, `Structural_Loop_12_Node_v1_0.md`, `Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`
- **Examples (bad):**  
  Long descriptive sentences in filenames; no version; random abbreviations.

---

## 2. Where things live

| Kind | Location | Rule |
|------|----------|------|
| **Specs** | Repo **root** (or `specs/`) | All specs findable from root. Existing: `NN_CATEGORY__Title_vX_Y.txt`. New: max 4 words + `_vX_Y`. |
| **Python** | **Single place:** `sphere_rag/` (core), `api/` (service), `scripts/` (one-off), `hesperia_lex/scripts/` (lex builds) | No new top-level Python folders. No scattered `.py` at root. |
| **Artifacts** | **Subfolders only:** `artifacts/<product>/` | All generated outputs go under `artifacts/`. Not in `docs/` or root. |
| **Governance / project** | `governance/`, `project/` | Policy, tasks, handoffs. Names: readable, versioned where relevant. |
| **Docs (narrative)** | `docs/` | Prose, findings, procedures. No run outputs here. |
| **Archive** | `archive/` | Old versions, deprecated. Do not use for new work. |
| **MRT (12×8=96 fork)** | **`HESPERIA_MRT/`** | On branch `hesperia-mrt-fork` here; standalone repo: **`mrt`** → `git@github.com:igareosh/hesperia_mrt.git` (branch `main`). |

---

## 3. Artifacts layout

All produced outputs go under **`artifacts/`**:

```
artifacts/
  e2e/           # E2E run outputs (run_output_*.json, *.txt)
  layer_runs/    # L1–L9 layer run outputs
  lex/           # Lexical/Dict builds (if not under hesperia_lex)
  calibration/   # Calibration runs
  api/           # API or service outputs (if any)
```

- **Naming inside artifacts:** Same rule: up to 4 words + version (e.g. `Run_Output_E2E_Sentence_v1_0.txt` or keep `run_output_e2e_sentence.txt` as-is for scripts; new files use the rule).

---

## 4. Specs (root vs specs/)

- **Current:** Numbered specs at repo root (`10_MASTER_SPEC__...`, `42_POLICY__...`, etc.). Keep them there; they are the canonical references.
- **New specs:** Add at root with pattern `NN_Name_Up_To_Four_Words_vX_Y.ext`, or under `specs/` with the same naming. No new spec without a version.

---

## 5. Python (single place)

- **Core engine:** `sphere_rag/` — analyze, attribution, layers, guards, R1–R4, etc.
- **Service:** `api/` — HTTP/API entrypoints.
- **One-off / ops:** `scripts/` — guards, calibration, verify.
- **Lex builds:** `hesperia_lex/scripts/` — Dict A/B, families, ingest.
- Do **not** add new Python at repo root or under arbitrary folders. Put new code in one of the above.

---

## 6. Why this order

- **Specs at root:** So anyone can find them from anywhere; one mental map.
- **Python in one place:** So we don’t hunt for “where’s the script”; one tree.
- **Artifacts in subfolders:** So outputs don’t mix with source and specs; one place to look for runs.
- **4 words + version:** So names stay scannable and we can tell versions apart without opening files.

---

**Refs:** `AGENTS.md` (agent rules), `DOC_INDEX.md` (doc index), `README-REPO-STRUCTURE.md` (structure).
