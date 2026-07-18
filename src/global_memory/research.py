from __future__ import annotations

import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo

from .errors import NotFoundError, ValidationError
from .markdown import read_document, render_document
from .repository import Repository, now_iso


TZ = ZoneInfo("Asia/Shanghai")
ANNOTATION_KINDS = {"capture_intent", "connection_feedback", "research_note"}
SALIENCE_LEVELS = {"low", "medium", "high", "unknown"}
FEEDBACK_LABELS = {"obvious", "forced", "interesting", "actionable"}
ACTIVATION_KINDS = {"selected", "opened", "used", "cited", "coactivated"}
FEEDBACK_TARGET_TYPES = {
    "analogy", "hypothesis", "tension", "question", "concept", "synthesis",
    "claim", "source",
}


def _event_time() -> str:
    return datetime.now(TZ).isoformat(timespec="microseconds")


def _clean_list(values: Iterable[str] | None) -> list[str]:
    return sorted({str(value).strip() for value in (values or []) if str(value).strip()})


def _stable_id(prefix: str, payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(encoded).hexdigest()[:24]}"


class ResearchAnnotationService:
    """Append-only user-owned research signals, separate from knowledge truth."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "annotations" / "research"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("annotation-*.md")) if self.directory.exists() else []

    def all(self, *, target_id: str | None = None, kind: str | None = None) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for path in self.documents():
            metadata, body = read_document(path)
            if target_id and target_id not in metadata.get("target_ids", []):
                continue
            if kind and metadata.get("annotation_kind") != kind:
                continue
            records.append({**metadata, "body": body, "path": self.repository.rel(path)})
        return records

    def _validate_targets(self, target_ids: list[str], allow_unresolved: bool) -> list[str]:
        unresolved: list[str] = []
        for target_id in target_ids:
            try:
                self.repository.find_document(target_id)
            except NotFoundError:
                unresolved.append(target_id)
        if unresolved and not allow_unresolved:
            raise ValidationError(
                "annotation target 不存在；如需保留未解析引用请显式使用 --allow-unresolved: "
                + ", ".join(unresolved)
            )
        return unresolved

    def create(
        self,
        kind: str,
        *,
        target_ids: Iterable[str] | None = None,
        why_saved: str | None = None,
        what_surprised_me: str | None = None,
        possible_connections: Iterable[str] | None = None,
        research_projects: Iterable[str] | None = None,
        domains: Iterable[str] | None = None,
        personal_salience: str = "unknown",
        note: str | None = None,
        feedback_label: str | None = None,
        feedback_note: str | None = None,
        supersedes_annotation_id: str | None = None,
        allow_unresolved: bool = False,
        created_by: str = "user",
    ) -> dict[str, Any]:
        if created_by != "user":
            raise ValidationError("Research Annotation 只能保存明确的用户输入；Agent interpretation 必须分层")
        if kind not in ANNOTATION_KINDS:
            raise ValidationError(f"未知 annotation kind: {kind}")
        if personal_salience not in SALIENCE_LEVELS:
            raise ValidationError(f"未知 personal salience: {personal_salience}")
        if kind == "connection_feedback" and feedback_label not in FEEDBACK_LABELS:
            raise ValidationError("feedback label 必须是 obvious/forced/interesting/actionable")
        if kind != "connection_feedback" and feedback_label is not None:
            raise ValidationError("feedback_label 只适用于 connection_feedback")

        targets = _clean_list(target_ids)
        projects = _clean_list(research_projects)
        domain_list = _clean_list(domains)
        connections = _clean_list(possible_connections)
        unresolved = self._validate_targets(targets, allow_unresolved)
        if kind == "connection_feedback":
            for target_id in targets:
                if target_id in unresolved:
                    continue
                _, target, _ = self.repository.find_document(target_id)
                if target.get("type") not in FEEDBACK_TARGET_TYPES:
                    raise ValidationError(
                        f"connection feedback 不支持 target type: {target.get('type')}"
                    )
        if supersedes_annotation_id:
            previous = next(
                (item for item in self.all() if item.get("id") == supersedes_annotation_id), None
            )
            if previous is None:
                raise ValidationError(f"superseded annotation 不存在: {supersedes_annotation_id}")
            if previous.get("annotation_kind") != kind:
                raise ValidationError("correction 必须 supersede 同一种 annotation kind")
            previous_targets = set(map(str, previous.get("target_ids", [])))
            if targets and previous_targets and not (set(targets) & previous_targets):
                raise ValidationError("correction 必须与被 supersede annotation 共享 target")

        user_fields = {
            "why_saved": (why_saved or "").strip(),
            "what_surprised_me": (what_surprised_me or "").strip(),
            "possible_connections": connections,
            "research_projects": projects,
            "domains": domain_list,
            "note": (note or "").strip(),
            "feedback_label": feedback_label,
            "feedback_note": (feedback_note or "").strip(),
        }
        has_content = any(
            value for key, value in user_fields.items()
            if key not in {"research_projects", "domains", "feedback_label"}
        ) or bool(feedback_label)
        if not has_content:
            raise ValidationError("annotation 至少需要一个真实内容字段")

        created_at = _event_time()
        identity = {
            "annotation_kind": kind,
            "target_ids": targets,
            "created_at": created_at,
            "created_by": created_by,
            **user_fields,
            "personal_salience": personal_salience,
            "supersedes_annotation_id": supersedes_annotation_id,
        }
        annotation_id = _stable_id("annotation", identity)
        metadata: dict[str, Any] = {
            "id": annotation_id,
            "type": "annotation",
            "status": "active",
            "title": {
                "capture_intent": "保存意图",
                "connection_feedback": f"连接反馈：{feedback_label}",
                "research_note": "研究笔记",
            }[kind],
            "created_at": created_at,
            "updated_at": created_at,
            "created_by": created_by,
            "user_authored": created_by == "user",
            "annotation_kind": kind,
            "target_ids": targets,
            "unresolved_target_ids": unresolved,
            "source_ids": [item for item in targets if item.startswith("source_")],
            "aliases": [],
            "tags": [kind],
            "domains": domain_list,
            "confidence": "unknown",
            "research_projects": projects,
            "personal_salience": personal_salience,
            "why_saved": user_fields["why_saved"],
            "what_surprised_me": user_fields["what_surprised_me"],
            "possible_connections": connections,
            "note": user_fields["note"],
            "feedback_label": feedback_label,
            "feedback_note": user_fields["feedback_note"],
            "supersedes_annotation_id": supersedes_annotation_id,
            "agent_interpretation": None,
            "truth_layer": "user_annotation",
        }
        body_parts = []
        for heading, value in (
            ("为什么保存", metadata["why_saved"]),
            ("让我意外的地方", metadata["what_surprised_me"]),
            ("研究笔记", metadata["note"]),
            ("连接反馈", metadata["feedback_note"]),
        ):
            if value:
                body_parts.append(f"## {heading}\n\n{value}")
        body = "\n\n".join(body_parts)
        path = self.directory / f"annotation-{annotation_id}.md"
        self.repository.immutable_write(path, render_document(metadata, body).encode("utf-8"))
        self.repository.rebuild_index()
        return {"id": annotation_id, "path": self.repository.rel(path), "annotation_kind": kind}

    def feedback_summary(self) -> dict[str, Any]:
        feedback = self.all(kind="connection_feedback")
        labels = Counter(str(item.get("feedback_label")) for item in feedback)
        by_type: Counter[str] = Counter()
        by_project: Counter[str] = Counter()
        by_domain: Counter[str] = Counter()
        for item in feedback:
            for target_id in item.get("target_ids", []):
                try:
                    _, target, _ = self.repository.find_document(str(target_id))
                    by_type[str(target.get("type", "unknown"))] += 1
                except NotFoundError:
                    by_type["unresolved"] += 1
            by_project.update(map(str, item.get("research_projects", [])))
            by_domain.update(map(str, item.get("domains", [])))
        def selected(label: str) -> list[dict[str, Any]]:
            return [
                {"id": item["id"], "target_ids": item.get("target_ids", []),
                 "note": item.get("feedback_note", ""), "projects": item.get("research_projects", [])}
                for item in feedback if item.get("feedback_label") == label
            ][-20:]
        return {
            "total": len(feedback),
            **{label: labels[label] for label in sorted(FEEDBACK_LABELS)},
            "by_object_type": dict(sorted(by_type.items())),
            "by_project": dict(sorted(by_project.items())),
            "by_domain": dict(sorted(by_domain.items())),
            "top_interesting": selected("interesting"),
            "top_actionable": selected("actionable"),
            "repeated_forced_patterns": selected("forced"),
        }

    def signal_summary(self) -> dict[str, Any]:
        annotations = self.all()
        by_project: dict[str, list[str]] = defaultdict(list)
        by_domain: dict[str, list[str]] = defaultdict(list)
        for item in annotations:
            for project in item.get("research_projects", []):
                by_project[str(project)].append(str(item["id"]))
            for domain in item.get("domains", []):
                by_domain[str(domain)].append(str(item["id"]))
        high_unannotated = []
        for item in annotations:
            if (
                item.get("annotation_kind") == "capture_intent"
                and item.get("personal_salience") == "high"
                and not item.get("why_saved")
            ):
                high_unannotated.extend(item.get("target_ids", []))
        return {
            "total": len(annotations),
            "high_salience_without_why_saved": sorted(set(high_unannotated)),
            "interesting_actionable": [
                item["id"] for item in annotations
                if item.get("feedback_label") in {"interesting", "actionable"}
            ],
            "forced": [item["id"] for item in annotations if item.get("feedback_label") == "forced"],
            "by_project": {key: value for key, value in sorted(by_project.items())},
            "by_domain": {key: value for key, value in sorted(by_domain.items())},
        }


class ActivationService:
    """Explicit local operational signals. Activation never changes knowledge trust."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.path = repository.root / "system" / "logs" / "activation-events.jsonl"

    def events(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        events: list[dict[str, Any]] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(item, dict) and item.get("event_id"):
                events.append(item)
        return events

    def record(
        self,
        object_id: str,
        *,
        kind: str,
        project_id: str | None = None,
        query: str | None = None,
        context_pack_id: str | None = None,
        reason: str = "",
        source: str = "cli",
        coactivated_ids: Iterable[str] | None = None,
        event_id: str | None = None,
    ) -> dict[str, Any]:
        if kind not in ACTIVATION_KINDS:
            raise ValidationError(f"未知 activation kind: {kind}")
        self.repository.find_document(object_id)
        created_at = _event_time()
        payload = {
            "object_id": object_id,
            "event_kind": kind,
            "project_id": project_id,
            "query_hash": hashlib.sha256((query or "").encode("utf-8")).hexdigest()[:24] if query else None,
            "context_pack_id": context_pack_id,
            "reason": reason.strip(),
            "created_at": created_at,
            "source": source,
            "coactivated_ids": _clean_list(coactivated_ids),
        }
        event_id = event_id or _stable_id("activation", payload)
        if any(item.get("event_id") == event_id for item in self.events()):
            return {"event_id": event_id, "written": False, "duplicate": True}
        record = {"event_id": event_id, **payload}
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        return {"event_id": event_id, "written": True, "duplicate": False}

    def aggregate(
        self, object_id: str | None = None, project_id: str | None = None,
        since: str | None = None,
    ) -> list[dict[str, Any]]:
        groups: dict[str, dict[str, Any]] = {}
        for event in self.events():
            if object_id and event.get("object_id") != object_id:
                continue
            if project_id and event.get("project_id") != project_id:
                continue
            if since and str(event.get("created_at", "")) < since:
                continue
            key = str(event["object_id"])
            group = groups.setdefault(key, {
                "object_id": key, "selected_count": 0, "opened_count": 0,
                "used_count": 0, "cited_count": 0, "coactivated_count": 0,
                "last_used_at": None, "projects": Counter(), "coactivated_objects": Counter(),
                "recent_events": [],
            })
            field = f"{event['event_kind']}_count"
            if field in group:
                group[field] += 1
            if event["event_kind"] in {"used", "cited", "opened", "selected"}:
                group["last_used_at"] = max(group["last_used_at"] or "", str(event.get("created_at", "")))
            if event.get("project_id"):
                group["projects"][str(event["project_id"])] += 1
            group["coactivated_objects"].update(map(str, event.get("coactivated_ids", [])))
            group["recent_events"].append(event)
        results = []
        for group in groups.values():
            group["projects"] = dict(group["projects"].most_common())
            group["coactivated_objects"] = dict(group["coactivated_objects"].most_common())
            group["recent_events"] = group["recent_events"][-10:]
            results.append(group)
        return sorted(
            results,
            key=lambda item: (-(item["used_count"] + item["cited_count"] + item["opened_count"]), item["object_id"]),
        )


@dataclass(frozen=True)
class RoutePlan:
    query: str
    explicit_project: str | None
    selected_project: str | None
    project_candidates: list[dict[str, Any]]
    selected_domains: list[str]
    seed_objects: list[str]
    relation_expansions: list[dict[str, Any]]
    annotation_matches: list[str]
    fallback_used: bool
    raw_opened: list[str]
    selection_reasons: list[str]

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


class ResearchRouterService:
    """Bounded, explainable project/domain-first retrieval planning."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.annotations = ResearchAnnotationService(repository)

    def _project_candidates(self, query: str) -> list[dict[str, Any]]:
        query_folded = query.casefold()
        query_terms = {
            term for term in re.findall(r"[\w\u3400-\u9fff-]+", query_folded)
            if len(term) >= 2
        }
        candidates = []
        seen: set[str] = set()
        for candidate_query in [query, *sorted(query_terms, key=lambda item: (-len(item), item))[:4]]:
            for item in self.repository.search(
                candidate_query, 10, object_types={"project", "goal", "question"},
                include_proposals=False,
            ):
                if item.id not in seen:
                    seen.add(item.id)
                    candidates.append(item)
            if len(candidates) >= 10:
                break
        result: list[dict[str, Any]] = []
        for rank, item in enumerate(candidates, start=1):
            title = item.title.casefold()
            title_terms = set(re.findall(r"[\w\u3400-\u9fff-]+", title))
            overlap = len(query_terms & title_terms) / max(1, len(query_terms))
            exact_title = bool(title and (title in query_folded or query_folded in title))
            score = 0.95 if exact_title else 0.35 + 0.45 * overlap - (rank - 1) * 0.03
            if item.type == "project" and (exact_title or overlap >= 0.5):
                score += 0.05
            result.append({"id": item.id, "type": item.type, "title": item.title,
                           "score": round(max(0.0, min(score, 1.0)), 2), "reason": item.match_reason})
        return result

    def plan(
        self,
        query: str,
        *,
        project: str | None = None,
        domains: Iterable[str] | None = None,
        relation_depth: int = 1,
    ) -> RoutePlan:
        query = query.strip()
        if not query:
            raise ValidationError("research route query 不能为空")
        if relation_depth < 0 or relation_depth > 2:
            raise ValidationError("research route relation depth 必须在 0..2")
        candidates = self._project_candidates(query)
        selected_project = project
        reasons: list[str] = []
        if project:
            reasons.append("调用者提供了显式 Project；它具有最高路由优先级。")
        elif candidates and candidates[0]["type"] == "project" and candidates[0]["score"] >= 0.75:
            selected_project = str(candidates[0]["id"])
            reasons.append("标题/别名/正文检索得到高置信 Project 候选。")
        else:
            reasons.append("没有可靠 Project 候选，保留 Global Route。")

        selected_domains = _clean_list(domains)
        annotation_matches: list[str] = []
        seed_objects: list[str] = []
        for annotation in self.annotations.all():
            projects = set(map(str, annotation.get("research_projects", [])))
            annotation_domains = set(map(str, annotation.get("domains", [])))
            if (selected_project and selected_project in projects) or (set(selected_domains) & annotation_domains):
                annotation_matches.append(str(annotation["id"]))
                seed_objects.extend(map(str, annotation.get("target_ids", [])))
                if not selected_domains:
                    selected_domains.extend(sorted(annotation_domains))
        if selected_project:
            seed_objects.append(selected_project)
            for candidate in candidates:
                if candidate["id"] == selected_project or candidate["type"] in {"goal", "question"}:
                    seed_objects.append(str(candidate["id"]))
        elif candidates:
            seed_objects.extend(str(item["id"]) for item in candidates[:3])

        expansions: list[dict[str, Any]] = []
        seen = set(seed_objects)
        frontier = [(item, 0) for item in list(dict.fromkeys(seed_objects))]
        while frontier and len(expansions) < 30:
            current, depth = frontier.pop(0)
            if depth >= relation_depth:
                continue
            try:
                relations = self.repository.related(current)
            except Exception:
                continue
            for relation in relations:
                neighbor = relation["target_id"] if relation["source_id"] == current else relation["source_id"]
                expansions.append({"from": current, "to": neighbor, "type": relation["relation_type"], "depth": depth + 1})
                if neighbor not in seen:
                    seen.add(neighbor)
                    frontier.append((neighbor, depth + 1))
                if len(expansions) >= 30:
                    break
        return RoutePlan(
            query=query,
            explicit_project=project,
            selected_project=selected_project,
            project_candidates=candidates,
            selected_domains=sorted(set(selected_domains)),
            seed_objects=list(dict.fromkeys(seed_objects)),
            relation_expansions=expansions,
            annotation_matches=annotation_matches,
            fallback_used=selected_project is None,
            raw_opened=[],
            selection_reasons=reasons,
        )


class ResearchDigestService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.annotations = ResearchAnnotationService(repository)
        self.activation = ActivationService(repository)

    def collect(self) -> dict[str, Any]:
        week_start = (datetime.now(TZ) - timedelta(days=7)).isoformat(timespec="seconds")
        annotations = [
            item for item in self.annotations.all()
            if str(item.get("created_at", "")) >= week_start
        ]
        feedback_items = [item for item in annotations if item.get("annotation_kind") == "connection_feedback"]
        feedback = {
            "top_interesting": [item for item in feedback_items if item.get("feedback_label") == "interesting"],
            "top_actionable": [item for item in feedback_items if item.get("feedback_label") == "actionable"],
            "repeated_forced_patterns": [item for item in feedback_items if item.get("feedback_label") == "forced"],
        }
        activation = self.activation.aggregate(since=week_start)
        capture_intents = [item for item in annotations if item.get("annotation_kind") == "capture_intent"]
        notes = [item for item in annotations if item.get("annotation_kind") == "research_note"]
        project_counts: Counter[str] = Counter()
        source_projects: dict[str, Counter[str]] = defaultdict(Counter)
        for item in annotations:
            projects = list(map(str, item.get("research_projects", [])))
            project_counts.update(projects)
            for target in item.get("target_ids", []):
                if str(target).startswith("source_"):
                    source_projects[str(target)].update(projects)
        active_questions: list[dict[str, Any]] = []
        for item in activation:
            try:
                _, target, _ = self.repository.find_document(str(item["object_id"]))
            except NotFoundError:
                continue
            if target.get("type") == "question":
                active_questions.append(item)
        return {
            "generated_at": now_iso(),
            "period_start": week_start,
            "new_sources": sum(
                str(read_document(path)[0].get("captured_at", "")) >= week_start
                for path in self.repository.source_documents()
            ),
            "sources_with_why_saved": len({
                target for item in capture_intents if item.get("why_saved")
                for target in item.get("target_ids", []) if str(target).startswith("source_")
            }),
            "high_salience_sources_without_why_saved": sorted({
                target for item in capture_intents
                if item.get("personal_salience") == "high" and not item.get("why_saved")
                for target in item.get("target_ids", []) if str(target).startswith("source_")
            }),
            "most_active_projects": project_counts.most_common(20),
            "most_active_questions": active_questions[:20],
            "interesting_connections": feedback["top_interesting"],
            "actionable_connections": feedback["top_actionable"],
            "forced_connections": feedback["repeated_forced_patterns"],
            "recently_used_trusted": self._used_by_tier(activation, "trusted"),
            "recently_used_working": self._used_by_tier(activation, "working"),
            "possible_unprocessed_connections": sorted({
                connection for item in annotations for connection in item.get("possible_connections", [])
            }),
            "recently_added_research_notes": [
                {"id": item["id"], "note": item.get("note", ""), "target_ids": item.get("target_ids", [])}
                for item in notes[-20:]
            ],
            "sources_with_repeated_project_associations": {
                source: dict(counts) for source, counts in source_projects.items() if sum(counts.values()) > 1
            },
        }

    def _used_by_tier(self, activation: list[dict[str, Any]], tier: str) -> list[dict[str, Any]]:
        result = []
        for item in activation:
            try:
                _, metadata, _ = self.repository.find_document(item["object_id"])
            except NotFoundError:
                continue
            if metadata.get("memory_tier") == tier:
                result.append(item)
        return result[:20]

    def write(self) -> dict[str, Any]:
        digest = self.collect()
        day = str(digest["generated_at"])[:10]
        path = self.repository.root / "system" / "reports" / f"generated-research-signals_{day}.md"
        lines = ["# Research Signal Digest", "", f"Generated: {digest['generated_at']}", ""]
        for key, value in digest.items():
            if key == "generated_at":
                continue
            lines.extend([f"## {key.replace('_', ' ').title()}", "", "```json",
                          json.dumps(value, ensure_ascii=False, indent=2), "```", ""])
        from .markdown import atomic_write_text
        atomic_write_text(path, "\n".join(lines).rstrip() + "\n")
        return {"path": self.repository.rel(path), "digest": digest}


class ResearchMapService:
    GENERATED_BY = "global-memory-research-map-v1"

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "views" / "research"
        self.digest = ResearchDigestService(repository)

    def build(self) -> dict[str, Any]:
        data = self.digest.collect()
        pages = {
            "研究项目.md": data["most_active_projects"],
            "研究问题.md": data["most_active_questions"],
            "高关注资料.md": data["high_salience_sources_without_why_saved"],
            "有趣连接.md": data["interesting_connections"],
            "可行动连接.md": data["actionable_connections"],
            "近期使用.md": [*data["recently_used_trusted"], *data["recently_used_working"]],
            "待补保存原因.md": data["high_salience_sources_without_why_saved"],
        }
        written: list[str] = []
        unchanged: list[str] = []
        skipped: list[str] = []
        removed: list[str] = []
        self.directory.mkdir(parents=True, exist_ok=True)
        from .markdown import atomic_write_text
        expected = {self.directory / name for name in pages}
        for stale in self.directory.glob("*.md"):
            if stale in expected:
                continue
            try:
                metadata, _ = read_document(stale)
            except ValidationError:
                continue
            if metadata.get("generated_by") == self.GENERATED_BY:
                removed.append(self.repository.rel(stale))
                stale.unlink()
        for name, value in pages.items():
            path = self.directory / name
            existing_metadata: dict[str, Any] | None = None
            existing_body: str | None = None
            if path.exists():
                try:
                    existing_metadata, existing_body = read_document(path)
                except ValidationError:
                    skipped.append(self.repository.rel(path))
                    continue
                if existing_metadata.get("generated_by") != self.GENERATED_BY:
                    skipped.append(self.repository.rel(path))
                    continue
            body = f"# {path.stem}\n\n```json\n{json.dumps(value, ensure_ascii=False, indent=2)}\n```"
            if existing_body == body:
                unchanged.append(self.repository.rel(path))
                continue
            timestamp = now_iso()
            metadata = {
                "id": "research_view_" + hashlib.sha256(name.encode("utf-8")).hexdigest()[:16],
                "type": "view", "status": "generated", "title": path.stem,
                "created_at": existing_metadata.get("created_at", timestamp) if existing_metadata else timestamp,
                "updated_at": timestamp,
                "generated_by": self.GENERATED_BY, "truth_layer": "derived_view",
            }
            atomic_write_text(path, render_document(metadata, body))
            written.append(self.repository.rel(path))
        return {"ok": True, "written": written, "unchanged": unchanged,
                "removed_stale_generated": removed,
                "skipped_non_generated": skipped}
