from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from .backups import RawBackupService
from .capture import CaptureService
from .context import ContextPackService
from .errors import GlobalMemoryError
from .markdown import read_document
from .proposals import ProposalService
from .recovery import ApprovalRecoveryManager
from .repository import Repository, sha256_bytes


PROPOSAL_STATUSES = {"pending", "deferred", "superseded", "published", "approved", "rejected"}
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def _repository(args: argparse.Namespace) -> Repository:
    root = Path(args.root or os.environ.get("GM_ROOT") or Path.cwd())
    return Repository(root)


def _print(value: object) -> None:
    if isinstance(value, str):
        print(value)
    else:
        print(json.dumps(value, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gm", description="Global Memory local-first CLI")
    parser.add_argument("--root", help="仓库根目录；默认当前目录或 GM_ROOT")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("init", help="初始化目录并建立派生索引")
    capture = commands.add_parser("capture", help="捕获 URL 或本地文件")
    capture.add_argument("target")
    capture.add_argument("--comment", default="")
    capture.add_argument(
        "--refresh", action="store_true",
        help="显式重新抓取 URL；变化时追加 source version 并生成 review proposal",
    )
    capture_text = commands.add_parser("capture-text", help="捕获粘贴文本；默认从 stdin 读取")
    capture_text.add_argument("--text")
    capture_text.add_argument("--title", default="人工输入")
    capture_text.add_argument("--comment", default="")
    commands.add_parser("inbox", help="列出尚未 compile 的来源")
    compile_parser = commands.add_parser("compile", help="为来源生成 proposal")
    compile_parser.add_argument("source_id")
    synthesize = commands.add_parser("synthesize", help="从多个 canonical claim 生成待审综合 proposal")
    synthesize.add_argument("claim_ids", nargs="+")
    discover = commands.add_parser("discover", help="为 canonical claim 生成可解释的关联候选 proposal")
    discover.add_argument("seed_id")
    update_parser = commands.add_parser(
        "propose-update", help="从 UTF-8 Markdown candidate 创建 canonical update proposal"
    )
    update_parser.add_argument("target_id")
    update_parser.add_argument("--from-file", dest="candidate_file", required=True)
    update_parser.add_argument("--reason", required=True)
    model_propose = commands.add_parser(
        "model-propose", help="导入外部模型 candidate；命令本身不调用任何 provider"
    )
    model_propose.add_argument("source_id")
    model_propose.add_argument("--candidate", dest="candidate_file", required=True)
    model_propose.add_argument("--provider", required=True)
    model_propose.add_argument("--model", required=True)
    model_propose.add_argument("--prompt-version", required=True)
    model_propose.add_argument("--prompt-file")
    model_propose.add_argument("--uncertainty", required=True)
    model_propose.add_argument("--reason", required=True)
    proposals = commands.add_parser("proposals", help="列出 proposals")
    proposals.add_argument(
        "--status", choices=["pending", "deferred", "superseded", "published", "approved", "rejected"]
    )

    proposal = commands.add_parser("proposal", help="审阅 proposal")
    proposal_commands = proposal.add_subparsers(dest="proposal_command", required=True)
    proposal_show = proposal_commands.add_parser("show")
    proposal_show.add_argument("proposal_id")
    proposal_approve = proposal_commands.add_parser("approve")
    proposal_approve.add_argument("proposal_id")
    proposal_publish = proposal_commands.add_parser(
        "publish", help="经自动门禁发布为可检索但未人工确认的 provisional knowledge"
    )
    proposal_publish.add_argument("proposal_id")
    proposal_reject = proposal_commands.add_parser("reject")
    proposal_reject.add_argument("proposal_id")
    proposal_reject.add_argument("--reason", default="")
    proposal_defer = proposal_commands.add_parser("defer")
    proposal_defer.add_argument("proposal_id")
    proposal_defer.add_argument("--reason", default="")
    proposal_revise = proposal_commands.add_parser("revise")
    proposal_revise.add_argument("proposal_id")
    proposal_revise.add_argument("--from-file", dest="candidate_file", required=True)
    proposal_revise.add_argument("--reason", required=True)

    promote = commands.add_parser("promote", help="将 provisional canonical knowledge 显式晋升为 confirmed")
    promote.add_argument("target_id")
    promote.add_argument("--reason", default="")

    search = commands.add_parser("search", help="全文检索来源和 canonical knowledge")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20)
    context = commands.add_parser("context", help="按 query 和 token budget 生成只读 Context Pack")
    context.add_argument("query")
    context.add_argument("--token-budget", type=int, default=1200)
    show = commands.add_parser("show", help="按稳定 ID 显示对象")
    show.add_argument("object_id")
    related = commands.add_parser("related", help="显示 typed relations")
    related.add_argument("object_id")
    commands.add_parser("status", help="显示仓库统计")
    commands.add_parser("rebuild-index", help="从 Markdown 与 raw source 重建 SQLite 索引")
    commands.add_parser("doctor", help="检查 schema、原始内容哈希和索引")
    commands.add_parser("lint", help="只读检查链接、来源、raw 与 proposal 完整性")
    backup = commands.add_parser("backup", help="生成、校验或增量复制 vault/raw 备份")
    backup_commands = backup.add_subparsers(dest="backup_command", required=True)
    backup_manifest = backup_commands.add_parser("manifest")
    backup_manifest.add_argument("--output")
    backup_create = backup_commands.add_parser("create")
    backup_create.add_argument("directory")
    backup_verify = backup_commands.add_parser("verify")
    backup_verify.add_argument("directory")
    backup_restore = backup_commands.add_parser("restore")
    backup_restore.add_argument("directory")
    backup_restore.add_argument("--apply", action="store_true")
    audit = commands.add_parser("audit", help="只读生成知识治理审计报告")
    audit_commands = audit.add_subparsers(dest="audit_command", required=True)
    audit_commands.add_parser("contradictions", help="报告 evidence 与 relation 中的显式冲突")
    commands.add_parser("recover", help="幂等续做未完成的 canonical approval journal")
    return parser


def doctor(repository: Repository) -> dict[str, object]:
    issues: list[str] = []
    sources: dict[str, dict[str, object]] = {}
    document_count = 0
    source_count = 0
    for path in repository.all_indexed_documents():
        document_count += 1
        try:
            metadata, _ = read_document(path)
            repository._validate_metadata(metadata, path)
            if metadata.get("type") == "source":
                source_count += 1
                sources[metadata["id"]] = metadata
                raw = repository.resolve_inside(metadata["raw_content_path"])
                if not raw.exists():
                    issues.append(f"缺少 raw 内容: {metadata['id']} -> {metadata['raw_content_path']}")
                elif sha256_bytes(raw.read_bytes()) != metadata["content_sha256"]:
                    issues.append(f"raw 内容哈希不匹配: {metadata['id']}")
        except Exception as exc:  # doctor must continue and report all local defects
            issues.append(f"{repository.rel(path)}: {exc}")
    families: dict[str, list[dict[str, object]]] = {}
    for source in sources.values():
        families.setdefault(str(source.get("canonical_locator", source["id"])), []).append(source)
    for canonical_locator, versions in families.items():
        seen_versions: set[int] = set()
        for source in versions:
            version_number = int(source.get("version_number", 1))
            if version_number in seen_versions:
                issues.append(f"来源版本号重复: {canonical_locator} v{version_number}")
            seen_versions.add(version_number)
            previous_id = source.get("previous_version_id")
            if version_number > 1:
                previous = sources.get(str(previous_id))
                if previous is None:
                    issues.append(f"来源版本缺少 previous: {source['id']} -> {previous_id}")
                elif int(previous.get("version_number", 1)) + 1 != version_number:
                    issues.append(f"来源版本链不连续: {previous_id} -> {source['id']}")
                elif previous.get("canonical_locator") != source.get("canonical_locator"):
                    issues.append(f"来源版本 locator 不一致: {previous_id} -> {source['id']}")
    try:
        indexed_count = sum(repository.count_by_type().values())
        if indexed_count != document_count:
            issues.append(f"索引对象数 {indexed_count} != 文件对象数 {document_count}")
    except Exception as exc:
        indexed_count = None
        issues.append(f"索引不可用: {exc}")
    recovery_journals = ApprovalRecoveryManager(repository).pending()
    for journal in recovery_journals:
        issues.append(f"存在未完成 approval recovery journal: {repository.rel(journal)}")
    return {
        "ok": not issues,
        "documents": document_count,
        "sources": source_count,
        "indexed_documents": indexed_count,
        "pending_recovery_journals": len(recovery_journals),
        "issues": issues,
    }


def lint(repository: Repository) -> dict[str, object]:
    """Check truth-layer references without rebuilding or modifying the repository."""
    errors: list[str] = []
    warnings: list[str] = []
    records: list[tuple[Path, dict[str, object], str, str]] = []
    candidate_paths = sorted((repository.root / "vault" / "proposals").glob("candidate-*.md"))
    document_paths = list(repository.all_indexed_documents()) + list(repository.proposal_documents())
    for path in document_paths:
        try:
            metadata, body = read_document(path)
            repository._validate_metadata(metadata, path)
            records.append((path, metadata, body, "document"))
        except Exception as exc:
            errors.append(f"无法读取或校验对象 {repository.rel(path)}: {exc}")
    for path in candidate_paths:
        try:
            metadata, body = read_document(path)
            repository._validate_metadata(metadata, path)
            records.append((path, metadata, body, "candidate"))
        except Exception as exc:
            errors.append(f"无法读取或校验 candidate {repository.rel(path)}: {exc}")

    indexed = [(path, metadata, body) for path, metadata, body, role in records if role == "document"]
    sources = {str(metadata["id"]) for _, metadata, _ in indexed if metadata.get("type") == "source"}
    proposal_ids = {str(metadata["id"]) for _, metadata, _ in indexed if metadata.get("type") == "proposal"}
    object_ids = {str(metadata["id"]) for _, metadata, _ in indexed if metadata.get("type") != "proposal"}
    known_ids = sources | proposal_ids | object_ids
    relation_targets: dict[str, int] = {object_id: 0 for object_id in known_ids}
    referenced_candidates: set[Path] = set()
    referenced_bases: set[Path] = set()

    def check_source_ids(path: Path, metadata: dict[str, object]) -> None:
        source_ids = metadata.get("source_ids", [])
        if not isinstance(source_ids, list):
            errors.append(f"source_ids 不是列表: {repository.rel(path)}")
            return
        if metadata.get("type") == "claim" and not source_ids:
            errors.append(f"claim 缺少 source_ids: {repository.rel(path)}")
        for source_id in source_ids:
            if source_id not in sources:
                errors.append(f"无效 source_id: {repository.rel(path)} -> {source_id}")

    def check_wikilinks(path: Path, body: str) -> None:
        for match in WIKILINK_PATTERN.finditer(body):
            reference, object_id = match.groups()
            if object_id:
                if object_id not in known_ids:
                    errors.append(f"失效 wikilink ID: {repository.rel(path)} -> {object_id}")
                continue
            relative = reference.strip()
            candidate = repository.resolve_inside(relative)
            if not candidate.suffix:
                candidate = candidate.with_suffix(".md")
            if not candidate.exists():
                errors.append(f"失效 wikilink 路径: {repository.rel(path)} -> {reference}")

    for path, metadata, body, _ in records:
        check_source_ids(path, metadata)
        relations = metadata.get("relations", [])
        if isinstance(relations, list):
            for relation in relations:
                if not isinstance(relation, dict):
                    continue
                target_id = relation.get("target_id")
                if target_id not in known_ids:
                    errors.append(f"失效 relation: {repository.rel(path)} -> {target_id}")
                else:
                    relation_targets[str(target_id)] = relation_targets.get(str(target_id), 0) + 1
        check_wikilinks(path, body)

    for path, metadata, _ in indexed:
        if metadata.get("type") == "source":
            raw_path = metadata.get("raw_content_path")
            if not raw_path:
                errors.append(f"source 缺少 raw_content_path: {repository.rel(path)}")
                continue
            try:
                raw = repository.resolve_inside(str(raw_path))
                if not raw.exists():
                    errors.append(f"缺少 raw 内容: {repository.rel(path)} -> {raw_path}")
                elif sha256_bytes(raw.read_bytes()) != metadata.get("content_sha256"):
                    errors.append(f"raw 内容哈希不匹配: {repository.rel(path)}")
            except Exception as exc:
                errors.append(f"raw 路径无效: {repository.rel(path)}: {exc}")
        elif metadata.get("type") != "proposal":
            has_relations = bool(metadata.get("relations")) or relation_targets.get(str(metadata["id"]), 0) > 0
            if not metadata.get("source_ids") and not has_relations:
                warnings.append(f"孤立 canonical 页面: {repository.rel(path)}")

    for path, proposal, _, _ in records:
        if proposal.get("type") != "proposal":
            continue
        status = proposal.get("status")
        if status not in PROPOSAL_STATUSES:
            errors.append(f"proposal 状态非法: {repository.rel(path)} -> {status}")
        proposal_kind = proposal.get("proposal_kind")
        if proposal_kind == "source_refresh":
            for key in ("previous_source_id", "new_source_id"):
                if proposal.get(key) not in sources:
                    errors.append(f"source refresh 引用不存在: {repository.rel(path)} -> {key}")
            continue
        if proposal_kind == "model_candidate":
            model_run = proposal.get("model_run")
            if not isinstance(model_run, dict):
                errors.append(f"model proposal 缺少 model_run: {repository.rel(path)}")
            else:
                for key in ("provider", "model", "prompt_version", "input_source_id", "input_sha256", "uncertainty"):
                    if not model_run.get(key):
                        errors.append(f"model proposal 缺少 model_run.{key}: {repository.rel(path)}")
                input_source_id = model_run.get("input_source_id")
                if input_source_id not in sources:
                    errors.append(f"model proposal 输入来源不存在: {repository.rel(path)}")
                else:
                    source_path, source_metadata, _ = repository.find_document(str(input_source_id))
                    if model_run.get("input_sha256") != source_metadata.get("content_sha256"):
                        errors.append(f"model proposal 输入哈希不匹配: {repository.rel(path)}")
                    if input_source_id not in proposal.get("source_ids", []):
                        errors.append(f"model proposal 未保留输入 source_id: {repository.rel(path)}")
        if proposal_kind == "deterministic_synthesis":
            input_claims = proposal.get("input_claims")
            if not isinstance(input_claims, list) or len(input_claims) < 2:
                errors.append(f"synthesis proposal 缺少至少两个 input_claims: {repository.rel(path)}")
            else:
                for item in input_claims:
                    if not isinstance(item, dict) or not item.get("id") or not item.get("path") or not item.get("sha256"):
                        errors.append(f"synthesis proposal input_claims 条目无效: {repository.rel(path)}")
                        continue
                    try:
                        input_path = repository.resolve_inside(str(item["path"]))
                        if not input_path.is_file():
                            errors.append(f"synthesis 输入 claim 不存在: {repository.rel(path)} -> {item['id']}")
                            continue
                        input_metadata, _ = read_document(input_path)
                        if input_metadata.get("id") != item["id"] or input_metadata.get("type") != "claim":
                            errors.append(f"synthesis 输入 claim 身份无效: {repository.rel(path)} -> {item['id']}")
                        elif sha256_bytes(input_path.read_bytes()) != item["sha256"]:
                            errors.append(f"synthesis 输入 claim 哈希不匹配: {repository.rel(path)} -> {item['id']}")
                    except Exception as exc:
                        errors.append(f"synthesis 输入 claim 路径无效: {repository.rel(path)}: {exc}")
        if proposal_kind == "relation_discovery":
            discovery_inputs = proposal.get("discovery_inputs")
            discovery_candidates = proposal.get("discovery_candidates")
            if not isinstance(discovery_inputs, list) or len(discovery_inputs) < 2:
                errors.append(f"relation discovery 缺少 discovery_inputs: {repository.rel(path)}")
            if not isinstance(discovery_candidates, list) or not discovery_candidates:
                errors.append(f"relation discovery 缺少 discovery_candidates: {repository.rel(path)}")
            if isinstance(discovery_inputs, list):
                for item in discovery_inputs:
                    if not isinstance(item, dict) or not item.get("id") or not item.get("path") or not item.get("sha256"):
                        errors.append(f"relation discovery 输入条目无效: {repository.rel(path)}")
                        continue
                    try:
                        input_path = repository.resolve_inside(str(item["path"]))
                        if not input_path.is_file():
                            errors.append(f"relation discovery 输入 claim 不存在: {repository.rel(path)} -> {item['id']}")
                            continue
                        input_metadata, _ = read_document(input_path)
                        if input_metadata.get("id") != item["id"] or input_metadata.get("type") != "claim":
                            errors.append(f"relation discovery 输入 claim 身份无效: {repository.rel(path)} -> {item['id']}")
                        elif sha256_bytes(input_path.read_bytes()) != item["sha256"]:
                            errors.append(f"relation discovery 输入 claim 哈希不匹配: {repository.rel(path)} -> {item['id']}")
                    except Exception as exc:
                        errors.append(f"relation discovery 输入 claim 路径无效: {repository.rel(path)}: {exc}")
            continue
        for key in ("candidate_path", "candidate_sha256", "target_id", "target_path", "action"):
            if not proposal.get(key):
                errors.append(f"proposal 缺少 {key}: {repository.rel(path)}")
        candidate_path_value = proposal.get("candidate_path")
        if candidate_path_value:
            try:
                candidate_path = repository.resolve_inside(str(candidate_path_value))
                referenced_candidates.add(candidate_path)
                if not candidate_path.exists():
                    errors.append(f"proposal candidate 不存在: {repository.rel(path)} -> {candidate_path_value}")
                else:
                    candidate_bytes = candidate_path.read_bytes()
                    if sha256_bytes(candidate_bytes) != proposal.get("candidate_sha256"):
                        errors.append(f"proposal candidate 哈希不匹配: {repository.rel(path)}")
                    candidate, _ = read_document(candidate_path)
                    if candidate.get("id") != proposal.get("target_id"):
                        errors.append(f"proposal candidate ID 不匹配: {repository.rel(path)}")
                    if candidate.get("status") != "proposal":
                        errors.append(f"proposal candidate 状态非法: {repository.rel(path)}")
            except Exception as exc:
                errors.append(f"proposal candidate 无效: {repository.rel(path)}: {exc}")
        action = proposal.get("action")
        target_path_value = proposal.get("target_path")
        target_path: Path | None = None
        if target_path_value:
            try:
                target_path = repository.resolve_inside(str(target_path_value))
                if target_path.exists():
                    target, _ = read_document(target_path)
                    if target.get("id") != proposal.get("target_id"):
                        errors.append(f"proposal target ID 不匹配: {repository.rel(path)}")
                elif action == "update" or status == "approved":
                    archived_target = None
                    for archived_path in repository.archive_documents():
                        archived_metadata, _ = read_document(archived_path)
                        if archived_metadata.get("id") == proposal.get("target_id"):
                            archived_target = archived_path
                            break
                    if archived_target is None:
                        errors.append(f"proposal target 不存在: {repository.rel(path)} -> {target_path_value}")
            except Exception as exc:
                errors.append(f"proposal target 路径无效: {repository.rel(path)}: {exc}")
        if action == "update":
            for key in ("base_path", "base_sha256"):
                if not proposal.get(key):
                    errors.append(f"update proposal 缺少 {key}: {repository.rel(path)}")
            if proposal.get("base_path"):
                try:
                    base_path = repository.resolve_inside(str(proposal["base_path"]))
                    referenced_bases.add(base_path)
                    if not base_path.exists():
                        errors.append(f"proposal base 不存在: {repository.rel(path)}")
                    elif sha256_bytes(base_path.read_bytes()) != proposal.get("base_sha256"):
                        errors.append(f"proposal base 哈希不匹配: {repository.rel(path)}")
                except Exception as exc:
                    errors.append(f"proposal base 路径无效: {repository.rel(path)}: {exc}")
        revision_of = proposal.get("revision_of")
        if revision_of:
            if revision_of not in proposal_ids:
                errors.append(f"revision_of 不存在: {repository.rel(path)} -> {revision_of}")
            elif not any(
                relation.get("type") == "supersedes" and relation.get("target_id") == revision_of
                for relation in proposal.get("relations", []) if isinstance(relation, dict)
            ):
                errors.append(f"revision 缺少 supersedes relation: {repository.rel(path)}")
        superseded_by = proposal.get("superseded_by")
        if superseded_by and superseded_by not in proposal_ids:
            errors.append(f"superseded_by 不存在: {repository.rel(path)} -> {superseded_by}")

    proposal_directory = repository.root / "vault" / "proposals"
    for path in candidate_paths:
        if path not in referenced_candidates:
            warnings.append(f"未被 proposal 引用的 candidate: {repository.rel(path)}")
    for path in proposal_directory.glob("base-*.md"):
        if path not in referenced_bases:
            warnings.append(f"未被 proposal 引用的 base snapshot: {repository.rel(path)}")
    return {
        "ok": not errors,
        "checked_documents": len(records),
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
    }


def contradiction_audit(repository: Repository) -> dict[str, object]:
    """Report explicit contradictions without inferring, ranking, or changing any claim."""
    claims: dict[str, tuple[Path, dict[str, object]]] = {}
    errors: list[str] = []
    for path in repository.canonical_documents():
        try:
            metadata, _ = read_document(path)
            repository._validate_metadata(metadata, path)
            if metadata.get("type") == "claim":
                claims[str(metadata["id"])] = (path, metadata)
        except Exception as exc:
            errors.append(f"无法读取 claim {repository.rel(path)}: {exc}")

    evidence_conflicts: list[dict[str, object]] = []
    relation_contradictions: list[dict[str, object]] = []
    for claim_id, (path, metadata) in sorted(claims.items()):
        evidence = metadata.get("evidence", [])
        supports = [item for item in evidence if item.get("stance") == "supports"]
        contradicts = [item for item in evidence if item.get("stance") == "contradicts"]
        if supports and contradicts:
            evidence_conflicts.append({
                "claim_id": claim_id,
                "path": repository.rel(path),
                "status": metadata.get("status"),
                "supports": supports,
                "contradicts": contradicts,
            })
        for relation in metadata.get("relations", []):
            if relation.get("type") == "contradicts" and relation.get("target_id") in claims:
                target_path, target = claims[str(relation["target_id"])]
                relation_contradictions.append({
                    "source_claim_id": claim_id,
                    "source_path": repository.rel(path),
                    "target_claim_id": relation["target_id"],
                    "target_path": repository.rel(target_path),
                    "source_status": metadata.get("status"),
                    "target_status": target.get("status"),
                    "reason": relation.get("reason"),
                })
    return {
        "ok": not errors,
        "claim_count": len(claims),
        "evidence_conflicts": evidence_conflicts,
        "relation_contradictions": relation_contradictions,
        "errors": errors,
        "note": "报告仅呈现显式冲突；不会裁决、降级置信度或修改 canonical claim。",
    }


def run(args: argparse.Namespace) -> int:
    repository = _repository(args)
    if args.command == "init":
        repository.init()
        _print({"root": str(repository.root), "index": repository.rel(repository.index_path), "status": "initialized"})
        return 0
    repository.ensure_initialized()
    captures = CaptureService(repository)
    proposals = ProposalService(repository)
    backups = RawBackupService(repository)
    if args.command == "capture":
        _print(captures.capture(args.target, args.comment, refresh=args.refresh).__dict__)
    elif args.command == "capture-text":
        text = args.text if args.text is not None else sys.stdin.read()
        _print(captures.capture_text(text, args.comment, args.title).__dict__)
    elif args.command == "inbox":
        _print(proposals.inbox())
    elif args.command == "compile":
        _print(proposals.compile(args.source_id).__dict__)
    elif args.command == "synthesize":
        _print(proposals.synthesize(args.claim_ids).__dict__)
    elif args.command == "discover":
        _print(proposals.discover(args.seed_id).__dict__)
    elif args.command == "propose-update":
        _print(
            proposals.propose_update(
                args.target_id, args.candidate_file, args.reason
            ).__dict__
        )
    elif args.command == "model-propose":
        _print(
            proposals.propose_model_candidate(
                args.source_id, args.candidate_file, args.provider, args.model,
                args.prompt_version, args.uncertainty, args.reason, args.prompt_file,
            ).__dict__
        )
    elif args.command == "proposals":
        _print(proposals.list(args.status))
    elif args.command == "proposal":
        if args.proposal_command == "show":
            _print(proposals.show(args.proposal_id))
        elif args.proposal_command == "approve":
            _print({"approved": args.proposal_id, "target_path": proposals.approve(args.proposal_id)})
        elif args.proposal_command == "publish":
            _print({"published": args.proposal_id, "target_path": proposals.publish(args.proposal_id)})
        elif args.proposal_command == "reject":
            _print({"rejected": args.proposal_id, "proposal_path": proposals.reject(args.proposal_id, args.reason)})
        elif args.proposal_command == "defer":
            _print({"deferred": args.proposal_id, "proposal_path": proposals.defer(args.proposal_id, args.reason)})
        else:
            _print(proposals.revise(args.proposal_id, args.candidate_file, args.reason).__dict__)
    elif args.command == "promote":
        _print({"confirmed": args.target_id, "target_path": proposals.promote(args.target_id, args.reason)})
    elif args.command == "search":
        _print([result.__dict__ for result in repository.search(args.query, args.limit)])
    elif args.command == "context":
        _print(ContextPackService(repository).build(args.query, args.token_budget).as_dict())
    elif args.command == "show":
        path, metadata, body = repository.find_document(args.object_id)
        _print({"path": repository.rel(path), "metadata": metadata, "body": body})
    elif args.command == "related":
        _print(repository.related(args.object_id))
    elif args.command == "status":
        _print({
            "root": str(repository.root), "objects_by_type": repository.count_by_type(),
            "inbox": len(proposals.inbox()), "proposals_by_status": {
                state: len(proposals.list(state))
                for state in ("pending", "deferred", "superseded", "approved", "rejected")
            },
            "pending_recovery_journals": len(ApprovalRecoveryManager(repository).pending()),
        })
    elif args.command == "rebuild-index":
        _print({"indexed_documents": repository.rebuild_index(), "index": repository.rel(repository.index_path)})
    elif args.command == "doctor":
        result = doctor(repository)
        _print(result)
        return 0 if result["ok"] else 1
    elif args.command == "lint":
        result = lint(repository)
        _print(result)
        return 0 if result["ok"] else 1
    elif args.command == "backup":
        if args.backup_command == "manifest":
            _print({"manifest_path": backups.write_manifest(args.output)})
        elif args.backup_command == "create":
            result = backups.backup(args.directory)
            _print(result.__dict__)
            return 0 if not result.conflicts else 1
        elif args.backup_command == "verify":
            result = backups.verify(args.directory)
            _print(result)
            return 0 if result["ok"] else 1
        else:
            result = backups.restore(args.directory, apply=args.apply)
            _print(result)
            return 0 if result["ok"] else 1
    elif args.command == "audit":
        if args.audit_command == "contradictions":
            result = contradiction_audit(repository)
            _print(result)
            return 0 if result["ok"] else 1
    elif args.command == "recover":
        result = ApprovalRecoveryManager(repository).recover_all()
        _print(result)
        return 1 if result["blocked"] else 0
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    try:
        return run(parser.parse_args(argv))
    except GlobalMemoryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("error: 已取消", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
