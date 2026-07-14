from __future__ import annotations

import difflib
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .recovery import ApprovalRecoveryManager, FailureHook
from .repository import Repository, now_iso, sha256_bytes, slugify


CANONICAL_STATUSES = {"confirmed", "contested", "superseded", "archived"}
REVIEWABLE_PROPOSAL_STATUSES = {"pending", "deferred"}
CANONICAL_DIRECTORIES = {
    "entity": "vault/knowledge/entities",
    "concept": "vault/knowledge/concepts",
    "claim": "vault/knowledge/claims",
    "synthesis": "vault/knowledge/syntheses",
    "intuition": "vault/frontier/intuitions",
    "question": "vault/frontier/questions",
    "tension": "vault/frontier/tensions",
    "analogy": "vault/frontier/analogies",
    "hypothesis": "vault/frontier/hypotheses",
    "project": "vault/action/projects",
    "decision": "vault/action/decisions",
    "experiment": "vault/action/experiments",
    "failure": "vault/action/failures",
    "opportunity": "vault/action/opportunities",
}


@dataclass(frozen=True)
class ProposalResult:
    proposal_id: str
    proposal_path: str
    candidate_path: str
    target_path: str
    action: str


@dataclass(frozen=True)
class RefreshProposalResult:
    proposal_id: str
    proposal_path: str
    previous_source_id: str
    new_source_id: str


class ProposalService:
    def __init__(
        self,
        repository: Repository,
        failure_hook: FailureHook | None = None,
    ):
        self.repository = repository
        self.failure_hook = failure_hook

    def _source(self, source_id: str) -> tuple[Path, dict[str, Any], str]:
        path, metadata, body = self.repository.find_document(source_id)
        if metadata.get("type") != "source":
            raise ValidationError(f"compile 只接受 source 对象: {source_id}")
        return path, metadata, body

    def _source_text(self, metadata: dict[str, Any]) -> str:
        raw_path = self.repository.resolve_inside(metadata["raw_content_path"])
        try:
            return raw_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return ""

    def _canonical_target(self, target_id: str) -> tuple[Path, dict[str, Any], str]:
        path, metadata, body = self.repository.find_document(target_id)
        relative = self.repository.rel(path)
        if not relative.startswith(("vault/knowledge/", "vault/frontier/", "vault/action/")):
            raise ValidationError(f"update 目标不是 canonical knowledge: {target_id}")
        return path, metadata, body

    def propose_update(
        self,
        target_id: str,
        candidate_file: Path | str,
        reason: str,
    ) -> ProposalResult:
        reason = reason.strip()
        if not reason:
            raise ValidationError("knowledge update 必须说明 reason")
        target_path, target, _ = self._canonical_target(target_id)
        input_path = Path(candidate_file).expanduser().resolve()
        if not input_path.is_file():
            raise ValidationError(f"candidate 文件不存在: {input_path}")
        try:
            candidate_text = input_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValidationError("candidate 必须是 UTF-8 Markdown") from exc
        candidate, _ = read_document(input_path)
        if candidate.get("id") != target_id or candidate.get("type") != target.get("type"):
            raise ValidationError("candidate 的 id/type 必须与 canonical target 一致")
        if candidate.get("status") != "proposal":
            raise ValidationError("candidate status 必须为 proposal")
        proposed_status = candidate.get("proposed_status", target.get("status", "confirmed"))
        if proposed_status not in CANONICAL_STATUSES:
            raise ValidationError(f"candidate proposed_status 非法: {proposed_status}")
        if candidate.get("created_at") != target.get("created_at"):
            raise ValidationError("candidate 必须保留 canonical created_at")
        if candidate.get("type") == "claim" and not candidate.get("source_ids"):
            raise ValidationError("claim update 必须保留至少一个 source_id")
        self.repository._validate_metadata(candidate, input_path)

        base_bytes = target_path.read_bytes()
        base_hash = sha256_bytes(base_bytes)
        candidate_hash = sha256_bytes(candidate_text.encode("utf-8"))
        proposal_digest = hashlib.sha256(
            f"knowledge-update\n{target_id}\n{base_hash}\n{candidate_hash}".encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_{proposal_digest[:24]}"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        candidate_path = self.repository.root / "vault" / "proposals" / f"candidate-{proposal_id}.md"
        base_path = self.repository.root / "vault" / "proposals" / f"base-{proposal_id}.md"
        if proposal_path.exists():
            existing, _ = read_document(proposal_path)
            return ProposalResult(
                proposal_id, self.repository.rel(proposal_path), existing["candidate_path"],
                existing["target_path"], existing["action"],
            )

        self.repository.immutable_write(base_path, base_bytes)
        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        diff = "".join(
            difflib.unified_diff(
                base_bytes.decode("utf-8").splitlines(keepends=True),
                candidate_text.splitlines(keepends=True),
                fromfile=f"base:{self.repository.rel(target_path)}",
                tofile=f"candidate:{self.repository.rel(target_path)}",
            )
        )
        timestamp = now_iso()
        proposal_metadata = {
            "id": proposal_id,
            "type": "proposal",
            "status": "pending",
            "title": f"更新 {target['title']}",
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": candidate.get("source_ids", []),
            "relations": [],
            "proposal_kind": "knowledge_update",
            "processor": "explicit-candidate-v1",
            "action": "update",
            "target_id": target_id,
            "target_path": self.repository.rel(target_path),
            "base_path": self.repository.rel(base_path),
            "base_sha256": base_hash,
            "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_hash,
            "change_reason": reason,
            "reviewed_at": None,
            "review_reason": None,
        }
        proposal_body = (
            f"# {proposal_metadata['title']}\n\n"
            "## 更新说明\n\n"
            f"- Target：`{target_id}`\n"
            f"- Base SHA-256：`{base_hash}`\n"
            f"- Candidate SHA-256：`{candidate_hash}`\n"
            f"- 变更理由：{reason}\n"
            "- 并发策略：审批时 target 必须仍等于 base；不自动合并。\n\n"
            "## Base → Candidate Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(
            proposal_path, render_document(proposal_metadata, proposal_body).encode("utf-8")
        )
        self.repository.append_event(
            "proposal-events",
            {
                "event": "knowledge-update-proposed", "proposal_id": proposal_id,
                "target_id": target_id, "base_sha256": base_hash,
                "candidate_sha256": candidate_hash, "reason": reason,
            },
        )
        return ProposalResult(
            proposal_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path),
            self.repository.rel(target_path), "update",
        )

    def propose_model_candidate(
        self,
        source_id: str,
        candidate_file: Path | str,
        provider: str,
        model: str,
        prompt_version: str,
        uncertainty: str,
        reason: str,
        prompt_file: Path | str | None = None,
    ) -> ProposalResult:
        provider, model = provider.strip(), model.strip()
        prompt_version, uncertainty, reason = prompt_version.strip(), uncertainty.strip(), reason.strip()
        if not all((provider, model, prompt_version, uncertainty, reason)):
            raise ValidationError(
                "model proposal 必须提供 provider、model、prompt_version、uncertainty 和 reason"
            )
        _, source, _ = self._source(source_id)
        input_path = Path(candidate_file).expanduser().resolve()
        if not input_path.is_file():
            raise ValidationError(f"candidate 文件不存在: {input_path}")
        try:
            candidate_text = input_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValidationError("candidate 必须是 UTF-8 Markdown") from exc
        candidate, _ = read_document(input_path)
        candidate_type = candidate.get("type")
        if candidate_type not in CANONICAL_DIRECTORIES:
            raise ValidationError(f"model candidate 不能写入该 canonical 类型: {candidate_type}")
        if candidate.get("status") != "proposal":
            raise ValidationError("model candidate status 必须为 proposal")
        if source_id not in candidate.get("source_ids", []):
            raise ValidationError("model candidate 必须在 source_ids 中保留输入 source")
        self.repository._validate_metadata(candidate, input_path)
        if candidate_type == "claim":
            missing_claim_fields = [
                field for field in ("evidence", "applicability", "uncertainty")
                if field not in candidate
            ]
            if missing_claim_fields:
                raise ValidationError(
                    "model claim candidate 缺少字段: " + ", ".join(missing_claim_fields)
                )

        target_id = str(candidate.get("id", ""))
        if not target_id:
            raise ValidationError("model candidate 缺少稳定 id")
        try:
            target_path, target, _ = self._canonical_target(target_id)
            action = "update"
            if candidate.get("type") != target.get("type"):
                raise ValidationError("model update candidate 的 type 必须与 canonical target 一致")
            if candidate.get("created_at") != target.get("created_at"):
                raise ValidationError("model update candidate 必须保留 canonical created_at")
            base_bytes = target_path.read_bytes()
            base_hash: str | None = sha256_bytes(base_bytes)
            proposed_status = candidate.get("proposed_status", target.get("status", "confirmed"))
        except NotFoundError:
            action = "create"
            target_path = (
                self.repository.root / CANONICAL_DIRECTORIES[str(candidate_type)]
                / f"{target_id}-{slugify(str(candidate.get('title', 'untitled')))}.md"
            )
            base_bytes = b""
            base_hash = None
            proposed_status = candidate.get("proposed_status", "confirmed")
        if proposed_status not in CANONICAL_STATUSES:
            raise ValidationError(f"model candidate proposed_status 非法: {proposed_status}")

        prompt_sha256: str | None = None
        if prompt_file is not None:
            prompt_path = Path(prompt_file).expanduser().resolve()
            if not prompt_path.is_file():
                raise ValidationError(f"prompt 文件不存在: {prompt_path}")
            prompt_sha256 = sha256_bytes(prompt_path.read_bytes())
        candidate_hash = sha256_bytes(candidate_text.encode("utf-8"))
        digest = hashlib.sha256(
            (
                f"model-candidate\n{source_id}\n{provider}\n{model}\n{prompt_version}\n"
                f"{prompt_sha256 or ''}\n{base_hash or ''}\n{candidate_hash}"
            ).encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_{digest[:24]}"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        candidate_path = self.repository.root / "vault" / "proposals" / f"candidate-{proposal_id}.md"
        base_path = self.repository.root / "vault" / "proposals" / f"base-{proposal_id}.md"
        if proposal_path.exists():
            existing, _ = read_document(proposal_path)
            return ProposalResult(
                proposal_id, self.repository.rel(proposal_path), existing["candidate_path"],
                existing["target_path"], existing["action"],
            )

        if action == "update":
            self.repository.immutable_write(base_path, base_bytes)
        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        before = base_bytes.decode("utf-8").splitlines(keepends=True) if base_bytes else []
        diff = "".join(
            difflib.unified_diff(
                before,
                candidate_text.splitlines(keepends=True),
                fromfile=f"base:{self.repository.rel(target_path)}" if before else "/dev/null",
                tofile=f"candidate:{self.repository.rel(target_path)}",
            )
        )
        timestamp = now_iso()
        metadata = {
            "id": proposal_id,
            "type": "proposal",
            "status": "pending",
            "title": f"模型提议：{candidate.get('title')}",
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": candidate.get("confidence", "unknown"),
            "source_ids": candidate.get("source_ids", []),
            "relations": [],
            "proposal_kind": "model_candidate",
            "processor": "external-model-candidate-v1",
            "action": action,
            "target_id": target_id,
            "target_path": self.repository.rel(target_path),
            "base_path": self.repository.rel(base_path) if action == "update" else None,
            "base_sha256": base_hash,
            "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_hash,
            "change_reason": reason,
            "model_run": {
                "provider": provider,
                "model": model,
                "prompt_version": prompt_version,
                "prompt_sha256": prompt_sha256,
                "input_source_id": source_id,
                "input_sha256": source.get("content_sha256"),
                "uncertainty": uncertainty,
            },
            "reviewed_at": None,
            "review_reason": None,
        }
        body = (
            f"# {metadata['title']}\n\n"
            "## 模型运行记录\n\n"
            f"- Provider：`{provider}`\n"
            f"- Model：`{model}`\n"
            f"- Prompt version：`{prompt_version}`\n"
            f"- Prompt SHA-256：`{prompt_sha256 or 'not-recorded'}`\n"
            f"- Input source：`{source_id}`\n"
            f"- Input SHA-256：`{source.get('content_sha256')}`\n"
            f"- 不确定性：{uncertainty}\n"
            f"- 提议理由：{reason}\n"
            "- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。\n\n"
            "## Base → Candidate Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(
            proposal_path, render_document(metadata, body).encode("utf-8")
        )
        self.repository.append_event(
            "proposal-events",
            {
                "event": "model-candidate-proposed", "proposal_id": proposal_id,
                "source_id": source_id, "provider": provider, "model": model,
                "prompt_version": prompt_version, "input_sha256": source.get("content_sha256"),
            },
        )
        return ProposalResult(
            proposal_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path),
            self.repository.rel(target_path), action,
        )

    def synthesize(self, claim_ids: list[str]) -> ProposalResult:
        ordered_ids = list(dict.fromkeys(claim_ids))
        if len(ordered_ids) < 2:
            raise ValidationError("synthesis 至少需要两个不同的 canonical claim")
        inputs: list[tuple[Path, dict[str, Any], str, str]] = []
        source_ids: list[str] = []
        for claim_id in ordered_ids:
            path, metadata, body = self._canonical_target(claim_id)
            if metadata.get("type") != "claim":
                raise ValidationError(f"synthesis 只接受 claim: {claim_id}")
            text = path.read_text(encoding="utf-8")
            inputs.append((path, metadata, body, sha256_bytes(text.encode("utf-8"))))
            for source_id in metadata.get("source_ids", []):
                if source_id not in source_ids:
                    source_ids.append(source_id)
        input_claims = [
            {
                "id": metadata["id"],
                "path": self.repository.rel(path),
                "sha256": digest,
                "status": metadata.get("status"),
            }
            for path, metadata, _, digest in inputs
        ]
        digest = hashlib.sha256(
            "\n".join(f"{item['id']}\n{item['sha256']}" for item in input_claims).encode("utf-8")
        ).hexdigest()
        target_id = f"synthesis_{digest[:24]}"
        title = f"待审综合：{len(inputs)} 个主张"
        target_path = (
            self.repository.root / CANONICAL_DIRECTORIES["synthesis"]
            / f"{target_id}-{slugify(title)}.md"
        )
        proposal_id = f"proposal_{digest[:24]}"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        candidate_path = self.repository.root / "vault" / "proposals" / f"candidate-{proposal_id}.md"
        if proposal_path.exists():
            existing, _ = read_document(proposal_path)
            return ProposalResult(
                proposal_id, self.repository.rel(proposal_path), existing["candidate_path"],
                existing["target_path"], existing["action"],
            )

        sections: list[str] = []
        for path, metadata, body, _ in inputs:
            sections.append(
                f"### [[{self.repository.rel(path)[:-3]}|{metadata['id']}]]\n\n"
                f"- 状态：`{metadata.get('status')}`\n"
                f"- 来源：{', '.join(f'`{source_id}`' for source_id in metadata.get('source_ids', [])) or 'none'}\n"
                f"- 适用条件：{'；'.join(metadata.get('applicability', [])) or '未结构化'}\n"
                f"- 不确定性：{metadata.get('uncertainty', '未结构化')}\n"
            )
            evidence = metadata.get("evidence", [])
            if evidence:
                sections.append("- 显式证据：\n")
                for item in evidence:
                    sections.append(
                        f"  - [{item['stance']}] `{item['source_id']}`，{item['location']}："
                        f"{item['excerpt']}（{item['reason']}）\n"
                    )
            contradictions = [
                relation for relation in metadata.get("relations", [])
                if relation.get("type") == "contradicts" and relation.get("target_id") in ordered_ids
            ]
            if contradictions:
                sections.append("- 显式冲突关系：\n")
                for relation in contradictions:
                    sections.append(
                        f"  - 与 `{relation['target_id']}`：{relation['reason']}\n"
                    )
            sections.append("\n")
        timestamp = now_iso()
        candidate_metadata = {
            "id": target_id,
            "type": "synthesis",
            "status": "proposal",
            "title": title,
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": source_ids,
            "relations": [
                {"type": "related_to", "target_id": item["id"], "reason": "本综合以该主张为输入"}
                for item in input_claims
            ],
            "input_claims": input_claims,
            "synthesis_method": "deterministic-explicit-evidence-v1",
            "uncertainty": "本综合只整理显式材料，不判断证据权重、不解决矛盾，也不产生新的事实结论。",
        }
        candidate_body = (
            f"# {title}\n\n"
            "## 综合边界\n\n"
            "本候选只汇总输入 claim 已显式记录的来源、证据方向、适用条件与冲突。"
            "它不自动裁决矛盾、不合并观点，也不把摘录升级为新事实。\n\n"
            "## 输入主张\n\n"
            + "".join(sections)
            + "## 待人工判断\n\n"
            "- 哪些证据在当前问题和适用范围内更相关？\n"
            "- 是否需要创建 contested、superseded 或新的 claim/update proposal？\n"
            "- 是否存在尚未捕获的反例、边界条件或原始材料？\n"
        )
        candidate_text = render_document(candidate_metadata, candidate_body)
        candidate_hash = sha256_bytes(candidate_text.encode("utf-8"))
        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        diff = "".join(
            difflib.unified_diff(
                [], candidate_text.splitlines(keepends=True),
                fromfile="/dev/null", tofile=self.repository.rel(target_path),
            )
        )
        proposal_metadata = {
            "id": proposal_id,
            "type": "proposal",
            "status": "pending",
            "title": title,
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": source_ids,
            "relations": [],
            "proposal_kind": "deterministic_synthesis",
            "processor": "deterministic-explicit-evidence-v1",
            "action": "create",
            "target_id": target_id,
            "target_path": self.repository.rel(target_path),
            "base_path": None,
            "base_sha256": None,
            "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_hash,
            "input_claims": input_claims,
            "reviewed_at": None,
            "review_reason": None,
        }
        proposal_body = (
            f"# {title}\n\n"
            "## 综合输入\n\n"
            + "".join(
                f"- `{item['id']}`：`{item['sha256']}`（状态：`{item['status']}`）\n"
                for item in input_claims
            )
            + "- 审批前会重新校验所有输入 claim 的哈希；任何变化都会阻止批准。\n\n"
            "## Content Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(
            proposal_path, render_document(proposal_metadata, proposal_body).encode("utf-8")
        )
        self.repository.append_event(
            "proposal-events",
            {"event": "synthesis-proposed", "proposal_id": proposal_id, "input_claim_ids": ordered_ids},
        )
        return ProposalResult(
            proposal_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path),
            self.repository.rel(target_path), "create",
        )

    def _validate_synthesis_inputs(self, proposal: dict[str, Any]) -> None:
        inputs = proposal.get("input_claims")
        if not isinstance(inputs, list) or len(inputs) < 2:
            raise ValidationError("synthesis proposal 缺少至少两个 input_claims")
        for item in inputs:
            if not isinstance(item, dict) or not item.get("id") or not item.get("path") or not item.get("sha256"):
                raise ValidationError("synthesis proposal input_claims 条目无效")
            path = self.repository.resolve_inside(str(item["path"]))
            if not path.is_file():
                raise ValidationError(f"synthesis 输入 claim 不存在: {item['id']}")
            metadata, _ = read_document(path)
            if metadata.get("id") != item["id"] or metadata.get("type") != "claim":
                raise ValidationError(f"synthesis 输入 claim 身份无效: {item['id']}")
            if sha256_bytes(path.read_bytes()) != item["sha256"]:
                raise ValidationError(
                    "synthesis 输入 claim 在 proposal 创建后已变化；请重新生成综合"
                )

    def create_source_refresh(
        self,
        previous_source_id: str,
        new_source_id: str,
    ) -> RefreshProposalResult:
        previous_path, previous, _ = self._source(previous_source_id)
        new_path, new, _ = self._source(new_source_id)
        if previous.get("canonical_locator") != new.get("canonical_locator"):
            raise ValidationError("source refresh 的 canonical_locator 不一致")
        if new.get("previous_version_id") != previous_source_id:
            raise ValidationError("source refresh 的 previous_version_id 链无效")

        proposal_digest = hashlib.sha256(
            f"source-refresh\n{previous_source_id}\n{new_source_id}".encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_{proposal_digest[:24]}"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        if proposal_path.exists():
            return RefreshProposalResult(
                proposal_id, self.repository.rel(proposal_path), previous_source_id, new_source_id
            )

        previous_text = self._source_text(previous)
        new_text = self._source_text(new)
        diff_truncated = len(previous_text) > 200_000 or len(new_text) > 200_000
        if previous_text or new_text:
            diff = "".join(
                difflib.unified_diff(
                    previous_text[:200_000].splitlines(keepends=True),
                    new_text[:200_000].splitlines(keepends=True),
                    fromfile=f"{previous_source_id}:{previous['content_sha256']}",
                    tofile=f"{new_source_id}:{new['content_sha256']}",
                )
            )
        else:
            diff = "（二进制或不可解码内容；仅比较 SHA-256。）"
        timestamp = now_iso()
        metadata = {
            "id": proposal_id,
            "type": "proposal",
            "status": "pending",
            "title": f"确认来源更新：{new['title']}",
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": [new_source_id],
            "relations": [],
            "proposal_kind": "source_refresh",
            "processor": "capture-refresh-v1",
            "action": "acknowledge_source_version",
            "target_id": new_source_id,
            "target_path": self.repository.rel(new_path),
            "previous_source_id": previous_source_id,
            "new_source_id": new_source_id,
            "source_family_id": new.get("source_family_id"),
            "previous_content_sha256": previous["content_sha256"],
            "new_content_sha256": new["content_sha256"],
            "diff_truncated": diff_truncated,
            "reviewed_at": None,
            "review_reason": None,
        }
        body = (
            f"# {metadata['title']}\n\n"
            "## 版本变化\n\n"
            f"- 上一版本：[[{self.repository.rel(previous_path)[:-3]}|{previous_source_id}]]\n"
            f"- 新版本：[[{self.repository.rel(new_path)[:-3]}|{new_source_id}]]\n"
            f"- Version：`{previous.get('version_number', 1)}` → `{new.get('version_number')}`\n"
            f"- 内容哈希：`{previous['content_sha256']}` → `{new['content_sha256']}`\n"
            "- 审批含义：确认这是一条需要进入后续知识处理的新来源版本；不直接修改 canonical knowledge。\n\n"
            "## 原始内容 Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(
            proposal_path, render_document(metadata, body).encode("utf-8")
        )
        self.repository.append_event(
            "proposal-events",
            {
                "event": "source-refresh-proposed", "proposal_id": proposal_id,
                "previous_source_id": previous_source_id, "new_source_id": new_source_id,
            },
        )
        return RefreshProposalResult(
            proposal_id, self.repository.rel(proposal_path), previous_source_id, new_source_id
        )

    def compile(self, source_id: str) -> ProposalResult:
        source_path, source, _ = self._source(source_id)
        raw_text = self._source_text(source)
        excerpt = " ".join(raw_text.split())[:500]
        if not excerpt:
            excerpt = "该来源为二进制内容，第一版规则编译器未提取正文。"
        title = f"来自《{source['title']}》的待确认主张"
        target_digest = hashlib.sha256(f"claim\n{source_id}".encode("utf-8")).hexdigest()
        target_id = f"claim_{target_digest[:24]}"
        target_path = self.repository.root / "vault" / "knowledge" / "claims" / f"{target_id}-{slugify(source['title'])}.md"
        action = "update" if target_path.exists() else "create"
        base_bytes = target_path.read_bytes() if target_path.exists() else b""
        base_hash = sha256_bytes(base_bytes) if base_bytes else None
        target_metadata = read_document(target_path)[0] if target_path.exists() else {}
        timestamp = now_iso()
        candidate_metadata = {
            "id": target_id,
            "type": "claim",
            "status": "proposal",
            "title": title,
            "created_at": target_metadata.get("created_at", timestamp),
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": [source_id],
            "evidence": [
                {
                    "source_id": source_id,
                    "location": "正文开头（第一版规则编译器截取）",
                    "excerpt": excerpt,
                    "stance": "context",
                    "reason": "确定性处理器只保留来源片段，不自动判断支持或反对。",
                }
            ],
            "applicability": [],
            "uncertainty": "该内容由确定性规则生成，尚未经过模型解释或人工事实核验。",
            "relations": [
                {"type": "derived_from", "target_id": source_id, "reason": "由该原始来源的规则编译结果提出"}
            ],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "由规则编译器提出，等待人工核验",
        }
        if action == "update":
            candidate_metadata["proposed_status"] = target_metadata.get("status", "confirmed")
        candidate_body = (
            f"# {title}\n\n"
            "## 候选主张\n\n"
            f"{excerpt}\n\n"
            "## 证据与位置\n\n"
            f"- 来源：[[{self.repository.rel(source_path)[:-3]}|{source_id}]]\n"
            "- 位置：正文开头（第一版规则编译器截取）\n"
            "- 证据方向：待人工判断支持或反对\n\n"
            "## 不确定性\n\n"
            "该内容由确定性规则生成，尚未经过模型解释或人工事实核验。批准仅表示纳入知识库，"
            "不自动将置信度提升为高。\n"
        )
        candidate_text = render_document(candidate_metadata, candidate_body)
        candidate_hash = sha256_bytes(candidate_text.encode("utf-8"))
        proposal_digest = hashlib.sha256(
            f"{source_id}\n{base_hash or ''}\n{candidate_hash}".encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_{proposal_digest[:24]}"
        candidate_path = self.repository.root / "vault" / "proposals" / f"candidate-{proposal_id}.md"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        base_path = self.repository.root / "vault" / "proposals" / f"base-{proposal_id}.md"

        if proposal_path.exists():
            existing, _ = read_document(proposal_path)
            return ProposalResult(
                proposal_id, self.repository.rel(proposal_path), existing["candidate_path"],
                existing["target_path"], existing["action"],
            )

        if action == "update":
            self.repository.immutable_write(base_path, base_bytes)
        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        before = base_bytes.decode("utf-8").splitlines(keepends=True) if base_bytes else []
        after = candidate_text.splitlines(keepends=True)
        diff = "".join(
            difflib.unified_diff(
                before, after,
                fromfile=self.repository.rel(target_path) if before else "/dev/null",
                tofile=self.repository.rel(target_path),
            )
        )
        proposal_metadata = {
            "id": proposal_id,
            "type": "proposal",
            "status": "pending",
            "title": f"编译 {source['title']}",
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": [source_id],
            "relations": [],
            "processor": "deterministic-excerpt-v1",
            "proposal_kind": "knowledge_compile",
            "action": action,
            "target_id": target_id,
            "target_path": self.repository.rel(target_path),
            "base_path": self.repository.rel(base_path) if action == "update" else None,
            "base_sha256": base_hash,
            "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_hash,
            "reviewed_at": None,
            "review_reason": None,
        }
        proposal_body = (
            f"# {proposal_metadata['title']}\n\n"
            "## 编译说明\n\n"
            f"- 读取来源：[[{self.repository.rel(source_path)[:-3]}|{source_id}]]\n"
            f"- 建议操作：`{action}` `{self.repository.rel(target_path)}`\n"
            "- 矛盾：第一版规则处理器未自动判定，必须人工复核\n"
            "- 原因：将来源开头转换为一个低置信度候选主张，验证审批闭环\n\n"
            "## 内容级 Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(proposal_path, render_document(proposal_metadata, proposal_body).encode("utf-8"))
        self.repository.append_event(
            "proposal-events",
            {"event": "compiled", "proposal_id": proposal_id, "source_ids": [source_id], "action": action},
        )
        return ProposalResult(
            proposal_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path),
            self.repository.rel(target_path), action,
        )

    def list(self, status: str | None = None) -> list[dict[str, Any]]:
        proposals: list[dict[str, Any]] = []
        for path in sorted(self.repository.proposal_documents()):
            metadata, _ = read_document(path)
            if status is None or metadata.get("status") == status:
                proposals.append({**metadata, "path": self.repository.rel(path)})
        return proposals

    def inbox(self) -> list[dict[str, str]]:
        compiled_sources = {
            source_id
            for proposal in self.list()
            if proposal.get("proposal_kind", "knowledge_compile") == "knowledge_compile"
            for source_id in proposal.get("source_ids", [])
        }
        result = []
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            if metadata["id"] not in compiled_sources:
                result.append({"id": metadata["id"], "title": metadata["title"], "path": self.repository.rel(path)})
        return sorted(result, key=lambda item: item["id"])

    def show(self, proposal_id: str) -> str:
        path, metadata, body = self.repository.find_document(proposal_id)
        if metadata.get("type") != "proposal":
            raise ValidationError(f"不是 proposal: {proposal_id}")
        if metadata.get("action") == "update" and metadata.get("base_sha256"):
            base_path = self.repository.resolve_inside(metadata["base_path"])
            candidate_path = self.repository.resolve_inside(metadata["candidate_path"])
            target_path = self.repository.resolve_inside(metadata["target_path"])
            base_bytes = base_path.read_bytes()
            candidate_bytes = candidate_path.read_bytes()
            if sha256_bytes(base_bytes) != metadata["base_sha256"]:
                raise ValidationError("proposal base snapshot 哈希不匹配")
            if sha256_bytes(candidate_bytes) != metadata["candidate_sha256"]:
                raise ValidationError("proposal candidate 哈希不匹配")
            current_bytes = target_path.read_bytes() if target_path.exists() else b""
            current_hash = sha256_bytes(current_bytes) if current_bytes else None
            if current_hash != metadata["base_sha256"]:
                base_to_current = "".join(
                    difflib.unified_diff(
                        base_bytes.decode("utf-8").splitlines(keepends=True),
                        current_bytes.decode("utf-8").splitlines(keepends=True),
                        fromfile=f"base:{metadata['target_path']}",
                        tofile=f"current:{metadata['target_path']}",
                    )
                )
                body = (
                    body.rstrip()
                    + "\n\n## 并发冲突：Base → Current Diff\n\n"
                    + f"- Base SHA-256：`{metadata['base_sha256']}`\n"
                    + f"- Current SHA-256：`{current_hash or 'missing'}`\n"
                    + "- 状态：target 已在 proposal 创建后变化；当前 proposal 不可批准。\n\n"
                    + f"```diff\n{base_to_current.rstrip()}\n```\n"
                )
        return render_document(metadata, body)

    def _load_proposal(self, proposal_id: str) -> tuple[Path, dict[str, Any], str]:
        path, metadata, body = self.repository.find_document(proposal_id)
        if metadata.get("type") != "proposal":
            raise ValidationError(f"不是 proposal: {proposal_id}")
        return path, metadata, body

    def defer(self, proposal_id: str, reason: str = "") -> str:
        proposal_path, proposal, proposal_body = self._load_proposal(proposal_id)
        if proposal.get("status") != "pending":
            raise ValidationError(f"proposal 状态不是 pending: {proposal.get('status')}")
        reviewed_at = now_iso()
        proposal["status"] = "deferred"
        proposal["updated_at"] = reviewed_at
        proposal["reviewed_at"] = reviewed_at
        proposal["review_reason"] = reason.strip() or "人工暂缓"
        atomic_write_text(proposal_path, render_document(proposal, proposal_body))
        self.repository.append_event(
            "proposal-events",
            {"event": "deferred", "proposal_id": proposal_id, "reason": reason.strip()},
        )
        return self.repository.rel(proposal_path)

    def revise(
        self,
        proposal_id: str,
        candidate_file: Path | str,
        reason: str,
    ) -> ProposalResult:
        reason = reason.strip()
        if not reason:
            raise ValidationError("proposal revision 必须说明 reason")
        old_path, old, old_body = self._load_proposal(proposal_id)
        if old.get("status") not in REVIEWABLE_PROPOSAL_STATUSES:
            raise ValidationError(f"proposal 状态不可修订: {old.get('status')}")
        if old.get("proposal_kind") == "source_refresh" or not old.get("candidate_path"):
            raise ValidationError("source refresh proposal 没有可修订 candidate")

        input_path = Path(candidate_file).expanduser().resolve()
        if not input_path.is_file():
            raise ValidationError(f"candidate 文件不存在: {input_path}")
        try:
            candidate_text = input_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValidationError("candidate 必须是 UTF-8 Markdown") from exc
        candidate, _ = read_document(input_path)
        old_candidate_path = self.repository.resolve_inside(old["candidate_path"])
        old_candidate, _ = read_document(old_candidate_path)
        if (
            candidate.get("id") != old.get("target_id")
            or candidate.get("type") != old_candidate.get("type")
        ):
            raise ValidationError("revision candidate 的 id/type 必须与原 proposal 一致")
        if candidate.get("status") != "proposal":
            raise ValidationError("revision candidate status 必须为 proposal")
        if candidate.get("type") == "claim" and not candidate.get("source_ids"):
            raise ValidationError("claim revision 必须保留至少一个 source_id")
        self.repository._validate_metadata(candidate, input_path)

        target_path = self.repository.resolve_inside(old["target_path"])
        action = old["action"]
        base_bytes = b""
        base_hash: str | None = None
        if action == "update":
            if not target_path.exists():
                raise ValidationError("revision 的 canonical target 已不存在")
            base_bytes = target_path.read_bytes()
            base_hash = sha256_bytes(base_bytes)
            current, _ = read_document(target_path)
            if candidate.get("created_at") != current.get("created_at"):
                raise ValidationError("revision candidate 必须保留 canonical created_at")
            proposed_status = candidate.get("proposed_status", current.get("status", "confirmed"))
        elif action == "create":
            if target_path.exists():
                raise ValidationError("revision 的 create target 已存在；请创建 update proposal")
            if candidate.get("created_at") != old_candidate.get("created_at"):
                raise ValidationError("revision candidate 必须保留原 candidate created_at")
            proposed_status = candidate.get("proposed_status", "confirmed")
        else:
            raise ValidationError(f"proposal action 不支持 candidate revision: {action}")
        if proposed_status not in CANONICAL_STATUSES:
            raise ValidationError(f"revision candidate proposed_status 非法: {proposed_status}")

        candidate_hash = sha256_bytes(candidate_text.encode("utf-8"))
        if candidate_hash == old.get("candidate_sha256"):
            raise ValidationError("revision candidate 与原 candidate 完全相同")
        digest = hashlib.sha256(
            f"proposal-revision\n{proposal_id}\n{base_hash or ''}\n{candidate_hash}".encode("utf-8")
        ).hexdigest()
        new_id = f"proposal_{digest[:24]}"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{new_id}.md"
        candidate_path = self.repository.root / "vault" / "proposals" / f"candidate-{new_id}.md"
        base_path = self.repository.root / "vault" / "proposals" / f"base-{new_id}.md"
        if action == "update":
            self.repository.immutable_write(base_path, base_bytes)
        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        before = base_bytes.decode("utf-8").splitlines(keepends=True) if base_bytes else []
        diff = "".join(
            difflib.unified_diff(
                before,
                candidate_text.splitlines(keepends=True),
                fromfile=f"base:{old['target_path']}" if before else "/dev/null",
                tofile=f"candidate:{old['target_path']}",
            )
        )
        timestamp = now_iso()
        metadata = {
            "id": new_id,
            "type": "proposal",
            "status": "pending",
            "title": f"修订：{old['title']}",
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": old.get("tags", []),
            "domains": old.get("domains", []),
            "confidence": old.get("confidence", "unknown"),
            "source_ids": candidate.get("source_ids", old.get("source_ids", [])),
            "relations": [
                {"type": "supersedes", "target_id": proposal_id, "reason": reason}
            ],
            "proposal_kind": "knowledge_revision",
            "processor": "human-candidate-revision-v1",
            "action": action,
            "target_id": old["target_id"],
            "target_path": old["target_path"],
            "base_path": self.repository.rel(base_path) if action == "update" else None,
            "base_sha256": base_hash,
            "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_hash,
            "change_reason": reason,
            "revision_of": proposal_id,
            "reviewed_at": None,
            "review_reason": None,
        }
        body = (
            f"# {metadata['title']}\n\n"
            "## 修订说明\n\n"
            f"- 被替代 proposal：`{proposal_id}`\n"
            f"- 修订理由：{reason}\n"
            f"- 建议操作：`{action}` `{old['target_path']}`\n"
            "- 原 candidate 保持不可变；本 proposal 使用新的 candidate。\n\n"
            "## Base → Revised Candidate Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(
            proposal_path, render_document(metadata, body).encode("utf-8")
        )

        old["status"] = "superseded"
        old["updated_at"] = timestamp
        old["reviewed_at"] = timestamp
        old["review_reason"] = reason
        old["superseded_by"] = new_id
        atomic_write_text(old_path, render_document(old, old_body))
        self.repository.append_event(
            "proposal-events",
            {
                "event": "revised", "proposal_id": new_id,
                "revision_of": proposal_id, "reason": reason,
            },
        )
        return ProposalResult(
            new_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path),
            old["target_path"], action,
        )

    def approve(self, proposal_id: str) -> str:
        proposal_path, proposal, proposal_body = self._load_proposal(proposal_id)
        if proposal.get("status") not in REVIEWABLE_PROPOSAL_STATUSES:
            raise ValidationError(f"proposal 状态不可批准: {proposal.get('status')}")
        if proposal.get("proposal_kind") == "source_refresh":
            target_path = self.repository.resolve_inside(proposal["target_path"])
            target, _ = read_document(target_path)
            _, previous, _ = self._source(proposal["previous_source_id"])
            target_raw_hash = sha256_bytes(
                self.repository.resolve_inside(target["raw_content_path"]).read_bytes()
            )
            previous_raw_hash = sha256_bytes(
                self.repository.resolve_inside(previous["raw_content_path"]).read_bytes()
            )
            if (
                target.get("id") != proposal.get("new_source_id")
                or target.get("previous_version_id") != previous.get("id")
                or target.get("content_sha256") != proposal.get("new_content_sha256")
                or previous.get("content_sha256") != proposal.get("previous_content_sha256")
                or target_raw_hash != target.get("content_sha256")
                or previous_raw_hash != previous.get("content_sha256")
            ):
                raise ValidationError("source refresh proposal 的目标版本无效")
            approved_at = now_iso()
            proposal["status"] = "approved"
            proposal["updated_at"] = approved_at
            proposal["reviewed_at"] = approved_at
            proposal["review_reason"] = "人工确认新的不可变来源版本"
            atomic_write_text(proposal_path, render_document(proposal, proposal_body))
            self.repository.append_event(
                "proposal-events",
                {
                    "event": "source-refresh-approved", "proposal_id": proposal_id,
                    "new_source_id": proposal["new_source_id"],
                },
            )
            return self.repository.rel(target_path)
        candidate_path = self.repository.resolve_inside(proposal["candidate_path"])
        candidate_text = candidate_path.read_text(encoding="utf-8")
        if sha256_bytes(candidate_text.encode("utf-8")) != proposal["candidate_sha256"]:
            raise ValidationError("candidate 内容哈希不匹配，拒绝批准")
        candidate, body = read_document(candidate_path)
        if candidate.get("status") != "proposal" or candidate.get("id") != proposal["target_id"]:
            raise ValidationError("candidate 身份或状态无效")
        if proposal.get("proposal_kind") == "deterministic_synthesis":
            self._validate_synthesis_inputs(proposal)
        target_path = self.repository.resolve_inside(proposal["target_path"])
        target_before_sha256: str | None = None
        if proposal["action"] == "create" and target_path.exists():
            raise ValidationError("目标已存在；请重新 compile 生成 update proposal")
        default_status = "confirmed"
        if proposal["action"] == "update":
            if not proposal.get("base_path") or not proposal.get("base_sha256"):
                raise ValidationError("update proposal 缺少不可变 base snapshot")
            base_path = self.repository.resolve_inside(proposal["base_path"])
            base_bytes = base_path.read_bytes()
            if sha256_bytes(base_bytes) != proposal["base_sha256"]:
                raise ValidationError("proposal base snapshot 哈希不匹配")
            if not target_path.exists():
                raise ValidationError("update target 已不存在；拒绝批准")
            current_hash = sha256_bytes(target_path.read_bytes())
            if current_hash != proposal["base_sha256"]:
                raise ValidationError(
                    "canonical target 在 proposal 创建后已变化；拒绝覆盖。"
                    "请运行 proposal show 查看三方 diff，并基于当前版本重新提案"
                )
            target_before_sha256 = current_hash
            base_metadata, _ = read_document(base_path)
            if candidate.get("created_at") != base_metadata.get("created_at"):
                raise ValidationError("update candidate 未保留 canonical created_at")
            default_status = base_metadata.get("status", "confirmed")
        self.repository._validate_metadata(candidate, candidate_path)
        approved_at = now_iso()
        canonical = dict(candidate)
        proposed_status = canonical.pop("proposed_status", default_status)
        if proposed_status not in CANONICAL_STATUSES:
            raise ValidationError(f"candidate proposed_status 非法: {proposed_status}")
        canonical["status"] = proposed_status
        canonical["updated_at"] = approved_at
        canonical["approved_via"] = proposal_id
        canonical["change_reason"] = proposal.get(
            "change_reason", f"人工批准 proposal {proposal_id}"
        )
        canonical_text = render_document(canonical, body)
        proposal["status"] = "approved"
        proposal["updated_at"] = approved_at
        proposal["reviewed_at"] = approved_at
        proposal["review_reason"] = "人工通过 CLI 明确批准"
        proposal_after_text = render_document(proposal, proposal_body)

        recovery = ApprovalRecoveryManager(self.repository)
        journal_path = recovery.prepare(
            proposal_id=proposal_id,
            target_id=proposal["target_id"],
            target_path=target_path,
            target_before_sha256=target_before_sha256,
            target_after_text=canonical_text,
            proposal_path=proposal_path,
            proposal_before_sha256=sha256_bytes(proposal_path.read_bytes()),
            proposal_after_text=proposal_after_text,
            audit_payload={
                "event": "approved", "proposal_id": proposal_id,
                "target_path": proposal["target_path"],
            },
        )
        if self.failure_hook is not None:
            self.failure_hook("prepared")
        recovery.recover_one(journal_path, self.failure_hook)
        return self.repository.rel(target_path)

    def reject(self, proposal_id: str, reason: str = "") -> str:
        proposal_path, proposal, proposal_body = self._load_proposal(proposal_id)
        if proposal.get("status") not in REVIEWABLE_PROPOSAL_STATUSES:
            raise ValidationError(f"proposal 状态不可拒绝: {proposal.get('status')}")
        reviewed_at = now_iso()
        proposal["status"] = "rejected"
        proposal["updated_at"] = reviewed_at
        proposal["reviewed_at"] = reviewed_at
        proposal["review_reason"] = reason or "人工拒绝"
        atomic_write_text(proposal_path, render_document(proposal, proposal_body))
        self.repository.append_event(
            "proposal-events", {"event": "rejected", "proposal_id": proposal_id, "reason": reason}
        )
        return self.repository.rel(proposal_path)
