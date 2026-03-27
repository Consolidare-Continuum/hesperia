# Runner hook order (HC-04) — aligned with MODEL_CARD + frozen appendix

**Ref:** cursor `operational/assignments/HESPERIA_CONTROL_MERGED_v1_APPENDIX-2026-03-27.md`

## Ordered stages (lexical pipeline)

1. Tokenize / marker → raw concept weights  
2. `_stabilize_concept_weights`  
3. **B↔A validation trace** (HC-01) — emit envelopes; may filter invalid activations  
4. **Modifier MVP (pre-CD)** (HC-03) — adjust stabilized weights before CD  
5. **`apply_cd_phase1`** (CD) — env `HESPERIA_CD_ENABLED`  
6. Hex aggregation / `aggregate_hex_state` → families / areas  
7. **Strict dominance readout** (HC-05) — policy on segment area vector (no feedback into hex H for product signals)  
8. Topology / session rollup downstream  

**Unmapped diagnostics (HC-08):** parallel branch, non-blocking.

`SIGNED: Liam (task HC-04) | hook order doc | 2026-03-27 | Hesperia repo`
