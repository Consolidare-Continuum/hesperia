<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Task: Ethan — address Gena developments, consolidate opinion, provide agents-oriented Hesperia path

**Purpose**: **Address** Gena's developments (matrix, schema §6, compressed world view, matrix_run, families table/ingest); **consolidate opinion** (Ethan's synthesis and assessment); **provide a further path** of **agents-oriented development** of the Hesperia project that is **realistic, deployable, and addressable** as per Hesperia documentation and project foundations. **Owner**: Ethan. **Triage**: Grace. **Added**: 2026-02-17. **Status**: DONE (2026-02-17) — deliverable: [HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](HESPERIA-AGENTS-PATH-ETHAN-REPORT.md).

**Refs**: Gena deliverables — [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md) (incl. §6 calculable units), [BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md](BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md), [TASK-GENA-BOOKS-MATRIX-MAIN-DEV.md](TASK-GENA-BOOKS-MATRIX-MAIN-DEV.md), [TASK-GENA-SCHEMA-HEX-TRAVERSAL-UNITS.md](TASK-GENA-SCHEMA-HEX-TRAVERSAL-UNITS.md), [TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT.md](TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT.md); cluster/chroma-server/matrix_run.py, ingest_hesperia_families.py. **Hesperia project foundations**: [projects/hesperia/PROJECT-CHARTER.md](../projects/hesperia/PROJECT-CHARTER.md), [projects/hesperia/CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md), [projects/hesperia/SCOPE-AND-SYNC.md](../projects/hesperia/SCOPE-AND-SYNC.md), [projects/hesperia/ARCH-DECISION.md](../projects/hesperia/ARCH-DECISION.md); [CLIENTS/hesperia/DOC_INDEX.md](../CLIENTS/hesperia/DOC_INDEX.md) and numbered specs (10_MASTER_SPEC, 11_BLUEPRINT, 20_GEOMETRY, 40_POLICY, etc.).

---

## 1. Scope

1. **Address Gena's developments**: Review and assess what Gena delivered (Chroma families schema, §6 calculable units and traversal, compressed world-view description, matrix_run script, ingest script). Summarise how it fits the current Hesperia scope (documentation and scripting; agents use in cursor repo) and where it touches or differs from SCOPE-AND-SYNC / CONTEXT-PACKET (e.g. families table in Chroma for Albina/agents vs “semantic layer not in scope” for the product).

2. **Consolidate opinion**: Provide a **consolidated opinion** (synthesis, risks, alignment with project foundations): what is in place, what is consistent with Hesperia docs, what should be clarified or adjusted for a coherent agents-oriented line.

3. **Further path — agents-oriented development**: Propose a **realistic, deployable, and addressable** path for **agents-oriented development** of the Hesperia project:
   - Grounded in **Hesperia documentation** (project foundations, DOC_INDEX, numbered specs).
   - **Agents-oriented**: Cursor and other agents consume matrix, schema, and run outputs; Chroma layer hesperia_families; matrix_run; optional books–matrix wiring and FPF/Albina integration.
   - **Realistic**: Phased; respects current scope (SCOPE-AND-SYNC, CONTEXT-PACKET) and gates; no unbounded scope creep.
   - **Deployable**: Concrete steps (ingest, wiring, scripts, docs) that can be executed and verified.
   - **Addressable**: Clear ownership and handoffs (Grace, Gena, Abelard, Cursor, etc.) and reference to existing task/docs.

---

## 2. Deliverables

- **Document** (e.g. in governance/ or projects/hesperia/): (a) short assessment of Gena's developments; (b) consolidated opinion; (c) proposed **agents-oriented development path** for Hesperia (phases, next steps, refs to foundations). Format: report or addendum to CONTEXT-PACKET / project docs as appropriate; artifact signature per ARTIFACT-SIGNATURE-POLICY.

---

## 3. Handoffs

- **Implementation**: Gena (matrix/main dev); Abelard (ingest, Chroma). Ethan delivers assessment and path; Grace triages follow-on tasks.

---

## 4. Completion (Ethan, 2026-02-17)

- **Deliverable**: [HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](HESPERIA-AGENTS-PATH-ETHAN-REPORT.md) — (a) assessment of Gena's developments and fit with SCOPE-AND-SYNC / CONTEXT-PACKET; (b) consolidated opinion (in place, risks, scope clarification recommendation); (c) phased agents-oriented path (Phase A done/in hand; B = scope wording + ingest + FPF wire + optional agent doc; C = books–matrix wiring + loopability preset when data exists; D = product semantic layer when scope changes). Ref: project foundations and DOC_INDEX/specs.

---

**SIGNED: Product/Triage (Grace) | task Ethan hesperia agents path | 2026-02-17 | governance**
