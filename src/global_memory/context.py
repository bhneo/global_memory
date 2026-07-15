from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .errors import ValidationError
from .extraction import ExtractionService
from .markdown import read_document
from .repository import Repository, sha256_bytes


MIN_TOKEN_BUDGET = 128
MAX_TOKEN_BUDGET = 20_000
SEARCH_LIMIT = 50
PROFILE_PRIORITIES = {
    "execution": {
        "project": 100, "goal": 95, "architecture": 90, "decision": 88,
        "failure": 86, "experiment": 82, "opportunity": 75, "question": 70,
        "tension": 68, "claim": 55, "source": 30,
    },
    "research": {
        "claim": 95, "concept": 90, "source": 88, "work": 84,
        "question": 80, "tension": 78, "synthesis": 75, "hypothesis": 70,
    },
    "exploration": {
        "intuition": 100, "tension": 95, "analogy": 92, "anomaly": 90,
        "hypothesis": 88, "question": 82, "concept": 65, "claim": 45,
    },
}


@dataclass(frozen=True)
class ContextPack:
    query: str
    token_budget: int
    estimated_tokens: int
    items: list[dict[str, Any]]
    omitted: list[dict[str, Any]]
    profiles: list[str]
    filters: dict[str, Any]

    def as_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "token_budget": self.token_budget,
            "estimated_tokens": self.estimated_tokens,
            "items": self.items,
            "omitted": self.omitted,
            "profiles": self.profiles,
            "filters": self.filters,
            "truncation_report": {
                "selected_items": len(self.items),
                "omitted_items": len(self.omitted),
                "budget_exhausted": any("budget" in str(item.get("reason", "")) for item in self.omitted),
            },
            "selection_policy": {
                "kind": "profiled-read-only-query-context-v2",
                "notes": [
                    "Context Pack 是临时读取视图，不写入 Markdown、索引或日志。",
                    "它不替代检索，不把命中或摘录升级为事实，也不改变 canonical 状态。",
                    "provisional 表示已通过自动门禁但尚未人工确认；调用方必须保留该信任标记。",
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
        try:
            _, extraction, extracted = ExtractionService(self.repository).latest_for_source(str(metadata["id"]))
            if extraction.get("status") == "ready" and extracted.strip():
                return extracted.strip()
        except Exception:
            pass
        raw_path = self.repository.resolve_inside(str(metadata["raw_content_path"]))
        try:
            return raw_path.read_text(encoding="utf-8").strip()
        except UnicodeDecodeError:
            return body.strip()

    @staticmethod
    def _evidence_view(metadata: dict[str, Any]) -> list[dict[str, Any]]:
        view: list[dict[str, Any]] = []
        for item in metadata.get("evidence", []):
            if not isinstance(item, dict):
                continue
            text = item.get("original_text") or item.get("interpretation") or item.get("excerpt") or ""
            view.append({
                "evidence_id": item.get("evidence_id"),
                "evidence_kind": item.get("evidence_kind", "legacy_excerpt"),
                "source_id": item.get("source_id"), "stance": item.get("stance"),
                "page": item.get("page"), "section": item.get("section"),
                "text": str(text)[:240], "verification_status": item.get("verification_status"),
            })
        return view

    @staticmethod
    def _type_priority(object_type: str, profiles: list[str], status: str) -> int:
        priority = max(PROFILE_PRIORITIES[profile].get(object_type, 0) for profile in profiles)
        if status == "confirmed":
            priority += 12
        elif status == "provisional":
            priority += 4
        elif status in {"contested", "pending", "deferred"}:
            priority -= 2
        if object_type in {"decision", "failure", "goal", "project"}:
            priority += 8
        return priority

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
        for path in [*self.repository.canonical_documents(), *self.repository.archive_documents()]:
            metadata, _ = read_document(path)
            destination = archived if metadata.get("status") == "archived" else active
            destination.update(str(item) for item in metadata.get("source_ids", []))
        return archived - active

    def build(
        self, query: str, token_budget: int = 1_200, *, profiles: list[str] | None = None,
        project: str | None = None, domains: set[str] | None = None,
        object_types: set[str] | None = None, statuses: set[str] | None = None,
        updated_since: str | None = None, source_kinds: set[str] | None = None,
        include_proposals: bool = False, relation_depth: int = 1,
    ) -> ContextPack:
        query = query.strip()
        if not query:
            raise ValidationError("Context Pack query 不能为空")
        if not MIN_TOKEN_BUDGET <= token_budget <= MAX_TOKEN_BUDGET:
            raise ValidationError(
                f"Context Pack token budget 必须介于 {MIN_TOKEN_BUDGET} 和 {MAX_TOKEN_BUDGET}"
            )
        profiles = profiles or ["research"]
        invalid_profiles = set(profiles) - PROFILE_PRIORITIES.keys()
        if invalid_profiles:
            raise ValidationError(f"未知 Context Pack profile: {', '.join(sorted(invalid_profiles))}")
        allowed_types = set().union(*(PROFILE_PRIORITIES[profile].keys() for profile in profiles))
        if object_types:
            allowed_types &= object_types
        if include_proposals:
            allowed_types.add("proposal")
        filter_report = {
            "project": project, "domains": sorted(domains or []),
            "object_types": sorted(object_types or []), "statuses": sorted(statuses or []),
            "updated_since": updated_since, "source_kinds": sorted(source_kinds or []),
            "include_proposals": include_proposals, "relation_depth": relation_depth,
        }

        latest_source_ids = self._latest_source_ids()
        archived_only_source_ids = self._archived_only_source_ids()
        ranked: list[tuple[int, int, dict[str, Any]]] = []
        omitted: list[dict[str, Any]] = []
        results = self.repository.search_with_relations(
            query, SEARCH_LIMIT, max_depth=relation_depth, max_nodes=SEARCH_LIMIT,
            object_types=allowed_types, statuses=statuses, include_proposals=include_proposals,
            domains=domains, source_kinds=source_kinds,
        )
        for search_rank, result in enumerate(results, start=1):
            path, metadata, body = self.repository.find_document(result.id)
            object_type = str(metadata.get("type"))
            if object_type not in allowed_types:
                continue
            if updated_since and str(metadata.get("updated_at", "")) < updated_since:
                omitted.append({"id": str(metadata["id"]), "reason": "早于 updated_since filter"})
                continue
            if project:
                related_projects = {
                    str(metadata.get("project_id", "")), str(metadata.get("id", "")),
                    *(str(relation.get("target_id")) for relation in metadata.get("relations", []) if isinstance(relation, dict)),
                }
                if project not in related_projects and project.casefold() not in str(metadata.get("title", "")).casefold():
                    omitted.append({"id": str(metadata["id"]), "reason": "不满足 project filter"})
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
                -(1_000 - search_rank + self._type_priority(object_type, profiles, str(metadata.get("status")))),
                search_rank,
                {
                    "id": str(metadata["id"]),
                    "type": object_type,
                    "knowledge_status": str(metadata.get("status")),
                    "title": str(metadata["title"]),
                    "path": self.repository.rel(path),
                    "document_sha256": sha256_bytes(path.read_bytes()),
                    "source_ids": source_ids,
                    "raw_content_sha256": metadata.get("content_sha256") if object_type == "source" else None,
                    "source_version": int(metadata.get("version_number", 1)) if object_type == "source" else None,
                    "evidence": self._evidence_view(metadata) if object_type == "claim" else [],
                    "match_reason": result.match_reason,
                    "content": content,
                    "selection_reason": (
                        f"全文检索命中第 {search_rank} 位；"
                        f"对象类型为 {object_type}；状态为 {metadata.get('status')}；"
                        f"profile={','.join(profiles)}；{result.match_reason}；保留其显式来源链。"
                    ),
                },
            ))
        ranked.sort(key=lambda item: (item[0], item[1], item[2]["id"]))

        available = token_budget - 48  # reserve room for outer query and policy metadata
        selected: list[dict[str, Any]] = []
        used = 0
        for _, _, item in ranked:
            metadata_text = " ".join(
                [item["id"], item["title"], item["path"], *item["source_ids"],
                 item["selection_reason"], str(item["evidence"])]
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
        return ContextPack(query, token_budget, used, selected, omitted, profiles, filter_report)
