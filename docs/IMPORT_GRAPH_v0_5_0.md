<!--
  HESPERIA — Generated file. Regenerate:
    python3 tools/gen_import_graph_doc.py --write
  CI drift check:
    python3 tools/gen_import_graph_doc.py | diff -q docs/IMPORT_GRAPH_v0_5_0.md -
-->

# Import graph — public runtime & services (v0.5.0 seal baseline)

This document lists **static** `import` / `from` targets seen under the scanned trees. It is a **drift detector**: unexpected new edges often mean a boundary or layering mistake.

## Scanned directories

- `runtime/api/`
- `runtime/pipeline/`
- `runtime/public_reports/`
- `runtime/artifact_writer/`
- `runtime/runners/`
- `runtime/shipping/`
- `runtime/services/`

## Excluded files (see `tools/check_import_boundary.py`)

- `runtime/pipeline/analyze.py`
- `runtime/pipeline/batch_runner.py`
- `runtime/pipeline/r1_r4_pipeline.py`
- `runtime/pipeline/reading_scales.py`
- `runtime/pipeline/run_corpus_benchmark.py`

## Forbidden targets (must never appear in scanned public-runtime files)

Enforced by `python3 tools/check_import_boundary.py`.

### Prefixes

- `core.math.*`
- `core.domain.bridge*`
- `core.topology.invariant_catalog*`
- `sphere.pipeline.pipeline_runner*`
- `sphere.pipeline.layer_registry*`
- `sphere.pipeline.pipeline_state*`

### Module aliases

- `core.attribution.structural`
- `core.contracts.layer_contract`
- `core.layers`
- `core.policy`
- `core.stability`

## Aggregate import targets (reference count)

- `__future__` — **22**
- `argparse` — **11**
- `collections` — **1**
- `core.projection` — **1**
- `datetime` — **3**
- `fastapi` — **3**
- `fastapi.exceptions` — **1**
- `fastapi.middleware.cors` — **1**
- `fastapi.openapi.utils` — **1**
- `fastapi.responses` — **3**
- `fastapi.security` — **2**
- `hashlib` — **2**
- `hesperia.engine.hex_outputs.e2e_integration` — **1**
- `hesperia.engine.kme.clinical_bridge` — **1**
- `hesperia.engine.kme.models` — **1**
- `hesperia.engine.kme.pipeline` — **1**
- `hesperia.engine.multiscale_product_bridge` — **1**
- `hesperia.engine.projection` — **2**
- `hesperia.engine.sealed_multiscale_stack` — **1**
- `hesperia.experiments.experiment_runner` — **1**
- `hesperia.extensions.dynamics.calibration` — **1**
- `hesperia.extensions.dynamics.e2e_bridge` — **1**
- `hesperia.extensions.triz.commercial_intelligence` — **1**
- `hesperia.extensions.triz.pipeline` — **3**
- `hesperia.nlp.session_parser` — **1**
- `hesperia.product.api_contracts.triz_analysis_v1` — **1**
- `hesperia.product.api_contracts.triz_compare_v1` — **1**
- `hesperia.product.api_contracts.triz_export_v1` — **1**
- `hesperia.product.comparison_engine` — **1**
- `hesperia.product.mvp_acceptance` — **1**
- `hesperia.product.package_builder` — **1**
- `hesperia.system.capabilities` — **2**
- `hesperia.system.system_seal` — **2**
- `hesperia.system.version` — **7**
- `json` — **14**
- `logging` — **1**
- `os` — **11**
- `pathlib` — **20**
- `pydantic` — **2**
- `research.clinical_tfp.interpretation` — **1**
- `research.clinical_tfp.session_topology` — **1**
- `research.clinical_tfp.stage_detection` — **1**
- `runtime.api.main` — **1**
- `runtime.api.triz_mvp_v1` — **1**
- `runtime.artifact_writer` — **8**
- `runtime.artifact_writer.writer` — **1**
- `runtime.dossier` — **1**
- `runtime.dossier.index_manager` — **1**
- `runtime.pipeline` — **1**
- `runtime.pipeline.analyze` — **2**
- `runtime.pipeline.batch_runner` — **1**
- `runtime.pipeline.r1_r4_pipeline` — **2**
- `runtime.pipeline.reading_scales` — **1**
- `runtime.pipeline.run_e2e_all` — **1**
- `runtime.pipeline.run_l1_through_l9` — **1**
- `runtime.provenance` — **1**
- `runtime.public_reports.public_manifest_writer` — **1**
- `runtime.semantic_field.run_field_calibration` — **1**
- `runtime.semantic_field.run_semantic_field` — **1**
- `runtime.services.analysis_service` — **13**
- `runtime.shipping.cli_main` — **1**
- `runtime.shipping.env_guard` — **1**
- `runtime.shipping.license_check` — **1**
- `runtime.shipping.schema_guard` — **6**
- `runtime.shipping.schema_integrity` — **1**
- `runtime.shipping.version_info` — **2**
- `sphere.topology.activation_propagation` — **1**
- `sphere.topology.family_embedding` — **1**
- `subprocess` — **1**
- `sys` — **14**
- `tempfile` — **1**
- `time` — **2**
- `typing` — **8**
- `uuid` — **2**
- `uvicorn` — **1**

## Per-file edges (sorted by path)

### `runtime/api/__init__.py`

### `runtime/api/main.py`

**import**
- `logging`
- `os`
- `time`
- `uuid`

**from**
- `__future__`
- `fastapi`
- `fastapi.exceptions`
- `fastapi.middleware.cors`
- `fastapi.openapi.utils`
- `fastapi.responses`
- `fastapi.security`
- `hesperia.extensions.triz.pipeline`
- `hesperia.system.capabilities`
- `hesperia.system.version`
- `pathlib`
- `pydantic`
- `runtime.api.triz_mvp_v1`
- `runtime.services.analysis_service`
- `runtime.shipping.schema_guard`
- `typing`

### `runtime/api/triz_mvp_v1.py`

**import**
- `os`

**from**
- `__future__`
- `fastapi`
- `fastapi.responses`
- `fastapi.security`
- `hesperia.extensions.triz.commercial_intelligence`
- `hesperia.extensions.triz.pipeline`
- `hesperia.product.api_contracts.triz_analysis_v1`
- `hesperia.product.api_contracts.triz_compare_v1`
- `hesperia.product.api_contracts.triz_export_v1`
- `hesperia.product.comparison_engine`
- `hesperia.product.package_builder`
- `runtime.api.main`
- `typing`

### `runtime/artifact_writer/__init__.py`

**from**
- `runtime.artifact_writer.writer`

### `runtime/artifact_writer/writer.py`

**import**
- `json`
- `os`

**from**
- `__future__`
- `hesperia.engine.projection`
- `hesperia.system.version`
- `pathlib`
- `runtime.shipping.schema_guard`
- `typing`

### `runtime/pipeline/__init__.py`

### `runtime/pipeline/run_e2e_all.py`

**import**
- `argparse`
- `json`
- `os`
- `sys`
- `tempfile`
- `uuid`

**from**
- `__future__`
- `collections`
- `core.projection`
- `hesperia.engine.hex_outputs.e2e_integration`
- `hesperia.engine.kme.clinical_bridge`
- `hesperia.engine.kme.models`
- `hesperia.engine.kme.pipeline`
- `hesperia.engine.sealed_multiscale_stack`
- `hesperia.experiments.experiment_runner`
- `hesperia.extensions.dynamics.calibration`
- `hesperia.extensions.dynamics.e2e_bridge`
- `hesperia.extensions.triz.pipeline`
- `hesperia.nlp.session_parser`
- `hesperia.product.mvp_acceptance`
- `hesperia.system.version`
- `pathlib`
- `research.clinical_tfp.interpretation`
- `research.clinical_tfp.session_topology`
- `research.clinical_tfp.stage_detection`
- `runtime.artifact_writer`
- `runtime.pipeline`
- `runtime.pipeline.analyze`
- `runtime.pipeline.batch_runner`
- `runtime.pipeline.r1_r4_pipeline`
- `runtime.pipeline.reading_scales`
- `runtime.pipeline.run_l1_through_l9`
- `runtime.semantic_field.run_field_calibration`
- `runtime.semantic_field.run_semantic_field`
- `runtime.services.analysis_service`
- `sphere.topology.activation_propagation`
- `sphere.topology.family_embedding`
- `typing`

### `runtime/pipeline/run_e2e_full_stack.py`

**import**
- `argparse`
- `hashlib`
- `json`
- `os`
- `subprocess`
- `sys`

**from**
- `__future__`
- `datetime`
- `hesperia.system.system_seal`
- `hesperia.system.version`
- `pathlib`
- `runtime.pipeline.run_e2e_all`
- `runtime.services.analysis_service`
- `runtime.shipping.schema_guard`
- `typing`

### `runtime/pipeline/run_e2e_product.py`

**import**
- `json`
- `os`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.services.analysis_service`
- `runtime.shipping.schema_guard`

### `runtime/pipeline/run_e2e_sentence.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.pipeline.analyze`

### `runtime/pipeline/run_l1_l2.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.services.analysis_service`

### `runtime/pipeline/run_l1_l2_l3.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.services.analysis_service`

### `runtime/pipeline/run_l1_through_l9.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.dossier`
- `runtime.dossier.index_manager`
- `runtime.provenance`
- `runtime.services.analysis_service`

### `runtime/pipeline/run_r1_r4_pipeline.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.pipeline.r1_r4_pipeline`

### `runtime/pipeline/run_sphere_math_100_sentences.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.services.analysis_service`

### `runtime/pipeline/run_sphere_math_values.py`

**import**
- `argparse`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.services.analysis_service`

### `runtime/public_reports/__init__.py`

**from**
- `runtime.public_reports.public_manifest_writer`

### `runtime/public_reports/public_manifest_writer.py`

**import**
- `json`

**from**
- `__future__`
- `datetime`
- `pathlib`
- `typing`

### `runtime/runners/__init__.py`

### `runtime/runners/run_reference_pipeline.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.services.analysis_service`

### `runtime/services/__init__.py`

**from**
- `runtime.services.analysis_service`

### `runtime/services/analysis_service.py`

**from**
- `__future__`
- `hesperia.engine.multiscale_product_bridge`
- `hesperia.engine.projection`
- `hesperia.system.version`
- `pathlib`
- `typing`

### `runtime/shipping/__init__.py`

**from**
- `runtime.shipping.cli_main`

### `runtime/shipping/api_main.py`

**import**
- `os`
- `sys`
- `time`
- `uvicorn`

**from**
- `__future__`
- `fastapi`
- `fastapi.responses`
- `hesperia.system.capabilities`
- `hesperia.system.system_seal`
- `hesperia.system.version`
- `pathlib`
- `pydantic`
- `runtime.services.analysis_service`
- `runtime.shipping.env_guard`
- `runtime.shipping.license_check`
- `runtime.shipping.schema_guard`
- `runtime.shipping.schema_integrity`
- `runtime.shipping.version_info`
- `typing`

### `runtime/shipping/cli_main.py`

**import**
- `argparse`
- `json`
- `sys`

**from**
- `__future__`
- `hesperia.system.version`
- `pathlib`
- `runtime.artifact_writer`
- `runtime.services.analysis_service`
- `runtime.shipping.schema_guard`
- `runtime.shipping.version_info`

### `runtime/shipping/env_guard.py`

**import**
- `os`
- `sys`

**from**
- `__future__`

### `runtime/shipping/license_check.py`

**import**
- `os`

**from**
- `__future__`
- `datetime`
- `pathlib`

### `runtime/shipping/schema_guard.py`

**import**
- `json`
- `os`

**from**
- `__future__`
- `pathlib`

### `runtime/shipping/schema_integrity.py`

**import**
- `hashlib`
- `os`

**from**
- `__future__`
- `pathlib`

### `runtime/shipping/version_info.py`

