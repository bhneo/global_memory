from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .consolidation import ConsolidationReceiptService
from .epistemics import default_epistemic_status, infer_epistemic_status, infer_tier
from .markdown import atomic_write_text, read_document, render_document
from .memory import ExceptionService
from .repository import Repository, now_iso, sha256_bytes
from .governance import TrustedPromotionRecoveryManager
from .proposals import CANONICAL_STATUSES, ProposalService


CHANGE_TYPES = {"support", "refine", "limit", "contradict", "supersede", "metadata_only"}


class KnowledgeEvolutionService:
    """Apply explicit semantic changes while preserving trusted versions and tier boundaries."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.exceptions = ExceptionService(repository)
        self.receipts = ConsolidationReceiptService(repository)
        self.recovery = TrustedPromotionRecoveryManager(repository)

    def _snapshot(self, path: Path, object_id: str) -> str:
        content = path.read_bytes()
        digest = sha256_bytes(content)
        target = self.repository.root / "vault" / "archive" / "versions" / object_id / f"{digest}.md"
        self.repository.immutable_write(target, content)
        return self.repository.rel(target)

    def _propose_canonical_evolution(
        self, path: Path, current: dict[str, Any], current_body: str,
        incoming: dict[str, Any], body: str, *, change_type: str,
        reason: str, trigger_source: str | None,
    ) -> dict[str, Any]:
        object_id = str(current["id"])
        incoming_sources = [str(item) for item in incoming.get("source_ids", [])]
        if trigger_source and trigger_source not in incoming_sources:
            incoming_sources.append(trigger_source)
        candidate = dict(current)
        candidate_body = current_body
        changed_fields: list[str] = []
        if change_type in {"support", "metadata_only", "contradict"}:
            candidate["source_ids"] = list(dict.fromkeys([*current.get("source_ids", []), *incoming_sources]))
            existing_evidence = [item for item in current.get("evidence", []) if isinstance(item, dict)]
            incoming_evidence = [item for item in incoming.get("evidence", []) if isinstance(item, dict)]
            known = {item.get("evidence_id") for item in existing_evidence}
            candidate["evidence"] = [*existing_evidence, *[item for item in incoming_evidence if item.get("evidence_id") not in known]]
            changed_fields = ["source_ids", "evidence"]
            if change_type == "contradict":
                candidate["epistemic_status"] = "contested"
                candidate["unresolved_contradictions"] = list(dict.fromkeys([
                    *[str(item) for item in current.get("unresolved_contradictions", [])],
                    *incoming_sources,
                ]))
                changed_fields.extend(["epistemic_status", "unresolved_contradictions"])
        else:
            candidate.update(incoming)
            candidate["id"] = object_id
            candidate["type"] = current["type"]
            candidate["created_at"] = current["created_at"]
            candidate_body = body
            changed_fields = ["body"]
        record = self._record(change_type, current_body, candidate_body, reason, trigger_source, [], changed_fields)
        candidate["change_history"] = [*current.get("change_history", []), record]
        candidate["status"] = "proposal"
        proposed_status = "contested" if change_type == "contradict" else str(current.get("status", "confirmed"))
        candidate["proposed_status"] = proposed_status if proposed_status in CANONICAL_STATUSES else "confirmed"
        candidate["updated_at"] = now_iso()
        candidate["updated_by"] = "knowledge-evolution-proposal-v1"
        candidate_text = render_document(candidate, candidate_body)
        digest = sha256_bytes(candidate_text.encode("utf-8"))
        temporary = self.repository.root / "system" / "tmp" / f"canonical-evolution-{object_id}-{digest[:16]}.md"
        atomic_write_text(temporary, candidate_text)
        try:
            proposal = ProposalService(self.repository).propose_update(object_id, temporary, reason)
        finally:
            temporary.unlink(missing_ok=True)
        exception_id = None
        if change_type == "contradict":
            exception_id = self.exceptions.create(
                "canonical-conflict", f"Contradiction: {current.get('title', object_id)}",
                [reason.strip()], object_id=object_id, source_ids=incoming_sources,
                severity="must_confirm", context={"change": record, "proposal_id": proposal.proposal_id},
            )
        return {
            "action": "canonical_proposal", "object_id": object_id, "memory_tier": "canonical",
            "proposal_id": proposal.proposal_id, "proposal_path": proposal.proposal_path,
            "exception_id": exception_id, "change": record,
            "updated_object_count": 0, "knowledge_reuse_count": 1,
        }

    @staticmethod
    def _record(
        change_type: str, previous: str, current: str, reason: str,
        trigger_source: str | None, evidence_added: list[str], changed_fields: list[str],
    ) -> dict[str, Any]:
        return {
            "change_type": change_type,
            "previous_statement": previous.strip(),
            "new_statement": current.strip(),
            "changed_fields": changed_fields,
            "reason": reason.strip(),
            "trigger_source": trigger_source,
            "evidence_added": evidence_added,
        }

    def apply(
        self, object_id: str, incoming: dict[str, Any], body: str, *,
        change_type: str, reason: str, trigger_source: str | None = None,
    ) -> dict[str, Any]:
        if change_type not in CHANGE_TYPES:
            raise ValueError(f"unsupported knowledge change type: {change_type}")
        if not reason.strip():
            raise ValueError("knowledge evolution requires a reason")
        path, current, current_body = self.repository.find_document(object_id)
        tier = infer_tier(current, path)
        epistemic = infer_epistemic_status(current, tier)
        incoming_sources = [str(item) for item in incoming.get("source_ids", [])]
        if trigger_source and trigger_source not in incoming_sources:
            incoming_sources.append(trigger_source)
        incoming_evidence = [item for item in incoming.get("evidence", []) if isinstance(item, dict)]
        evidence_ids = [str(item.get("evidence_id")) for item in incoming_evidence if item.get("evidence_id")]
        if change_type == "contradict":
            contradiction_evidence = [
                item for item in incoming_evidence
                if item.get("stance") == "contradicts" and item.get("source_id")
                and item.get("excerpt") and item.get("reason")
            ]
            if not contradiction_evidence:
                raise ValueError("contradict requires source-linked contradictory evidence with excerpt and reason")

        if tier == "canonical":
            return self._propose_canonical_evolution(
                path, current, current_body, incoming, body,
                change_type=change_type, reason=reason,
                trigger_source=trigger_source,
            )

        if tier == "trusted" and change_type in {"refine", "limit", "supersede"}:
            previous_version = self._snapshot(path, object_id)
            stable = f"{object_id}:{change_type}:{sha256_bytes(body.encode('utf-8'))}:{trigger_source or ''}"
            revision_id = "revision_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:24]
            revision = dict(incoming)
            revision.update({
                "id": revision_id,
                "type": current["type"],
                "status": "working",
                "memory_tier": "working",
                "epistemic_status": incoming.get("epistemic_status") or default_epistemic_status(str(current["type"])),
                "title": incoming.get("title") or current["title"],
                "created_at": now_iso(), "updated_at": now_iso(),
                "aliases": list(incoming.get("aliases", current.get("aliases", []))),
                "tags": list(incoming.get("tags", current.get("tags", []))),
                "domains": list(incoming.get("domains", current.get("domains", []))),
                "confidence": incoming.get("confidence", current.get("confidence", "unknown")),
                "source_ids": list(dict.fromkeys([*current.get("source_ids", []), *incoming_sources])),
                "relations": [
                    *[item for item in incoming.get("relations", []) if isinstance(item, dict)],
                    {"type": "refines" if change_type == "refine" else "limits" if change_type == "limit" else "supersedes",
                     "target_id": object_id, "reason": reason.strip()},
                ],
                "created_by": "knowledge-evolution-v1", "updated_by": "knowledge-evolution-v1",
                "consolidation_count": 0, "promotion_history": [], "trust_score": 0,
                "trust_reasons": [], "revision_of": object_id, "previous_version": previous_version,
                "needs_revalidation": True, "memory_schema_version": 2,
            })
            record = self._record(change_type, current_body, body, reason, trigger_source, evidence_ids, ["body"])
            revision["change_record"] = record
            revision_path = self.repository.root / "vault" / "memory" / "revisions" / str(current["type"]) / f"{revision_id}.md"
            self.repository.immutable_write(revision_path, render_document(revision, body).encode("utf-8"))
            self.repository.rebuild_index()
            self.repository.append_event("memory-events", {
                "event": "working-revision-created", "object_id": object_id,
                "revision_id": revision_id, "change_type": change_type,
            })
            return {
                "action": "working_revision", "object_id": object_id, "memory_tier": tier,
                "revision_id": revision_id, "revision_path": self.repository.rel(revision_path),
                "previous_version": previous_version, "change": record,
                "updated_object_count": 1, "knowledge_reuse_count": 1,
            }

        previous_version = self._snapshot(path, object_id) if tier in {"trusted", "canonical"} else None
        updated = dict(current)
        record = self._record(change_type, current_body, body, reason, trigger_source, evidence_ids, [])
        exception_id: str | None = None
        if change_type in {"support", "metadata_only"}:
            updated["source_ids"] = list(dict.fromkeys([*current.get("source_ids", []), *incoming_sources]))
            existing_evidence = [item for item in current.get("evidence", []) if isinstance(item, dict)]
            known = {item.get("evidence_id") for item in existing_evidence}
            updated["evidence"] = [*existing_evidence, *[item for item in incoming_evidence if item.get("evidence_id") not in known]]
            updated["last_verified_at"] = now_iso()
            updated["change_history"] = [*current.get("change_history", []), record]
            updated["updated_at"] = now_iso()
            updated["updated_by"] = "knowledge-evolution-v1"
            # The existing tier and epistemic interpretation remain intact.
            updated["status"] = tier
            updated["memory_tier"] = tier
            updated["epistemic_status"] = epistemic
            record["changed_fields"] = ["source_ids", "evidence", "last_verified_at"]
            new_body = current_body
            result = "supported" if change_type == "support" else "unchanged"
        elif change_type == "contradict":
            updated["memory_tier"] = tier
            updated["status"] = tier
            updated["epistemic_status"] = "contested"
            updated["source_ids"] = list(dict.fromkeys([*current.get("source_ids", []), *incoming_sources]))
            existing_evidence = [item for item in current.get("evidence", []) if isinstance(item, dict)]
            known = {item.get("evidence_id") for item in existing_evidence}
            updated["evidence"] = [*existing_evidence, *[item for item in incoming_evidence if item.get("evidence_id") not in known]]
            updated["unresolved_contradictions"] = list(dict.fromkeys([
                *[str(item) for item in current.get("unresolved_contradictions", [])],
                *incoming_sources,
            ]))
            updated["updated_at"] = now_iso()
            updated["updated_by"] = "knowledge-evolution-v1"
            updated["change_history"] = [*current.get("change_history", []), record]
            record["changed_fields"] = ["epistemic_status", "source_ids", "evidence", "unresolved_contradictions"]
            exception_id = self.exceptions.create(
                "canonical-conflict" if tier == "canonical" else "trusted-conflict",
                f"Contradiction: {current.get('title', object_id)}",
                [reason.strip()], object_id=object_id, source_ids=incoming_sources,
                severity="must_confirm", context={"change": record, "previous_version": previous_version},
            )
            new_body = current_body
            result = "contradicted"
        else:
            # Working objects can evolve directly, but their change stays explicit.
            updated.update(incoming)
            updated["id"] = current["id"]
            updated["created_at"] = current["created_at"]
            updated["status"] = "working"
            updated["memory_tier"] = "working"
            updated["epistemic_status"] = incoming.get("epistemic_status") or epistemic
            updated["change_history"] = [*current.get("change_history", []), record]
            updated["updated_at"] = now_iso()
            updated["updated_by"] = "knowledge-evolution-v1"
            new_body = body
            result = {"refine": "refined", "limit": "limited", "supersede": "superseded"}[change_type]
        before_bytes = path.read_bytes()
        staged_text = render_document(updated, new_body)
        event = {
            "event": f"knowledge-{change_type}", "object_id": object_id,
            "memory_tier": tier, "exception_id": exception_id,
        }
        evolution_id = "evolution_" + hashlib.sha256(
            f"{object_id}:{change_type}:{sha256_bytes(staged_text.encode('utf-8'))}".encode("utf-8")
        ).hexdigest()[:24]
        journal = None
        if tier == "trusted":
            journal = self.recovery.prepare(
                evolution_id, path, before_bytes, staged_text,
                operation=f"trusted_{change_type}", event=event,
            )
        try:
            atomic_write_text(path, staged_text)
            if journal:
                self.recovery.checkpoint(journal, "staged")
            self.repository.rebuild_index()
            receipt = self.receipts.consolidate(
                object_id, result=result, changes=[record], change_summary=reason,
                exceptions_created=[exception_id] if exception_id else [],
            )
            if tier == "trusted" and not self.receipts.complete(receipt):
                raise ValueError("trusted evolution rolled back because consolidation receipt failed")
            if journal:
                self.recovery.checkpoint(journal, "receipt_completed", receipt["consolidation_id"])
        except Exception:
            path.write_bytes(before_bytes)
            self.repository.rebuild_index()
            if journal:
                journal.unlink(missing_ok=True)
            raise
        event_with_recovery = {
            **event, "recovery_operation_id": evolution_id,
            "receipt_id": receipt["consolidation_id"],
        }
        self.repository.append_event("memory-events", event_with_recovery)
        if journal:
            self.recovery.checkpoint(journal, "event_logged")
            self.recovery.checkpoint(journal, "finalized")
            journal.unlink(missing_ok=True)
        return {
            "action": change_type, "object_id": object_id, "memory_tier": tier,
            "epistemic_status": updated.get("epistemic_status"),
            "previous_version": previous_version, "change": record,
            "receipt_id": receipt["consolidation_id"], "exception_id": exception_id,
            "updated_object_count": 1, "knowledge_reuse_count": 1,
        }
