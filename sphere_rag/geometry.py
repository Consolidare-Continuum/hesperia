from __future__ import annotations

from dataclasses import dataclass

# Canonical constants (13_SPEC__Indexing_and_Coordinates_v1_0.txt)
AREAS = 12
FAMILIES_PER_AREA = 24
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6

TOTAL_FAMILIES = AREAS * FAMILIES_PER_AREA  # 288
TOTAL_HEXES = TOTAL_FAMILIES * HEXES_PER_FAMILY  # 72,000
TOTAL_SIDES = TOTAL_HEXES * SIDES_PER_HEX  # 432,000

SIDES_PER_FAMILY = HEXES_PER_FAMILY * SIDES_PER_HEX  # 1,500
SIDES_PER_AREA = SIDES_PER_FAMILY * FAMILIES_PER_AREA  # 36,000


def clamp_int(v: int, lo: int, hi: int) -> int:
    return lo if v < lo else hi if v > hi else v


@dataclass(frozen=True, slots=True)
class SideCoord:
    area: int  # 0..11
    family_local: int  # 0..23
    hex_index: int  # 0..249
    side_index: int  # 0..5

    def family_global(self) -> int:
        return (self.area * FAMILIES_PER_AREA) + self.family_local

    def side_id(self) -> int:
        fam = self.family_global()
        return (((fam * HEXES_PER_FAMILY) + self.hex_index) * SIDES_PER_HEX) + self.side_index

    def label(self) -> str:
        return f"A{self.area + 1:02d}-F{self.family_local + 1:02d}-H{self.hex_index + 1:03d}-S{self.side_index}"

    @staticmethod
    def from_side_id(side_id: int) -> "SideCoord":
        if side_id < 0 or side_id >= TOTAL_SIDES:
            raise ValueError(f"side_id out of range: {side_id}")
        side_index = side_id % SIDES_PER_HEX
        tmp = side_id // SIDES_PER_HEX

        hex_index = tmp % HEXES_PER_FAMILY
        family_global = tmp // HEXES_PER_FAMILY

        area = family_global // FAMILIES_PER_AREA
        family_local = family_global % FAMILIES_PER_AREA

        return SideCoord(area=area, family_local=family_local, hex_index=hex_index, side_index=side_index)


def side_id_from_coord(area: int, family_local: int, hex_index: int, side_index: int) -> int:
    return SideCoord(
        area=clamp_int(area, 0, AREAS - 1),
        family_local=clamp_int(family_local, 0, FAMILIES_PER_AREA - 1),
        hex_index=clamp_int(hex_index, 0, HEXES_PER_FAMILY - 1),
        side_index=clamp_int(side_index, 0, SIDES_PER_HEX - 1),
    ).side_id()


def area_left(area_id: int) -> int:
    return (area_id - 1 + AREAS) % AREAS


def area_right(area_id: int) -> int:
    return (area_id + 1) % AREAS


def neighbors(
    side_id: int,
    *,
    allow_cross_area: bool = True,
    allow_new_family: bool = True,
    allow_radial: bool = True,
) -> list[int]:
    """Deterministic, bounded neighbor set for traversal.

    Note: full hex-sphere adjacency is more complex; this is a minimal deterministic
    neighborhood function suitable for region exploration + metrics.
    """
    c = SideCoord.from_side_id(side_id)
    out: list[int] = []

    # In-hex edge rotation
    out.append(side_id_from_coord(c.area, c.family_local, c.hex_index, (c.side_index + 1) % SIDES_PER_HEX))
    out.append(side_id_from_coord(c.area, c.family_local, c.hex_index, (c.side_index - 1) % SIDES_PER_HEX))

    if allow_radial:
        out.append(side_id_from_coord(c.area, c.family_local, c.hex_index + 1, c.side_index))
        out.append(side_id_from_coord(c.area, c.family_local, c.hex_index - 1, c.side_index))

    if allow_new_family:
        out.append(side_id_from_coord(c.area, (c.family_local + 1) % FAMILIES_PER_AREA, c.hex_index, c.side_index))
        out.append(side_id_from_coord(c.area, (c.family_local - 1) % FAMILIES_PER_AREA, c.hex_index, c.side_index))

    if allow_cross_area:
        out.append(side_id_from_coord(area_left(c.area), c.family_local, c.hex_index, c.side_index))
        out.append(side_id_from_coord(area_right(c.area), c.family_local, c.hex_index, c.side_index))

    return sorted(set(out))

