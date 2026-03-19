---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-SYSTEM-GOV
---

# Versioning, structure, and spec authority — canonical

## 1. Version truth (Task 1)

- **Single source:** `VERSION.yaml` at repository root (`system_version`, `schema.public_output`, `components`, `pipelines`, `build` injection).
- **Python:** `hesperia.system.version` loads YAML; **no** silent override of trace fields on public JSON.
- **Policy:** `docs/VERSION_POLICY.md` (explanatory) must not contradict this section.

## 2. Repository structure (Task 2)

- **Policy files:** `REPO_STRUCTURE_POLICY.md`, `EXTENSION_STATUS.yaml`, `GENERATED_ARTIFACT_POLICY.md`.
- **Experimental code:** `research.*` (e.g. `research.clinical_tfp`) — not baseline product surface.
- **Extensions:** `hesperia.extensions.dynamics`, `hesperia.extensions.triz`.

## 3. Spec authority (Task 3) — three tiers

| Tier | Location | May define equations? |
|------|----------|------------------------|
| **1 — Canonical** | `specs/core/`, `specs/dynamics/semantic_field_dynamics.md`, `specs/calibration/*.md`, `specs/triz/*.md`, `specs/schema/public_output_schema.md`, `specs/system/*.md` | **Yes** (once only) |
| **2 — Derived / explanatory** | `docs/**` | **No** new binding rules; reference Tier-1 |
| **3 — Research** | `research/**` | **No** system truth |

## 4. Spec file header (binding)

Every **Tier-1** spec must begin with YAML front matter:

```yaml
spec_version: "x.y"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-...
```

## 5. `spec/` symlink

`spec/` → `specs/canon/` holds **YAML/PL** assets for loaders. **Markdown** under `specs/canon/` that duplicates Tier-1 must be **redirect stubs** only.

## 6. Change control

- **Schema / public shape change** → bump `schema.public_output` + update `schemas/public/public_output_schema.md` mirror + release notes.
- **Equation change** → edit **exactly one** Tier-1 file + bump `spec_version` + align code or mark code wrong.
