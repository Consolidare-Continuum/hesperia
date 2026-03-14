# HESPERIA Consistency Verification Program

Run **before any release tag**. Two main blocks:

- **Block A — Functional integrity** (A1–A5): Baseline stability, runner/service equivalence, stage-limited correctness, batch/single equivalence, domain metric switch.
- **Block B — Sealing integrity** (B1–B6): Projection verification, reserved structure, import boundary, writer enforcement, packaging, reflection spot test.
- **Block C — Performance sanity** (C1–C2): Single-text latency, batch scaling.

**Summary report:** [HESPERIA_POST_SEAL_CONSISTENCY_REPORT_v1.md](HESPERIA_POST_SEAL_CONSISTENCY_REPORT_v1.md) — fill after running all checks; do not release until A, B, and (as policy) C pass.

**Index**

| Id | Document |
|----|----------|
| A1 | [CONSISTENCY_A1_BASELINE_STABILITY.md](CONSISTENCY_A1_BASELINE_STABILITY.md) |
| A2 | [CONSISTENCY_A2_RUNNER_SERVICE_EQUIVALENCE.md](CONSISTENCY_A2_RUNNER_SERVICE_EQUIVALENCE.md) |
| A3 | [CONSISTENCY_A3_STAGE_LIMITED_RUNS.md](CONSISTENCY_A3_STAGE_LIMITED_RUNS.md) |
| A4 | [CONSISTENCY_A4_BATCH_SINGLE_EQUIVALENCE.md](CONSISTENCY_A4_BATCH_SINGLE_EQUIVALENCE.md) |
| A5 | [CONSISTENCY_A5_DOMAIN_METRIC_SWITCH.md](CONSISTENCY_A5_DOMAIN_METRIC_SWITCH.md) |
| B1 | [SEAL_B1_PROJECTION_VERIFICATION.md](SEAL_B1_PROJECTION_VERIFICATION.md) |
| B2 | [SEAL_B2_RESERVED_STRUCTURE_TEST.md](SEAL_B2_RESERVED_STRUCTURE_TEST.md) |
| B3 | [SEAL_B3_IMPORT_BOUNDARY_CHECK.md](SEAL_B3_IMPORT_BOUNDARY_CHECK.md) |
| B4 | [SEAL_B4_WRITER_ENFORCEMENT.md](SEAL_B4_WRITER_ENFORCEMENT.md) |
| B5 | [SEAL_B5_RELEASE_PACKAGE_CHECK.md](SEAL_B5_RELEASE_PACKAGE_CHECK.md) |
| B6 | [SEAL_B6_REFLECTION_SPOT_TEST.md](SEAL_B6_REFLECTION_SPOT_TEST.md) |
| C1 | [PERF_C1_SINGLE_TEXT.md](PERF_C1_SINGLE_TEXT.md) |
| C2 | [PERF_C2_BATCH_RUN.md](PERF_C2_BATCH_RUN.md) |
