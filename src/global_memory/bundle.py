from __future__ import annotations

import difflib
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol

from .errors import NotFoundError, ValidationError
from .atomicity import AtomicClaimInspector
from .extraction import ExtractionService
from .followups import FollowupService
from .markdown import atomic_write_text, read_document, render_document
from .proposals import CANONICAL_DIRECTORIES, REVIEWABLE_PROPOSAL_STATUSES
from .quality import SourceQualityService
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
        "anomaly": re.compile(r"^(?:anomaly|异常)\s*[:：]\s*(.+)$", re.I),
        "project": re.compile(r"^(?:project|项目)\s*[:：]\s*(.+)$", re.I),
        "goal": re.compile(r"^(?:goal|目标)\s*[:：]\s*(.+)$", re.I),
        "architecture": re.compile(r"^(?:architecture|架构)\s*[:：]\s*(.+)$", re.I),
        "decision": re.compile(r"^(?:decision|决策)\s*[:：]\s*(.+)$", re.I),
        "experiment": re.compile(r"^(?:experiment|实验)\s*[:：]\s*(.+)$", re.I),
        "failure": re.compile(r"^(?:failure|失败)\s*[:：]\s*(.+)$", re.I),
        "opportunity": re.compile(r"^(?:opportunity|机会)\s*[:：]\s*(.+)$", re.I),
    }

    def compile(
        self, source: dict[str, Any], extraction: dict[str, Any], text: str,
        existing_context: list[dict[str, Any]], schema: dict[str, Any],
    ) -> list[dict[str, Any]]:
        markers: list[tuple[int, int, str, str]] = []
        offset = 0
        for line in text.splitlines(keepends=True):
            stripped = line.strip().lstrip("#*- ").strip()
            for object_type, pattern in self.MARKERS.items():
                match = pattern.match(stripped)
                if match:
                    statement = match.group(1).strip()
                    markers.append((offset, offset + len(line), object_type, statement))
                    break
            offset += len(line)
        if markers:
            items: list[dict[str, Any]] = []
            for index, (line_start, line_end, object_type, statement) in enumerate(markers):
                block_end = markers[index + 1][0] if index + 1 < len(markers) else len(text)
                tail = text[line_end:block_end].strip()
                body = statement + (f"\n\n{tail}" if tail else "")
                items.append({
                    "object_type": object_type, "title": statement[:160],
                    "body": body, "span_start": line_start + text[line_start:line_end].find(statement),
                    "explicit_marker": True,
                })
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


class JsonBundleProvider:
    """Provider-neutral adapter for externally generated, local JSON bundle items."""

    def __init__(self, path: Path | str, name: str = "external-json-bundle-v1"):
        self.path = Path(path).expanduser().resolve()
        self.name = name

    def compile(
        self, source: dict[str, Any], extraction: dict[str, Any], text: str,
        existing_context: list[dict[str, Any]], schema: dict[str, Any],
    ) -> list[dict[str, Any]]:
        if not self.path.is_file():
            raise ValidationError(f"external bundle JSON 不存在: {self.path}")
        try:
            payload = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValidationError(f"无法读取 external bundle JSON: {exc}") from exc
        items = payload.get("items") if isinstance(payload, dict) else payload
        if not isinstance(items, list):
            raise ValidationError("external bundle JSON 必须是 item 列表或包含 items 列表")
        return items


@dataclass(frozen=True)
class BundleResult:
    proposal_id: str | None
    proposal_path: str | None
    item_count: int
    item_ids: list[str]
    compile_disposition: str = "knowledge_proposed"
    quality: dict[str, Any] | None = None


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
    UNSTRUCTURED_FALLBACK_MAX_CHARS = 2000

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
        for path in [*self.repository.memory_documents(), *self.repository.canonical_documents()]:
            metadata, body = read_document(path)
            aliases = [metadata.get("title", ""), *metadata.get("aliases", [])]
            if metadata.get("type") == object_type and any(self._semantic_key(str(item)) == key for item in aliases):
                return path, metadata, body
        return None

    def _find_target(self, target_id: str, object_type: str) -> tuple[Path, dict[str, Any], str]:
        try:
            path, metadata, body = self.repository.find_document(target_id)
        except Exception as exc:
            raise ValidationError(f"provider update target_id does not exist: {target_id}") from exc
        relative = self.repository.rel(path)
        if not relative.startswith(("vault/memory/", "vault/knowledge/", "vault/frontier/", "vault/action/")):
            raise ValidationError(f"provider update target_id is not governed knowledge: {target_id}")
        if metadata.get("type") != object_type:
            raise ValidationError(
                f"provider update target_id type mismatch: expected {object_type}, got {metadata.get('type')}"
            )
        return path, metadata, body

    def _record_source_only(
        self, source_id: str, source: dict[str, Any], extraction: dict[str, Any],
        quality: Any, *, reason: str,
    ) -> BundleResult:
        digest = hashlib.sha256(
            f"source-only\n{source_id}\n{extraction['input_sha256']}\n{self.provider.name}\n{reason}".encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_bundle_{digest[:20]}"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        if not proposal_path.exists():
            timestamp = now_iso()
            proposal = {
                "id": proposal_id, "type": "proposal", "status": "source_only",
                "title": f"Source-only compile: {source.get('title', source_id)}",
                "created_at": timestamp, "updated_at": timestamp,
                "aliases": [], "tags": [], "domains": [], "confidence": "unknown",
                "source_ids": [source_id], "relations": [],
                "proposal_kind": "compile_bundle", "processor": self.provider.name,
                "review_unit": "source_bundle", "compile_disposition": "source_only",
                "source_summary": str(source.get("title", source_id)),
                "source_authority": quality.source_authority,
                "availability_status": quality.availability_status,
                "content_quality": quality.content_quality,
                "extraction_quality": quality.extraction_quality,
                "extraction_id": extraction["extraction_id"],
                "input_sha256": extraction["input_sha256"],
                "bundle_items": [], "source_only_source_ids": [source_id],
                "low_value_items_not_proposed": [reason],
                "reviewed_at": timestamp, "review_reason": reason,
            }
            body = (
                f"# {proposal['title']}\n\n"
                "No governed knowledge object was materialized. The immutable source and extraction remain searchable.\n\n"
                f"- Reason: {reason}\n- Provider: `{self.provider.name}`\n"
            )
            self.repository.immutable_write(
                proposal_path, render_document(proposal, body).encode("utf-8")
            )
        return BundleResult(
            proposal_id, self.repository.rel(proposal_path), 0, [],
            "source_only", quality.as_dict(),
        )

    def _deterministic_fallback_allowed(self, source: dict[str, Any], text: str, specs: list[dict[str, Any]]) -> bool:
        """Allow paragraph fallback only for deliberate, sentence-like user notes."""
        if any(bool(spec.get("explicit_marker")) for spec in specs):
            return True
        if source.get("source_kind") != "personal-notes":
            return False
        normalized = " ".join(text.split())
        if len(normalized) < 40 or len(normalized) > self.UNSTRUCTURED_FALLBACK_MAX_CHARS:
            return False
        if normalized == str(source.get("title", "")).strip():
            return False
        return any(mark in normalized for mark in (".", "?", "!", "。", "？", "！"))

    def compile(self, source_id: str) -> BundleResult:
        source_path, source, _ = self.repository.find_document(source_id)
        if source.get("type") != "source":
            raise ValidationError(f"compile 只接受 source: {source_id}")
        quality = SourceQualityService(self.repository).assess(source_id, persist=True)
        if not quality.compile_allowed:
            FollowupService(self.repository).create(
                source_id, str(source.get("canonical_locator") or "") or None,
                reason=f"source unavailable or invalid: {quality.availability_status}/{quality.content_quality}",
                kind="source_recovery",
            )
            return BundleResult(None, None, 0, [], "invalid_content", quality.as_dict())
        extraction_path, extraction, text = ExtractionService(self.repository).latest_for_source(source_id, create=True)
        existing_context = self._existing_context(source, text)
        specs = self.provider.compile(
            source, extraction, text, existing_context,
            {"object_types": sorted(CANONICAL_DIRECTORIES), "evidence_kinds": ["quote", "paraphrase", "translation", "table_value", "figure", "calculation"]},
        )
        if not isinstance(specs, list):
            raise ValidationError("compiler provider 必须返回 bundle item 列表")
        if not specs:
            return self._record_source_only(
                source_id, source, extraction, quality,
                reason="compiler provider produced no governed knowledge candidates",
            )
        if isinstance(self.provider, DeterministicCompilerProvider) and not self._deterministic_fallback_allowed(source, text, specs):
            return self._record_source_only(
                source_id, source, extraction, quality,
                reason=(
                    "unmarked capture is source-only by default; deterministic paragraph fallback "
                    "is reserved for bounded, sentence-like personal notes"
                ),
            )
        expanded_specs: list[dict[str, Any]] = []
        for spec in specs:
            if not isinstance(spec, dict):
                raise ValidationError("compiler provider item 必须是对象")
            expanded_specs.extend(AtomicClaimInspector.split_spec(spec, text))
        specs = []
        seen_specs: set[tuple[str, str, str, str]] = set()
        for spec in expanded_specs:
            key = (
                str(spec.get("object_type")), str(spec.get("action", "")),
                str(spec.get("target_id", "")), self._semantic_key(str(spec.get("title", ""))),
            )
            if key in seen_specs:
                continue
            seen_specs.add(key)
            specs.append(spec)
        timestamp = now_iso()
        prepared: list[dict[str, Any]] = []
        for index, spec in enumerate(specs, start=1):
            object_type = str(spec.get("object_type", ""))
            if object_type not in CANONICAL_DIRECTORIES or object_type == "synthesis":
                raise ValidationError(f"compiler provider 返回不支持的 object_type: {object_type}")
            title = str(spec.get("title", "")).strip()
            body_text = str(spec.get("body", "")).strip()
            if not title or not body_text:
                raise ValidationError("compiler provider item 缺少 title/body")
            requested_action = str(spec.get("action", "")).strip().lower()
            requested_target_id = str(spec.get("target_id", "")).strip()
            if requested_action and requested_action not in {"create", "update"}:
                raise ValidationError(f"compiler provider item has unsupported action: {requested_action}")
            if requested_action == "update" and not requested_target_id:
                raise ValidationError("provider update requires stable target_id")
            same = (
                self._find_target(requested_target_id, object_type)
                if requested_target_id and requested_action != "create"
                else self._find_same_object(object_type, title) if not requested_action else None
            )
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
                supplied_metadata = spec.get("metadata", {})
                if supplied_metadata is not None and not isinstance(supplied_metadata, dict):
                    raise ValidationError("compiler provider item.metadata 必须是对象")
                explicit_id = requested_target_id or str((supplied_metadata or {}).get("id", ""))
                if requested_action == "create" and requested_target_id:
                    try:
                        self.repository.find_document(requested_target_id)
                    except Exception:
                        pass
                    else:
                        raise ValidationError(f"provider create target_id already exists: {requested_target_id}")
                if object_type == "work" and not explicit_id:
                    raise ValidationError("bundle work enrichment 必须提供 metadata.id 稳定身份")
                digest = hashlib.sha256(f"{object_type}\n{self._semantic_key(title)}".encode("utf-8")).hexdigest()
                target_id = explicit_id or f"{object_type}_{digest[:24]}"
                target_path = self.repository.root / CANONICAL_DIRECTORIES[object_type] / f"{target_id}-{slugify(title)}.md"
                action = "create"
                base_bytes = b""
                source_ids = [source_id]
                created_at = timestamp
                relations = [{
                    "type": "derived_from", "target_id": source_id,
                    "reason": "由 compile bundle 从该来源提出", "confidence": "high",
                    "created_by": self.provider.name, "status": "proposal",
                }]
                canonical_body = f"# {title}\n\n{body_text}\n"
            contradiction = re.search(r"\[contradicts:([\w_-]+)\]", body_text, re.I)
            if contradiction:
                relations.append({
                    "type": "contradicts", "target_id": contradiction.group(1),
                    "reason": "来源显式标注为与既有主张冲突", "confidence": "medium",
                    "created_by": self.provider.name, "status": "proposal",
                })
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
            # A provider must name the semantic effect of an update.  Heuristic
            # compilation is not allowed to silently turn new text into support.
            if action == "update":
                candidate["change_type"] = str(spec.get("change_type") or "needs_review")
            extra_metadata = spec.get("metadata", {}) or {}
            protected = {"id", "type", "status", "created_at", "updated_at", "source_ids", "relations"}
            for key, value in extra_metadata.items():
                if key not in protected:
                    candidate[key] = value
            if action == "update":
                candidate["proposed_status"] = target.get("status", "confirmed")
            if object_type == "claim":
                start = max(0, int(spec.get("span_start", text.find(body_text))))
                original = text[start:start + len(body_text)]
                if original != body_text:
                    start = text.find(body_text)
                evidence = {
                    "evidence_id": f"evidence_{hashlib.sha256(f'{source_id}:{start}:{body_text}'.encode()).hexdigest()[:20]}",
                    "evidence_kind": "quote" if start >= 0 else "paraphrase", "source_id": source_id,
                    "content_id": source.get("content_id"), "extraction_id": extraction["extraction_id"],
                    "span_start": start, "span_end": start + len(body_text), "original_text": body_text,
                    "interpretation": body_text if start < 0 else None,
                    "section": "deterministic extracted block" if start < 0 else None,
                    "page": self._page_for_span(text, start), "stance": "context",
                    "verification_status": "verified" if start >= 0 else "derived", "input_sha256": extraction["input_sha256"],
                    "extractor": extraction["extractor"], "extractor_version": extraction["extractor_version"],
                    "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。",
                }
                candidate.update({
                    "evidence": [evidence], "applicability": [],
                    "uncertainty": "确定性 fallback 能力有限；该原文尚未经过语义事实核验。",
                    "atomicity_status": spec.get("atomicity_status", "atomic"),
                    "evidence_coverage": spec.get("evidence_coverage", "full" if start >= 0 else "missing"),
                    "split_from": spec.get("split_from"), "split_reason": spec.get("split_reason"),
                    "quote_verification": "exact" if start >= 0 else "failed",
                    "extraction_quality": quality.extraction_quality,
                    "epistemic_source_authority": (
                        "primary" if quality.source_authority in {"primary", "official", "peer_reviewed", "preprint"}
                        else "secondary" if quality.source_authority == "secondary_analysis"
                        else "commentary" if quality.source_authority in {"industry_commentary", "marketing", "social_post"}
                        else "anecdotal" if quality.source_authority == "anecdotal" else "unknown"
                    ),
                    "evidence_entailment": str(spec.get("evidence_entailment", "none")),
                    "claim_confidence": str(spec.get("claim_confidence", "low")),
                    "publication_gate": "needs_review",
                })
                # Provider-supplied stance/evidence is semantic input, not a
                # cosmetic override; preserve it after deterministic defaults.
                for key in ("evidence", "evidence_entailment", "claim_confidence", "applicability"):
                    if key in extra_metadata:
                        candidate[key] = extra_metadata[key]
            candidate_text = render_document(candidate, canonical_body)
            # Validate candidate semantics in the proposal layer. The target may already
            # be a Working object whose lifecycle schema intentionally rejects status=proposal.
            self.repository._validate_metadata(
                candidate, self.repository.root / "vault" / "proposals" / "_candidate-validation.md"
            )
            candidate_sha = sha256_bytes(candidate_text.encode("utf-8"))
            item_id = f"{object_type}-{index}"
            prepared.append({
                "item_id": item_id, "object_type": object_type, "action": action,
                "target_id": target_id, "target_path": self.repository.rel(target_path),
                "base_sha256": sha256_bytes(base_bytes) if base_bytes else None,
                "base_bytes": base_bytes, "candidate_text": candidate_text,
                "candidate_sha256": candidate_sha, "decision": "pending",
                "potential_conflicts": [relation for relation in relations if relation["type"] == "contradicts"],
                "atomicity_status": candidate.get("atomicity_status"),
                "evidence_coverage": candidate.get("evidence_coverage"),
                "review_tier": "high" if (
                    object_type != "claim" or (
                        candidate.get("atomicity_status") == "atomic"
                        and candidate.get("evidence_coverage") == "full"
                        and candidate.get("evidence_entailment") == "full"
                        and quality.extraction_quality == "good"
                    )
                ) and quality.source_authority in {"primary", "official", "peer_reviewed", "preprint"} else "low",
            })
        bundle_digest = hashlib.sha256(
            (source_id + "\n" + "\n".join(item["candidate_sha256"] for item in prepared)).encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_bundle_{bundle_digest[:20]}"
        proposal_path = self.repository.root / "vault/proposals" / f"proposal-{proposal_id}.md"
        if proposal_path.exists():
            old, _ = read_document(proposal_path)
            return BundleResult(proposal_id, self.repository.rel(proposal_path), len(old["bundle_items"]), [item["item_id"] for item in old["bundle_items"]], old.get("compile_disposition", "knowledge_proposed"), quality.as_dict())
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
        followups = FollowupService(self.repository).detect(source_id)
        new_count = sum(item["action"] == "create" for item in bundle_items)
        update_count = sum(item["action"] == "update" for item in bundle_items)
        proposal = {
            "id": proposal_id, "type": "proposal", "status": "pending",
            "title": f"Compile bundle：{source['title']}", "created_at": timestamp,
            "updated_at": timestamp, "aliases": [], "tags": [], "domains": [],
            "confidence": "low", "source_ids": [source_id], "relations": [],
            "proposal_kind": "compile_bundle", "processor": self.provider.name,
            "review_unit": "source_bundle", "compile_disposition": "knowledge_proposed",
            "source_summary": str(source.get("title", source_id)),
            "source_authority": quality.source_authority,
            "availability_status": quality.availability_status,
            "content_quality": quality.content_quality,
            "extraction_quality": quality.extraction_quality,
            "extraction_id": extraction["extraction_id"], "input_sha256": extraction["input_sha256"],
            "bundle_items": bundle_items, "existing_context": existing_context,
            "contradiction_candidates": [conflict for item in bundle_items for conflict in item["potential_conflicts"]],
            "unresolved_items": [] if specs else ["provider 未产生候选"],
            "provenance_validation": {"ok": True, "items": len(bundle_items), "source_id": source_id},
            "primary_source_followups": [item["id"] for item in followups],
            "duplicate_findings": [], "low_value_items_not_proposed": [],
            "bundle_metrics": {
                "novelty_score": round(new_count / max(1, len(bundle_items)), 2),
                "importance_score": "requires_human_judgment",
                "source_authority": quality.source_authority,
                "evidence_quality": quality.extraction_quality,
                "knowledge_reuse_count": update_count,
                "new_object_count": new_count, "updated_object_count": update_count,
                "duplicate_count": len(expanded_specs) - len(specs),
                "unresolved_count": 0, "review_cost_estimate": len(bundle_items),
                "scoring_basis": "deterministic counts and quality labels; not a calibrated probability",
            },
            "reviewed_at": None, "review_reason": None,
        }
        body = (
            f"# {proposal['title']}\n\n## 编译边界\n\n"
            f"- Provider：`{self.provider.name}`\n- Extraction：`{extraction['extraction_id']}`\n"
            f"- 编译前召回已有对象：{len(existing_context)}\n"
            "- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。\n\n"
            "## Items and diffs\n\n" + "\n".join(diff_sections)
        )
        self.repository.immutable_write(proposal_path, render_document(proposal, body).encode("utf-8"))
        return BundleResult(proposal_id, self.repository.rel(proposal_path), len(bundle_items), [item["item_id"] for item in bundle_items], "knowledge_proposed", quality.as_dict())

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
        if metadata.get("proposal_kind") not in {"compile_bundle", "source_bundle", "corpus_distillation"}:
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
        selected_targets = {str(item["target_id"]) for item in selected}
        bundle_targets = {str(item["target_id"]) for item in proposal.get("bundle_items", [])}
        targets: list[dict[str, Any]] = []
        timestamp = now_iso()
        for item in selected:
            candidate_path = self.repository.resolve_inside(item["candidate_path"])
            candidate_text = candidate_path.read_text(encoding="utf-8")
            if sha256_bytes(candidate_text.encode("utf-8")) != item["candidate_sha256"]:
                raise ValidationError(f"bundle candidate hash 不匹配: {item['item_id']}")
            candidate, candidate_body = read_document(candidate_path)
            self.repository._validate_metadata(candidate, candidate_path)
            for relation in candidate.get("relations", []):
                target_id = str(relation.get("target_id", ""))
                if target_id in bundle_targets and target_id not in selected_targets:
                    try:
                        self.repository.find_document(target_id)
                    except NotFoundError as exc:
                        raise ValidationError(
                            f"bundle item {item['item_id']} 依赖未选择的 item target: {target_id}"
                        ) from exc
            if candidate.get("type") == "claim":
                if candidate.get("atomicity_status") == "compound":
                    raise ValidationError(f"compound claim 必须先拆分: {item['item_id']}")
                if candidate.get("evidence_coverage") in {"partial", "missing"}:
                    raise ValidationError(f"claim evidence coverage 不完整: {item['item_id']}")
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
        selected["atomicity_status"] = candidate.get("atomicity_status")
        selected["evidence_coverage"] = candidate.get("evidence_coverage")
        if candidate.get("type") == "claim" and (
            candidate.get("atomicity_status") == "compound"
            or candidate.get("evidence_coverage") in {"partial", "missing"}
        ):
            selected["review_tier"] = "low"
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

    def split_item(
        self, proposal_id: str, item_id: str, candidate_files: list[Path | str], reason: str,
    ) -> dict[str, Any]:
        """Replace one pending compound claim with independently reviewable atomic children."""
        proposal_path, proposal, body = self._load(proposal_id)
        selected = self._selected(proposal, [item_id])[0]
        if selected.get("object_type") != "claim" or selected.get("atomicity_status") != "compound":
            raise ValidationError("只能拆分 pending compound claim")
        if len(candidate_files) < 2 or not reason.strip():
            raise ValidationError("claim split 至少需要两个 candidate 文件和 reason")
        original_path = self.repository.resolve_inside(str(selected["candidate_path"]))
        original, _ = read_document(original_path)
        existing_targets = {str(item["target_id"]) for item in proposal.get("bundle_items", [])}
        timestamp = now_iso()
        children: list[dict[str, Any]] = []
        for index, candidate_file in enumerate(candidate_files, start=1):
            input_path = Path(candidate_file).expanduser().resolve()
            if not input_path.is_file():
                raise ValidationError(f"split candidate 不存在: {input_path}")
            candidate_text = input_path.read_text(encoding="utf-8")
            candidate, _ = read_document(input_path)
            self.repository._validate_metadata(candidate, input_path)
            if candidate.get("type") != "claim" or candidate.get("status") != "proposal":
                raise ValidationError("split candidate 必须是 proposal claim")
            if candidate.get("atomicity_status") != "atomic":
                raise ValidationError("split child 必须标记为 atomic")
            if candidate.get("split_from") != original.get("id"):
                raise ValidationError("split child 必须记录原 claim ID")
            if not set(candidate.get("source_ids", [])) <= set(original.get("source_ids", [])):
                raise ValidationError("split child 不得引入原 claim 之外的 source")
            target_id = str(candidate["id"])
            if target_id in existing_targets or any(child["target_id"] == target_id for child in children):
                raise ValidationError(f"split child target 重复: {target_id}")
            digest = sha256_bytes(candidate_text.encode("utf-8"))
            child_item_id = f"{item_id}.split-{index}"
            stored = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}-{child_item_id}-{digest[:12]}.md"
            self.repository.immutable_write(stored, candidate_text.encode("utf-8"))
            target = self.repository.root / CANONICAL_DIRECTORIES["claim"] / f"{target_id}-{slugify(str(candidate['title']))}.md"
            children.append({
                "item_id": child_item_id, "object_type": "claim", "action": "create",
                "target_id": target_id, "target_path": self.repository.rel(target),
                "base_path": None, "base_sha256": None,
                "candidate_path": self.repository.rel(stored), "candidate_sha256": digest,
                "decision": "pending", "potential_conflicts": [], "review_tier": "low",
                "atomicity_status": "atomic", "evidence_coverage": candidate.get("evidence_coverage"),
                "split_from_item_id": item_id, "split_reason": reason.strip(),
            })
        selected["decision"] = "superseded"
        selected["reviewed_at"] = timestamp
        selected["review_reason"] = reason.strip()
        selected["split_into"] = [child["item_id"] for child in children]
        proposal["bundle_items"].extend(children)
        proposal["updated_at"] = timestamp
        metrics = proposal.get("bundle_metrics", {})
        metrics["new_object_count"] = sum(
            item.get("decision") == "pending" and item.get("action") == "create"
            for item in proposal["bundle_items"]
        )
        metrics["review_cost_estimate"] = sum(item.get("decision") == "pending" for item in proposal["bundle_items"])
        node_counts = metrics.get("node_counts", {})
        node_counts["claim"] = sum(
            item.get("decision") == "pending" and item.get("object_type") == "claim"
            for item in proposal["bundle_items"]
        )
        body = body.rstrip() + (
            f"\n\n## Item split: {item_id}\n\n- Reason: {reason.strip()}\n"
            f"- Children: {', '.join(child['item_id'] for child in children)}\n"
        )
        atomic_write_text(proposal_path, render_document(proposal, body))
        self.repository.append_event("proposal-events", {
            "event": "bundle-item-split", "proposal_id": proposal_id, "item_id": item_id,
            "child_item_ids": [child["item_id"] for child in children], "reason": reason.strip(),
        })
        return {"proposal_id": proposal_id, "superseded_item": item_id,
                "child_items": [child["item_id"] for child in children]}

    def verify_item_quote(
        self, proposal_id: str, item_id: str, source_id: str, extraction_id: str,
        span_start: int, original_text: str, section: str, reason: str,
    ) -> dict[str, Any]:
        """Attach a byte-checked primary quote to a pending atomic claim revision."""
        proposal_path, proposal, body = self._load(proposal_id)
        selected = self._selected(proposal, [item_id])[0]
        candidate_path = self.repository.resolve_inside(str(selected["candidate_path"]))
        candidate, candidate_body = read_document(candidate_path)
        if candidate.get("type") != "claim" or candidate.get("atomicity_status") != "atomic":
            raise ValidationError("primary quote verification 只适用于 atomic claim")
        _, source, _ = self.repository.find_document(source_id)
        _, extraction, extraction_text = ExtractionService(self.repository).find(extraction_id)
        if extraction.get("source_id") != source_id:
            raise ValidationError("extraction 与 primary source 不匹配")
        if span_start < 0:
            if extraction_text.count(original_text) != 1:
                raise ValidationError("primary quote 无法唯一定位，必须提供 span_start")
            span_start = extraction_text.index(original_text)
        span_end = span_start + len(original_text)
        if extraction_text[span_start:span_end] != original_text:
            raise ValidationError("primary quote 与 extraction span 不逐字匹配")
        timestamp = now_iso()
        evidence_id = "ev_primary_" + hashlib.sha256(
            f"{source_id}\n{extraction_id}\n{span_start}\n{original_text}".encode()
        ).hexdigest()[:12]
        evidence = list(candidate.get("evidence", []))
        verified_evidence = {
            "evidence_id": evidence_id, "evidence_kind": "quote", "source_id": source_id,
            "content_id": source.get("content_id"), "extraction_id": extraction_id,
            "input_sha256": extraction.get("input_sha256"), "span_start": span_start,
            "span_end": span_end, "original_text": original_text, "section": section,
            "stance": "supports", "verification_status": "verified", "reason": reason.strip(),
        }
        existing_evidence = next((
            index for index, item in enumerate(evidence) if item.get("evidence_id") == evidence_id
        ), None)
        if existing_evidence is None:
            evidence.append(verified_evidence)
        else:
            evidence[existing_evidence] = verified_evidence
        candidate["evidence"] = evidence
        candidate["source_ids"] = list(dict.fromkeys([*candidate.get("source_ids", []), source_id]))
        relations = list(candidate.get("relations", []))
        existing_relation = next((
            relation for relation in relations
            if relation.get("type") == "derived_from" and relation.get("target_id") == source_id
        ), None)
        if existing_relation is None:
            relations.append({
                "type": "derived_from", "target_id": source_id, "reason": reason.strip(),
                "confidence": "high", "created_by": "primary-quote-verification-v1", "status": "proposal",
            })
        candidate["relations"] = relations
        candidate["evidence_coverage"] = "full"
        candidate["evidence_entailment"] = "full"
        candidate["epistemic_source_authority"] = "primary"
        candidate["claim_confidence"] = "high"
        candidate["publication_gate"] = "needs_review"
        candidate["uncertainty"] = "已逐字回验 primary PDF；仍需用户审批后才能进入 canonical。"
        candidate["updated_at"] = timestamp
        candidate_text = render_document(candidate, candidate_body)
        digest = sha256_bytes(candidate_text.encode("utf-8"))
        revision_path = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}-{item_id}-primary-{digest[:12]}.md"
        self.repository.immutable_write(revision_path, candidate_text.encode("utf-8"))
        selected.setdefault("revision_history", []).append({
            "candidate_path": selected["candidate_path"], "candidate_sha256": selected["candidate_sha256"],
            "reason": reason.strip(), "revised_at": timestamp,
        })
        selected["candidate_path"] = self.repository.rel(revision_path)
        selected["candidate_sha256"] = digest
        selected["evidence_coverage"] = "full"
        selected["review_reason"] = reason.strip()
        proposal["updated_at"] = timestamp
        body = body.rstrip() + (
            f"\n\n## Primary quote verification: {item_id}\n\n"
            f"- Source: `{source_id}`\n- Extraction: `{extraction_id}`\n"
            f"- Span: `{span_start}:{span_end}`\n- Reason: {reason.strip()}\n"
        )
        atomic_write_text(proposal_path, render_document(proposal, body))
        self.repository.append_event("proposal-events", {
            "event": "bundle-item-primary-quote-verified", "proposal_id": proposal_id,
            "item_id": item_id, "source_id": source_id, "extraction_id": extraction_id,
            "evidence_id": evidence_id,
        })
        return {"proposal_id": proposal_id, "item_id": item_id,
                "candidate_path": self.repository.rel(revision_path), "evidence_id": evidence_id}

    def mark_item_compound(self, proposal_id: str, item_id: str, reason: str) -> dict[str, Any]:
        """Correct a pending claim's atomicity without erasing its previous candidate."""
        proposal_path, proposal, body = self._load(proposal_id)
        selected = self._selected(proposal, [item_id])[0]
        candidate_path = self.repository.resolve_inside(str(selected["candidate_path"]))
        candidate, candidate_body = read_document(candidate_path)
        if candidate.get("type") != "claim" or not reason.strip():
            raise ValidationError("mark-compound 需要 pending claim 和 reason")
        timestamp = now_iso()
        candidate["atomicity_status"] = "compound"
        candidate["publication_gate"] = "needs_split"
        candidate["updated_at"] = timestamp
        candidate_text = render_document(candidate, candidate_body)
        digest = sha256_bytes(candidate_text.encode("utf-8"))
        revision_path = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}-{item_id}-compound-{digest[:12]}.md"
        self.repository.immutable_write(revision_path, candidate_text.encode("utf-8"))
        selected.setdefault("revision_history", []).append({
            "candidate_path": selected["candidate_path"], "candidate_sha256": selected["candidate_sha256"],
            "reason": reason.strip(), "revised_at": timestamp,
        })
        selected["candidate_path"] = self.repository.rel(revision_path)
        selected["candidate_sha256"] = digest
        selected["atomicity_status"] = "compound"
        selected["review_tier"] = "low"
        selected["review_reason"] = reason.strip()
        proposal["updated_at"] = timestamp
        body = body.rstrip() + f"\n\n## Atomicity correction: {item_id}\n\n- Reason: {reason.strip()}\n"
        atomic_write_text(proposal_path, render_document(proposal, body))
        self.repository.append_event("proposal-events", {
            "event": "bundle-item-marked-compound", "proposal_id": proposal_id,
            "item_id": item_id, "reason": reason.strip(),
        })
        return {"proposal_id": proposal_id, "item_id": item_id,
                "candidate_path": self.repository.rel(revision_path), "atomicity_status": "compound"}
