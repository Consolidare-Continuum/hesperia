# Class A / Class B science narrative hub (HWIKI-DOC-28)

**Status:** RATIFIED template hub  
**Date:** 2026-07-23  
**Owners:** Ethan + Colombo

## Purpose

Bind wiki theory pages to Hesperia modular architecture — **Class A (universal, `hesperia/modules/default/`)** vs **Class B (branch, `hesperia/modules/<branch>/`)** — so science narratives do not smuggle Class B into sealed `/analyze` stacks.

**Location correction 2026-08-04:** neither class lives inside `core/` — `core/` holds zero module-registry-shaped code as of this date (dict_a/dict_b/topology/metrics moved `core/runtime/` → `hesperia/modules/default/`). "Cored" below is legacy terminology meaning "universal, registered with core" — not a physical location claim.

Refs: [HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md](../HESPERIA-MODULAR-BRANCH-ARCHITECTURE.md) §2c (see its own 2026-08-04 correction note) · [TEMPLATES-DECISION-THEORY.md](TEMPLATES-DECISION-THEORY.md)

## Class A (universal) — wiki binding

`hesperia/modules/default/` (dict_a/dict_b/topology/metrics/nlp) / TFP / MRT / COBALT sealed math: LIVE pages must cite engine modules + call sites (CODE template). Theory pages (Shannon, Markov λ, tension, etc.) explain **why the formula exists in the registered-with-core path** — not "inside core" itself.

Also Class-A-shaped but *not* module-registry-shaped, living directly in `core/domain/` alongside KME (pure-function derived-measurement, not `provides`/`requires`/`create()`): `core/domain/ksi/` (KSI-Inspector) and `sphere/topology/ipov/`/`sphere/topology/gtp/` (positional/geometry math) — added 2026-08-04.

## Class B (branch)

Psy / IT / semantic attribution / themes: wiki may document, but must label **Class B** and must not imply membership in sealed analyze core.

## Hub usage

Theory-depth DOC pages link here when discussing branch placement. Decision narratives use TEMPLATES-DECISION-THEORY.md structure.

SIGNED: Architecture (Ethan) / Cursor | HWIKI-DOC-28 Class A/B hub | 2026-07-23 | wiki
