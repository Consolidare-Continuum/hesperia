<!--
  HESPERIA — Generated file. Regenerate:
    python3 tools/gen_import_graph_doc.py --write --profile engine
  CI drift check:
    python3 tools/gen_import_graph_doc.py --profile engine | diff -q docs/IMPORT_GRAPH_ENGINE_v0_5_0.md -
-->

# Import graph — `hesperia/engine` (v0.5.0 seal baseline)

This document lists **static** `import` / `from` targets seen under the scanned trees. It is a **drift detector**: unexpected new edges often mean a boundary or layering mistake.

## Scanned directories

- `hesperia/engine/`

## Aggregate import targets (reference count)

- `__future__` — **73**
- `collections` — **3**
- `copy` — **1**
- `core.attribution.structural` — **1**
- `core.diagnostics.failures` — **1**
- `core.domain.bridge` — **1**
- `core.domain.loader` — **1**
- `core.domain.models` — **1**
- `core.domain.pipeline` — **1**
- `core.dynamics.constants` — **1**
- `core.dynamics.numeric` — **2**
- `core.guards.determinism` — **1**
- `core.guards.invariants` — **1**
- `core.hexmap.aggregate` — **1**
- `core.hexmap.analytics` — **1**
- `core.hexmap.topology` — **1**
- `core.layers` — **1**
- `core.lexical.analysis_input` — **1**
- `core.lexical.cooccurrence` — **1**
- `core.lexical.matcher` — **1**
- `core.lexical.policy` — **1**
- `core.math.io_deterministic_json` — **1**
- `core.output.result_builder` — **1**
- `core.pipeline.dynamics` — **1**
- `core.pipeline.lexical` — **1**
- `core.pipeline.projection` — **1**
- `core.pipeline.resolver` — **1**
- `core.pipeline.trajectory` — **1**
- `core.projection` — **1**
- `core.projection.public_projection_layer` — **1**
- `core.result.contract` — **1**
- `core.runtime.engine` — **2**
- `core.sequence.segmentation` — **1**
- `core.state.semantic_state` — **1**
- `core.topology.invariant_catalog` — **2**
- `dataclasses` — **10**
- `enum` — **1**
- `functools` — **4**
- `hashlib` — **4**
- `hesperia.engine.aggregation` — **1**
- `hesperia.engine.calibration.activation_calibration` — **1**
- `hesperia.engine.calibration.hspr_field` — **1**
- `hesperia.engine.calibration_dict_paths` — **1**
- `hesperia.engine.concept_dictionary.executor` — **2**
- `hesperia.engine.concept_dictionary.loader` — **2**
- `hesperia.engine.concept_dictionary.validator` — **1**
- `hesperia.engine.conflict_resolver` — **1**
- `hesperia.engine.context_guard` — **1**
- `hesperia.engine.context_schema` — **1**
- `hesperia.engine.context_snapshot` — **1**
- `hesperia.engine.core` — **2**
- `hesperia.engine.energy` — **2**
- `hesperia.engine.engine_signal_calibration` — **1**
- `hesperia.engine.execution_graph` — **1**
- `hesperia.engine.explainability` — **1**
- `hesperia.engine.hesperia_control.dominance` — **1**
- `hesperia.engine.hesperia_control.modifier_mvp` — **1**
- `hesperia.engine.hesperia_control.readonly_guard` — **2**
- `hesperia.engine.hesperia_control.unmapped_diagnostics` — **1**
- `hesperia.engine.hex_dynamics` — **2**
- `hesperia.engine.hex_family_bridge` — **1**
- `hesperia.engine.hex_matrix_builders` — **3**
- `hesperia.engine.hex_outputs.cluster_gravity` — **1**
- `hesperia.engine.hex_outputs.contradiction_front` — **1**
- `hesperia.engine.hex_outputs.e2e_integration` — **1**
- `hesperia.engine.hex_outputs.hex_output_engine` — **2**
- `hesperia.engine.hex_outputs.hotspot_map` — **1**
- `hesperia.engine.hex_outputs.multiscale_consistency` — **1**
- `hesperia.engine.hex_outputs.propagation_corridors` — **1**
- `hesperia.engine.hspr_index` — **1**
- `hesperia.engine.kme.active_graph` — **3**
- `hesperia.engine.kme.clinical_bridge` — **1**
- `hesperia.engine.kme.derived.calculator` — **4**
- `hesperia.engine.kme.extractor` — **2**
- `hesperia.engine.kme.fingerprint.builder` — **6**
- `hesperia.engine.kme.fingerprint_distance` — **1**
- `hesperia.engine.kme.loader` — **1**
- `hesperia.engine.kme.models` — **11**
- `hesperia.engine.kme.pipeline` — **2**
- `hesperia.engine.kme.primitives.calculator` — **4**
- `hesperia.engine.kme.profiling.profiler` — **2**
- `hesperia.engine.language` — **1**
- `hesperia.engine.lexical_concept.pipeline` — **2**
- `hesperia.engine.matrix_loader` — **3**
- `hesperia.engine.module_loader` — **1**
- `hesperia.engine.module_validator` — **1**
- `hesperia.engine.observables` — **1**
- `hesperia.engine.output_anomalies` — **1**
- `hesperia.engine.pch_loader` — **2**
- `hesperia.engine.product_signals` — **1**
- `hesperia.engine.projection.public_projection` — **1**
- `hesperia.engine.projection.sanitizer` — **1**
- `hesperia.engine.projection.schema_enforcer` — **2**
- `hesperia.engine.sealed_multiscale_stack` — **1**
- `hesperia.engine.tfp_math` — **1**
- `hesperia.engine.validators` — **1**
- `hesperia.extensions.dynamics.e2e_bridge` — **3**
- `hesperia.extensions.dynamics.equations` — **1**
- `hesperia.extensions.triz.kme_bridge` — **2**
- `hesperia.extensions.triz.models` — **1**
- `hesperia.extensions.triz.pipeline` — **1**
- `hesperia.modules.registry` — **1**
- `hesperia.nlp.session_parser` — **1**
- `hesperia.ontology.dictB.loader` — **1**
- `hesperia.system.version` — **7**
- `importlib` — **1**
- `json` — **16**
- `math` — **15**
- `numpy` — **19**
- `os` — **7**
- `pathlib` — **25**
- `re` — **3**
- `runtime.shipping.schema_guard` — **1**
- `scipy.sparse` — **3**
- `sphere.topology` — **1**
- `sphere.topology.family_embedding` — **2**
- `statistics` — **1**
- `types` — **1**
- `typing` — **64**
- `warnings` — **1**
- `yaml` — **5**

## Per-file edges (sorted by path)

### `hesperia/engine/__init__.py`

### `hesperia/engine/aggregation.py`

**from**
- `__future__`
- `hesperia.engine.conflict_resolver`
- `typing`

### `hesperia/engine/api.py`

**from**
- `__future__`
- `core.runtime.engine`
- `typing`

### `hesperia/engine/calculus.py`

**from**
- `__future__`
- `core.result.contract`
- `hesperia.engine.tfp_math`
- `typing`

### `hesperia/engine/calibration/__init__.py`

**from**
- `hesperia.engine.calibration.activation_calibration`
- `hesperia.engine.calibration.hspr_field`

### `hesperia/engine/calibration/activation_calibration.py`

**import**
- `yaml`

**from**
- `__future__`
- `pathlib`
- `typing`

### `hesperia/engine/calibration/hspr_field.py`

**import**
- `numpy`

**from**
- `__future__`
- `dataclasses`
- `hesperia.engine.observables`
- `typing`

### `hesperia/engine/calibration_dict_paths.py`

**import**
- `os`

**from**
- `__future__`
- `pathlib`
- `typing`

### `hesperia/engine/calibration_profile.py`

**import**
- `json`

**from**
- `__future__`
- `hesperia.extensions.dynamics.equations`
- `hesperia.system.version`
- `pathlib`
- `typing`

### `hesperia/engine/calibration_release_gate.py`

**import**
- `json`

**from**
- `__future__`
- `hesperia.engine.output_anomalies`
- `pathlib`
- `typing`

### `hesperia/engine/concept_dictionary/__init__.py`

**from**
- `hesperia.engine.concept_dictionary.executor`
- `hesperia.engine.concept_dictionary.loader`

### `hesperia/engine/concept_dictionary/executor.py`

**import**
- `math`

**from**
- `__future__`
- `core.dynamics.numeric`
- `hesperia.engine.concept_dictionary.loader`
- `pathlib`
- `typing`

### `hesperia/engine/concept_dictionary/loader.py`

**import**
- `json`

**from**
- `__future__`
- `hesperia.engine.concept_dictionary.validator`
- `pathlib`
- `typing`

### `hesperia/engine/concept_dictionary/validator.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/conflict_resolver.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/context_guard.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/context_schema.py`

**from**
- `__future__`
- `hesperia.engine.language`
- `typing`

### `hesperia/engine/context_snapshot.py`

**import**
- `copy`
- `hashlib`
- `json`

**from**
- `__future__`
- `types`
- `typing`

### `hesperia/engine/core.py`

**import**
- `json`
- `yaml`

**from**
- `__future__`
- `dataclasses`
- `hesperia.engine.aggregation`
- `hesperia.engine.context_guard`
- `hesperia.engine.context_schema`
- `hesperia.engine.context_snapshot`
- `hesperia.engine.execution_graph`
- `hesperia.engine.module_loader`
- `hesperia.engine.module_validator`
- `pathlib`
- `typing`

### `hesperia/engine/dependency_resolver.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/energy.py`

**import**
- `numpy`

**from**
- `__future__`
- `dataclasses`
- `enum`
- `typing`

### `hesperia/engine/engine_signal_calibration.py`

**import**
- `json`
- `math`

**from**
- `__future__`
- `functools`
- `pathlib`
- `typing`

### `hesperia/engine/execution_graph.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/explainability.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/hesperia_control/__init__.py`

**from**
- `hesperia.engine.hesperia_control.dominance`
- `hesperia.engine.hesperia_control.modifier_mvp`
- `hesperia.engine.hesperia_control.readonly_guard`
- `hesperia.engine.hesperia_control.unmapped_diagnostics`

### `hesperia/engine/hesperia_control/dominance.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/hesperia_control/modifier_mvp.py`

**from**
- `__future__`
- `hesperia.engine.hesperia_control.readonly_guard`
- `typing`

### `hesperia/engine/hesperia_control/readonly_guard.py`

**import**
- `os`

**from**
- `__future__`
- `pathlib`

### `hesperia/engine/hesperia_control/unmapped_diagnostics.py`

**from**
- `__future__`
- `dataclasses`
- `typing`

### `hesperia/engine/hex_dynamics.py`

**import**
- `dataclasses`
- `numpy`
- `warnings`

**from**
- `__future__`
- `dataclasses`
- `hesperia.engine.energy`
- `hesperia.engine.hex_matrix_builders`
- `hesperia.engine.pch_loader`
- `typing`

### `hesperia/engine/hex_family_bridge.py`

**import**
- `json`
- `numpy`
- `re`

**from**
- `__future__`
- `pathlib`
- `typing`

### `hesperia/engine/hex_matrix_builders.py`

**import**
- `numpy`
- `os`

**from**
- `__future__`
- `core.topology.invariant_catalog`
- `scipy.sparse`
- `typing`

### `hesperia/engine/hex_outputs/__init__.py`

**from**
- `hesperia.engine.hex_outputs.e2e_integration`
- `hesperia.engine.hex_outputs.hex_output_engine`

### `hesperia/engine/hex_outputs/cluster_gravity.py`

**import**
- `numpy`

**from**
- `__future__`

### `hesperia/engine/hex_outputs/contradiction_front.py`

**import**
- `numpy`

**from**
- `__future__`

### `hesperia/engine/hex_outputs/e2e_integration.py`

**import**
- `numpy`

**from**
- `__future__`
- `hesperia.engine.hex_dynamics`
- `hesperia.engine.hex_outputs.hex_output_engine`
- `hesperia.engine.matrix_loader`
- `hesperia.extensions.dynamics.e2e_bridge`
- `hesperia.system.version`
- `pathlib`
- `sphere.topology`
- `sphere.topology.family_embedding`
- `typing`

### `hesperia/engine/hex_outputs/hex_output_engine.py`

**import**
- `numpy`

**from**
- `__future__`
- `dataclasses`
- `hesperia.engine.hex_outputs.cluster_gravity`
- `hesperia.engine.hex_outputs.contradiction_front`
- `hesperia.engine.hex_outputs.hotspot_map`
- `hesperia.engine.hex_outputs.multiscale_consistency`
- `hesperia.engine.hex_outputs.propagation_corridors`
- `hesperia.engine.matrix_loader`
- `typing`

### `hesperia/engine/hex_outputs/hotspot_map.py`

**import**
- `numpy`

**from**
- `__future__`

### `hesperia/engine/hex_outputs/multiscale_consistency.py`

**import**
- `numpy`

**from**
- `__future__`
- `typing`

### `hesperia/engine/hex_outputs/propagation_corridors.py`

**import**
- `numpy`

**from**
- `__future__`

### `hesperia/engine/hex_topology_authority.py`

**import**
- `json`

**from**
- `__future__`
- `core.topology.invariant_catalog`
- `functools`
- `pathlib`
- `typing`

### `hesperia/engine/hspr_index.py`

**import**
- `numpy`

**from**
- `__future__`
- `dataclasses`
- `typing`

### `hesperia/engine/kme/__init__.py`

**from**
- `hesperia.engine.kme.active_graph`
- `hesperia.engine.kme.clinical_bridge`
- `hesperia.engine.kme.derived.calculator`
- `hesperia.engine.kme.extractor`
- `hesperia.engine.kme.fingerprint.builder`
- `hesperia.engine.kme.fingerprint_distance`
- `hesperia.engine.kme.loader`
- `hesperia.engine.kme.models`
- `hesperia.engine.kme.pipeline`
- `hesperia.engine.kme.primitives.calculator`
- `hesperia.engine.kme.profiling.profiler`
- `hesperia.extensions.triz.models`

### `hesperia/engine/kme/active_graph.py`

**from**
- `__future__`
- `hesperia.engine.kme.models`
- `typing`

### `hesperia/engine/kme/bridge.py`

**from**
- `__future__`
- `hesperia.engine.kme.models`

### `hesperia/engine/kme/clinical_bridge.py`

**import**
- `yaml`

**from**
- `__future__`
- `hesperia.engine.kme.active_graph`
- `hesperia.engine.kme.derived.calculator`
- `hesperia.engine.kme.extractor`
- `hesperia.engine.kme.fingerprint.builder`
- `hesperia.engine.kme.models`
- `hesperia.engine.kme.primitives.calculator`
- `hesperia.extensions.triz.kme_bridge`
- `hesperia.nlp.session_parser`
- `hesperia.ontology.dictB.loader`
- `pathlib`
- `sphere.topology.family_embedding`
- `typing`

### `hesperia/engine/kme/derived/__init__.py`

**from**
- `hesperia.engine.kme.derived.calculator`

### `hesperia/engine/kme/derived/calculator.py`

**import**
- `math`

**from**
- `__future__`
- `hesperia.engine.kme.models`
- `typing`

### `hesperia/engine/kme/execution_flow.py`

**from**
- `__future__`
- `hesperia.engine.kme.pipeline`

### `hesperia/engine/kme/extractor.py`

**import**
- `math`

**from**
- `__future__`
- `collections`
- `hesperia.engine.kme.models`
- `typing`

### `hesperia/engine/kme/fingerprint/__init__.py`

**from**
- `hesperia.engine.kme.fingerprint.builder`

### `hesperia/engine/kme/fingerprint/builder.py`

**import**
- `hashlib`
- `math`

**from**
- `__future__`
- `hesperia.engine.kme.models`
- `typing`

### `hesperia/engine/kme/fingerprint_distance.py`

**import**
- `math`

**from**
- `__future__`
- `hesperia.engine.kme.fingerprint.builder`
- `typing`

### `hesperia/engine/kme/loader.py`

**import**
- `json`

**from**
- `__future__`
- `hesperia.engine.kme.models`
- `pathlib`

### `hesperia/engine/kme/models.py`

**from**
- `__future__`
- `dataclasses`

### `hesperia/engine/kme/pipeline.py`

**from**
- `__future__`
- `core.math.io_deterministic_json`
- `hesperia.engine.explainability`
- `hesperia.engine.kme.active_graph`
- `hesperia.engine.kme.derived.calculator`
- `hesperia.engine.kme.fingerprint.builder`
- `hesperia.engine.kme.models`
- `hesperia.engine.kme.primitives.calculator`
- `hesperia.extensions.triz.kme_bridge`
- `pathlib`
- `typing`

### `hesperia/engine/kme/primitives/__init__.py`

**from**
- `hesperia.engine.kme.primitives.calculator`

### `hesperia/engine/kme/primitives/calculator.py`

**import**
- `math`

**from**
- `__future__`
- `collections`
- `hesperia.engine.kme.models`
- `typing`

### `hesperia/engine/kme/profiling/__init__.py`

**from**
- `hesperia.engine.kme.profiling.profiler`

### `hesperia/engine/kme/profiling/profiler.py`

**import**
- `hashlib`
- `math`
- `statistics`

**from**
- `__future__`
- `hesperia.engine.kme.fingerprint.builder`
- `hesperia.engine.kme.models`
- `typing`

### `hesperia/engine/kme/validation/__init__.py`

### `hesperia/engine/language.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/lexical_concept/__init__.py`

**from**
- `hesperia.engine.lexical_concept.pipeline`

### `hesperia/engine/lexical_concept/pipeline.py`

**import**
- `json`
- `math`
- `os`
- `re`
- `yaml`

**from**
- `__future__`
- `collections`
- `core.diagnostics.failures`
- `core.dynamics.constants`
- `core.dynamics.numeric`
- `core.guards.determinism`
- `core.guards.invariants`
- `core.hexmap.aggregate`
- `core.hexmap.analytics`
- `core.hexmap.topology`
- `core.lexical.cooccurrence`
- `core.lexical.matcher`
- `core.lexical.policy`
- `core.output.result_builder`
- `core.pipeline.dynamics`
- `core.pipeline.lexical`
- `core.pipeline.projection`
- `core.pipeline.resolver`
- `core.pipeline.trajectory`
- `core.runtime.engine`
- `core.sequence.segmentation`
- `core.state.semantic_state`
- `hesperia.engine.calibration_dict_paths`
- `hesperia.engine.concept_dictionary.executor`
- `hesperia.engine.engine_signal_calibration`
- `pathlib`
- `typing`

### `hesperia/engine/matrix_loader.py`

**import**
- `json`
- `numpy`
- `os`

**from**
- `__future__`
- `hesperia.system.version`
- `pathlib`
- `typing`

### `hesperia/engine/module_loader.py`

**import**
- `importlib`

**from**
- `__future__`
- `hesperia.modules.registry`
- `typing`

### `hesperia/engine/module_validator.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/multiscale_product_bridge.py`

**import**
- `math`

**from**
- `__future__`
- `core.attribution.structural`
- `core.domain.bridge`
- `core.domain.loader`
- `core.domain.models`
- `core.domain.pipeline`
- `core.layers`
- `core.lexical.analysis_input`
- `hesperia.engine.hex_matrix_builders`
- `hesperia.engine.sealed_multiscale_stack`
- `hesperia.extensions.dynamics.e2e_bridge`
- `hesperia.system.version`
- `pathlib`
- `typing`

### `hesperia/engine/observables.py`

**import**
- `numpy`

**from**
- `__future__`
- `dataclasses`
- `typing`

### `hesperia/engine/output_anomalies.py`

**import**
- `json`

**from**
- `__future__`
- `pathlib`
- `typing`

### `hesperia/engine/output_readout.py`

**import**
- `json`

**from**
- `__future__`
- `functools`
- `pathlib`
- `typing`

### `hesperia/engine/output_trace.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/pch_builder.py`

**import**
- `math`
- `numpy`

**from**
- `__future__`
- `scipy.sparse`
- `typing`

### `hesperia/engine/pch_loader.py`

**import**
- `json`
- `numpy`
- `os`

**from**
- `__future__`
- `hesperia.system.version`
- `pathlib`
- `scipy.sparse`
- `typing`

### `hesperia/engine/pipeline_runner.py`

**import**
- `hashlib`
- `json`
- `yaml`

**from**
- `__future__`
- `hesperia.engine.core`
- `hesperia.engine.validators`
- `pathlib`
- `typing`

### `hesperia/engine/product_signals.py`

**import**
- `math`
- `numpy`

**from**
- `__future__`
- `hesperia.extensions.triz.pipeline`
- `typing`

### `hesperia/engine/projection/__init__.py`

**from**
- `hesperia.engine.projection.public_projection`
- `hesperia.engine.projection.sanitizer`
- `hesperia.engine.projection.schema_enforcer`

### `hesperia/engine/projection/dlcr_public.py`

**from**
- `__future__`
- `typing`

### `hesperia/engine/projection/public_projection.py`

**from**
- `__future__`
- `core.projection`
- `hesperia.engine.projection.schema_enforcer`
- `typing`

### `hesperia/engine/projection/sanitizer.py`

**from**
- `__future__`
- `core.projection.public_projection_layer`
- `typing`

### `hesperia/engine/projection/schema_enforcer.py`

**from**
- `__future__`
- `runtime.shipping.schema_guard`
- `typing`

### `hesperia/engine/release_meta.py`

**from**
- `hesperia.system.version`

### `hesperia/engine/runner.py`

**from**
- `__future__`
- `hesperia.engine.core`
- `pathlib`
- `typing`

### `hesperia/engine/sealed_multiscale_stack.py`

**import**
- `numpy`
- `os`

**from**
- `__future__`
- `hesperia.engine.energy`
- `hesperia.engine.hex_dynamics`
- `hesperia.engine.hex_family_bridge`
- `hesperia.engine.hex_matrix_builders`
- `hesperia.engine.hspr_index`
- `hesperia.engine.lexical_concept.pipeline`
- `hesperia.engine.matrix_loader`
- `hesperia.engine.pch_loader`
- `hesperia.engine.product_signals`
- `hesperia.extensions.dynamics.e2e_bridge`
- `hesperia.system.version`
- `pathlib`
- `typing`

### `hesperia/engine/tfp_math.py`

**import**
- `math`
- `re`

**from**
- `__future__`
- `typing`

### `hesperia/engine/tfp_signal_calibration.py`

**import**
- `json`
- `math`

**from**
- `__future__`
- `functools`
- `pathlib`
- `typing`

### `hesperia/engine/validators.py`

**import**
- `math`

**from**
- `__future__`
- `typing`

