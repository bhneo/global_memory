from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .errors import ValidationError
from .markdown import read_document
from .repository import Repository, sha256_bytes


MIN_TOKEN_BUDGET = 128
MAX_TOKEN_BUDGET = 20_000
SEARCH_LIMIT = 50


@dataclass(frozen=True)
class ContextPack:
    query: str
    token_budget: int
    estimated_tokens: int
    items: list[dict[str, Any]]
    omitted: list[dict[str, Any]]

    def as_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "token_budget": self.token_budget,
            "estimated_tokens": self.estimated_tokens,
            "items": self.items,
            "omitted": self.omitted,
            "selection_policy": {
                "kind": "read-only-query-context-v1",
                "notes": [
                    "Context Pack 是临时读取视图，不写入 Markdown、索引或日志。",
                    "它不替代检索，不把命中或摘录升级为事实，也不改变 canonical 状态。",
                    "token 为保守估算；每项保留路径、哈希、来源和入选理由，供调用方回溯。",
                ],
            },
        }


class ContextPackService:
    """Build a small, deterministic, provenance-preserving read-only view."""

    def __init__(self, repository: Repository):
        self.repository = repository

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """Conservative mixed Chinese/Latin token estimate, without a model tokenizer."""
        cjk = len(re.findall(r"[\u3400-\u9fff]", text))
        non_cjk = re.sub(r"[\u3400-\u9fff]", " ", text)
        latin_words = len(re.findall(r"\S+", non_cjk))
        return max(1, cjk + (latin_words * 2 + 2) // 3)

    @staticmethod
    def _clip_to_budget(text: str, token_budget: int) -> str:
        if ContextPackService._estimate_tokens(text) <= token_budget:
            return text
        if token_budget <= 1:
            return "…"
        clipped: list[str] = []
        cjk = 0
        latin_words = 0
        in_latin_word = False
        for character in text:
            next_cjk = cjk
            next_latin_words = latin_words
            next_in_latin_word = in_latin_word
            if re.match(r"[\u3400-\u9fff]", character):
                next_cjk += 1
                next_in_latin_word = False
            elif character.isspace():
                next_in_latin_word = False
            elif not next_in_latin_word:
                next_latin_words += 1
                next_in_latin_word = True
            estimated = next_cjk + (next_latin_words * 2 + 2) // 3
            # Reserve one token for the visible truncation marker.
            if estimated + 1 > token_budget:
                break
            clipped.append(character)
            cjk, latin_words, in_latin_word = next_cjk, next_latin_words, next_in_latin_word
        return ("".join(clipped).rstrip() + "…") if clipped else "…"

    def _content(self, metadata: dict[str, Any], body: str) -> str:
        if metadata.get("type") != "source":
            return body.strip()
        raw_path = self.repository.resolve_inside(str(metadata["raw_content_path"]))
        try:
            return raw_path.read_text(encoding="utf-8").strip()
        except UnicodeDecodeError:
            return body.strip()

    @staticmethod
    def _type_priority(object_type: str) -> int:
        # Prefer reviewed interpretations over duplicated raw text, without hiding sources.
        return {"synthesis": 30, "claim": 20, "source": 10}.get(object_type, 0)

    def _latest_source_ids(self) -> set[str]:
        """Return the current source record for every append-only source family."""
        latest: dict[str, tuple[tuple[int, str, str], str]] = {}
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            family = str(metadata.get("canonical_locator", metadata["id"]))
            version_key = (
                int(metadata.get("version_number", 1)),
                str(metadata.get("captured_at", "")),
                str(metadata["id"]),
            )
            existing = latest.get(family)
            if existing is None or version_key > existing[0]:
                latest[family] = (version_key, str(metadata["id"]))
        return {item[1] for item in latest.values()}

    def _archived_only_source_ids(self) -> set[str]:
        """Return sources referenced by archived canonical knowledge and no active canonical."""
        archived: set[str] = set()
        active: set[str] = set()
        for path in self.repository.canonical_documents():
            metadata, _ = read_document(path)
            destination = archived if metadata.get("status") == "archived" else active
            destination.update(str(item) for item in metadata.get("source_ids", []))
        return archived - active

    def build(self, query: str, token_budget: int = 1_200) -> ContextPack:
        query = query.strip()
        if not query:
            raise ValidationError("Context Pack query 不能为空")
        if not MIN_TOKEN_BUDGET <= token_budget <= MAX_TOKEN_BUDGET:
            raise ValidationError(
                f"Context Pack token budget 必须介于 {MIN_TOKEN_BUDGET} 和 {MAX_TOKEN_BUDGET}"
            )

        latest_source_ids = self._latest_source_ids()
        archived_only_source_ids = self._archived_only_source_ids()
        ranked: list[tuple[int, int, dict[str, Any]]] = []
        omitted: list[dict[str, Any]] = []
        for search_rank, result in enumerate(self.repository.search(query, SEARCH_LIMIT), start=1):
            path, metadata, body = self.repository.find_document(result.id)
            object_type = str(metadata.get("type"))
            if object_type not in {"source", "claim", "synthesis"}:
                continue
            if object_type != "source" and metadata.get("status") == "archived":
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "canonical 对象已归档；Context Pack 默认排除非活动知识",
                })
                continue
            if object_type == "source" and str(metadata["id"]) not in latest_source_ids:
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "同一 source family 的旧版本；Context Pack 默认只选最新版本",
                })
                continue
            if object_type == "source" and str(metadata["id"]) in archived_only_source_ids:
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "source 仅被已归档 canonical 引用；Context Pack 默认排除",
                })
                continue
            content = self._content(metadata, body)
            if not content:
                continue
            source_ids = [str(item) for item in metadata.get("source_ids", [])]
            if object_type == "source":
                source_ids = [str(metadata["id"])]
            ranked.append((
                -(1_000 - search_rank + self._type_priority(object_type)),
                search_rank,
                {
                    "id": str(metadata["id"]),
                    "type": object_type,
                    "title": str(metadata["title"]),
                    "path": self.repository.rel(path),
                    "document_sha256": sha256_bytes(path.read_bytes()),
                    "source_ids": source_ids,
                    "raw_content_sha256": metadata.get("content_sha256") if object_type == "source" else None,
                    "source_version": int(metadata.get("version_number", 1)) if object_type == "source" else None,
                    "content": content,
                    "selection_reason": (
                        f"全文检索命中第 {search_rank} 位；"
                        f"对象类型为 {object_type}；保留其显式来源链。"
                    ),
                },
            ))
        ranked.sort(key=lambda item: (item[0], item[1], item[2]["id"]))

        available = token_budget - 48  # reserve room for outer query and policy metadata
        selected: list[dict[str, Any]] = []
        used = 0
        for _, _, item in ranked:
            metadata_text = " ".join(
                [item["id"], item["title"], item["path"], *item["source_ids"], item["selection_reason"]]
            )
            metadata_tokens = self._estimate_tokens(metadata_text)
            remaining = available - used - metadata_tokens
            if remaining < 24:
                omitted.append({"id": item["id"], "reason": "token budget 已耗尽"})
                continue
            content = self._clip_to_budget(item["content"], remaining)
            estimated_tokens = metadata_tokens + self._estimate_tokens(content)
            if used + estimated_tokens > available:
                omitted.append({"id": item["id"], "reason": "token budget 不足"})
                continue
            selected.append({**item, "content": content, "estimated_tokens": estimated_tokens})
            used += estimated_tokens
        return ContextPack(query, token_budget, used, selected, omitted)
