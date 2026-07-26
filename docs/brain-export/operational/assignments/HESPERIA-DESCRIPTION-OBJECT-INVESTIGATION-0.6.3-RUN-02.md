# Hesperia Description Object Investigation — Run 02 of 05

**Title:** Modular engine kernel — phased module execution, calculus, aggregation, exit contract  
**Version:** Hesperia 0.6.3 (description object investigation)  
**Product SHA:** `e9eaa07` · **Index:** [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md) · **Prior:** [RUN-01](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md)

---

## Abstract

Run 02 traces **Spine A** (modular engine kernel) at **file and block granularity**: how `configs/pipeline.yaml` loads six modules, how each implements `preprocess` / `project` / `postprocess`, how `hesperia/engine/calculus.py` computes shared transforms, and how `aggregate_modules` plus `analyze_engine` produce the canonical result contract. Only **`nlp.basic`** runs in **preprocess**; five modules run in **project**; **postprocess** is empty for the default roster. No module uses **postprocess** in the default config.

---

## 1. Entry and load sequence

### 1.1 Call chain

| Order | File | Function | Parameters in | Parameters out |
|-------|------|----------|---------------|----------------|
| 1 | `hesperia/engine/runner.py` | `run_orchestration(text, repo_root, config_path)` | UTF-8 `text`, path to `configs/pipeline.yaml` | Full `ctx` |
| 2 | `hesperia/engine/core.py` | `HesperiaEngine.load_from_config(config_path)` | YAML modules list | Populated `self.modules` |
| 3 | `hesperia/engine/core.py` | `HesperiaEngine.run(text, signals=None)` | `text`, optional `signals[]` | `ctx` after aggregation |
| 4 | `hesperia/engine/pipeline_runner.py` | `run_pipeline(text, config_path=…)` | Same + manifest | Subset dict for tests |
| 5 | `core/runtime/engine.py` | `analyze_engine(text)` | `text` | `hesperia.result.v1` dict |

**`pipeline_runner` difference:** After `engine.run`, calls `validate_final_ctx(ctx)` when `until_phase is None`, stamps `meta.version_manifest` and `meta.run_manifest` (config checksum, module versions, phase hashes).

### 1.2 Module load (`module_loader.py` + `module_aliases.py`)

Alias resolution (SSOT):

| YAML alias | Import path | Factory |
|------------|-------------|---------|
| `nlp.basic` | `hesperia.modules.nlp.basic` | `create()` → `NLPModule` |
| `core.dict_a` | `hesperia.modules.core.dict_a` | `DictAModule` |
| `core.dict_b` | `hesperia.modules.core.dict_b` | `DictBModule` |
| `topology.core` | `hesperia.modules.topology.core` | `TopologyModule` |
| `tfp` | `hesperia.modules.tfp.v1` | `TFPModule` (name `tfp.v1`) |
| `metrics.base` | `hesperia.modules.metrics.base` | `MetricsModule` |

**Load-time validation** (`module_validator.py`): each module must expose `name`, `version`, `provides`, `requires`, `capabilities`, `output_schema`, callable `configure`, and callable bodies for every phase where `capabilities[phase]==True`.

**Version pin:** `pipeline.yaml` may set `expected_module_versions` + `fail_on_version_mismatch`; default config does not fail on mismatch.

---

## 2. Kernel loop — one iteration explained

**File:** `hesperia/engine/core.py` — `HesperiaEngine.run`

### 2.1 Initialization block

```python
base_ctx = build_context(text, signals=signals)
ctx = GuardedContext(base_ctx)
ctx["meta"]["module_config_resolved"] = self.module_runtime_config
ctx["meta"]["aggregation_strategy"] = ...  # default "weighted_merge"
validate_context(ctx, "start")
graph = build_execution_graph(self.modules)
ctx["meta"]["execution_graph"] = {phase: [m.name for m in modules] for ...}
snapshot = freeze_context(ctx)
```

**State after init:** empty `families`, `areas`, `metrics`, `modules`; `meta.trace=[]`.

### 2.2 Inner loop (per module, per phase)

For each `(phase, module)`:

1. **Scope grant:** `ctx.allow(module=m.name, path=f"modules.{m.name}.*")` plus read paths `input.*`, `signals.*`, `modules.*`, `meta.trace`; deny read `metrics.final`.
2. **Snapshot module slots:** `before = _snapshot_modules(ctx)`.
3. **Phase dispatch:** if `m.capabilities[phase]`: call `getattr(m, phase)(ctx)`.
4. **Schema check:** `_validate_output_schema(m, ctx)` against `output_schema` types.
5. **Scope audit:** `_assert_module_scope(before, ctx, m.name)` — no cross-module writes.
6. **Trace append:** `{module, phase, inputs, outputs}` to `meta.trace`.
7. **Validate:** `validate_context(ctx, f"{phase}:{m.name}")`.
8. **Clear grants:** `ctx.clear_allow()`.

**Strict mode:** any exception in step 3 re-raises; `failure_mode != strict` appends to `meta.failed_modules` and continues.

### 2.3 Phase boundary

After all modules in a phase: `snapshot = freeze_context(ctx)`; `ctx["meta"][f"hash_{phase}"] = hash_context(ctx)`.

### 2.4 Terminal aggregation

```python
aggregate_modules(ctx)
validate_context(ctx, "aggregated")
ctx["meta"]["hash_aggregated"] = hash_context(ctx)
return ctx
```

---

## 3. Default execution graph order

**Symbolic availability** starts `{input.text, input.signals}`.

| Phase | Order | Module | Capability | New symbols (provides) |
|-------|-------|--------|------------|------------------------|
| **preprocess** | 1 | `nlp.basic` | yes | `normalized_tokens`, `canonical_text` |
| **preprocess** | 2–6 | others | no | (skipped) |
| **project** | 1 | `core.dict_a` | yes | `concept_hits` |
| **project** | 2 | `core.dict_b` | yes | `family_scores_raw`, `area_scores_raw` |
| **project** | 3 | `topology.core` | yes | `area_scores_normalized` |
| **project** | 4 | `tfp.v1` | yes | `tfp_vector`, `tfp_profile`, `tfp_conflicts` |
| **project** | 5 | `metrics.base` | yes | `metrics_bundle` |
| **postprocess** | — | all | no | — |

**Note:** Topological sort may swap `topology.core` and `tfp.v1` (both depend only on `dict_b` outputs); **`metrics.base` must follow `topology.core`** because it requires `area_scores_normalized`.

**Iteration count (active steps):** 1 preprocess + 5 project = **6 module invocations** per `engine.run`.

---

## 4. Module file — block-by-block

### 4.1 `hesperia/modules/nlp/basic.py` — `NLPModule`

**Scope:** First transform of raw operator text. **Phase:** preprocess only.

**Contract:**

| Field | Value |
|-------|--------|
| `name` | `nlp.basic` |
| `version` | `v1` |
| `requires.preprocess` | `["input.text"]` |
| `provides.preprocess` | `normalized_tokens`, `canonical_text` |
| `output_schema` | `tokens: list`, `canonical_text: str` |

**`configure(config)`:** `self.stopwords = set(config.get("stopwords", []))` — from YAML `module_config.nlp.basic.stopwords` (default `[]`).

**`preprocess(ctx)` block:**

```python
norm = normalize_text(str((ctx.get("input") or {}).get("text") or ""))
tokens = [t for t in (norm.get("tokens") or []) if t and t not in self.stopwords]
ctx["modules"][self.name]["tokens"] = tokens
ctx["modules"][self.name]["canonical_text"] = norm.get("canonical_text", "")
```

**Downstream dependency:** `core.lexical.normalization.normalize_text` (`core/lexical/normalization.py`):

- NFKC unicode normalize, casefold, whitespace collapse.
- Token regex: `[a-z0-9]+(?:'[a-z0-9]+)?` on canonical text.
- Emits `tokens`, `token_spans`, `phrase_spans` (phrases length 2–5 for DLCR; unused here).

**Output → input mapping:**

| Output slot | Consumer |
|-------------|----------|
| `modules.nlp.basic.tokens` | `dict_a.project`, `tfp.v1.project` (as `normalized_tokens`) |
| `modules.nlp.basic.canonical_text` | diagnostics only in this pipeline |

**Example:** `text = "Пациент чувствует СТЫД."` → casefold + tokenization yields tokens including `стыд` if Cyrillic passes token regex (Latin-centric regex — **RU tokens may require separate lexical path on shipping**; modular path inherits this limitation).

---

### 4.2 `hesperia/modules/core/dict_a.py` — `DictAModule`

**Scope:** Lexical form → concept id hits (Dict A calibration). **Phase:** project.

**Contract:**

| Field | Value |
|-------|--------|
| `requires.project` | `normalized_tokens` |
| `provides.project` | `concept_hits` |
| `output_schema` | `concept_hits: list` |

**`configure(config)` block:**

1. If `config.entries` empty → resolve `dict_a.jsonl` via `resolve_dict_file(repo, "dict_a.jsonl", calibration_dict_version)`.
2. Fallback path: `assets/data/engine_dynamics_v060/dict_a/dict_a_seed.jsonl`.
3. Build `self.entries: dict[normalized_form → list[candidate_concept_ids]]`.

**`project(ctx)` block:**

```python
hits: list[str] = []
tokens = list((ctx.get("modules") or {}).get("nlp.basic", {}).get("tokens") or [])
for token in tokens:
    hits.extend(self.entries.get(str(token), []))
ctx["modules"][self.name]["concept_hits"] = sorted(hits)
```

**Transform:** multiset union of concept ids per token; sorted for determinism.

**Parameters:** `HESPERIA_CALIB_DICT_VERSION`, `HESPERIA_DICT_A_*` env vars affect asset path (via calibration loader — not reread each token in module).

**Output → input:** `concept_hits` → `dict_b.project`, `tfp.v1.project`.

---

### 4.3 `hesperia/modules/core/dict_b.py` — `DictBModule`

**Scope:** Concept ids → raw family and area score maps via ontology rows. **Phase:** project.

**`configure`:** loads `dict_b.jsonl` / seed into `self.map: concept_id → {family_ids, area_ids, ...}`.

**`project(ctx)` block:**

```python
concept_hits = list((ctx.get("modules") or {}).get("core.dict_a", {}).get("concept_hits") or [])
family_scores, area_scores, families, areas = concepts_to_family_area_scores(concept_hits, self.map)
ctx["modules"][self.name]["family_scores"] = family_scores
ctx["modules"][self.name]["area_scores"] = area_scores
ctx["modules"][self.name]["families"] = families
ctx["modules"][self.name]["areas"] = areas
```

**Calculus** (`hesperia/engine/calculus.py` — `concepts_to_family_area_scores`):

For each concept id \(c\) in hits, for each family id \(f \in \text{meta}(c).\text{family\_ids}\):

\[
\text{family\_scores}[f] \mathrel{+}= 1
\]

Similarly for area ids. Keys sorted lexicographically in return tuples.

**Output slots (module namespace):**

| Key | Role | Symbol name in graph |
|-----|------|----------------------|
| `family_scores` | raw counts/weights | `family_scores_raw` |
| `area_scores` | raw counts/weights | `area_scores_raw` |
| `families`, `areas` | key lists | diagnostics |

---

### 4.4 `hesperia/modules/topology/core.py` — `TopologyModule`

**Scope:** Normalize area scores to simplex over `area_count` (default 12). **Phase:** project.

**`configure`:** `self.area_count = int(config.get("area_count", 12))`.

**`project(ctx)` block:**

```python
area_scores = dict((ctx.get("modules") or {}).get("core.dict_b", {}).get("area_scores") or {})
ctx["modules"][self.name]["area_scores"] = normalize_area_scores(area_scores, self.area_count)
```

**Formula** (`normalize_area_scores`):

Let \(s_k\) be raw scores. If \(\sum s_k = 0\): uniform \(1/|K|\). Else:

\[
\hat{s}_k = \frac{s_k}{\sum_j s_j}
\]

If empty input: initialize `A1…A12` at 0 then uniform fallback.

**Output → input:** `modules.topology.core.area_scores` → `metrics.base` as **`area_scores_normalized`**.

---

### 4.5 `hesperia/modules/tfp/v1.py` — `TFPModule`

**Scope:** TFP vector, clinical stage profile, conflict flags. **Phase:** project. Loaded via alias `tfp` in YAML; **`name = "tfp.v1"`** in ctx keys.

**Seal hook:** first line of `project` calls `enforce_tfp_module_seal_on_project()` (`hesperia/modules/tfp/seal.py`):

| `HESPERIA_TFP_MODULE_SEALED` | Behavior |
|----------------------------|----------|
| unset / off | no-op |
| `1` / `true` | stderr WARNING |
| `block` | `RuntimeError` — fail closed |

**`project(ctx)` block:**

```python
vector, profile, conflicts = compute_tfp_bundle(
    family_scores=dict(modules.get("core.dict_b", {}).get("family_scores") or {}),
    area_scores=dict(modules.get("core.dict_b", {}).get("area_scores") or {}),
    concept_hits=list(modules.get("core.dict_a", {}).get("concept_hits") or []),
    text=str((ctx.get("input") or {}).get("text") or ""),
    tokens=list(modules.get("nlp.basic", {}).get("tokens") or []),
    labels=self.labels,
)
ctx["modules"][self.name]["tfp_vector"] = vector
ctx["modules"][self.name]["tfp_profile"] = profile
ctx["modules"][self.name]["tfp_conflicts"] = conflicts
```

**`compute_tfp_bundle` formulas** (`calculus.py`):

1. **TFP vector buckets** (default labels `control`, `aggression`, `identity`, `trust`):
   - Enumerate sorted `family_scores` pairs \((f_i, v_i)\).
   - Assign \(v_i\) to `labels[i mod len(labels)]`.
   - Normalize bucket sums to simplex.

2. **Profile:**
   - `dominant` = argmax bucket
   - `stage` = `detect_tfp_stage(area_scores, family_scores)` (see Run 01 / `tfp_math.py`)
   - `affect_intensity` = `estimate_affect_intensity(text, tokens)`
   - `confidence_scores` = entropy-based (`compute_confidence_scores`)

3. **Conflicts:**
   - Any bucket value \(> 0.4\) → conflict string key
   - `detect_interaction_loops([snapshot, snapshot])` with duplicated single-step timeline → optional `interaction_loop` entries

**Output → aggregation:** `tfp_conflicts` merged in `aggregate_modules` → `ctx.signals.tfp_conflicts`.

---

### 4.6 `hesperia/modules/metrics/base.py` — `MetricsModule`

**Scope:** Engine-facing scalars and vectors for `analyze_engine`. **Phase:** project.

**`configure`:** `family_count=24`, `area_count=12` from YAML.

**`project(ctx)` block:**

```python
area_scores = dict(modules.get("topology.core", {}).get("area_scores") or {})
family_scores = dict(modules.get("core.dict_b", {}).get("family_scores") or {})
metrics = compute_metrics_bundle(
    area_scores=area_scores,
    family_scores=family_scores,
    area_count=self.area_count,
    family_count=self.family_count,
)
ctx["modules"][self.name]["metrics"] = metrics
ctx["modules"][self.name]["area_scores"] = area_scores
ctx["modules"][self.name]["family_scores"] = family_scores
```

**`compute_metrics_bundle` output fields:**

| Field | Definition |
|-------|------------|
| `area_vector` | `[area_scores.get(f"A{i+1}", 0) for i in 0..11]` |
| `family_vector` | normalized over `F1…F24` from raw family_scores |
| `dominant_area` | argmax index of `area_vector` |
| `dominant_family` | argmax index of `family_vector` |
| `tension` | `compute_tension(area_vector)` — paired antipodal areas |
| `loopability` | from synthetic trajectory `{segment_count:1, …}` |
| `stability` | `compute_stability([0.0])` → 1.0 default |

**Tension formula** (`core/result/contract.py`):

Pairs \((i, i+6)\) for \(i \in 0..5\):

\[
\text{tension} = \sum_{i=0}^{5} |A_i - A_{i+6}|
\]

(quantized/clamped in contract builder.)

**Loopability:**

\[
\text{return\_frequency} = 1 - \frac{\text{transition\_count}}{\max(1, \text{segment\_count}-1)}
\]
\[
\text{cycle\_detection} = 1 - \min\left(1, \frac{\text{jump\_distance}}{24}\right)
\]
\[
\text{loopability} = \frac{\text{return\_frequency} + \text{cycle\_detection} + \text{stability\_window}}{3}
\]

---

## 5. Aggregation — modules → top-level `ctx`

**File:** `hesperia/engine/aggregation.py` — `aggregate_modules(ctx)`

**Steps:**

1. Collect each module payload with optional `weight` (default 1.0) and `priority` (default 0) from `meta.module_config_resolved`.
2. Merge all `payload.metrics` dicts into `merged_metrics`.
3. Collect all `tfp_conflicts` strings.
4. `merge_module_payloads(payloads, strategy)` — default **`weighted_merge`**:
   - Family and area score dicts merged separately via `resolve_scores`.
   - Weighted merge: \( \text{out}[k] \mathrel{+}= v \cdot weight \).
5. `_normalize` family and area merged dicts to simplex (non-negative, sum 1).
6. Write:
   - `ctx["families"]`, `ctx["areas"]`, `ctx["metrics"]`
   - `ctx["signals"]["tfp_conflicts"]` = sorted unique list

**Alternate strategies:** `exclusive` (highest priority module only), `priority` (first-seen keys by priority).

---

## 6. Post-run validation

### 6.1 `validate_final_ctx` (`validators.py`)

- No NaN/Inf in families, areas, metrics floats.
- If families non-empty: sum ≈ 1 (±0.01).
- If areas non-empty: sum ≈ 1.
- Metric magnitudes bounded (\(|v| \le 10^9\)).

### 6.2 `analyze_engine` exit (`core/runtime/engine.py`)

```python
ctx = run_orchestration(text, repo_root=repo_root)
metrics = dict(ctx.get("metrics") or {})
area_vector = list(metrics.get("area_vector") or [])
family_vector = list(metrics.get("family_vector") or [])
area_activation = {f"A{i+1}": float(v) for i, v in enumerate(area_vector)}
family_activation = {f"F{i+1}": float(v) for i, v in enumerate(family_vector)}
failure_flags = list(dict(ctx.get("signals") or {}).get("tfp_conflicts") or [])
result = build_result(...)
guard_determinism(result)
return result
```

**`build_result`** → `build_result_contract` (`core/result/contract.py`):

- Re-normalizes to 12 / 24 dimensions.
- Computes `dominant_area`, `dominant_family` with confidence gap.
- Adds `fingerprint`, `deterministic_hash` over payload.
- Schema version **`hesperia.result.v1`**.

**Note:** Modular path emits **24-family** vector in metrics module but shipping sealed stack uses **288 families** — Spine A and Spine B differ in dimensionality (Run 03 vs Run 04).

---

## 7. Context evolution example (toy)

**Input:** `text = "shame rejection anger"`, seed dict maps tokens → concepts → families/areas.

| Step | `modules.*` keys populated | Top-level `ctx` |
|------|---------------------------|-----------------|
| init | `{}` | empty buckets |
| after `nlp.basic` preprocess | `nlp.basic: {tokens, canonical_text}` | unchanged |
| after `dict_a` project | `+ concept_hits: ["SHAME", "REJECTION"]` | unchanged |
| after `dict_b` project | `+ family_scores, area_scores, …` | unchanged |
| after `topology` project | `topology.core.area_scores` normalized | unchanged |
| after `tfp.v1` project | `tfp_vector, tfp_profile, tfp_conflicts` | unchanged |
| after `metrics.base` project | `metrics: {area_vector, tension, …}` | unchanged |
| after `aggregate_modules` | (module slots frozen) | `families`, `areas`, `metrics`, `signals.tfp_conflicts` |

**`meta.trace` length:** 6 entries (one per active phase invocation) plus optional error records.

---

## 8. `pipeline_runner` manifest (audit artifact)

**File:** `hesperia/engine/pipeline_runner.py`

After run, attaches:

```python
ctx["meta"]["run_manifest"] = {
    "config_path": str(config_path),
    "config_checksum": sha256(config bytes),
    "modules_loaded": [m.name for m in engine.modules],
    "input_checksum": sha256(text),
    "hashes": {k: v for k, v in ctx.meta if k.startswith("hash_")},
}
```

**Returned dict** (API of `run_pipeline`):

```python
{
    "meta": ctx["meta"],
    "signals": ctx["signals"],
    "areas": ctx["areas"],
    "families": ctx["families"],
    "metrics": ctx["metrics"],
    "trace": ctx["meta"]["trace"],
}
```

---

## 9. Relation to 0.6.3 and shipping

| Path | Uses modular Spine A? |
|------|------------------------|
| `analyze_engine()` / `run_orchestration` | **Yes** — full module pipeline |
| `run_structural_analysis` (shipping) | **No** — sealed multiscale only |
| `runtime/irc_teacher` HTTP `/analyze` | **Shipping** — not `analyze_engine` directly |

**Implication:** 0.6.3 IRC Teacher observes **shipping** analyze output (ENGINE-ANALYZE sidecar), not raw modular `ctx`. Modular path remains critical for **tests**, **module development**, and **TFP plugin** behavior documented here.

---

## 10. Run 02 summary

| Artifact | Blocks documented |
|----------|-------------------|
| Kernel | `core.py` run loop, guard, hash phases |
| Loader | aliases, validator, YAML config |
| 6 modules | all active phase methods |
| Calculus | concept→family/area, TFP bundle, metrics bundle |
| Aggregation | weighted_merge, normalization |
| Exit | `validate_final_ctx`, `hesperia.result.v1` |

---

## NEXT (Colombo)

1. [ ] **Run 03** — `sealed_multiscale_stack` tensor pipeline + hex step numeric example — owner: **Colombo**
2. [ ] **Run 04** — ENGINE-ANALYZE `trace[]` + FastAPI handler — owner: **Colombo**
3. [ ] **Run 05** — 0.6.3 full RU trace + parameter tables — owner: **Colombo**

**Verified exists:** all module sources @ `e9eaa07`; `configs/pipeline.yaml`; `calculus.py`, `aggregation.py`  
**Still unverified:** whether prod `/analyze` sidecar ever embeds modular `ctx` dump (expect engine_result from shipping only)

---

SIGNED: Research (Colombo) | Hesperia description object investigation Run 02 | 2026-06-14 | v0.6.3
