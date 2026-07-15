from __future__ import annotations

import sqlite3
import shutil
import uuid
import json
from contextlib import closing
from pathlib import Path

import pytest

from global_memory.capture import CaptureService, canonicalize_url
from global_memory.backups import BACKUP_MANIFEST_NAME, RawBackupService
from global_memory.bundle import BundleCompiler, BundleRecoveryManager, BundleReviewService
from global_memory.cli import build_parser, contradiction_audit, doctor, lint
from global_memory.context import ContextPackService
from global_memory.errors import ImmutableContentError, ValidationError
from global_memory.extraction import ExtractionService
from global_memory.markdown import read_document, render_document
from global_memory.proposals import ProposalService
from global_memory.recovery import ApprovalRecoveryManager
from global_memory.raw_store import RawStoreService
from global_memory.repository import Repository, sha256_bytes
from global_memory.works import WorkService


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


def make_text_pdf(pages: list[str]) -> bytes:
    """Create a tiny dependency-free PDF fixture with one text stream per page."""
    objects: list[bytes] = []
    page_ids = [3 + index * 2 for index in range(len(pages))]
    font_id = 3 + len(pages) * 2
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{page_id} 0 R" for page_id in page_ids)
    objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>".encode())
    for index, text in enumerate(pages):
        page_id = page_ids[index]
        content_id = page_id + 1
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>".encode()
        )
        escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        stream = f"BT /F1 12 Tf 72 720 Td ({escaped}) Tj ET".encode()
        objects.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    payload = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for number, obj in enumerate(objects, start=1):
        offsets.append(len(payload))
        payload.extend(f"{number} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    payload.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode())
    payload.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    )
    return bytes(payload)


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


def test_same_pdf_from_url_and_local_file_share_global_object(
    repo: Repository, workspace: Path
) -> None:
    payload = b"%PDF-1.4\nshared-pdf-fixture\n%%EOF"
    remote = CaptureService(repo)._write_source(
        kind="web", original_locator="https://arxiv.org/pdf/2607.11119",
        canonical_locator="https://arxiv.org/pdf/2607.11119", content=payload,
        title="Remote paper", import_method="test", content_type="application/pdf",
    )
    local_path = workspace / "论文副本.pdf"
    local_path.write_bytes(payload)
    local = CaptureService(repo).capture_file(local_path, "local copy")

    assert remote.source_id != local.source_id
    assert remote.content_id == local.content_id
    assert remote.raw_content_path == local.raw_content_path
    assert remote.raw_content_path.endswith(remote.content_id.removeprefix("content_"))
    assert "/objects/sha256/" in remote.raw_content_path
    remote_source = repo.root / remote.source_path
    remote_source.unlink()
    assert (repo.root / local.raw_content_path).read_bytes() == payload


def test_text_and_txt_file_share_global_object(repo: Repository, workspace: Path) -> None:
    text = "中文内容通过两个入口共享对象。"
    pasted = CaptureService(repo).capture_text(text, title="粘贴文本")
    local_path = workspace / "中文资料.txt"
    local_path.write_text(text, encoding="utf-8")
    local = CaptureService(repo).capture_file(local_path)
    assert pasted.source_id != local.source_id
    assert pasted.content_id == local.content_id
    assert pasted.raw_content_path == local.raw_content_path
    _, metadata, _ = repo.find_document(local.source_id)
    assert metadata["original_filename"] == "中文资料.txt"
    assert metadata["display_extension"] == ".txt"


def test_raw_store_migration_is_recoverable_and_idempotent(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("legacy raw migration")
    source_path = repo.root / captured.source_path
    metadata, body = read_document(source_path)
    object_path = repo.root / captured.raw_content_path
    legacy_path = repo.root / "vault/raw/personal-notes/content/legacy.txt"
    legacy_path.parent.mkdir(parents=True, exist_ok=True)
    legacy_path.write_bytes(object_path.read_bytes())
    metadata["raw_content_path"] = repo.rel(legacy_path)
    source_path.write_text(render_document(metadata, body), encoding="utf-8")
    object_path.unlink()

    plan = RawStoreService(repo).plan()
    assert plan.dry_run is True
    assert plan.updated_sources == 1
    assert not object_path.exists()

    calls = 0
    def fail_once(phase: str) -> None:
        nonlocal calls
        if phase == "source_written" and calls == 0:
            calls += 1
            raise RuntimeError("simulated interruption")

    with pytest.raises(RuntimeError, match="interruption"):
        RawStoreService(repo, failure_hook=fail_once).migrate()
    assert RawStoreService(repo).journal_path.exists()
    report = RawStoreService(repo).migrate()
    assert report.updated_sources == 1
    assert report.backup_path
    assert RawStoreService(repo).verify()["ok"] is True
    second = RawStoreService(repo).migrate()
    assert second.updated_sources == 0
    assert second.backup_path is None


def test_html_extraction_removes_navigation_and_script(repo: Repository) -> None:
    html = b"""<html><head><title>Article Title</title><script>secret()</script></head>
    <body><nav>menu noise</nav><main><h1>Useful Heading</h1><p>First paragraph.</p>
    <p>Second paragraph.</p></main><footer>footer noise</footer></body></html>"""
    captured = CaptureService(repo)._write_source(
        kind="web", original_locator="https://example.com/article",
        canonical_locator="https://example.com/article", content=html, title="Article Title",
        import_method="test", content_type="text/html; charset=utf-8",
    )
    result = ExtractionService(repo).extract(captured.source_id)
    _, metadata, body = ExtractionService(repo).find(result.extraction_id)
    assert result.status == "ready"
    assert metadata["input_sha256"] == captured.content_id.removeprefix("content_")
    assert "Useful Heading" in body and "First paragraph" in body
    assert "secret" not in body and "menu noise" not in body and "footer noise" not in body


def test_pdf_extraction_preserves_page_boundaries_and_rebuilds(
    repo: Repository, workspace: Path
) -> None:
    pdf_path = workspace / "多页论文.pdf"
    pdf_path.write_bytes(make_text_pdf(["First page evidence", "Second page evidence"]))
    captured = CaptureService(repo).capture_file(pdf_path)
    service = ExtractionService(repo)
    result = service.extract(captured.source_id)
    extraction_path = repo.root / result.extraction_path
    _, metadata, body = service.find(result.extraction_id)
    assert metadata["page_count"] == 2
    assert "<!-- page: 1 -->" in body and "First page evidence" in body
    assert "<!-- page: 2 -->" in body and "Second page evidence" in body
    raw_before = (repo.root / captured.raw_content_path).read_bytes()
    extraction_path.unlink()
    rebuilt = service.extract(captured.source_id, rebuild=True)
    assert (repo.root / rebuilt.extraction_path).exists()
    assert (repo.root / captured.raw_content_path).read_bytes() == raw_before


def test_chinese_encoding_fallback_and_failed_extraction_preserve_raw(repo: Repository) -> None:
    payload = "中文 GB18030 抽取".encode("gb18030")
    captured = CaptureService(repo)._write_source(
        kind="files", original_locator="C:/资料/中文.txt", canonical_locator="file:c:/资料/中文.txt",
        content=payload, title="中文.txt", import_method="test",
        content_type="text/plain; charset=gb18030", original_filename="中文.txt",
    )
    raw_before = (repo.root / captured.raw_content_path).read_bytes()
    result = ExtractionService(repo).extract(captured.source_id)
    _, metadata, body = ExtractionService(repo).find(result.extraction_id)
    assert "中文 GB18030 抽取" in body
    assert metadata["warnings"]

    binary = CaptureService(repo)._write_source(
        kind="files", original_locator="C:/资料/data.bin", canonical_locator="file:c:/资料/data.bin",
        content=b"\xff\xfe\x00\x81", title="data.bin", import_method="test",
        content_type="application/octet-stream", original_filename="data.bin",
    )
    binary_before = (repo.root / binary.raw_content_path).read_bytes()
    failed = ExtractionService(repo).extract(binary.source_id)
    assert failed.status == "error"
    assert (repo.root / binary.raw_content_path).read_bytes() == binary_before
    assert (repo.root / captured.raw_content_path).read_bytes() == raw_before


def test_multiple_arxiv_captures_enrich_one_auditable_work(
    repo: Repository, workspace: Path
) -> None:
    payload = make_text_pdf(["same paper"])
    remote = CaptureService(repo)._write_source(
        kind="web", original_locator="https://arxiv.org/pdf/2607.11119",
        canonical_locator="https://arxiv.org/pdf/2607.11119", content=payload,
        title="Interface First Robot Control", import_method="test", content_type="application/pdf",
    )
    local_path = workspace / "VIA-paper.pdf"
    local_path.write_bytes(payload)
    local = CaptureService(repo).capture_file(local_path)
    source_before = (repo.root / local.source_path).read_bytes()
    proposal = WorkService(repo).propose(
        [remote.source_id, local.source_id], arxiv_id="2607.11119v1",
        title="Interface First Robot Control", authors=["Researcher A"],
    )
    assert proposal.action == "create"
    assert not (repo.root / proposal.target_path).exists()
    ProposalService(repo).approve(proposal.proposal_id)
    work, _ = read_document(repo.root / proposal.target_path)
    assert work["id"] == "work_arxiv_2607_11119"
    assert work["arxiv_id"] == "2607.11119"
    assert set(work["source_ids"]) == {remote.source_id, local.source_id}
    assert (repo.root / local.source_path).read_bytes() == source_before

    abstract = CaptureService(repo)._write_source(
        kind="web", original_locator="https://arxiv.org/abs/2607.11119",
        canonical_locator="https://arxiv.org/abs/2607.11119", content=b"abstract page",
        title="VIA abstract", import_method="test", content_type="text/plain",
    )
    update = WorkService(repo).propose([abstract.source_id])
    assert update.action == "update"
    _, update_metadata, _ = repo.find_document(update.proposal_id)
    assert update_metadata["target_id"] == work["id"]
    ProposalService(repo).approve(update.proposal_id)
    updated, _ = read_document(repo.root / update.target_path)
    assert abstract.source_id in updated["source_ids"]
    works = [metadata for path in repo.canonical_documents() for metadata, _ in [read_document(path)] if metadata.get("type") == "work"]
    assert len(works) == 1


def test_typed_evidence_quote_translation_table_figure_and_calculation(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Exact quoted evidence and more context.")
    extraction_result = ExtractionService(repo).extract(captured.source_id)
    _, extraction, body = ExtractionService(repo).find(extraction_result.extraction_id)
    original = "Exact quoted evidence"
    start = body.index(original)
    common = {
        "source_id": captured.source_id, "stance": "supports",
        "input_sha256": extraction["input_sha256"], "verification_status": "verified",
        "reason": "测试证据分类。",
    }
    evidence = [
        {**common, "evidence_id": "ev_quote", "evidence_kind": "quote",
         "content_id": captured.content_id, "extraction_id": extraction_result.extraction_id,
         "span_start": start, "span_end": start + len(original), "original_text": original,
         "page": 1},
        {**common, "evidence_id": "ev_para", "evidence_kind": "paraphrase",
         "section": "第 1 段", "interpretation": "证据表达了一个可验证陈述。"},
        {**common, "evidence_id": "ev_translation", "evidence_kind": "translation",
         "section": "第 1 段", "original_text": original,
         "translated_text": "精确引用的证据", "target_language": "zh-CN"},
        {**common, "evidence_id": "ev_table", "evidence_kind": "table_value",
         "page": 2, "table": "Table 1", "row": "success", "column": "method A",
         "value": 97.8, "unit": "%"},
        {**common, "evidence_id": "ev_figure", "evidence_kind": "figure",
         "page": 3, "figure": "Figure 2", "interpretation": "曲线在末段上升。"},
        {**common, "evidence_id": "ev_calc", "evidence_kind": "calculation",
         "input_evidence_ids": ["ev_table"], "calculation_method": "97.8 / 2",
         "result": 48.9, "unit": "%"},
    ]
    metadata = {
        "id": "claim_typed_evidence", "type": "claim", "status": "proposal",
        "title": "Typed evidence", "created_at": "2026-07-15T10:00:00+08:00",
        "updated_at": "2026-07-15T10:00:00+08:00", "aliases": [], "tags": [],
        "domains": [], "confidence": "medium", "source_ids": [captured.source_id],
        "relations": [], "evidence": evidence, "applicability": ["test"],
        "uncertainty": "test only",
    }
    candidate = repo.root / "data/derived/typed-evidence.md"
    candidate.write_text(render_document(metadata, "typed evidence"), encoding="utf-8")
    repo._validate_metadata(metadata, candidate)

    evidence[1]["verification_status"] = "verbatim"
    with pytest.raises(ValidationError, match="paraphrase"):
        repo._validate_metadata(metadata, candidate)
    evidence[1]["verification_status"] = "verified"
    evidence[0]["original_text"] = "not the extraction span"
    with pytest.raises(ValidationError, match="quote"):
        repo._validate_metadata(metadata, candidate)


def test_compile_bundle_isolated_until_item_level_atomic_review(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Concept: Materialized memory view\n\n"
        "Claim: A derived view can be rebuilt from its source.\n\n"
        "Question: When should the view be refreshed?",
        title="Bundle fixture",
    )
    bundle = BundleCompiler(repo).compile(captured.source_id)
    assert bundle.item_count == 3
    proposal, body = read_document(repo.root / bundle.proposal_path)
    assert proposal["proposal_kind"] == "compile_bundle"
    assert proposal["existing_context"] == []
    assert "Items and diffs" in body
    for item in proposal["bundle_items"]:
        assert not (repo.root / item["target_path"]).exists()

    review = BundleReviewService(repo)
    concept_item = next(item["item_id"] for item in proposal["bundle_items"] if item["object_type"] == "concept")
    approved = review.approve(bundle.proposal_id, [concept_item])
    assert approved["remaining_items"] == 2
    updated_proposal, _ = read_document(repo.root / bundle.proposal_path)
    concept = next(item for item in updated_proposal["bundle_items"] if item["item_id"] == concept_item)
    assert concept["decision"] == "approved"
    assert (repo.root / concept["target_path"]).exists()
    question_item = next(item["item_id"] for item in updated_proposal["bundle_items"] if item["object_type"] == "question")
    review.reject(bundle.proposal_id, [question_item], "暂不保留该问题")
    final_review = review.approve(bundle.proposal_id)
    assert final_review["remaining_items"] == 0
    final_proposal, _ = read_document(repo.root / bundle.proposal_path)
    assert final_proposal["status"] == "approved"
    assert {item["decision"] for item in final_proposal["bundle_items"]} == {"approved", "rejected"}
    assert lint(repo)["ok"] is True


def test_bundle_compiler_updates_existing_concept_instead_of_duplicate(repo: Repository) -> None:
    first = CaptureService(repo).capture_text("Concept: Shared mechanism", title="First")
    first_bundle = BundleCompiler(repo).compile(first.source_id)
    BundleReviewService(repo).approve(first_bundle.proposal_id)
    second = CaptureService(repo).capture_text("Concept: Shared mechanism", title="Second")
    second_bundle = BundleCompiler(repo).compile(second.source_id)
    second_proposal, _ = read_document(repo.root / second_bundle.proposal_path)
    assert second_proposal["existing_context"]
    assert second_proposal["bundle_items"][0]["action"] == "update"
    BundleReviewService(repo).approve(second_bundle.proposal_id)
    concepts = [
        metadata for path in repo.canonical_documents()
        for metadata, _ in [read_document(path)] if metadata.get("type") == "concept"
    ]
    assert len(concepts) == 1
    assert set(concepts[0]["source_ids"]) == {first.source_id, second.source_id}


def test_bundle_approval_recovers_all_targets_after_interruption(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Concept: Recovery concept\n\nClaim: Recovery preserves every selected item.",
        title="Recovery bundle",
    )
    bundle = BundleCompiler(repo).compile(captured.source_id)

    def fail_after_targets(phase: str) -> None:
        if phase == "targets_written":
            raise RuntimeError("simulated bundle interruption")

    with pytest.raises(RuntimeError, match="interruption"):
        BundleReviewService(repo, failure_hook=fail_after_targets).approve(bundle.proposal_id)
    assert BundleRecoveryManager(repo).pending()
    recovered = BundleRecoveryManager(repo).recover_all()
    assert len(recovered["recovered"]) == 1 and not recovered["blocked"]
    proposal, _ = read_document(repo.root / bundle.proposal_path)
    assert proposal["status"] == "approved"
    assert all((repo.root / item["target_path"]).exists() for item in proposal["bundle_items"])


def test_bundle_provider_output_is_schema_validated(repo: Repository) -> None:
    class InvalidProvider:
        name = "invalid-test-provider"
        def compile(self, source, extraction, text, existing_context, schema):
            return [{"object_type": "made_up", "title": "bad", "body": "bad"}]

    captured = CaptureService(repo).capture_text("provider input")
    with pytest.raises(ValidationError, match="object_type"):
        BundleCompiler(repo, InvalidProvider()).compile(captured.source_id)


def test_bundle_item_revision_preserves_old_candidate(repo: Repository, workspace: Path) -> None:
    captured = CaptureService(repo).capture_text("Concept: Revisable concept")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    proposal, _ = read_document(repo.root / bundle.proposal_path)
    item = proposal["bundle_items"][0]
    old_path = repo.root / item["candidate_path"]
    old_bytes = old_path.read_bytes()
    candidate, body = read_document(old_path)
    candidate["updated_at"] = "2026-07-15T20:00:00+08:00"
    revised_file = workspace / "revised-bundle-item.md"
    revised_file.write_text(render_document(candidate, body + "\nHuman clarification."), encoding="utf-8")
    result = BundleReviewService(repo).revise_item(
        bundle.proposal_id, item["item_id"], revised_file, "补充人工澄清"
    )
    assert old_path.read_bytes() == old_bytes
    assert (repo.root / result["candidate_path"]).exists()
    updated, _ = read_document(repo.root / bundle.proposal_path)
    assert updated["bundle_items"][0]["revision_history"][0]["candidate_path"] == item["candidate_path"]
    BundleReviewService(repo).approve(bundle.proposal_id)
    assert lint(repo)["ok"] is True


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


def test_context_pack_is_read_only_budgeted_and_traceable(repo: Repository) -> None:
    captured, target_path = create_approved_claim(
        repo, "Context pack keeps the source chain visible for later review."
    )
    before = {
        repo.rel(path): path.read_bytes()
        for path in list(repo.all_indexed_documents()) + list(repo.proposal_documents())
    }

    pack = ContextPackService(repo).build("Context pack", token_budget=400).as_dict()

    assert pack["estimated_tokens"] <= pack["token_budget"]
    assert pack["items"]
    assert any(item["id"] == read_document(target_path)[0]["id"] for item in pack["items"])
    assert all(item["document_sha256"] and item["source_ids"] for item in pack["items"])
    assert all("全文检索命中" in item["selection_reason"] for item in pack["items"])
    after = {
        repo.rel(path): path.read_bytes()
        for path in list(repo.all_indexed_documents()) + list(repo.proposal_documents())
    }
    assert after == before
    assert captured.source_id in {source_id for item in pack["items"] for source_id in item["source_ids"]}


def test_context_pack_rejects_invalid_token_budget(repo: Repository) -> None:
    CaptureService(repo).capture_text("Context budget validation.")
    with pytest.raises(ValidationError, match="token budget"):
        ContextPackService(repo).build("Context", token_budget=127)


def test_context_pack_uses_only_the_latest_source_in_a_family(repo: Repository) -> None:
    first = capture_web_bytes(
        repo, "https://example.com/context-history", b"shared context version one"
    )
    second = capture_web_bytes(
        repo, "https://example.com/context-history", b"shared context version two", refresh=True
    )

    pack = ContextPackService(repo).build("shared context", token_budget=400).as_dict()

    selected_source_ids = {item["id"] for item in pack["items"] if item["type"] == "source"}
    assert selected_source_ids == {second.source_id}
    assert any(item["id"] == first.source_id and "旧版本" in item["reason"] for item in pack["omitted"])


def test_context_pack_excludes_archived_canonical_knowledge(repo: Repository) -> None:
    captured, target_path = create_approved_claim(repo, "Archived quickstart fixture knowledge.")
    metadata, body = read_document(target_path)
    metadata["status"] = "archived"
    target_path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    pack = ContextPackService(repo).build("Archived quickstart", token_budget=400).as_dict()

    target_id = str(metadata["id"])
    assert target_id not in {item["id"] for item in pack["items"]}
    assert captured.source_id not in {item["id"] for item in pack["items"]}
    assert any(
        item["id"] == target_id and "已归档" in item["reason"]
        for item in pack["omitted"]
    )
    assert any(
        item["id"] == captured.source_id and "仅被已归档" in item["reason"]
        for item in pack["omitted"]
    )


def test_lint_accepts_valid_truth_and_proposal_chain(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Lint checks provenance and proposal integrity.")
    proposal = ProposalService(repo).compile(captured.source_id)
    result = lint(repo)

    assert result["ok"] is True
    assert result["errors"] == []
    assert result["warnings"] == []
    assert result["checked_documents"] == 3
    assert proposal.proposal_id


def test_lint_accepts_approved_target_moved_to_archive(repo: Repository) -> None:
    _, target_path = create_approved_claim(repo, "Disposable fixture knowledge.")
    archived_path = repo.root / "vault" / "archive" / target_path.name
    archived_path.parent.mkdir(parents=True, exist_ok=True)
    metadata, body = read_document(target_path)
    metadata["status"] = "archived"
    archived_path.write_text(render_document(metadata, body), encoding="utf-8")
    target_path.unlink()

    result = lint(repo)

    assert result["ok"] is True
    assert result["errors"] == []


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


def test_raw_backup_is_incremental_verifiable_and_restorable(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("Raw backup recovery drill.")
    backup_directory = workspace / "external-raw-backup"
    service = RawBackupService(repo)

    first = service.backup(backup_directory)
    assert first.conflicts == []
    assert len(first.copied) == 2
    assert (backup_directory / BACKUP_MANIFEST_NAME).is_file()
    assert service.verify(backup_directory)["ok"] is True

    second = service.backup(backup_directory)
    assert second.copied == []
    assert sorted(second.skipped) == sorted(first.copied)

    source_path = repo.root / captured.source_path
    raw_path = repo.root / captured.raw_content_path
    source_path.unlink()
    raw_path.unlink()
    planned = service.restore(backup_directory)
    assert planned["ok"] is True
    assert planned["dry_run"] is True
    assert sorted(planned["restored"]) == sorted(first.copied)
    assert not source_path.exists()

    restored = service.restore(backup_directory, apply=True)
    assert restored["ok"] is True
    assert restored["dry_run"] is False
    assert sorted(restored["restored"]) == sorted(first.copied)
    assert source_path.exists()
    assert raw_path.exists()
    assert doctor(repo)["ok"] is True


def test_raw_backup_restore_refuses_to_overwrite_conflicting_local_file(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("Original backup payload.")
    backup_directory = workspace / "external-raw-backup-conflict"
    service = RawBackupService(repo)
    service.backup(backup_directory)
    raw_path = repo.root / captured.raw_content_path
    raw_path.write_text("Local conflicting payload.", encoding="utf-8")

    result = service.restore(backup_directory, apply=True)
    assert result["ok"] is False
    assert result["conflicts"] == [captured.raw_content_path]
    assert raw_path.read_text(encoding="utf-8") == "Local conflicting payload."


def test_raw_backup_cli_arguments() -> None:
    manifest = build_parser().parse_args(["backup", "manifest", "--output", "manifest.json"])
    assert manifest.backup_command == "manifest"
    assert manifest.output == "manifest.json"
    restored = build_parser().parse_args(["backup", "restore", "D:/backup", "--apply"])
    assert restored.backup_command == "restore"
    assert restored.directory == "D:/backup"
    assert restored.apply is True


def test_model_candidate_import_records_reproducibility_and_requires_approval(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("Model input must remain locally owned.")
    candidate_metadata = {
        "id": "claim_model_candidate",
        "type": "claim",
        "status": "proposal",
        "title": "模型生成的待确认主张",
        "created_at": "2026-07-14T21:00:00+08:00",
        "updated_at": "2026-07-14T21:00:00+08:00",
        "aliases": [],
        "tags": [],
        "domains": [],
        "confidence": "low",
        "source_ids": [captured.source_id],
        "evidence": [
            {
                "source_id": captured.source_id,
                "location": "第 1 段",
                "excerpt": "Model input must remain locally owned.",
                "stance": "supports",
                "reason": "来源直接陈述本地所有权要求。",
            }
        ],
        "applicability": ["仅适用于用户明确提供的本地资料。"],
        "uncertainty": "模型输出未经独立事实核验。",
        "relations": [
            {"type": "derived_from", "target_id": captured.source_id, "reason": "模型基于输入来源提出"}
        ],
    }
    candidate_file = workspace / "model-candidate.md"
    candidate_file.write_text(
        render_document(candidate_metadata, "模型候选内容，等待人工批准。"), encoding="utf-8"
    )
    prompt_file = workspace / "prompt.md"
    prompt_file.write_text("从来源提取低置信度主张。", encoding="utf-8")
    service = ProposalService(repo)

    proposal = service.propose_model_candidate(
        captured.source_id, candidate_file, "local-test", "test-model-1", "v1",
        "模型输出未经事实核验。", "导入外部模型结果供审阅", prompt_file,
    )
    assert proposal.action == "create"
    assert not (repo.root / proposal.target_path).exists()
    _, metadata, body = repo.find_document(proposal.proposal_id)
    model_run = metadata["model_run"]
    assert metadata["proposal_kind"] == "model_candidate"
    assert model_run["provider"] == "local-test"
    assert model_run["model"] == "test-model-1"
    assert model_run["prompt_version"] == "v1"
    assert model_run["prompt_sha256"] == sha256_bytes(prompt_file.read_bytes())
    assert model_run["input_source_id"] == captured.source_id
    assert model_run["input_sha256"] == captured.content_id.removeprefix("content_")
    assert model_run["uncertainty"] == "模型输出未经事实核验。"
    assert "不调用 provider" in body
    assert lint(repo)["ok"] is True

    service.approve(proposal.proposal_id)
    approved, approved_body = read_document(repo.root / proposal.target_path)
    assert approved["approved_via"] == proposal.proposal_id
    assert "模型候选内容" in approved_body


def test_validated_claim_can_publish_provisional_then_promote(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("Evidence supports a bounded claim.")
    metadata = {
        "id": "claim_provisional_flow", "type": "claim", "status": "proposal",
        "title": "可分级发布的主张", "created_at": "2026-07-15T10:00:00+08:00",
        "updated_at": "2026-07-15T10:00:00+08:00", "aliases": [], "tags": [],
        "domains": ["knowledge-management"], "confidence": "medium",
        "source_ids": [captured.source_id],
        "evidence": [{
            "source_id": captured.source_id, "location": "第 1 段",
            "excerpt": "Evidence supports a bounded claim.", "stance": "supports",
            "reason": "来源直接支持该限定主张。",
        }],
        "applicability": ["仅限该来源明确描述的范围。"],
        "uncertainty": "尚未经过用户人工确认。",
        "relations": [{
            "type": "derived_from", "target_id": captured.source_id,
            "reason": "从该来源提取",
        }],
    }
    candidate = workspace / "provisional-candidate.md"
    candidate.write_text(render_document(metadata, "bounded searchable claim"), encoding="utf-8")
    proposal = ProposalService(repo).propose_model_candidate(
        captured.source_id, candidate, "cursor", "test-model", "v1",
        "未经人工确认", "批量导入", None,
    )

    service = ProposalService(repo)
    target = service.publish(proposal.proposal_id)
    published, _ = read_document(repo.root / target)
    assert published["status"] == "provisional"
    assert published["published_via"] == proposal.proposal_id
    assert "approved_via" not in published
    _, proposal_metadata, _ = repo.find_document(proposal.proposal_id)
    assert proposal_metadata["status"] == "published"
    result = next(item for item in repo.search("bounded") if item.id == metadata["id"])
    assert result.status == "provisional"
    pack = ContextPackService(repo).build("bounded", 512).as_dict()
    item = next(item for item in pack["items"] if item["id"] == metadata["id"])
    assert item["knowledge_status"] == "provisional"

    service.promote(metadata["id"], "用户核对原文后确认")
    confirmed, _ = read_document(repo.root / target)
    assert confirmed["status"] == "confirmed"
    assert confirmed["confirmed_by"] == "human-cli"


def test_provisional_publish_blocks_conflicting_or_high_risk_claim(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("A disputed investment claim.")
    metadata = {
        "id": "claim_blocked_provisional", "type": "claim", "status": "proposal",
        "title": "高风险主张", "created_at": "2026-07-15T10:00:00+08:00",
        "updated_at": "2026-07-15T10:00:00+08:00", "aliases": [],
        "tags": ["investment"], "domains": [], "confidence": "medium",
        "source_ids": [captured.source_id],
        "evidence": [{
            "source_id": captured.source_id, "location": "第 1 段",
            "excerpt": "A disputed investment claim.", "stance": "supports",
            "reason": "来源提出该主张。",
        }],
        "applicability": ["测试"], "uncertainty": "高风险且未经确认。",
        "relations": [],
    }
    candidate = workspace / "blocked-candidate.md"
    candidate.write_text(render_document(metadata, "blocked"), encoding="utf-8")
    proposal = ProposalService(repo).propose_model_candidate(
        captured.source_id, candidate, "cursor", "test-model", "v1", "高风险", "测试", None,
    )
    with pytest.raises(ValidationError, match="高风险"):
        ProposalService(repo).publish(proposal.proposal_id)
    assert not (repo.root / proposal.target_path).exists()


def test_cli_exposes_publish_and_promote_commands() -> None:
    published = build_parser().parse_args(["proposal", "publish", "proposal_123"])
    assert published.proposal_command == "publish"
    promoted = build_parser().parse_args(["promote", "claim_123", "--reason", "reviewed"])
    assert promoted.target_id == "claim_123"


def test_model_candidate_requires_input_source_provenance(repo: Repository, workspace: Path) -> None:
    captured = CaptureService(repo).capture_text("Model provenance validation.")
    candidate_metadata = {
        "id": "claim_model_invalid",
        "type": "claim",
        "status": "proposal",
        "title": "Missing source",
        "created_at": "2026-07-14T21:05:00+08:00",
        "updated_at": "2026-07-14T21:05:00+08:00",
        "aliases": [], "tags": [], "domains": [], "confidence": "unknown",
        "source_ids": [], "relations": [],
    }
    candidate_file = workspace / "model-invalid.md"
    candidate_file.write_text(render_document(candidate_metadata, "invalid"), encoding="utf-8")
    with pytest.raises(ValidationError, match="source_ids"):
        ProposalService(repo).propose_model_candidate(
            captured.source_id, candidate_file, "provider", "model", "v1", "unknown", "reason"
        )


def test_model_propose_cli_arguments() -> None:
    args = build_parser().parse_args(
        [
            "model-propose", "source_example", "--candidate", "candidate.md",
            "--provider", "local", "--model", "model-x", "--prompt-version", "v1",
            "--prompt-file", "prompt.md", "--uncertainty", "unknown", "--reason", "review",
        ]
    )
    assert args.source_id == "source_example"
    assert args.candidate_file == "candidate.md"
    assert args.provider == "local"
    assert args.prompt_file == "prompt.md"


def test_claim_evidence_schema_is_emitted_and_validated(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Evidence must preserve its direction.")
    proposal = ProposalService(repo).compile(captured.source_id)
    candidate_path = repo.root / proposal.candidate_path
    candidate, _ = read_document(candidate_path)
    evidence = candidate["evidence"]
    assert evidence[0]["source_id"] == captured.source_id
    assert evidence[0]["stance"] == "context"
    assert candidate["applicability"] == []
    assert "尚未经过模型解释" in candidate["uncertainty"]

    candidate["evidence"][0]["stance"] = "made_up"
    with pytest.raises(ValidationError, match="evidence stance"):
        repo._validate_metadata(candidate, candidate_path)


def test_contradiction_audit_reports_evidence_and_relation_without_mutation(repo: Repository) -> None:
    supporting = CaptureService(repo).capture_text("Evidence supporting the claim.")
    opposing = CaptureService(repo).capture_text("Evidence contradicting the claim.")
    shared = {
        "status": "confirmed",
        "created_at": "2026-07-14T22:00:00+08:00",
        "updated_at": "2026-07-14T22:00:00+08:00",
        "aliases": [], "tags": [], "domains": [], "confidence": "low",
        "applicability": [], "uncertainty": "需要人工判断证据权重。",
    }
    first_metadata = {
        **shared,
        "id": "claim_audit_first",
        "type": "claim",
        "title": "存在内部正反证据的主张",
        "source_ids": [supporting.source_id, opposing.source_id],
        "evidence": [
            {
                "source_id": supporting.source_id, "location": "第 1 段",
                "excerpt": "Evidence supporting the claim.", "stance": "supports", "reason": "明确支持。",
            },
            {
                "source_id": opposing.source_id, "location": "第 1 段",
                "excerpt": "Evidence contradicting the claim.", "stance": "contradicts", "reason": "明确反对。",
            },
        ],
        "relations": [],
    }
    second_metadata = {
        **shared,
        "id": "claim_audit_second",
        "type": "claim",
        "title": "显式反对另一主张的主张",
        "source_ids": [opposing.source_id],
        "evidence": [
            {
                "source_id": opposing.source_id, "location": "第 1 段",
                "excerpt": "Evidence contradicting the claim.", "stance": "context", "reason": "作为关系的背景。",
            }
        ],
        "relations": [
            {"type": "contradicts", "target_id": "claim_audit_first", "reason": "结论不能同时成立。"}
        ],
    }
    first_path = repo.root / "vault" / "knowledge" / "claims" / "claim_audit_first.md"
    second_path = repo.root / "vault" / "knowledge" / "claims" / "claim_audit_second.md"
    first_path.write_text(render_document(first_metadata, "First claim."), encoding="utf-8")
    second_path.write_text(render_document(second_metadata, "Second claim."), encoding="utf-8")
    repo.rebuild_index()
    first_before = first_path.read_bytes()
    second_before = second_path.read_bytes()

    result = contradiction_audit(repo)
    assert result["ok"] is True
    assert result["claim_count"] == 2
    assert result["evidence_conflicts"][0]["claim_id"] == "claim_audit_first"
    assert result["relation_contradictions"] == [
        {
            "source_claim_id": "claim_audit_second",
            "source_path": "vault/knowledge/claims/claim_audit_second.md",
            "target_claim_id": "claim_audit_first",
            "target_path": "vault/knowledge/claims/claim_audit_first.md",
            "source_status": "confirmed",
            "target_status": "confirmed",
            "reason": "结论不能同时成立。",
        }
    ]
    assert first_path.read_bytes() == first_before
    assert second_path.read_bytes() == second_before


def test_contradiction_audit_cli_arguments() -> None:
    args = build_parser().parse_args(["audit", "contradictions"])
    assert args.audit_command == "contradictions"


def test_synthesis_proposal_preserves_inputs_and_requires_approval(repo: Repository) -> None:
    first_capture, first_path = create_approved_claim(repo, "First synthesis input.")
    second_capture, second_path = create_approved_claim(repo, "Second synthesis input.")
    first, _ = read_document(first_path)
    second, _ = read_document(second_path)
    service = ProposalService(repo)

    proposal = service.synthesize([first["id"], second["id"]])
    assert proposal.action == "create"
    assert not (repo.root / proposal.target_path).exists()
    _, metadata, body = repo.find_document(proposal.proposal_id)
    assert metadata["proposal_kind"] == "deterministic_synthesis"
    assert [item["id"] for item in metadata["input_claims"]] == [first["id"], second["id"]]
    assert first_capture.source_id in metadata["source_ids"]
    assert second_capture.source_id in metadata["source_ids"]
    assert "不自动裁决矛盾" in body
    assert lint(repo)["ok"] is True

    service.approve(proposal.proposal_id)
    synthesis, synthesis_body = read_document(repo.root / proposal.target_path)
    assert synthesis["type"] == "synthesis"
    assert synthesis["approved_via"] == proposal.proposal_id
    assert first["id"] in synthesis_body
    assert second["id"] in synthesis_body


def test_synthesis_approval_rejects_changed_input_claim(repo: Repository) -> None:
    _, first_path = create_approved_claim(repo, "Mutable synthesis input.")
    _, second_path = create_approved_claim(repo, "Stable synthesis input.")
    first, first_body = read_document(first_path)
    second, _ = read_document(second_path)
    proposal = ProposalService(repo).synthesize([first["id"], second["id"]])

    first_path.write_text(
        render_document(first, first_body.replace("Mutable synthesis input.", "Human changed input.")),
        encoding="utf-8",
    )
    with pytest.raises(ValidationError, match="输入 claim 在 proposal 创建后已变化"):
        ProposalService(repo).approve(proposal.proposal_id)
    assert not (repo.root / proposal.target_path).exists()


def test_synthesize_cli_arguments() -> None:
    args = build_parser().parse_args(["synthesize", "claim_one", "claim_two"])
    assert args.claim_ids == ["claim_one", "claim_two"]


def test_discovery_proposal_reports_explainable_shared_source_without_writing_relation(
    repo: Repository
) -> None:
    captured, first_path = create_approved_claim(repo, "Shared source for discovery.")
    first, _ = read_document(first_path)
    second_metadata = {
        "id": "claim_discovery_second",
        "type": "claim",
        "status": "confirmed",
        "title": "来自同一来源的另一主张",
        "created_at": "2026-07-14T23:00:00+08:00",
        "updated_at": "2026-07-14T23:00:00+08:00",
        "aliases": [], "tags": [], "domains": [], "confidence": "unknown",
        "source_ids": [captured.source_id], "relations": [],
    }
    second_path = repo.root / "vault" / "knowledge" / "claims" / "claim_discovery_second.md"
    second_path.write_text(render_document(second_metadata, "Second discovery claim."), encoding="utf-8")
    repo.rebuild_index()
    first_before = first_path.read_bytes()
    second_before = second_path.read_bytes()
    first_relations_before = read_document(first_path)[0]["relations"]
    second_relations_before = read_document(second_path)[0]["relations"]

    result = ProposalService(repo).discover(first["id"])
    assert result.candidate_count == 1
    assert result.proposal_id
    _, metadata, body = repo.find_document(result.proposal_id)
    assert metadata["proposal_kind"] == "relation_discovery"
    assert metadata["discovery_candidates"][0]["id"] == "claim_discovery_second"
    assert metadata["discovery_candidates"][0]["signals"]["shared_source_ids"] == [captured.source_id]
    assert "共享来源" in body
    assert lint(repo)["ok"] is True

    approved_path = ProposalService(repo).approve(result.proposal_id)
    assert approved_path == result.proposal_path
    _, approved, _ = repo.find_document(result.proposal_id)
    assert approved["status"] == "approved"
    assert first_path.read_bytes() == first_before
    assert second_path.read_bytes() == second_before
    assert read_document(first_path)[0]["relations"] == first_relations_before
    assert read_document(second_path)[0]["relations"] == second_relations_before


def test_discovery_approval_rejects_changed_candidate_input(repo: Repository) -> None:
    captured, first_path = create_approved_claim(repo, "Discovery stale seed.")
    first, first_body = read_document(first_path)
    second_metadata = {
        "id": "claim_discovery_stale_second",
        "type": "claim", "status": "confirmed", "title": "Discovery stale candidate",
        "created_at": "2026-07-14T23:05:00+08:00", "updated_at": "2026-07-14T23:05:00+08:00",
        "aliases": [], "tags": [], "domains": [], "confidence": "unknown",
        "source_ids": [captured.source_id], "relations": [],
    }
    second_path = repo.root / "vault" / "knowledge" / "claims" / "claim_discovery_stale_second.md"
    second_path.write_text(render_document(second_metadata, "Stale candidate."), encoding="utf-8")
    repo.rebuild_index()
    proposal = ProposalService(repo).discover(first["id"])
    first_path.write_text(
        render_document(first, first_body.replace("Discovery stale seed.", "Changed after discovery.")),
        encoding="utf-8",
    )
    with pytest.raises(ValidationError, match="输入 claim 在 proposal 创建后已变化"):
        ProposalService(repo).approve(proposal.proposal_id)


def test_discover_cli_arguments() -> None:
    args = build_parser().parse_args(["discover", "claim_seed"])
    assert args.seed_id == "claim_seed"


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


def test_context_cli_arguments() -> None:
    args = build_parser().parse_args(["context", "long-term memory", "--token-budget", "640"])
    assert args.command == "context"
    assert args.query == "long-term memory"
    assert args.token_budget == 640


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
