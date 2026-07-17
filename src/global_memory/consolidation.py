from __future__ import annotations

import hashlib
from collections import Counter
from pathlib import Path
from typing import Any

from .bundle import BundleCompiler
from .governance import PromotionService
from .markdown import atomic_write_text, read_document, render_document
from .memory import ExceptionService, WorkingMemoryService
from .proposals import ProposalService
from .repository import Repository, now_iso
from .triage import DailyTriageService


class DriftAuditService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def run(self) -> dict[str, Any]:
        issues: list[dict[str, Any]] = []
        checked = 0
        for path in [*self.repository.memory_documents(), *self.repository.canonical_documents()]:
            metadata, body = read_document(path)
            checked += 1
            object_id = str(metadata["id"])
            if metadata.get("type") == "claim":
                for evidence in metadata.get("evidence", []):
                    if evidence.get("evidence_kind") == "translation" and evidence.get("verification_status") in {"exact", "verbatim"}:
                        issues.append({"object_id": object_id, "kind": "translation-as-quote", "path": self.repository.rel(path)})
                if not metadata.get("source_ids") or not metadata.get("evidence"):
                    issues.append({"object_id": object_id, "kind": "claim-source-drift", "path": self.repository.rel(path)})
            if metadata.get("type") == "synthesis" and (not metadata.get("source_ids") or "## New evidence" not in body):
                issues.append({"object_id": object_id, "kind": "unsupported-synthesis", "path": self.repository.rel(path)})
            if metadata.get("type") == "analogy" and not metadata.get("where_it_breaks"):
                issues.append({"object_id": object_id, "kind": "analogy-boundary-loss", "path": self.repository.rel(path)})
            if metadata.get("claim_confidence") == "high" and metadata.get("evidence_entailment") not in {"full"}:
                issues.append({"object_id": object_id, "kind": "uncertainty-erasure", "path": self.repository.rel(path)})
        return {"ok": not issues, "checked": checked, "issues": issues, "writes": 0}


class ConsolidationService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.exceptions = ExceptionService(repository)
        self.promotions = PromotionService(repository)

    def _increment_review(self, path: Path) -> bool:
        metadata, body = read_document(path)
        if metadata.get("user_locked"):
            return False
        timestamp = now_iso()
        if str(metadata.get("last_consolidated_at", ""))[:10] == timestamp[:10]:
            return False
        metadata["consolidation_count"] = int(metadata.get("consolidation_count", 0)) + 1
        metadata["last_consolidated_at"] = timestamp
        metadata["updated_at"] = metadata["last_consolidated_at"]
        metadata["updated_by"] = "weekly-consolidation-v1"
        atomic_write_text(path, render_document(metadata, body))
        return True

    def daily(self, *, limit: int = 25) -> dict[str, Any]:
        triage = DailyTriageService(self.repository).run(limit=limit)
        compiled = []
        blocked_sources = {
            str(item.get("context", {}).get("source_id"))
            for item in self.exceptions.list({"open", "deferred"})
            if item.get("exception_kind") == "daily-compile"
        }
        for item in ProposalService(self.repository).inbox()[:limit]:
            source_id = str(item["id"])
            if source_id in blocked_sources:
                compiled.append({"source_id": source_id, "status": "blocked-by-open-exception"})
                continue
            try:
                result = BundleCompiler(self.repository).compile(source_id)
                if result.proposal_id:
                    written = WorkingMemoryService(self.repository).ingest_bundle(
                        result.proposal_id, rebuild_index=False
                    )
                    compiled.append({"source_id": source_id, "status": "working", **written.__dict__})
            except Exception as exc:
                exception_id = self.exceptions.create(
                    "daily-compile", f"Daily compile failed: {source_id}", [str(exc)],
                    source_ids=[source_id], context={"source_id": source_id, "error": str(exc)},
                )
                compiled.append({"source_id": source_id, "status": "exception", "exception_id": exception_id})
        self.repository.rebuild_index()
        return {"mode": "daily-consolidation", "triage": triage, "compiled": compiled, "canonical_writes": 0}

    def weekly(self) -> dict[str, Any]:
        before = list(self.repository.memory_documents())
        reviewed = 0
        for path in before:
            reviewed += int(self._increment_review(path))
        self.repository.rebuild_index()
        promoted, retained = [], []
        for path in list(self.repository.memory_documents()):
            metadata, _ = read_document(path)
            if metadata.get("status") != "working":
                continue
            result = self.promotions.promote_trusted(
                str(metadata["id"]), automatic=True, rebuild_index=False
            )
            if result.get("promoted"):
                promoted.append(str(metadata["id"]))
            else:
                retained.append({"object_id": str(metadata["id"]), "failed_conditions": result["evaluation"]["failed_conditions"]})
        self.repository.rebuild_index()
        drift = DriftAuditService(self.repository).run()
        for issue in drift["issues"]:
            self.exceptions.create(
                "memory-drift", f"Drift audit: {issue['object_id']}", [issue["kind"]],
                object_id=issue["object_id"], context=issue,
            )
        canonical_candidates = []
        for path in self.repository.memory_documents():
            metadata, _ = read_document(path)
            if metadata.get("status") == "trusted" and metadata.get("type") in {"decision", "architecture", "goal", "project", "synthesis"}:
                canonical_candidates.append(self.promotions.recommend_canonical(str(metadata["id"]), "high-impact trusted memory"))
        exceptions = self.exceptions.list({"open", "deferred"})
        raw_count = len(list(self.repository.source_documents()))
        working_count = sum(read_document(path)[0].get("status") == "working" for path in self.repository.memory_documents())
        trusted_count = sum(read_document(path)[0].get("status") == "trusted" for path in self.repository.memory_documents())
        review_items = len(exceptions) + len(canonical_candidates)
        original_review = max(1, raw_count)
        retention_reasons = Counter(
            reason for item in retained for reason in item["failed_conditions"]
        )
        report = {
            "mode": "weekly-consolidation", "raw_item_count": raw_count,
            "working_changes": reviewed, "working_count": working_count,
            "trusted_promotions": len(promoted), "trusted_count": trusted_count,
            "exceptions": len(exceptions), "canonical_candidates": len(canonical_candidates),
            "estimated_human_review_minutes": review_items * 3,
            "compression_ratio": round(1 - review_items / original_review, 4),
            "promoted_ids": promoted, "retained_working_count": len(retained),
            "retained_working": retained[:20],
            "retained_working_omitted": max(0, len(retained) - 20),
            "retention_reason_counts": dict(retention_reasons.most_common()),
            "exception_ids": [item["id"] for item in exceptions],
            "canonical_promotion_ids": [item["promotion_id"] for item in canonical_candidates],
            "drift": drift, "canonical_writes": 0,
        }
        report_id = "weekly_" + hashlib.sha256(now_iso()[:10].encode()).hexdigest()[:16]
        report_path = self.repository.root / "system" / "reports" / f"generated-{report_id}.md"
        atomic_write_text(report_path, "# Weekly Consolidation Digest\n\n" + "\n".join(f"- {key}: {value}" for key, value in report.items() if not isinstance(value, (list, dict))) + "\n")
        report["report_path"] = self.repository.rel(report_path)
        return report


class ProposalGateMigration:
    def __init__(self, repository: Repository):
        self.repository = repository

    def plan(self) -> dict[str, Any]:
        pending, items, invalid, preserved = 0, 0, 0, Counter()
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            status = str(metadata.get("status"))
            preserved[status] += 1
            if status not in {"pending", "deferred"}:
                continue
            pending += 1
            bundle = metadata.get("bundle_items")
            if isinstance(bundle, list):
                for item in bundle:
                    if item.get("decision") in {"pending", "deferred"}:
                        items += 1
                        if item.get("atomicity_status") == "compound" or item.get("evidence_coverage") == "missing":
                            invalid += 1
            elif metadata.get("candidate_path"):
                items += 1
            else:
                invalid += 1
        return {
            "dry_run": True, "pending_proposals": pending, "candidate_items": items,
            "predicted_working": max(0, items - invalid), "predicted_exceptions": invalid,
            "canonical_unchanged": len(list(self.repository.canonical_documents())),
            "preserved_by_status": dict(sorted(preserved.items())),
        }

    def apply(self) -> dict[str, Any]:
        plan = self.plan()
        if plan["pending_proposals"] == 0:
            return {
                **plan, "dry_run": False, "backup_path": None,
                "migrated_working_objects": 0, "exceptions_created": 0,
                "results": [], "idempotent_noop": True,
            }
        timestamp = now_iso().replace(":", "-")
        backup = self.repository.root / "data" / "backups" / f"promotion-migration-{timestamp}"
        backup.mkdir(parents=True, exist_ok=False)
        for path in self.repository.proposal_documents():
            shutil_target = backup / path.name
            shutil_target.write_bytes(path.read_bytes())
        results = []
        for path in list(self.repository.proposal_documents()):
            metadata, _ = read_document(path)
            if metadata.get("status") not in {"pending", "deferred"}:
                continue
            result = WorkingMemoryService(self.repository).ingest_bundle(
                str(metadata["id"]), rebuild_index=False
            )
            results.append(result.__dict__)
        self.repository.rebuild_index()
        report = {
            **plan, "dry_run": False, "backup_path": self.repository.rel(backup),
            "migrated_working_objects": sum(len(item["written"]) + len(item["updated"]) for item in results),
            "exceptions_created": sum(len(item["exceptions"]) for item in results),
            "results": results, "canonical_unchanged": len(list(self.repository.canonical_documents())),
        }
        return report
