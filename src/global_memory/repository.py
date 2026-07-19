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
from .epistemics import EPISTEMIC_STATUSES
from .markdown import atomic_write_text, read_document, render_document


OBJECT_TYPES = {
    "source", "intuition", "entity", "concept", "claim", "question",
    "tension", "analogy", "anomaly", "hypothesis", "project", "goal", "architecture", "decision",
    "experiment", "failure", "opportunity", "synthesis", "work", "proposal", "followup",
    "exception", "promotion", "annotation", "input", "reflection",
}
RELATION_TYPES = {
    "supports", "contradicts", "refines", "analogous_to", "derived_from",
    "applied_in", "raises", "supersedes", "related_to", "limits", "defines",
    "instantiates", "answers", "tested_by", "failed_in", "depends_on", "part_of",
}
CONFIDENCE_LEVELS = {"unknown", "low", "medium", "high"}
EVIDENCE_STANCES = {"supports", "contradicts", "context"}
EVIDENCE_KINDS = {"quote", "paraphrase", "translation", "table_value", "figure", "calculation"}
CANONICAL_ROOTS = ("knowledge", "frontier", "action")
MEMORY_STATUSES = {"working", "trusted", "canonical", "contested", "superseded", "archived"}
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
    match_reason: str = "full-text"


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
            "vault/raw/wechat", "vault/raw/personal-notes/content", "vault/knowledge/entities",
            "vault/knowledge/concepts", "vault/knowledge/claims", "vault/knowledge/patterns",
            "vault/knowledge/works",
            "vault/knowledge/comparisons", "vault/knowledge/syntheses",
            "vault/frontier/intuitions", "vault/frontier/questions", "vault/frontier/tensions",
            "vault/frontier/analogies", "vault/frontier/hypotheses", "vault/frontier/anomalies",
            "vault/action/projects", "vault/action/decisions", "vault/action/experiments",
            "vault/action/goals", "vault/action/architectures",
            "vault/action/failures", "vault/action/opportunities", "vault/proposals",
            "vault/memory", "vault/exceptions", "vault/promotions",
            "vault/archive", "data/imports", "data/derived", "data/indexes", "data/backups",
            "system/logs", "system/reports", "system/error-book",
            "system/recovery", "system/runs", "vault/followups", "vault/annotations",
            "vault/annotations/research", "vault/views/research",
            "vault/views", "vault/receipts", "vault/inputs", "vault/reflections", "vault/synthesis",
            "data/derived/extractions", "data/derived/quality",
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

    def memory_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "memory"
        if path.exists():
            yield from path.rglob("*.md")

    def active_memory_documents(self) -> Iterable[Path]:
        """Return routine-maintenance memory, preserving historical files for audit only."""
        for path in self.memory_documents():
            metadata, _ = read_document(path)
            if metadata.get("memory_tier") not in {"working", "trusted"}:
                continue
            if metadata.get("status") in {"archived", "superseded"}:
                continue
            yield path

    def archive_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "archive"
        if path.exists():
            yield from path.rglob("*.md")

    def proposal_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "proposals"
        if path.exists():
            yield from path.glob("proposal-*.md")

    def followup_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "followups"
        if path.exists():
            yield from path.glob("followup-*.md")

    def annotation_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "annotations" / "research"
        if path.exists():
            yield from path.glob("annotation-*.md")

    def input_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "inputs"
        if path.exists():
            yield from path.glob("input-*.md")

    def reflection_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "reflections"
        if path.exists():
            yield from path.glob("reflection-*.md")

    def synthesis_documents(self) -> Iterable[Path]:
        path = self.root / "vault" / "synthesis"
        if path.exists():
            yield from path.glob("synthesis-*.md")

    def all_indexed_documents(self) -> Iterable[Path]:
        yield from self.source_documents()
        yield from self.memory_documents()
        yield from self.canonical_documents()
        yield from self.annotation_documents()
        yield from self.input_documents()
        yield from self.reflection_documents()
        yield from self.synthesis_documents()

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
                aliases TEXT NOT NULL,
                tags TEXT NOT NULL,
                domains TEXT NOT NULL,
                source_kind TEXT NOT NULL,
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
                id UNINDEXED, title, aliases, tags, domains, body, tokenize='unicode61'
            );
            CREATE TABLE activation_events (
                event_id TEXT PRIMARY KEY,
                object_id TEXT NOT NULL,
                event_kind TEXT NOT NULL,
                project_id TEXT,
                created_at TEXT NOT NULL,
                payload TEXT NOT NULL
            );
            CREATE TABLE activation_aggregates (
                object_id TEXT PRIMARY KEY,
                selected_count INTEGER NOT NULL,
                opened_count INTEGER NOT NULL,
                used_count INTEGER NOT NULL,
                cited_count INTEGER NOT NULL,
                coactivated_count INTEGER NOT NULL,
                last_used_at TEXT,
                projects TEXT NOT NULL
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
        try:
            relative = self.rel(path)
        except ValueError:
            # Explicit CLI candidate files may live outside the repository. They
            # are validated before being copied into the governed proposal layer.
            relative = str(path)
        if relative.startswith("vault/memory/"):
            if metadata.get("status") not in MEMORY_STATUSES:
                raise ValidationError(f"{relative} 使用非法 memory status: {metadata.get('status')}")
            if metadata.get("memory_tier") not in {"working", "trusted", "historical"}:
                raise ValidationError(f"{relative} 缺少有效 memory_tier")
            if metadata.get("memory_tier") == "historical" and metadata.get("status") not in {"archived", "superseded"}:
                raise ValidationError(f"{relative} historical memory must be archived or superseded")
            if metadata.get("epistemic_status") not in EPISTEMIC_STATUSES:
                raise ValidationError(f"{relative} missing valid epistemic_status")
            for key in ("created_by", "updated_by", "consolidation_count", "promotion_history"):
                if key not in metadata:
                    raise ValidationError(f"{relative} 缺少 lifecycle field: {key}")
        elif metadata.get("type") == "exception" and metadata.get("status") not in {"open", "resolved", "deferred", "dismissed"}:
            raise ValidationError(f"{relative} 使用非法 exception status")
        elif metadata.get("type") == "promotion" and metadata.get("status") not in {"pending", "approved", "rejected", "deferred"}:
            raise ValidationError(f"{relative} 使用非法 promotion status")
        if metadata.get("type") == "annotation":
            if metadata.get("status") != "active":
                raise ValidationError(f"{relative} annotation status 必须是 active")
            if metadata.get("annotation_kind") not in {"capture_intent", "connection_feedback", "research_note"}:
                raise ValidationError(f"{relative} annotation_kind 非法")
            if metadata.get("user_authored") is not True:
                raise ValidationError(f"{relative} annotation 必须保留 user_authored=true")
            if not isinstance(metadata.get("target_ids", []), list):
                raise ValidationError(f"{relative} target_ids 必须是列表")
        if metadata.get("type") == "input":
            if metadata.get("status") != "active" or metadata.get("truth_layer") != "input_episode":
                raise ValidationError(f"{relative} input must remain active in the input_episode truth layer")
            if metadata.get("input_type") not in {
                "article", "paper", "github", "conversation", "idea", "experiment", "meeting",
            }:
                raise ValidationError(f"{relative} invalid input_type")
            if metadata.get("memory_tier") or metadata.get("epistemic_status"):
                raise ValidationError(f"{relative} input cannot carry Memory Tier or Epistemic Status")
        if metadata.get("type") == "reflection":
            if metadata.get("status") != "active" or metadata.get("truth_layer") != "reflection":
                raise ValidationError(f"{relative} reflection must remain active in the reflection truth layer")
            if metadata.get("created_by") not in {"agent", "user"}:
                raise ValidationError(f"{relative} reflection created_by must be agent or user")
            if metadata.get("memory_tier") or metadata.get("epistemic_status"):
                raise ValidationError(f"{relative} reflection cannot carry Memory Tier or Epistemic Status")
            if not isinstance(metadata.get("target_ids"), list) or not metadata.get("target_ids"):
                raise ValidationError(f"{relative} reflection requires target_ids")
        if metadata.get("type") == "synthesis" and relative.startswith("vault/synthesis/"):
            if metadata.get("status") != "active" or metadata.get("truth_layer") != "cognitive_synthesis":
                raise ValidationError(f"{relative} cognitive synthesis must remain active and explicitly labeled")
            if metadata.get("memory_tier") or metadata.get("epistemic_status"):
                raise ValidationError(f"{relative} cognitive synthesis cannot carry Memory Tier or Epistemic Status")
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
            governance = {"confidence", "created_by", "status"}
            if governance & set(relation) and not governance <= set(relation):
                raise ValidationError(f"{self.rel(path)} 的 M6 relation 缺少 confidence/created_by/status")
        if metadata["type"] == "claim":
            if metadata.get("atomicity_status") not in {None, "atomic", "compound", "uncertain"}:
                raise ValidationError(f"{self.rel(path)} 的 atomicity_status 非法")
            if metadata.get("evidence_coverage") not in {None, "full", "partial", "missing"}:
                raise ValidationError(f"{self.rel(path)} 的 evidence_coverage 非法")
            for key, allowed in {
                "quote_verification": {"exact", "normalized_match", "failed", "not_applicable"},
                "extraction_quality": {"good", "degraded", "failed"},
                "epistemic_source_authority": {"primary", "official", "peer_reviewed", "secondary", "commentary", "anecdotal", "unknown"},
                "evidence_entailment": {"full", "partial", "indirect", "conflicting", "none"},
                "claim_confidence": {"high", "medium", "low", "unknown"},
            }.items():
                if metadata.get(key) not in {None, *allowed}:
                    raise ValidationError(f"{self.rel(path)} 的 {key} 非法")
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
            try:
                _, extraction, _ = extraction_service.find(str(item["extraction_id"]))
            except NotFoundError:
                relative = self.rel(path)
                if not relative.startswith(("vault/memory/", "vault/knowledge/", "vault/frontier/", "vault/action/")):
                    raise ValidationError(f"{relative} 的 quote extraction 不存在")
                _, source, _ = self.find_document(str(item.get("source_id")))
                if (
                    source.get("content_sha256") != item.get("input_sha256")
                    or (item.get("content_id") and source.get("content_id") != item.get("content_id"))
                ):
                    raise ValidationError(f"{relative} 的 quote provenance 与 source 不一致")
                # Derived extraction is deliberately deletable. Canonical Markdown and raw
                # remain index-rebuildable; exact span is rechecked when extraction is rebuilt.
                return
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
                    aliases = " ".join(str(item) for item in metadata.get("aliases", []))
                    domains = " ".join(str(item) for item in metadata.get("domains", []))
                    values = (
                        metadata["id"], metadata["type"], metadata["title"],
                        metadata["status"], self.rel(path), json.dumps(source_ids, ensure_ascii=False),
                        index_body, aliases, tags, domains, str(metadata.get("source_kind", "")),
                        metadata["updated_at"],
                    )
                    connection.execute("INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)
                    connection.execute(
                        "INSERT INTO documents_fts(id, title, aliases, tags, domains, body) VALUES (?, ?, ?, ?, ?, ?)",
                        (metadata["id"], metadata["title"], aliases, tags, domains, index_body),
                    )
                    for relation in metadata.get("relations", []):
                        connection.execute(
                            "INSERT INTO relations VALUES (?, ?, ?, ?)",
                            (metadata["id"], relation["type"], relation["target_id"], relation["reason"]),
                        )
                    count += 1
                activation_path = self.root / "system" / "logs" / "activation-events.jsonl"
                activation_totals: dict[str, dict[str, Any]] = {}
                if activation_path.exists():
                    for line in activation_path.read_text(encoding="utf-8").splitlines():
                        if not line.strip():
                            continue
                        try:
                            event = json.loads(line)
                        except json.JSONDecodeError:
                            continue
                        if not isinstance(event, dict) or not event.get("event_id") or not event.get("object_id"):
                            continue
                        connection.execute(
                            "INSERT OR IGNORE INTO activation_events VALUES (?, ?, ?, ?, ?, ?)",
                            (
                                event["event_id"], event["object_id"], event.get("event_kind", ""),
                                event.get("project_id"), event.get("created_at", ""),
                                json.dumps(event, ensure_ascii=False, sort_keys=True),
                            ),
                        )
                        aggregate = activation_totals.setdefault(str(event["object_id"]), {
                            "selected": 0, "opened": 0, "used": 0, "cited": 0, "coactivated": 0,
                            "last": None, "projects": {},
                        })
                        kind = str(event.get("event_kind", ""))
                        if kind in {"selected", "opened", "used", "cited", "coactivated"}:
                            aggregate[kind] += 1
                        created = str(event.get("created_at", ""))
                        if kind in {"selected", "opened", "used", "cited"}:
                            aggregate["last"] = max(aggregate["last"] or "", created)
                        if event.get("project_id"):
                            project_id = str(event["project_id"])
                            aggregate["projects"][project_id] = aggregate["projects"].get(project_id, 0) + 1
                for object_id, aggregate in activation_totals.items():
                    connection.execute(
                        "INSERT INTO activation_aggregates VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            object_id, aggregate["selected"], aggregate["opened"], aggregate["used"],
                            aggregate["cited"], aggregate["coactivated"], aggregate["last"],
                            json.dumps(aggregate["projects"], ensure_ascii=False, sort_keys=True),
                        ),
                    )
                connection.commit()
            os.replace(temp_path, self.index_path)
            return count
        finally:
            temp_path.unlink(missing_ok=True)

    def search(
        self, query: str, limit: int = 20, *, object_types: set[str] | None = None,
        statuses: set[str] | None = None, canonical_only: bool = False,
        include_proposals: bool = False, domains: set[str] | None = None,
        source_kinds: set[str] | None = None,
    ) -> list[SearchResult]:
        self.ensure_initialized()
        query = query.strip()
        if not query:
            raise ValidationError("搜索词不能为空")
        fts_query = " ".join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in query.split())
        clauses: list[str] = []
        parameters: list[Any] = [fts_query]
        if object_types:
            clauses.append(f"d.type IN ({','.join('?' for _ in object_types)})")
            parameters.extend(sorted(object_types))
        if statuses:
            clauses.append(f"d.status IN ({','.join('?' for _ in statuses)})")
            parameters.extend(sorted(statuses))
        if canonical_only:
            clauses.append("d.type != 'source'")
        if domains:
            clauses.append("(" + " OR ".join("d.domains LIKE ?" for _ in domains) + ")")
            parameters.extend(f"%{domain}%" for domain in sorted(domains))
        if source_kinds:
            clauses.append(f"(d.type != 'source' OR d.source_kind IN ({','.join('?' for _ in source_kinds)}))")
            parameters.extend(sorted(source_kinds))
        where = (" AND " + " AND ".join(clauses)) if clauses else ""
        with closing(sqlite3.connect(self.index_path)) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                f"""
                SELECT d.*, snippet(documents_fts, 5, '[', ']', '…', 18) AS snippet,
                       bm25(documents_fts, 0.0, 8.0, 5.0, 4.0, 3.0, 1.0) AS rank
                FROM documents_fts JOIN documents d ON d.id = documents_fts.id
                WHERE documents_fts MATCH ?{where} ORDER BY rank LIMIT ?
                """,
                (*parameters, limit),
            ).fetchall()
            seen = {row["id"] for row in rows}
            if len(rows) < limit:
                like = f"%{query}%"
                fallback_clauses = ["(title LIKE ? OR aliases LIKE ? OR tags LIKE ? OR domains LIKE ? OR body LIKE ?)"]
                fallback_parameters: list[Any] = [like, like, like, like, like]
                fallback_clauses.extend(clause.replace("d.", "") for clause in clauses)
                fallback_parameters.extend(parameters[1:])
                fallback = connection.execute(
                    "SELECT *, substr(body, 1, 240) AS snippet FROM documents WHERE "
                    + " AND ".join(fallback_clauses) + " LIMIT ?",
                    (*fallback_parameters, limit),
                ).fetchall()
                rows.extend(row for row in fallback if row["id"] not in seen)
        results = [
            SearchResult(
                id=row["id"], type=row["type"], title=row["title"], path=row["path"],
                status=row["status"],
                source_ids=json.loads(row["source_ids"]), snippet=row["snippet"] or "",
                match_reason=self._match_reason(query, row),
            )
            for row in rows[:limit]
        ]
        if include_proposals and len(results) < limit:
            needle = query.casefold()
            seen = {item.id for item in results}
            for path in self.proposal_documents():
                metadata, body = read_document(path)
                haystack = " ".join([
                    str(metadata.get("title", "")), body,
                    *map(str, metadata.get("aliases", [])), *map(str, metadata.get("tags", [])),
                    *map(str, metadata.get("domains", [])),
                ]).casefold()
                if needle not in haystack or metadata["id"] in seen:
                    continue
                if object_types and "proposal" not in object_types:
                    continue
                if statuses and metadata.get("status") not in statuses:
                    continue
                results.append(SearchResult(
                    id=str(metadata["id"]), type="proposal", title=str(metadata["title"]),
                    path=self.rel(path), status=str(metadata["status"]),
                    source_ids=list(metadata.get("source_ids", [])), snippet=body[:240],
                    match_reason="explicit proposal text match",
                ))
                if len(results) >= limit:
                    break
        return results[:limit]

    @staticmethod
    def _match_reason(query: str, row: sqlite3.Row) -> str:
        needle = query.casefold()
        for field in ("title", "aliases", "tags", "domains"):
            if needle in str(row[field]).casefold():
                return f"metadata:{field}"
        return "full-text:body"

    def search_with_relations(
        self, query: str, limit: int = 20, *, max_depth: int = 1,
        max_nodes: int = 30, **filters: Any,
    ) -> list[SearchResult]:
        if not 0 <= max_depth <= 3 or not 1 <= max_nodes <= 100:
            raise ValidationError("relation traversal 限制为 depth 0..3、nodes 1..100")
        seeds = self.search(query, min(limit, max_nodes), **filters)
        results = list(seeds)
        seen = {item.id for item in results}
        frontier = [(item.id, 0) for item in seeds]
        while frontier and len(results) < min(limit, max_nodes):
            current_id, depth = frontier.pop(0)
            if depth >= max_depth:
                continue
            for relation in self.related(current_id):
                neighbor = relation["target_id"] if relation["source_id"] == current_id else relation["source_id"]
                if neighbor in seen:
                    continue
                try:
                    path, metadata, body = self.find_document(neighbor)
                except NotFoundError:
                    continue
                if metadata.get("type") == "proposal" and not filters.get("include_proposals"):
                    continue
                if filters.get("canonical_only") and metadata.get("type") == "source":
                    continue
                object_types = filters.get("object_types")
                statuses = filters.get("statuses")
                if object_types and metadata.get("type") not in object_types:
                    continue
                if statuses and metadata.get("status") not in statuses:
                    continue
                seen.add(neighbor)
                source_ids = list(metadata.get("source_ids", []))
                if metadata.get("type") == "source":
                    source_ids = [neighbor]
                results.append(SearchResult(
                    id=neighbor, type=str(metadata["type"]), title=str(metadata["title"]),
                    path=self.rel(path), status=str(metadata["status"]), source_ids=source_ids,
                    snippet=body[:240],
                    match_reason=f"relation depth {depth + 1}: {relation['relation_type']} via {current_id}",
                ))
                frontier.append((neighbor, depth + 1))
                if len(results) >= min(limit, max_nodes):
                    break
        return results

    def find_document(self, object_id: str) -> tuple[Path, dict[str, Any], str]:
        candidates = (
            list(self.all_indexed_documents())
            + list(self.archive_documents())
            + list(self.proposal_documents())
        )
        candidates += list((self.root / "vault" / "proposals").glob("candidate-*.md"))
        candidates += list(self.followup_documents())
        candidates += list((self.root / "vault" / "exceptions").glob("exception-*.md"))
        candidates += list((self.root / "vault" / "promotions").glob("promotion-*.md"))
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
