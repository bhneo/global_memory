from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from .backups import RawBackupService
from .bundle import BundleCompiler, BundleRecoveryManager, BundleReviewService, JsonBundleProvider
from .capture import CaptureService
from .context import ContextPackService
from .consolidation import ConsolidationReceiptService, ConsolidationService, DriftAuditService, ProposalGateMigration
from .distillation import CorpusDistillationService
from .errors import GlobalMemoryError
from .extraction import ExtractionService
from .followups import FollowupService
from .lifecycle import SourceAnnotationService, SourceLifecycleService
from .maintenance import MaintenanceService
from .memory import ExceptionService, WorkingMemoryService
from .metrics import ProjectMetricsService
from .migration import EpistemicStatusMigration, TrustPolicyRequalificationMigration
from .evolution import KnowledgeEvolutionService
from .mcp_server import add_mcp_arguments, run_mcp
from .obsidian import ObsidianViewService
from .markdown import read_document
from .proposals import ProposalService
from .recovery import ApprovalRecoveryManager
from .raw_store import RawStoreService
from .quality import SourceQualityService
from .review import SourceBundleReviewService
from .runs import BatchArtifactMigrator, RunArtifactService
from .repository import Repository, sha256_bytes
from .receipts import ReceiptService
from .triage import DailyTriageService
from .works import WorkService
from .governance import PromotionService


PROPOSAL_STATUSES = {"pending", "deferred", "migrated", "superseded", "published", "approved", "rejected"}
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
    capture_wechat = commands.add_parser(
        "capture-wechat",
        help="捕获单篇微信公众号文章（移动端 UA + 元数据解析）",
    )
    capture_wechat.add_argument("url")
    capture_wechat.add_argument("--comment", default="")
    capture_wechat.add_argument(
        "--refresh", action="store_true",
        help="显式重新抓取；内容变化时追加 source version",
    )
    capture_text = commands.add_parser("capture-text", help="捕获粘贴文本；默认从 stdin 读取")
    capture_text.add_argument("--text")
    capture_text.add_argument("--title", default="人工输入")
    capture_text.add_argument("--comment", default="")
    commands.add_parser("inbox", help="列出 derived processing state 中待 compile 的来源")
    triage = commands.add_parser("triage", aliases=["daily"], help="低成本批量准备 inbox；默认不生成 proposal")
    triage.add_argument("source_ids", nargs="*")
    triage.add_argument("--limit", type=int, default=25)
    triage.add_argument("--compile-selected", action="store_true", help="仅对本次选中来源显式生成 pending proposal")
    triage.add_argument("--recheck", action="store_true", help="重新运行已有质量检查")
    source = commands.add_parser("source", help="查看 source 处理状态或补充用户注意力信号")
    source_commands = source.add_subparsers(dest="source_command", required=True)
    source_status = source_commands.add_parser("status")
    source_status.add_argument("source_id")
    source_history = source_commands.add_parser("history")
    source_history.add_argument("source_id")
    source_annotate = source_commands.add_parser("annotate")
    source_annotate.add_argument("source_id")
    source_annotate.add_argument("--why-saved")
    source_annotate.add_argument("--salience", choices=["low", "medium", "high", "unknown"])
    quality = commands.add_parser("quality", help="运行 source availability/content quality gate")
    quality.add_argument("source_id")
    extract = commands.add_parser("extract", help="从 immutable raw 创建可重建的 derived extraction")
    extract.add_argument("source_id")
    extract.add_argument("--rebuild", action="store_true")
    extractions = commands.add_parser("extractions", help="列出 derived extractions")
    extractions.add_argument("--source")
    work = commands.add_parser("work", help="审计式识别 logical document/work")
    work_commands = work.add_subparsers(dest="work_command", required=True)
    work_propose = work_commands.add_parser("propose")
    work_propose.add_argument("source_ids", nargs="+")
    work_propose.add_argument("--arxiv-id")
    work_propose.add_argument("--title")
    work_propose.add_argument("--author", action="append", default=[])
    compile_parser = commands.add_parser("compile", help="为来源生成 proposal")
    compile_parser.add_argument("source_id")
    compile_parser.add_argument("--bundle-file", help="外部 provider 生成的本地 JSON items；核心不调用模型")
    compile_parser.add_argument("--provider-name", default="external-json-bundle-v1")
    synthesize = commands.add_parser("synthesize", help="从多个 canonical claim 生成待审综合 proposal")
    synthesize.add_argument("claim_ids", nargs="+")
    discover = commands.add_parser("discover", help="兼容别名：related-content（词汇/metadata 关联候选）")
    discover.add_argument("seed_id")
    related_content = commands.add_parser("related-content", help="生成可解释的 related-content 候选；不声称真正 serendipity")
    related_content.add_argument("seed_id")
    distill = commands.add_parser("distill", help="对现有正式 proposals 做受控知识蒸馏")
    distill_commands = distill.add_subparsers(dest="distill_command", required=True)
    distill_corpus = distill_commands.add_parser("corpus")
    distill_corpus.add_argument("--dry-run", action="store_true")
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
        "--status", choices=["pending", "deferred", "migrated", "superseded", "published", "approved", "rejected"]
    )
    review = commands.add_parser("review", help="以 Source Bundle 为主要审阅单位")
    review_commands = review.add_subparsers(dest="review_command", required=True)
    review_commands.add_parser("queue")
    review_source = review_commands.add_parser("source")
    review_source.add_argument("source_id")
    review_bundle = review_commands.add_parser("bundle")
    review_bundle.add_argument("bundle_id")
    review_bundle.add_argument("--details", action="store_true")
    review_approve = review_commands.add_parser("approve")
    review_approve.add_argument("bundle_id")
    review_approve.add_argument("--high-confidence", action="store_true")
    review_approve.add_argument("--items")
    review_source_only = review_commands.add_parser("source-only")
    review_source_only.add_argument("bundle_id")
    review_source_only.add_argument("--reason", default="")
    review_defer = review_commands.add_parser("defer")
    review_defer.add_argument("bundle_id")
    review_defer.add_argument("--reason", default="")
    followups = commands.add_parser("followups", help="列出 primary-source 与 recovery follow-ups")
    followups.add_argument("--status")
    followup = commands.add_parser("followup", help="检测、查看或解决 follow-up")
    followup_commands = followup.add_subparsers(dest="followup_command", required=True)
    followup_detect = followup_commands.add_parser("detect")
    followup_detect.add_argument("source_id")
    followup_show = followup_commands.add_parser("show")
    followup_show.add_argument("followup_id")
    followup_normalize = followup_commands.add_parser("normalize-locators")
    followup_normalize.add_argument("--apply", action="store_true", help="写入迁移；默认仅 dry-run")
    followup_resolve = followup_commands.add_parser("resolve")
    followup_resolve.add_argument("followup_id")
    followup_resolve.add_argument("--captured-source")

    proposal = commands.add_parser("proposal", help="审阅 proposal")
    proposal_commands = proposal.add_subparsers(dest="proposal_command", required=True)
    proposal_show = proposal_commands.add_parser("show")
    proposal_show.add_argument("proposal_id")
    proposal_diff = proposal_commands.add_parser("diff")
    proposal_diff.add_argument("proposal_id")
    proposal_approve = proposal_commands.add_parser("approve")
    proposal_approve.add_argument("proposal_id")
    proposal_approve.add_argument("--items", help="逗号分隔的 compile bundle item IDs")
    proposal_publish = proposal_commands.add_parser(
        "publish", help="经自动门禁发布为可检索但未人工确认的 provisional knowledge"
    )
    proposal_publish.add_argument("proposal_id")
    proposal_reject = proposal_commands.add_parser("reject")
    proposal_reject.add_argument("proposal_id")
    proposal_reject.add_argument("--reason", default="")
    proposal_reject.add_argument("--items", help="逗号分隔的 compile bundle item IDs")
    proposal_defer = proposal_commands.add_parser("defer")
    proposal_defer.add_argument("proposal_id")
    proposal_defer.add_argument("--reason", default="")
    proposal_revise = proposal_commands.add_parser("revise")
    proposal_revise.add_argument("proposal_id")
    proposal_revise.add_argument("--from-file", dest="candidate_file", required=True)
    proposal_revise.add_argument("--reason", required=True)
    proposal_revise.add_argument("--item", help="要编辑的 compile bundle item ID")
    proposal_split = proposal_commands.add_parser("split-item")
    proposal_split.add_argument("proposal_id")
    proposal_split.add_argument("--item", required=True, help="要拆分的 compound item ID")
    proposal_split.add_argument("--from-files", required=True, help="逗号分隔的 atomic candidate 文件")
    proposal_split.add_argument("--reason", required=True)
    proposal_verify = proposal_commands.add_parser("verify-item-quote")
    proposal_verify.add_argument("proposal_id")
    proposal_verify.add_argument("--item", required=True)
    proposal_verify.add_argument("--source", required=True)
    proposal_verify.add_argument("--extraction", required=True)
    proposal_verify.add_argument("--span-start", type=int, required=True)
    proposal_verify.add_argument("--quote", required=True)
    proposal_verify.add_argument("--section", required=True)
    proposal_verify.add_argument("--reason", required=True)
    proposal_mark_compound = proposal_commands.add_parser("mark-compound")
    proposal_mark_compound.add_argument("proposal_id")
    proposal_mark_compound.add_argument("--item", required=True)
    proposal_mark_compound.add_argument("--reason", required=True)

    promote = commands.add_parser("promote", help="晋升 working/trusted memory；canonical 只创建 promotion card")
    promote.add_argument("target_id")
    promote.add_argument("--to", choices=["trusted", "canonical"], default="trusted")
    promote.add_argument("--reason", required=True)
    demote = commands.add_parser("demote", help="将 trusted memory 降回 working")
    demote.add_argument("target_id")
    demote.add_argument("--to", choices=["working"], default="working")
    demote.add_argument("--reason", required=True)
    trust = commands.add_parser("trust", help="解释 working/trusted 对象的信任依据")
    trust_commands = trust.add_subparsers(dest="trust_command", required=True)
    trust_explain = trust_commands.add_parser("explain")
    trust_explain.add_argument("target_id")
    history = commands.add_parser("history", help="显示对象的晋升历史")
    history.add_argument("target_id")
    rollback = commands.add_parser("rollback", help="回滚最近一次 trusted 晋升")
    rollback.add_argument("change_id")
    rollback.add_argument("--reason", required=True)

    exceptions = commands.add_parser("exceptions", help="列出例外队列")
    exceptions.add_argument("--status", action="append")
    exception = commands.add_parser("exception", help="查看或处理例外")
    exception_commands = exception.add_subparsers(dest="exception_command", required=True)
    exception_show = exception_commands.add_parser("show")
    exception_show.add_argument("exception_id")
    exception_resolve = exception_commands.add_parser("resolve")
    exception_resolve.add_argument("exception_id")
    exception_resolve.add_argument("--resolution", required=True)
    exception_resolve.add_argument("--action", choices=["resolved", "deferred", "dismissed"], default="resolved")

    promotions = commands.add_parser("promotions", help="列出 canonical promotion cards")
    promotions.add_argument("--status", action="append")
    promotion = commands.add_parser("promotion", help="查看或处理 canonical promotion card")
    promotion_commands = promotion.add_subparsers(dest="promotion_command", required=True)
    promotion_show = promotion_commands.add_parser("show")
    promotion_show.add_argument("promotion_id")
    promotion_approve = promotion_commands.add_parser("approve")
    promotion_approve.add_argument("promotion_id")
    promotion_approve.add_argument("--lock", action="store_true")
    for decision in ("reject", "defer"):
        decision_parser = promotion_commands.add_parser(decision)
        decision_parser.add_argument("promotion_id")
        decision_parser.add_argument("--reason", required=True)

    consolidate = commands.add_parser("consolidate", help="运行 daily 或 weekly memory consolidation")
    consolidate_commands = consolidate.add_subparsers(dest="consolidate_command", required=True)
    consolidate_daily = consolidate_commands.add_parser("daily")
    consolidate_daily.add_argument("--limit", type=int, default=25)
    consolidate_commands.add_parser("weekly")
    consolidate_object = consolidate_commands.add_parser("object")
    consolidate_object.add_argument("object_id")
    evolve = commands.add_parser("evolve")
    evolve.add_argument("object_id")
    evolve.add_argument("--change-type", choices=["support", "refine", "limit", "contradict", "supersede", "metadata_only"], required=True)
    evolve.add_argument("--from-file", required=True)
    evolve.add_argument("--reason", required=True)
    evolve.add_argument("--trigger-source")
    commands.add_parser("weekly-report", help="运行 weekly consolidation 并输出 digest")

    search = commands.add_parser("search", help="全文检索来源和 canonical knowledge")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20)
    search.add_argument("--types", help="逗号分隔 object types")
    search.add_argument("--statuses", help="逗号分隔 statuses")
    search.add_argument("--canonical-only", action="store_true")
    search.add_argument("--include-proposals", action="store_true")
    search.add_argument("--relation-depth", type=int, default=0)
    context = commands.add_parser("context", help="按 query 和 token budget 生成只读 Context Pack")
    context.add_argument("query", nargs="?")
    context.add_argument("--question")
    context.add_argument("--profile", default="research")
    context.add_argument("--project")
    context.add_argument("--domain")
    context.add_argument("--types")
    context.add_argument("--statuses")
    context.add_argument("--updated-since")
    context.add_argument("--source-kind")
    context.add_argument("--include-proposals", action="store_true")
    context.add_argument("--relation-depth", type=int, default=1)
    context.add_argument("--strict-execution", action="store_true", help="execution profile requires current Receipt v2")
    context.add_argument("--token-budget", type=int, default=1200)
    context.add_argument("--format", choices=["json", "markdown"], default="json")
    obsidian = commands.add_parser("obsidian", help="构建可重建的 Obsidian 导航视图")
    obsidian_commands = obsidian.add_subparsers(dest="obsidian_command", required=True)
    obsidian_commands.add_parser("build")
    receipt = commands.add_parser("receipt", help="创建 session receipt 并通过 proposal 写回")
    receipt_commands = receipt.add_subparsers(dest="receipt_command", required=True)
    receipt_create = receipt_commands.add_parser("create")
    receipt_create.add_argument("--agent", choices=["codex", "cursor", "claude"], required=True)
    receipt_create.add_argument("--project", required=True)
    receipt_create.add_argument("--task", required=True)
    receipt_create.add_argument("--from-file", required=True)
    receipt_propose = receipt_commands.add_parser("propose")
    receipt_propose.add_argument("receipt_id")
    maintain = commands.add_parser("maintain", help="汇总只读维护状态；可显式重建派生层")
    maintain.add_argument("--rebuild-derived", action="store_true")
    weekly = commands.add_parser("weekly", help="运行每周维护：daily triage、完整性、矛盾审计与派生视图")
    weekly.add_argument("--triage-limit", type=int, default=100)
    weekly.add_argument("--recheck", action="store_true", help="重新运行已有 source 质量检查")
    weekly.add_argument("--no-rebuild-derived", action="store_true", help="不重建 SQLite/Obsidian 派生视图")
    mcp = commands.add_parser("mcp", help="运行 provider-neutral 只读 MCP 服务")
    add_mcp_arguments(mcp)
    show = commands.add_parser("show", help="按稳定 ID 显示对象")
    show.add_argument("object_id")
    related = commands.add_parser("related", help="显示 typed relations")
    related.add_argument("object_id")
    status = commands.add_parser("status", help="显示仓库统计")
    status.add_argument("--machine-readable", action="store_true")
    metrics = commands.add_parser("metrics", help="generate current vault metrics")
    metrics.add_argument("--write-project-state", action="store_true")
    commands.add_parser("rebuild-index", help="从 Markdown 与 raw source 重建 SQLite 索引")
    doctor_parser = commands.add_parser("doctor", help="检查 schema、状态、批处理、关系和索引")
    doctor_parser.add_argument("--check-state", action="store_true")
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
    raw = commands.add_parser("raw", help="校验全局 content-addressed raw object store")
    raw_commands = raw.add_subparsers(dest="raw_command", required=True)
    raw_commands.add_parser("verify", help="校验 source、content_id、object path 与磁盘哈希")
    migrate = commands.add_parser("migrate", help="执行可恢复的数据迁移")
    migrate_commands = migrate.add_subparsers(dest="migrate_command", required=True)
    raw_store_migration = migrate_commands.add_parser("raw-store")
    raw_store_mode = raw_store_migration.add_mutually_exclusive_group()
    raw_store_mode.add_argument("--dry-run", action="store_true")
    raw_store_mode.add_argument("--verify", action="store_true")
    batch_migration = migrate_commands.add_parser("batch-artifacts")
    batch_migration.add_argument("--dry-run", action="store_true")
    proposal_gate_migration = migrate_commands.add_parser("proposal-gate-to-promotion")
    proposal_gate_mode = proposal_gate_migration.add_mutually_exclusive_group()
    proposal_gate_mode.add_argument("--dry-run", action="store_true")
    proposal_gate_mode.add_argument("--verify", action="store_true")
    epistemic_migration = migrate_commands.add_parser("epistemic-status")
    epistemic_mode = epistemic_migration.add_mutually_exclusive_group()
    epistemic_mode.add_argument("--dry-run", action="store_true")
    epistemic_mode.add_argument("--verify", action="store_true")
    trust_requalification = migrate_commands.add_parser("trust-requalification")
    trust_requalification.add_argument("--dry-run", action="store_true")
    runs = commands.add_parser("runs", help="查看或清理可重建的 system/runs")
    runs_commands = runs.add_subparsers(dest="runs_command", required=True)
    runs_commands.add_parser("list")
    runs_show = runs_commands.add_parser("show")
    runs_show.add_argument("run_id")
    runs_cleanup = runs_commands.add_parser("cleanup")
    runs_cleanup.add_argument("run_id")
    runs_cleanup.add_argument("--apply", action="store_true")
    audit = commands.add_parser("audit", help="只读生成知识治理审计报告")
    audit_commands = audit.add_subparsers(dest="audit_command", required=True)
    audit_commands.add_parser("contradictions", help="报告 evidence 与 relation 中的显式冲突")
    audit_commands.add_parser("drift", help="检查翻译冒充原文、证据漂移与不确定性擦除")
    commands.add_parser("recover", help="幂等续做未完成的 canonical approval journal")
    return parser


def doctor(repository: Repository) -> dict[str, object]:
    issues: list[str] = []
    warnings: list[str] = []
    sources: dict[str, dict[str, object]] = {}
    document_count = 0
    source_count = 0
    governance_documents = [
        *sorted((repository.root / "vault" / "exceptions").glob("exception-*.md")),
        *sorted((repository.root / "vault" / "promotions").glob("promotion-*.md")),
    ]
    indexed_documents = list(repository.all_indexed_documents())
    for path in [*indexed_documents, *governance_documents]:
        if path in indexed_documents:
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
    recovery_journals = [*ApprovalRecoveryManager(repository).pending(), *BundleRecoveryManager(repository).pending()]
    for journal in recovery_journals:
        issues.append(f"存在未完成 approval recovery journal: {repository.rel(journal)}")
    lifecycle = SourceLifecycleService(repository).check()
    issues.extend(f"source state inconsistency: {item}" for item in lifecycle["issues"])
    proposal_ids: dict[str, list[str]] = {}
    for path in repository.proposal_documents():
        try:
            proposal, _ = read_document(path)
            proposal_ids.setdefault(str(proposal.get("id")), []).append(repository.rel(path))
        except Exception:
            continue
    for proposal_id, paths in proposal_ids.items():
        if proposal_id and len(paths) > 1:
            issues.append(f"proposal 存在多个正式副本: {proposal_id} -> {paths}")
    for path in repository.canonical_documents():
        try:
            metadata, _ = read_document(path)
        except Exception:
            continue
        if metadata.get("type") == "claim":
            if metadata.get("atomicity_status") == "compound":
                issues.append(f"canonical compound claim: {repository.rel(path)}")
            if metadata.get("evidence_coverage") == "partial" and metadata.get("status") == "confirmed":
                issues.append(f"confirmed claim 只有部分 evidence coverage: {repository.rel(path)}")
            if metadata.get("extraction_quality") == "degraded" and metadata.get("status") == "confirmed":
                issues.append(f"degraded extraction 被确认为 canonical: {repository.rel(path)}")
        if metadata.get("relations") == [] and not metadata.get("source_ids"):
            warnings.append(f"孤立 canonical: {repository.rel(path)}")
    temporary = [path for path in repository.root.iterdir() if path.is_dir() and path.name.startswith(".tmp-")]
    for path in temporary:
        issues.append(f"临时 batch 目录仍位于仓库根目录: {repository.rel(path)}")
    for item in FollowupService(repository).list():
        if item.get("status") in {"missing", "inaccessible", "not_identified"}:
            warnings.append(f"未关闭 follow-up: {item['id']} ({item['status']})")
    return {
        "ok": not issues,
        "documents": document_count,
        "sources": source_count,
        "indexed_documents": indexed_count,
        "pending_recovery_journals": len(recovery_journals),
        "source_state_consistent": lifecycle["ok"],
        "proposal_unique": not any(len(paths) > 1 for paths in proposal_ids.values()),
        "warnings": warnings,
        "issues": issues,
    }


def _approved_target_physically_purged(repository: Repository, proposal: dict[str, object]) -> bool:
    """Allow approved proposals whose archived target was later removed from vault/archive."""
    target_id = str(proposal.get("target_id", ""))
    if not target_id or proposal.get("status") != "approved":
        return False

    def archived_candidate(candidate_path_value: object) -> bool:
        if not candidate_path_value:
            return False
        try:
            candidate_path = repository.resolve_inside(str(candidate_path_value))
            candidate, _ = read_document(candidate_path)
        except Exception:
            return False
        return (
            candidate.get("id") == target_id
            and candidate.get("proposed_status") == "archived"
        )

    if proposal.get("action") == "update" and archived_candidate(proposal.get("candidate_path")):
        return True
    for path in repository.proposal_documents():
        other, _ = read_document(path)
        if (
            other.get("type") != "proposal"
            or other.get("status") != "approved"
            or other.get("target_id") != target_id
            or other.get("action") != "update"
        ):
            continue
        if archived_candidate(other.get("candidate_path")):
            return True
    return False


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
    archived: list[tuple[Path, dict[str, object], str]] = []
    for path in repository.archive_documents():
        try:
            metadata, body = read_document(path)
            repository._validate_metadata(metadata, path)
            archived.append((path, metadata, body))
        except Exception as exc:
            errors.append(f"无法读取或校验归档对象 {repository.rel(path)}: {exc}")
    sources = {str(metadata["id"]) for _, metadata, _ in indexed if metadata.get("type") == "source"}
    sources.update(
        str(metadata["id"]) for _, metadata, _ in archived if metadata.get("type") == "source"
    )
    proposal_ids = {str(metadata["id"]) for _, metadata, _ in indexed if metadata.get("type") == "proposal"}
    object_ids = {str(metadata["id"]) for _, metadata, _ in indexed if metadata.get("type") != "proposal"}
    object_ids.update(
        str(metadata["id"]) for _, metadata, _ in archived if metadata.get("type") != "proposal"
    )
    known_ids = sources | proposal_ids | object_ids
    for _, metadata, _, role in records:
        if role != "document" or metadata.get("type") != "proposal":
            continue
        items = metadata.get("bundle_items", [])
        if isinstance(items, list):
            known_ids.update(
                str(item["target_id"])
                for item in items
                if isinstance(item, dict) and item.get("target_id")
            )
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

    for path, metadata, _ in [*indexed, *archived]:
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
            if metadata.get("type") == "claim" and metadata.get("atomicity_status") == "compound":
                errors.append(f"canonical claim 仍为 compound: {repository.rel(path)}")
            if metadata.get("type") == "claim" and metadata.get("evidence_coverage") == "partial" and metadata.get("status") == "confirmed":
                errors.append(f"confirmed claim evidence coverage 仅为 partial: {repository.rel(path)}")

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
        if proposal_kind in {"compile_bundle", "source_bundle", "corpus_distillation"}:
            items = proposal.get("bundle_items")
            if not isinstance(items, list) or not items:
                errors.append(f"compile bundle 缺少 bundle_items: {repository.rel(path)}")
                continue
            for item in items:
                if not isinstance(item, dict):
                    errors.append(f"compile bundle item 非对象: {repository.rel(path)}")
                    continue
                for key in ("item_id", "candidate_path", "candidate_sha256", "target_id", "target_path", "action", "decision"):
                    if item.get(key) is None:
                        errors.append(f"compile bundle item 缺少 {key}: {repository.rel(path)}")
                try:
                    for revision in item.get("revision_history", []):
                        if isinstance(revision, dict) and revision.get("candidate_path"):
                            referenced_candidates.add(repository.resolve_inside(str(revision["candidate_path"])))
                    candidate_path = repository.resolve_inside(str(item["candidate_path"]))
                    referenced_candidates.add(candidate_path)
                    if not candidate_path.is_file() or sha256_bytes(candidate_path.read_bytes()) != item.get("candidate_sha256"):
                        errors.append(f"compile bundle candidate 缺失或哈希不匹配: {item.get('item_id')}")
                    else:
                        candidate, _ = read_document(candidate_path)
                        if candidate.get("id") != item.get("target_id") or candidate.get("status") != "proposal":
                            errors.append(f"compile bundle candidate 身份无效: {item.get('item_id')}")
                    if item.get("action") == "update":
                        base_path = repository.resolve_inside(str(item.get("base_path")))
                        referenced_bases.add(base_path)
                        if not base_path.is_file() or sha256_bytes(base_path.read_bytes()) != item.get("base_sha256"):
                            errors.append(f"compile bundle base 缺失或哈希不匹配: {item.get('item_id')}")
                except Exception as exc:
                    errors.append(f"compile bundle item 无效: {item.get('item_id')}: {exc}")
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
                    if archived_target is None and not _approved_target_physically_purged(
                        repository, proposal
                    ):
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
    raw_store = RawStoreService(repository)
    extraction_service = ExtractionService(repository)
    works = WorkService(repository)
    lifecycle = SourceLifecycleService(repository)
    quality_service = SourceQualityService(repository)
    followup_service = FollowupService(repository)
    run_service = RunArtifactService(repository)
    if args.command == "capture":
        result = captures.capture(args.target, args.comment, refresh=args.refresh).__dict__
        obsidian_result = ObsidianViewService(repository).build()
        result["obsidian"] = {
            "ok": obsidian_result["ok"], "documents": obsidian_result["documents"],
            "sources": obsidian_result["sources"], "written_count": len(obsidian_result["written"]),
            "removed": obsidian_result["removed"],
        }
        _print(result)
    elif args.command == "capture-wechat":
        result = captures.capture_wechat_url(args.url, args.comment, refresh=args.refresh).__dict__
        result["obsidian"] = ObsidianViewService(repository).build()
        _print(result)
    elif args.command == "capture-text":
        text = args.text if args.text is not None else sys.stdin.read()
        result = captures.capture_text(text, args.comment, args.title).__dict__
        result["obsidian"] = ObsidianViewService(repository).build()
        _print(result)
    elif args.command == "inbox":
        _print(proposals.inbox())
    elif args.command in {"triage", "daily"}:
        result = DailyTriageService(repository).run(
            args.source_ids, limit=args.limit,
            compile_selected=args.compile_selected, recheck=args.recheck,
        )
        result["obsidian"] = ObsidianViewService(repository).build()
        _print(result)
    elif args.command == "source":
        if args.source_command == "status":
            _print(lifecycle.status(args.source_id, assess=True).as_dict())
        elif args.source_command == "history":
            _print(lifecycle.history(args.source_id))
        else:
            _print({"path": SourceAnnotationService(repository).annotate(args.source_id, why_saved=args.why_saved, salience=args.salience)})
    elif args.command == "quality":
        _print(quality_service.assess(args.source_id, persist=True).as_dict())
    elif args.command == "extract":
        result = extraction_service.extract(args.source_id, rebuild=args.rebuild)
        _print(result.__dict__)
        return 0 if result.status == "ready" else 1
    elif args.command == "extractions":
        items = []
        for path in extraction_service.documents():
            metadata, _ = read_document(path)
            if args.source and metadata.get("source_id") != args.source:
                continue
            items.append({**metadata, "path": repository.rel(path)})
        _print(items)
    elif args.command == "work":
        _print(works.propose(
            args.source_ids, arxiv_id=args.arxiv_id, title=args.title, authors=args.author
        ).__dict__)
    elif args.command == "compile":
        provider = JsonBundleProvider(args.bundle_file, args.provider_name) if args.bundle_file else None
        compiled = BundleCompiler(repository, provider).compile(args.source_id)
        result = {"compile": compiled.__dict__, "working": None, "canonical_writes": 0}
        if compiled.proposal_id:
            result["working"] = WorkingMemoryService(repository).ingest_bundle(compiled.proposal_id).__dict__
        obsidian_result = ObsidianViewService(repository).build()
        result["obsidian"] = {
            "ok": obsidian_result["ok"], "documents": obsidian_result["documents"],
            "sources": obsidian_result["sources"], "written_count": len(obsidian_result["written"]),
            "removed": obsidian_result["removed"],
        }
        _print(result)
    elif args.command == "synthesize":
        _print(proposals.synthesize(args.claim_ids).__dict__)
    elif args.command in {"discover", "related-content"}:
        _print(proposals.discover(args.seed_id).__dict__)
    elif args.command == "distill":
        service = CorpusDistillationService(repository)
        _print((service.plan() if args.dry_run else service.apply()).__dict__)
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
    elif args.command == "review":
        service = SourceBundleReviewService(repository)
        if args.review_command == "queue":
            _print(service.queue())
        elif args.review_command == "source":
            _print([item for item in service.queue() if args.source_id in item["source_ids"]])
        elif args.review_command == "bundle":
            _print(service.show(args.bundle_id, details=args.details))
        elif args.review_command == "approve":
            _print(WorkingMemoryService(repository).ingest_bundle(
                args.bundle_id, args.items.split(",") if args.items else None
            ).__dict__)
        elif args.review_command == "source-only":
            _print(service.source_only(args.bundle_id, args.reason))
        else:
            _print({"deferred": args.bundle_id, "proposal_path": proposals.defer(args.bundle_id, args.reason)})
    elif args.command == "followups":
        items = followup_service.list()
        _print([item for item in items if not args.status or item.get("status") == args.status])
    elif args.command == "followup":
        if args.followup_command == "detect":
            _print(followup_service.detect(args.source_id))
        elif args.followup_command == "show":
            _print(followup_service.show(args.followup_id))
        elif args.followup_command == "normalize-locators":
            _print(followup_service.normalize_locators(apply=args.apply))
        else:
            _print({"path": followup_service.resolve(args.followup_id, args.captured_source)})
    elif args.command == "proposal":
        if args.proposal_command in {"show", "diff"}:
            _print(proposals.show(args.proposal_id))
        elif args.proposal_command == "approve":
            _, proposal_metadata, _ = repository.find_document(args.proposal_id)
            if proposal_metadata.get("proposal_kind") in {"compile_bundle", "source_bundle", "corpus_distillation"}:
                item_ids = args.items.split(",") if args.items else None
                _print(WorkingMemoryService(repository).ingest_bundle(args.proposal_id, item_ids).__dict__)
            else:
                if args.items:
                    raise GlobalMemoryError("--items 只适用于 compile bundle")
                _print(WorkingMemoryService(repository).ingest_bundle(args.proposal_id).__dict__)
        elif args.proposal_command == "publish":
            _print(WorkingMemoryService(repository).ingest_bundle(args.proposal_id).__dict__)
        elif args.proposal_command == "reject":
            _, proposal_metadata, _ = repository.find_document(args.proposal_id)
            if proposal_metadata.get("proposal_kind") in {"compile_bundle", "source_bundle", "corpus_distillation"}:
                item_ids = args.items.split(",") if args.items else None
                _print(BundleReviewService(repository).reject(args.proposal_id, item_ids, args.reason))
            else:
                if args.items:
                    raise GlobalMemoryError("--items 只适用于 compile bundle")
                _print({"rejected": args.proposal_id, "proposal_path": proposals.reject(args.proposal_id, args.reason)})
        elif args.proposal_command == "defer":
            _print({"deferred": args.proposal_id, "proposal_path": proposals.defer(args.proposal_id, args.reason)})
        elif args.proposal_command == "split-item":
            _print(BundleReviewService(repository).split_item(
                args.proposal_id, args.item, args.from_files.split(","), args.reason
            ))
        elif args.proposal_command == "verify-item-quote":
            _print(BundleReviewService(repository).verify_item_quote(
                args.proposal_id, args.item, args.source, args.extraction,
                args.span_start, args.quote, args.section, args.reason,
            ))
        elif args.proposal_command == "mark-compound":
            _print(BundleReviewService(repository).mark_item_compound(
                args.proposal_id, args.item, args.reason,
            ))
        else:
            _, proposal_metadata, _ = repository.find_document(args.proposal_id)
            if proposal_metadata.get("proposal_kind") in {"compile_bundle", "source_bundle", "corpus_distillation"}:
                if not args.item:
                    raise GlobalMemoryError("compile bundle revise 必须指定 --item")
                _print(BundleReviewService(repository).revise_item(
                    args.proposal_id, args.item, args.candidate_file, args.reason
                ))
            else:
                if args.item:
                    raise GlobalMemoryError("--item 只适用于 compile bundle")
                _print(proposals.revise(args.proposal_id, args.candidate_file, args.reason).__dict__)
    elif args.command == "promote":
        service = PromotionService(repository)
        if args.to == "trusted":
            _print(service.promote_trusted(args.target_id, automatic=False, reason=args.reason))
        else:
            _print(service.recommend_canonical(args.target_id, args.reason))
    elif args.command == "demote":
        _print(PromotionService(repository).demote_working(args.target_id, args.reason))
    elif args.command == "trust":
        _print(PromotionService(repository).explain(args.target_id))
    elif args.command == "history":
        _, metadata, _ = repository.find_document(args.target_id)
        _print({"object_id": args.target_id, "promotion_history": metadata.get("promotion_history", [])})
    elif args.command == "rollback":
        _print(PromotionService(repository).rollback(args.change_id, args.reason))
    elif args.command == "exceptions":
        _print(ExceptionService(repository).list(set(args.status) if args.status else None))
    elif args.command == "exception":
        service = ExceptionService(repository)
        if args.exception_command == "show":
            path, metadata, body = repository.find_document(args.exception_id)
            _print({"path": repository.rel(path), "metadata": metadata, "body": body})
        else:
            _print(service.resolve(args.exception_id, args.resolution, args.action))
    elif args.command == "promotions":
        _print(PromotionService(repository).list_cards(set(args.status) if args.status else None))
    elif args.command == "promotion":
        service = PromotionService(repository)
        if args.promotion_command == "show":
            path, metadata, body = repository.find_document(args.promotion_id)
            _print({"path": repository.rel(path), "metadata": metadata, "body": body})
        elif args.promotion_command == "approve":
            _print(service.approve_canonical(args.promotion_id, lock=args.lock))
        else:
            decision = "rejected" if args.promotion_command == "reject" else "deferred"
            _print(service.decide(args.promotion_id, decision, args.reason))
    elif args.command == "consolidate":
        service = ConsolidationService(repository)
        if args.consolidate_command == "daily":
            result = service.daily(limit=args.limit)
        elif args.consolidate_command == "weekly":
            result = service.weekly()
        else:
            result = ConsolidationReceiptService(repository).consolidate(args.object_id)
        obsidian_result = ObsidianViewService(repository).build()
        result["obsidian"] = {
            "ok": obsidian_result["ok"], "documents": obsidian_result["documents"],
            "sources": obsidian_result["sources"], "written_count": len(obsidian_result["written"]),
            "removed": obsidian_result["removed"],
        }
        _print(result)
    elif args.command == "evolve":
        candidate, body = read_document(Path(args.from_file).expanduser().resolve())
        _print(KnowledgeEvolutionService(repository).apply(
            args.object_id, candidate, body, change_type=args.change_type,
            reason=args.reason, trigger_source=args.trigger_source,
        ))
    elif args.command == "weekly-report":
        result = ConsolidationService(repository).weekly()
        obsidian_result = ObsidianViewService(repository).build()
        result["obsidian"] = {
            "ok": obsidian_result["ok"], "documents": obsidian_result["documents"],
            "sources": obsidian_result["sources"], "written_count": len(obsidian_result["written"]),
            "removed": obsidian_result["removed"],
        }
        _print(result)
    elif args.command == "search":
        filters = {
            "object_types": set(args.types.split(",")) if args.types else None,
            "statuses": set(args.statuses.split(",")) if args.statuses else None,
            "canonical_only": args.canonical_only,
            "include_proposals": args.include_proposals,
        }
        results = (
            repository.search_with_relations(
                args.query, args.limit, max_depth=args.relation_depth,
                max_nodes=max(1, min(100, args.limit)), **filters,
            ) if args.relation_depth else repository.search(args.query, args.limit, **filters)
        )
        _print([result.__dict__ for result in results])
    elif args.command == "context":
        question = args.question or args.query
        if not question:
            raise GlobalMemoryError("context 必须提供 positional query 或 --question")
        pack = ContextPackService(repository).build(
            question, args.token_budget,
            profiles=[item for item in args.profile.split(",") if item], project=args.project,
            domains=set(args.domain.split(",")) if args.domain else None,
            object_types=set(args.types.split(",")) if args.types else None,
            statuses=set(args.statuses.split(",")) if args.statuses else None,
            updated_since=args.updated_since,
            source_kinds=set(args.source_kind.split(",")) if args.source_kind else None,
            include_proposals=args.include_proposals, relation_depth=args.relation_depth,
            strict_execution=args.strict_execution,
        )
        _print(pack.as_markdown() if args.format == "markdown" else pack.as_dict())
    elif args.command == "obsidian":
        _print(ObsidianViewService(repository).build())
    elif args.command == "receipt":
        service = ReceiptService(repository)
        if args.receipt_command == "create":
            _print(service.create(args.agent, args.project, args.task, args.from_file))
        else:
            _print(service.propose(args.receipt_id))
    elif args.command == "maintain":
        rebuilt = None
        if args.rebuild_derived:
            rebuilt = {
                "indexed_documents": repository.rebuild_index(),
                "obsidian": ObsidianViewService(repository).build(),
            }
        doctor_result = doctor(repository)
        lint_result = lint(repository)
        raw_result = raw_store.verify()
        result = {
            "ok": doctor_result["ok"] and lint_result["ok"] and raw_result["ok"],
            "mode": "rebuild-derived" if args.rebuild_derived else "read-only",
            "integrity": {
                "doctor": doctor_result,
                "lint": lint_result,
                "raw": raw_result,
            },
            "inventory": MaintenanceService(repository).inventory(),
            "derived_views": ObsidianViewService(repository).status(),
            "rebuilt": rebuilt,
        }
        _print(result)
        return 0 if result["ok"] else 1
    elif args.command == "weekly":
        triage_result = DailyTriageService(repository).run(
            limit=args.triage_limit, recheck=args.recheck
        )
        consolidation_result = ConsolidationService(repository).weekly()
        rebuilt = None
        if not args.no_rebuild_derived:
            rebuilt = {
                "indexed_documents": repository.rebuild_index(),
                "obsidian": ObsidianViewService(repository).build(),
            }
        doctor_result = doctor(repository)
        lint_result = lint(repository)
        raw_result = raw_store.verify()
        contradictions = contradiction_audit(repository)
        claim_ids = []
        for path in repository.canonical_documents():
            metadata, _ = read_document(path)
            if metadata.get("type") == "claim" and metadata.get("status") not in {"archived", "superseded"}:
                claim_ids.append(str(metadata["id"]))
        result = {
            "ok": (
                doctor_result["ok"] and lint_result["ok"]
                and raw_result["ok"] and contradictions["ok"]
            ),
            "mode": "weekly-maintenance",
            "triage": triage_result,
            "consolidation": consolidation_result,
            "integrity": {
                "doctor": doctor_result,
                "lint": lint_result,
                "raw": raw_result,
            },
            "contradictions": contradictions,
            "inventory": MaintenanceService(repository).inventory(),
            "derived_views": ObsidianViewService(repository).status(),
            "rebuilt": rebuilt,
            "synthesis_eligibility": {
                "eligible": len(claim_ids) >= 2,
                "canonical_claim_count": len(claim_ids),
                "claim_ids": sorted(claim_ids),
                "proposal_created": False,
                "note": "Weekly maintenance reports eligibility only; synthesis remains an explicit governed command.",
            },
            "canonical_writes": 0,
        }
        _print(result)
        return 0 if result["ok"] else 1
    elif args.command == "mcp":
        run_mcp(repository, args)
        return 0
    elif args.command == "show":
        path, metadata, body = repository.find_document(args.object_id)
        _print({"path": repository.rel(path), "metadata": metadata, "body": body})
    elif args.command == "related":
        _print(repository.related(args.object_id))
    elif args.command == "status":
        state_counts: dict[str, int] = {}
        for state in lifecycle.all():
            state_counts[state["state"]] = state_counts.get(state["state"], 0) + 1
        status_result = {
            "root": str(repository.root), "objects_by_type": repository.count_by_type(),
            "inbox": len(proposals.inbox()), "proposals_by_status": {
                state: len(proposals.list(state))
                for state in ("pending", "deferred", "migrated", "superseded", "published", "approved", "rejected")
            },
            "pending_recovery_journals": len(ApprovalRecoveryManager(repository).pending()) + len(BundleRecoveryManager(repository).pending()),
            "source_processing_states": state_counts,
            "metrics": ProjectMetricsService(repository).collect(),
        }
        _print(status_result)
    elif args.command == "metrics":
        service = ProjectMetricsService(repository)
        metrics_result = service.collect()
        _print(service.write_project_state(metrics_result) if args.write_project_state else metrics_result)
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
    elif args.command == "raw":
        result = raw_store.verify()
        _print(result)
        return 0 if result["ok"] else 1
    elif args.command == "migrate":
        if args.migrate_command == "trust-requalification":
            migration = TrustPolicyRequalificationMigration(repository)
            _print(migration.plan() if args.dry_run else migration.apply())
            return 0
        if args.migrate_command == "epistemic-status":
            migration = EpistemicStatusMigration(repository)
            result = migration.verify() if args.verify else migration.plan() if args.dry_run else migration.apply()
            _print(result)
            return 0 if not args.verify or result["ok"] else 1
        if args.migrate_command == "batch-artifacts":
            migration = BatchArtifactMigrator(repository)
            result = migration.plan() if args.dry_run else migration.migrate()
            _print(result.__dict__)
            return 0 if not result.errors else 1
        if args.migrate_command == "proposal-gate-to-promotion":
            migration = ProposalGateMigration(repository)
            if args.verify:
                result = migration.plan()
                result["verified"] = result["pending_proposals"] == 0
            else:
                result = migration.plan() if args.dry_run else migration.apply()
            _print(result)
            return 0 if not args.verify or result["verified"] else 1
        if args.verify:
            result = raw_store.verify()
            _print(result)
            return 0 if result["ok"] else 1
        result = raw_store.plan() if args.dry_run else raw_store.migrate()
        _print(result.__dict__)
        return 0 if not result.errors else 1
    elif args.command == "runs":
        if args.runs_command == "list":
            _print(run_service.list())
        elif args.runs_command == "show":
            _print(run_service.show(args.run_id))
        else:
            _print(run_service.cleanup(args.run_id, apply=args.apply))
    elif args.command == "audit":
        if args.audit_command == "contradictions":
            result = contradiction_audit(repository)
            _print(result)
            return 0 if result["ok"] else 1
        result = DriftAuditService(repository).run()
        _print(result)
        return 0 if result["ok"] else 1
    elif args.command == "recover":
        approval = ApprovalRecoveryManager(repository).recover_all()
        bundle = BundleRecoveryManager(repository).recover_all()
        result = {
            "recovered": [*approval["recovered"], *bundle["recovered"]],
            "blocked": [*approval["blocked"], *bundle["blocked"]],
        }
        _print(result)
        return 1 if result["blocked"] else 0
    return 0


def main(argv: list[str] | None = None) -> int:
    # Windows commonly inherits a GBK console; vault content may contain symbols
    # such as non-breaking spaces that GBK cannot encode. CLI JSON is UTF-8.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8")
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
