import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pymysql


@dataclass
class MysqlConfig:
    host: str
    port: int
    user: str
    password: str
    database: str


def _load_mysql_vars_from_env(prefix: str) -> dict:
    return {
        "host": os.environ.get(f"{prefix}HOST"),
        "port": os.environ.get(f"{prefix}PORT"),
        "user": os.environ.get(f"{prefix}USER"),
        "password": os.environ.get(f"{prefix}PASSWORD"),
        "database": os.environ.get(f"{prefix}DB"),
    }


def _load_mysql_vars_from_dotenv(prefix: str, repo_root: Path) -> dict:
    dotenv_path = repo_root / ".env"
    values: dict[str, Optional[str]] = {
        "host": None,
        "port": None,
        "user": None,
        "password": None,
        "database": None,
    }
    if not dotenv_path.is_file():
        return values

    text = dotenv_path.read_text(encoding="utf-8")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip("\"'")
        if not key.startswith(prefix):
            continue
        suffix = key[len(prefix) :]
        if suffix == "HOST":
            values["host"] = val
        elif suffix == "PORT":
            values["port"] = val
        elif suffix == "USER":
            values["user"] = val
        elif suffix == "PASSWORD":
            values["password"] = val
        elif suffix == "DB":
            values["database"] = val
    return values


def load_config_from_env(prefix: str = "MYSQL_") -> MysqlConfig:
    repo_root = Path(__file__).resolve().parents[1]
    env_vals = _load_mysql_vars_from_env(prefix)
    file_vals = _load_mysql_vars_from_dotenv(prefix, repo_root)

    host = env_vals["host"] or file_vals["host"] or "localhost"
    port_str = env_vals["port"] or file_vals["port"] or "3306"
    user = env_vals["user"] or file_vals["user"] or "root"
    password = env_vals["password"] or file_vals["password"] or ""
    database = env_vals["database"] or file_vals["database"] or "HSPR"

    port = int(port_str)
    return MysqlConfig(host=host, port=port, user=user, password=password, database=database)


def get_connection(cfg: Optional[MysqlConfig] = None):
    if cfg is None:
        cfg = load_config_from_env()
    return pymysql.connect(
        host=cfg.host,
        port=cfg.port,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database,
        charset="utf8mb4",
        autocommit=True,
    )


def ensure_author(cursor, name: str) -> int:
    cursor.execute("SELECT id FROM authors WHERE name = %s", (name,))
    row = cursor.fetchone()
    if row:
        return int(row[0])
    cursor.execute("INSERT INTO authors (name) VALUES (%s)", (name,))
    return int(cursor.lastrowid)


def ensure_book(
    cursor,
    title: str,
    author_id: int,
    code: Optional[str],
    chunks_json_path: str,
    statements_json_path: Optional[str],
) -> int:
    cursor.execute("SELECT id FROM books WHERE title = %s AND author_id = %s", (title, author_id))
    row = cursor.fetchone()
    if row:
        return int(row[0])
    cursor.execute(
        """
        INSERT INTO books (title, author_id, code, chunks_json_path, statements_json_path)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (title, author_id, code, chunks_json_path, statements_json_path),
    )
    return int(cursor.lastrowid)


def _extract_chunk_meta(chunk: dict) -> Optional[dict]:
    extra_keys = [k for k in chunk.keys() if k not in ("id", "text")]
    if not extra_keys:
        return None
    return {k: chunk[k] for k in extra_keys}


def load_chunks_for_book(
    conn,
    *,
    book_id: int,
    chunks: list[dict],
    chunks_json_relpath: str,
) -> int:
    with conn.cursor() as cursor:
        inserted = 0
        for chunk in chunks:
            json_id = int(chunk["id"])
            text = chunk["text"]
            meta_obj = _extract_chunk_meta(chunk)
            meta_json = json.dumps(meta_obj) if meta_obj is not None else None
            cursor.execute(
                """
                INSERT INTO chunks (book_id, json_id, text, meta, source_file_path)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE text = VALUES(text),
                                        meta = VALUES(meta),
                                        source_file_path = VALUES(source_file_path)
                """,
                (book_id, json_id, text, meta_json, chunks_json_relpath),
            )
            inserted += 1
    return inserted


def load_book_theory_of_moral_sentiments(
    repo_root: Path,
    *,
    cfg: Optional[MysqlConfig] = None,
) -> None:
    chunks_rel = "text_chunks/HSPR_CHUNKED_2_TMS_AS.json"
    statements_rel = "statements/2_TMS-AS.json"

    chunks_path = repo_root / chunks_rel
    statements_path = repo_root / statements_rel

    if not chunks_path.is_file():
        raise FileNotFoundError(f"Chunks JSON not found: {chunks_path}")

    if not statements_path.is_file():
        statements_rel = None

    obj = json.loads(chunks_path.read_text(encoding="utf-8"))
    title = obj.get("book", "The Theory of Moral Sentiments")
    author_name = obj.get("author", "Adam Smith")
    chunks = obj.get("chunks", [])

    conn = get_connection(cfg)
    try:
        with conn.cursor() as cursor:
            author_id = ensure_author(cursor, author_name)
            book_id = ensure_book(
                cursor,
                title=title,
                author_id=author_id,
                code="2_TMS-AS",
                chunks_json_path=chunks_rel,
                statements_json_path=statements_rel,
            )
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM chunks WHERE book_id = %s", (book_id,))
            (existing_count,) = cursor.fetchone()
        total_chunks = len(chunks)
        if existing_count >= total_chunks and total_chunks > 0:
            return
        load_chunks_for_book(
            conn,
            book_id=book_id,
            chunks=chunks,
            chunks_json_relpath=chunks_rel,
        )
    finally:
        conn.close()


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    load_book_theory_of_moral_sentiments(repo_root)


if __name__ == "__main__":
    main()
