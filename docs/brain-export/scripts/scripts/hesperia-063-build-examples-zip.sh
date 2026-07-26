#!/usr/bin/env bash
# Add 0.6.3 example outputs to hesperia release and build zip in brain repo root.
set -euo pipefail
HES="${HES_ROOT:-/data/workspaces/atomic-commit-hesperia}"
BRAIN="${BRAIN_ROOT:-/data/altitudine/prichindel.com}"
EX="$HES/release/v0.6.3/examples"
mkdir -p "$EX"

cd "$HES"
export HESPERIA_DICT_CALIB_OFFLINE=1
PY="${HES}/.venv/bin/python"

# 1) Real analyze + API output (fixture text, offline — no prod corpus)
"$PY" << 'PY' > "$EX/example_analyze_shipping_output.json"
import json
from runtime.pipeline.analyze import analyze
from hesperia.engine.api import run_engine_api_v1

text_ru = (
    "Агрессия в семейной системе снижает способность к саморегуляции "
    "и усиливает защитные механизмы при нарушении границ."
)
minimal, extended = analyze(text_ru, r1_r4=False)
api = run_engine_api_v1(text_ru)
print(json.dumps({
    "_comment": "Example POST /analyze style result (offline fixture dict). Out of context demo.",
    "lang": "ru",
    "input": {"text_ru": text_ru, "kind": "tfp_scientific_statement"},
    "minimal": minimal,
    "extended_summary": {
        "family_vector_len": len((extended or {}).get("family_vector") or []),
        "dict_b_keys": sorted((extended or {}).get("dict_b") or {})[:8],
        "matched_tokens": (extended or {}).get("matched_tokens"),
    },
    "engine_api_v1": api,
}, ensure_ascii=False, indent=2))
PY

# 2) 0.6.3 envelope (illustrative, aligned to tersagor schema)
cat > "$EX/example_engine_run_envelope_v063.json" << 'EOF'
{
  "_comment": "IRC ENGINE_ENVELOPE trace payload — operator full view. Demo IDs only.",
  "schema": "hesperia.engine_run_envelope.v063",
  "lang": "ru",
  "correlation_id": "cid-demo-063-001",
  "run_id": "550e8400-e29b-41d4-a716-446655440000",
  "input": {
    "text_ru": "Агрессия в семейной системе снижает способность к саморегуляции.",
    "kind": "tfp_scientific_statement"
  },
  "engine": {
    "hesperia_ref": "16286fa",
    "tersagor_ref": "0149120",
    "propagation_trace": [
      {"hop": 0, "concept": "AGGRESSION", "area_id": "A09", "activation": 0.72},
      {"hop": 1, "concept": "SELF_REGULATION", "area_id": "A04", "activation": 0.31}
    ],
    "areas": {"A09": 0.41, "A04": 0.22},
    "families": {"F228": 0.38, "F105": 0.19},
    "corpus_activations": [
      {"concept_id": "AGGRESSION", "observed": 0.72, "expected": 0.85},
      {"concept_id": "SHAME", "observed": 0.28, "expected": 0.55}
    ],
    "roads": [
      {"hop": 0, "concept": "AGGRESSION"},
      {"gtp_path_ids": ["hex-path-demo-1", "hex-path-demo-2"]}
    ],
    "interior_pov": {"step": 1, "surface": "family_boundary"},
    "gtp_coherence": {"path_ids": ["hex-path-demo-1"], "psi": 0.67}
  },
  "ksi": {
    "version": "0.1",
    "incidents": [
      {"type": "residual_high", "concept_id": "SHAME", "residual": -0.27}
    ],
    "missing_bridges": [
      {"source": "AGGRESSION", "target": "SELF_REGULATION", "need_score": 0.81}
    ],
    "phi_trace": {
      "AGGRESSION->SELF_REGULATION": {"W_e": 0.12, "R_e": 0.4, "phi_sat": 0.05}
    }
  },
  "parameters": {
    "W_e": [
      {"edge": "AGGRESSION->SELF_REGULATION", "W_e": 0.12, "R_e": 0.4}
    ],
    "ksi_config_ref": "assets/data/ksi/ksi_config_v01.json"
  }
}
EOF

# 3) Teacher response (values only)
cat > "$EX/example_teacher_response_v063.json" << 'EOF'
{
  "_comment": "OpenAI Teacher output — proposals only, no justification/message.",
  "schema": "hesperia.teacher_response.v063",
  "lang": "ru",
  "proposals": [
    {
      "action": "update_edge_weight",
      "source": "AGGRESSION",
      "target": "SELF_REGULATION",
      "W_e_current": 0.12,
      "W_e_proposed": 0.58,
      "confidence": 0.84
    },
    {
      "action": "update_cd_field",
      "concept_id": "SHAME",
      "field": "expected_activation",
      "value_current": 0.55,
      "value_proposed": 0.48,
      "confidence": 0.71
    }
  ]
}
EOF

# 4) Reweight preview
cat > "$EX/example_reweight_preview.json" << 'EOF'
{
  "_comment": "REWEIGHT_PREVIEW IRC message body — applied=0 until 0.7.0 sandbox.",
  "correlation_id": "cid-demo-063-001",
  "preview": [
    {
      "parameter_key": "W_e:AGGRESSION->SELF_REGULATION",
      "value_before": 0.12,
      "value_after": 0.58,
      "applied": 0
    },
    {
      "parameter_key": "SHAME.expected_activation",
      "value_before": 0.55,
      "value_after": 0.48,
      "applied": 0
    }
  ]
}
EOF

# 5) IRC trace JSONL (chunked demo)
cat > "$EX/example_irc_trace.jsonl" << 'EOF'
{"ts":"2026-06-14T13:00:00+00:00","channel":"#hesperia-teacher","type":"RUN_START","payload":{"correlation_id":"cid-demo-063-001","run_id":"550e8400-e29b-41d4-a716-446655440000","lang":"ru"}}
{"ts":"2026-06-14T13:00:01+00:00","channel":"#hesperia-teacher","type":"ENGINE_ENVELOPE","payload":{"correlation_id":"cid-demo-063-001","schema":"hesperia.engine_run_envelope.v063","input":{"text_ru":"Агрессия в семейной системе…","kind":"tfp_scientific_statement"}}}
{"ts":"2026-06-14T13:00:02+00:00","channel":"#hesperia-teacher","type":"TEACHER_REQUEST","payload":{"correlation_id":"cid-demo-063-001","incidents":[{"type":"residual_high","concept_id":"SHAME"}]}}
{"ts":"2026-06-14T13:00:03+00:00","channel":"#hesperia-teacher","type":"TEACHER_RESPONSE","payload":{"schema":"hesperia.teacher_response.v063","proposals":[{"action":"update_edge_weight","confidence":0.84}]}}
{"ts":"2026-06-14T13:00:03+00:00","channel":"#hesperia-teacher","type":"REWEIGHT_PREVIEW","payload":{"correlation_id":"cid-demo-063-001","preview":[{"parameter_key":"W_e:AGGRESSION->SELF_REGULATION","applied":0}]}}
{"ts":"2026-06-14T13:00:04+00:00","channel":"#hesperia-teacher","type":"RUN_DONE","payload":{"correlation_id":"cid-demo-063-001","run_id":"550e8400-e29b-41d4-a716-446655440000","status":"stored"}}
EOF

# 6) MySQL row shape (not a live DB dump)
cat > "$EX/example_mysql_teacher_run_row.json" << 'EOF'
{
  "_comment": "Shape of hesperia.hesperia_teacher_run after persist_teach_run()",
  "run_id": "550e8400-e29b-41d4-a716-446655440000",
  "correlation_id": "cid-demo-063-001",
  "lang": "ru",
  "input_kind": "tfp_scientific_statement",
  "status": "stored",
  "irc_channel": "#hesperia-teacher",
  "hesperia_git_sha": "16286fa",
  "tersagor_git_sha": "0149120",
  "proposal_status": "pending",
  "tables_touched": [
    "hesperia_teacher_run",
    "hesperia_edge_snapshot",
    "hesperia_activation_snapshot",
    "hesperia_proposal",
    "hesperia_reweight_event"
  ]
}
EOF

# 7) Index
cat > "$EX/README.md" << 'EOF'
# Hesperia 0.6.3 — example outputs

Out-of-context demonstration artifacts. Safe for public archive; not live patient data.

| File | What it shows |
|------|----------------|
| `example_analyze_shipping_output.json` | Engine `/analyze` minimal + API v1 envelope (offline fixture) |
| `example_engine_run_envelope_v063.json` | Full IRC `ENGINE_ENVELOPE` for 0.6.3 Teacher run |
| `example_teacher_response_v063.json` | OpenAI Teacher strict JSON — numeric proposals only |
| `example_reweight_preview.json` | Scalar deltas before graph apply (`applied=0`) |
| `example_irc_trace.jsonl` | Lounge-visible trace sequence RUN_START → RUN_DONE |
| `example_mysql_teacher_run_row.json` | MySQL ledger row shape after persist |

**Live path:** tersagor `0149120` + `TERSAGOR_HESPERIA_IRC_TEACHER=1` → writes real rows; these files are reference only.
EOF

cat > "$HES/release/v0.6.3/output_inventory.json" << 'EOF'
{
  "version": "0.6.3",
  "examples_dir": "release/v0.6.3/examples/",
  "artifacts": [
    "example_analyze_shipping_output.json",
    "example_engine_run_envelope_v063.json",
    "example_teacher_response_v063.json",
    "example_reweight_preview.json",
    "example_irc_trace.jsonl",
    "example_mysql_teacher_run_row.json"
  ]
}
EOF

./tools/build_063_github_archive.sh
OUT_ZIP="$HES/dist/hesperia-0.6.3-archive.zip"
BRAIN_ZIP="$BRAIN/hesperia-0.6.3-archive.zip"
mkdir -p "$BRAIN"
cp -f "$OUT_ZIP" "$BRAIN_ZIP"
( cd "$BRAIN" && sha256sum "$(basename "$BRAIN_ZIP")" > hesperia-0.6.3-archive.SHA256SUMS.txt )
echo "Brain zip: $BRAIN_ZIP"
ls -lh "$BRAIN_ZIP" "$BRAIN/hesperia-0.6.3-archive.SHA256SUMS.txt"
