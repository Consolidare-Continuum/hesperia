<!--
HESPERIA — Reference Architecture Definition (RAD)
-->

# Path ownership matrix

High-level **authority** and packaging hints by top-level path. Details: `REPO_STRUCTURE_POLICY.md`, `docs/governance/SHIPPING_PATH_POLICY_v1.md`.

| Path | Owner / authority | Import into shipping runtime? | Packaged in release bundle? | Safe to delete after a seal tag? |
|------|-------------------|-------------------------------|-----------------------------|----------------------------------|
| `core/` | Engine / math — binding via specs | Yes (internal stack) | Internal packages yes; not raw dump | **No** |
| `hesperia/` | Engine / KME / projection | Yes | Yes (Python package) | **No** |
| `runtime/` | Orchestration / API | Yes | Yes | **No** |
| `sphere/` | Internal structural compute | Yes (internal) | Often yes as dependency | **No** |
| `lexicon/` | Lexical artifacts & tooling | Yes (where wired) | Yes | **No** |
| `schemas/` | Schema artifacts | Yes (by reference) | Yes | **No** |
| `specs/` | **Tier-1 binding** specs | N/A (docs) | Index + selected refs | **No** |
| `tests/` | QA | N/A | Optional dev bundle | **No** (in dev repo) |
| `tools/` | Dev / seal / diagnostics | No (except explicit shims) | Optional | **No** |
| `assets/` | Static inputs | Yes (configured paths) | Selected curated assets | **No** |
| `release/v0.5.0/` | Frozen seal evidence | N/A | **Versioned audit only** | **Never** (historical record) |
| `docs/` | Architecture & governance docs | No | Selected | **No** |
| `examples/` | Runnable demos | No | Optional | Yes if unused |
| `deploy/` | Compose / Docker examples | No | Optional | Yes if unused |
| `benchmarks/` | Evaluation corpora | No | Optional | Yes if unused |
| `research/` | Non-product | **No** | **No** | Yes only if explicitly abandoned |
| `legacy/` | Archive | **No** | **No** | **No** (history) |
| `outputs/`, `tmp/` | Generated | **No** | **No** | Yes (local) |
