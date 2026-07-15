from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import tempfile
from contextlib import closing
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

from .errors import ImmutableContentError, NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document, render_document


OBJECT_TYPES = {
    "source", "intuition", "entity", "concept", "claim", "question",
    "tension", "analogy", "hypothesis", "project", "decision",
    "experiment", "failure", "opportunity", "synthesis", "work", "proposal",
}
RELATION_TYPES = {
    "supports", "contradicts", "refines", "analogous_to", "derived_from",
    "applied_in", "raises", "supersedes", "related_to",
}
CONFIDENCE_LEVELS = {"unknown", "low", "medium", "high"}
EVIDENCE_STANCES = {"supports", "contradicts", "context"}
EVIDENCE_KINDS = {"quote", "paraphrase", "translation", "table_value", "figure", "calculation"}
CANONICAL_ROOTS = ("knowledge", "frontier", "action")
TZ = ZoneInfo("Asia/Shanghai")


def now_iso() -> str:
    return datetime.now(TZ).isoformat(timespec="seconds")


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def slugify(value: str, fallback: str = "untitled") -> str:
    value = re.sub(r"[^\w\-\u4e00-\u9fff]+", "-", value, flags=re.UNICODE).strip("-_").lower()
    return (value[:64] or fallback)


@dataclass(frozen=True)
class SearchResult:
    id: str
    type: str
    title: str
    path: str
    status: str
    source_ids: list[str]
    snippet: str


class Repository:
    def __init__(self, root: Path | str):
        self.root = Path(root).resolve()
        self.index_path = self.root / "data" / "indexes" / "global_memory.sqlite3"

    def rel(self, path: Path) -> str:
        return path.resolve().relative_to(self.root).as_posix()

    def resolve_inside(self, relative_path: str) -> Path:
        candidate = (self.root / relative_path).resolve()
        try:
            candidate.relative_to(self.root)
        except ValueError as exc:
            raise ValidationError(f"路径越出仓库: {relative_path}") from exc
        return candidate

    def init(self) -> None:
        directories = [
            "vault/raw/objects/sha256",
            "vault/raw/web/content", "vault/raw/files/content", "vault/raw/files/blobs",
            "vault/raw/personal-notes/content", "vault/knowledge/entities",
            "vault/knowledge/concepts", "vault/knowledge/claims", "vault/knowledge/patterns",
            "vault/knowledge/works",
            "vault/knowledge/comparisons", "vault/knowledge/syntheses",
            "vault/frontier/intuitions", "vault/frontier/questions", "vault/frontier/tensions",
            "vault/frontier/analogies", "vault/frontier/hypotheses", "vault/frontier/anomalies",
            "vault/action/projects", "vault/action/decisions", "vault/action/experiments",
            "vault/action/failures", "vault/action/opportunities", "vault/proposals",
            "vault/archive", "data/imports", "data/derived", "data/indexes", "data/backups",
            "system/logs", "system/reports", "system/error-book",
            "system/recovery",
            "data/derived/extractions",
        ]
        for directory in directories:
            (self.root / directory).mkdir(parents=True, exist_ok=True)
        self.rebuild_index()

    def content_object_path(self, digest: str) -> Path:
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValidationError(f"非法 SHA-256: {digest}")
        return self.root / "vault" / "raw" / "objects" / "sha256" / digest[:2] / digest[2:4] / digest

    def ensure_initialized(self) -> None:
        if not (self.root / "vault").is_dir():
            raise ValidationError(f"尚未初始化 Global Memory 仓库: {self.root}")
        if not self.index_path.exists():
            self.rebuild_index()

    def append_event(self, name: str, payload: dict[str, Any]) -> None:
        log_path = self.root / "system" / "logs" / f"{name}.jsonl"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        record = {"at": now_iso(), **payload}
        with log_path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())

    def immutable_write(self, path: Path, content: bytes) -> bool:
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with path.open("xb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            return True
        except FileExistsError:
            if path.read_bytes() != content:
                raise ImmutableContentError(f"拒绝覆盖不可变 raw 内容: {self.rel(path)}")
            return False

    def source_documents(self) -> Iterable[Path]:
        raw = self.root / "vault" / "raw"
        if raw.exists():
            yield from raw.rglob("source-*.md")

    def canonical_documents(self) -> Iterable[Path]:
        vault = self.root / "vault"
        for root_name in CANONICAL_ROOTS:
            path = vault / root_name
            if path.exists():
                yield from path.rglob("*.md")

    def archive_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "archive"
        if path.exists():
            yield from path.rglob("*.md")

    def proposal_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "proposals"
        if path.exists():
            yield from path.glob("proposal-*.md")

    def all_indexed_documents(self) -> Iterable[Path]:
        yield from self.source_documents()
        yield from self.canonical_documents()

    def _schema(self, connection: sqlite3.Connection) -> None:
        connection.executescript(
            """
            PRAGMA journal_mode=WAL;
            CREATE TABLE documents (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL,
                path TEXT NOT NULL UNIQUE,
                source_ids TEXT NOT NULL,
                body TEXT NOT NULL,
                tags TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            CREATE TABLE relations (
                source_id TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                target_id TEXT NOT NULL,
                reason TEXT NOT NULL,
                PRIMARY KEY (source_id, relation_type, target_id)
            );
            CREATE VIRTUAL TABLE documents_fts USING fts5(
                id UNINDEXED, title, body, tags, tokenize='unicode61'
            );
            """
        )

    def _document_index_body(self, path: Path, metadata: dict[str, Any], body: str) -> str:
        if metadata.get("type") != "source":
            return body
        raw_path = metadata.get("raw_content_path")
        if not raw_path:
            return body
        payload = self.resolve_inside(str(raw_path))
        if not payload.exists() or payload.stat().st_size > 5_000_000:
            return body
        try:
            return body + "\n\n" + payload.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return body

    def _validate_metadata(self, metadata: dict[str, Any], path: Path) -> None:
        required = {"id", "type", "status", "title", "created_at", "updated_at"}
        missing = sorted(required - metadata.keys())
        if missing:
            raise ValidationError(f"{self.rel(path)} 缺少字段: {', '.join(missing)}")
        if metadata["type"] not in OBJECT_TYPES:
            raise ValidationError(f"{self.rel(path)} 使用非法对象类型: {metadata['type']}")
        if metadata.get("confidence") not in CONFIDENCE_LEVELS:
            raise ValidationError(f"{self.rel(path)} 使用非法 confidence: {metadata.get('confidence')}")
        source_ids = metadata.get("source_ids", [])
        if not isinstance(source_ids, list) or not all(isinstance(source_id, str) and source_id for source_id in source_ids):
            raise ValidationError(f"{self.rel(path)} 的 source_ids 必须是非空字符串列表")
        for relation in metadata.get("relations", []):
            relation_type = relation.get("type") if isinstance(relation, dict) else None
            if relation_type not in RELATION_TYPES:
                raise ValidationError(f"{self.rel(path)} 使用非法关系类型: {relation_type}")
            if not relation.get("target_id") or not relation.get("reason"):
                raise ValidationError(f"{self.rel(path)} 的关系缺少 target_id 或 reason")
        if metadata["type"] == "claim":
            if "applicability" in metadata:
                applicability = metadata["applicability"]
                if not isinstance(applicability, list) or not all(
                    isinstance(condition, str) and condition.strip() for condition in applicability
                ):
                    raise ValidationError(f"{self.rel(path)} 的 applicability 必须是非空文本列表")
            if "uncertainty" in metadata and (
                not isinstance(metadata["uncertainty"], str) or not metadata["uncertainty"].strip()
            ):
                raise ValidationError(f"{self.rel(path)} 的 uncertainty 必须是非空文本")
            if "evidence" in metadata:
                evidence = metadata["evidence"]
                if not isinstance(evidence, list):
                    raise ValidationError(f"{self.rel(path)} 的 evidence 必须是列表")
                evidence_ids: set[str] = set()
                for item in evidence:
                    if not isinstance(item, dict):
                        raise ValidationError(f"{self.rel(path)} 的 evidence 条目必须是对象")
                    if item.get("source_id") not in source_ids:
                        raise ValidationError(f"{self.rel(path)} 的 evidence 必须引用 source_ids 中的来源")
                    if item.get("stance") not in EVIDENCE_STANCES:
                        raise ValidationError(f"{self.rel(path)} 的 evidence stance 非法")
                    evidence_kind = item.get("evidence_kind")
                    if evidence_kind is not None:
                        if evidence_kind not in EVIDENCE_KINDS:
                            raise ValidationError(f"{self.rel(path)} 的 evidence_kind 非法: {evidence_kind}")
                        evidence_id = item.get("evidence_id")
                        if not isinstance(evidence_id, str) or not evidence_id:
                            raise ValidationError(f"{self.rel(path)} 的结构化 evidence 缺少 evidence_id")
                        if evidence_id in evidence_ids:
                            raise ValidationError(f"{self.rel(path)} 的 evidence_id 重复: {evidence_id}")
                        evidence_ids.add(evidence_id)
                        self._validate_typed_evidence(item, path)
                    for key in ("location", "excerpt", "reason"):
                        if evidence_kind is None and (
                            not isinstance(item.get(key), str) or not item[key].strip()
                        ):
                            raise ValidationError(f"{self.rel(path)} 的 evidence 缺少 {key}")
                for item in evidence:
                    if item.get("evidence_kind") == "calculation":
                        inputs = item.get("input_evidence_ids")
                        if not isinstance(inputs, list) or not inputs or not set(inputs) <= evidence_ids:
                            raise ValidationError(f"{self.rel(path)} 的 calculation 输入 evidence 无效")

    def _validate_typed_evidence(self, item: dict[str, Any], path: Path) -> None:
        kind = item["evidence_kind"]
        for key in ("verification_status", "input_sha256", "reason"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValidationError(f"{self.rel(path)} 的 {kind} evidence 缺少 {key}")
        if kind == "quote":
            required = ("extraction_id", "span_start", "span_end", "original_text")
            if any(item.get(key) is None for key in required):
                raise ValidationError(f"{self.rel(path)} 的 quote 缺少 extraction/span/original_text")
            from .extraction import ExtractionService
            extraction_service = ExtractionService(self)
            _, extraction, _ = extraction_service.find(str(item["extraction_id"]))
            if (
                extraction.get("source_id") != item.get("source_id")
                or extraction.get("input_sha256") != item.get("input_sha256")
                or (item.get("content_id") and extraction.get("content_id") != item.get("content_id"))
            ):
                raise ValidationError(f"{self.rel(path)} 的 quote provenance 与 extraction 不一致")
            if not extraction_service.verify_span(
                str(item["extraction_id"]), int(item["span_start"]),
                int(item["span_end"]), str(item["original_text"]),
            ):
                raise ValidationError(f"{self.rel(path)} 的 quote 无法回验 extraction span")
        elif kind == "paraphrase":
            if not item.get("interpretation") or not any(item.get(key) is not None for key in ("page", "section", "span_start")):
                raise ValidationError(f"{self.rel(path)} 的 paraphrase 缺少转述内容或来源位置")
            if str(item.get("verification_status", "")).lower() in {"verbatim", "exact-quote"}:
                raise ValidationError(f"{self.rel(path)} 的 paraphrase 不能标记为逐字 quote")
        elif kind == "translation":
            if not item.get("original_text") or not item.get("translated_text") or not item.get("target_language"):
                raise ValidationError(f"{self.rel(path)} 的 translation 必须保留原文、译文和目标语言")
            if not any(item.get(key) is not None for key in ("page", "section", "span_start")):
                raise ValidationError(f"{self.rel(path)} 的 translation 缺少原文位置")
        elif kind == "table_value":
            if item.get("value") is None or not item.get("unit") or not any(item.get(key) is not None for key in ("table", "page")):
                raise ValidationError(f"{self.rel(path)} 的 table_value 必须保留数值、单位和表格/页码")
        elif kind == "figure":
            if not item.get("figure") or item.get("page") is None or not item.get("interpretation"):
                raise ValidationError(f"{self.rel(path)} 的 figure 必须保留图号、页码和解释")
        elif kind == "calculation":
            if not item.get("calculation_method") or item.get("result") is None:
                raise ValidationError(f"{self.rel(path)} 的 calculation 缺少方法或结果")

    def rebuild_index(self) -> int:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        fd, temp_name = tempfile.mkstemp(prefix="global-memory-", suffix=".sqlite3", dir=self.index_path.parent)
        os.close(fd)
        temp_path = Path(temp_name)
        temp_path.unlink(missing_ok=True)
        count = 0
        try:
            with closing(sqlite3.connect(temp_path)) as connection:
                self._schema(connection)
                for path in sorted(self.all_indexed_documents()):
                    metadata, body = read_document(path)
                    self._validate_metadata(metadata, path)
                    source_ids = metadata.get("source_ids", [])
                    if metadata.get("type") == "source":
                        source_ids = [metadata["id"]]
                    index_body = self._document_index_body(path, metadata, body)
                    tags = " ".join(str(item) for item in metadata.get("tags", []))
                    values = (
                        metadata["id"], metadata["type"], metadata["title"],
                        metadata["status"], self.rel(path), json.dumps(source_ids, ensure_ascii=False),
                        index_body, tags, metadata["updated_at"],
                    )
                    connection.execute("INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
                    connection.execute(
                        "INSERT INTO documents_fts(id, title, body, tags) VALUES (?, ?, ?, ?)",
                        (metadata["id"], metadata["title"], index_body, tags),
                    )
                    for relation in metadata.get("relations", []):
                        connection.execute(
                            "INSERT INTO relations VALUES (?, ?, ?, ?)",
                            (metadata["id"], relation["type"], relation["target_id"], relation["reason"]),
                        )
                    count += 1
                connection.commit()
            os.replace(temp_path, self.index_path)
            return count
        finally:
            temp_path.unlink(missing_ok=True)

    def search(self, query: str, limit: int = 20) -> list[SearchResult]:
        self.ensure_initialized()
        query = query.strip()
        if not query:
            raise ValidationError("搜索词不能为空")
        fts_query = " ".join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in query.split())
        with closing(sqlite3.connect(self.index_path)) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                """
                SELECT d.*, snippet(documents_fts, 2, '[', ']', '…', 18) AS snippet
                FROM documents_fts JOIN documents d ON d.id = documents_fts.id
                WHERE documents_fts MATCH ? LIMIT ?
                """,
                (fts_query, limit),
            ).fetchall()
            seen = {row["id"] for row in rows}
            if len(rows) < limit:
                like = f"%{query}%"
                fallback = connection.execute(
                    "SELECT *, substr(body, 1, 240) AS snippet FROM documents "
                    "WHERE (title LIKE ? OR body LIKE ?) LIMIT ?",
                    (like, like, limit),
                ).fetchall()
                rows.extend(row for row in fallback if row["id"] not in seen)
        return [
            SearchResult(
                id=row["id"], type=row["type"], title=row["title"], path=row["path"],
                status=row["status"],
                source_ids=json.loads(row["source_ids"]), snippet=row["snippet"] or "",
            )
            for row in rows[:limit]
        ]

    def find_document(self, object_id: str) -> tuple[Path, dict[str, Any], str]:
        candidates = list(self.all_indexed_documents()) + list(self.proposal_documents())
        candidates += list((self.root / "vault" / "proposals").glob("candidate-*.md"))
        for path in candidates:
            metadata, body = read_document(path)
            if metadata.get("id") == object_id:
                return path, metadata, body
        raise NotFoundError(f"未找到对象: {object_id}")

    def related(self, object_id: str) -> list[dict[str, str]]:
        self.ensure_initialized()
        with closing(sqlite3.connect(self.index_path)) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                """
                SELECT source_id, relation_type, target_id, reason FROM relations
                WHERE source_id = ? OR target_id = ? ORDER BY source_id, relation_type
                """,
                (object_id, object_id),
            ).fetchall()
        return [dict(row) for row in rows]

    def count_by_type(self) -> dict[str, int]:
        self.ensure_initialized()
        with closing(sqlite3.connect(self.index_path)) as connection:
            rows = connection.execute("SELECT type, count(*) FROM documents GROUP BY type").fetchall()
        return {kind: count for kind, count in rows}
