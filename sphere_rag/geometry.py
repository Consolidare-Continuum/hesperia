from dataclasses import dataclass
from typing import List


AREAS = 12
FAMILIES_PER_AREA = 24
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6

TOTAL_FAMILIES = AREAS * FAMILIES_PER_AREA
TOTAL_HEXES = TOTAL_FAMILIES * HEXES_PER_FAMILY
TOTAL_SIDES = TOTAL_HEXES * SIDES_PER_HEX


@dataclass
class HexSide:
    """
    Canonical coordinate for a side on the sphere.

    All indices are 0-based and match the Java-style math:
    - area:          0..11
    - family_local:  0..23  (family index within the area)
    - hex_index:     0..249
    - side_index:    0..5   (hexagon side)
    """

    area: int
    family_local: int
    hex_index: int
    side_index: int
    tau: float = 0.0  # truth weight in [0,1]

    @property
    def family_global(self) -> int:
        """Family index in [0, TOTAL_FAMILIES)."""
        return self.area * FAMILIES_PER_AREA + self.family_local

    @property
    def side_id(self) -> int:
        """
        Linear index in [0, TOTAL_SIDES).

        This is the canonical 1D index used for arrays like tau[sideId].
        """
        fam = self.family_global
        return (((fam * HEXES_PER_FAMILY) + self.hex_index) * SIDES_PER_HEX) + self.side_index

    def human_label(self) -> str:
        """
        Human-readable coordinate, stable and sortable.

        Example: A01-F05-H123-S2
        Areas/Families/Hexes are printed 1-based for humans.
        """
        return f"A{self.area + 1:02d}-F{self.family_local + 1:02d}-H{self.hex_index + 1:03d}-S{self.side_index}"


def side_from_id(side_id: int) -> HexSide:
    """
    Inverse of HexSide.side_id().

    Takes a 0-based linear side_id in [0, TOTAL_SIDES) and returns
    the corresponding HexSide coordinate.
    """
    side_index = side_id % SIDES_PER_HEX
    tmp = side_id // SIDES_PER_HEX

    hex_index = tmp % HEXES_PER_FAMILY
    fam_global = tmp // HEXES_PER_FAMILY

    area = fam_global // FAMILIES_PER_AREA
    family_local = fam_global % FAMILIES_PER_AREA

    return HexSide(
        area=area,
        family_local=family_local,
        hex_index=hex_index,
        side_index=side_index,
    )


@dataclass
class SphereRegion:
    """A connected semantic region on the sphere."""

    active_sides: List[HexSide]

    def area_activation(self) -> List[float]:
        vec = [0.0] * AREAS
        for side in self.active_sides:
            vec[side.area] += side.tau
        total = sum(vec) or 1.0
        return [v / total for v in vec]

    def family_activation(self) -> List[float]:
        vec = [0.0] * TOTAL_FAMILIES
        for side in self.active_sides:
            idx = side.family_global
            vec[idx] += side.tau
        total = sum(vec) or 1.0
        return [v / total for v in vec]


class GeometryService:
    """
    Responsible for mapping StatementAttributions into discrete sphere locations
    and building regions for traversal.
    """

    def locate_statement(self, area: int, family: int) -> HexSide:
        """
        Map a classified statement (area, family) to a concrete side.

        `family` is assumed to be the global family id in [0, TOTAL_FAMILIES).
        Area is checked against the family-derived area for safety.
        """
        derived_area = family // FAMILIES_PER_AREA
        family_local = family % FAMILIES_PER_AREA
        if derived_area != area:
            area = derived_area

        # For the prototype we place each statement on a canonical hex/side.
        return HexSide(
            area=area,
            family_local=family_local,
            hex_index=0,
            side_index=0,
            tau=1.0,
        )

    def build_region(self, seed: HexSide) -> SphereRegion:
        # Prototype: region = just the seed
        return SphereRegion(active_sides=[seed])
