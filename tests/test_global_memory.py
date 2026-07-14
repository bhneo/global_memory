from __future__ import annotations

import sqlite3
import shutil
import uuid
from contextlib import closing
from pathlib import Path

import pytest

from global_memory.capture import CaptureService, canonicalize_url
from global_memory.cli import build_parser, doctor
from global_memory.errors import ImmutableContentError, ValidationError
from global_memory.markdown import read_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository


@pytest.fixture()
def workspace() -> Path:
    parent = Path.cwd() / "data" / "derived"
    parent.mkdir(parents=True, exist_ok=True)
    path = parent / f"gm-tests-{uuid.uuid4().hex}"
    path.mkdir()
    try:
        yield path
    finally:
        shutil.rmtree(path)


@pytest.fixture()
def repo(workspace: Path) -> Repository:
    repository = Repository(workspace / "全局记忆库")
    repository.init()
    return repository


def capture_web_bytes(
    repo: Repository,
    url: str,
    content: bytes = b"Global memory keeps provenance.",
    title: str = "Global Memory",
    refresh: bool = False,
):
    canonical = canonicalize_url(url)
    return CaptureService(repo)._write_source(
        kind="web",
        original_locator=url,
        canonical_locator=canonical,
        content=content,
        title=title,
        comment="test evidence",
        import_method="test",
        content_type="text/plain; charset=utf-8",
        refresh=refresh,
    )


def test_same_url_is_duplicate(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://example.com/article?a=1")
    second = capture_web_bytes(repo, "https://example.com/article?a=1")
    assert second.duplicate_source is True
    assert second.source_id == first.source_id
    assert len(list(repo.source_documents())) == 1


def test_tracking_parameters_share_canonical_url(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://EXAMPLE.com/article?utm_source=x&a=1#part")
    second = capture_web_bytes(repo, "https://example.com/article?a=1&utm_campaign=y")
    assert second.duplicate_source is True
    assert second.source_id == first.source_id


def test_same_content_from_different_urls_preserves_both_sources(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://one.example/item")
    second = capture_web_bytes(repo, "https://two.example/mirror")
    assert second.duplicate_source is False
    assert second.duplicate_content is True
    assert second.source_id != first.source_id
    assert second.raw_content_path == first.raw_content_path
    assert len(list(repo.source_documents())) == 2


def test_unchanged_refresh_reuses_latest_version_without_proposal(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://example.com/changing", b"version one")
    refreshed = capture_web_bytes(
        repo, "https://example.com/changing", b"version one", refresh=True
    )
    assert refreshed.duplicate_source is True
    assert refreshed.source_id == first.source_id
    assert refreshed.version_number == 1
    assert refreshed.refresh_proposal_id is None
    assert len(list(repo.source_documents())) == 1


def test_changed_refresh_appends_version_and_diff_proposal(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://example.com/changing", b"version one")
    old_source_bytes = (repo.root / first.source_path).read_bytes()
    old_raw_bytes = (repo.root / first.raw_content_path).read_bytes()

    refreshed = capture_web_bytes(
        repo, "https://example.com/changing", b"version two", refresh=True
    )

    assert refreshed.duplicate_source is False
    assert refreshed.version_number == 2
    assert refreshed.previous_source_id == first.source_id
    assert refreshed.refresh_proposal_id
    assert len(list(repo.source_documents())) == 2
    assert (repo.root / first.source_path).read_bytes() == old_source_bytes
    assert (repo.root / first.raw_content_path).read_bytes() == old_raw_bytes
    metadata, _ = read_document(repo.root / refreshed.source_path)
    assert metadata["previous_version_id"] == first.source_id
    assert metadata["version_number"] == 2
    proposal_path, proposal, proposal_body = repo.find_document(refreshed.refresh_proposal_id)
    assert proposal_path.parent == repo.root / "vault" / "proposals"
    assert proposal["proposal_kind"] == "source_refresh"
    assert proposal["status"] == "pending"
    assert "-version one" in proposal_body
    assert "+version two" in proposal_body
    assert doctor(repo)["ok"] is True


def test_repeated_refresh_and_content_reversion_preserve_version_history(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://example.com/history", b"alpha")
    second = capture_web_bytes(repo, "https://example.com/history", b"beta", refresh=True)
    repeated = capture_web_bytes(repo, "https://example.com/history", b"beta", refresh=True)
    third = capture_web_bytes(repo, "https://example.com/history", b"alpha", refresh=True)

    assert repeated.source_id == second.source_id
    assert repeated.duplicate_source is True
    assert repeated.refresh_proposal_id == second.refresh_proposal_id
    assert third.version_number == 3
    assert third.previous_source_id == second.source_id
    assert third.source_id not in {first.source_id, second.source_id}
    assert third.raw_content_path == first.raw_content_path
    assert len(list(repo.source_documents())) == 3


def test_source_refresh_approval_does_not_modify_canonical(repo: Repository) -> None:
    first = capture_web_bytes(repo, "https://example.com/review", b"old evidence")
    ProposalService(repo).compile(first.source_id)
    refreshed = capture_web_bytes(
        repo, "https://example.com/review", b"new evidence", refresh=True
    )
    service = ProposalService(repo)
    target_path = service.approve(refreshed.refresh_proposal_id)

    assert target_path == refreshed.source_path
    assert list(repo.canonical_documents()) == []
    proposal_path, proposal, _ = repo.find_document(refreshed.refresh_proposal_id)
    assert proposal_path.exists()
    assert proposal["status"] == "approved"
    assert proposal["review_reason"] == "人工确认新的不可变来源版本"
    assert [item["id"] for item in service.inbox()] == [refreshed.source_id]


def test_source_refresh_approval_revalidates_version_hashes(repo: Repository) -> None:
    capture_web_bytes(repo, "https://example.com/tamper", b"old")
    refreshed = capture_web_bytes(
        repo, "https://example.com/tamper", b"new", refresh=True
    )
    proposal_path, proposal, _ = repo.find_document(refreshed.refresh_proposal_id)
    text = proposal_path.read_text(encoding="utf-8").replace(
        proposal["new_content_sha256"], "0" * 64
    )
    proposal_path.write_text(text, encoding="utf-8")

    with pytest.raises(ValidationError, match="目标版本无效"):
        ProposalService(repo).approve(refreshed.refresh_proposal_id)
    _, unchanged, _ = repo.find_document(refreshed.refresh_proposal_id)
    assert unchanged["status"] == "pending"


def test_doctor_reports_broken_source_version_chain(repo: Repository) -> None:
    capture_web_bytes(repo, "https://example.com/broken-chain", b"old")
    refreshed = capture_web_bytes(
        repo, "https://example.com/broken-chain", b"new", refresh=True
    )
    source_path = repo.root / refreshed.source_path
    text = source_path.read_text(encoding="utf-8").replace(
        "version_number: 2", "version_number: 4"
    )
    source_path.write_text(text, encoding="utf-8")

    result = doctor(repo)
    assert result["ok"] is False
    assert any("版本链不连续" in issue for issue in result["issues"])


def test_capture_refresh_cli_flag_and_url_fetch(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    class Response:
        def __init__(self, body: bytes):
            self.body = body
            self.headers = {"Content-Type": "text/plain; charset=utf-8"}

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self, _limit: int) -> bytes:
            return self.body

        def geturl(self) -> str:
            return "https://example.com/live"

    responses = iter([Response(b"first"), Response(b"second")])
    monkeypatch.setattr(
        "global_memory.capture.urllib.request.urlopen",
        lambda *_args, **_kwargs: next(responses),
    )
    service = CaptureService(repo)
    first = service.capture_url("https://example.com/live")
    second = service.capture_url("https://example.com/live", refresh=True)
    args = build_parser().parse_args(
        ["capture", "https://example.com/live", "--refresh"]
    )

    assert first.version_number == 1
    assert second.version_number == 2
    assert args.refresh is True
    with pytest.raises(ValidationError, match="只支持 HTTP"):
        service.capture("local-file.txt", refresh=True)


def test_same_local_file_is_duplicate(repo: Repository, workspace: Path) -> None:
    local = workspace / "中文资料.txt"
    local.write_text("中文路径与文件名可以工作。", encoding="utf-8")
    service = CaptureService(repo)
    first = service.capture_file(local, "保留原话")
    second = service.capture_file(local, "再次导入")
    assert second.duplicate_source is True
    assert first.source_id == second.source_id


def test_immutable_raw_content_cannot_be_overwritten(repo: Repository) -> None:
    path = repo.root / "vault" / "raw" / "web" / "content" / "fixed.txt"
    assert repo.immutable_write(path, b"first") is True
    assert repo.immutable_write(path, b"first") is False
    with pytest.raises(ImmutableContentError):
        repo.immutable_write(path, b"changed")
    assert path.read_bytes() == b"first"


def test_invalid_input_does_not_damage_database(repo: Repository) -> None:
    with pytest.raises(ValidationError):
        CaptureService(repo).capture_text("   ")
    with closing(sqlite3.connect(repo.index_path)) as connection:
        assert connection.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    assert list(repo.source_documents()) == []


def test_search_returns_result_with_provenance(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "A provenance chain links every claim to immutable evidence.",
        title="Provenance principle",
    )
    results = repo.search("provenance")
    assert results
    assert results[0].id == captured.source_id
    assert results[0].source_ids == [captured.source_id]


def test_unapproved_proposal_does_not_touch_canonical(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Evidence should remain traceable.")
    proposal = ProposalService(repo).compile(captured.source_id)
    assert not (repo.root / proposal.target_path).exists()
    metadata, _ = read_document(repo.root / proposal.proposal_path)
    assert metadata["status"] == "pending"


def test_approved_proposal_creates_searchable_knowledge(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Approval gates protect canonical knowledge.")
    service = ProposalService(repo)
    proposal = service.compile(captured.source_id)
    target = service.approve(proposal.proposal_id)
    target_path = repo.root / target
    assert target_path.exists()
    metadata, body = read_document(target_path)
    assert metadata["status"] == "confirmed"
    assert metadata["approved_via"] == proposal.proposal_id
    assert metadata["source_ids"] == [captured.source_id]
    assert "Approval gates" in body
    assert any(result.id == metadata["id"] for result in repo.search("Approval"))


def test_rejected_proposal_never_creates_target(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("A rejected candidate.")
    service = ProposalService(repo)
    proposal = service.compile(captured.source_id)
    service.reject(proposal.proposal_id, "证据不足")
    assert not (repo.root / proposal.target_path).exists()
    metadata, _ = read_document(repo.root / proposal.proposal_path)
    assert metadata["status"] == "rejected"
    assert metadata["review_reason"] == "证据不足"


def test_illegal_relation_type_blocks_rebuild(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Typed relations need validation.")
    proposal = ProposalService(repo).compile(captured.source_id)
    candidate = repo.root / proposal.candidate_path
    text = candidate.read_text(encoding="utf-8").replace('"derived_from"', '"made_up_relation"')
    candidate.write_text(text, encoding="utf-8")
    with pytest.raises(ValidationError, match="非法关系类型"):
        metadata, _ = read_document(candidate)
        repo._validate_metadata(metadata, candidate)


def test_deleted_index_can_be_rebuilt(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Rebuildable indexes are not truth.")
    repo.index_path.unlink()
    assert not repo.index_path.exists()
    assert repo.rebuild_index() == 1
    assert repo.search("Rebuildable")[0].id == captured.source_id


def test_markdown_is_directly_readable(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Human-readable original text.", title="Readable")
    source_text = (repo.root / captured.source_path).read_text(encoding="utf-8")
    raw_text = (repo.root / captured.raw_content_path).read_text(encoding="utf-8")
    assert source_text.startswith("---\n")
    assert "# Readable" in source_text
    assert raw_text == "Human-readable original text."


def test_chinese_filename_and_content_are_searchable(repo: Repository, workspace: Path) -> None:
    local = workspace / "具身智能观察.md"
    local.write_text("机器人长期记忆需要来源追踪。", encoding="utf-8")
    captured = CaptureService(repo).capture_file(local)
    assert repo.search("来源追踪")[0].id == captured.source_id


def test_files_remain_recoverable_if_index_refresh_fails(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    real_rebuild = repo.rebuild_index

    def fail_rebuild() -> int:
        raise sqlite3.OperationalError("simulated index failure")

    monkeypatch.setattr(repo, "rebuild_index", fail_rebuild)
    with pytest.raises(sqlite3.OperationalError):
        CaptureService(repo).capture_text("Durable before derived indexing.")
    assert len(list(repo.source_documents())) == 1
    monkeypatch.setattr(repo, "rebuild_index", real_rebuild)
    assert repo.rebuild_index() == 1
    assert doctor(repo)["ok"] is True
