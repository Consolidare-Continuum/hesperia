---

# Hesperia v0.2 Release

**Release Date**: February 20, 2026  
**Status**: Production Ready

## What's New in v0.2

### Core Components ✅
- **Stable Geometry Kernel**: Fixed structure (12 areas, 24 families/area, 250 hexes/family, 6 sides/hex)
- **Deterministic Ring Traversal**: Predictable (start_area, direction, steps) → single path
- **Context RAG Daemon (MVP)**: Single entry point for full context packets (calculable + coherence hints + observability + optional retrieval)
- **Loop Safeguard (Proven)**: Three consecutive failures → SAFEGUARD_STOP with fail_trace and obstacle marking
- **Observability Extension v0.1**: Loopability band, entropy metric, safeguard events count (read-only telemetry; no core changes)

### Guard Layer Integration ✅
- **Σ (Sigma) Guard**: Static invariant validation (geometry, topology, schema, borders, hashes)
- **Γ (Gamma) Guard**: Dynamic invariant monitoring (bounds, trends, ΣΓ relational coherence)
- **Θ (Theta) Guard**: Governance legitimacy gate (versioning, config hashes, operator discipline, publishability)

### Scripts Shipped
1. `matrix_run.py` — Ring traversal + geometry calculation
2. `context_rag.py` — Full context packet assembly (calculable + coherence + observability + retrieval)
3. `hesperia_logic.py` — Logic operators + loop safeguard
4. `sigma_guard.py` — Static invariant guard
5. `gamma_guard.py` — Dynamic invariant guard
6. `theta_guard.py` — Governance legitimacy guard
7. `apple_path_imprint.py` — Store traversal paths
8. `apple_involvements.py` — Coverage summary (areas, families, pairs)
9. `ingest_hesperia_families.py` — Load 288 families into Chroma (layer=hesperia_families)
10. `run_core_mode_invocation.py` — Plan 1 calibration harness (internal)
11. `multi_loop_runs_harness.py` — Generate 24-run dataset for traversal analysis
12. `hesperia_safeguard_stress_test.py` — Safeguard verification (PASS)

### Governance Documentation
- **25+ governance documents signed** (architecture, operators, safeguard spec, observability extension, integration plans)
- **GOVERNANCE-ORCHESTRATION-HESPERIA.md**: Unified orchestration pipeline (Σ→Γ→Θ→Context RAG→Apple)
- **CONTEXT-RAG-PACKET-SCHEMA.md**: Full packet contract including v0.1 observability block
- **Safeguard stress-test results**: Proven that safeguard fires correctly after 3 consecutive failures

### Testing & Quality
- ✅ Unit tests for all guards (Σ/Γ/Θ)
- ✅ Integration tests (full pipeline: matrix → context → logic → apple)
- ✅ Stress-tested safeguard (3-fail rule verified)
- ✅ Smoke tests all pass (matrix_run, context_rag, apple, Plan 1)
- ✅ Core-mode calibration validated

## Documentation

- **README**: `cluster/chroma-server/README.md` (script reference + quick start)
- **Usage Guide**: `cluster/chroma-server/USAGE.md` (complete CLI reference + examples)
- **Release Notes**: `projects/hesperia/RELEASE-NOTES-v0.2.md`
- **Known Issues**: `projects/hesperia/KNOWN-ISSUES.md`

## Quick Start

### Get full context packet
```bash
python cluster/chroma-server/context_rag.py \
  --start 0 \
  --direction 1 \
  --steps 12 \
  --chroma
```

### Query for families
```bash
python cluster/chroma-server/context_rag.py \
  --start 0 \
  --steps 12 \
  --query "polarity order" \
  --families-limit 10 \
  --chroma
```

### Run core-mode calibration (internal)
```bash
python cluster/chroma-server/run_core_mode_invocation.py \
  --chroma \
  --log-dir /tmp/hesperia_logs
```

## What v0.2 Is NOT

- **Not semantic reasoning layer** (Phase D): Logic stubs ready for upgrade; SATISFY/ENTAILS bounded depth only
- **Not activation pipeline** (deferred): --activation flag accepts manual activation data files; automation pending
- **Not kernel wiring of capacity doctrine** (Phase D): Waterline principle defined; governance layer only
- **Not full semantic weight** (Phase D): Per-area weights pending observability integration

## Known Issues (Phase D Backlog)

- Activation data pipeline not automated (requires external source; manual --activation flag available)
- Hex.evaluate and semantic operators (SATISFY, ENTAILS) are stubs (ready for Phase D full reasoning)
- Waterline/capacity doctrine not wired into traversal kernel (governance definition only)
- obstacleScore composition and decision FSM pending formal specification
- Full semantic weight per area pending Phase D integration

## Architecture & Design

**Unified orchestration pipeline** (locked for v0.2):
```
Input → Σ (static check) → Matrix → Γ (dynamic check) → Logic (safeguard) → Θ (governance) → Context RAG → Apple → Output
```

All stages **gated** (failure halts); all outputs **deterministic** (same input = same output); all errors **traceable** (error code + detail + stage).

## Deployment

**For Cursor agents**: Use `context_rag.py` to get full context packets for model reasoning.

**For Albina**: Matrix available via Chroma layer `hesperia_families` (288 families, 12 areas, coordinates, book references).

**For audit**: Use `apple_path_imprint.py` + `apple_involvements.py` to track traversal coverage.

**For development**: Run `run_core_mode_invocation.py` for internal calibration logs.

## Sign-offs

- ✅ Grace (triage): v0.2 complete, ready for production
- ✅ Ethan (architecture): Orchestration locked, no core changes, Phase D deferred
- ✅ Gena (development): All scripts tested, stubs documented
- ✅ Abelard (operations): Ingest runnable, Chroma ready, logs working
- ✅ igareosh (owner): v0.2 approved for release

## Next Steps (Phase D)

1. Activate semantics (full reasoning layer)
2. Implement activation data pipeline (automation)
3. Wire waterline/capacity doctrine into kernel
4. Formalize obstacleScore and decision FSM
5. Integrate full semantic weight per area

---

**Hesperia v0.2 is stable, documented, tested, and production-ready. Thank you for using Hesperia!**