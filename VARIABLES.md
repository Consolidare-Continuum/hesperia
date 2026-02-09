# HESPERIA — SYSTEM VARIABLES AND CONSTANTS (v0.1)

Purpose: accumulate all **system-level** variables and constants used by
HESPERIA’s geometry, math apparatus, and DB layer. Each entry has a
short, imperative description; API/wrapper details are intentionally
omitted.

Variables are grouped by role:
- Geometry & indexing
- Semantic attribution & embeddings
- Activation vectors & polarity
- Structural metrics & traversal
- Evidence, temporal dynamics & governance
- Data / DB identifiers

Names follow the Java-style specs; array subscripts (e.g. `[s]`, `[a]`)
indicate indexing by side or area.

---

## 1. GEOMETRY & INDEXING

- `AREAS = 12`  
  Fix the number of semantic macro-areas on the ring to 12.

- `FAMILIES_PER_AREA = 24`  
  Fix the number of Families per Area to 24 (→ 288 total Families).

- `TOTAL_FAMILIES = AREAS * FAMILIES_PER_AREA`  
  Derive the total Family count and keep all Family-indexed arrays at this length.

- `HEXES_PER_FAMILY = 250`  
  Allocate exactly 250 hexes for each Family in the lattice.

- `TOTAL_HEXES = TOTAL_FAMILIES * HEXES_PER_FAMILY`  
  Compute the global number of hexes in the hex-sphere lattice.

- `SIDES_PER_HEX = 6`  
  Treat each hex as having exactly 6 sides (truth slots).

- `TOTAL_SIDES = TOTAL_HEXES * SIDES_PER_HEX`  
  Fix the global number of atomic truth sides.

- `SIDES_PER_FAMILY = HEXES_PER_FAMILY * SIDES_PER_HEX`  
  Use this as the fixed capacity of sides per Family.

- `SIDES_PER_AREA = SIDES_PER_FAMILY * FAMILIES_PER_AREA`  
  Use this as the fixed capacity of sides per Area.

- `sideId` (0..TOTAL_SIDES-1)  
  Use `sideId` as the canonical linear index for all side-level arrays.

- `areaOf[sideId]`  
  Store the Area index of each side and use it to compute Area-level metrics.

- `familyOf[sideId]`  
  Store the Family index of each side and use it to compute Family-level metrics.

- `hex_index`, `side_index`  
  Maintain hex-local indices (0..249, 0..5) to reconstruct full coordinates.

---

## 2. SEMANTIC ATTRIBUTION & EMBEDDINGS

- `dictWordToFamily`  
  Maintain a deterministic mapping from lemma to Family id for dictionary matches.

- `familyToArea`  
  Map each Family to its owning Area and keep this mapping stable.

- `embedWord[lemma]`  
  Store the embedding vector for each lemma used in nearest-neighbor search.

- `embedFamily[f]`  
  Maintain the centroid embedding for each Family to pull unknown words/statements.

- `embedArea[a]`  
  Maintain the centroid embedding for each Area to support area-level similarity.

- `axisPos[k]`, `axisNeg[k]` (k = 0..5)  
  Store positive and negative pole embeddings for the six bipolar axes.

- `THRESH_DICT`  
  Enforce this threshold as priority for dictionary matches over other signals.

- `THRESH_NN`  
  Use this as the minimum similarity for counting nearest-neighbor votes.

- `THRESH_FAM`  
  Use this to decide when family centroid similarity can override neighbors.

- `THRESH_AXIS`  
  Use this to accept or reject polarity corrections along the axes.

- `F_sentence[288]` / `A_sentence[12]`  
  Populate these as normalized Family/Area distributions per sentence.

- `F_statement[288]` / `A_statement[12]`  
  Populate these as aggregated Family/Area distributions per statement.

- `inwardVector[12]`, `outwardVector[12]`  
  Compute these per statement to express inward strengthening and outward reference across Areas.

---

## 3. ACTIVATION VECTORS & POLARITY

- `A_vec[AREAS]`  
  Use this as the primary Area activation vector over the ring (sum to 1).

- `F_vec[TOTAL_FAMILIES]`  
  Use this as the primary Family activation vector (not necessarily normalized).

- `areaHit[AREAS]`  
  Mark which Areas have been touched during traversal to compute coverage.

- `coveragePhi`  
  Compute this as the fraction of Areas hit to measure exploration breadth.

- `bipolarAxes(A_vec)` → `B[6]`  
  Derive six bipolar axis values from `A_vec` to quantify semantic polarity.

- `tensionEnergy(B)`  
  Sum the squared axis values to measure total polarization energy.

- `O_obstacle`  
  Maintain a scalar obstacle score in [0,1] to represent hazard rate or blockage of a Region.

---

## 4. TRUTH, STRUCTURAL METRICS & TRAVERSAL

- `tau[sideId]` (0..1)  
  Store the truth weight of each side and update it as statements are assigned.

- `fillingRate(R)`  
  Compute the fraction of sides in Region R that are filled to gauge utilization.

- `minSentences(R)`, `maxSentences(R)`, `avgSentences(R)`  
  Use these to estimate sentence capacity of Region R based on filled sides.

- `T(R)`  
  Sum `tau` over all sides in R to get total truth magnitude.

- `T_norm(R)`  
  Normalize truth by side count to get truth density in R.

- `TAU_THRESHOLD`  
  Use this fixed threshold (e.g. 0.8) to count “truth points” in R.

- `truthPoints(R)` / `truthPointDensity(R)`  
  Count and normalize sides exceeding `TAU_THRESHOLD` to quantify strong support.

- `A[i][j]`  
  Maintain adjacency between sides in the graph to support cluster calculations.

- `K(R)` / `L(R)`  
  Compute cluster count and largest cluster size to analyze connectivity of R.

- `activeSides(R)`  
  Count sides with `tau > 0` in R to define the active set for structural metrics.

- `C(R)` (coherence)  
  Compute `L(R) / activeSides(R)` to measure how concentrated truth is.

- `fragIndex(R)`  
  Compute `K(R) / activeSides(R)` to measure fragmentation of truth.

- `adjacencyCorrelation(R)`  
  Measure how smoothly tau varies across adjacent sides as a [0,1] index.

- `X_A(R)`  
  Compute dominant Area alignment by counting active sides per Area in R.

- `X_F(R)`  
  Compute dominant Family alignment by counting active sides per Family in R.

- `S(R)` / `S_prime(R)`  
  Combine T, C, and alignment metrics into composite structural scores for R.

- `areaEntropy(R)`  
  Compute entropy over Area usage in R to measure spread vs concentration.

- `entropy(p[])`  
  Use Shannon entropy as a generic measure of distribution spread.

- `loopability(newHits, hops)`  
  Compute loopability as new-family hits per hop during traversal.

- `kl(p,q)`  
  Use KL divergence between distributions for domain and calibration checks.

- `cosine(x,y)`  
  Use cosine similarity as the base similarity for embeddings and vectors.

- `turnCoherence(A_t, A_prev)`  
  Measure Area activation similarity across time steps to detect coherence.

- `cumulativeDrift(A_start, A_end)`  
  Measure change in activation distributions over time to detect drift.

- `expectedTimeToObstacle(O)`  
  Interpret obstacle level as a hazard rate and invert it to get expected time.

- `ringSmoothness(A)`  
  Use low-frequency spectral power on the ring to quantify smoothness of activations.

---

## 5. EVIDENCE, TEMPORAL DYNAMICS & GOVERNANCE

- `credibility[s]`, `recency[s]`, `consensus[s]`  
  Maintain per-side evidence factors in [0,1] for provenance weighting.

- `provenanceWeight[s]`  
  Multiply credibility, recency, and consensus to get a single weight per side.

- `evidenceQuality(R)`  
  Compute the tau-weighted average of provenance weights over Region R.

- `embed_side[s]`, `embed_hex[h]`, `embed_family[f]`  
  Keep multi-scale embeddings to assess consistency across side/hex/family levels.

- `scaleConsistency(R)`  
  Compare average embeddings across scales to ensure retrieval and structure agree.

- `timestamp[s]`  
  Record when a side was last updated for temporal stability checks.

- `tau_t[s]`  
  Apply time decay to `tau[s]` to obtain a time-weighted truth value.

- `temporalStability(R)`  
  Compute stability of timestamps in R (e.g. 1 − variance) to detect volatility.

- `contradictionScore(R)`  
  Combine tension energy and misalignment (1 − X_A(R)) to flag conflict in R.

- `goalVector[a]`  
  Store desired Area profile for a given task or domain.

- `riskProfile[a]`  
  Store per-Area risk weights used to penalize otherwise useful activations.

- `utility(A_vec)`  
  Compute cosine similarity between `A_vec` and `goalVector` to quantify fit.

- `actionScore`  
  Subtract risk-weighted penalties from utility to rate candidate actions.

- `causal[a][b]`  
  Maintain a causal influence matrix over Areas for causal coherence checks.

- `causalPush[b]`  
  Aggregate causal influence weighted by A_vec to see where actions push the system.

- `causalCoherence`  
  Compute cosine between A_vec and causalPush to rate causal alignment.

- `gradient[s]`  
  Compute average |tau[s] − tau[neighbor]| to capture local semantic pressure.

- `pressure(R)`  
  Average gradient in R to detect sharp local changes or tension.

- `saturation(R)`  
  Measure redundancy in side embeddings to detect over-saturated regions.

- `retrievalError[f]`, `retrievalConfidence[f]`  
  Track retrieval performance per Family to adjust retrieval weighting.

- `adaptiveFamilyWeight[f]`  
  Scale F_vec[f] by retrieval confidence to adapt family influence.

- `tau_threshold_domain[d]`, `obstacle_threshold_domain[d]`  
  Set per-domain thresholds for tau and obstacles to tune sensitivity.

- `domainFit(d)`  
  Evaluate how well `A_vec` matches a domain profile using KL divergence.

- `summaryFidelity`, `compressionRatio`, `IPS`  
  Track summarization quality and compression physics for downstream use.

- `rationale[s]`, `override[a]`, `trace(R)`  
  Record human/algorithmic rationales and overrides for auditing regions.

- `M_ext2sphere`, `M_sphere2ext`  
  Maintain mapping operators between external embedding spaces and HESPERIA’s space.

- `compatibilityLoss`  
  Quantify mismatch between external embeddings and internal Area activations.

- `decisionIntegrity(R)`  
  Combine evidenceQuality, scaleConsistency, temporalStability, and (1 − contradictionScore) into a reliability score.

- `strategicScore`  
  Combine actionScore, causalCoherence, (1 − saturation), and evidenceQuality into an action-level utility score.

---

## 6. DATA / DB IDENTIFIERS

- `area.id`, `family.id`  
  Use these as stable 0-based identifiers mapped directly to Areas and Families in the math.

- `hex.id`, `hex_index`  
  Keep hex IDs and local indices consistent with Family ownership and indexing rules.

- `side.side_id`  
  Store the canonical sideId from the indexing spec as the primary key in SQL.

- `statement.id`  
  Use this as the primary identifier for statements across SQL and vector DB.

- `dictionary_word.lemma`  
  Use lemma as the unique key for word-level dictionary entries.

- `domain_profile.id` / `name`  
  Use these to manage domain-specific Area profiles for calibration.

These variables and constants form the complete internal surface of
HESPERIA’s geometry, math, and data layer. Any new metric or stateful
quantity added to the core system should be appended here with a short,
imperative description before being used in code or specs.

