"""
Example attribution and placement flow using MySQL.

This module demonstrates how to:
- Create a source statement row (in `statements`).
- Run a placeholder attribution step.
- Insert a semantic `statement` row and assign a side.

It is intentionally simple and uses a dummy attribution function so
that DB wiring can be tested before the full engine is ready.
"""

from dataclasses import dataclass
from typing import Optional

import pymysql

from .attribution_helper import SideCoord, insert_semantic_statement_from_source
from .mysql_loader import MysqlConfig, get_connection, load_config_from_env


@dataclass
class DummyAttributionResult:
    area_id: int
    family_id: int
    inward_vector: Optional[bytes]
    outward_vector: Optional[bytes]
    f_vector: Optional[bytes]
    a_vector: Optional[bytes]
    side_coord: SideCoord
    tau: float


def _dummy_attribution(text: str) -> DummyAttributionResult:
    """
    Placeholder attribution engine.

    Maps text length to a stable but arbitrary area/family and side
    coordinates. Real implementations must replace this with the
    semantic engine described in 12/13/15 specs.
    """
    # For now we pin everything to area 0, family 0 to keep the
    # example simple and compatible with a minimal area/family setup.
    length = max(len(text), 1)
    area_id = 0
    family_id = 0
    hex_index = length % 250
    side_index = length % 6
    side_id = ((family_id * 250) + hex_index) * 6 + side_index

    coord = SideCoord(
        area_id=area_id,
        family_id=family_id,
        hex_index=hex_index,
        side_index=side_index,
        side_id=side_id,
    )

    # Vectors are left as None; a real engine would serialize float arrays.
    return DummyAttributionResult(
        area_id=area_id,
        family_id=family_id,
        inward_vector=None,
        outward_vector=None,
        f_vector=None,
        a_vector=None,
        side_coord=coord,
        tau=1.0,
    )


def _ensure_area_family(
    conn: pymysql.connections.Connection,
    *,
    area_id: int,
    family_id: int,
) -> None:
    """
    Ensure minimal rows exist in `area` and `family` for the IDs that
    attribution will use. Names are placeholders; canonical mappings
    should be loaded separately from the families tables.
    """
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1 FROM area WHERE id = %s", (area_id,))
        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO area (id, name, ring_index) VALUES (%s, %s, %s)",
                (area_id, f"DUMMY_AREA_{area_id}", area_id),
            )

        cursor.execute("SELECT 1 FROM family WHERE id = %s", (family_id,))
        if cursor.fetchone() is None:
            cursor.execute(
                """
                INSERT INTO family (id, area_id, local_index, name)
                VALUES (%s, %s, %s, %s)
                """,
                (family_id, area_id, family_id, f"DUMMY_FAMILY_{family_id}"),
            )


def _ensure_source_statement_from_chunk(
    conn: pymysql.connections.Connection,
    *,
    book_code: str,
    chunk_json_id: int,
) -> int:
    """
    Create (or reuse) a row in `statements` based on an existing chunk.

    This is a convenience for testing attribution/placement before a
    dedicated statements JSON ingestion pipeline is added.
    """
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, book_id
            FROM statements
            WHERE book_id = (
                SELECT id FROM books WHERE code = %s
            )
              AND chunk_json_id = %s
            LIMIT 1
            """,
            (book_code, chunk_json_id),
        )
        row = cursor.fetchone()
        if row:
            return int(row[0])

        cursor.execute(
            """
            SELECT book_id, text, source_file_path
            FROM chunks
            WHERE book_id = (SELECT id FROM books WHERE code = %s)
              AND json_id = %s
            LIMIT 1
            """,
            (book_code, chunk_json_id),
        )
        chunk_row = cursor.fetchone()
        if not chunk_row:
            raise ValueError(f"No chunk found for book_code={book_code}, json_id={chunk_json_id}")

        book_id, text, source_file_path = int(chunk_row[0]), chunk_row[1], chunk_row[2]

        cursor.execute(
            """
            INSERT INTO statements (
                book_id,
                chunk_json_id,
                json_id,
                text,
                source_file_path
            )
            VALUES (
                (SELECT id FROM books WHERE code = %s),
                %s,
                %s,
                %s,
                %s
            )
            """,
            (book_code, chunk_json_id, chunk_json_id, text, source_file_path),
        )
        return int(cursor.lastrowid)


def run_example_for_first_chunk(
    *,
    cfg: Optional[MysqlConfig] = None,
    book_code: str = "2_TMS-AS",
    chunk_json_id: int = 1,
) -> int:
    """
    End-to-end example:
    - Pick a chunk by (book_code, chunk_json_id).
    - Ensure a corresponding source statement row.
    - Run dummy attribution.
    - Insert semantic statement and assign a side.

    Returns:
        semantic_statement_id created (or reused) by this run.
    """
    if cfg is None:
        cfg = load_config_from_env()
    conn = get_connection(cfg)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT text
                FROM chunks
                WHERE book_id = (SELECT id FROM books WHERE code = %s)
                  AND json_id = %s
                LIMIT 1
                """,
                (book_code, chunk_json_id),
            )
            row = cursor.fetchone()
            if not row:
                raise ValueError(f"No chunk found for book_code={book_code}, json_id={chunk_json_id}")
            text = row[0]

        source_statement_id = _ensure_source_statement_from_chunk(
            conn,
            book_code=book_code,
            chunk_json_id=chunk_json_id,
        )

        attrib = _dummy_attribution(text)

        _ensure_area_family(
            conn,
            area_id=attrib.area_id,
            family_id=attrib.family_id,
        )

        semantic_id = insert_semantic_statement_from_source(
            source_statement_id=source_statement_id,
            raw_text=text,
            area_id=attrib.area_id,
            family_id=attrib.family_id,
            inward_vector=attrib.inward_vector,
            outward_vector=attrib.outward_vector,
            f_vector=attrib.f_vector,
            a_vector=attrib.a_vector,
            side_coord=attrib.side_coord,
            tau=attrib.tau,
            cfg=cfg,
        )

        return semantic_id
    finally:
        conn.close()


def main() -> None:
    cfg = load_config_from_env()
    semantic_id = run_example_for_first_chunk(cfg=cfg)
    print(f"Inserted semantic statement with id={semantic_id}")


if __name__ == "__main__":
    main()
