# Grace — Hesperia v0.5.6+ visualization of outputs (Ethan deliverable — record)

**Status:** Documented as **product baseline** for Hesperia **v0.5.6 and above** to visualize engine outputs (not a generic “team foundation”).  
**Canonical spec:** **`/data/hesperia/hesperia/docs/VISUALIZATION_OUTPUTS_v0_5_6_AND_ABOVE.md`** (Hesperia repo).

---

## Cross-reference (mirror paths — cursor brain)

Static viewers and bundled `outputs/inspection/*.json` examples also live under this repo’s `hesperia/` tree for LAN serve; engine producers remain on `/data/hesperia/hesperia`.

| Layer | Cursor path |
|--------|-------------|
| Session trace viewer (D3) | `hesperia/tools/inspection_viewer/` |
| Substrate map viewer | `hesperia/tools/substrate_viewer/` |
| Area↔family viewer | `hesperia/tools/area_family_viewer/` |
| LAN helper | `hesperia/serve_viewer.sh` |
| Systemd (prichindel) | `cluster/prichindel/systemd/hesperia-inspection-viewer.service` |

Ethan task notes (historical): `operational/assignments/reports/HESPERIA-D3-VIEWER-v056-ETHAN-INTEGRATION-2026-03-30.md`.

---

## LAN URLs (default :8765)

- `http://192.168.100.21:8765/tools/inspection_viewer/index.html`
- `http://192.168.100.21:8765/tools/substrate_viewer/index.html`
- `http://192.168.100.21:8765/tools/area_family_viewer/index.html`

---

## Conclusion

The visualization stack is **version-scoped to the Hesperia product line (v0.5.6+)**: it exposes **outputs** (trace JSON, substrate JSON) and **read-only** browser views. Extensions belong in the same contract: engine emits truth, UI renders it. Full regeneration commands, contracts, and product conclusion are in **`docs/VISUALIZATION_OUTPUTS_v0_5_6_AND_ABOVE.md`** on the Hesperia repo.

---

SIGNED: Triage (Grace) | Hesperia v0.5.6+ visualization baseline — pointer to canonical doc | 2026-03-30 | `/data/hesperia/hesperia/docs/VISUALIZATION_OUTPUTS_v0_5_6_AND_ABOVE.md`
