from __future__ import annotations

from collections import Counter
from typing import Any

from .lifecycle import SourceLifecycleService
from .markdown import read_document
from .proposals import ProposalService
from .repository import Repository


class MaintenanceService:
    """Summarize actionable maintenance state without changing truth-layer files."""

    def __init__(self, repository: Repository):
        self.repository = repository

    def inventory(self) -> dict[str, Any]:
        canonical = []
        for path in self.repository.canonical_documents():
            metadata, _ = read_document(path)
            canonical.append((path, metadata))

        proposals = []
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            proposals.append((path, metadata))

        followups = []
        for path in self.repository.followup_documents():
            metadata, _ = read_document(path)
            followups.append((path, metadata))

        receipts = []
        receipts_path = self.repository.root / "vault" / "receipts"
        for path in sorted(receipts_path.glob("receipt-*.md")) if receipts_path.exists() else []:
            metadata, _ = read_document(path)
            receipts.append((path, metadata))

        captured_hashes = set()
        for source_path in self.repository.source_documents():
            metadata, _ = read_document(source_path)
            captured_hashes.add(str(metadata.get("content_sha256", "")))

        weak_evidence = [
            self.repository.rel(path) for path, metadata in canonical
            if metadata.get("type") == "claim"
            and metadata.get("evidence_coverage") in {"partial", "missing"}
        ]
        weak_proposal_items = []
        for path, metadata in proposals:
            if metadata.get("status") not in {"pending", "deferred"}:
                continue
            items = metadata.get("bundle_items")
            if isinstance(items, list):
                for item in items:
                    if (
                        isinstance(item, dict)
                        and item.get("decision") not in {"approved", "rejected", "superseded"}
                        and item.get("object_type") == "claim"
                        and item.get("evidence_coverage") in {"partial", "missing"}
                    ):
                        weak_proposal_items.append(
                            f"{metadata.get('id')}:{item.get('item_id')}"
                        )
                continue
            candidate_value = metadata.get("candidate_path")
            if candidate_value:
                candidate_path = self.repository.resolve_inside(str(candidate_value))
                if candidate_path.exists():
                    candidate, _ = read_document(candidate_path)
                    if (
                        candidate.get("type") == "claim"
                        and candidate.get("evidence_coverage") in {"partial", "missing"}
                    ):
                        weak_proposal_items.append(str(metadata.get("id")))
        stale_or_historical = [
            self.repository.rel(path) for path, metadata in canonical
            if metadata.get("status") in {"contested", "superseded", "archived"}
            or metadata.get("stale_reason")
        ]
        uncaptured_receipts = [
            str(metadata.get("id")) for _, metadata in receipts
            if str(metadata.get("content_sha256", "")) not in captured_hashes
        ]

        proposal_counts = Counter(str(metadata.get("status", "unknown")) for _, metadata in proposals)
        canonical_counts = Counter(str(metadata.get("type", "unknown")) for _, metadata in canonical)
        open_followups = [
            str(metadata.get("id")) for _, metadata in followups
            if metadata.get("status") not in {"resolved", "closed", "superseded"}
        ]
        inbox = ProposalService(self.repository).inbox()
        lifecycle = SourceLifecycleService(self.repository)
        unprepared_inbox = [
            item for item in inbox
            if lifecycle.status(str(item["id"])).state in {"captured", "extracted"}
        ]
        capture_only = [item for item in inbox if item not in unprepared_inbox]

        actions = []
        if uncaptured_receipts:
            actions.append(f"route {len(uncaptured_receipts)} receipt(s) through gm receipt propose")
        if proposal_counts["pending"] or proposal_counts["deferred"]:
            actions.append(
                f"review {proposal_counts['pending']} pending and {proposal_counts['deferred']} deferred proposal(s) selectively"
            )
        if unprepared_inbox:
            actions.append(f"triage {len(unprepared_inbox)} unprepared inbox source(s)")
        if weak_evidence:
            actions.append(f"review evidence boundaries for {len(weak_evidence)} canonical claim(s)")
        if weak_proposal_items:
            actions.append(
                f"keep {len(weak_proposal_items)} weak-evidence proposal item(s) out of confirmed canonical"
            )
        if open_followups:
            actions.append(f"resolve {len(open_followups)} open follow-up(s)")
        if not actions:
            actions.append("no governance backlog detected")

        return {
            "canonical_by_type": dict(sorted(canonical_counts.items())),
            "proposals_by_status": dict(sorted(proposal_counts.items())),
            "inbox_count": len(inbox),
            "inbox_source_ids": [item["id"] for item in inbox],
            "triage_backlog_count": len(unprepared_inbox),
            "triage_backlog_source_ids": [item["id"] for item in unprepared_inbox],
            "capture_only_count": len(capture_only),
            "receipt_count": len(receipts),
            "uncaptured_receipt_ids": uncaptured_receipts,
            "open_followup_ids": open_followups,
            "weak_evidence_paths": weak_evidence,
            "weak_evidence_proposal_items": weak_proposal_items,
            "stale_or_historical_paths": stale_or_historical,
            "recommended_actions": actions,
        }
