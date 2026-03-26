# Hesperia Engine Dynamics — Release Notes **v0.5.0**

**Tags:** `v0.5.0` · `hesperia-engine-dynamics-v0.5.0` (same commit; use the product tag for the GitHub Release title if you prefer.)

**Sealed audit:** `release/v0.5.0/` — `final_gate_status.json` → `sealed: true`, full pytest, schema + determinism reports (build timestamp used for seal: **2026-03-19T12:00:00Z**).

---

## Summary

**v0.5.0** is the canonical **Engine Dynamics** release: a **deterministic** structural inspection / placement stack with **sealed public projection** — **concept → hex → family → area → product signals → HSPR** — plus auditable build metadata and E2E proof artifacts.

This is **not** a claim of generative truth, clinical certification, or an unconstrained research distribution.

---

## Highlights

- **Hex layer:** Microphysics (`hex_dynamics`), hex→family bridge (`hex_family_bridge`), hex outputs, topology weights (`data/topology/hex_family_weights.json`).
- **Sealed multiscale stack:** `hesperia.engine.sealed_multiscale_stack` — one-shot chain to family/area activations, **product signals**, and **HSPR** system scalar.
- **Supporting modules:** `observables`, `product_signals`, `hspr_index`; normative specs under `specs/` (canon, dynamics, calibration, schema).
- **E2E baseline:** `python3 -m runtime.execution_flow.run_e2e_all` produces **19** reference JSON artifacts (**20** with `HESPERIA_FIELD_DYNAMICS=1`). See `docs/E2E_RUN_ORDER.md`, `assets/artifacts/e2e/E2E_OUTPUTS.md`.
- **Public API (shipping):** `POST /analyze`, `/compare`, `/batch` (alias `/batch-analyze`), `GET /health`; responses go through **projection** (`runtime/services/analysis_service.py`). OpenAPI/docs **off** on the shipping app by default.
- **Version authority:** `pyproject.toml`, `hesperia.__version__`, `VERSION.yaml`, and OpenAPI product version aligned at **0.5.0**.

---

## Release audit & tooling

- **Audit driver:** `tools/release/build_release_audit_v0_5_0.py` (use **full** run, not `--quick`, before tagging).
- **Git hygiene:** Audit snapshots **clean worktree before** writing under `release/v0.5.0/` (fix landed in `fix(release): snapshot git dirty before writing release/v0.5.0 artifacts`).
- **CI — Sealed runtime gate:** `fix(ci): sealing scan — word-boundary 3D, skip v0.5.0 audit + triz_demo` aligns `tools/sealing_scan.py` with audit JSON (hex hashes) and non-shipping demos so **GitHub Actions** stays green on `main`.

---

## Out of scope for the v0.5 product definition

- **TFP / clinical experimental** trees (e.g. `research/clinical_tfp/`) and TFP-heavy testing collateral — not the minimal Engine Dynamics spec core.
- **`legacy/`** — archival only.
- **TRIZ HTTP** — optional; not on the minimal product surface by default.

---

## Verify locally

```bash
python3 -m runtime.execution_flow.run_e2e_all
pytest tests/test_e2e_flows.py -v
```

Full seal (maintainers):

```bash
export HESPERIA_RELEASE_BUILD_TIMESTAMP=2026-03-19T12:00:00Z
python3 tools/release/build_release_audit_v0_5_0.py
```

---

## Documentation

| Doc | Purpose |
|-----|---------|
| `docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md` | Master index (spec ↔ engine ↔ E2E) |
| `specs/release/releases/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md` | Canonical release narrative |
| `CHANGELOG.md` | Version history |
| `docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md` | Naming vocabulary |
| `release/v0.5.0/README.md` | Audit package layout & regeneration |

---

## License

Restricted Research Disclosure License — inspection and reference only. See **LEGAL_NOTICE.md**.

---

*Hesperia Engine Dynamics v0.5.0 — sealed multiscale semantic physics.*
