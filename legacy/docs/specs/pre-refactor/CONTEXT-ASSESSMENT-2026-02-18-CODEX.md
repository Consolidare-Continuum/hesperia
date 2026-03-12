<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Hesperia Repo Context Assessment (2026-02-18) — Codex

Scope: repo-wide scan of `/data/hesperia/hesperia` as of 2026-02-18.
This document exists to help agents (including Codex) and new team
members quickly understand what is currently in the repo, what is
canonical, and what constraints are in force.

## Executive Summary

- This repository is a documentation-first “brain” + governance pack for
  HESPERIA (HSPR), plus a small set of scripts and statement artifacts.
- The “system” is defined as a CLI/kernel pipeline: deterministic
  attribution -> placement into fixed geometry -> traversal/safeguard ->
  governance output.
- A fixed baseline is explicitly declared on **2026-02-18** in
  `project/RELEASE-V1-FIXED-POINT-2026-02-18.md`.
- Names in filenames such as **Ethan** / **Grace** / **Gena** are team
  member/author/owner markers for governance artifacts (not technical
  terms in the semantic model).

## What This Repo Contains (Top-Level)

- **Numbered specs (canonical semantics/math/geometry)**: root `10_*`
  through `41_*` files define the core model (Areas/Families/hexes/sides,
  indexing, attribution, metrics, traversal policy).
- **Glossary**: `ACADEMIC.md` is the canonical academic glossary surface
  for project terms and variables (hashtagged identifiers).
- **Concepts/principles**: `04_CONCEPTS__HESPERIA_v1_0.md` captures the
  currently applicable project principles as constraints.
- **Project governance**: `project/` contains gate-bound context,
  charter/scope, fixed-point baseline, risk/security baselines, and
  handoff artifacts.
- **Team governance artifacts**: `governance/` contains authored specs,
  reports, and tasks (often prefixed with author names).
- **Scripts**: `scripts/` contains runnable Python utilities for context
  packets, matrix runs, ingestion, and safeguard stress tests.
- **Statements**: `statements/` contains extraction/classification
  scripts and a large JSON artifact (chunked statements).
- **Legacy snapshot**: `v0.1/` contains an older “HISPERIA” snapshot of
  specs and related artifacts (treat as legacy unless re-validated
  against the numbered root specs).
- **Archive**: `archive/` is reserved for dated snapshots/manifests.

## Canonical Reading Path (Recommended)

- **Start here (baseline)**: `project/RELEASE-V1-FIXED-POINT-2026-02-18.md`
- **Project state and constraints**: `project/CONTEXT-PACKET.md`
- **Core semantics**: `10_MASTER_SPEC__HESPERIA_v1_0.txt`,
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt`
- **Attribution and evolution**: `12_SPEC__Semantic_Engine_v0_4.txt`
- **Indexing and coordinates**: `13_SPEC__Indexing_and_Coordinates_v1_0.txt`
- **Loopability/governance metrics**: `40_POLICY__Loopability_and_traversal.txt`,
  `41_POLICY__Operational_additions_v0_1.txt`

## What “State Now” Means (As of 2026-02-18)

From the project’s own gate docs (`project/CONTEXT-PACKET.md` and
`project/RELEASE-V1-FIXED-POINT-2026-02-18.md`):

- Hesperia is currently positioned as a **geometry-safe traversal and
  validation kernel** (“structure-only”), not a full semantic reasoning
  product runtime.
- Retrieval/semantic layer work is explicitly constrained (many items
  are “definition only” and not wired into the kernel).

The highest-authority narrative on current boundaries is:
`governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md`.

## Governance Concepts Present Now

- **Waterline principle** exists in this repo (capacity doctrine), with
  a formal definition and integration placement:
  `governance/ETHAN-HESPERIA-WATERLINE-PRINCIPLE.md`.
- That document includes a “**Sinkage function**” section (so “sink”
  *is* described here as a waterline/capacity concept, not as a geometry
  primitive).

## Notable Gaps / Risks / Mismatches

- `DOC_INDEX.md` references items not currently present here (examples:
  `README.md`, `sphere_rag/`, and several numbered specs in the 16–18 and
  33 ranges). Treat `DOC_INDEX.md` as needing reconciliation with the
  actual repo contents.
- `WORKSPACE.md` and several project/governance docs reference paths in
  other repos (e.g. “cursor repo” paths like `cluster/chroma-server/*`).
  This repo is intended to be a synced subset of a larger workspace.
- `v0.1/openai_python_api_key_for_scripts.txt` exists and *may* represent
  secret material. Agents should not read or replicate key values. If
  this file contains a real key, it should be treated as a security
  incident (rotate/remove) rather than “documentation.”
- There is no `.gitignore` at repo root; large artifacts and secrets are
  at higher risk of accidental inclusion.

## Repo Facts (Quick Stats)

- File count (all files under repo): ~100
- Largest folders by size:
  - `statements/` (large JSON artifact)
  - `v0.1/` (legacy snapshot)
  - `governance/` (team artifacts)

