/**
 * Canonical 12×24 family lattice F(s,b) on a spheroid shell.
 * s = sector (0..11), b = band (0..23). Linear index: row-major with sector across, band down.
 *
 * Adjacency (explicit):
 * - left:  F((s - 1) mod 12, b)
 * - right: F((s + 1) mod 12, b)
 * - up:    F(s, b - 1) when b > 0
 * - down:  F(s, b + 1) when b < 23
 */

export const SECTORS = 12;
export const BANDS = 24;
export const N_FAMILY_CELLS = SECTORS * BANDS; // 288

/**
 * @param {number} s
 * @param {number} b
 */
export function familyLinearIndex(s, b) {
  return b * SECTORS + s;
}

/**
 * @param {number} idx 0..287
 * @returns {{ s: number; b: number }}
 */
export function parseFamilyLinear(idx) {
  const s = idx % SECTORS;
  const b = Math.floor(idx / SECTORS);
  return { s, b };
}

/**
 * Matches existing mock: family_id = sector*24 + band (sector was area_id, band was fam_in_area).
 * @param {number} familyId 0..287
 */
export function familyIdToSB(familyId) {
  const s = Math.floor(familyId / BANDS);
  const b = familyId % BANDS;
  return { s, b };
}

/**
 * Inverse: (s,b) -> family_id 0..287
 * @param {number} s
 * @param {number} b
 */
export function sbToFamilyId(s, b) {
  return s * BANDS + b;
}

/**
 * Neighbors with boundary semantics (no vertical wrap).
 * @param {number} s
 * @param {number} b
 */
export function latticeNeighbors(s, b) {
  const left = { s: (s - 1 + SECTORS) % SECTORS, b };
  const right = { s: (s + 1) % SECTORS, b };
  /** @type {{ s: number; b: number }[]} */
  const out = [left, right];
  if (b > 0) out.push({ s, b: b - 1 });
  if (b < BANDS - 1) out.push({ s, b: b + 1 });
  return out;
}

/**
 * Spherical mapping per spec:
 * theta = (2π/12)*s, phi = π*(b/23 - 0.5), r = cos(phi), z_pole = sin(phi)
 * x = r*cos(theta), y = r*sin(theta), z = z_pole
 * Three.js Y-up: use x,z as equatorial plane, Y as pole.
 * @param {number} s
 * @param {number} b
 * @param {number} [radius] default 1
 * @returns {{ x: number; y: number; z: number }}
 */
export function spherePosition(s, b, radius = 1) {
  const theta = (2 * Math.PI * s) / SECTORS;
  const phi = Math.PI * (b / 23 - 0.5);
  const r = Math.cos(phi) * radius;
  const y = Math.sin(phi) * radius;
  const x = r * Math.cos(theta);
  const z = r * Math.sin(theta);
  return { x, y, z };
}

/**
 * Cylinder: sector wraps, band is linear height (north b=0 at +Y).
 * @param {number} s
 * @param {number} b
 * @param {number} cylRadius
 * @param {number} height full height of band axis
 */
export function cylinderPosition(s, b, cylRadius = 1, height = 2.2) {
  const theta = (2 * Math.PI * s) / SECTORS;
  const y = (b / 23 - 0.5) * height;
  const x = cylRadius * Math.cos(theta);
  const z = cylRadius * Math.sin(theta);
  return { x, y, z };
}

/**
 * Flat Mercator-like: X = sector, Y = band (north at top, b=0).
 * Returns normalized 0..1 cell center.
 * @param {number} s
 * @param {number} b
 */
export function flatNormalizedCenter(s, b) {
  return {
    x: (s + 0.5) / SECTORS,
    y: (b + 0.5) / BANDS,
  };
}
