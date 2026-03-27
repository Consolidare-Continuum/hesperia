<!--
Ethan — architect ruling: dict layer order after lexical A is frozen.
-->

# Ethan — Dict layer order after A is green

**Status:** **LOCKED** — aligns `docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md` §Layer chain.

## Order (do not invert)

1. **`A`** — lexical evidence (frozen calibration `dict_a` when green).
2. **`B`** — **concept identity / resolver**: inventory and winning `concept_id` from evidence (`dict_b` + links in the same calibration version). **Surface** resolution lives here (what concept the engine commits to).
3. **`CD`** — **Concept Dictionary**: deterministic rows **keyed by `concept_id`**, no lexical strings. **Activation** law (base, cap, threshold, saturation), requires/excludes, later effects / co_occurs. Default row `*` when a B concept has no explicit CD line.
4. **`C_agg`** — families / areas / hex aggregation.
5. **Topology** — session / segments.

## Anti-pattern (rejected)

- **CD before B:** authoring `concept_dict_cd.jsonl` as if it “creates” concepts ahead of a stable B inventory breaks the contract; CD **annotates** IDs that B must already define (or fall through to `*`).
- **“C concepts then B activations”:** conflates **CD** with a separate concept factory. Correct sequence is **B identity first**, **then CD activations/constraints** on those IDs.

## Execution

- Validators + smoke: `tools/run_b_cd_wave_after_a.sh` (Hesperia repo root).
- Calibration version: `HESPERIA_CALIB_DICT_VERSION` (e.g. `v0_6_0_clr_v052_1`).

---

`SIGNED: Architect (Ethan) | dict layer order after A | 2026-03-28 | Hesperia governance/working`
