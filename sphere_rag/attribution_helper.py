from dataclasses import dataclass
from typing import Optional

from .mysql_loader import MysqlConfig, get_connection


@dataclass
class SideCoord:
    area_id: int
    family_id: int
    hex_index: int
    side_index: int
    side_id: int


def insert_semantic_statement_from_source(
    source_statement_id: int,
    raw_text: str,
    area_id: int,
    family_id: int,
    *,
    inward_vector: Optional[bytes] = None,
    outward_vector: Optional[bytes] = None,
    f_vector: Optional[bytes] = None,
    a_vector: Optional[bytes] = None,
    side_coord: Optional[SideCoord] = None,
    tau: float = 0.0,
    cfg: Optional[MysqlConfig] = None,
) -> int:
    """
    Create a semantic `statement` row from a source `statements` row and
    optionally assign it to a side.

    This helper performs only DB operations. The caller is responsible
    for computing:
    - Attribution (area_id, family_id, vectors).
    - Geometry/indexing (side_id, hex_index, side_index).
    """
    conn = get_connection(cfg)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO statement (
                    raw_text,
                    area_id,
                    family_id,
                    inward_vector,
                    outward_vector,
                    f_vector,
                    a_vector
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    raw_text,
                    area_id,
                    family_id,
                    inward_vector,
                    outward_vector,
                    f_vector,
                    a_vector,
                ),
            )
            semantic_id = int(cursor.lastrowid)

            cursor.execute(
                """
                UPDATE statements
                SET semantic_statement_id = %s
                WHERE id = %s
                """,
                (semantic_id, source_statement_id),
            )

            if side_coord is not None:
                cursor.execute(
                    """
                    INSERT INTO side (
                        side_id,
                        area_id,
                        family_id,
                        hex_index,
                        side_index,
                        tau,
                        statement_id
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        tau = VALUES(tau),
                        statement_id = VALUES(statement_id),
                        last_updated = CURRENT_TIMESTAMP
                    """,
                    (
                        side_coord.side_id,
                        side_coord.area_id,
                        side_coord.family_id,
                        side_coord.hex_index,
                        side_coord.side_index,
                        float(tau),
                        semantic_id,
                    ),
                )

        return semantic_id
    finally:
        conn.close()

