from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

from .consolidation import ConsolidationReceiptService, DriftAuditService
from .epistemics import infer_epistemic_status, infer_tier
from .markdown import atomic_write_text, read_document
from .memory import ExceptionService
from .repository import Repository, now_iso
from .governance import POLICY_VERSION
from .research import ActivationService, ResearchAnnotationService


class ProjectMetricsService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def collect(self) -> dict[str, Any]:
        tier_counts: Counter[str] = Counter()
        epistemic_counts: Counter[str] = Counter()
        revisions = 0
        trusted_qualified = 0
        trusted_awaiting = 0
        trusted_contested = 0
        trusted_current_policy = 0
        trusted_current_receipt = 0
        trusted_stale_receipt = 0
        trusted_high_risk_drift = 0
        trusted_factual = 0
        trusted_exploration = 0
        canonical_current_receipt = 0
        receipts = ConsolidationReceiptService(self.repository)
        languages: Counter[str] = Counter()
        documents = [*self.repository.memory_documents(), *self.repository.canonical_documents()]
        for path in documents:
            metadata, body = read_document(path)
            tier = infer_tier(metadata, path)
            epistemic = infer_epistemic_status(metadata, tier)
            tier_counts[tier] += 1
            epistemic_counts[epistemic] += 1
            if tier == "trusted":
                current_receipt = receipts.valid_for(str(metadata["id"]))
                receipt_current = current_receipt is not None
                semantic_failures = receipts.semantic_qualification_failures(str(metadata.get("type")), current_receipt)
                current_policy = metadata.get("trust_policy_version") == POLICY_VERSION
                awaiting = bool(metadata.get("needs_policy_requalification"))
                high_risk = bool(metadata.get("high_risk_drift"))
                contested = epistemic == "contested"
                trusted_current_policy += int(current_policy)
                trusted_current_receipt += int(receipt_current)
                trusted_stale_receipt += int(not receipt_current)
                trusted_high_risk_drift += int(high_risk)
                trusted_factual += int(metadata.get("type") in {"claim", "concept"})
                trusted_exploration += int(metadata.get("type") not in {"claim", "concept"})
                if metadata.get("needs_policy_requalification"):
                    trusted_awaiting += 1
                elif current_policy and receipt_current and not semantic_failures and not contested and not high_risk:
                    trusted_qualified += 1
                if contested:
                    trusted_contested += 1
            if tier == "canonical":
                canonical_current_receipt += int(receipts.valid_for(str(metadata["id"])) is not None)
            revisions += int(bool(metadata.get("revision_of")))
            if any("\u3400" <= char <= "\u9fff" for char in body):
                languages["zh"] += 1
            if any("a" <= char.casefold() <= "z" for char in body):
                languages["en"] += 1
        exceptions = ExceptionService(self.repository).list({"open", "deferred"})
        promotions = []
        promotion_dir = self.repository.root / "vault" / "promotions"
        for path in promotion_dir.glob("promotion-*.md") if promotion_dir.exists() else []:
            metadata, _ = read_document(path)
            if metadata.get("status") in {"pending", "deferred"}:
                promotions.append(metadata)
        receipt_counts = receipts.counts()
        receipt_versions: Counter[str] = Counter()
        for receipt_path in receipts.documents():
            receipt, _ = read_document(receipt_path)
            receipt_versions[f"v{int(receipt.get('receipt_schema_version', 1))}"] += 1
        current_v2_objects = sum(
            receipts.valid_for(str(read_document(path)[0]["id"])) is not None
            for path in documents
        )
        recovery_directory = self.repository.root / "system" / "recovery"
        recovery_journals = len(list(recovery_directory.glob("*.json"))) if recovery_directory.exists() else 0
        drift = DriftAuditService(self.repository).run()
        annotations = ResearchAnnotationService(self.repository).all()
        capture_intents = [item for item in annotations if item.get("annotation_kind") == "capture_intent"]
        feedback = [item for item in annotations if item.get("annotation_kind") == "connection_feedback"]
        annotated_sources = {
            str(target) for item in capture_intents if item.get("why_saved")
            for target in item.get("target_ids", []) if str(target).startswith("source_")
        }
        all_source_ids = {
            str(read_document(path)[0]["id"]) for path in self.repository.source_documents()
        }
        high_salience_unannotated = {
            str(target) for item in capture_intents
            if item.get("personal_salience") == "high" and not item.get("why_saved")
            for target in item.get("target_ids", []) if str(target).startswith("source_")
        }
        activation_events = ActivationService(self.repository).events()
        return {
            "generated_at": now_iso(),
            "working": tier_counts["working"],
            "trusted": tier_counts["trusted"],
            "trusted_total": tier_counts["trusted"],
            "trusted_current_policy": trusted_current_policy,
            "trusted_current_receipt": trusted_current_receipt,
            "trusted_v3_qualified": trusted_qualified,
            "trusted_awaiting_requalification": trusted_awaiting,
            "trusted_stale_receipt": trusted_stale_receipt,
            "trusted_contested": trusted_contested,
            "trusted_high_risk_drift": trusted_high_risk_drift,
            "trusted_factual": trusted_factual,
            "trusted_exploration": trusted_exploration,
            "canonical": tier_counts["canonical"],
            "canonical_with_current_receipt": canonical_current_receipt,
            "historical": tier_counts["historical"],
            "contested": epistemic_counts["contested"],
            "working_revisions": revisions,
            "exceptions": len(exceptions),
            "promotion_candidates": len(promotions),
            "consolidation_receipts": receipt_counts["total"],
            "receipt_versions": dict(sorted(receipt_versions.items())),
            "objects_with_current_v2": current_v2_objects,
            "failed_receipts": receipt_counts["failed"],
            "recovery_journals": recovery_journals,
            "drift_warnings": len(drift["issues"]),
            "high_severity_drift": drift["high_severity"],
            "corpus": {
                "sources": len(list(self.repository.source_documents())),
                "knowledge_objects": len(documents),
                "language_document_counts": dict(sorted(languages.items())),
            },
            "ci_status": "unavailable-locally",
            "research_annotations": len(annotations),
            "capture_intent_annotations": len(capture_intents),
            "research_notes": sum(item.get("annotation_kind") == "research_note" for item in annotations),
            "connection_feedback": len(feedback),
            "feedback_obvious": sum(item.get("feedback_label") == "obvious" for item in feedback),
            "feedback_forced": sum(item.get("feedback_label") == "forced" for item in feedback),
            "feedback_interesting": sum(item.get("feedback_label") == "interesting" for item in feedback),
            "feedback_actionable": sum(item.get("feedback_label") == "actionable" for item in feedback),
            "sources_with_why_saved": len(annotated_sources),
            "sources_without_why_saved": len(all_source_ids - annotated_sources),
            "high_salience_unannotated_sources": len(high_salience_unannotated),
            "projects_with_activity": len({
                str(project) for item in annotations for project in item.get("research_projects", [])
            }),
            "activation_events": len(activation_events),
            "objects_used": len({event["object_id"] for event in activation_events if event.get("event_kind") == "used"}),
            "objects_cited": len({event["object_id"] for event in activation_events if event.get("event_kind") == "cited"}),
            "objects_opened": len({event["object_id"] for event in activation_events if event.get("event_kind") == "opened"}),
            "objects_coactivated": len({event["object_id"] for event in activation_events if event.get("event_kind") == "coactivated" or event.get("coactivated_ids")}),
        }

    def write_project_state(self, metrics: dict[str, Any] | None = None) -> dict[str, Any]:
        metrics = metrics or self.collect()
        path = self.repository.root / "PROJECT_STATE.md"
        text = path.read_text(encoding="utf-8") if path.exists() else "# Current State\n\n## Current metrics\n\n"
        start = "<!-- GENERATED_METRICS_START -->"
        end = "<!-- GENERATED_METRICS_END -->"
        rows = [
            start,
            f"- Generated at: {metrics['generated_at']}",
            f"- Working / Trusted / Canonical / Historical: {metrics['working']} / {metrics['trusted']} / {metrics['canonical']} / {metrics['historical']}",
            f"- Trusted current policy / receipt / qualified: {metrics['trusted_current_policy']} / {metrics['trusted_current_receipt']} / {metrics['trusted_v3_qualified']}",
            f"- Trusted awaiting / stale receipt / contested / high-risk drift: {metrics['trusted_awaiting_requalification']} / {metrics['trusted_stale_receipt']} / {metrics['trusted_contested']} / {metrics['trusted_high_risk_drift']}",
            f"- Trusted factual / exploration; Canonical with current Receipt: {metrics['trusted_factual']} / {metrics['trusted_exploration']} / {metrics['canonical_with_current_receipt']}",
            f"- Contested: {metrics['contested']}",
            f"- Working revisions: {metrics['working_revisions']}",
            f"- Open exceptions: {metrics['exceptions']}",
            f"- Promotion candidates: {metrics['promotion_candidates']}",
            f"- Consolidation receipts / failed: {metrics['consolidation_receipts']} / {metrics['failed_receipts']}",
            f"- Receipt schema versions: {metrics['receipt_versions']}",
            f"- Objects with current valid Receipt v2: {metrics['objects_with_current_v2']}",
            f"- Pending recovery journals: {metrics['recovery_journals']}",
            f"- Drift warnings / high severity: {metrics['drift_warnings']} / {metrics['high_severity_drift']}",
            f"- Corpus sources / knowledge objects: {metrics['corpus']['sources']} / {metrics['corpus']['knowledge_objects']}",
            end,
        ]
        block = "\n".join(rows)
        if start in text and end in text:
            prefix, remainder = text.split(start, 1)
            _, suffix = remainder.split(end, 1)
            text = prefix.rstrip() + "\n\n" + block + suffix
        else:
            marker = "## Current metrics"
            if marker not in text:
                text = text.rstrip() + "\n\n" + marker + "\n"
            before, after = text.split(marker, 1)
            text = before + marker + "\n\n" + block + after
        atomic_write_text(path, text.rstrip() + "\n")
        return {"ok": True, "path": self.repository.rel(path), "metrics": metrics}
