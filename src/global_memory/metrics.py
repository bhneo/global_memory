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
        languages: Counter[str] = Counter()
        documents = [*self.repository.memory_documents(), *self.repository.canonical_documents()]
        for path in documents:
            metadata, body = read_document(path)
            tier = infer_tier(metadata, path)
            epistemic = infer_epistemic_status(metadata, tier)
            tier_counts[tier] += 1
            epistemic_counts[epistemic] += 1
            if tier == "trusted":
                if metadata.get("needs_policy_requalification"):
                    trusted_awaiting += 1
                elif metadata.get("trust_policy_version") == POLICY_VERSION:
                    trusted_qualified += 1
                if epistemic == "contested":
                    trusted_contested += 1
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
        receipt_counts = ConsolidationReceiptService(self.repository).counts()
        receipt_versions: Counter[str] = Counter()
        for receipt_path in ConsolidationReceiptService(self.repository).documents():
            receipt, _ = read_document(receipt_path)
            receipt_versions[f"v{int(receipt.get('receipt_schema_version', 1))}"] += 1
        current_v2_objects = sum(
            ConsolidationReceiptService(self.repository).valid_for(str(read_document(path)[0]["id"])) is not None
            for path in documents
        )
        recovery_directory = self.repository.root / "system" / "recovery"
        recovery_journals = len(list(recovery_directory.glob("*.json"))) if recovery_directory.exists() else 0
        drift = DriftAuditService(self.repository).run()
        return {
            "generated_at": now_iso(),
            "working": tier_counts["working"],
            "trusted": tier_counts["trusted"],
            "trusted_v3_qualified": trusted_qualified,
            "trusted_awaiting_requalification": trusted_awaiting,
            "trusted_contested": trusted_contested,
            "canonical": tier_counts["canonical"],
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
            f"- Trusted v3-qualified / awaiting requalification / contested: {metrics['trusted_v3_qualified']} / {metrics['trusted_awaiting_requalification']} / {metrics['trusted_contested']}",
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
