# Production interaction matrices (governed)

Versioned NumPy bundles for **L_F** (family Laplacian), **C_F** (contradiction), **R_F** (diagonal resistance).

- **Manifest:** `matrix_manifest.json` — must align with `VERSION.yaml` → `matrices.production_bundle`.
- **Regenerate:** from repo root, `python3 tools/matrices/build_production_matrices_v1.py`
- **Override path (tests / ops):** `HESPERIA_PRODUCTION_MATRICES_DIR`

Runtime load: `hesperia.engine.matrix_loader.load_production_matrices`. Stub builders in
`semantic_field_v1` are **disabled** unless `HESPERIA_SEMANTIC_FIELD_STUB_MATRICES=1`.
