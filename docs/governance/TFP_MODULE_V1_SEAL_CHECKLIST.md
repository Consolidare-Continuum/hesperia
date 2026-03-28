# TFP module v1 — seal checklist and handoff

**TFP-V1-15 (Ethan):** Execute before declaring **module v1 sealed** and moving team default to **dict/calibration-only** edits.

## Checklist

- [ ] All **TFP-V1-01 … TFP-V1-14** deliverables merged on `main` (Hesperia).
- [ ] [`TFP_MODULE_V1_RELEASE.md`](TFP_MODULE_V1_RELEASE.md) chain green on a full checkout (version → wave → phase-C smoke → module pytest).
- [ ] `VERSION.yaml` / `hesperia/VERSION.yaml`: set `tfp_module_v1.seal_requested: true` when leadership freezes module code.
- [ ] **Git tag (convention):** `tfp-module-v1` or `tfp-module-v1-YYYY-MM-DD` on the sealing commit (operator push).
- [ ] **Brain repo `active.md`:** TFP-V1-* rows → **DONE** with Hesperia commit SHA.
- [ ] Post-seal: new module features only with **new Grace row**; ongoing work = `assets/calibration/dicts/**`, `concept_dict`, links/metrics JSONL, wave scripts, validators.

## Seal hook

- Operators may set `HESPERIA_TFP_MODULE_SEALED=1` (warn) or `block` (hard fail on `TFPModule.project`) per [`TFP_ENV_FLAGS_V1.md`](TFP_ENV_FLAGS_V1.md).

`SIGNED: Ethan (seal handoff) | TFP module v1 | 2026-03-28 | TFP-V1-15`
