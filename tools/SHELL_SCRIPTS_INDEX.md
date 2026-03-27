# `tools/*.sh` index

One-line purpose + where to read more. Run from **Hesperia repo root** unless noted.

| Script | Purpose | Doc / context |
|--------|---------|-----------------|
| `tools/run_dict_release_gates.sh` | Version check + conditional B+CD wave (if `dict_a.jsonl` present) | [`docs/governance/working/RUNBOOK-DICT-RELEASE-GATES.md`](../docs/governance/working/RUNBOOK-DICT-RELEASE-GATES.md) |
| `tools/run_b_cd_wave_after_a.sh` | Validators + CD pytest + smoke after lexical A green | [`docs/HESPERIA_TFP_MODULE_DICTS.md`](../docs/HESPERIA_TFP_MODULE_DICTS.md), `CHANGELOG.md` |
| `tools/sync_tfp_module_data.sh` | Sync TFP module / calibration assets | [`docs/HESPERIA_TFP_MODULE_DICTS.md`](../docs/HESPERIA_TFP_MODULE_DICTS.md) |
| `tools/run_dict_calibration_clearance.sh` | Dict calibration clearance pipeline | [`tools/dict_calibration/README.md`](dict_calibration/README.md) |
| `tools/run_dict_calibration_phases_a_d.sh` | Phases A–D calibration driver | [`tools/dict_calibration/README.md`](dict_calibration/README.md) |
| `tools/run_openai_calibration_t1_bundle_batches.sh` | OpenAI calibration T1 batches | header in script |
| `tools/run_openai_calibration_t2_openai_batches.sh` | OpenAI calibration T2 batches | header in script |
| `tools/diagnostics/verify_surface_map_checksum.sh` | Surface map checksum verify | header in script |
| `tools/e2e_full_deliverables.sh` | Full E2E stack + manifest (physics, seal, product JSON) | header in script; `docs/E2E_RUN_ORDER.md` |
| `tools/release/run_release_reference.sh` | Release reference run helper | `release/README.md` |
| `tools/build_nuitka_cli.sh` | Nuitka CLI build | header in script |
| `tools/run_release_gate.sh` | Local release gate wrapper | `docs/governance/SEALED_RUNTIME_RELEASE_GATE_v1.md` |
| `tools/sync_backup_to_remotes.sh` | Push backups to remotes | internal ops |
| `tools/backup_hesperia_full.sh` | Full repo backup archive | internal ops |
| `tools/detect_unused.sh` | Vulture / orphan hints (no auto-delete) | header in script |
| `tools/push_mirrors.sh` | Git mirror push helper | header in script |

---

*GAP-WIRE-07: reduce orphan `*.sh` discoverability gap.*
