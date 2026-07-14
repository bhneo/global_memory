from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from .capture import CaptureService
from .errors import GlobalMemoryError
from .markdown import read_document
from .proposals import ProposalService
from .recovery import ApprovalRecoveryManager
from .repository import Repository, sha256_bytes


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
    update_parser = commands.add_parser(
        "propose-update", help="从 UTF-8 Markdown candidate 创建 canonical update proposal"
    )
    update_parser.add_argument("target_id")
    update_parser.add_argument("--from-file", dest="candidate_file", required=True)
    update_parser.add_argument("--reason", required=True)
    proposals = commands.add_parser("proposals", help="列出 proposals")
    proposals.add_argument(
        "--status", choices=["pending", "deferred", "superseded", "approved", "rejected"]
    )

    proposal = commands.add_parser("proposal", help="审阅 proposal")
    proposal_commands = proposal.add_subparsers(dest="proposal_command", required=True)
    proposal_show = proposal_commands.add_parser("show")
    proposal_show.add_argument("proposal_id")
    proposal_approve = proposal_commands.add_parser("approve")
    proposal_approve.add_argument("proposal_id")
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

    search = commands.add_parser("search", help="全文检索来源和 canonical knowledge")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20)
    show = commands.add_parser("show", help="按稳定 ID 显示对象")
    show.add_argument("object_id")
    related = commands.add_parser("related", help="显示 typed relations")
    related.add_argument("object_id")
    commands.add_parser("status", help="显示仓库统计")
    commands.add_parser("rebuild-index", help="从 Markdown 与 raw source 重建 SQLite 索引")
    commands.add_parser("doctor", help="检查 schema、原始内容哈希和索引")
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


def run(args: argparse.Namespace) -> int:
    repository = _repository(args)
    if args.command == "init":
        repository.init()
        _print({"root": str(repository.root), "index": repository.rel(repository.index_path), "status": "initialized"})
        return 0
    repository.ensure_initialized()
    captures = CaptureService(repository)
    proposals = ProposalService(repository)
    if args.command == "capture":
        _print(captures.capture(args.target, args.comment, refresh=args.refresh).__dict__)
    elif args.command == "capture-text":
        text = args.text if args.text is not None else sys.stdin.read()
        _print(captures.capture_text(text, args.comment, args.title).__dict__)
    elif args.command == "inbox":
        _print(proposals.inbox())
    elif args.command == "compile":
        _print(proposals.compile(args.source_id).__dict__)
    elif args.command == "propose-update":
        _print(
            proposals.propose_update(
                args.target_id, args.candidate_file, args.reason
            ).__dict__
        )
    elif args.command == "proposals":
        _print(proposals.list(args.status))
    elif args.command == "proposal":
        if args.proposal_command == "show":
            _print(proposals.show(args.proposal_id))
        elif args.proposal_command == "approve":
            _print({"approved": args.proposal_id, "target_path": proposals.approve(args.proposal_id)})
        elif args.proposal_command == "reject":
            _print({"rejected": args.proposal_id, "proposal_path": proposals.reject(args.proposal_id, args.reason)})
        elif args.proposal_command == "defer":
            _print({"deferred": args.proposal_id, "proposal_path": proposals.defer(args.proposal_id, args.reason)})
        else:
            _print(proposals.revise(args.proposal_id, args.candidate_file, args.reason).__dict__)
    elif args.command == "search":
        _print([result.__dict__ for result in repository.search(args.query, args.limit)])
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
