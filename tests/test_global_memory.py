from __future__ import annotations

import sqlite3
import shutil
import uuid
import json
from contextlib import closing
from pathlib import Path

import pytest

from global_memory.capture import CaptureService, canonicalize_url
from global_memory.cli import build_parser, doctor, lint
from global_memory.errors import ImmutableContentError, ValidationError
from global_memory.markdown import read_document, render_document
from global_memory.proposals import ProposalService
from global_memory.recovery import ApprovalRecoveryManager
from global_memory.repository import Repository, sha256_bytes


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


def create_approved_claim(repo: Repository, text: str = "Original canonical claim."):
    captured = CaptureService(repo).capture_text(text, title="Canonical claim source")
    service = ProposalService(repo)
    proposal = service.compile(captured.source_id)
    target = service.approve(proposal.proposal_id)
    return captured, repo.root / target


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


def test_lint_accepts_valid_truth_and_proposal_chain(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Lint checks provenance and proposal integrity.")
    proposal = ProposalService(repo).compile(captured.source_id)
    result = lint(repo)

    assert result["ok"] is True
    assert result["errors"] == []
    assert result["warnings"] == []
    assert result["checked_documents"] == 3
    assert proposal.proposal_id


def test_lint_reports_broken_references_hashes_and_orphans(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Lint failure fixture.")
    proposal = ProposalService(repo).compile(captured.source_id)
    candidate_path = repo.root / proposal.candidate_path
    candidate_path.write_text(candidate_path.read_text(encoding="utf-8") + "tampered\n", encoding="utf-8")

    broken_metadata = {
        "id": "claim_lint_broken",
        "type": "claim",
        "status": "confirmed",
        "title": "Broken lint claim",
        "created_at": "2026-07-14T20:00:00+08:00",
        "updated_at": "2026-07-14T20:00:00+08:00",
        "aliases": [],
        "tags": [],
        "domains": [],
        "confidence": "unknown",
        "source_ids": [],
        "relations": [{"type": "related_to", "target_id": "missing_object", "reason": "test"}],
    }
    broken_path = repo.root / "vault" / "knowledge" / "claims" / "claim_lint_broken.md"
    broken_path.write_text(
        render_document(broken_metadata, "[[vault/knowledge/claims/missing|missing_object]]"),
        encoding="utf-8",
    )
    orphan_metadata = dict(broken_metadata)
    orphan_metadata.update({
        "id": "concept_lint_orphan",
        "type": "concept",
        "title": "Orphan concept",
        "relations": [],
    })
    orphan_path = repo.root / "vault" / "knowledge" / "concepts" / "concept_lint_orphan.md"
    orphan_path.write_text(render_document(orphan_metadata, "Standalone."), encoding="utf-8")

    result = lint(repo)
    assert result["ok"] is False
    assert any("candidate 哈希不匹配" in issue for issue in result["errors"])
    assert any("claim 缺少 source_ids" in issue for issue in result["errors"])
    assert any("失效 relation" in issue for issue in result["errors"])
    assert any("失效 wikilink ID" in issue for issue in result["errors"])
    assert any("孤立 canonical 页面" in warning for warning in result["warnings"])


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


def test_deferred_proposal_remains_reviewable_and_can_be_approved(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("A deferred candidate can be reviewed later.")
    service = ProposalService(repo)
    proposal = service.compile(captured.source_id)

    service.defer(proposal.proposal_id, "等待补充材料")
    _, deferred, _ = repo.find_document(proposal.proposal_id)
    assert deferred["status"] == "deferred"
    assert deferred["review_reason"] == "等待补充材料"
    assert not (repo.root / proposal.target_path).exists()

    service.approve(proposal.proposal_id)
    _, approved, _ = repo.find_document(proposal.proposal_id)
    assert approved["status"] == "approved"
    assert (repo.root / proposal.target_path).exists()


def test_revision_creates_new_candidate_and_supersedes_original(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("Original evidence excerpt.")
    service = ProposalService(repo)
    original = service.compile(captured.source_id)
    original_candidate_path = repo.root / original.candidate_path
    original_bytes = original_candidate_path.read_bytes()
    candidate, body = read_document(original_candidate_path)
    candidate["updated_at"] = "2026-07-14T19:00:00+08:00"
    revised_file = workspace / "revised-candidate.md"
    revised_file.write_text(
        render_document(candidate, body.replace("Original evidence excerpt.", "Human reviewed claim.")),
        encoding="utf-8",
    )

    revised = service.revise(original.proposal_id, revised_file, "人工澄清主张")
    assert revised.proposal_id != original.proposal_id
    assert original_candidate_path.read_bytes() == original_bytes
    assert (repo.root / revised.candidate_path).read_text(encoding="utf-8") == revised_file.read_text(encoding="utf-8")

    _, old_metadata, _ = repo.find_document(original.proposal_id)
    _, new_metadata, new_body = repo.find_document(revised.proposal_id)
    assert old_metadata["status"] == "superseded"
    assert old_metadata["superseded_by"] == revised.proposal_id
    assert new_metadata["status"] == "pending"
    assert new_metadata["revision_of"] == original.proposal_id
    assert new_metadata["relations"] == [
        {"type": "supersedes", "target_id": original.proposal_id, "reason": "人工澄清主张"}
    ]
    assert "Base → Revised Candidate Diff" in new_body
    with pytest.raises(ValidationError, match="不可批准"):
        service.approve(original.proposal_id)

    service.approve(revised.proposal_id)
    target, target_body = read_document(repo.root / revised.target_path)
    assert target["approved_via"] == revised.proposal_id
    assert "Human reviewed claim." in target_body


def test_explicit_update_proposal_uses_base_snapshot_and_approval(repo: Repository, workspace: Path) -> None:
    _, target_path = create_approved_claim(repo)
    original_bytes = target_path.read_bytes()
    original, body = read_document(target_path)
    candidate = dict(original)
    candidate["status"] = "proposal"
    candidate["proposed_status"] = "contested"
    candidate["updated_at"] = "2026-07-14T18:00:00+08:00"
    candidate_path = workspace / "candidate-update.md"
    candidate_path.write_text(
        render_document(candidate, body.replace("Original canonical claim.", "Revised canonical claim.")),
        encoding="utf-8",
    )

    service = ProposalService(repo)
    proposal = service.propose_update(
        original["id"], candidate_path, "新证据限制了原主张的适用范围"
    )
    proposal_path, metadata, proposal_body = repo.find_document(proposal.proposal_id)

    assert target_path.read_bytes() == original_bytes
    assert metadata["proposal_kind"] == "knowledge_update"
    assert metadata["base_sha256"] == sha256_bytes(original_bytes)
    assert (repo.root / metadata["base_path"]).read_bytes() == original_bytes
    assert "Base → Candidate Diff" in proposal_body
    assert proposal_path.exists()

    service.approve(proposal.proposal_id)
    updated, updated_body = read_document(target_path)
    assert updated["status"] == "contested"
    assert updated["created_at"] == original["created_at"]
    assert updated["approved_via"] == proposal.proposal_id
    assert updated["change_reason"] == "新证据限制了原主张的适用范围"
    assert "Revised canonical claim." in updated_body


def test_update_approval_blocks_concurrent_canonical_edit_and_shows_three_way_diff(
    repo: Repository, workspace: Path
) -> None:
    _, target_path = create_approved_claim(repo, "Base statement.")
    target, body = read_document(target_path)
    candidate = dict(target)
    candidate["status"] = "proposal"
    candidate["updated_at"] = "2026-07-14T18:05:00+08:00"
    candidate_path = workspace / "candidate-concurrent.md"
    candidate_path.write_text(
        render_document(candidate, body.replace("Base statement.", "Agent candidate statement.")),
        encoding="utf-8",
    )
    service = ProposalService(repo)
    proposal = service.propose_update(target["id"], candidate_path, "候选修订")

    human_text = render_document(target, body.replace("Base statement.", "Human concurrent edit."))
    target_path.write_text(human_text, encoding="utf-8")
    shown = service.show(proposal.proposal_id)
    assert "Base → Candidate Diff" in shown
    assert "并发冲突：Base → Current Diff" in shown
    assert "Human concurrent edit." in shown

    with pytest.raises(ValidationError, match="拒绝覆盖"):
        service.approve(proposal.proposal_id)
    assert target_path.read_text(encoding="utf-8") == human_text
    _, pending, _ = repo.find_document(proposal.proposal_id)
    assert pending["status"] == "pending"


def test_conflicted_update_can_be_reproposed_against_current_base(
    repo: Repository, workspace: Path
) -> None:
    _, target_path = create_approved_claim(repo, "Initial statement.")
    target, body = read_document(target_path)
    candidate = dict(target)
    candidate["status"] = "proposal"
    candidate["updated_at"] = "2026-07-14T18:10:00+08:00"
    candidate_path = workspace / "candidate-rebase.md"
    candidate_text = render_document(
        candidate, body.replace("Initial statement.", "Final reviewed statement.")
    )
    candidate_path.write_text(candidate_text, encoding="utf-8")
    service = ProposalService(repo)
    stale = service.propose_update(target["id"], candidate_path, "初次更新")

    target_path.write_text(
        render_document(target, body.replace("Initial statement.", "Intervening edit.")),
        encoding="utf-8",
    )
    fresh = service.propose_update(target["id"], candidate_path, "基于当前版本重新审核")
    assert fresh.proposal_id != stale.proposal_id
    service.approve(fresh.proposal_id)
    updated, updated_body = read_document(target_path)
    assert updated["approved_via"] == fresh.proposal_id
    assert "Final reviewed statement." in updated_body


def test_update_revision_rebases_on_current_canonical(
    repo: Repository, workspace: Path
) -> None:
    _, target_path = create_approved_claim(repo, "Revision base.")
    target, body = read_document(target_path)
    first_candidate = dict(target)
    first_candidate["status"] = "proposal"
    first_path = workspace / "first-update.md"
    first_path.write_text(
        render_document(first_candidate, body.replace("Revision base.", "First proposal.")),
        encoding="utf-8",
    )
    service = ProposalService(repo)
    first = service.propose_update(target["id"], first_path, "初稿")

    current_text = render_document(target, body.replace("Revision base.", "Concurrent human edit."))
    target_path.write_text(current_text, encoding="utf-8")
    revised_candidate = dict(target)
    revised_candidate["status"] = "proposal"
    revised_candidate["updated_at"] = "2026-07-14T19:05:00+08:00"
    revised_path = workspace / "rebased-revision.md"
    revised_path.write_text(
        render_document(revised_candidate, body.replace("Revision base.", "Reviewed final update.")),
        encoding="utf-8",
    )

    revised = service.revise(first.proposal_id, revised_path, "基于 current 重新修订")
    _, metadata, _ = repo.find_document(revised.proposal_id)
    assert (repo.root / metadata["base_path"]).read_text(encoding="utf-8") == current_text
    assert metadata["base_sha256"] == sha256_bytes(target_path.read_bytes())
    service.approve(revised.proposal_id)
    updated, updated_body = read_document(target_path)
    assert updated["approved_via"] == revised.proposal_id
    assert "Reviewed final update." in updated_body


def test_update_candidate_validation_rejects_wrong_identity_and_missing_reason(
    repo: Repository, workspace: Path
) -> None:
    _, target_path = create_approved_claim(repo)
    target, body = read_document(target_path)
    candidate = dict(target)
    candidate["id"] = "claim_wrong"
    candidate["status"] = "proposal"
    candidate_path = workspace / "invalid-candidate.md"
    candidate_path.write_text(render_document(candidate, body), encoding="utf-8")
    service = ProposalService(repo)

    with pytest.raises(ValidationError, match="id/type"):
        service.propose_update(target["id"], candidate_path, "有理由")
    candidate["id"] = target["id"]
    candidate_path.write_text(render_document(candidate, body), encoding="utf-8")
    with pytest.raises(ValidationError, match="必须说明 reason"):
        service.propose_update(target["id"], candidate_path, "  ")


def test_update_approval_rejects_tampered_base_snapshot(
    repo: Repository, workspace: Path
) -> None:
    _, target_path = create_approved_claim(repo, "Protected base.")
    target, body = read_document(target_path)
    candidate = dict(target)
    candidate["status"] = "proposal"
    candidate_path = workspace / "candidate-base-integrity.md"
    candidate_path.write_text(
        render_document(candidate, body.replace("Protected base.", "Proposed update.")),
        encoding="utf-8",
    )
    service = ProposalService(repo)
    proposal = service.propose_update(target["id"], candidate_path, "验证 base 完整性")
    _, metadata, _ = repo.find_document(proposal.proposal_id)
    base_path = repo.root / metadata["base_path"]
    base_path.write_text(base_path.read_text(encoding="utf-8") + "tampered\n", encoding="utf-8")

    with pytest.raises(ValidationError, match="base snapshot 哈希不匹配"):
        service.approve(proposal.proposal_id)
    assert "Protected base." in target_path.read_text(encoding="utf-8")


def test_compile_update_also_captures_optimistic_base(repo: Repository) -> None:
    captured, target_path = create_approved_claim(repo, "Compile update baseline.")
    proposal = ProposalService(repo).compile(captured.source_id)
    _, metadata, _ = repo.find_document(proposal.proposal_id)

    assert proposal.action == "update"
    assert metadata["base_sha256"] == sha256_bytes(target_path.read_bytes())
    assert (repo.root / metadata["base_path"]).read_bytes() == target_path.read_bytes()
    ProposalService(repo).approve(proposal.proposal_id)
    updated, _ = read_document(target_path)
    assert updated["approved_via"] == proposal.proposal_id


def test_propose_update_cli_arguments() -> None:
    args = build_parser().parse_args(
        [
            "propose-update", "claim_example", "--from-file", "candidate.md",
            "--reason", "new evidence",
        ]
    )
    assert args.target_id == "claim_example"
    assert args.candidate_file == "candidate.md"
    assert args.reason == "new evidence"


def test_proposal_review_cli_arguments() -> None:
    deferred = build_parser().parse_args(
        ["proposal", "defer", "proposal_example", "--reason", "wait"]
    )
    assert deferred.proposal_command == "defer"
    assert deferred.reason == "wait"
    revised = build_parser().parse_args(
        [
            "proposal", "revise", "proposal_example", "--from-file", "candidate.md",
            "--reason", "reviewed",
        ]
    )
    assert revised.proposal_command == "revise"
    assert revised.candidate_file == "candidate.md"
    assert revised.reason == "reviewed"


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


@pytest.mark.parametrize("failure_phase", ["prepared", "target_written", "proposal_written"])
def test_approval_journal_recovers_from_injected_phase_failures(
    repo: Repository, failure_phase: str
) -> None:
    captured = CaptureService(repo).capture_text(f"Recovery at {failure_phase}.")
    proposal = ProposalService(repo).compile(captured.source_id)

    def fail_at(phase: str) -> None:
        if phase == failure_phase:
            raise RuntimeError(f"injected failure at {phase}")

    with pytest.raises(RuntimeError, match="injected failure"):
        ProposalService(repo, failure_hook=fail_at).approve(proposal.proposal_id)

    recovery = ApprovalRecoveryManager(repo)
    assert len(recovery.pending()) == 1
    assert doctor(repo)["ok"] is False
    result = recovery.recover_all()
    assert len(result["recovered"]) == 1
    assert result["blocked"] == []
    assert recovery.pending() == []
    target, metadata, _ = repo.find_document(
        read_document(repo.root / proposal.candidate_path)[0]["id"]
    )
    assert target == repo.root / proposal.target_path
    assert metadata["approved_via"] == proposal.proposal_id
    proposal_path, approved, _ = repo.find_document(proposal.proposal_id)
    assert proposal_path.exists()
    assert approved["status"] == "approved"
    assert doctor(repo)["ok"] is True


def test_approval_recovery_is_audit_idempotent_after_index_failure(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    captured = CaptureService(repo).capture_text("Index recovery journal.")
    proposal = ProposalService(repo).compile(captured.source_id)
    real_rebuild = repo.rebuild_index

    def fail_rebuild() -> int:
        raise sqlite3.OperationalError("simulated approval index failure")

    monkeypatch.setattr(repo, "rebuild_index", fail_rebuild)
    with pytest.raises(sqlite3.OperationalError, match="approval index failure"):
        ProposalService(repo).approve(proposal.proposal_id)
    recovery = ApprovalRecoveryManager(repo)
    journal = recovery.pending()[0]
    record = json.loads(journal.read_text(encoding="utf-8"))
    assert record["phase"] == "audit_written"
    operation_id = record["operation_id"]

    monkeypatch.setattr(repo, "rebuild_index", real_rebuild)
    first = recovery.recover_all()
    second = recovery.recover_all()
    assert len(first["recovered"]) == 1
    assert second == {"recovered": [], "blocked": []}
    events = [
        json.loads(line)
        for line in (repo.root / "system" / "logs" / "proposal-events.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    assert sum(event.get("operation_id") == operation_id for event in events) == 1
    assert doctor(repo)["ok"] is True


def test_update_approval_recovery_rolls_forward_from_original_hash(
    repo: Repository, workspace: Path
) -> None:
    _, target_path = create_approved_claim(repo, "Update before crash.")
    target, body = read_document(target_path)
    candidate = dict(target)
    candidate["status"] = "proposal"
    candidate_path = workspace / "candidate-recovery-update.md"
    candidate_path.write_text(
        render_document(candidate, body.replace("Update before crash.", "Update after recovery.")),
        encoding="utf-8",
    )
    proposal = ProposalService(repo).propose_update(
        target["id"], candidate_path, "恢复 update approval"
    )

    def fail_after_target(phase: str) -> None:
        if phase == "target_written":
            raise RuntimeError("update interrupted")

    with pytest.raises(RuntimeError, match="update interrupted"):
        ProposalService(repo, failure_hook=fail_after_target).approve(proposal.proposal_id)
    assert "Update after recovery." in target_path.read_text(encoding="utf-8")
    _, pending, _ = repo.find_document(proposal.proposal_id)
    assert pending["status"] == "pending"

    result = ApprovalRecoveryManager(repo).recover_all()
    assert len(result["recovered"]) == 1
    updated, updated_body = read_document(target_path)
    assert updated["approved_via"] == proposal.proposal_id
    assert "Update after recovery." in updated_body


def test_recovery_blocks_third_state_instead_of_overwriting_human_edit(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Human edit after partial approval.")
    proposal = ProposalService(repo).compile(captured.source_id)

    def fail_after_target(phase: str) -> None:
        if phase == "target_written":
            raise RuntimeError("stop after target")

    with pytest.raises(RuntimeError):
        ProposalService(repo, failure_hook=fail_after_target).approve(proposal.proposal_id)
    target_path = repo.root / proposal.target_path
    human_text = target_path.read_text(encoding="utf-8") + "\nHuman post-crash edit.\n"
    target_path.write_text(human_text, encoding="utf-8")

    result = ApprovalRecoveryManager(repo).recover_all()
    assert result["recovered"] == []
    assert len(result["blocked"]) == 1
    assert "既不是写前也不是写后" in result["blocked"][0]["error"]
    assert target_path.read_text(encoding="utf-8") == human_text
    assert len(ApprovalRecoveryManager(repo).pending()) == 1


def test_recovery_rejects_tampered_journal_payload(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Tampered recovery payload.")
    proposal = ProposalService(repo).compile(captured.source_id)

    def fail_prepared(phase: str) -> None:
        if phase == "prepared":
            raise RuntimeError("stop prepared")

    with pytest.raises(RuntimeError):
        ProposalService(repo, failure_hook=fail_prepared).approve(proposal.proposal_id)
    journal = ApprovalRecoveryManager(repo).pending()[0]
    record = json.loads(journal.read_text(encoding="utf-8"))
    record["target_after_text"] += "tampered"
    journal.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")

    result = ApprovalRecoveryManager(repo).recover_all()
    assert result["recovered"] == []
    assert "payload 哈希不匹配" in result["blocked"][0]["error"]
    assert not (repo.root / proposal.target_path).exists()


def test_recover_cli_arguments() -> None:
    args = build_parser().parse_args(["recover"])
    assert args.command == "recover"
