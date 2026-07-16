from __future__ import annotations

from typing import Any

from .bundle import BundleReviewService
from .errors import ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .repository import Repository, now_iso


class SourceBundleReviewService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def queue(self) -> list[dict[str, Any]]:
        result = []
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            if metadata.get("proposal_kind") not in {"compile_bundle", "source_bundle", "corpus_distillation"} or metadata.get("status") not in {"pending", "deferred"}:
                continue
            metrics = metadata.get("bundle_metrics", {})
            items = metadata.get("bundle_items", [])
            result.append({
                "bundle_id": metadata["id"], "source_ids": metadata.get("source_ids", []),
                "status": metadata["status"], "title": metadata.get("title"),
                "review_cost_estimate": metrics.get("review_cost_estimate", len(items)),
                "high_confidence": sum(item.get("review_tier") == "high" for item in items),
                "low_confidence": sum(item.get("review_tier") == "low" for item in items),
                "new_object_count": metrics.get("new_object_count", sum(item.get("action") == "create" for item in items)),
                "updated_object_count": metrics.get("updated_object_count", sum(item.get("action") == "update" for item in items)),
                "contradiction_count": len(metadata.get("contradiction_candidates", [])),
                "primary_followup_count": len(metadata.get("primary_source_followups", [])),
                "path": self.repository.rel(path),
            })
        return sorted(result, key=lambda item: (-item["contradiction_count"], -item["updated_object_count"], item["review_cost_estimate"]))

    def show(self, bundle_id: str, *, details: bool = False) -> dict[str, Any]:
        path, metadata, body = self.repository.find_document(bundle_id)
        if metadata.get("proposal_kind") not in {"compile_bundle", "source_bundle", "corpus_distillation"}:
            raise ValidationError("不是 Source Bundle")
        summary = {
            "bundle_id": bundle_id, "status": metadata.get("status"),
            "source_ids": metadata.get("source_ids", []), "source_summary": metadata.get("source_summary"),
            "source_authority": metadata.get("source_authority"), "content_quality": metadata.get("content_quality"),
            "compile_disposition": metadata.get("compile_disposition"), "bundle_metrics": metadata.get("bundle_metrics", {}),
            "contradictions": metadata.get("contradiction_candidates", []),
            "primary_source_followups": metadata.get("primary_source_followups", []),
        }
        if details:
            summary["items"] = metadata.get("bundle_items", [])
            summary["body"] = body
        return summary

    def approve_high_confidence(self, bundle_id: str) -> dict[str, Any]:
        _, metadata, _ = self.repository.find_document(bundle_id)
        eligible = [
            str(item["item_id"]) for item in metadata.get("bundle_items", [])
            if item.get("decision") == "pending" and item.get("review_tier") == "high"
            and item.get("atomicity_status") != "compound"
            and item.get("evidence_coverage") != "partial"
        ]
        if not eligible:
            raise ValidationError("没有可安全批量批准的 high-confidence items")
        return BundleReviewService(self.repository).approve(bundle_id, eligible)

    def source_only(self, bundle_id: str, reason: str = "") -> dict[str, Any]:
        path, metadata, body = self.repository.find_document(bundle_id)
        if metadata.get("status") not in {"pending", "deferred"}:
            raise ValidationError("bundle 状态不可标记 source-only")
        for item in metadata.get("bundle_items", []):
            if item.get("decision") == "pending":
                item["decision"] = "rejected"
                item["review_reason"] = reason or "仅保留 source，不进入知识层"
        metadata["compile_disposition"] = "source_only"
        metadata["status"] = "rejected"
        metadata["reviewed_at"] = now_iso()
        metadata["updated_at"] = metadata["reviewed_at"]
        metadata["review_reason"] = reason or "仅保留 source，不进入知识层"
        atomic_write_text(path, render_document(metadata, body))
        self.repository.append_event("proposal-events", {"event": "bundle-source-only", "proposal_id": bundle_id, "source_ids": metadata.get("source_ids", []), "reason": reason})
        return {"bundle_id": bundle_id, "status": "source_only", "rejected_items": len(metadata.get("bundle_items", []))}
