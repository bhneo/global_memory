from __future__ import annotations

import difflib
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from .errors import NotFoundError, ValidationError
from .extraction import ExtractionService
from .markdown import atomic_write_text, read_document, render_document
from .proposals import CANONICAL_DIRECTORIES, REVIEWABLE_PROPOSAL_STATUSES
from .repository import Repository, now_iso, sha256_bytes, slugify


class CompilerProvider(Protocol):
    name: str

    def compile(
        self, source: dict[str, Any], extraction: dict[str, Any], text: str,
        existing_context: list[dict[str, Any]], schema: dict[str, Any],
    ) -> list[dict[str, Any]]: ...


class DeterministicCompilerProvider:
    name = "deterministic-bounded-bundle-v1"
    MARKERS = {
        "claim": re.compile(r"^(?:claim|主张)\s*[:：]\s*(.+)$", re.I),
        "concept": re.compile(r"^(?:concept|概念)\s*[:：]\s*(.+)$", re.I),
        "question": re.compile(r"^(?:question|问题)\s*[:：]\s*(.+)$", re.I),
        "hypothesis": re.compile(r"^(?:hypothesis|假设)\s*[:：]\s*(.+)$", re.I),
        "tension": re.compile(r"^(?:tension|张力)\s*[:：]\s*(.+)$", re.I),
        "analogy": re.compile(r"^(?:analogy|类比)\s*[:：]\s*(.+)$", re.I),
    }

    def compile(
        self, source: dict[str, Any], extraction: dict[str, Any], text: str,
        existing_context: list[dict[str, Any]], schema: dict[str, Any],
    ) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        for line in text.splitlines():
            stripped = line.strip().lstrip("#*- ").strip()
            for object_type, pattern in self.MARKERS.items():
                match = pattern.match(stripped)
                if match:
                    statement = match.group(1).strip()
                    items.append({
                        "object_type": object_type, "title": statement[:160],
                        "body": statement, "span_start": text.find(statement),
                        "explicit_marker": True,
                    })
                    break
        if items:
            return items
        paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip() and not part.startswith("<!-- page:")]
        if not paragraphs:
            return []
        statement = paragraphs[0][:500]
        return [{
            "object_type": "claim", "title": f"来源原文：{statement[:80]}",
            "body": statement, "span_start": text.find(statement),
            "explicit_marker": False,
        }]


@dataclass(frozen=True)
class BundleResult:
    proposal_id: str
    proposal_path: str
    item_count: int
    item_ids: list[str]


class BundleRecoveryManager:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "system/recovery"

    def pending(self) -> list[Path]:
        return sorted(self.directory.glob("bundle-*.json")) if self.directory.exists() else []

    def prepare(self, record: dict[str, Any]) -> Path:
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.directory / f"bundle-{record['operation_id']}.json"
        atomic_write_text(path, json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        return path

    def recover_one(self, path: Path, failure_hook: Any = None) -> dict[str, Any]:
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("journal_version") != 1 or record.get("operation") != "approve_bundle":
            raise ValidationError(f"无效 bundle recovery journal: {path.name}")
        for target in record["targets"]:
            target_path = self.repository.resolve_inside(target["path"])
            before = sha256_bytes(target_path.read_bytes()) if target_path.exists() else None
            after = target["after_sha256"]
            if before == target["before_sha256"]:
                atomic_write_text(target_path, target["after_text"])
            elif before != after:
                raise ValidationError(f"bundle recovery blocked: {target['path']}")
        if failure_hook:
            failure_hook("targets_written")
        proposal_path = self.repository.resolve_inside(record["proposal_path"])
        current = sha256_bytes(proposal_path.read_bytes())
        if current == record["proposal_before_sha256"]:
            atomic_write_text(proposal_path, record["proposal_after_text"])
        elif current != record["proposal_after_sha256"]:
            raise ValidationError("bundle recovery blocked: proposal changed")
        if failure_hook:
            failure_hook("proposal_written")
        log_path = self.repository.root / "system/logs/proposal-events.jsonl"
        event_exists = False
        if log_path.exists():
            for line in log_path.read_text(encoding="utf-8").splitlines():
                try:
                    event_exists |= json.loads(line).get("operation_id") == record["operation_id"]
                except json.JSONDecodeError:
                    continue
        if not event_exists:
            self.repository.append_event("proposal-events", record["audit_payload"])
        self.repository.rebuild_index()
        path.unlink()
        return {"operation_id": record["operation_id"], "status": "recovered"}

    def recover_all(self) -> dict[str, list[dict[str, Any]]]:
        recovered, blocked = [], []
        for path in self.pending():
            try:
                recovered.append(self.recover_one(path))
            except Exception as exc:
                blocked.append({"journal": self.repository.rel(path), "error": str(exc)})
        return {"recovered": recovered, "blocked": blocked}


class BundleCompiler:
    def __init__(self, repository: Repository, provider: CompilerProvider | None = None):
        self.repository = repository
        self.provider = provider or DeterministicCompilerProvider()

    @staticmethod
    def _semantic_key(value: str) -> str:
        return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", value.lower())

    def _existing_context(self, source: dict[str, Any], text: str) -> list[dict[str, Any]]:
        terms = [str(source.get("title", ""))]
        terms.extend(re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}|[\u4e00-\u9fff]{4,}", text[:1500])[:5])
        found: dict[str, dict[str, Any]] = {}
        for term in terms:
            try:
                for result in self.repository.search(term, 10):
                    if result.type != "source" and result.status != "archived":
                        found[result.id] = result.__dict__
            except ValidationError:
                continue
        return list(found.values())

    def _find_same_object(self, object_type: str, title: str) -> tuple[Path, dict[str, Any], str] | None:
        key = self._semantic_key(title)
        for path in self.repository.canonical_documents():
            metadata, body = read_document(path)
            aliases = [metadata.get("title", ""), *metadata.get("aliases", [])]
            if metadata.get("type") == object_type and any(self._semantic_key(str(item)) == key for item in aliases):
                return path, metadata, body
        return None

    def compile(self, source_id: str) -> BundleResult:
        source_path, source, _ = self.repository.find_document(source_id)
        if source.get("type") != "source":
            raise ValidationError(f"compile 只接受 source: {source_id}")
        extraction_path, extraction, text = ExtractionService(self.repository).latest_for_source(source_id, create=True)
        existing_context = self._existing_context(source, text)
        specs = self.provider.compile(
            source, extraction, text, existing_context,
            {"object_types": sorted(CANONICAL_DIRECTORIES), "evidence_kinds": ["quote", "paraphrase", "translation", "table_value", "figure", "calculation"]},
        )
        if not isinstance(specs, list) or not specs:
            raise ValidationError("compiler 没有产生有意义的 bundle item")
        timestamp = now_iso()
        prepared: list[dict[str, Any]] = []
        for index, spec in enumerate(specs, start=1):
            object_type = str(spec.get("object_type", ""))
            if object_type not in CANONICAL_DIRECTORIES or object_type in {"work", "synthesis"}:
                raise ValidationError(f"compiler provider 返回不支持的 object_type: {object_type}")
            title = str(spec.get("title", "")).strip()
            body_text = str(spec.get("body", "")).strip()
            if not title or not body_text:
                raise ValidationError("compiler provider item 缺少 title/body")
            same = self._find_same_object(object_type, title)
            if same:
                target_path, target, old_body = same
                action = "update"
                base_bytes = target_path.read_bytes()
                target_id = str(target["id"])
                source_ids = list(dict.fromkeys([*target.get("source_ids", []), source_id]))
                created_at = target["created_at"]
                relations = list(target.get("relations", []))
                canonical_body = old_body
                if source_id not in target.get("source_ids", []):
                    canonical_body = old_body.rstrip() + f"\n\n## 新增来源材料\n\n- `{source_id}`：{body_text}\n"
            else:
                digest = hashlib.sha256(f"{object_type}\n{self._semantic_key(title)}".encode("utf-8")).hexdigest()
                target_id = f"{object_type}_{digest[:24]}"
                target_path = self.repository.root / CANONICAL_DIRECTORIES[object_type] / f"{target_id}-{slugify(title)}.md"
                action = "create"
                base_bytes = b""
                source_ids = [source_id]
                created_at = timestamp
                relations = [{"type": "derived_from", "target_id": source_id, "reason": "由 compile bundle 从该来源提出"}]
                canonical_body = f"# {title}\n\n{body_text}\n"
            contradiction = re.search(r"\[contradicts:([\w_-]+)\]", body_text, re.I)
            if contradiction:
                relations.append({"type": "contradicts", "target_id": contradiction.group(1), "reason": "来源显式标注为与既有主张冲突"})
            candidate: dict[str, Any] = {
                "id": target_id, "type": object_type, "status": "proposal", "title": title,
                "created_at": created_at, "updated_at": timestamp,
                "aliases": list(target.get("aliases", [])) if action == "update" else [],
                "tags": list(target.get("tags", [])) if action == "update" else [],
                "domains": list(target.get("domains", [])) if action == "update" else [],
                "confidence": target.get("confidence", "unknown") if action == "update" else ("low" if object_type in {"claim", "hypothesis"} else "unknown"),
                "source_ids": source_ids, "relations": relations,
                "change_reason": f"compile bundle from {source_id}",
            }
            if action == "update":
                candidate["proposed_status"] = target.get("status", "confirmed")
            if object_type == "claim":
                start = max(0, int(spec.get("span_start", text.find(body_text))))
                original = text[start:start + len(body_text)]
                if original != body_text:
                    start = text.find(body_text)
                evidence = {
                    "evidence_id": f"evidence_{hashlib.sha256(f'{source_id}:{start}:{body_text}'.encode()).hexdigest()[:20]}",
                    "evidence_kind": "quote", "source_id": source_id,
                    "content_id": source.get("content_id"), "extraction_id": extraction["extraction_id"],
                    "span_start": start, "span_end": start + len(body_text), "original_text": body_text,
                    "page": self._page_for_span(text, start), "stance": "context",
                    "verification_status": "verified", "input_sha256": extraction["input_sha256"],
                    "extractor": extraction["extractor"], "extractor_version": extraction["extractor_version"],
                    "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。",
                }
                candidate.update({
                    "evidence": [evidence], "applicability": [],
                    "uncertainty": "确定性 fallback 能力有限；该原文尚未经过语义事实核验。",
                })
            candidate_text = render_document(candidate, canonical_body)
            self.repository._validate_metadata(candidate, target_path)
            candidate_sha = sha256_bytes(candidate_text.encode("utf-8"))
            item_id = f"{object_type}-{index}"
            prepared.append({
                "item_id": item_id, "object_type": object_type, "action": action,
                "target_id": target_id, "target_path": self.repository.rel(target_path),
                "base_sha256": sha256_bytes(base_bytes) if base_bytes else None,
                "base_bytes": base_bytes, "candidate_text": candidate_text,
                "candidate_sha256": candidate_sha, "decision": "pending",
                "potential_conflicts": [relation for relation in relations if relation["type"] == "contradicts"],
            })
        bundle_digest = hashlib.sha256(
            (source_id + "\n" + "\n".join(item["candidate_sha256"] for item in prepared)).encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_bundle_{bundle_digest[:20]}"
        proposal_path = self.repository.root / "vault/proposals" / f"proposal-{proposal_id}.md"
        if proposal_path.exists():
            old, _ = read_document(proposal_path)
            return BundleResult(proposal_id, self.repository.rel(proposal_path), len(old["bundle_items"]), [item["item_id"] for item in old["bundle_items"]])
        bundle_items: list[dict[str, Any]] = []
        diff_sections: list[str] = []
        for item in prepared:
            candidate_path = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}-{item['item_id']}.md"
            base_path = self.repository.root / "vault/proposals" / f"base-{proposal_id}-{item['item_id']}.md"
            self.repository.immutable_write(candidate_path, item["candidate_text"].encode("utf-8"))
            if item["base_bytes"]:
                self.repository.immutable_write(base_path, item["base_bytes"])
            diff = "".join(difflib.unified_diff(
                item["base_bytes"].decode("utf-8").splitlines(keepends=True) if item["base_bytes"] else [],
                item["candidate_text"].splitlines(keepends=True),
                fromfile=f"base:{item['target_path']}" if item["base_bytes"] else "/dev/null",
                tofile=f"candidate:{item['target_path']}",
            ))
            bundle_items.append({
                key: value for key, value in item.items()
                if key not in {"base_bytes", "candidate_text"}
            } | {
                "candidate_path": self.repository.rel(candidate_path),
                "base_path": self.repository.rel(base_path) if item["base_bytes"] else None,
            })
            diff_sections.append(f"### {item['item_id']} ({item['action']} {item['object_type']})\n\n```diff\n{diff.rstrip()}\n```\n")
        proposal = {
            "id": proposal_id, "type": "proposal", "status": "pending",
            "title": f"Compile bundle：{source['title']}", "created_at": timestamp,
            "updated_at": timestamp, "aliases": [], "tags": [], "domains": [],
            "confidence": "low", "source_ids": [source_id], "relations": [],
            "proposal_kind": "compile_bundle", "processor": self.provider.name,
            "extraction_id": extraction["extraction_id"], "input_sha256": extraction["input_sha256"],
            "bundle_items": bundle_items, "existing_context": existing_context,
            "contradiction_candidates": [conflict for item in bundle_items for conflict in item["potential_conflicts"]],
            "unresolved_items": [] if specs else ["provider 未产生候选"],
            "provenance_validation": {"ok": True, "items": len(bundle_items), "source_id": source_id},
            "reviewed_at": None, "review_reason": None,
        }
        body = (
            f"# {proposal['title']}\n\n## 编译边界\n\n"
            f"- Provider：`{self.provider.name}`\n- Extraction：`{extraction['extraction_id']}`\n"
            f"- 编译前召回已有对象：{len(existing_context)}\n"
            "- deterministic fallback 只识别显式类型标记或保留第一段逐字材料，不补齐无意义对象。\n\n"
            "## Items and diffs\n\n" + "\n".join(diff_sections)
        )
        self.repository.immutable_write(proposal_path, render_document(proposal, body).encode("utf-8"))
        return BundleResult(proposal_id, self.repository.rel(proposal_path), len(bundle_items), [item["item_id"] for item in bundle_items])

    @staticmethod
    def _page_for_span(text: str, start: int) -> int | None:
        pages = list(re.finditer(r"<!-- page:\s*(\d+)\s*-->", text[:max(0, start) + 1]))
        return int(pages[-1].group(1)) if pages else None


class BundleReviewService:
    def __init__(self, repository: Repository, failure_hook: Any = None):
        self.repository = repository
        self.failure_hook = failure_hook

    def _load(self, proposal_id: str) -> tuple[Path, dict[str, Any], str]:
        path, metadata, body = self.repository.find_document(proposal_id)
        if metadata.get("proposal_kind") != "compile_bundle":
            raise ValidationError(f"不是 compile bundle: {proposal_id}")
        return path, metadata, body

    @staticmethod
    def _selected(proposal: dict[str, Any], item_ids: list[str] | None) -> list[dict[str, Any]]:
        items = proposal.get("bundle_items", [])
        requested = set(item_ids or [item["item_id"] for item in items if item.get("decision") == "pending"])
        selected = [item for item in items if item.get("item_id") in requested]
        if not selected or {item["item_id"] for item in selected} != requested:
            raise ValidationError("bundle items 不存在或为空")
        if any(item.get("decision") != "pending" for item in selected):
            raise ValidationError("只能审阅 pending bundle items")
        return selected

    def approve(self, proposal_id: str, item_ids: list[str] | None = None) -> dict[str, Any]:
        proposal_path, proposal, body = self._load(proposal_id)
        if proposal.get("status") not in REVIEWABLE_PROPOSAL_STATUSES:
            raise ValidationError(f"bundle proposal 状态不可审批: {proposal.get('status')}")
        selected = self._selected(proposal, item_ids)
        targets: list[dict[str, Any]] = []
        timestamp = now_iso()
        for item in selected:
            candidate_path = self.repository.resolve_inside(item["candidate_path"])
            candidate_text = candidate_path.read_text(encoding="utf-8")
            if sha256_bytes(candidate_text.encode("utf-8")) != item["candidate_sha256"]:
                raise ValidationError(f"bundle candidate hash 不匹配: {item['item_id']}")
            candidate, candidate_body = read_document(candidate_path)
            self.repository._validate_metadata(candidate, candidate_path)
            target_path = self.repository.resolve_inside(item["target_path"])
            before_sha = sha256_bytes(target_path.read_bytes()) if target_path.exists() else None
            if before_sha != item.get("base_sha256"):
                raise ValidationError(f"bundle target 在审阅期间变化: {item['item_id']}")
            canonical = dict(candidate)
            status = canonical.pop("proposed_status", "confirmed")
            canonical["status"] = status
            canonical["updated_at"] = timestamp
            canonical["approved_via"] = f"{proposal_id}:{item['item_id']}"
            after_text = render_document(canonical, candidate_body)
            targets.append({
                "item_id": item["item_id"], "path": item["target_path"],
                "before_sha256": before_sha, "after_text": after_text,
                "after_sha256": sha256_bytes(after_text.encode("utf-8")),
            })
            item["decision"] = "approved"
            item["reviewed_at"] = timestamp
        pending = [item for item in proposal["bundle_items"] if item.get("decision") == "pending"]
        proposal["status"] = "pending" if pending else "approved"
        proposal["updated_at"] = timestamp
        proposal["reviewed_at"] = timestamp
        proposal["review_reason"] = f"批准 bundle items: {', '.join(item['item_id'] for item in selected)}"
        proposal_after = render_document(proposal, body)
        operation_id = f"bundle_{proposal_id}_{hashlib.sha256(','.join(item['item_id'] for item in selected).encode()).hexdigest()[:12]}"
        record = {
            "journal_version": 1, "operation": "approve_bundle", "operation_id": operation_id,
            "proposal_id": proposal_id, "created_at": timestamp, "targets": targets,
            "proposal_path": self.repository.rel(proposal_path),
            "proposal_before_sha256": sha256_bytes(proposal_path.read_bytes()),
            "proposal_after_text": proposal_after,
            "proposal_after_sha256": sha256_bytes(proposal_after.encode("utf-8")),
            "audit_payload": {"event": "bundle-items-approved", "operation_id": operation_id,
                              "proposal_id": proposal_id, "item_ids": [item["item_id"] for item in selected]},
        }
        journal = BundleRecoveryManager(self.repository).prepare(record)
        if self.failure_hook:
            self.failure_hook("prepared")
        BundleRecoveryManager(self.repository).recover_one(journal, self.failure_hook)
        return {"proposal_id": proposal_id, "approved_items": [item["item_id"] for item in selected],
                "target_paths": [target["path"] for target in targets], "remaining_items": len(pending)}

    def reject(self, proposal_id: str, item_ids: list[str] | None = None, reason: str = "") -> dict[str, Any]:
        proposal_path, proposal, body = self._load(proposal_id)
        selected = self._selected(proposal, item_ids)
        timestamp = now_iso()
        for item in selected:
            item["decision"] = "rejected"
            item["reviewed_at"] = timestamp
            item["review_reason"] = reason or "用户拒绝该 bundle item"
        pending = [item for item in proposal["bundle_items"] if item.get("decision") == "pending"]
        proposal["status"] = "pending" if pending else "rejected"
        proposal["updated_at"] = timestamp
        atomic_write_text(proposal_path, render_document(proposal, body))
        self.repository.append_event("proposal-events", {
            "event": "bundle-items-rejected", "proposal_id": proposal_id,
            "item_ids": [item["item_id"] for item in selected], "reason": reason,
        })
        return {"proposal_id": proposal_id, "rejected_items": [item["item_id"] for item in selected],
                "remaining_items": len(pending)}

    def revise_item(
        self, proposal_id: str, item_id: str, candidate_file: Path | str, reason: str,
    ) -> dict[str, Any]:
        proposal_path, proposal, body = self._load(proposal_id)
        selected = self._selected(proposal, [item_id])[0]
        input_path = Path(candidate_file).expanduser().resolve()
        if not input_path.is_file() or not reason.strip():
            raise ValidationError("bundle item revision 必须提供 candidate 文件和 reason")
        candidate_text = input_path.read_text(encoding="utf-8")
        candidate, _ = read_document(input_path)
        if (
            candidate.get("id") != selected["target_id"]
            or candidate.get("type") != selected["object_type"]
            or candidate.get("status") != "proposal"
        ):
            raise ValidationError("bundle revision candidate 的 id/type/status 无效")
        self.repository._validate_metadata(candidate, input_path)
        old_path = self.repository.resolve_inside(selected["candidate_path"])
        old_text = old_path.read_text(encoding="utf-8")
        digest = sha256_bytes(candidate_text.encode("utf-8"))
        revision_path = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}-{item_id}-rev-{digest[:12]}.md"
        self.repository.immutable_write(revision_path, candidate_text.encode("utf-8"))
        history = list(selected.get("revision_history", []))
        history.append({
            "candidate_path": selected["candidate_path"],
            "candidate_sha256": selected["candidate_sha256"], "reason": reason.strip(),
            "revised_at": now_iso(),
        })
        selected["revision_history"] = history
        selected["candidate_path"] = self.repository.rel(revision_path)
        selected["candidate_sha256"] = digest
        selected["review_reason"] = reason.strip()
        proposal["updated_at"] = now_iso()
        diff = "".join(difflib.unified_diff(
            old_text.splitlines(keepends=True), candidate_text.splitlines(keepends=True),
            fromfile="previous-candidate", tofile="revised-candidate",
        ))
        body = body.rstrip() + f"\n\n## Item revision: {item_id}\n\n- Reason: {reason.strip()}\n\n```diff\n{diff.rstrip()}\n```\n"
        atomic_write_text(proposal_path, render_document(proposal, body))
        self.repository.append_event("proposal-events", {
            "event": "bundle-item-revised", "proposal_id": proposal_id,
            "item_id": item_id, "candidate_sha256": digest, "reason": reason.strip(),
        })
        return {"proposal_id": proposal_id, "item_id": item_id,
                "candidate_path": self.repository.rel(revision_path), "candidate_sha256": digest}
