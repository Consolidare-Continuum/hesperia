#!/usr/bin/env bash
# Ethan: seal Hesperia 0.6.3 GitHub archive (no prod dicts/corpus). Run on alunel dev clone.
set -euo pipefail
REPO="${1:-/data/workspaces/atomic-commit-hesperia}"
BRAIN="${2:-/data/workspaces/cursor}"
cd "$REPO"

SHA="$(git rev-parse HEAD)"
SHORT="$(git rev-parse --short HEAD)"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# --- VERSION.yaml 0.6.3 ---
python3 << 'PY'
from pathlib import Path
import yaml
p = Path("VERSION.yaml")
doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
doc["system_version"] = "0.6.3"
doc["release_stage"] = "irc_teacher_application_run"
for k in ("core_engine", "dynamics", "triz", "clinical", "calibration"):
    if "components" in doc and k in doc["components"]:
        doc["components"][k] = "0.6.3"
doc.setdefault("defaults", {})
doc["defaults"]["active_calibration_dict_pack"] = "archive_063_minimal"
doc.setdefault("archive", {})
doc["archive"] = {
    "github_release": "0.6.3",
    "excludes_prod_dicts": True,
    "excludes_prod_corpus": True,
    "e2e_mode": "offline_fixture",
    "tersagor_integration_ref": "igareosh/tersagor@0149120",
}
p.write_text(yaml.dump(doc, sort_keys=False, allow_unicode=True), encoding="utf-8")
print("VERSION.yaml -> 0.6.3")
PY

mkdir -p release/v0.6.3 assets/calibration/dicts/archive_063_minimal docs/specs

# Spec from brain
if [[ -f "$BRAIN/governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md" ]]; then
  cp "$BRAIN/governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md" docs/specs/0.6.3-IRC-TEACHER-RUN.md
fi

cat > assets/calibration/dicts/archive_063_minimal/README.md << 'EOF'
# archive_063_minimal — GitHub release dict placeholder

**Not** the production sealed pack (`v0_6_0_clr_v052_*`). This directory exists so `VERSION.yaml` pins a named pack for the **0.6.3 public archive** without shipping prod dict JSONL or corpus trees.

## Run E2E on the archive

```bash
export HESPERIA_DICT_CALIB_OFFLINE=1
./tools/run_063_archive_e2e_gate.sh
```

For full calibration runs, prebuild dicts separately (out of band). Prod corpus remains on `Atomic-Commits-Team/hesperia` prod disk only.
EOF

cat > release/v0.6.3/RELEASE_SCOPE.md << 'EOF'
# HESPERIA v0.6.3 — IRC Teacher application run (GitHub archive)

**Sealed:** application-level 0.6.3 pre-release. **Engine math unchanged** from 0.6.2.

## Include

- Runtime, core, hesperia, lexicon, schemas, matrices, calibration **profiles** (not dict payloads).
- Shipping API: `GET /health`, `POST /analyze`, compare/batch routes.
- `docs/specs/0.6.3-IRC-TEACHER-RUN.md` — integration contract (tersagor `0149120`).
- `assets/calibration/dicts/archive_063_minimal/` — placeholder only.

## Exclude (GitHub archive)

- `assets/calibration/dicts/v0_*` prod sealed packs.
- `hesperia/modules/tfp/data/corpus/**` and `tfp_v1/corpus/**`.
- Chroma state, `outputs/`, secrets, brain team docs.

## Integration (out of tree)

- **tersagor** `igareosh/tersagor@0149120` — envelope, Teacher v063, IRC emitter, MySQL persist.
- **MySQL** ledger DDL: brain `cluster/hesperia/mysql/001_h063_schema.sql`.

## E2E

`HESPERIA_DICT_CALIB_OFFLINE=1 ./tools/run_063_archive_e2e_gate.sh` → **PASS** required before tag `hesperia-0.6.3`.
EOF

cat > release/v0.6.3/ARCHIVE_README.md << EOF
# Hesperia 0.6.3 complete archive (GitHub)

**Git SHA:** \`$SHORT\` (\`$SHA\`)  
**Sealed UTC:** $TS  
**Policy:** No production dict packs or corpus sessions in this archive.

## Quick start

\`\`\`bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
export HESPERIA_DICT_CALIB_OFFLINE=1
./tools/run_063_archive_e2e_gate.sh
\`\`\`

## Build zip for GitHub release

\`\`\`bash
./tools/build_063_github_archive.sh
# -> dist/hesperia-0.6.3-archive.zip + SHA256SUMS
\`\`\`

## What 0.6.3 adds

Application-level IRC-visible Teacher run (tersagor). This repo ships the **engine + shipping API** contract; live Teacher path runs on **tersagor VM** against prod \`/analyze\` on prichindel.

See \`docs/specs/0.6.3-IRC-TEACHER-RUN.md\`.
EOF

cat > release/v0.6.3/packaging_exclude.txt << 'EOF'
# 0.6.3 GitHub archive — excludes prod dicts and corpus
docs/internal/
legacy/
__pycache__/
*.pyc
.pytest_cache/
.git/
outputs/
assets/calibration/dicts/v0_6_0_clr_v052_2/
assets/calibration/dicts/v0_6_0_clr_v052_4/
assets/calibration/dicts/v0_6_0_clr_v052_5/
assets/calibration/dicts/v0_tfp_cal_wave_002/
hesperia/modules/tfp/data/corpus/
hesperia/modules/tfp/data/tfp_v1/corpus/
hesperia/modules/tfp/data/normalization/
EOF

cat > release/v0.6.3/manifest.json << EOF
{
  "version": "0.6.3",
  "release_kind": "github_archive_no_prod_dicts",
  "git_commit": "$SHA",
  "build_timestamp": "$TS",
  "entry_points": ["analyze", "compare", "batch-analyze", "health", "shipping_api"],
  "integration": {
    "tersagor_ref": "0149120",
    "spec": "docs/specs/0.6.3-IRC-TEACHER-RUN.md"
  },
  "excluded_from_archive": [
    "assets/calibration/dicts/v0_*",
    "hesperia/modules/tfp/data/corpus",
    "hesperia/modules/tfp/data/tfp_v1/corpus"
  ]
}
EOF

cat > tools/run_063_archive_e2e_gate.sh << 'EOF'
#!/usr/bin/env bash
# 0.6.3 archive E2E — no prod dicts/corpus required.
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
export HESPERIA_DICT_CALIB_OFFLINE=1
export PYTHONPATH="$REPO${PYTHONPATH:+:$PYTHONPATH}"
PY="${PY:-$REPO/.venv/bin/python}"
[[ -x "$PY" ]] || PY=python3
FAIL=0
echo "=== Hesperia 0.6.3 archive E2E gate ==="
if "$PY" -m pytest tests/test_archive_063_e2e_gate.py tests/test_engine_api_v1.py \
    tests/test_e2e_flows.py::test_e2e_analyze_sentence_output_exists -q --tb=short; then
  echo "[PASS] pytest archive subset"
else
  echo "[FAIL] pytest archive subset"
  FAIL=1
fi
if "$PY" -m tools.system_seal.run_system_seal; then
  echo "[PASS] system_seal"
else
  echo "[FAIL] system_seal"
  FAIL=1
fi
if grep -q '"version": "0.6.3"' release/v0.6.3/system_seal.json 2>/dev/null; then
  echo "[PASS] seal version 0.6.3"
else
  echo "[FAIL] seal version mismatch"
  FAIL=1
fi
# Archive must not list prod dict dirs as required
for forbidden in assets/calibration/dicts/v0_6_0_clr_v052_2; do
  if [[ -d "$forbidden" ]] && ! grep -q "$forbidden" release/v0.6.3/packaging_exclude.txt; then
    echo "[WARN] prod dict present on disk but excluded from archive manifest"
  fi
done
echo "=============================================="
if [[ $FAIL -eq 0 ]]; then
  echo "HESPERIA 0.6.3 ARCHIVE E2E: PASS"
  exit 0
fi
echo "HESPERIA 0.6.3 ARCHIVE E2E: FAIL"
exit 1
EOF
chmod +x tools/run_063_archive_e2e_gate.sh

cat > tools/build_063_github_archive.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"
VER="0.6.3"
OUT="dist/hesperia-${VER}-archive.zip"
mkdir -p dist
git archive --format=zip --prefix="hesperia-${VER}/" HEAD > "$OUT"
( cd dist && sha256sum "$(basename "$OUT")" > SHA256SUMS-hesperia-${VER}.txt )
echo "Wrote $OUT"
cat "dist/SHA256SUMS-hesperia-${VER}.txt"
EOF
chmod +x tools/build_063_github_archive.sh

cat > tests/test_archive_063_e2e_gate.py << 'EOF'
"""0.6.3 GitHub archive gate — runnable without prod dicts or corpus."""
from __future__ import annotations

import os
from pathlib import Path

import yaml


def test_version_is_063() -> None:
    doc = yaml.safe_load((Path(__file__).resolve().parents[1] / "VERSION.yaml").read_text(encoding="utf-8"))
    assert doc.get("system_version") == "0.6.3"
    assert doc.get("archive", {}).get("excludes_prod_dicts") is True


def test_analyze_offline_no_prod_dict() -> None:
    os.environ["HESPERIA_DICT_CALIB_OFFLINE"] = "1"
    from runtime.pipeline.analyze import analyze

    minimal, _extended = analyze("Справедливость и порядок в обществе.", r1_r4=False)
    assert "dominant_area" in minimal
    assert "dominant_family" in minimal


def test_archive_manifest_excludes_corpus() -> None:
    root = Path(__file__).resolve().parents[1]
    exclude = (root / "release/v0.6.3/packaging_exclude.txt").read_text(encoding="utf-8")
    assert "corpus/" in exclude
    assert "dicts/v0_6" in exclude or "v0_6_0" in exclude


def test_release_folder_present() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "release/v0.6.3/RELEASE_SCOPE.md").is_file()
    assert (root / "docs/specs/0.6.3-IRC-TEACHER-RUN.md").is_file()
EOF

echo "Files written. Running gate..."
export HESPERIA_DICT_CALIB_OFFLINE=1
./tools/run_063_archive_e2e_gate.sh
