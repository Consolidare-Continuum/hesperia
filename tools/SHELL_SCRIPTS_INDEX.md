# `tools/*.sh` index

One-line purpose + where to read more. Run from **Hesperia repo root** unless noted.

| Script | Purpose | Doc / context |
|--------|---------|-----------------|
| `tools/run_dict_release_gates.sh` | Version check + conditional B+CD wave (if `dict_a.jsonl` present) | [`docs/governance/working/RUNBOOK-DICT-RELEASE-GATES.md`](../docs/governance/working/RUNBOOK-DICT-RELEASE-GATES.md) |
| `tools/run_b_cd_wave_after_a.sh` | Validators + CD pytest + smoke after lexical A green | [`docs/HESPERIA_TFP_MODULE_DICTS.md`](../docs/HESPERIA_TFP_MODULE_DICTS.md), `CHANGELOG.md` |
| `tools/sync_tfp_module_data.sh` | Refresh `tfp_v1/` dict faces from `assets/` (no `research/`) | [`hesperia/modules/tfp/data/README.md`](../hesperia/modules/tfp/data/README.md) |
| `tools/migrate_research_tfp_to_module_tfp_v1.sh` | One-shot legacy noone corpus + calibration pack → `tfp_v1/` | [`docs/governance/working/ETHAN-TFP-MODULE-ONLY-DICT-SSOT-2026-03-28.md`](../docs/governance/working/ETHAN-TFP-MODULE-ONLY-DICT-SSOT-2026-03-28.md) |
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
| `tools/mirror_sister_workflows_into_hesperia_data.sh` | Rsync `/data/workflows` (or `WORKFLOWS_SRC`) → `/data/hesperia/workflows-mirror/` for cold recovery | [`docs/governance/working/GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md`](../docs/governance/working/GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md) |
| `tools/detect_unused.sh` | Vulture / orphan hints (no auto-delete) | header in script |
| `tools/push_mirrors.sh` | Git mirror push helper | header in script |

## Python (`tools/*.py`)

| Script | Purpose | Doc / context |
|--------|---------|---------------|
| `tools/copy_dict_calibration_provenance_to_tfp_v1.py` | Mirror `outputs/dict_calibration/**` → `tfp_v1/provenance/api/runs/outputs_dict_calibration_mirror/` + write `COPY_MANIFEST_DICT_CALIBRATION.json` | [`hesperia/modules/tfp/data/tfp_v1/provenance/api/README.md`](../hesperia/modules/tfp/data/tfp_v1/provenance/api/README.md) |

---

*GAP-WIRE-07: reduce orphan `*.sh` discoverability gap.*
