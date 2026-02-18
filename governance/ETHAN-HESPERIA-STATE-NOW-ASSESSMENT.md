# Hesperia — state now: what it is, what it does, what it does not (Ethan)

**Purpose**: Make sense of current Hesperia baseline; state formally what it **is** and what it **does**; add notes, strategic fork, and next-step discipline. **Owner**: Ethan. **Date**: 2026-02-18.

**Refs**: [HESPERIA-MID-STAGE-PRODUCT-REPORT.md](projects/hesperia/HESPERIA-MID-STAGE-PRODUCT-REPORT.md), [ETHAN-HESPERIA-CORE-MODE-MVP.md](ETHAN-HESPERIA-CORE-MODE-MVP.md), [ETHAN-HESPERIA-LOOP-SAFEGUARD.md](ETHAN-HESPERIA-LOOP-SAFEGUARD.md), [CONTEXT-PACKET](projects/hesperia/CONTEXT-PACKET.md).

---

## I. What Hesperia is now (formal statement)

**Hesperia is:**

> A **geometry-safe semantic traversal kernel**.

In product terms:

> A **deterministic semantic traversal and validation core**.

**It is already:**

- **Fixed geometry**: 12 areas × 24 families × 250 hexes per family (72k hexes, 432k sides).
- **Deterministic ring traversal**: start, direction, steps → one path, one set of road_coordinates and border_passings.
- **Border-crossing tracking**: area-to-area and family-to-family passings recorded.
- **Context packet with adjacency hints**: current area, suggested adjacent areas (CW/CCW), traversal summary, border counts.
- **Logic layer + safeguard**: path-level validity check; three consecutive logical failures → SAFEGUARD_STOP.
- **Apple coverage summary**: which areas and families a run touched (policy/balance audit).
- **One successful full-ring run** (no contradiction, no safeguard trigger) — clean structural baseline.

So: **no noise, no retrieval in core run, no drift.** A solid **mid-stage engine**.

---

## II. What it does (technical truth)

You do **not** yet have semantic reasoning. You have:

1. **Deterministic graph traversal** on the area ring.
2. **Structural adjacency model** (left/right area, borders).
3. **Logical validity check** at path level (Hex.evaluate, run_traversal_with_safeguard).
4. **Loop-safeguard mechanism** (fail_count ≥ 3 → stop; valid_streak ≥ 2 to reset).
5. **Coverage accounting** (apple involvements: areas, families, pairs).

**It is not yet:**

- Value-evaluating.
- Conflict-detecting across content.
- Retrieval-aware (retrieval is optional and off in core calibration).
- Policy-aware (no policy rules in the kernel).

But it is **stable**. That matters.

---

## III. What it does NOT yet do

- No semantic weight per area.
- No content polarity mapping.
- No internal family-level constraint logic.
- No inter-family contradiction detection.
- No multi-path interference.
- No region/obstacle semantics beyond simple fail detection.

This is **structure-only traversal**. Do not confuse it with reasoning.

---

## IV. Real current applications (concrete)

### 1. Deterministic context framing for agents (context governor)

Instead of LLM improvising context, you can force: current area, adjacent areas, border context, traversal history. This prevents topic teleportation, axis skipping, semantic drift.

### 2. Structural path validation

Test arbitrary paths; inject jumps; force polarity flips; observe safeguard triggers. Essential for calibration, stress-testing traversal rules, future product QA.

### 3. Coverage verification (Apple)

Policy audit (“Did this query touch CARE?”); balance audit (“Did we only stay in ORDER/CONTROL?”); bias detection (“Was HARM skipped?”). Governance-grade telemetry.

### 4. Path comparison framework

Compare clockwise vs counter-clockwise, partial arcs vs full ring, start shifts, random vs guided walk. Calibration of traversal heuristics; studying structural bias. An experimental lab.

### 5. Logic layer baseline

Full ring passed: no contradictions, no safeguard stop. Ring topology is coherent. Foundational integrity check.

---

## V. Where retrieval fits

Retrieval is off in core calibration. When turned on it must:

1. Be constrained by current area/family.
2. Be filtered by adjacency.
3. Respect safeguard (block if 3-fail rule triggers).
4. Never let content override structure. **Structure is sovereign.**

---

## VI. Do not touch (until Phase D defined)

The most dangerous phase is now — because everything works. Do not touch until Phase D is defined formally:

- Ring ordering.
- Area adjacency.
- Family counts.
- Hex geometry (12 × 24 × 250).
- Safeguard threshold (3 consecutive failures, valid_streak ≥ 2 to reset).

---

## VII. Safeguard layer — evaluation needed

The 3-fail safeguard did not trigger on the full ring. That is good. But it must be **proven** by stress tests:

- Force jump GOOD → DESTRUCTION (skip adjacency).
- Inject artificial contradiction.
- Force oscillation CONTROL ↔ FREEDOM.
- Run partial loop repeatedly.

We need to see the safeguard fire. Otherwise it is unproven.

---

## VIII. Strategic fork — next serious move

Two main directions.

**Option A — Structural expansion (harden structure)**

Stay structure-only; add: more path types, randomized ring hops, multi-ring traversal, cross-family jumps, polarity-flip stress tests. Strengthens geometry and safeguard. Safe, conservative.

**Option B — Inject semantic weight**

Introduce: polarity scores, contradiction matrices, inter-area tension coefficients, family compatibility rules, entailment mapping between families. Turns traversal into semantic computation. Riskier; transforms the engine.

**Plus:**

- **Option C** — Add **controlled retrieval** (structure-first constraint; retrieval injection protocol).
- **Option D** — Begin **Phase D** product semantic layer (formal scope and WBS).

**Next step must be deliberate — not experimental.** Choose one vector: A) Harden structure; B) Inject semantic computation; C) Add controlled retrieval; D) Begin Phase D product semantic layer.

---

## IX. Formal specs to lock (pick one first)

To avoid drift, lock one of:

1. **Traversal Operators Spec v0.1** (formal).
2. **Safeguard State Machine Spec v0.1** (formal).
3. **Family Compatibility Matrix Spec v0.1** (formal).
4. **Retrieval injection protocol** (structure-first constraint).

Pick one and lock. No drift.

---

## X. Notes (Ethan)

- **Plateau**: This is the first real engineering plateau. Stable geometry, traversal, logging, safeguard, coverage telemetry.
- **Product terms**: With this alone you can build: structured AI assistant context stabilizer, policy traversal audit tool, semantic bias detector, narrative flow analyzer, controlled reasoning sandbox. Not trivial.
- **State in project**: The project must **already state** in one place what Hesperia **is** and what it **does** now — so new work and Grace tasks refer to a single source of truth. This doc is the governance source; project (CONTEXT-PACKET, mid-stage report) should point to it and repeat the one-line “is” and “does” in plain language.

---

## XI. Summary table

| Item | Statement |
|------|-----------|
| **What it is** | Geometry-safe semantic traversal kernel; deterministic semantic traversal and validation core. |
| **What it does** | Fixed geometry, deterministic ring traversal, border tracking, context packet + adjacency hints, logic layer + safeguard, apple coverage; context governor, path validation, coverage verification, path comparison, logic baseline. |
| **What it does not** | No semantic reasoning, value-evaluating, content conflict detection, retrieval-aware logic, policy-aware logic. Structure-only. |
| **Do not touch** | Ring order, adjacency, family counts, hex geometry, safeguard threshold — until Phase D defined. |
| **Safeguard** | Must be stress-tested until it fires; then documented. |
| **Next** | Choose A/B/C/D; pick one formal spec to lock. |

---

**SIGNED: Architecture (Ethan) | Hesperia state-now assessment — what it is, what it does, fork, tasks | 2026-02-18 | governance**
