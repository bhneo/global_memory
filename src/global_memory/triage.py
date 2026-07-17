from __future__ import annotations

from typing import Any

from .bundle import BundleCompiler
from .errors import ValidationError
from .extraction import ExtractionService
from .lifecycle import SourceLifecycleService
from .proposals import ProposalService
from .quality import SourceQualityService
from .repository import Repository


class DailyTriageService:
    """Incrementally prepare inbox sources without promoting them to knowledge."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.extractions = ExtractionService(repository)
        self.quality = SourceQualityService(repository)
        self.lifecycle = SourceLifecycleService(repository)

    def run(
        self,
        source_ids: list[str] | None = None,
        *,
        limit: int = 25,
        compile_selected: bool = False,
        recheck: bool = False,
    ) -> dict[str, Any]:
        if limit < 1:
            raise ValidationError("triage limit must be at least 1")
        if source_ids:
            selected = list(dict.fromkeys(source_ids))[:limit]
        else:
            selected = []
            for item in ProposalService(self.repository).inbox():
                source_id = str(item["id"])
                if self.lifecycle.status(source_id).state in {"captured", "extracted"}:
                    selected.append(source_id)
                if len(selected) >= limit:
                    break

        results: list[dict[str, Any]] = []
        for source_id in selected:
            _, metadata, _ = self.repository.find_document(source_id)
            if metadata.get("type") != "source":
                raise ValidationError(f"triage only accepts source objects: {source_id}")

            extraction_created = False
            try:
                _, extraction, _ = self.extractions.latest_for_source(source_id)
            except Exception:
                extraction_result = self.extractions.extract(source_id)
                extraction_created = True
                _, extraction, _ = self.extractions.latest_for_source(source_id)

            assessment = self.quality.load(source_id)
            quality_checked = False
            if assessment is None or recheck or extraction_created:
                assessment = self.quality.assess(source_id, persist=True)
                quality_checked = True

            proposal_id = None
            action = "capture_only"
            if not assessment.compile_allowed:
                action = "blocked_by_quality"
            elif compile_selected:
                proposal_id = BundleCompiler(self.repository).compile(source_id).proposal_id
                action = "proposal_created"
            elif not extraction_created and not quality_checked:
                action = "already_prepared"

            results.append({
                "source_id": source_id,
                "action": action,
                "extraction_created": extraction_created,
                "quality_checked": quality_checked,
                "availability_status": assessment.availability_status,
                "content_quality": assessment.content_quality,
                "compile_allowed": assessment.compile_allowed,
                "proposal_id": proposal_id,
                "state": self.lifecycle.status(source_id).state,
            })

        unprepared = [
            str(item["id"]) for item in ProposalService(self.repository).inbox()
            if self.lifecycle.status(str(item["id"])).state in {"captured", "extracted"}
        ]
        return {
            "mode": "compile-selected" if compile_selected else "capture-only",
            "selected": len(selected),
            "limit": limit,
            "remaining_inbox": len(ProposalService(self.repository).inbox()),
            "remaining_unprepared": len(unprepared),
            "results": results,
            "note": (
                "No canonical knowledge is written. Compilation is explicit and creates pending proposals only."
                if compile_selected
                else "Sources were only extracted and quality-checked; knowledge compilation is deferred."
            ),
        }
