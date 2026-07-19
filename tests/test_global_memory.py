from __future__ import annotations

import sqlite3
import shutil
import uuid
import json
import sys
from contextlib import closing
from pathlib import Path

import pytest
import global_memory.research as research_module

from global_memory.capture import CaptureService, canonicalize_url
from global_memory.backups import BACKUP_MANIFEST_NAME, RawBackupService
from global_memory.bundle import BundleCompiler, BundleRecoveryManager, BundleReviewService, JsonBundleProvider
from global_memory.atomicity import AtomicClaimInspector
from global_memory.cli import build_parser, contradiction_audit, doctor, lint, run
from global_memory.context import ContextPackService
from global_memory.cognition import (
    DailyDreamService, InputEpisodeService, ReflectionService, SynthesisService,
    WeeklyDreamService,
)
from global_memory.distillation import CorpusDistillationService
from global_memory.errors import ImmutableContentError, ValidationError
from global_memory.extraction import ExtractionService
from global_memory.followups import FollowupService
from global_memory.lifecycle import SourceAnnotationService, SourceLifecycleService
from global_memory.markdown import read_document, render_document
from global_memory.maintenance import MaintenanceService
from global_memory.memory import ExceptionService, WorkingMemoryService
from global_memory.governance import PromotionService, TrustedPromotionRecoveryManager
from global_memory.consolidation import ConsolidationReceiptService, ConsolidationService, DriftAuditService, ProposalGateMigration, REQUIRED_RECEIPT_CHECKS, WorkingQualityMigration
from global_memory.epistemics import truth_layer
from global_memory.evolution import KnowledgeEvolutionService
from global_memory.migration import EpistemicStatusMigration, TrustPolicyRequalificationMigration, TrustRequalificationRepairMigration
from global_memory.metrics import ProjectMetricsService
from global_memory.mcp_server import MCPApplication, ReadOnlyMemoryTools, serve_http
from global_memory.obsidian import ObsidianViewService
from global_memory.proposals import ProposalService
from global_memory.receipts import ReceiptService
from global_memory.recovery import ApprovalRecoveryManager
from global_memory.raw_store import RawStoreService
from global_memory.quality import SourceQualityService, normalize_primary_locator
from global_memory.review import SourceBundleReviewService
from global_memory.research import (
    ActivationService, ResearchAnnotationService, ResearchDigestService,
    ResearchMapService, ResearchRouterService,
)
from global_memory.semantic import SemanticDistillationQueue
from global_memory.runs import BatchArtifactMigrator, RunArtifactService
from global_memory.repository import Repository, sha256_bytes
from global_memory.triage import DailyTriageService
from global_memory.works import WorkService


def write_research_fixture_object(
    repo: Repository, object_id: str, object_type: str, title: str, body: str,
    *, relations: list[dict[str, str]] | None = None, domains: list[str] | None = None,
) -> Path:
    root = "action/projects" if object_type == "project" else "frontier/questions"
    path = repo.root / "vault" / root / f"{object_id}.md"
    timestamp = "2026-07-18T12:00:00+08:00"
    metadata = {
        "id": object_id, "type": object_type, "status": "confirmed", "title": title,
        "created_at": timestamp, "updated_at": timestamp, "aliases": [], "tags": [],
        "domains": domains or [], "confidence": "unknown", "source_ids": [],
        "relations": relations or [],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    return path


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


def test_daily_triage_defaults_to_capture_only_and_is_incremental(repo: Repository):
    captured = capture_web_bytes(repo, "https://example.com/triage", b"Useful article body. " * 20)

    first = DailyTriageService(repo).run([captured.source_id])

    assert first["mode"] == "capture-only"
    assert first["results"][0]["action"] == "capture_only"
    assert first["results"][0]["state"] == "compile_pending"
    assert first["results"][0]["proposal_id"] is None
    assert ProposalService(repo).list("pending") == []

    second = DailyTriageService(repo).run([captured.source_id])
    assert second["results"][0]["action"] == "already_prepared"
    assert second["results"][0]["extraction_created"] is False
    assert second["results"][0]["quality_checked"] is False

    automatic = DailyTriageService(repo).run()
    assert automatic["selected"] == 0
    assert automatic["remaining_inbox"] == 1
    assert automatic["remaining_unprepared"] == 0


def test_daily_triage_explicit_web_marker_stays_source_only(repo: Repository):
    captured = capture_web_bytes(
        repo,
        "https://example.com/important",
        b"Claim: Explicitly selected knowledge. " + b"Supporting article context. " * 10,
    )

    result = DailyTriageService(repo).run([captured.source_id], compile_selected=True)

    assert result["mode"] == "compile-selected"
    assert result["results"][0]["action"] == "proposal_created"
    assert result["results"][0]["proposal_id"]
    assert result["results"][0]["state"] == "completed"
    proposal_path, proposal, _ = repo.find_document(result["results"][0]["proposal_id"])
    assert proposal_path.exists()
    assert proposal["compile_disposition"] == "source_only"


def test_triage_cli_defaults_are_cost_bounded():
    args = build_parser().parse_args(["triage"])

    assert args.source_ids == []
    assert args.limit == 25
    assert args.compile_selected is False


def create_approved_claim(repo: Repository, text: str = "Original canonical claim."):
    captured = CaptureService(repo).capture_text(text, title="Canonical claim source")
    service = ProposalService(repo)
    proposal = service.compile(captured.source_id)
    target = service.approve(proposal.proposal_id)
    return captured, repo.root / target


@pytest.mark.parametrize(
    ("content", "availability", "quality"),
    [
        ("该内容已被发布者删除", "deleted", "boilerplate_only"),
        ("请先登录，扫码登录后继续", "login_required", "boilerplate_only"),
        ("访问过于频繁，请完成安全验证", "anti_bot", "boilerplate_only"),
        ("", "available", "too_short"),
        ("过短正文", "available", "too_short"),
    ],
)
def test_m6_quality_gate_blocks_invalid_web_sources(
    repo: Repository, content: str, availability: str, quality: str,
) -> None:
    captured = capture_web_bytes(repo, f"https://example.com/{uuid.uuid4().hex}", content.encode("utf-8"))
    result = SourceQualityService(repo).assess(captured.source_id)
    assert result.availability_status == availability
    assert result.content_quality == quality
    assert result.compile_allowed is False
    compiled = BundleCompiler(repo).compile(captured.source_id)
    assert compiled.compile_disposition == "invalid_content"
    assert compiled.proposal_id is None
    assert FollowupService(repo).list()


def test_m6_quality_gate_accepts_normal_article_and_reports_degraded(repo: Repository) -> None:
    text = "正常文章正文。" * 100
    captured = capture_web_bytes(repo, "https://example.com/normal", text.encode("utf-8"))
    service = SourceQualityService(repo)
    valid = service.assess(captured.source_id)
    assert valid.content_quality == "valid" and valid.compile_allowed
    extraction_path, extraction, body = ExtractionService(repo).latest_for_source(captured.source_id)
    extraction["warnings"] = ["formula may be incomplete"]
    extraction_path.write_text(render_document(extraction, body), encoding="utf-8")
    degraded = service.assess(captured.source_id)
    assert degraded.content_quality == "degraded"
    assert degraded.extraction_quality == "degraded"
    assert degraded.compile_allowed


def test_m6_quality_gate_does_not_treat_forbidden_symbol_as_access_denied(repo: Repository) -> None:
    text = ("The algorithm excludes forbidden symbols that violate unit constraints. " * 20).encode()
    captured = capture_web_bytes(repo, "https://example.com/physics-paper", text)
    result = SourceQualityService(repo).assess(captured.source_id)
    assert result.availability_status == "available"
    assert result.content_quality == "valid"


def test_m6_atomic_claim_split_and_partial_coverage_gate(repo: Repository) -> None:
    statement = "模型使用双编码器，并且训练数据包含三类任务，同时评测报告提升百分之十"
    inspected = AtomicClaimInspector.inspect(statement, ["模型使用双编码器"])
    assert inspected.status == "compound"
    assert inspected.evidence_coverage == "partial"
    split = AtomicClaimInspector.split_spec(
        {"object_type": "claim", "title": statement, "body": statement}, statement,
    )
    assert len(split) == 3
    assert all(item["atomicity_status"] == "atomic" for item in split)
    assert AtomicClaimInspector.inspect("方法使用强化学习，并纳入物理单位约束", ["证据"]).status == "compound"


def test_m6_lifecycle_derives_review_state_without_mutating_source(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Claim: lifecycle proposal evidence that is long enough")
    source_path, before, _ = repo.find_document(captured.source_id)
    original = source_path.read_bytes()
    BundleCompiler(repo).compile(captured.source_id)
    state = SourceLifecycleService(repo).status(captured.source_id)
    assert state.state == "awaiting_review"
    assert source_path.read_bytes() == original
    assert SourceLifecycleService(repo).check()["ok"]
    annotation = SourceAnnotationService(repo).annotate(captured.source_id, why_saved="用于验证生命周期", salience="high")
    assert (repo.root / annotation).exists()
    assert source_path.read_bytes() == original


def test_m6_batch_artifact_migration_has_backup_and_one_formal_truth(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("migration candidate")
    proposal = ProposalService(repo).compile(captured.source_id)
    formal = repo.root / proposal.candidate_path
    temporary = repo.root / ".tmp-batch-import"
    temporary.mkdir()
    shutil.copy2(formal, temporary / "candidate-copy.md")
    (temporary / "one-off.py").write_text("print('old batch')\n", encoding="utf-8")
    service = BatchArtifactMigrator(repo)
    dry = service.plan()
    assert dry.dry_run and dry.candidates_matched_to_formal_proposals == 1
    assert temporary.exists()
    applied = service.migrate()
    assert not temporary.exists() and formal.exists()
    assert applied.backup_path and (repo.root / applied.backup_path).exists()
    run = RunArtifactService(repo).show(str(applied.run_id))
    assert {item["name"] for item in run["files"]} == {
        "manifest.json", "source-summary.md", "compiler-output.json",
        "validation-report.md", "errors.jsonl", "metrics.json",
    }


def test_m6_primary_followup_and_source_bundle_review(repo: Repository) -> None:
    text = ("论文解读引用 https://arxiv.org/abs/2607.11119 ，需要回到原论文核验。" * 10)
    captured = CaptureService(repo)._write_source(
        kind="wechat", original_locator="https://mp.weixin.qq.com/s/test-primary",
        canonical_locator="https://mp.weixin.qq.com/s/test-primary", content=text.encode("utf-8"),
        title="论文解读", comment="", import_method="test", content_type="text/plain; charset=utf-8",
    )
    detected = FollowupService(repo).detect(captured.source_id)
    assert len(detected) == 1 and detected[0]["status"] == "missing"
    bundle = BundleCompiler(repo, JsonBundleProvider(
        _write_json_bundle(repo, [{
            "object_type": "question", "title": "原论文是否支持二手解读？",
            "body": "原论文是否支持二手解读？",
        }])
    )).compile(captured.source_id)
    queue = SourceBundleReviewService(repo).queue()
    assert any(item["bundle_id"] == bundle.proposal_id for item in queue)
    shown = SourceBundleReviewService(repo).show(str(bundle.proposal_id))
    assert shown["source_authority"] == "secondary_analysis"
    assert shown["primary_source_followups"]


@pytest.mark.parametrize(
    ("locator", "expected"),
    [
        ("https://arxiv.org/pdf/1810.08647.pdf", "https://arxiv.org/abs/1810.08647"),
        ("https://arxiv.org/pdf/1810.08647v1.pdf[7", "https://arxiv.org/abs/1810.08647"),
        ("http://arxiv.org/abs/2601.03220v2", "https://arxiv.org/abs/2601.03220"),
        ("https://GitHub.com/Xbotics/Job/?tab=readme", "https://github.com/Xbotics/Job"),
    ],
)
def test_m61_primary_locator_normalization(locator: str, expected: str) -> None:
    assert normalize_primary_locator(locator) == expected


def test_m61_quality_detection_deduplicates_malformed_arxiv_variants(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "References https://arxiv.org/pdf/1810.08647.pdf and "
        "https://arxiv.org/pdf/1810.08647v1.pdf[7 plus "
        "https://arxiv.org/pdf/1811.05931v1.pdf[6."
    )
    assessment = SourceQualityService(repo).assess(captured.source_id)
    assert assessment.primary_source_locators == [
        "https://arxiv.org/abs/1810.08647",
        "https://arxiv.org/abs/1811.05931",
    ]


def test_m61_followup_locator_migration_is_dry_run_backed_up_and_idempotent(repo: Repository) -> None:
    source = CaptureService(repo).capture_text("Secondary interpretation with primary references")
    service = FollowupService(repo)
    legacy_ids = []
    for locator in (
        "https://arxiv.org/pdf/1810.08647.pdf",
        "https://arxiv.org/pdf/1810.08647v1.pdf[7",
    ):
        legacy_id = service._id(source.source_id, locator, "primary_source")
        legacy_ids.append(legacy_id)
        metadata = {
            "id": legacy_id, "type": "followup", "status": "missing",
            "title": f"Primary source follow-up for {source.source_id}",
            "created_at": "2026-07-15T10:00:00+08:00", "updated_at": "2026-07-15T10:00:00+08:00",
            "source_id": source.source_id, "followup_kind": "primary_source",
            "primary_source_locator": locator, "reason": "legacy extraction",
            "captured_source_id": None, "resolution_history": [],
        }
        service._path(legacy_id).write_text(render_document(metadata, "# Legacy follow-up\n"), encoding="utf-8")
    proposal_path = repo.root / "vault/proposals/proposal-locator-migration.md"
    proposal = {
        "id": "proposal_locator_migration", "type": "proposal", "status": "pending",
        "title": "Locator migration fixture", "created_at": "2026-07-15T10:00:00+08:00",
        "updated_at": "2026-07-15T10:00:00+08:00", "primary_source_followups": legacy_ids,
    }
    proposal_path.write_text(render_document(proposal, "# Proposal\n"), encoding="utf-8")
    before = {path: path.read_bytes() for path in [*service.directory.glob("*.md"), proposal_path]}

    dry = service.normalize_locators()
    assert dry["dry_run"] and dry["changed_followups"] == 2 and dry["active_after"] == 1
    assert all(path.read_bytes() == content for path, content in before.items())

    applied = service.normalize_locators(apply=True)
    assert not applied["dry_run"] and applied["backup_path"]
    assert (repo.root / str(applied["backup_path"])).is_dir()
    active = service.list()
    assert len(active) == 1
    assert active[0]["primary_source_locator"] == "https://arxiv.org/abs/1810.08647"
    assert len(service.list(include_superseded=True)) == 3
    migrated_proposal, _ = read_document(proposal_path)
    assert migrated_proposal["primary_source_followups"] == [active[0]["id"]]
    assert service.normalize_locators(apply=True)["changed_followups"] == 0


def _write_json_bundle(repo: Repository, items: list[dict[str, object]]) -> Path:
    path = repo.root / "data/derived/m6-bundle.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"items": items}, ensure_ascii=False), encoding="utf-8")
    return path


def write_canonical_fixture(
    repo: Repository, object_type: str, object_id: str, title: str, body: str,
    source_ids: list[str], *, status: str = "confirmed", domains: list[str] | None = None,
    relations: list[dict[str, str]] | None = None,
) -> Path:
    directories = {
        "project": "vault/action/projects", "goal": "vault/action/goals",
        "architecture": "vault/action/architectures", "decision": "vault/action/decisions",
        "experiment": "vault/action/experiments", "failure": "vault/action/failures",
        "opportunity": "vault/action/opportunities", "concept": "vault/knowledge/concepts",
        "claim": "vault/knowledge/claims", "question": "vault/frontier/questions",
        "intuition": "vault/frontier/intuitions", "tension": "vault/frontier/tensions",
        "analogy": "vault/frontier/analogies", "anomaly": "vault/frontier/anomalies",
        "hypothesis": "vault/frontier/hypotheses",
    }
    metadata = {
        "id": object_id, "type": object_type, "status": status, "title": title,
        "created_at": "2026-07-15T10:00:00+08:00", "updated_at": "2026-07-15T10:00:00+08:00",
        "aliases": [], "tags": [], "domains": domains or [], "confidence": "medium",
        "source_ids": source_ids, "relations": relations or [],
    }
    path = repo.root / directories[object_type] / f"{object_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_document(metadata, body), encoding="utf-8")
    return path


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


def test_pdf_optional_dependency_missing_is_graceful(
    repo: Repository, workspace: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    pdf_path = workspace / "optional.pdf"
    pdf_path.write_bytes(make_text_pdf(["optional dependency"]));
    captured = CaptureService(repo).capture_file(pdf_path)
    monkeypatch.setitem(sys.modules, "pypdf", None)
    result = ExtractionService(repo).extract(captured.source_id)
    assert result.status == "error"
    assert "pip install -e .[pdf]" in result.warnings[0]
    assert (repo.root / captured.raw_content_path).read_bytes() == pdf_path.read_bytes()


def test_extraction_replaces_unpaired_surrogates_only_in_derived_view(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    captured = CaptureService(repo).capture_text("raw input remains unchanged")
    raw_before = (repo.root / captured.raw_content_path).read_bytes()
    service = ExtractionService(repo)
    monkeypatch.setattr(
        service,
        "_extract_payload",
        lambda *args, **kwargs: (f"valid {chr(0xD835)} text", "test-extractor", None, [], "ready", "utf-8"),
    )

    result = service.extract(captured.source_id)
    _, metadata, body = service.find(result.extraction_id)

    assert result.status == "ready"
    assert chr(0xD835) not in body
    assert "\ufffd" in body
    assert any("unpaired Unicode surrogates" in warning for warning in metadata["warnings"])
    assert (repo.root / captured.raw_content_path).read_bytes() == raw_before


def test_extraction_marks_old_input_stale(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("first extraction input")
    service = ExtractionService(repo)
    first = service.extract(captured.source_id)
    source_path = repo.root / captured.source_path
    source, body = read_document(source_path)
    replacement = b"second extraction input"
    digest = sha256_bytes(replacement)
    replacement_path = repo.content_object_path(digest)
    repo.immutable_write(replacement_path, replacement)
    source["content_sha256"] = digest
    source["content_id"] = f"content_{digest}"
    source["raw_content_path"] = repo.rel(replacement_path)
    source_path.write_text(render_document(source, body), encoding="utf-8")
    second = service.extract(captured.source_id)
    _, old_metadata, _ = service.find(first.extraction_id)
    assert first.extraction_id != second.extraction_id
    assert old_metadata["status"] == "stale"


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
    lint_result = lint(repo)
    assert lint_result["ok"] is True, lint_result["errors"]


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


def test_bundle_preserves_explicit_contradiction_candidate(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Claim: [contradicts:claim_existing] A conflicting bounded statement."
    )
    bundle = BundleCompiler(repo).compile(captured.source_id)
    proposal, _ = read_document(repo.root / bundle.proposal_path)
    assert proposal["contradiction_candidates"][0]["target_id"] == "claim_existing"
    assert proposal["bundle_items"][0]["potential_conflicts"]
    assert not (repo.root / proposal["bundle_items"][0]["target_path"]).exists()


def test_deterministic_compiler_does_not_treat_article_markers_as_agent_instructions(repo: Repository) -> None:
    captured = capture_web_bytes(
        repo,
        "https://example.com/article-with-question-heading",
        (b"Question: can this article heading trigger compilation?\n" + b"Article body remains source evidence. " * 30),
        title="Article with an incidental marker",
    )

    result = BundleCompiler(repo).compile(captured.source_id)

    assert result.compile_disposition == "source_only"
    assert result.item_count == 0


def test_external_json_bundle_adapter_never_writes_without_proposal(
    repo: Repository, workspace: Path
) -> None:
    captured = CaptureService(repo).capture_text("external provider input")
    bundle_file = workspace / "bundle.json"
    bundle_file.write_text(json.dumps({"items": [{
        "object_type": "question", "title": "What remains uncertain?",
        "body": "What remains uncertain?", "span_start": 0,
    }]}), encoding="utf-8")
    result = BundleCompiler(repo, JsonBundleProvider(bundle_file, "cursor-json-v1")).compile(captured.source_id)
    proposal, _ = read_document(repo.root / result.proposal_path)
    assert proposal["processor"] == "cursor-json-v1"
    assert not (repo.root / proposal["bundle_items"][0]["target_path"]).exists()


def test_external_provider_can_add_typed_relation_to_existing_object(repo: Repository, workspace: Path) -> None:
    anchor = write_m8_memory(
        repo, "concept_semantic_anchor", "concept", "Semantic Anchor",
        "Existing governed concept.", [],
    )
    captured = CaptureService(repo).capture_text("A model-derived connection grounded in this source.")
    bundle_file = workspace / "semantic-relation.json"
    bundle_file.write_text(json.dumps({"items": [{
        "object_type": "concept", "title": "Connected Concept",
        "body": "A model-derived connection grounded in this source.",
        "relations": [{
            "type": "related_to", "target_id": "concept_semantic_anchor",
            "reason": "Both concepts describe the same bounded mechanism.", "confidence": "medium",
        }],
    }]}), encoding="utf-8")

    result = BundleCompiler(repo, JsonBundleProvider(bundle_file, "agent-semantic-v1")).compile(captured.source_id)
    proposal, _ = read_document(repo.root / result.proposal_path)
    candidate, _ = read_document(repo.root / proposal["bundle_items"][0]["candidate_path"])

    assert anchor.exists()
    assert any(
        relation["type"] == "related_to" and relation["target_id"] == "concept_semantic_anchor"
        for relation in candidate["relations"]
    )


def test_external_provider_can_link_objects_created_in_same_bundle(
    repo: Repository, workspace: Path,
) -> None:
    captured = CaptureService(repo).capture_text("Two model-derived objects form one bounded semantic unit.")
    bundle_file = workspace / "semantic-intra-bundle-relation.json"
    bundle_file.write_text(json.dumps({"items": [
        {
            "action": "create", "target_id": "concept_bundle_anchor",
            "object_type": "concept", "title": "Bundle Anchor",
            "body": "The anchor is explicitly identified within the semantic bundle.",
        },
        {
            "action": "create", "target_id": "claim_bundle_evidence",
            "object_type": "claim", "title": "Bundle Evidence",
            "body": "The evidence is interpreted in relation to the bundle anchor.",
            "relations": [{
                "type": "supports", "target_id": "concept_bundle_anchor",
                "reason": "The claim supplies bounded evidence for the new concept.",
                "confidence": "medium",
            }],
        },
    ]}), encoding="utf-8")

    result = BundleCompiler(repo, JsonBundleProvider(bundle_file, "agent-semantic-v1")).compile(captured.source_id)
    proposal, _ = read_document(repo.root / result.proposal_path)
    claim_item = next(item for item in proposal["bundle_items"] if item["target_id"] == "claim_bundle_evidence")
    claim, _ = read_document(repo.root / claim_item["candidate_path"])

    assert any(
        relation["type"] == "supports" and relation["target_id"] == "concept_bundle_anchor"
        for relation in claim["relations"]
    )


def test_compile_cli_can_defer_obsidian_rebuild_for_bounded_batch(
    repo: Repository, workspace: Path, capsys: pytest.CaptureFixture[str],
) -> None:
    captured = CaptureService(repo).capture_text("Batch semantic input.")
    bundle_file = workspace / "batch-no-obsidian.json"
    bundle_file.write_text(json.dumps({"items": [{
        "object_type": "concept", "title": "Batch Semantic Concept",
        "body": "A bounded model-derived concept for batch compilation.",
    }]}), encoding="utf-8")

    exit_code = run(build_parser().parse_args([
        "--root", str(repo.root), "compile", captured.source_id,
        "--bundle-file", str(bundle_file), "--provider-name", "agent-semantic-test",
        "--skip-obsidian",
    ]))
    output = json.loads(capsys.readouterr().out)

    assert exit_code == 0 and output["obsidian"]["skipped"] is True
    assert not (repo.root / "vault/views/graph").exists()


def test_semantic_queue_exposes_source_only_and_closes_after_model_bundle(repo: Repository) -> None:
    captured = capture_web_bytes(
        repo, "https://example.com/semantic-queue",
        b"A long unmarked research article needs model interpretation. " * 30,
        title="Semantic Queue Article",
    )
    daily = ConsolidationService(repo).daily(limit=5)
    assert daily["compiled"][0]["status"] == "source_only"

    queued = SemanticDistillationQueue(repo).queue(limit=5, max_chars=1200)
    assert queued["pending_count"] == 1
    assert queued["items"][0]["source_id"] == captured.source_id
    assert "model interpretation" in queued["items"][0]["excerpt"]

    bundle_file = _write_json_bundle(repo, [{
        "object_type": "concept", "title": "Model-interpreted research article",
        "body": "The source requires semantic interpretation before knowledge admission.",
    }])
    compiled = BundleCompiler(repo, JsonBundleProvider(bundle_file, "agent-semantic-v1")).compile(captured.source_id)
    WorkingMemoryService(repo).ingest_bundle(str(compiled.proposal_id))

    after = SemanticDistillationQueue(repo).queue(limit=5, max_chars=1200)
    assert after["pending_count"] == 0


def test_external_provider_update_uses_stable_target_id_not_title(
    repo: Repository, workspace: Path,
) -> None:
    target_path, _ = write_m8_claim(repo, "claim_provider_stable_target")
    original = target_path.read_bytes()
    captured = CaptureService(repo).capture_text("Updated bounded evidence from a new source.")
    bundle_file = workspace / "target-update.json"
    bundle_file.write_text(json.dumps({"items": [{
        "action": "update", "target_id": "claim_provider_stable_target",
        "object_type": "claim", "title": "A deliberately different title",
        "body": "Updated bounded evidence from a new source.", "change_type": "support",
    }]}), encoding="utf-8")

    result = BundleCompiler(repo, JsonBundleProvider(bundle_file)).compile(captured.source_id)
    proposal, _ = read_document(repo.root / result.proposal_path)
    item = proposal["bundle_items"][0]

    assert item["action"] == "update" and item["target_id"] == "claim_provider_stable_target"
    assert target_path.read_bytes() == original


def test_external_provider_update_rejects_missing_target_id(repo: Repository, workspace: Path) -> None:
    captured = CaptureService(repo).capture_text("Provider update without identity.")
    bundle_file = workspace / "missing-target-update.json"
    bundle_file.write_text(json.dumps({"items": [{
        "action": "update", "object_type": "question", "title": "Same title is not identity",
        "body": "Provider update without identity.",
    }]}), encoding="utf-8")

    with pytest.raises(ValidationError, match="requires stable target_id"):
        BundleCompiler(repo, JsonBundleProvider(bundle_file)).compile(captured.source_id)


def test_external_bundle_can_propose_work_enrichment(repo: Repository, workspace: Path) -> None:
    captured = CaptureService(repo).capture_text("work metadata input")
    bundle_file = workspace / "work-bundle.json"
    bundle_file.write_text(json.dumps({"items": [{
        "object_type": "work", "title": "Auditable Work", "body": "Logical work metadata.",
        "metadata": {
            "id": "work_arxiv_2600_00001", "work_type": "paper",
            "canonical_title": "Auditable Work", "authors": ["Author"],
            "arxiv_id": "2600.00001", "language": "en", "same_work_as": [],
        },
    }]}), encoding="utf-8")
    result = BundleCompiler(repo, JsonBundleProvider(bundle_file)).compile(captured.source_id)
    proposal, _ = read_document(repo.root / result.proposal_path)
    item = proposal["bundle_items"][0]
    candidate, _ = read_document(repo.root / item["candidate_path"])
    assert candidate["type"] == "work" and candidate["arxiv_id"] == "2600.00001"
    assert not (repo.root / item["target_path"]).exists()


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
    lint_result = lint(repo)
    assert lint_result["ok"] is True, lint_result["errors"]


def test_bundle_compound_item_split_preserves_parent_and_adds_atomic_children(repo: Repository, workspace: Path) -> None:
    captured = CaptureService(repo).capture_text("Claim: first assertion")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    proposal_path = repo.root / str(bundle.proposal_path)
    proposal, _ = read_document(proposal_path)
    parent = proposal["bundle_items"][0]
    parent_path = repo.root / parent["candidate_path"]
    parent_candidate, parent_body = read_document(parent_path)
    parent_candidate["atomicity_status"] = "compound"
    parent_candidate["publication_gate"] = "needs_split"
    parent_text = render_document(parent_candidate, parent_body)
    parent_path.write_text(parent_text, encoding="utf-8")
    parent["atomicity_status"] = "compound"
    parent["candidate_sha256"] = sha256_bytes(parent_path.read_bytes())
    proposal_path.write_text(render_document(proposal, "# Compound fixture\n"), encoding="utf-8")
    assert parent["atomicity_status"] == "compound"
    files = []
    for index, body in enumerate(("first assertion", "it records a second assertion"), start=1):
        candidate = {
            **parent_candidate, "id": f"claim_split_child_{index}", "title": body,
            "atomicity_status": "atomic", "evidence_coverage": "partial",
            "publication_gate": "needs_review", "split_from": parent_candidate["id"],
        }
        path = workspace / f"child-{index}.md"
        path.write_text(render_document(candidate, body), encoding="utf-8")
        files.append(path)
    result = BundleReviewService(repo).split_item(
        str(bundle.proposal_id), parent["item_id"], files, "拆成两个可独立核验的断言",
    )
    assert len(result["child_items"]) == 2
    updated, _ = read_document(proposal_path)
    old = next(item for item in updated["bundle_items"] if item["item_id"] == parent["item_id"])
    children = [item for item in updated["bundle_items"] if item.get("split_from_item_id") == parent["item_id"]]
    assert old["decision"] == "superseded" and old["split_into"] == result["child_items"]
    assert len(children) == 2 and all(item["decision"] == "pending" for item in children)
    assert not any((repo.root / item["target_path"]).exists() for item in children)
    with pytest.raises(ValidationError):
        BundleReviewService(repo).approve(str(bundle.proposal_id), [children[0]["item_id"]])
    lint_result = lint(repo)
    assert lint_result["ok"] is True, lint_result["errors"]


def test_bundle_atomic_item_primary_quote_verification_is_span_checked(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Claim: primary assertion")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    proposal, _ = read_document(repo.root / str(bundle.proposal_path))
    item = proposal["bundle_items"][0]
    _, extraction, text = ExtractionService(repo).latest_for_source(captured.source_id)
    quote = "primary assertion"
    start = text.index(quote)
    service = BundleReviewService(repo)
    with pytest.raises(ValidationError):
        service.verify_item_quote(
            str(bundle.proposal_id), item["item_id"], captured.source_id,
            extraction["extraction_id"], start, "wrong quote", "fixture", "primary verification",
        )
    result = service.verify_item_quote(
        str(bundle.proposal_id), item["item_id"], captured.source_id,
        extraction["extraction_id"], start, quote, "fixture", "primary verification",
    )
    candidate, _ = read_document(repo.root / result["candidate_path"])
    assert candidate["evidence_coverage"] == "full"
    assert candidate["epistemic_source_authority"] == "primary"
    assert candidate["evidence"][-1]["original_text"] == quote
    corrected = service.verify_item_quote(
        str(bundle.proposal_id), item["item_id"], captured.source_id,
        extraction["extraction_id"], start, quote, "corrected fixture", "primary verification",
    )
    corrected_candidate, _ = read_document(repo.root / corrected["candidate_path"])
    assert sum(evidence["evidence_id"] == result["evidence_id"] for evidence in corrected_candidate["evidence"]) == 1
    approved = service.approve(str(bundle.proposal_id), [item["item_id"]])
    assert approved["approved_items"] == [item["item_id"]]


def test_bundle_item_atomicity_correction_preserves_previous_candidate(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Claim: method summary")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    proposal, _ = read_document(repo.root / str(bundle.proposal_path))
    item = proposal["bundle_items"][0]
    old_path = repo.root / item["candidate_path"]
    old_bytes = old_path.read_bytes()
    result = BundleReviewService(repo).mark_item_compound(
        str(bundle.proposal_id), item["item_id"], "primary source review found two testable clauses",
    )
    assert old_path.read_bytes() == old_bytes
    candidate, _ = read_document(repo.root / result["candidate_path"])
    assert candidate["atomicity_status"] == "compound"
    with pytest.raises(ValidationError):
        BundleReviewService(repo).approve(str(bundle.proposal_id), [item["item_id"]])


def test_context_profiles_select_expected_layers_and_relation_expansion(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("M5 shared context source evidence", title="Shared source")
    source_ids = [captured.source_id]
    project_id = "project_m5_context"
    write_canonical_fixture(repo, "project", project_id, "M5 shared context project", "M5 shared context project goal", source_ids)
    for object_type in ("goal", "architecture", "decision", "experiment", "failure", "opportunity"):
        title = "Related decision" if object_type == "decision" else f"M5 shared context {object_type}"
        detail = "relation-only decision" if object_type == "decision" else f"M5 shared context {object_type} details"
        write_canonical_fixture(
            repo, object_type, f"{object_type}_m5", title, detail, source_ids,
            relations=[{"type": "applied_in", "target_id": project_id, "reason": "belongs to project"}],
        )
    for object_type in ("concept", "claim", "question"):
        write_canonical_fixture(
            repo, object_type, f"{object_type}_research", f"M5 shared context {object_type}",
            f"M5 shared context {object_type} evidence", source_ids, domains=["memory"],
        )
    for object_type in ("intuition", "tension", "analogy", "anomaly", "hypothesis"):
        write_canonical_fixture(
            repo, object_type, f"{object_type}_explore", f"M5 shared context {object_type}",
            f"M5 shared context {object_type} exploration", source_ids,
        )
    repo.rebuild_index()
    service = ContextPackService(repo)
    execution = service.build("M5 shared context", 5000, profiles=["execution"], relation_depth=1).as_dict()
    execution_types = {item["type"] for item in execution["items"]}
    assert {"project", "goal", "architecture", "decision", "experiment", "failure"} <= execution_types
    assert any(item["match_reason"].startswith("relation") for item in execution["items"])
    research = service.build(
        "M5 shared context", 5000, profiles=["research"], domains={"memory"},
        object_types={"claim", "concept", "question"}, relation_depth=0,
    ).as_dict()
    assert {item["type"] for item in research["items"]} == {"claim", "concept", "question"}
    exploration = service.build("M5 shared context", 5000, profiles=["exploration"]).as_dict()
    assert {"intuition", "tension", "analogy", "anomaly", "hypothesis"} <= {item["type"] for item in exploration["items"]}
    combined = service.build("M5 shared context", 5000, profiles=["execution", "research"]).as_dict()
    assert "project" in {item["type"] for item in combined["items"]}
    assert "claim" in {item["type"] for item in combined["items"]}
    assert all(item["source_ids"] for item in combined["items"])


def test_context_never_confuses_pending_bundle_with_canonical(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Claim: proposal boundary token", title="Proposal boundary")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    normal = ContextPackService(repo).build("proposal boundary token", 1200).as_dict()
    assert all(item["type"] != "proposal" for item in normal["items"])
    explicit = ContextPackService(repo).build(
        "proposal boundary token", 2000, include_proposals=True,
        object_types={"proposal", "source"}, statuses={"pending", "captured"},
    ).as_dict()
    proposal_item = next(item for item in explicit["items"] if item["id"] == bundle.proposal_id)
    assert proposal_item["type"] == "proposal"
    assert proposal_item["knowledge_status"] == "pending"
    candidates = ContextPackService(repo).build(
        "proposal boundary token", 2000, include_proposals=True,
        object_types={"claim"}, statuses={"proposal"},
    ).as_dict()
    claim_item = next(item for item in candidates["items"] if item["type"] == "claim")
    assert claim_item["truth_layer"] == "proposal"
    assert claim_item["proposal_id"] == bundle.proposal_id
    assert claim_item["knowledge_status"] == "proposal"


def test_m6_corpus_distillation_is_idempotent_and_keeps_canonical_untouched(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Epiplexity evidence " + ("reusable bounded structure " * 12),
        title="Epiplexity source",
    )
    timestamp = "2026-07-16T00:00:00+08:00"
    candidate_id = "claim_wechat_epiplexity_definition_20260715"
    candidate_path = repo.root / "vault/proposals" / "candidate-model-epiplexity.md"
    candidate = {
        "id": candidate_id, "type": "claim", "status": "proposal",
        "title": "Epiplexity describes reusable bounded structure",
        "created_at": timestamp, "updated_at": timestamp, "aliases": [],
        "tags": ["epiplexity"], "domains": ["information-theory"],
        "confidence": "medium", "source_ids": [captured.source_id],
        "relations": [{"type": "derived_from", "target_id": captured.source_id, "reason": "test evidence"}],
        "evidence": [{"original_text": "reusable bounded structure", "verification_status": "verified"}],
    }
    candidate_path.write_text(render_document(candidate, "# Epiplexity\n\nCandidate body.\n"), encoding="utf-8")
    old_proposal_path = repo.root / "vault/proposals" / "proposal-model-epiplexity.md"
    old_proposal = {
        "id": "proposal_model_epiplexity", "type": "proposal", "status": "pending",
        "title": "Model Epiplexity candidate", "created_at": timestamp, "updated_at": timestamp,
        "aliases": [], "tags": [], "domains": [], "confidence": "medium",
        "source_ids": [captured.source_id], "relations": [], "proposal_kind": "model_candidate",
        "candidate_path": repo.rel(candidate_path),
    }
    old_proposal_path.write_text(render_document(old_proposal, "# Model proposal\n"), encoding="utf-8")

    service = CorpusDistillationService(repo)
    dry_run = service.plan()
    assert dry_run.dry_run is True
    assert not any((repo.root / "vault/knowledge").rglob(f"{candidate_id}*.md"))
    first = service.apply()
    second = service.apply()

    assert first.proposal_id == second.proposal_id
    corpus = []
    for path in repo.proposal_documents():
        metadata, _ = read_document(path)
        if metadata.get("proposal_kind") == "corpus_distillation":
            corpus.append(metadata)
    assert len(corpus) == 1
    old_after, _ = read_document(old_proposal_path)
    assert old_after["status"] == "superseded"
    assert old_after["superseded_by"] == first.proposal_id
    assert not any((repo.root / "vault/knowledge").rglob(f"{candidate_id}*.md"))


def test_search_filters_weighted_metadata_and_bounded_traversal(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("source body", title="source")
    project = write_canonical_fixture(
        repo, "project", "project_search", "Weighted Needle Project", "project body", [captured.source_id],
        domains=["architecture"],
    )
    write_canonical_fixture(
        repo, "decision", "decision_search", "Related Decision", "decision body", [captured.source_id],
        relations=[{"type": "applied_in", "target_id": "project_search", "reason": "project decision"}],
    )
    repo.rebuild_index()
    result = repo.search("Weighted Needle", object_types={"project"}, statuses={"confirmed"})
    assert result[0].id == "project_search"
    assert result[0].match_reason == "metadata:title"
    expanded = repo.search_with_relations(
        "Weighted Needle", max_depth=1, max_nodes=5, object_types={"project", "decision"}
    )
    assert {item.id for item in expanded} == {"project_search", "decision_search"}
    assert any(item.match_reason.startswith("relation depth 1") for item in expanded)
    with pytest.raises(ValidationError, match="depth"):
        repo.search_with_relations("Weighted", max_depth=4)
    assert project.exists()


def test_long_unicode_paths_and_posix_metadata_are_cross_platform(repo: Repository, workspace: Path) -> None:
    nested = workspace
    while len(str(nested)) < 190:
        nested = nested / "中文长路径层级"
    nested.mkdir(parents=True)
    local = nested / ("很长的中文文件名" * 4 + ".txt")
    local.write_text("跨平台路径分隔符验证", encoding="utf-8")
    captured = CaptureService(repo).capture_file(local)
    assert "/" in captured.raw_content_path and "\\" not in captured.raw_content_path
    assert (repo.root / Path(captured.raw_content_path)).is_file()
    assert RawStoreService(repo).verify()["ok"] is True


def test_index_rebuild_survives_deleted_derived_extraction(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Claim: Derived data is rebuildable.")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    BundleReviewService(repo).approve(bundle.proposal_id)
    extraction_path, _, _ = ExtractionService(repo).latest_for_source(captured.source_id)
    extraction_path.unlink()
    repo.index_path.unlink()
    assert repo.rebuild_index() >= 2
    rebuilt = ExtractionService(repo).extract(captured.source_id, rebuild=True)
    assert rebuilt.status == "ready"
    assert repo.search("Derived data")


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


def test_find_document_and_lint_resolve_archived_source(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Archived source fixture.")
    source_path = next(path for path in repo.source_documents() if path.name.endswith(f"{captured.source_id}.md"))
    archived_path = repo.root / "vault" / "archive" / source_path.name
    archived_path.parent.mkdir(parents=True, exist_ok=True)
    metadata, body = read_document(source_path)
    metadata["status"] = "archived"
    archived_path.write_text(render_document(metadata, body), encoding="utf-8")
    source_path.unlink()
    repo.rebuild_index()

    resolved_path, resolved_metadata, _ = repo.find_document(captured.source_id)
    assert resolved_path == archived_path
    assert resolved_metadata["status"] == "archived"
    assert lint(repo)["ok"] is True


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


WECHAT_ARTICLE_HTML = """<!DOCTYPE html>
<html>
<head>
<meta property="og:title" content="测试文章标题" />
<meta property="og:article:author" content="张三" />
<script>var ct = "1710000000"; var nickname = htmlDecode("测试公众号");</script>
</head>
<body>
<h1 id="activity-name">测试文章标题</h1>
<div id="js_name">测试公众号</div>
<div class="rich_media_content" id="js_content">
<p>第一段正文内容。</p>
<p>第二段正文内容。</p>
</div>
</body>
</html>"""


def test_wechat_url_detection_and_canonicalization() -> None:
    from global_memory.wechat import canonicalize_wechat_url, is_wechat_article_url

    short = "https://mp.weixin.qq.com/s/AbCdEfGhIjKl?utm_source=foo"
    long = (
        "https://mp.weixin.qq.com/s?__biz=MzA4MTg1NzYyNQ==&mid=2650812345"
        "&idx=1&sn=abc123&chksm=deadbeef&scene=27"
    )
    assert is_wechat_article_url(short) is True
    assert is_wechat_article_url(long) is True
    assert is_wechat_article_url("https://example.com/s/foo") is False
    assert canonicalize_wechat_url(short) == "https://mp.weixin.qq.com/s/AbCdEfGhIjKl"
    assert canonicalize_wechat_url(long) == (
        "https://mp.weixin.qq.com/s?"
        "__biz=MzA4MTg1NzYyNQ%3D%3D&idx=1&mid=2650812345&sn=abc123"
    )


def test_capture_wechat_article_parses_metadata_and_extracts_body(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    from global_memory.wechat import parse_wechat_metadata

    class Response:
        def __init__(self, body: bytes, final_url: str):
            self.body = body
            self.headers = {"Content-Type": "text/html; charset=utf-8"}
            self.final_url = final_url

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self, _limit: int) -> bytes:
            return self.body

        def geturl(self) -> str:
            return self.final_url

    url = "https://mp.weixin.qq.com/s/AbCdEfGhIjKl"
    monkeypatch.setattr(
        "global_memory.wechat.urllib.request.urlopen",
        lambda *_args, **_kwargs: Response(WECHAT_ARTICLE_HTML.encode("utf-8"), url),
    )
    metadata = parse_wechat_metadata(WECHAT_ARTICLE_HTML)
    assert metadata.title == "测试文章标题"
    assert metadata.author == "张三"
    assert metadata.account_name == "测试公众号"
    assert metadata.published_at is not None

    captured = CaptureService(repo).capture_wechat_url(url, "微信单篇导入测试")
    source_path = repo.root / captured.source_path
    source_meta, _ = read_document(source_path)
    assert source_meta["source_kind"] == "wechat"
    assert source_meta["import_method"] == "cli-wechat"
    assert source_meta["author"] == "张三"
    assert source_meta["published_at"] is not None

    extracted = ExtractionService(repo).extract(captured.source_id)
    assert extracted.status == "ready"
    assert extracted.extractor == "wechat-article-v1"
    _, extraction_meta, body = ExtractionService(repo).find(extracted.extraction_id)
    assert "第一段正文内容" in body
    assert "第二段正文内容" in body
    assert extraction_meta["extractor"] == "wechat-article-v1"


def test_capture_wechat_cli_command(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    class Response:
        def __init__(self, body: bytes):
            self.body = body
            self.headers = {"Content-Type": "text/html; charset=utf-8"}

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self, _limit: int) -> bytes:
            return self.body

        def geturl(self) -> str:
            return "https://mp.weixin.qq.com/s/AbCdEfGhIjKl"

    monkeypatch.setattr(
        "global_memory.wechat.urllib.request.urlopen",
        lambda *_args, **_kwargs: Response(WECHAT_ARTICLE_HTML.encode("utf-8")),
    )
    args = build_parser().parse_args(
        ["capture-wechat", "https://mp.weixin.qq.com/s/AbCdEfGhIjKl", "--comment", "cli"]
    )
    assert args.command == "capture-wechat"
    captured = CaptureService(repo).capture_wechat_url(args.url, args.comment)
    assert captured.duplicate_source is False
    duplicate = CaptureService(repo).capture_wechat_url(args.url, args.comment)
    assert duplicate.duplicate_source is True
def test_context_pack_markdown_is_versioned_and_preserves_provenance(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Claim: Bounded context preserves provenance.", title="Context contract"
    )
    repo.rebuild_index()
    pack = ContextPackService(repo).build("bounded context", token_budget=800)

    assert pack.as_dict()["context_pack_version"] == 1
    markdown = pack.as_markdown()
    assert "context_pack_version: 1" in markdown
    assert captured.source_id in markdown
    assert "## Truncation report" in markdown


def test_context_pack_relaxes_empty_natural_language_query_and_renders_status(
    repo: Repository,
) -> None:
    captured = CaptureService(repo).capture_text(
        "Claim: VIA supports bounded robot control conclusions with explicit limits. " * 5,
        title="VIA bounded robot control",
    )
    bundle = BundleCompiler(repo).compile(captured.source_id)
    BundleReviewService(repo).approve(bundle.proposal_id, item_ids=["claim-1"])
    CaptureService(repo).capture_text(
        "Task: VIA robot control 的实验结论和适用边界是什么. "
        "This is a session receipt that repeats the exact query but is not canonical. " * 4,
        title="Session receipt: competing source",
    )

    pack = ContextPackService(repo).build(
        "VIA robot control 的实验结论和适用边界是什么", token_budget=1200
    )
    markdown = pack.as_markdown()

    assert pack.filters["query_expansion"] == ["VIA"]
    assert pack.items
    assert pack.items[0]["type"] == "claim"
    assert any(item["id"] == captured.source_id for item in pack.items[1:])
    assert "Type/status: `claim` / `confirmed`" in markdown


def test_context_pack_archived_exact_hit_does_not_block_active_term_expansion(repo: Repository) -> None:
    active = write_m8_memory(
        repo, "concept_active_vla_term", "concept", "Active VLA Concept",
        "A governed concept about policy caching.", [],
    )
    second_active = write_m8_memory(
        repo, "concept_active_deployment_term", "concept", "Active Deployment Concept",
        "A governed concept about real-world policy use.", [],
    )
    archived = write_m8_memory(
        repo, "question_archived_exact_query", "question", "Archived exact query",
        "VLA deployment is present only in this historical object.", [],
    )
    metadata, body = read_document(archived)
    metadata.update({"status": "archived", "memory_tier": "historical"})
    archived.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    pack = ContextPackService(repo).build(
        "VLA deployment", profiles=["research"], token_budget=1200,
    )

    assert active.exists()
    assert second_active.exists()
    assert any(item["id"] == "concept_active_vla_term" for item in pack.items)
    assert any(item["id"] == "concept_active_deployment_term" for item in pack.items)
    assert {"VLA", "deployment"} <= set(pack.filters["query_expansion"])


def test_obsidian_views_are_rebuildable_and_do_not_change_canonical(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Obsidian source", title="Obsidian source")
    before = (repo.root / captured.source_path).read_bytes()
    service = ObsidianViewService(repo)
    graph_config = repo.root / "vault/.obsidian/graph.json"
    graph_config.parent.mkdir(parents=True, exist_ok=True)
    graph_config.write_text('{"sentinel": true}\n', encoding="utf-8")

    first = service.build(graph_profile="all")
    first_bytes = {
        relative: (repo.root / relative).read_bytes() for relative in first["written"]
    }
    second = service.build(graph_profile="all")

    assert first["written"] == second["written"]
    assert first_bytes == {
        relative: (repo.root / relative).read_bytes() for relative in second["written"]
    }
    assert (repo.root / captured.source_path).read_bytes() == before
    assert graph_config.read_text(encoding="utf-8") == '{"sentinel": true}\n'
    home = (repo.root / "vault/INDEX.md").read_text(encoding="utf-8")
    reader = repo.root / "vault" / "views" / "readers" / f"{captured.source_id}.md"
    assert "超级大脑" in home
    assert "最近导入" in home
    assert reader.exists()
    assert "Obsidian source" in reader.read_text(encoding="utf-8")
    semantic_source = repo.root / "vault/views/graph/sources/Obsidian source.md"
    assert semantic_source.exists() and captured.source_id not in semantic_source.name
    assert service.status()["current"] is True


def test_obsidian_semantic_graph_uses_readable_names_and_materializes_source_edges(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Evidence body", title="Readable Evidence")
    write_m8_memory(
        repo,
        "claim_graph_internal_7f62757ed57fd38b",
        "claim",
        "Human Readable Claim",
        "Bounded claim body.",
        [captured.source_id],
    )

    ObsidianViewService(repo).build(graph_profile="all")

    node = repo.root / "vault/views/graph/claims/Human Readable Claim.md"
    assert node.exists()
    assert "7f62757ed57fd38b" not in node.name
    text = node.read_text(encoding="utf-8")
    assert "[[views/graph/sources/Readable Evidence|Readable Evidence]]" in text


def test_obsidian_trusted_graph_excludes_unreferenced_high_quality_source(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Primary research evidence. " * 20, title="High Quality Preprint")
    source_path = repo.root / captured.source_path
    metadata, body = read_document(source_path)
    metadata["source_authority"] = "preprint"
    metadata["source_kind"] = "web"
    source_path.write_text(render_document(metadata, body), encoding="utf-8")
    SourceQualityService(repo).assess(captured.source_id)

    ObsidianViewService(repo).build(graph_profile="trusted")

    assert not (repo.root / "vault/views/graph/sources/High Quality Preprint.md").exists()
    assert not (repo.root / "vault/views/graph/hubs/高质量原始资料.md").exists()
    assert not list((repo.root / "vault/memory").rglob(f"*{captured.source_id}*"))


def test_obsidian_trusted_graph_excludes_primary_personal_notes(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Session receipt details. " * 20, title="Agent Receipt")
    SourceQualityService(repo).assess(captured.source_id)

    ObsidianViewService(repo).build(graph_profile="trusted")

    assert not (repo.root / "vault/views/graph/sources/Agent Receipt.md").exists()


def test_obsidian_trusted_graph_includes_only_source_referenced_by_trusted_knowledge(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Evidence body", title="Trusted Evidence")
    write_m8_memory(
        repo, "claim_trusted_graph", "claim", "Trusted Graph Claim",
        "Bounded claim body.", [captured.source_id], tier="trusted", epistemic_status="provisional",
    )

    ObsidianViewService(repo).build(graph_profile="trusted")

    claim = repo.root / "vault/views/graph/claims/Trusted Graph Claim.md"
    source = repo.root / "vault/views/graph/sources/Trusted Evidence.md"
    assert claim.exists() and source.exists()
    assert "[[views/graph/sources/Trusted Evidence|Trusted Evidence]]" in claim.read_text(encoding="utf-8")
    assert "[[views/graph/claims/Trusted Graph Claim|Trusted Graph Claim]]" in source.read_text(encoding="utf-8")


def test_obsidian_default_knowledge_graph_shows_working_semantics_without_source_nodes(
    repo: Repository,
) -> None:
    captured = CaptureService(repo).capture_text("Working semantic evidence", title="Audit-only Source")
    concept = write_m8_memory(
        repo, "concept_working_semantic_graph", "concept", "Working Semantic Concept",
        "A model-distilled Working concept.", [captured.source_id],
    )
    write_m8_memory(
        repo, "claim_working_semantic_graph", "claim", "Working Semantic Claim",
        "A bounded Working claim.", [captured.source_id], epistemic_status="provisional",
    )
    metadata, body = read_document(concept)
    metadata["relations"] = [{
        "type": "supports", "target_id": "claim_working_semantic_graph",
        "reason": "The Working claim is bounded support for this semantic concept.",
        "confidence": "medium", "created_by": "agent-semantic-test", "status": "working",
    }]
    concept.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    result = ObsidianViewService(repo).build()

    concept_node = repo.root / "vault/views/graph/concepts/Working Semantic Concept.md"
    claim_node = repo.root / "vault/views/graph/claims/Working Semantic Claim.md"
    source_node = repo.root / "vault/views/graph/sources/Audit-only Source.md"
    assert result["graph_profile"] == "knowledge"
    assert concept_node.exists() and claim_node.exists()
    assert "[[views/graph/claims/Working Semantic Claim|Working Semantic Claim]]" in concept_node.read_text(encoding="utf-8")
    assert not source_node.exists()


def test_repository_obsidian_graph_is_semantically_grouped_and_hides_navigation_hubs() -> None:
    graph_path = Path(__file__).parents[1] / "vault/.obsidian/graph.json"
    config = json.loads(graph_path.read_text(encoding="utf-8"))

    assert config["search"] == 'path:"views/graph"'
    assert config["hideUnresolved"] is True and config["showOrphans"] is False
    queries = {item["query"] for item in config["colorGroups"]}
    assert any('views/graph/claims' in query for query in queries)
    assert any('views/graph/concepts' in query for query in queries)
    assert any('views/graph/questions' in query for query in queries)
    assert any('views/graph/sources' in query for query in queries)
    assert not any('views/graph/high-confidence-sources' in query for query in queries)
    assert not any('views/graph/hubs' in query for query in queries)
    assert config["textFadeMultiplier"] > 0 and config["lineSizeMultiplier"] < 1


def test_obsidian_views_use_explicit_topics_and_remove_only_stale_generated_readers(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Topic body", title="Topic article")
    source_path = repo.root / captured.source_path
    metadata, body = read_document(source_path)
    metadata["domains"] = ["memory-systems"]
    source_path.write_text(render_document(metadata, body), encoding="utf-8")
    service = ObsidianViewService(repo)
    service.build()

    topics = (repo.root / "vault/views/主题导航.md").read_text(encoding="utf-8")
    assert "memory-systems" in topics
    assert "Topic article" in topics

    readers = repo.root / "vault/views/readers"
    stale = readers / "source_stale.md"
    stale.write_text("<!-- generated by gm-obsidian-v2; safe to rebuild -->\n", encoding="utf-8")
    human = readers / "my-note.md"
    human.write_text("human note", encoding="utf-8")
    result = service.build()
    assert repo.rel(stale) in result["removed"]
    assert human.exists()


def test_receipt_is_immutable_idempotent_and_proposes_without_canonical_write(
    repo: Repository, workspace: Path
) -> None:
    input_file = workspace / "receipt.md"
    input_file.write_text(
        "Claim: Context must remain bounded.\n\nSource: local acceptance observation.",
        encoding="utf-8",
    )
    service = ReceiptService(repo)
    first = service.create("cursor", "global-memory", "bounded read", input_file)
    second = service.create("cursor", "global-memory", "bounded read", input_file)

    assert first == second
    result = service.propose(first["receipt_id"])
    assert result["proposal_id"]
    assert (repo.root / result["proposal_path"]).exists()
    proposal, _ = read_document(repo.root / result["proposal_path"])
    candidate_path = repo.root / proposal["bundle_items"][0]["candidate_path"]
    _, candidate_body = read_document(candidate_path)
    assert "Source: local acceptance observation." in candidate_body
    assert list(repo.canonical_documents()) == []


def test_explicit_marker_preserves_full_block_until_next_marker(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Experiment: Agent acceptance completed.\n\n"
        "## Observations\n\nThe bounded read succeeded and no canonical write occurred.\n\n"
        "Decision: Keep the result pending for human review.\n\n"
        "The decision remains reversible.",
        title="Typed block fixture",
    )
    result = BundleCompiler(repo).compile(captured.source_id)
    proposal, _ = read_document(repo.root / result.proposal_path)
    assert [item["object_type"] for item in proposal["bundle_items"]] == ["experiment", "decision"]
    experiment_path = repo.root / proposal["bundle_items"][0]["candidate_path"]
    decision_path = repo.root / proposal["bundle_items"][1]["candidate_path"]
    _, experiment_body = read_document(experiment_path)
    _, decision_body = read_document(decision_path)
    assert "## Observations" in experiment_body
    assert "no canonical write occurred" in experiment_body
    assert "Keep the result pending" not in experiment_body
    assert "The decision remains reversible" in decision_body


def test_receipt_rejects_unknown_agent(repo: Repository, workspace: Path) -> None:
    input_file = workspace / "receipt.md"
    input_file.write_text("durable note", encoding="utf-8")
    with pytest.raises(ValidationError, match="unsupported receipt agent"):
        ReceiptService(repo).create("hermes", "project", "task", input_file)


def test_agent_adapter_files_define_the_shared_memory_contract() -> None:
    root = Path(__file__).parents[1]
    assert "gm receipt create --agent claude" in (root / "CLAUDE.md").read_text(encoding="utf-8")
    assert "gm receipt create --agent cursor" in (
        root / ".cursor/rules/global-memory.mdc"
    ).read_text(encoding="utf-8")
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    assert "gm context \"<question>\" --format markdown" in agents
    assert "gm receipt create --agent codex" in agents


def test_maintenance_inventory_reports_actionable_backlog(
    repo: Repository, workspace: Path
) -> None:
    input_file = workspace / "maintenance-receipt.md"
    input_file.write_text("Claim: Maintenance is explicit.", encoding="utf-8")
    receipt = ReceiptService(repo).create("codex", "global-memory", "maintenance", input_file)
    weak_proposal = {
        "id": "proposal_maintenance_weak", "type": "proposal", "status": "pending",
        "title": "Weak evidence fixture", "created_at": "2026-07-16T00:00:00+08:00",
        "updated_at": "2026-07-16T00:00:00+08:00", "confidence": "unknown",
        "source_ids": [], "relations": [], "proposal_kind": "compile_bundle",
        "bundle_items": [{
            "item_id": "claim-1", "object_type": "claim", "decision": "pending",
            "evidence_coverage": "partial",
        }],
    }
    (repo.root / "vault/proposals/proposal-proposal_maintenance_weak.md").write_text(
        render_document(weak_proposal, "Weak evidence fixture."), encoding="utf-8"
    )
    CaptureService(repo).capture_text("Inbox item.", title="Inbox item")

    inventory = MaintenanceService(repo).inventory()

    assert inventory["inbox_count"] == 1
    assert inventory["triage_backlog_count"] == 1
    assert inventory["capture_only_count"] == 0
    assert inventory["uncaptured_receipt_ids"] == [receipt["receipt_id"]]
    assert inventory["weak_evidence_proposal_items"]
    assert any("receipt" in action for action in inventory["recommended_actions"])
    assert any("inbox" in action for action in inventory["recommended_actions"])


def test_maintain_defaults_to_read_only(repo: Repository, capsys: pytest.CaptureFixture[str]) -> None:
    before = {
        path: path.read_bytes()
        for path in repo.root.rglob("*")
        if path.is_file()
    }
    args = build_parser().parse_args(["--root", str(repo.root), "maintain"])

    assert run(args) == 0
    output = json.loads(capsys.readouterr().out)
    after = {
        path: path.read_bytes()
        for path in repo.root.rglob("*")
        if path.is_file()
    }
    assert output["mode"] == "read-only"
    assert output["rebuilt"] is None
    assert output["derived_views"]["current"] is False
    assert before == after


def test_maintain_can_explicitly_rebuild_derived_views(
    repo: Repository, capsys: pytest.CaptureFixture[str]
) -> None:
    args = build_parser().parse_args(
        ["--root", str(repo.root), "maintain", "--rebuild-derived"]
    )
    assert run(args) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["mode"] == "rebuild-derived"
    assert output["rebuilt"]["obsidian"]["ok"] is True
    assert output["derived_views"]["current"] is True
    assert (repo.root / "vault/INDEX.md").exists()


def test_weekly_runs_daily_integrity_and_views_without_canonical_writes(
    repo: Repository, capsys: pytest.CaptureFixture[str]
) -> None:
    captured = capture_web_bytes(
        repo, "https://example.com/weekly", b"A useful weekly source body. " * 10
    )
    canonical_before = list(repo.canonical_documents())
    args = build_parser().parse_args(
        ["--root", str(repo.root), "weekly", "--triage-limit", "10"]
    )

    assert run(args) == 0
    output = json.loads(capsys.readouterr().out)

    assert output["mode"] == "weekly-maintenance"
    assert output["triage"]["results"][0]["source_id"] == captured.source_id
    assert output["triage"]["results"][0]["proposal_id"] is None
    assert output["integrity"]["doctor"]["ok"] is True
    assert output["integrity"]["lint"]["ok"] is True
    assert output["integrity"]["raw"]["ok"] is True
    assert output["contradictions"]["ok"] is True
    assert output["derived_views"]["current"] is True
    assert output["synthesis_eligibility"]["proposal_created"] is False
    assert output["canonical_writes"] == 0
    assert list(repo.canonical_documents()) == canonical_before


def test_weekly_cli_has_bounded_defaults() -> None:
    args = build_parser().parse_args(["weekly"])

    assert args.triage_limit == 100
    assert args.recheck is False
    assert args.no_rebuild_derived is False


def test_read_only_mcp_exposes_only_bounded_query_tools(repo: Repository) -> None:
    definitions = ReadOnlyMemoryTools.definitions()

    assert [item["name"] for item in definitions] == [
        "memory_context", "memory_search", "memory_show", "memory_source", "memory_status"
    ]
    assert all(item["annotations"]["readOnlyHint"] is True for item in definitions)
    assert all(item["annotations"]["destructiveHint"] is False for item in definitions)
    assert not any(
        word in item["name"]
        for item in definitions
        for word in ("capture", "compile", "approve", "write", "delete")
    )


def test_read_only_mcp_search_show_source_and_context_do_not_mutate(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Global Memory MCP preserves provenance.", title="MCP source"
    )
    ExtractionService(repo).extract(captured.source_id)
    before = {path: path.read_bytes() for path in repo.root.rglob("*") if path.is_file()}
    tools = ReadOnlyMemoryTools(repo)

    search = tools.call("memory_search", {"query": "provenance"})
    shown = tools.call("memory_show", {"object_id": captured.source_id, "max_chars": 100})
    source = tools.call("memory_source", {"source_id": captured.source_id, "max_chars": 100})
    context = tools.call("memory_context", {"question": "provenance", "token_budget": 256})
    status = tools.call("memory_status", {})

    assert search["results"][0]["id"] == captured.source_id
    assert shown["metadata"]["id"] == captured.source_id
    assert source["extraction"]["metadata"]["source_id"] == captured.source_id
    assert context["context_pack_version"] == 1
    assert "capture_only_count" in status
    after = {path: path.read_bytes() for path in repo.root.rglob("*") if path.is_file()}
    assert before == after


def test_mcp_jsonrpc_lifecycle_and_structured_tool_result(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("MCP lifecycle evidence.", title="MCP lifecycle")
    app = MCPApplication(repo)

    initialized = app.handle({
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "test", "version": "1"}},
    })
    listed = app.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    called = app.handle({
        "jsonrpc": "2.0", "id": 3, "method": "tools/call",
        "params": {"name": "memory_show", "arguments": {"object_id": captured.source_id}},
    })

    assert initialized["result"]["capabilities"]["tools"]["listChanged"] is False
    assert len(listed["result"]["tools"]) == 5
    assert called["result"]["structuredContent"]["metadata"]["id"] == captured.source_id
    assert called["result"]["isError"] is False


def test_mcp_http_requires_token_when_not_loopback(repo: Repository) -> None:
    with pytest.raises(ValidationError, match="requires a bearer token"):
        serve_http(repo, "0.0.0.0", 0, bearer_token=None, allowed_origins=set())


def test_mcp_cli_arguments() -> None:
    stdio = build_parser().parse_args(["mcp", "stdio"])
    http = build_parser().parse_args(["mcp", "http", "--port", "9999", "--allowed-origin", "https://chatgpt.com"])

    assert stdio.mcp_transport == "stdio"
    assert http.mcp_transport == "http"
    assert http.host == "127.0.0.1"
    assert http.port == 9999
    assert http.allowed_origin == ["https://chatgpt.com"]


def test_m90_research_annotation_is_append_only_and_preserves_user_chinese(repo: Repository) -> None:
    captured = capture_web_bytes(repo, "https://example.com/research-signal")
    source_path, _, _ = repo.find_document(captured.source_id)
    source_hash = sha256_bytes(source_path.read_bytes())
    service = ResearchAnnotationService(repo)

    first = service.create(
        "capture_intent", target_ids=[captured.source_id],
        why_saved="它可能解释技能如何沉淀。", what_surprised_me="可逆失效条件很重要。",
        possible_connections=["人类习惯形成", "数据库物化视图"],
        research_projects=["embodied-agent"], domains=["具身智能"],
        personal_salience="high",
    )
    second = service.create(
        "capture_intent", target_ids=[captured.source_id], why_saved="第二次独立记录。",
        supersedes_annotation_id=first["id"],
    )

    assert first["id"] != second["id"]
    assert len(service.all(target_id=captured.source_id)) == 2
    _, first_metadata, first_body = repo.find_document(first["id"])
    assert first_metadata["user_authored"] is True
    assert first_metadata["truth_layer"] == "user_annotation"
    assert "可逆失效条件很重要" in first_body
    assert sha256_bytes(source_path.read_bytes()) == source_hash
    repo.index_path.unlink()
    repo.rebuild_index()
    assert any(item.id == first["id"] for item in repo.search("可逆失效条件", 10))
    assert doctor(repo)["ok"] is True
    assert lint(repo)["ok"] is True


def test_annotation_active_history_and_context_use_only_current_version(repo: Repository) -> None:
    captured = capture_web_bytes(repo, "https://example.com/annotation-active")
    service = ResearchAnnotationService(repo)
    first = service.create(
        "capture_intent", target_ids=[captured.source_id], why_saved="old intent",
        research_projects=["memory"], possible_connections=["old connection"], personal_salience="high",
    )
    second = service.create(
        "capture_intent", target_ids=[captured.source_id], why_saved="current intent",
        research_projects=["memory"], supersedes_annotation_id=first["id"],
    )

    assert [item["id"] for item in service.active()] == [second["id"]]
    assert {item["id"] for item in service.history(annotation_id=first["id"])} == {first["id"], second["id"]}
    with pytest.raises(ValidationError, match="already has an active correction"):
        service.create("capture_intent", target_ids=[captured.source_id], why_saved="parallel", supersedes_annotation_id=first["id"])
    pack = ContextPackService(repo).build("current intent", profiles=["research"])
    annotation = next(item for item in pack.items if item["id"] == second["id"])
    assert annotation["execution_safe"] is False
    assert annotation["annotation"]["why_saved"] == "current intent"
    assert annotation["annotation"]["annotation_id"] == second["id"]
    assert first["id"] not in {item["id"] for item in pack.items}


def test_annotation_active_builds_chain_before_target_filter(repo: Repository) -> None:
    first_target = capture_web_bytes(repo, "https://example.com/annotation-first-target")
    second_target = capture_web_bytes(repo, "https://example.com/annotation-second-target")
    service = ResearchAnnotationService(repo)
    first = service.create("capture_intent", target_ids=[first_target.source_id], why_saved="first")
    second = service.create(
        "capture_intent", target_ids=[first_target.source_id, second_target.source_id],
        why_saved="corrected", supersedes_annotation_id=first["id"],
    )

    assert [item["id"] for item in service.active(target_id=second_target.source_id)] == [second["id"]]
    assert [item["id"] for item in service.history(target_id=second_target.source_id, annotation_id=first["id"])] == [second["id"]]


def test_m90_annotation_id_normalizes_list_order(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    captured = capture_web_bytes(repo, "https://example.com/annotation-id")
    monkeypatch.setattr(research_module, "_event_time", lambda: "2026-07-18T12:00:00.000000+08:00")
    service = ResearchAnnotationService(repo)
    first = service.create(
        "capture_intent", target_ids=[captured.source_id], why_saved="稳定事件",
        possible_connections=["B", "A"], research_projects=["p2", "p1"],
        domains=["d2", "d1"],
    )
    repeated = service.create(
        "capture_intent", target_ids=[captured.source_id], why_saved="稳定事件",
        possible_connections=["A", "B"], research_projects=["p1", "p2"],
        domains=["d1", "d2"],
    )
    assert first["id"] == repeated["id"]
    assert len(service.documents()) == 1


def test_m90_annotation_rejects_empty_and_requires_explicit_unresolved(repo: Repository) -> None:
    service = ResearchAnnotationService(repo)
    with pytest.raises(ValidationError, match="至少需要"):
        service.create("research_note")
    with pytest.raises(ValidationError, match="allow-unresolved"):
        service.create("research_note", target_ids=["question_missing"], note="保留这个问题")
    created = service.create(
        "research_note", target_ids=["question_missing"], note="保留这个问题",
        allow_unresolved=True,
    )
    _, metadata, _ = repo.find_document(created["id"])
    assert metadata["unresolved_target_ids"] == ["question_missing"]


def test_m90_connection_feedback_is_value_signal_not_truth_mutation(repo: Repository) -> None:
    question_path = write_research_fixture_object(
        repo, "question_feedback", "question", "技能固化边界", "技能何时应该固化？"
    )
    before = sha256_bytes(question_path.read_bytes())
    service = ResearchAnnotationService(repo)
    for label in ("obvious", "forced", "interesting", "actionable"):
        service.create(
            "connection_feedback", target_ids=["question_feedback"],
            feedback_label=label, feedback_note=f"{label} 的用户判断",
            research_projects=["embodied-agent"], domains=["learning"],
        )
    with pytest.raises(ValidationError, match="feedback label"):
        service.create(
            "connection_feedback", target_ids=["question_feedback"],
            feedback_label="good", feedback_note="invalid",
        )
    summary = service.feedback_summary()
    assert summary["total"] == 4
    assert all(summary[label] == 1 for label in ("obvious", "forced", "interesting", "actionable"))
    assert summary["by_project"] == {"embodied-agent": 4}
    assert sha256_bytes(question_path.read_bytes()) == before


def test_m90_router_prefers_explicit_project_and_has_global_fallback(repo: Repository) -> None:
    write_research_fixture_object(
        repo, "project_embodied_agent", "project", "embodied-agent", "具身智能研究项目",
        domains=["robotics"],
    )
    router = ResearchRouterService(repo)
    explicit = router.plan("技能何时固化", project="embodied-agent", domains=["robotics"])
    automatic = router.plan("embodied-agent 下一步")
    fallback = router.plan("完全不存在的词汇组合")
    assert explicit.selected_project == "embodied-agent"
    assert explicit.explicit_project == "embodied-agent"
    assert explicit.fallback_used is False
    assert explicit.selected_domains == ["robotics"]
    assert automatic.selected_project == "project_embodied_agent"
    assert fallback.fallback_used is True
    with pytest.raises(ValidationError, match="0..2"):
        router.plan("技能", relation_depth=3)


def test_m90_activation_is_explicit_idempotent_and_trust_orthogonal(repo: Repository) -> None:
    target = write_research_fixture_object(
        repo, "question_activation", "question", "Activation 边界", "使用不等于正确。"
    )
    before = sha256_bytes(target.read_bytes())
    service = ActivationService(repo)
    first = service.record(
        "question_activation", kind="used", project_id="scientific-memory",
        reason="用于架构决策", event_id="activation_test_fixed",
    )
    duplicate = service.record(
        "question_activation", kind="used", project_id="scientific-memory",
        reason="用于架构决策", event_id="activation_test_fixed",
    )
    assert first["written"] is True
    assert duplicate["duplicate"] is True
    aggregate = service.aggregate(object_id="question_activation")[0]
    assert aggregate["used_count"] == 1
    assert sha256_bytes(target.read_bytes()) == before
    repo.rebuild_index()
    with closing(sqlite3.connect(repo.index_path)) as connection:
        assert connection.execute(
            "SELECT used_count FROM activation_aggregates WHERE object_id=?",
            ("question_activation",),
        ).fetchone()[0] == 1


def test_m90_context_is_read_only_by_default_and_route_trace_is_explainable(repo: Repository) -> None:
    captured = capture_web_bytes(
        repo, "https://example.com/context-research", b"skill consolidation signal " * 20
    )
    service = ResearchAnnotationService(repo)
    service.create(
        "capture_intent", target_ids=[captured.source_id],
        why_saved="技能固化研究", research_projects=["embodied-agent"],
    )
    activation_path = repo.root / "system" / "logs" / "activation-events.jsonl"
    before = activation_path.read_bytes() if activation_path.exists() else b""
    pack = ContextPackService(repo).build(
        "技能固化研究", profiles=["research"], project="embodied-agent",
    )
    after = activation_path.read_bytes() if activation_path.exists() else b""
    assert before == after
    assert pack.route_trace["explicit_project"] == "embodied-agent"
    assert pack.route_trace["selection_reasons"]
    annotation_items = [item for item in pack.items if item["type"] == "annotation"]
    assert annotation_items and annotation_items[0]["truth_layer"] == "user_annotation"
    assert annotation_items[0]["execution_safe"] is False
    assert any(item["id"] == captured.source_id for item in pack.items)
    assert pack.route_trace["annotation_matches"]
    run(build_parser().parse_args([
        "--root", str(repo.root), "context", "技能固化研究", "--profile", "research",
        "--project", "embodied-agent", "--record-use",
    ]))
    assert ActivationService(repo).events()


def test_m90_research_digest_and_map_are_idempotent_derived_outputs(repo: Repository) -> None:
    captured = capture_web_bytes(repo, "https://example.com/digest")
    capture_web_bytes(repo, "https://example.com/digest-unannotated")
    ResearchAnnotationService(repo).create(
        "capture_intent", target_ids=[captured.source_id],
        why_saved="用于每周研究复盘", research_projects=["scientific-memory"],
        personal_salience="high",
    )
    digest_service = ResearchDigestService(repo)
    first_digest = digest_service.write()
    second_digest = digest_service.write()
    assert first_digest["path"] == second_digest["path"]
    assert first_digest["digest"]["sources_with_why_saved"] == 1
    assert first_digest["digest"]["new_sources"] == 2
    view_service = ResearchMapService(repo)
    first_view = view_service.build()
    assert len(first_view["written"]) == 7
    user_page = repo.root / "vault" / "views" / "research" / "研究项目.md"
    user_page.write_text(render_document({
        "id": "user_research_view", "type": "view", "status": "manual",
        "title": "我的研究项目", "created_at": "2026-07-18T00:00:00+08:00",
        "updated_at": "2026-07-18T00:00:00+08:00", "generated_by": "user",
    }, "用户手写内容"), encoding="utf-8")
    stale = repo.root / "vault" / "views" / "research" / "旧生成页.md"
    stale.write_text(render_document({
        "id": "old_generated", "type": "view", "status": "generated",
        "title": "旧生成页", "created_at": "2026-07-18T00:00:00+08:00",
        "updated_at": "2026-07-18T00:00:00+08:00",
        "generated_by": ResearchMapService.GENERATED_BY,
    }, "stale"), encoding="utf-8")
    second_view = view_service.build()
    assert repo.rel(user_page) in second_view["skipped_non_generated"]
    assert len(second_view["unchanged"]) == 6
    assert user_page.read_text(encoding="utf-8").endswith("用户手写内容\n")
    assert repo.rel(stale) in second_view["removed_stale_generated"]
    assert not stale.exists()
    metrics = ProjectMetricsService(repo).collect()
    assert metrics["research_annotations"] == 1
    assert metrics["sources_with_why_saved"] == 1
    assert metrics["sources_without_why_saved"] == 1
    assert "system/reports/generated-*" in (Path.cwd() / ".gitignore").read_text(encoding="utf-8")


def test_m7_compile_materializes_working_without_canonical_write(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Concept: Working memory is usable before canonical promotion.", title="M7 working fixture"
    )
    raw_before = (repo.root / captured.source_path).read_bytes()
    bundle = BundleCompiler(repo).compile(captured.source_id)

    result = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))

    assert result.written and not result.exceptions
    assert (repo.root / captured.source_path).read_bytes() == raw_before
    working_path = repo.root / result.written[0]
    metadata, _ = read_document(working_path)
    assert metadata["status"] == metadata["memory_tier"] == "working"
    assert metadata["origin_proposal_id"] == bundle.proposal_id
    assert not list(repo.canonical_documents())
    repeat = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))
    assert repeat.written == [] and repeat.updated == []


def test_m7_working_write_rolls_back_on_interruption(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Atomic working rollback.", title="M7 rollback")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    proposal_path, before, _ = repo.find_document(str(bundle.proposal_id))
    original = proposal_path.read_bytes()

    def fail(phase: str) -> None:
        if phase == "working_written":
            raise RuntimeError("injected failure")

    with pytest.raises(RuntimeError, match="injected failure"):
        WorkingMemoryService(repo, failure_hook=fail).ingest_bundle(str(bundle.proposal_id))

    assert list(repo.memory_documents()) == []
    assert proposal_path.read_bytes() == original
    assert before["status"] == "pending"


def test_m7_trusted_policy_and_canonical_promotion_gate(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Reusable governed memory.", title="M7 promotion")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    result = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))
    path = repo.root / result.written[0]
    metadata, body = read_document(path)
    metadata["reuse_work_ids"] = ["work_independent_a", "work_independent_b"]
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    receipt = ConsolidationReceiptService(repo).consolidate(str(metadata["id"]))
    assert receipt["status"] == "complete"

    service = PromotionService(repo)
    promoted = service.promote_trusted(str(metadata["id"]), automatic=True)
    assert promoted["promoted"] is True
    assert not list(repo.canonical_documents())
    card = service.recommend_canonical(str(metadata["id"]), "stable reusable concept")
    assert service.list_cards({"pending"})[0]["id"] == card["promotion_id"]
    approved = service.approve_canonical(card["promotion_id"], lock=True)
    canonical, _ = read_document(repo.root / approved["path"])
    assert canonical["status"] == "canonical" and canonical["user_locked"] is True
    assert canonical["user_approved"] is True and canonical["approval_event_id"] == approved["approval_event_id"]
    assert ConsolidationReceiptService(repo).valid_for(str(canonical["id"]))["consolidation_id"] == approved["receipt_id"]
    strict = ContextPackService(repo).build("Reusable governed memory", 1200, profiles=["execution", "research"], strict_execution=True).as_dict()
    assert str(canonical["id"]) in {item["id"] for item in strict["items"]}
    assert list(repo.memory_documents()) == []


def test_canonical_promotion_recovers_exact_preimage_before_final_receipt(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Canonical recovery preimage.", title="Canonical recovery")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    written = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id)).written[0]
    path = repo.root / written
    metadata, body = read_document(path)
    metadata["reuse_work_ids"] = ["independent_a", "independent_b"]
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    ConsolidationReceiptService(repo).consolidate(str(metadata["id"]))
    PromotionService(repo).promote_trusted(str(metadata["id"]), automatic=True)
    service = PromotionService(repo)
    card = service.recommend_canonical(str(metadata["id"]))
    trusted_before = path.read_bytes()

    def fail(phase: str) -> None:
        if phase == "canonical_written":
            raise RuntimeError("injected interruption")

    with pytest.raises(RuntimeError, match="injected interruption"):
        PromotionService(repo, failure_hook=fail).approve_canonical(card["promotion_id"])

    assert path.read_bytes() == trusted_before
    assert not list(repo.canonical_documents())
    assert not PromotionService(repo).canonical_recovery.pending()


def test_canonical_promotion_rolls_forward_after_final_receipt(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Canonical recovery roll forward.", title="Canonical receipt")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    written = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id)).written[0]
    path = repo.root / written
    metadata, body = read_document(path)
    metadata["reuse_work_ids"] = ["independent_a", "independent_b"]
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    ConsolidationReceiptService(repo).consolidate(str(metadata["id"]))
    PromotionService(repo).promote_trusted(str(metadata["id"]), automatic=True)
    service = PromotionService(repo)
    card = service.recommend_canonical(str(metadata["id"]))

    def fail(phase: str) -> None:
        if phase == "canonical_receipt_completed":
            raise RuntimeError("injected interruption after receipt")

    recovered = PromotionService(repo, failure_hook=fail).approve_canonical(card["promotion_id"])

    canonical = list(repo.canonical_documents())
    assert len(canonical) == 1 and not path.exists()
    assert recovered["recovered_after_interruption"] is True
    canonical_metadata, _ = read_document(canonical[0])
    assert ConsolidationReceiptService(repo).valid_for(str(canonical_metadata["id"])) is not None
    assert not PromotionService(repo).canonical_recovery.pending()
    events = (repo.root / "system" / "logs" / "memory-events.jsonl").read_text(encoding="utf-8")
    assert events.count('"event": "promoted-canonical"') == 1


def test_m7_weak_or_contradicted_memory_stays_working(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Unreviewed idea.", title="M7 retained")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    result = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))
    object_id = read_document(repo.root / result.written[0])[0]["id"]

    evaluation = PromotionService(repo).evaluate(object_id)

    assert evaluation.eligible is False
    assert "requires a valid hash-bound consolidation receipt" in evaluation.failed_conditions
    assert PromotionService(repo).promote_trusted(object_id, automatic=True)["promoted"] is False


def test_m7_incremental_compile_reuses_working_identity(repo: Repository) -> None:
    first = CaptureService(repo).capture_text("Concept: Shared working identity", title="M7 reuse A")
    first_bundle = BundleCompiler(repo).compile(first.source_id)
    first_result = WorkingMemoryService(repo).ingest_bundle(str(first_bundle.proposal_id))
    first_path = repo.root / first_result.written[0]
    first_id = read_document(first_path)[0]["id"]

    second = CaptureService(repo).capture_text("Concept: Shared working identity", title="M7 reuse B")
    second_bundle = BundleCompiler(repo).compile(second.source_id)
    second_proposal, _ = read_document(repo.root / second_bundle.proposal_path)
    assert second_proposal["bundle_items"][0]["action"] == "update"
    second_result = WorkingMemoryService(repo).ingest_bundle(str(second_bundle.proposal_id))

    assert second_result.updated == [] and second_result.exceptions
    merged, _ = read_document(first_path)
    assert merged["id"] == first_id
    assert set(merged["source_ids"]) == {first.source_id}
    assert len(list(repo.memory_documents())) == 1


def test_m7_migration_is_dry_run_backed_up_and_idempotent(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Legacy pending candidate.", title="M7 migration")
    BundleCompiler(repo).compile(captured.source_id)
    service = ProposalGateMigration(repo)

    plan = service.plan()
    assert plan["dry_run"] is True and plan["candidate_items"] == 1
    assert list(repo.memory_documents()) == []
    applied = service.apply()
    assert applied["backup_path"] and (repo.root / applied["backup_path"]).exists()
    assert applied["migrated_working_objects"] == 1
    assert service.plan()["pending_proposals"] == 0


def test_m7_weekly_never_writes_canonical_and_drift_is_read_only(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: Weekly review candidate.", title="M7 weekly")
    bundle = BundleCompiler(repo).compile(captured.source_id)
    WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))

    report = ConsolidationService(repo).weekly()
    audit = DriftAuditService(repo).run()

    assert report["canonical_writes"] == 0
    assert not list(repo.canonical_documents())
    assert audit["writes"] == 0


def test_weekly_excludes_archived_historical_memory_from_consolidation(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Concept: routine maintenance candidate.", title="Active memory")
    active = write_m8_memory(
        repo, "concept_active_memory", "concept", "Active memory", "Active body.", [captured.source_id]
    )
    historical = write_m8_memory(
        repo, "claim_historical_memory", "claim", "Historical memory", "Historical body.", [captured.source_id]
    )
    historical_metadata, historical_body = read_document(historical)
    historical_metadata.update({"memory_tier": "historical", "status": "archived"})
    historical.write_text(render_document(historical_metadata, historical_body), encoding="utf-8")
    historical_before = historical.read_bytes()

    report = ConsolidationService(repo).weekly()

    assert str(historical_metadata["id"]) in report["historical_ids_skipped"]
    assert report["historical_objects_skipped"] == 1
    assert report["active_objects_considered"] == 1
    assert historical.read_bytes() == historical_before
    with pytest.raises(ValidationError, match="excluded from routine consolidation"):
        ConsolidationReceiptService(repo).consolidate(str(historical_metadata["id"]))
    assert active.exists()


def test_consolidate_weekly_admits_capture_only_sources_before_review(
    repo: Repository, capsys: pytest.CaptureFixture[str]
) -> None:
    captured = CaptureService(repo).capture_text(
        "Concept: Weekly catch-up candidate.", title="Weekly catch-up"
    )
    args = build_parser().parse_args(
        ["--root", str(repo.root), "consolidate", "weekly", "--admit-limit", "5"]
    )

    assert run(args) == 0
    output = json.loads(capsys.readouterr().out)

    assert output["daily_catchup"]["mode"] == "daily-consolidation"
    assert output["daily_catchup"]["compiled"][0]["source_id"] == captured.source_id
    assert output["daily_catchup"]["compiled"][0]["status"] == "working"
    assert output["objects_considered"] == 1
    assert output["canonical_writes"] == 0


def test_daily_keeps_long_unstructured_fallback_source_only(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "Paper title and author affiliation header. " * 120,
        title="Long unstructured paper",
    )

    result = ConsolidationService(repo).daily(limit=5)

    assert result["compiled"] == [{
        "source_id": captured.source_id,
        "status": "source_only",
        "proposal_id": result["compiled"][0]["proposal_id"],
        "reason": "no knowledge-safe deterministic candidate",
    }]
    assert result["compiled"][0]["proposal_id"]
    assert list(repo.memory_documents()) == []
    assert ProposalService(repo).inbox() == []
    proposal_path, proposal, _ = repo.find_document(result["compiled"][0]["proposal_id"])
    assert proposal_path.parent.name == "proposals"
    assert proposal["status"] == "source_only"
    assert proposal["compile_disposition"] == "source_only"
    assert proposal["bundle_items"] == []


def test_daily_keeps_unmarked_web_capture_source_only_even_when_short(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text(
        "A short extracted web abstract with a complete sentence. " * 4, title="Short web page"
    )
    source_path = repo.root / captured.source_path
    metadata, body = read_document(source_path)
    metadata["source_kind"] = "web"
    source_path.write_text(render_document(metadata, body), encoding="utf-8")

    result = BundleCompiler(repo).compile(captured.source_id)

    assert result.compile_disposition == "source_only"
    assert list(repo.memory_documents()) == []


def test_source_only_status_is_exposed_by_cli_and_metrics(repo: Repository, capsys: pytest.CaptureFixture[str]) -> None:
    captured = CaptureService(repo).capture_text("Unstructured article title and metadata. " * 120, title="Source-only record")
    ConsolidationService(repo).daily(limit=5)
    args = build_parser().parse_args(["--root", str(repo.root), "proposals", "--status", "source_only"])

    assert run(args) == 0
    proposals = json.loads(capsys.readouterr().out)
    metrics = ProjectMetricsService(repo).collect()
    assert len(proposals) == 1 and proposals[0]["status"] == "source_only"
    assert metrics["source_only_compile_records"] == 1
    assert metrics["sources_completed_source_only"] == 1
    assert lint(repo)["ok"] is True


def test_working_quality_review_flags_legacy_long_fallback(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    CaptureService(repo).capture_text(
        "Paper title and author affiliation header. " * 120,
        title="Legacy fallback paper",
    )
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 10000)
    result = ConsolidationService(repo).daily(limit=5)
    assert result["compiled"][0]["status"] == "working"
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 2000)

    review = ConsolidationService(repo).review_working_quality()

    assert review["flagged_count"] >= 1
    assert review["writes"] == 0
    assert review["flagged"][0]["recommended_action"] == "recompile_or_source_only"
    assert "no semantic evidence entailment" in review["flagged"][0]["reasons"]


def test_working_quality_review_flags_legacy_article_marker_false_positive(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    captured = capture_web_bytes(
        repo, "https://example.com/legacy-marker",
        b"Question: article prose was mistaken for an instruction.\n" + b"Long article body. " * 200,
        title="Legacy marker article",
    )
    monkeypatch.setattr(
        BundleCompiler,
        "_deterministic_fallback_allowed",
        lambda self, source, text, specs: any(bool(item.get("explicit_marker")) for item in specs),
    )
    compiled = ConsolidationService(repo).daily(limit=5)
    assert compiled["compiled"][0]["status"] == "working"

    review = ConsolidationService(repo).review_working_quality()

    assert review["flagged_count"] == 1
    assert review["flagged"][0]["source_ids"] == [captured.source_id]
    assert "automatic article marker misclassified as an Agent instruction" in review["flagged"][0]["reasons"]


def test_working_quality_migration_archives_with_snapshot_and_is_idempotent(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    CaptureService(repo).capture_text(
        "Paper title and author affiliation header. " * 120,
        title="Legacy migration paper",
    )
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 10000)
    ConsolidationService(repo).daily(limit=5)
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 2000)
    migration = WorkingQualityMigration(repo)
    plan = migration.plan()
    canonical_before = list(repo.canonical_documents())

    assert plan["candidate_count"] >= 1
    first = migration.apply()
    second = migration.apply()

    assert first["archived_count"] == plan["candidate_count"]
    assert first["remaining_flagged"] == 0
    assert second["archived_count"] == 0
    assert second["candidate_count"] == 0
    manifest_path = repo.root / first["backup_path"] / "manifest.json"
    assert manifest_path.exists()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["phase"] == "completed"
    assert all(item["status"] == "applied" and item["sha256_after"] for item in manifest["objects"])
    for object_id in first["archived_ids"]:
        _, metadata, _ = repo.find_document(object_id)
        assert metadata["status"] == "archived"
        assert metadata["memory_tier"] == "historical"
        assert metadata["quality_review_status"] == "source_only"
        assert list((repo.root / "vault/archive/versions" / object_id).glob("*.md"))
    assert list(repo.canonical_documents()) == canonical_before
    assert lint(repo)["ok"] is True


def test_working_quality_migration_verify_and_restore_are_guarded(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    CaptureService(repo).capture_text("Legacy fallback body. " * 120, title="Restore migration")
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 10000)
    ConsolidationService(repo).daily(limit=5)
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 2000)
    migration = WorkingQualityMigration(repo)
    applied = migration.apply()
    object_id = applied["archived_ids"][0]

    verified = migration.verify(applied["migration_id"])
    preview = migration.restore(applied["migration_id"], dry_run=True)
    restored = migration.restore(applied["migration_id"])

    assert verified["ok"] is True
    assert preview["restore_candidates"] == applied["archived_ids"]
    assert object_id in restored["restored"]
    _, metadata, _ = repo.find_document(object_id)
    assert metadata["memory_tier"] == "working" and metadata["status"] == "working"
    assert migration.restore(applied["migration_id"])["blocked"] is True


def test_working_quality_migration_detects_post_image_change_and_resumes_same_manifest(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    CaptureService(repo).capture_text("Legacy resume body. " * 120, title="Resume migration")
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 10000)
    ConsolidationService(repo).daily(limit=5)
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 2000)
    migration = WorkingQualityMigration(repo)
    original_append = repo.append_event
    calls = 0

    def interrupted_append(name: str, payload: dict[str, object]) -> None:
        nonlocal calls
        if payload.get("event") == "working-quality-archived":
            calls += 1
            if calls == 1:
                raise RuntimeError("injected interruption")
        original_append(name, payload)

    monkeypatch.setattr(repo, "append_event", interrupted_append)
    with pytest.raises(RuntimeError, match="injected interruption"):
        migration.apply()
    manifests = list((repo.root / "data" / "backups").glob("working_quality_*/manifest.json"))
    assert len(manifests) == 1

    monkeypatch.setattr(repo, "append_event", original_append)
    resumed = migration.apply()
    assert resumed["migration_id"] == json.loads(manifests[0].read_text(encoding="utf-8"))["migration_id"]
    assert resumed["archived_count"] == 0
    assert migration.verify(resumed["migration_id"])["ok"] is True

    object_id = json.loads(manifests[0].read_text(encoding="utf-8"))["objects"][0]["object_id"]
    path, metadata, body = repo.find_document(object_id)
    metadata["updated_by"] = "manual-edit"
    path.write_text(render_document(metadata, body), encoding="utf-8")
    assert migration.verify(resumed["migration_id"])["ok"] is False
    assert migration.restore(resumed["migration_id"])["blocked"] is True


def test_working_quality_migration_legacy_manifest_requires_explicit_safety_baseline(
    repo: Repository, monkeypatch: pytest.MonkeyPatch
) -> None:
    CaptureService(repo).capture_text("Legacy baseline body. " * 120, title="Legacy baseline")
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 10000)
    ConsolidationService(repo).daily(limit=5)
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 2000)
    migration = WorkingQualityMigration(repo)
    applied = migration.apply()
    manifest_path = repo.root / applied["backup_path"] / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.pop("canonical_sha256")
    for item in manifest["objects"]:
        item.pop("sha256_after")
        item.pop("snapshot_path")
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    assert migration.verify(applied["migration_id"])["ok"] is False
    upgraded = migration.upgrade_legacy_manifest(applied["migration_id"])
    assert upgraded["legacy_safety_baseline"] is True
    assert migration.verify(applied["migration_id"])["ok"] is True


def test_working_quality_restore_refuses_new_working_revision(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    captured = CaptureService(repo).capture_text("Legacy revision body. " * 120, title="Revision guard")
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 10000)
    ConsolidationService(repo).daily(limit=5)
    monkeypatch.setattr(BundleCompiler, "UNSTRUCTURED_FALLBACK_MAX_CHARS", 2000)
    migration = WorkingQualityMigration(repo)
    applied = migration.apply()
    object_id = applied["archived_ids"][0]
    revision = write_m8_memory(
        repo, "revision_restore_guard", "claim", "New revision", "A later revision.", [captured.source_id]
    )
    revision_metadata, revision_body = read_document(revision)
    revision_metadata["revision_of"] = object_id
    revision.write_text(render_document(revision_metadata, revision_body), encoding="utf-8")

    restored = migration.restore(applied["migration_id"], dry_run=True)
    assert restored["blocked"] is True
    assert any("new working revision exists" in conflict for conflict in restored["conflicts"])


def test_m7_cli_surface_parses_governance_commands() -> None:
    assert build_parser().parse_args(["consolidate", "daily"]).consolidate_command == "daily"
    weekly_args = build_parser().parse_args(["consolidate", "weekly"])
    assert weekly_args.admit_limit == 25
    assert weekly_args.skip_daily_admission is False
    assert build_parser().parse_args(["audit", "drift"]).audit_command == "drift"
    assert build_parser().parse_args(["migrate", "proposal-gate-to-promotion", "--dry-run"]).dry_run
    assert build_parser().parse_args(["promote", "concept_x", "--to", "canonical", "--reason", "important"]).to == "canonical"
    assert build_parser().parse_args([
        "evolve", "claim_x", "--change-type", "contradict", "--from-file", "candidate.md",
        "--reason", "human review", "--force-contest",
    ]).force_contest is True


def test_m7_exception_identity_includes_source_context(repo: Repository) -> None:
    service = ExceptionService(repo)
    first = service.create("daily-compile", "first", ["same failure"], source_ids=["source_a"], context={"source_id": "source_a"})
    second = service.create("daily-compile", "second", ["same failure"], source_ids=["source_b"], context={"source_id": "source_b"})
    assert first != second


def write_m8_memory(
    repo: Repository, object_id: str, object_type: str, title: str, body: str,
    source_ids: list[str], *, tier: str = "working", epistemic_status: str = "unknown",
) -> Path:
    timestamp = "2026-07-17T12:00:00+08:00"
    metadata = {
        "id": object_id, "type": object_type, "status": tier, "memory_tier": tier,
        "epistemic_status": epistemic_status, "title": title,
        "created_at": timestamp, "updated_at": timestamp, "aliases": [], "tags": [],
        "domains": [], "confidence": "unknown", "source_ids": source_ids, "relations": [],
        "created_by": "m8-test", "updated_by": "m8-test", "consolidation_count": 0,
        "promotion_history": [], "trust_score": 0, "trust_reasons": [], "memory_schema_version": 2,
    }
    path = repo.root / "vault" / "memory" / object_type / f"{object_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    return path


def write_m8_claim(repo: Repository, object_id: str = "claim_m8") -> tuple[Path, str]:
    captured = CaptureService(repo).capture_text(
        "The primary source states that bounded evidence supports the claim.", title="M8 primary source"
    )
    _, source_metadata, _ = repo.find_document(captured.source_id)
    path = write_m8_memory(
        repo, object_id, "claim", "Bounded evidence supports the claim",
        "Bounded evidence supports the claim.", [captured.source_id], epistemic_status="provisional",
    )
    metadata, body = read_document(path)
    metadata.update({
        "atomicity_status": "atomic", "evidence_coverage": "full",
        "evidence_entailment": "full", "extraction_quality": "good",
        "epistemic_source_authority": "primary", "applicability": ["bounded fixture"],
        "claim_confidence": "medium", "quote_verification": "exact",
        "evidence": [{
            "source_id": captured.source_id, "stance": "supports", "location": "body",
            "excerpt": "bounded evidence supports the claim", "reason": "direct support",
            "evidence_id": f"evidence_{object_id}", "evidence_kind": "quote",
            "verification_status": "verified", "input_sha256": source_metadata["content_sha256"],
            "extraction_id": f"extraction_{object_id}", "span_start": 0, "span_end": 44,
            "original_text": "bounded evidence supports the claim",
        }],
    })
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    return path, captured.source_id


def test_m90_annotation_and_activation_do_not_invalidate_receipt_or_trust(repo: Repository) -> None:
    target, _ = write_m8_claim(repo, "claim_m90_receipt")
    receipt_service = ConsolidationReceiptService(repo)
    receipt = receipt_service.consolidate("claim_m90_receipt")
    assert receipt["status"] == "complete"
    current = receipt_service.valid_for("claim_m90_receipt")
    assert current is not None
    target_hash = sha256_bytes(target.read_bytes())
    annotation = ResearchAnnotationService(repo).create(
        "research_note", target_ids=["claim_m90_receipt"], note="用户研究方向，不是答案。",
        research_projects=["scientific-memory"],
    )
    ActivationService(repo).record(
        "claim_m90_receipt", kind="used", project_id="scientific-memory",
        reason="边界测试", event_id="activation_m90_receipt_boundary",
    )
    assert annotation["id"]
    assert sha256_bytes(target.read_bytes()) == target_hash
    assert receipt_service.valid_for("claim_m90_receipt") is not None
    _, metadata, _ = repo.find_document("claim_m90_receipt")
    assert metadata["memory_tier"] == "working"
    assert metadata["epistemic_status"] == "provisional"
    assert metadata["trust_score"] == 0


def test_m90_agent_cannot_overwrite_user_annotation_fields(repo: Repository) -> None:
    captured = capture_web_bytes(repo, "https://example.com/user-field-boundary")
    with pytest.raises(ValidationError, match="Agent interpretation"):
        ResearchAnnotationService(repo).create(
            "capture_intent", target_ids=[captured.source_id], why_saved="agent rewrite",
            created_by="agent",
        )
    assert ResearchAnnotationService(repo).documents() == []


def test_m8_consolidation_receipt_is_real_and_hash_bound(repo: Repository) -> None:
    path, _ = write_m8_claim(repo)
    object_id = read_document(path)[0]["id"]
    assert ConsolidationReceiptService(repo).valid_for(object_id) is None
    receipt = ConsolidationReceiptService(repo).consolidate(object_id)
    assert receipt["receipt_schema_version"] == 2
    assert receipt["status"] == "complete"
    assert all(receipt["checks"].values())
    assert all(receipt["check_details"][key]["findings"] for key in receipt["checks"])
    entailment = receipt["check_details"]["evidence_entailment_rechecked"]
    assert entailment["execution_status"] == "completed"
    assert entailment["validation_outcome"] == "passed"
    assert entailment["semantic_recheck_performed"] is True
    assert receipt["check_details"]["source_independence_checked"]["validation_outcome"] == "not_applicable"
    assert any("record_sha256" in item for item in receipt["check_details"]["provenance_revalidated"]["findings"])
    assert any("drift_reports:" in item for item in receipt["check_details"]["drift_checked"]["findings"])
    assert receipt["object_sha256_after"] == sha256_bytes(path.read_bytes())
    assert receipt["consolidation_fingerprint"] == ConsolidationReceiptService(repo).fingerprint(object_id)
    assert ConsolidationReceiptService(repo).valid_for(object_id)["consolidation_id"] == receipt["consolidation_id"]
    metadata, body = read_document(path)
    metadata["confidence"] = "low"
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    assert ConsolidationReceiptService(repo).valid_for(object_id) is None


def test_receipt_v1_is_retained_but_regenerated_as_v2(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_receipt_v1_upgrade")
    service = ConsolidationReceiptService(repo)
    timestamp = "2026-07-17T10:00:00+08:00"
    legacy = {
        "id": "consolidation_legacy_v1", "type": "consolidation_receipt", "status": "complete",
        "title": "Legacy receipt", "created_at": timestamp, "updated_at": timestamp,
        "consolidation_id": "consolidation_legacy_v1", "object_id": "claim_receipt_v1_upgrade",
        "object_sha256_after": sha256_bytes(path.read_bytes()), "completed_at": timestamp,
        "checks": {key: True for key in REQUIRED_RECEIPT_CHECKS}, "result": "unchanged",
    }
    legacy_path = service.directory / "consolidation-consolidation_legacy_v1.md"
    repo.immutable_write(legacy_path, render_document(legacy, "# Legacy Receipt\n").encode("utf-8"))

    receipt = service.consolidate("claim_receipt_v1_upgrade")

    assert receipt["reused"] is False and receipt["receipt_schema_version"] == 2
    assert receipt["consolidation_id"] != legacy["consolidation_id"]
    assert legacy_path.exists() and service.valid_for("claim_receipt_v1_upgrade")["consolidation_id"] == receipt["consolidation_id"]


def test_receipt_v2_reuse_requires_full_current_fingerprint(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    path, source_id = write_m8_claim(repo, "claim_receipt_fingerprint")
    service = ConsolidationReceiptService(repo)
    first = service.consolidate("claim_receipt_fingerprint")
    reused = service.consolidate("claim_receipt_fingerprint")
    assert reused["reused"] is True and reused["consolidation_id"] == first["consolidation_id"]

    source_path, source, source_body = repo.find_document(source_id)
    source["comment"] = "source metadata changed"
    source_path.write_text(render_document(source, source_body), encoding="utf-8")
    repo.rebuild_index()
    assert service.valid_for("claim_receipt_fingerprint") is None
    source_changed = service.consolidate("claim_receipt_fingerprint")
    assert source_changed["reused"] is False and source_changed["consolidation_id"] != first["consolidation_id"]

    monkeypatch.setattr("global_memory.consolidation.POLICY_VERSION", "trusted-promotion-v3-test-change")
    assert service.valid_for("claim_receipt_fingerprint") is None
    policy_changed = service.consolidate("claim_receipt_fingerprint")
    assert policy_changed["reused"] is False and policy_changed["consolidation_id"] != source_changed["consolidation_id"]


def test_incoming_contradiction_invalidates_receipt_and_strict_execution(repo: Repository) -> None:
    path_a, _ = write_m8_claim(repo, "claim_incoming_contradiction_a")
    receipts = ConsolidationReceiptService(repo)
    first = receipts.consolidate("claim_incoming_contradiction_a")
    assert receipts.valid_for("claim_incoming_contradiction_a") is not None
    assert PromotionService(repo).promote_trusted("claim_incoming_contradiction_a", automatic=True)["promoted"]

    path_b, _ = write_m8_claim(repo, "claim_incoming_contradiction_b")
    metadata_b, body_b = read_document(path_b)
    metadata_b["relations"] = [{
        "type": "contradicts", "target_id": "claim_incoming_contradiction_a",
        "reason": "independent contrary result", "status": "active",
        "confidence": "high", "created_by": "test",
    }]
    path_b.write_text(render_document(metadata_b, body_b), encoding="utf-8")
    repo.rebuild_index()

    assert receipts.valid_for("claim_incoming_contradiction_a") is None
    second = receipts.consolidate("claim_incoming_contradiction_a")
    assert second["consolidation_id"] != first["consolidation_id"]
    assert second["contradiction_search"]["validation_outcome"] == "contested"
    assert second["contradiction_search"]["incoming"][0]["source_id"] == "claim_incoming_contradiction_b"
    assert PromotionService(repo).evaluate("claim_incoming_contradiction_a").eligible is False
    strict = ContextPackService(repo).build(
        "Bounded evidence", 1200, profiles=["execution"], strict_execution=True,
    ).as_dict()
    assert "claim_incoming_contradiction_a" not in {item["id"] for item in strict["items"]}


def test_relation_fingerprint_failure_cannot_create_a_usable_receipt(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    write_m8_claim(repo, "claim_relation_fingerprint_failure")
    service = ConsolidationReceiptService(repo)
    monkeypatch.setattr(repo, "related", lambda _: (_ for _ in ()).throw(RuntimeError("index unavailable")))

    with pytest.raises(RuntimeError, match="index unavailable"):
        service.fingerprint("claim_relation_fingerprint_failure")
    receipt = service.consolidate("claim_relation_fingerprint_failure")
    assert receipt["status"] == "failed"
    assert receipt["consolidation_fingerprint"] == {}
    assert service.valid_for("claim_relation_fingerprint_failure") is None


def test_legacy_contradiction_excerpt_creates_candidate_without_contesting_trusted(repo: Repository) -> None:
    path, source_a = write_m8_claim(repo, "claim_legacy_contradiction")
    ConsolidationReceiptService(repo).consolidate("claim_legacy_contradiction")
    assert PromotionService(repo).promote_trusted("claim_legacy_contradiction", automatic=True)["promoted"]
    source_b = CaptureService(repo).capture_text("Contrary result", title="Contrary evidence")

    result = KnowledgeEvolutionService(repo).apply(
        "claim_legacy_contradiction",
        {"source_ids": [source_b.source_id], "evidence": [{
            "source_id": source_b.source_id, "stance": "contradicts", "location": "body",
            "excerpt": "Contrary result", "reason": "legacy excerpt only",
        }]},
        read_document(path)[1], change_type="contradict", reason="legacy evidence requires review",
        trigger_source=source_b.source_id,
    )

    current, _ = read_document(path)
    assert result["action"] == "contradiction_candidate"
    assert current["epistemic_status"] != "contested"
    exception = next(item for item in ExceptionService(repo).list() if item["id"] == result["exception_id"])
    assert exception["exception_kind"] == "contradiction_candidate"


def test_force_contest_requires_source_and_preserves_unverified_boundary(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_forced_contradiction")
    ConsolidationReceiptService(repo).consolidate("claim_forced_contradiction")
    assert PromotionService(repo).promote_trusted("claim_forced_contradiction", automatic=True)["promoted"]
    source = CaptureService(repo).capture_text("Contrary observation", title="Forced contrary evidence")

    result = KnowledgeEvolutionService(repo).apply(
        "claim_forced_contradiction",
        {"source_ids": [source.source_id], "evidence": [{
            "source_id": source.source_id, "stance": "contradicts", "location": "body",
            "excerpt": "Contrary observation", "reason": "human escalation of legacy excerpt",
        }]},
        read_document(path)[1], change_type="contradict", reason="human reviewed and forced contest",
        trigger_source=source.source_id, force_contest=True,
    )

    current, _ = read_document(path)
    assert result["action"] == "contradict"
    assert current["epistemic_status"] == "contested"
    exceptions = ExceptionService(repo).list()
    assert [item["exception_kind"] for item in exceptions] == ["forced_contradiction"]
    assert exceptions[0]["context"]["verification"] == "not_verified"


def test_promotion_requires_receipt_semantic_check_details(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_receipt_semantics")
    receipt = ConsolidationReceiptService(repo).consolidate("claim_receipt_semantics")
    assert receipt["check_details"]["evidence_entailment_rechecked"]["semantic_recheck_performed"] is True
    assert PromotionService(repo).evaluate("claim_receipt_semantics").eligible is True
    promoted = PromotionService(repo).promote_trusted("claim_receipt_semantics", automatic=True)
    assert promoted["promoted"] is True

    # A current-looking Receipt without the semantic proof must not promote a claim.
    receipt_path, receipt_metadata, receipt_body = ConsolidationReceiptService(repo).load(promoted["receipt_id"])
    receipt_metadata["check_details"]["evidence_entailment_rechecked"]["semantic_recheck_performed"] = False
    receipt_path.write_text(render_document(receipt_metadata, receipt_body), encoding="utf-8")
    assert PromotionService(repo).evaluate("claim_receipt_semantics").eligible is False
    strict = ContextPackService(repo).build(
        "Bounded evidence", 1200, profiles=["execution"], strict_execution=True,
    ).as_dict()
    assert "claim_receipt_semantics" not in {item["id"] for item in strict["items"]}
    assert ProjectMetricsService(repo).collect()["trusted_v3_qualified"] == 0


def test_context_strict_execution_reports_receipt_policy(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_m81_context")
    ConsolidationReceiptService(repo).consolidate("claim_m81_context")
    PromotionService(repo).promote_trusted("claim_m81_context", automatic=True)
    pack = ContextPackService(repo).build(
        "Bounded evidence", 1200, profiles=["execution"], strict_execution=True,
    ).as_dict()
    item = next(item for item in pack["items"] if item["id"] == "claim_m81_context")
    assert item["receipt_state"] == "current_v2"
    assert item["policy_state"] == "execution_strict"


def test_trusted_promotion_recovery_rolls_back_staged_object(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_m81_recovery")
    before = path.read_bytes()
    metadata, body = read_document(path)
    metadata.update({"status": "trusted", "memory_tier": "trusted"})
    staged = render_document(metadata, body)
    recovery = TrustedPromotionRecoveryManager(repo)
    journal = recovery.prepare("promotion_m81_recovery", path, before, staged)
    path.write_bytes(staged.encode("utf-8"))
    recovery.checkpoint(journal, "staged")

    result = recovery.recover_all()

    assert result["blocked"] == []
    assert result["recovered"][0]["status"] == "rolled_back"
    assert path.read_bytes() == before


def test_governed_recovery_finalizes_receipt_completed_event_once(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_m81_recovery_finalize")
    before = path.read_bytes()
    metadata, body = read_document(path)
    metadata["comment"] = "durable staged mutation"
    staged = render_document(metadata, body)
    operation_id = "evolution_m81_finalize"
    event = {"event": "knowledge-support", "object_id": "claim_m81_recovery_finalize"}
    recovery = TrustedPromotionRecoveryManager(repo)
    journal = recovery.prepare(
        operation_id, path, before, staged, operation="trusted_support", event=event,
    )
    path.write_bytes(staged.encode("utf-8"))
    recovery.checkpoint(journal, "staged")
    receipt = ConsolidationReceiptService(repo).consolidate(
        "claim_m81_recovery_finalize", result="supported", rebuild_index=False,
    )
    recovery.checkpoint(journal, "receipt_completed", receipt["consolidation_id"])

    result = recovery.recover_all()

    assert result["blocked"] == [] and result["recovered"][0]["status"] == "finalized"
    assert sha256_bytes(path.read_bytes()) == receipt["object_sha256_after"]
    events = (repo.root / "system/logs/memory-events.jsonl").read_text(encoding="utf-8")
    assert events.count(f'"recovery_operation_id": "{operation_id}"') == 1
    assert recovery.pending() == []


def test_governed_recovery_rolls_forward_receipt_written_before_checkpoint(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_m812_receipt_before_checkpoint")
    before = path.read_bytes()
    metadata, body = read_document(path)
    metadata["comment"] = "durable committed mutation"
    staged = render_document(metadata, body)
    operation_id = "support_m812_missing_checkpoint"
    event = {"event": "knowledge-support", "object_id": "claim_m812_receipt_before_checkpoint"}
    recovery = TrustedPromotionRecoveryManager(repo)
    journal = recovery.prepare(operation_id, path, before, staged, operation="trusted_support", event=event)
    path.write_bytes(staged.encode("utf-8"))
    recovery.checkpoint(journal, "staged")
    receipt = ConsolidationReceiptService(repo).consolidate(
        "claim_m812_receipt_before_checkpoint", result="supported", rebuild_index=False,
    )

    result = recovery.recover_all()

    assert result["blocked"] == []
    assert result["recovered"][0]["status"] == "rolled_forward_after_missing_checkpoint"
    assert path.read_bytes() != before
    assert ConsolidationReceiptService(repo).valid_for("claim_m812_receipt_before_checkpoint")["consolidation_id"] == receipt["consolidation_id"]
    events = (repo.root / "system/logs/memory-events.jsonl").read_text(encoding="utf-8")
    assert events.count(f'"recovery_operation_id": "{operation_id}"') == 1


def test_governed_recovery_blocks_fake_or_stale_receipt(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_m812_recovery_fake_receipt")
    before = path.read_bytes()
    metadata, body = read_document(path)
    metadata["comment"] = "staged without matching receipt"
    staged = render_document(metadata, body)
    recovery = TrustedPromotionRecoveryManager(repo)
    journal = recovery.prepare("support_m812_fake", path, before, staged, operation="trusted_support")
    path.write_bytes(staged.encode("utf-8"))
    recovery.checkpoint(journal, "staged")
    recovery.checkpoint(journal, "receipt_completed", "consolidation_missing")

    result = recovery.recover_all()

    assert result["recovered"] == [] and result["blocked"]
    assert path.read_bytes() == staged.encode("utf-8")
    assert journal.exists()


def test_m81_test_functions_do_not_reference_object_id_before_assignment() -> None:
    import ast

    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    targets = {
        "test_m8_consolidation_receipt_is_real_and_hash_bound",
        "test_trusted_promotion_recovery_rolls_back_staged_object",
    }
    found = set()
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef) or node.name not in targets:
            continue
        found.add(node.name)
        assigned = {arg.arg for arg in node.args.args}
        for statement in node.body:
            loads = {
                child.id for child in ast.walk(statement)
                if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load)
            }
            assert "object_id" not in loads or "object_id" in assigned, node.name
            assigned.update(
                child.id for child in ast.walk(statement)
                if isinstance(child, ast.Name) and isinstance(child.ctx, (ast.Store, ast.Param))
            )
    assert found == targets


def test_m8_incomplete_receipt_and_failed_search_block_promotion(repo: Repository, monkeypatch: pytest.MonkeyPatch) -> None:
    path, _ = write_m8_claim(repo, "claim_m8_failed")
    metadata, body = read_document(path)
    metadata["evidence"] = []
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    failed = ConsolidationReceiptService(repo).consolidate("claim_m8_failed")
    assert failed["status"] == "failed"
    repeated = ConsolidationReceiptService(repo).consolidate("claim_m8_failed")
    assert repeated["reused"] is False
    assert repeated["consolidation_id"] != failed["consolidation_id"]
    assert PromotionService(repo).evaluate("claim_m8_failed").eligible is False

    path2, _ = write_m8_claim(repo, "claim_m8_search")
    monkeypatch.setattr(repo, "related", lambda _: (_ for _ in ()).throw(RuntimeError("search unavailable")))
    failed_search = ConsolidationReceiptService(repo).consolidate("claim_m8_search")
    assert failed_search["checks"]["contradiction_search_completed"] is False
    assert failed_search["status"] == "failed"


def test_weekly_high_drift_creates_exception_without_key_error(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_m81_high_drift")
    metadata, body = read_document(path)
    metadata["claim_confidence"] = "high"
    metadata["evidence_entailment"] = "partial"
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    report = ConsolidationService(repo).weekly()

    assert report["drift"]["high_severity"] >= 1
    assert any(item["exception_kind"] == "memory-drift" for item in ExceptionService(repo).list())


def test_m8_tier_and_epistemic_status_are_orthogonal(repo: Repository) -> None:
    source = CaptureService(repo).capture_text("durable exploration", title="durable exploration")
    cases = {
        "question": "open_question", "hypothesis": "hypothetical", "analogy": "exploratory_analogy",
    }
    for object_type, epistemic in cases.items():
        path = write_m8_memory(repo, f"{object_type}_m8", object_type, object_type, object_type, [source.source_id], epistemic_status=epistemic)
        object_id = read_document(path)[0]["id"]
        if object_type == "analogy":
            metadata, body = read_document(path)
            metadata["where_it_breaks"] = ["not factual equivalence"]
            path.write_text(render_document(metadata, body), encoding="utf-8")
            repo.rebuild_index()
        ConsolidationReceiptService(repo).consolidate(object_id)
        PromotionService(repo).promote_trusted(object_id, automatic=False, reason="durable exploration")
        promoted, _ = read_document(path)
        assert promoted["memory_tier"] == "trusted"
        assert promoted["epistemic_status"] == epistemic
        assert promoted["qualification_scope"] == {
            "question": "durable_question", "hypothesis": "exploratory_hypothesis",
            "analogy": "exploratory_analogy",
        }[object_type]
    assert truth_layer({"type": "claim", "status": "mystery"}) == "unknown"


def test_m8_trusted_support_revision_conflict_and_demotion_are_explicit(repo: Repository) -> None:
    path, source_a = write_m8_claim(repo, "claim_m8_evolve")
    ConsolidationReceiptService(repo).consolidate("claim_m8_evolve")
    PromotionService(repo).promote_trusted("claim_m8_evolve", automatic=True)
    trusted_before, trusted_body = read_document(path)
    trust_score = trusted_before["trust_score"]

    source_b = CaptureService(repo).capture_text("Independent support.", title="support B")
    support = KnowledgeEvolutionService(repo).apply(
        "claim_m8_evolve", {"source_ids": [source_b.source_id], "evidence": [{
            "source_id": source_b.source_id, "stance": "supports", "location": "body",
            "excerpt": "Independent support", "reason": "additional support",
        }]}, trusted_body, change_type="support", reason="new supporting evidence", trigger_source=source_b.source_id,
    )
    supported, _ = read_document(path)
    assert supported["memory_tier"] == "trusted" and supported["trust_score"] == trust_score
    assert set(supported["source_ids"]) == {source_a, source_b.source_id}
    assert support["receipt_id"]

    original_bytes = path.read_bytes()
    revision = KnowledgeEvolutionService(repo).apply(
        "claim_m8_evolve", {"source_ids": [source_b.source_id]}, "A refined statement.",
        change_type="refine", reason="scope changed", trigger_source=source_b.source_id,
    )
    assert path.read_bytes() == original_bytes
    revision_metadata, _ = read_document(repo.root / revision["revision_path"])
    assert revision_metadata["memory_tier"] == "working" and revision_metadata["needs_revalidation"] is True

    conflict = KnowledgeEvolutionService(repo).apply(
        "claim_m8_evolve", {"source_ids": [source_b.source_id], "evidence": [{
            "source_id": source_b.source_id, "stance": "contradicts", "location": "body",
            "evidence_id": "evidence_typed_conflict", "evidence_kind": "paraphrase",
            "verification_status": "verified", "input_sha256": "fixture", "section": "results",
            "interpretation": "Independent support conflicts with the previous scope", "reason": "primary evidence conflicts",
        }]}, trusted_body,
        change_type="contradict", reason="primary evidence conflicts", trigger_source=source_b.source_id,
    )
    contested, _ = read_document(path)
    assert contested["memory_tier"] == "trusted" and contested["epistemic_status"] == "contested"
    assert conflict["exception_id"]
    demotion = PromotionService(repo).demote_working("claim_m8_evolve", "user-approved demotion")
    assert demotion["demotion_id"] and (repo.root / demotion["event_path"]).exists()


def test_working_metadata_only_update_merges_retrieval_metadata_without_body_change(repo: Repository) -> None:
    captured = CaptureService(repo).capture_text("Alias provenance", title="Alias source")
    path = write_m8_memory(
        repo, "concept_metadata_aliases", "concept", "跨语言概念",
        "The governed semantic body remains unchanged.", [captured.source_id],
    )
    before, before_body = read_document(path)
    before["aliases"] = ["existing alias"]
    path.write_text(render_document(before, before_body), encoding="utf-8")
    repo.rebuild_index()

    result = KnowledgeEvolutionService(repo).apply(
        "concept_metadata_aliases",
        {
            "aliases": ["existing alias", "cross-language concept"],
            "tags": ["retrieval"], "domains": ["knowledge-systems"],
            "source_ids": [captured.source_id],
        },
        "This candidate body must not replace the governed statement.",
        change_type="metadata_only", reason="add bilingual retrieval metadata",
        trigger_source=captured.source_id,
    )
    updated, updated_body = read_document(path)

    assert result["change"]["changed_fields"] == ["aliases", "tags", "domains"]
    assert updated["aliases"] == ["existing alias", "cross-language concept"]
    assert updated["tags"] == ["retrieval"] and updated["domains"] == ["knowledge-systems"]
    assert updated_body == before_body and updated["memory_tier"] == "working"


@pytest.mark.parametrize("change_type", ["support", "metadata_only", "refine", "limit", "contradict", "supersede"])
def test_canonical_evolution_always_creates_proposal_without_direct_write(
    repo: Repository, change_type: str,
) -> None:
    object_id = f"claim_canonical_gate_{change_type}"
    memory_path, source_id = write_m8_claim(repo, object_id)
    metadata, current_body = read_document(memory_path)
    metadata.update({"status": "confirmed", "memory_tier": "canonical", "epistemic_status": "supported"})
    canonical_path = repo.root / "vault/knowledge/claims" / memory_path.name
    canonical_path.parent.mkdir(parents=True, exist_ok=True)
    canonical_path.write_text(render_document(metadata, current_body), encoding="utf-8")
    memory_path.unlink()
    repo.rebuild_index()
    before = canonical_path.read_bytes()
    incoming = {"source_ids": [source_id]}
    if change_type == "contradict":
        incoming["evidence"] = [{
            "source_id": source_id, "stance": "contradicts", "location": "body",
            "evidence_id": "evidence_canonical_conflict", "evidence_kind": "paraphrase",
            "verification_status": "verified", "input_sha256": "fixture", "section": "results",
            "interpretation": "bounded contradictory evidence", "reason": "fixture conflict",
        }]

    result = KnowledgeEvolutionService(repo).apply(
        object_id, incoming, "Candidate body changed.", change_type=change_type,
        reason=f"canonical {change_type} must be reviewed", trigger_source=source_id,
    )

    assert result["action"] == "canonical_proposal" and result["proposal_id"]
    assert canonical_path.read_bytes() == before
    proposal_path, proposal, _ = repo.find_document(result["proposal_id"])
    assert proposal["action"] == "update" and proposal["target_id"] == object_id
    assert proposal_path.exists()


def test_m8_incremental_a_b_c_and_execution_context(repo: Repository) -> None:
    path, source_a = write_m8_claim(repo, "claim_m8_abc")
    receipt_a = ConsolidationReceiptService(repo).consolidate("claim_m8_abc")
    source_b = CaptureService(repo).capture_text("B supports A.", title="B")
    b = KnowledgeEvolutionService(repo).apply(
        "claim_m8_abc", {"source_ids": [source_b.source_id], "evidence": [{
            "source_id": source_b.source_id, "stance": "supports", "location": "body",
            "excerpt": "B supports A", "reason": "support",
        }]}, read_document(path)[1], change_type="support", reason="B support", trigger_source=source_b.source_id,
    )
    source_c = CaptureService(repo).capture_text("C contradicts A.", title="C")
    c = KnowledgeEvolutionService(repo).apply(
        "claim_m8_abc", {"source_ids": [source_c.source_id], "evidence": [{
            "source_id": source_c.source_id, "stance": "contradicts", "location": "body",
            "evidence_id": "evidence_abc_conflict", "evidence_kind": "paraphrase",
            "verification_status": "verified", "input_sha256": "fixture", "section": "results",
            "interpretation": "C contradicts A", "reason": "C limitation",
        }]}, read_document(path)[1],
        change_type="contradict", reason="C limitation", trigger_source=source_c.source_id,
    )
    current, _ = read_document(path)
    assert receipt_a["consolidation_id"] != b["receipt_id"] != c["receipt_id"]
    assert b["updated_object_count"] > 0 and b["knowledge_reuse_count"] > 0
    assert current["epistemic_status"] == "contested" and c["exception_id"]
    research = ContextPackService(repo).build("Bounded evidence", 2000, profiles=["research"]).as_dict()
    item = next(item for item in research["items"] if item["id"] == "claim_m8_abc")
    assert item["memory_tier"] == "working" and item["epistemic_status"] == "contested"
    execution = ContextPackService(repo).build("Bounded evidence", 2000, profiles=["execution"]).as_dict()
    assert "claim_m8_abc" not in {item["id"] for item in execution["items"]}


def test_m8_drift_migration_and_metrics(repo: Repository) -> None:
    drift = DriftAuditService(repo)
    reports = drift.compare(
        "claim_drift", "The variables may be correlated.", "The variables prove and cause the outcome.",
    )
    assert {item["drift_type"] for item in reports} >= {"uncertainty-erasure", "correlation-to-causation"}
    assert all(item["severity"] == "high" for item in reports)

    path, _ = write_m8_claim(repo, "claim_m8_migration")
    metadata, body = read_document(path)
    metadata.pop("memory_tier")
    metadata.pop("epistemic_status")
    metadata["status"] = "contested"
    path.write_text(render_document(metadata, body), encoding="utf-8")
    migration = EpistemicStatusMigration(repo)
    assert migration.plan()["documents_to_change"] == 1
    applied = migration.apply()
    assert applied["backup_path"] and migration.verify()["ok"]
    migrated, _ = read_document(path)
    assert migrated["memory_tier"] == "working" and migrated["epistemic_status"] == "contested"
    assert migration.apply()["idempotent_noop"] is True
    metrics = ProjectMetricsService(repo).collect()
    assert metrics["working"] == 1 and metrics["contested"] == 1


def test_trust_requalification_marks_legacy_trusted_without_demotion(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_requal_mark")
    metadata, body = read_document(path)
    metadata.update({
        "status": "trusted", "memory_tier": "trusted", "legacy_status": "trusted",
        "trust_score": 88, "trust_reasons": ["legacy qualified"],
        "promotion_history": [{
            "promotion_id": "promotion_legacy", "from_status": "working", "to_status": "trusted",
            "policy_version": "trusted-promotion-v1", "promoted_at": "2026-07-16T12:00:00+08:00",
        }],
    })
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    migration = TrustPolicyRequalificationMigration(repo)
    result = migration.apply()
    current, current_body = read_document(path)

    assert result["documents_changed"] == 1 and result["canonical_content_writes"] == 0
    assert current_body == body
    assert current["memory_tier"] == "trusted" and current["status"] == "trusted"
    assert current["needs_policy_requalification"] is True
    assert current["trust_policy_version"] == "trusted-promotion-v1"
    assert current["trust_score"] == 88 and current["trust_reasons"] == ["legacy qualified"]
    assert migration.apply()["idempotent_noop"] is True
    assert migration.verify()["ok"] is True


def test_trusted_requalification_completes_without_demotion_or_new_promotion(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_requal_complete")
    metadata, body = read_document(path)
    legacy_history = [{
        "promotion_id": "promotion_legacy_complete", "from_status": "working", "to_status": "trusted",
        "policy_version": "trusted-promotion-v1", "promoted_at": "2026-07-16T12:00:00+08:00",
    }]
    metadata.update({
        "status": "trusted", "memory_tier": "trusted",
        "needs_policy_requalification": True,
        "trust_policy_version": "trusted-promotion-v1",
        "promotion_history": legacy_history,
    })
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    result = PromotionService(repo).requalify_trusted("claim_requal_complete")
    current, _ = read_document(path)

    assert result["requalified"] is True
    assert current["status"] == "trusted" and current["memory_tier"] == "trusted"
    assert current["needs_policy_requalification"] is False
    assert current["trust_policy_version"] == "trusted-promotion-v3-receipt-v2"
    assert current["promotion_history"] == legacy_history
    assert ConsolidationReceiptService(repo).valid_for("claim_requal_complete")["consolidation_id"] == result["receipt_id"]
    assert not (repo.root / "vault/receipts/demotions").exists()
    metrics = ProjectMetricsService(repo).collect()
    assert metrics["trusted_v3_qualified"] == 1
    assert metrics["trusted_awaiting_requalification"] == 0
    assert metrics["receipt_versions"]["v2"] >= 1 and metrics["recovery_journals"] == 0


def test_strict_execution_and_canonical_gate_exclude_awaiting_requalification(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_requal_gate")
    metadata, body = read_document(path)
    metadata.update({
        "status": "trusted", "memory_tier": "trusted",
        "epistemic_status": "supported", "needs_policy_requalification": True,
        "trust_policy_version": "trusted-promotion-v1",
    })
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()
    ConsolidationReceiptService(repo).consolidate("claim_requal_gate")

    pack = ContextPackService(repo).build(
        "Bounded evidence", 1200, profiles=["execution"], strict_execution=True,
    ).as_dict()
    assert "claim_requal_gate" not in {item["id"] for item in pack["items"]}
    with pytest.raises(ValidationError, match="awaits current-policy requalification"):
        PromotionService(repo).recommend_canonical("claim_requal_gate")


def test_repair_faulty_trust_requalification_restores_only_proven_state(repo: Repository) -> None:
    path, _ = write_m8_claim(repo, "claim_requal_repair")
    metadata, body = read_document(path)
    metadata.update({
        "status": "trusted", "memory_tier": "trusted", "legacy_status": "trusted",
        "trust_score": 91, "trust_reasons": ["legacy evidence"],
        "promotion_history": [{
            "promotion_id": "promotion_repair", "from_status": "working", "to_status": "trusted",
            "policy_version": "trusted-promotion-v1", "promoted_at": "2026-07-16T13:00:00+08:00",
        }],
    })
    original = render_document(metadata, body)
    path.write_text(original, encoding="utf-8")
    backup_path = repo.root / "data/backups/trust-requalification-2026-07-17T17-04-22+08-00" / repo.rel(path)
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    backup_path.write_text(original, encoding="utf-8")
    metadata.update({
        "status": "working", "memory_tier": "working", "needs_revalidation": True,
        "updated_by": "trusted-promotion-v3-receipt-v2", "updated_at": "2026-07-17T17:04:22+08:00",
    })
    path.write_text(render_document(metadata, body), encoding="utf-8")
    repo.rebuild_index()

    repair = TrustRequalificationRepairMigration(repo)
    assert len(repair.plan()["restorable"]) == 1
    result = repair.apply()
    restored, restored_body = read_document(path)

    assert result["restored"] == 1 and result["conflict_count"] == 0
    assert restored_body == body and restored["memory_tier"] == "trusted"
    assert restored["needs_policy_requalification"] is True
    assert restored["trust_policy_version"] == "trusted-promotion-v1"
    assert restored["trust_score"] == 91 and not (repo.root / "vault/receipts/demotions").exists()
def cognitive_reflection_payload(**overrides):
    payload = {
        "title": "Reflection on compiled robot skills",
        "created_by": "agent",
        "reflection_kind": "idea",
        "importance": "high",
        "why_important": "It changes how reusable robot skills can be understood as compiled representations rather than only runtime policies.",
        "what_changed": "Previously skill transfer was treated only as policy reuse; now compilation boundaries are also relevant.",
        "surprising": "Compression and validation may be coupled rather than separate stages.",
        "connections": [{
            "shared_mechanism": "expensive learning is compressed into a reusable execution form",
            "boundary": "the analogy applies to representation reuse, not semantic equivalence",
            "difference": "compiler outputs are deterministic while learned skills remain probabilistic",
        }],
        "conflicts": [],
        "open_questions": ["Which validation contract makes a compiled skill portable?"],
        "possible_mechanisms": ["typed preconditions and postconditions"],
        "future_directions": ["compare skill graphs with compiler intermediate representations"],
        "confidence": "medium",
    }
    payload.update(overrides)
    return payload


def test_idea_capture_creates_input_and_reflection_queue(repo: Repository):
    result = InputEpisodeService(repo).capture_idea(
        "机器人技能下移可能类似编译器优化", title="技能编译灵感",
    )

    _, episode, body = repo.find_document(result["input"]["object_id"])
    assert episode["type"] == "input"
    assert episode["input_type"] == "idea"
    assert episode["truth_layer"] == "input_episode"
    assert episode["user_authored"] is True
    assert "memory_tier" not in episode
    assert episode["source_id"] in body
    queue = ReflectionService(repo).queue(limit=5)
    assert queue["selected_count"] == 1
    assert queue["items"][0]["input_id"] == episode["id"]


def test_input_backfill_is_bounded_explicit_and_excludes_personal_notes(repo: Repository):
    first = capture_web_bytes(
        repo, "https://example.com/backfill-one", b"first backfill article", "Backfill one",
    )
    second = capture_web_bytes(
        repo, "https://example.com/backfill-two", b"second backfill article", "Backfill two",
    )
    personal = CaptureService(repo).capture_text("operator receipt", title="Personal receipt")

    selected = InputEpisodeService(repo).backfill(limit=1, source_ids=[first.source_id])
    remaining = InputEpisodeService(repo).backfill(limit=10)
    ExtractionService(repo).extract(first.source_id)
    input_sources = {
        read_document(path)[0]["source_id"]
        for path in InputEpisodeService(repo).documents()
    }
    queued = ReflectionService(repo).queue(limit=10)
    first_queue_item = next(
        item for item in queued["items"] if item["source_ids"] == [first.source_id]
    )

    assert selected["created_count"] == 1 and selected["knowledge_writes"] == 0
    assert remaining["created_count"] == 1
    assert input_sources == {first.source_id, second.source_id}
    assert personal.source_id not in input_sources
    assert first_queue_item["excerpt_source"] == "extraction"
    assert "first backfill article" in first_queue_item["excerpt"]


def test_article_reflection_is_agent_authored_and_nonfactual(repo: Repository):
    source = capture_web_bytes(
        repo, "https://example.com/world-model-critic",
        b"A world model can support prediction and internal evaluation.",
        "World model critic",
    )
    episode = InputEpisodeService(repo).create_from_source(
        source.source_id, input_type="article",
    )
    duplicate_episode = InputEpisodeService(repo).create_from_source(
        source.source_id, input_type="article",
    )
    assert duplicate_episode.object_id == episode.object_id
    assert duplicate_episode.created is False
    reflection = ReflectionService(repo).create(
        episode.object_id, cognitive_reflection_payload(
            reflection_kind="article", created_by="agent",
            why_important="It changes the role assigned to a world model from prediction alone to a possible internal evaluator.",
        ),
    )
    _, metadata, _ = repo.find_document(reflection.object_id)
    assert metadata["reflection_kind"] == "article"
    assert metadata["created_by"] == "agent"
    assert metadata["user_authored"] is False
    assert metadata["truth_layer"] == "reflection"
    duplicate_reflection = ReflectionService(repo).create(
        episode.object_id, cognitive_reflection_payload(
            reflection_kind="article", created_by="agent",
            why_important="It changes the role assigned to a world model from prediction alone to a possible internal evaluator.",
        ),
    )
    assert duplicate_reflection.object_id == reflection.object_id
    assert duplicate_reflection.created is False


def test_reflection_quality_gate_and_authorship_do_not_change_trust(repo: Repository):
    episode = InputEpisodeService(repo).capture_idea("World models may act as critics")["input"]
    service = ReflectionService(repo)

    with pytest.raises(ValidationError, match="cognitive value"):
        service.create(episode["object_id"], {
            "created_by": "agent", "reflection_kind": "idea",
            "why_important": "这篇文章介绍了世界模型。",
            "open_questions": ["What changes?"], "confidence": "low",
        })
    with pytest.raises(ValidationError, match="shared_mechanism"):
        service.create(episode["object_id"], cognitive_reflection_payload(
            connections=[{"shared_mechanism": "both use AI"}],
        ))

    result = service.create(
        episode["object_id"], cognitive_reflection_payload(created_by="user"),
    )
    _, reflection, _ = repo.find_document(result.object_id)
    assert reflection["truth_layer"] == "reflection"
    assert reflection["user_authored"] is True
    assert reflection["execution_safe"] is False
    assert "memory_tier" not in reflection
    assert "epistemic_status" not in reflection
    assert repo.count_by_type().get("reflection") == 1


def test_conversation_and_agent_session_import_only_queue_reflection(repo: Repository, workspace: Path):
    conversation = workspace / "conversation.md"
    conversation.write_text("User: a slow embodied system may compile reusable skills.\nAssistant: define the boundary.", encoding="utf-8")
    imported = InputEpisodeService(repo).import_conversation(
        conversation, participants=["user", "assistant"], topic="embodied-agent",
    )
    _, conversation_input, _ = repo.find_document(imported["input"]["object_id"])
    assert conversation_input["participants"] == ["user", "assistant"]

    session = workspace / "session.json"
    session.write_text(json.dumps({
        "goal": "fix GR00T deployment", "result": "success",
        "lesson": "N1.6 requires an explicit observation contract",
    }), encoding="utf-8")
    session_result = InputEpisodeService(repo).import_agent_session(session, agent="codex")
    _, session_input, _ = repo.find_document(session_result["input"]["object_id"])
    assert session_input["episode_kind"] == "agent_session"
    assert session_input["session"]["lesson"].startswith("N1.6")
    assert session_result["knowledge_writes"] == 0
    assert not list(repo.memory_documents())
    assert not list(repo.canonical_documents())


def test_daily_dream_creates_reflection_and_working_but_never_canonical(repo: Repository, workspace: Path):
    captured = InputEpisodeService(repo).capture_idea(
        "Robot skill compilation can compress expensive planning into fast execution.",
        title="Robot skill compilation",
    )
    input_id = captured["input"]["object_id"]
    bundle_path = workspace / "daily-dream.json"
    bundle_path.write_text(json.dumps({
        "provider_name": "gpt-5.6-terra-light",
        "reflections": [{
            "input_id": input_id,
            "reflection": cognitive_reflection_payload(),
            "semantic_items": [{
                "object_type": "concept",
                "title": "Compiled robot skill representation",
                "body": "A reusable robot skill representation compresses expensive planning into a bounded execution interface.",
                "metadata": {"aliases": ["机器人技能编译表示"], "confidence": "medium"},
            }],
        }],
    }, ensure_ascii=False), encoding="utf-8")

    result = DailyDreamService(repo).run(bundle_path, limit=5)
    assert result["inputs_processed"] == 1
    assert result["reflections_created"] == 1
    assert result["concepts_created"] == 1
    assert result["canonical_writes"] == 0
    assert not list(repo.canonical_documents())
    working_path = repo.root / result["working_written"][0]
    working, _ = read_document(working_path)
    assert working["memory_tier"] == "working"
    assert working["reflection_context"]["reflection_ids"] == result["reflection_ids"]


def test_daily_dream_prevalidates_forbidden_types_and_resumes_existing_reflection(
    repo: Repository, workspace: Path,
):
    captured = InputEpisodeService(repo).capture_idea(
        "Robot skill compilation needs a restart-safe reflection boundary.",
        title="Restart-safe reflection",
    )
    input_id = captured["input"]["object_id"]
    payload = cognitive_reflection_payload(
        title="Restart-safe reflection artifact",
        why_important="It changes Daily Dream from a best-effort sequence into a restartable cognitive boundary.",
    )
    bundle_path = workspace / "daily-restart.json"
    bundle = {
        "reflections": [{
            "input_id": input_id,
            "reflection": payload,
            "semantic_items": [{
                "object_type": "hypothesis", "title": "Forbidden daily hypothesis",
                "body": "Daily must not create this hypothesis.",
            }],
        }],
    }
    bundle_path.write_text(json.dumps(bundle), encoding="utf-8")

    with pytest.raises(ValidationError, match="does not allow object_type"):
        DailyDreamService(repo).run(bundle_path)
    assert not ReflectionService(repo).documents()
    assert not list(repo.memory_documents())

    interrupted = ReflectionService(repo).create(input_id, payload)
    bundle["reflections"][0]["semantic_items"] = [{
        "object_type": "concept", "title": "Restart-safe cognitive boundary",
        "body": "A restart-safe cognitive boundary reuses an immutable Reflection after interruption.",
    }]
    bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
    resumed = DailyDreamService(repo).run(bundle_path)
    repeated = DailyDreamService(repo).run(bundle_path)

    assert resumed["reflection_ids"] == [interrupted.object_id]
    assert resumed["reflections_created"] == 0
    assert resumed["reflections_reused"] == 1
    assert len(resumed["working_written"]) == 1
    assert repeated["reflections_created"] == 0
    assert repeated["reflections_reused"] == 1
    assert repeated["working_written"] == []


def test_weekly_dream_creates_nonfactual_synthesis_and_hypothesis(repo: Repository, workspace: Path):
    input_service = InputEpisodeService(repo)
    reflection_service = ReflectionService(repo)
    first = input_service.capture_idea("Human habits compress deliberation into fast routines.")["input"]
    second = input_service.capture_idea("Robot skills compress planning into fast execution.")["input"]
    first_reflection = reflection_service.create(first["object_id"], cognitive_reflection_payload(
        title="Human habit compilation reflection",
    ))
    second_reflection = reflection_service.create(second["object_id"], cognitive_reflection_payload(
        title="Robot skill compilation reflection",
        surprising="Habit formation and robot skill caching share a compression shape.",
    ))
    source_ids = []
    for reflection_id in (first_reflection.object_id, second_reflection.object_id):
        _, metadata, _ = repo.find_document(reflection_id)
        source_ids.extend(metadata["source_ids"])
    target_concept_id = "concept_weekly_amortization"
    write_m8_memory(
        repo, target_concept_id, "concept", "Weekly amortization concept",
        "Existing view: skill reuse is primarily action caching.", [source_ids[0]],
    )
    weekly = workspace / "weekly-dream.json"
    weekly.write_text(json.dumps({
        "provider_name": "gpt-5.6-sol-high",
        "synthesis": {
            "title": "Compression before fast execution",
            "period": "2026-W29",
            "input_reflections": [first_reflection.object_id, second_reflection.object_id],
            "input_concepts": [target_concept_id],
            "emerging_patterns": ["expensive computation is consolidated into a reusable fast path"],
            "knowledge_updates": [{
                "target_id": target_concept_id,
                "previous": "skill reuse is primarily action caching",
                "proposed": "skill reuse also requires a typed validation boundary",
                "reason": "the two reflections expose a shared failure-sensitive fast path",
                "change_type": "refine",
                "supporting_reflections": [first_reflection.object_id, second_reflection.object_id],
                "supporting_sources": sorted(set(source_ids)),
            }],
            "new_connections": [{
                "shared_mechanism": "slow deliberation is compressed into a reusable execution path",
                "boundary": "the pattern concerns amortization, not identical implementations",
                "difference": "habit formation is biological while robot compilation is engineered",
            }],
            "unresolved_tensions": ["compression can improve speed while hiding adaptation failures"],
            "candidate_hypotheses": [{
                "statement": "Typed validation makes compressed robot skills more portable.",
                "supporting_patterns": ["compression followed by fast execution"],
                "supporting_reflections": [first_reflection.object_id, second_reflection.object_id],
                "supporting_sources": sorted(set(source_ids)),
                "counter_arguments": ["Portability may depend mainly on embodiment alignment."],
                "falsifier": "Typed validation fails to improve transfer across two embodiments.",
                "possible_experiment": "Compare transfer success with and without typed contracts.",
            }],
            "possible_experiments": ["measure cross-embodiment transfer under typed contracts"],
            "confidence": "medium",
        },
        "knowledge_bundles": [{
            "source_id": source_ids[0],
            "reflection_ids": [first_reflection.object_id],
            "items": [{
                "object_type": "concept",
                "title": "Consolidated fast execution path",
                "body": "Expensive deliberation can be consolidated into a bounded reusable execution path.",
                "metadata": {"confidence": "medium"},
            }],
        }],
    }, ensure_ascii=False), encoding="utf-8")

    result = WeeklyDreamService(repo).run(weekly)
    assert result["candidate_hypotheses"] == 1
    assert len(result["working_created"]) == 1
    assert result["trusted_changes"] == 0
    assert result["canonical_writes"] == 0
    _, synthesis, _ = repo.find_document(result["synthesis_id"])
    assert synthesis["truth_layer"] == "cognitive_synthesis"
    assert synthesis["candidate_hypotheses"][0]["epistemic_status"] == "hypothetical"
    assert "memory_tier" not in synthesis
    assert "epistemic_status" not in synthesis
    assert not list(repo.canonical_documents())
    working, _ = read_document(repo.root / result["working_created"][0])
    assert working["reflection_context"]["reflection_ids"] == [first_reflection.object_id]
    repeated = WeeklyDreamService(repo).run(weekly)
    assert repeated["synthesis_id"] == result["synthesis_id"]
    assert repeated["synthesis_created"] is False
    assert repeated["canonical_writes"] == 0


def test_weekly_dream_prevalidates_bundle_provenance_before_writing_synthesis(
    repo: Repository, workspace: Path,
):
    first = InputEpisodeService(repo).capture_idea("first weekly source")["input"]
    second = InputEpisodeService(repo).capture_idea("second weekly source")["input"]
    reflection_ids = [
        ReflectionService(repo).create(item["object_id"], cognitive_reflection_payload()).object_id
        for item in (first, second)
    ]
    _, first_reflection, _ = repo.find_document(reflection_ids[0])
    weekly = workspace / "weekly-invalid-provenance.json"
    weekly.write_text(json.dumps({
        "synthesis": {
            "period": "2026-W29", "input_reflections": reflection_ids,
            "input_concepts": [], "emerging_patterns": ["shared pattern"],
            "knowledge_updates": [], "new_connections": [],
            "unresolved_tensions": [], "candidate_hypotheses": [],
        },
        "knowledge_bundles": [{
            "source_id": first_reflection["source_ids"][0],
            "reflection_ids": ["reflection_outside_synthesis"],
            "items": [{
                "object_type": "concept", "title": "Invalid provenance",
                "body": "This item must be rejected before Synthesis is written.",
            }],
        }],
    }), encoding="utf-8")

    with pytest.raises(ValidationError, match="reflection_ids from this synthesis"):
        WeeklyDreamService(repo).run(weekly)
    assert not SynthesisService(repo).documents()


def test_cognitive_synthesis_identity_covers_updates_experiments_and_provider(repo: Repository):
    first = InputEpisodeService(repo).capture_idea("first identity source")["input"]
    second = InputEpisodeService(repo).capture_idea("second identity source")["input"]
    reflection_ids = [
        ReflectionService(repo).create(item["object_id"], cognitive_reflection_payload()).object_id
        for item in (first, second)
    ]
    source_ids: list[str] = []
    for reflection_id in reflection_ids:
        _, reflection, _ = repo.find_document(reflection_id)
        source_ids.extend(reflection["source_ids"])
    target_id = "concept_synthesis_identity"
    write_m8_memory(
        repo, target_id, "concept", "Synthesis identity target",
        "Previous view.", sorted(set(source_ids)),
    )
    base = {
        "title": "Identity-complete synthesis", "period": "2026-W29",
        "input_reflections": reflection_ids, "input_concepts": [target_id],
        "emerging_patterns": ["shared identity-sensitive pattern"],
        "knowledge_updates": [{
            "target_id": target_id, "previous": "Previous view.",
            "proposed": "Refined view.", "reason": "two reflections support refinement",
            "change_type": "refine", "supporting_reflections": reflection_ids,
            "supporting_sources": sorted(set(source_ids)),
        }],
        "new_connections": [], "unresolved_tensions": [],
        "candidate_hypotheses": [], "possible_experiments": ["experiment A"],
        "confidence": "medium",
    }
    service = SynthesisService(repo)
    first_write = service.create(base, provider_name="provider-a")
    changed_experiment = json.loads(json.dumps(base))
    changed_experiment["possible_experiments"] = ["experiment B"]
    second_write = service.create(changed_experiment, provider_name="provider-a")
    third_write = service.create(base, provider_name="provider-b")

    assert len({first_write.object_id, second_write.object_id, third_write.object_id}) == 3


def test_weekly_hypothesis_gate_requires_falsifier_and_counterexample(repo: Repository):
    input_service = InputEpisodeService(repo)
    reflection_service = ReflectionService(repo)
    first = input_service.capture_idea("first input")["input"]
    second = input_service.capture_idea("second input")["input"]
    reflections = [
        reflection_service.create(item["object_id"], cognitive_reflection_payload()).object_id
        for item in (first, second)
    ]
    with pytest.raises(ValidationError, match="falsifier"):
        SynthesisService(repo).create({
            "period": "2026-W29", "input_reflections": reflections,
            "input_concepts": [], "emerging_patterns": ["shared compression"],
            "new_connections": [], "unresolved_tensions": [],
            "candidate_hypotheses": [{"statement": "Untestable claim"}],
        }, provider_name="test")


def test_research_context_includes_reflection_and_execution_excludes_it(repo: Repository):
    episode = InputEpisodeService(repo).capture_idea(
        "portable skill compiler validation contract",
        title="Portable skill compiler",
    )["input"]
    reflection = ReflectionService(repo).create(
        episode["object_id"], cognitive_reflection_payload(
            title="Portable skill compiler reflection",
            why_important="Portable skill compiler validation changes how cross-embodiment reuse is evaluated.",
        ),
    )

    research = ContextPackService(repo).build(
        "portable skill compiler", profiles=["research"], token_budget=1200,
    ).as_dict()
    reflected = next(item for item in research["items"] if item["id"] == reflection.object_id)
    assert reflected["truth_layer"] == "reflection"
    assert reflected["execution_safe"] is False
    assert reflected["reflection"]["why_important"].startswith("Portable")
    execution = ContextPackService(repo).build(
        "portable skill compiler", profiles=["execution"], token_budget=1200,
    ).as_dict()
    assert reflection.object_id not in {item["id"] for item in execution["items"]}
    assert not ({"source", "input", "reflection", "synthesis", "annotation"} & {
        item["type"] for item in execution["items"]
    })


def test_cognitive_cli_surface_is_provider_neutral():
    assert build_parser().parse_args(["idea", "capture", "--text", "idea"]).idea_command == "capture"
    assert build_parser().parse_args(["conversation", "import", "chat.md"]).conversation_command == "import"
    assert build_parser().parse_args([
        "session", "import", "--from-file", "session.json", "--agent", "codex",
    ]).session_command == "import"
    assert build_parser().parse_args(["reflection", "queue"]).reflection_command == "queue"
    parsed_backfill = build_parser().parse_args([
        "inputs", "--backfill", "--limit", "5", "--source-id", "source_x",
    ])
    assert parsed_backfill.backfill is True and parsed_backfill.limit == 5
    assert build_parser().parse_args([
        "dream", "daily", "--bundle-file", "daily.json",
    ]).dream_command == "daily"
    assert build_parser().parse_args([
        "dream", "weekly", "--bundle-file", "weekly.json",
    ]).dream_command == "weekly"
