# LEVEL 2 — FAMILY STRUCTURE (TFP / Kernberg domain)

**Цель:** Закрепить 240 семей (операционные; 24 на область A1–A10).

**Source:** `tfp_families.txt` (path e.g. `/home/igareosh/tfp_families.txt`). Format: sections "Area N — …", one family name per block.

---

## T2.1 Family Registry

**Master file:** `spec/families_master.txt`

**Format (4 fields, block per family):**

```
area_id	<A1|A2|...|A10>
family_id	family_<NNN>
family_name	<name RU/EN>
family_definition	<short definition>
```

- 240 families: family_001..family_240.
- Canonical order: A1 (24), A2 (24), … A10 (24).
- Built by: `python3 tools/build_families_master.py [source_path] [output_path]`.

---

## T2.2 Family Scope

Для каждой семьи определить:

| Field | Description |
|-------|-------------|
| **scope** | Short textual scope of the family (what it covers). |
| **included_phenomena** | List of phenomena/concepts included in this family. |
| **excluded_phenomena** | List of phenomena explicitly excluded. |

Stored in `spec/families_structure_tfp.yaml` (per-family `scope`, `included_phenomena`, `excluded_phenomena`). Used for attribution disambiguation and reporting.

---

## T2.3 Family Observability

Каждая семья получает уровень наблюдаемости для NLP:

| Level | Meaning |
|-------|---------|
| **high_observable** | Directly detectable in text (explicit terms, clear markers). |
| **moderate_observable** | Inferrable from context or indirect cues. |
| **latent** | Underlying structure; inferred from patterns, not surface. |

Stored in `spec/families_structure_tfp.yaml` as `observability: high_observable | moderate_observable | latent`. Default for generated entries: `moderate_observable`; adjust per family for NLP pipelines.

---

## T2.4 Family Adjacency

Связи между семьями (в том же и смежных областях):

| Field | Description |
|-------|-------------|
| **family_neighbors** | List of `family_id` topologically adjacent (from geometry / area adjacency). Used for propagation and semantic traversal. |
| **family_conflicts** | List of `family_id` in semantic conflict with this family (to be filled clinically). |
| **family_complements** | List of `family_id` that semantically complement this family (to be filled clinically). |

- **family_neighbors:** Derived from `spec/family_geometry.yaml` (neighbor_families by index → family_id) and/or area adjacency (same area + adjacent areas).
- **family_conflicts / family_complements:** Semantic; initially empty; fill from clinical/TFP expertise.

Stored in `spec/families_structure_tfp.yaml` per family.

---

## File layout

```
spec/families_master.txt           # T2.1 registry (area_id, family_id, family_name, family_definition)
spec/families_structure_tfp.yaml   # T2.2 scope, T2.3 observability, T2.4 adjacency
tools/build_families_master.py     # Build master from tfp_families.txt
tools/build_families_structure_tfp.py  # Generate structure YAML from master + geometry (neighbors)
docs/specs/LEVEL2_FAMILY_STRUCTURE.md  # this spec
```

---

## Loader

**Loaders:** `sphere.topology.family_structure.load_families_master(path)` returns list of registry entries. `load_families_structure_tfp(path)` returns full structure dict. `get_family_by_id(family_id)` returns one family’s scope/observability/adjacency. `OBSERVABILITY_LEVELS` = `high_observable`, `moderate_observable`, `latent`.
