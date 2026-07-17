from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ValidationError
from .epistemics import default_epistemic_status, infer_epistemic_status
from .markdown import atomic_write_text, read_document, render_document
from .memory import ExceptionService
from .proposals import CANONICAL_DIRECTORIES
from .repository import Repository, now_iso, sha256_bytes


POLICY_VERSION = "trusted-promotion-v3-receipt-v2"
AUTO_TRUSTED_TYPES = {"claim", "concept"}


def qualification_scope(object_type: str) -> str:
    return {
        "claim": "factual_reliability", "concept": "factual_reliability",
        "question": "durable_question", "tension": "durable_tension",
        "hypothesis": "exploratory_hypothesis", "analogy": "exploratory_analogy",
    }.get(object_type, "user_endorsed")


class TrustedPromotionRecoveryManager:
    """Crash-safe journal for governed object write -> Receipt -> event boundaries."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "system" / "recovery"

    def pending(self) -> list[Path]:
        return sorted(self.directory.glob("trusted-promotion-*.json")) if self.directory.exists() else []

    def prepare(
        self, promotion_id: str, target: Path, before: bytes, staged_text: str, *,
        operation: str = "trusted_promotion", event: dict[str, Any] | None = None,
        expected_result: str | set[str] | None = None,
    ) -> Path:
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.directory / f"trusted-promotion-{promotion_id}.json"
        target_metadata, _ = read_document(target)
        default_results = {
            "trusted_promotion": "promotion_candidate",
            "trusted_requalification": "requalified",
            "trusted_support": "supported",
        }
        record = {
            "journal_version": 3, "operation": operation, "promotion_id": promotion_id,
            "operation_id": promotion_id,
            "phase": "prepared", "target_path": self.repository.rel(target),
            "before_sha256": sha256_bytes(before), "before_text": before.decode("utf-8"),
            "initial_staged_sha256": sha256_bytes(staged_text.encode("utf-8")),
            # Kept for old journals and operators; never overwritten after stage.
            "staged_sha256": sha256_bytes(staged_text.encode("utf-8")),
            "current_committed_sha256": None, "receipt_id": None,
            "object_id": str(target_metadata["id"]),
            "expected_result": expected_result or default_results.get(operation),
            "expected_event": event.get("event") if isinstance(event, dict) else None,
            "event": event,
        }
        atomic_write_text(path, json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        return path

    def checkpoint(self, path: Path, phase: str, receipt_id: str | None = None) -> None:
        record = json.loads(path.read_text(encoding="utf-8"))
        transitions = {
            "prepared": {"staged"},
            "staged": {"receipt_completed"},
            "receipt_completed": {"event_logged"},
            "event_logged": {"finalized"},
        }
        current = str(record.get("phase"))
        if phase not in transitions.get(current, set()):
            raise ValidationError(f"invalid recovery phase transition: {current} -> {phase}")
        record["phase"] = phase
        record["receipt_id"] = receipt_id or record.get("receipt_id")
        if phase == "receipt_completed":
            target = self.repository.resolve_inside(str(record["target_path"]))
            record["current_committed_sha256"] = sha256_bytes(target.read_bytes())
        atomic_write_text(path, json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    def _event_already_logged(self, operation_id: str) -> bool:
        log_path = self.repository.root / "system" / "logs" / "memory-events.jsonl"
        if not log_path.exists():
            return False
        marker = f'"recovery_operation_id": "{operation_id}"'
        return marker in log_path.read_text(encoding="utf-8")

    def _matching_committed_receipt(self, record: dict[str, Any], current: str | None) -> dict[str, Any] | None:
        """Prove that a journal can safely roll forward instead of guessing."""
        receipt_id = str(record.get("receipt_id") or "")
        object_id = str(record.get("object_id") or "")
        if not object_id or current is None:
            return None
        committed_sha = record.get("current_committed_sha256")
        if committed_sha and current != committed_sha:
            return None
        try:
            from .consolidation import ConsolidationReceiptService

            receipts = ConsolidationReceiptService(self.repository)
            receipt = receipts.load(receipt_id)[1] if receipt_id else receipts.valid_for(object_id)
            if receipt is None:
                return None
            expected_result = record.get("expected_result")
            allowed_results = {expected_result} if isinstance(expected_result, str) else set(expected_result or [])
            if (
                int(receipt.get("receipt_schema_version", 1)) >= 2
                and receipts.complete(receipt)
                and receipt.get("object_id") == object_id
                and receipt.get("object_sha256_after") == current
                and (not allowed_results or receipt.get("result") in allowed_results)
                and receipts.valid_for(object_id) is not None
            ):
                return receipt
            return None
        except Exception:
            return None

    def _valid_committed_receipt(self, record: dict[str, Any], current: str | None) -> bool:
        return self._matching_committed_receipt(record, current) is not None

    def _finalize_event(self, journal: Path, record: dict[str, Any]) -> None:
        event = record.get("event")
        operation_id = str(record.get("operation_id") or record.get("promotion_id"))
        if isinstance(event, dict) and record.get("expected_event") == event.get("event") and not self._event_already_logged(operation_id):
            self.repository.append_event("memory-events", {**event, "recovery_operation_id": operation_id})
        self.checkpoint(journal, "event_logged")
        self.checkpoint(journal, "finalized")
        journal.unlink()

    def recover_all(self) -> dict[str, list[dict[str, str]]]:
        recovered, blocked = [], []
        for journal in self.pending():
            try:
                record = json.loads(journal.read_text(encoding="utf-8"))
                target = self.repository.resolve_inside(str(record["target_path"]))
                current = sha256_bytes(target.read_bytes()) if target.exists() else None
                phase = record.get("phase")
                if phase == "finalized":
                    journal.unlink()
                    recovered.append({"journal": self.repository.rel(journal), "status": "finalized"})
                elif phase in {"event_logged", "receipt_completed"}:
                    if not self._valid_committed_receipt(record, current):
                        blocked.append({"journal": self.repository.rel(journal), "error": "receipt is missing, stale, or does not match this governed operation"})
                        continue
                    if phase == "event_logged":
                        self.checkpoint(journal, "finalized")
                        journal.unlink()
                    else:
                        self._finalize_event(journal, record)
                    recovered.append({"journal": self.repository.rel(journal), "status": "finalized"})
                elif phase == "prepared" and current == record.get("before_sha256"):
                    journal.unlink()
                    recovered.append({"journal": self.repository.rel(journal), "status": "not_started"})
                elif phase == "staged" and current == record.get("before_sha256"):
                    journal.unlink()
                    recovered.append({"journal": self.repository.rel(journal), "status": "abort-before-stage"})
                elif phase == "staged" and current == record.get("initial_staged_sha256", record.get("staged_sha256")):
                    target.write_bytes(str(record["before_text"]).encode("utf-8"))
                    journal.unlink()
                    recovered.append({"journal": self.repository.rel(journal), "status": "rolled_back"})
                elif phase == "staged" and (receipt := self._matching_committed_receipt(record, current)) is not None:
                    # Receipt may have reached disk before the checkpoint write.
                    self.checkpoint(journal, "receipt_completed", str(receipt["consolidation_id"]))
                    self._finalize_event(journal, record)
                    recovered.append({"journal": self.repository.rel(journal), "status": "rolled_forward_after_missing_checkpoint"})
                else:
                    blocked.append({"journal": self.repository.rel(journal), "error": "target no longer matches staged state"})
            except Exception as exc:
                blocked.append({"journal": self.repository.rel(journal), "error": str(exc)})
        if recovered:
            self.repository.rebuild_index()
        return {"recovered": recovered, "blocked": blocked}


class CanonicalPromotionRecoveryManager:
    """Journal the multi-file Trusted -> Canonical boundary.

    Canonical promotion temporarily removes the Trusted path because the index
    deliberately enforces one path for a stable object id.  The journal keeps
    the exact pre-image until a final, hash-bound Canonical Receipt exists.
    """

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "system" / "recovery"

    def pending(self) -> list[Path]:
        return sorted(self.directory.glob("canonical-promotion-*.json")) if self.directory.exists() else []

    def prepare(
        self, promotion_id: str, *, memory_path: Path, target_path: Path,
        card_path: Path, memory_before: bytes, card_before: bytes,
        canonical_text: str, card_after_text: str, event: dict[str, Any],
    ) -> Path:
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.directory / f"canonical-promotion-{promotion_id}.json"
        metadata, _ = read_document(memory_path)
        record = {
            "journal_version": 1, "operation": "canonical_promotion",
            "operation_id": promotion_id, "promotion_id": promotion_id,
            "object_id": str(metadata["id"]), "phase": "prepared",
            "memory_path": self.repository.rel(memory_path),
            "memory_before_sha256": sha256_bytes(memory_before),
            "memory_before_text": memory_before.decode("utf-8"),
            "target_path": self.repository.rel(target_path),
            "canonical_sha256": sha256_bytes(canonical_text.encode("utf-8")),
            "canonical_text": canonical_text,
            "card_path": self.repository.rel(card_path),
            "card_before_sha256": sha256_bytes(card_before),
            "card_before_text": card_before.decode("utf-8"),
            "card_after_sha256": sha256_bytes(card_after_text.encode("utf-8")),
            "card_after_text": card_after_text,
            "receipt_id": None, "event": event,
        }
        atomic_write_text(path, json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        return path

    def checkpoint(self, journal: Path, phase: str, receipt_id: str | None = None) -> None:
        record = json.loads(journal.read_text(encoding="utf-8"))
        transitions = {
            "prepared": {"canonical_written"},
            "canonical_written": {"trusted_removed"},
            "trusted_removed": {"receipt_completed"},
            "receipt_completed": {"card_updated"},
            "card_updated": {"event_logged"},
            "event_logged": {"finalized"},
        }
        if phase not in transitions.get(str(record.get("phase")), set()):
            raise ValidationError(f"invalid canonical recovery phase transition: {record.get('phase')} -> {phase}")
        record["phase"] = phase
        if receipt_id:
            record["receipt_id"] = receipt_id
            if isinstance(record.get("event"), dict):
                record["event"]["receipt_id"] = receipt_id
        if phase == "receipt_completed":
            target = self.repository.resolve_inside(str(record["target_path"]))
            record["committed_canonical_sha256"] = sha256_bytes(target.read_bytes())
        atomic_write_text(journal, json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    def _event_already_logged(self, operation_id: str) -> bool:
        log_path = self.repository.root / "system" / "logs" / "memory-events.jsonl"
        return log_path.exists() and f'"recovery_operation_id": "{operation_id}"' in log_path.read_text(encoding="utf-8")

    def _valid_receipt(self, record: dict[str, Any], target: Path) -> dict[str, Any] | None:
        if not target.exists():
            return None
        committed_sha = record.get("committed_canonical_sha256")
        current = sha256_bytes(target.read_bytes())
        if committed_sha and current != committed_sha:
            return None
        try:
            from .consolidation import ConsolidationReceiptService

            receipts = ConsolidationReceiptService(self.repository)
            receipt = receipts.load(str(record.get("receipt_id")))[1] if record.get("receipt_id") else receipts.valid_for(str(record["object_id"]))
            if receipt and (
                int(receipt.get("receipt_schema_version", 1)) >= 2
                and receipts.complete(receipt)
                and receipt.get("result") == "canonical_approved"
                and receipt.get("object_id") == record.get("object_id")
                and receipt.get("object_sha256_after") == current
                and receipts.valid_for(str(record["object_id"])) is not None
            ):
                return receipt
        except Exception:
            pass
        return None

    def _restore_before(self, journal: Path, record: dict[str, Any]) -> None:
        memory = self.repository.resolve_inside(str(record["memory_path"]))
        target = self.repository.resolve_inside(str(record["target_path"]))
        card = self.repository.resolve_inside(str(record["card_path"]))
        if memory.exists() and sha256_bytes(memory.read_bytes()) != record["memory_before_sha256"]:
            raise ValidationError("trusted source was externally modified during canonical recovery")
        if card.exists() and sha256_bytes(card.read_bytes()) not in {record["card_before_sha256"], record["card_after_sha256"]}:
            raise ValidationError("promotion card was externally modified during canonical recovery")
        if target.exists() and sha256_bytes(target.read_bytes()) != record["canonical_sha256"]:
            raise ValidationError("canonical target was externally modified during canonical recovery")
        target.unlink(missing_ok=True)
        memory.parent.mkdir(parents=True, exist_ok=True)
        memory.write_bytes(str(record["memory_before_text"]).encode("utf-8"))
        card.write_bytes(str(record["card_before_text"]).encode("utf-8"))
        journal.unlink(missing_ok=True)
        self.repository.rebuild_index()

    def _roll_forward(self, journal: Path, record: dict[str, Any], receipt: dict[str, Any]) -> None:
        memory = self.repository.resolve_inside(str(record["memory_path"]))
        target = self.repository.resolve_inside(str(record["target_path"]))
        card = self.repository.resolve_inside(str(record["card_path"]))
        if memory.exists():
            if sha256_bytes(memory.read_bytes()) != record["memory_before_sha256"]:
                raise ValidationError("trusted source was externally modified during canonical recovery")
            memory.unlink()
        if not target.exists():
            raise ValidationError("canonical target is missing during roll-forward")
        if not card.exists() or sha256_bytes(card.read_bytes()) != record["card_after_sha256"]:
            card.write_bytes(str(record["card_after_text"]).encode("utf-8"))
        phase = str(record.get("phase"))
        if phase == "trusted_removed":
            self.checkpoint(journal, "receipt_completed", str(receipt["consolidation_id"]))
            phase = "receipt_completed"
        if phase == "receipt_completed":
            self.checkpoint(journal, "card_updated")
            phase = "card_updated"
        if phase == "card_updated":
            operation_id = str(record["operation_id"])
            if not self._event_already_logged(operation_id):
                self.repository.append_event("memory-events", {**record["event"], "recovery_operation_id": operation_id})
            self.checkpoint(journal, "event_logged")
            phase = "event_logged"
        if phase == "event_logged":
            self.checkpoint(journal, "finalized")
        journal.unlink(missing_ok=True)
        self.repository.rebuild_index()

    def recover_all(self) -> dict[str, list[dict[str, str]]]:
        recovered, blocked = [], []
        for journal in self.pending():
            try:
                record = json.loads(journal.read_text(encoding="utf-8"))
                phase = str(record.get("phase"))
                memory = self.repository.resolve_inside(str(record["memory_path"]))
                target = self.repository.resolve_inside(str(record["target_path"]))
                if phase == "prepared" and not target.exists() and memory.exists() and sha256_bytes(memory.read_bytes()) == record["memory_before_sha256"]:
                    journal.unlink()
                    recovered.append({"journal": self.repository.rel(journal), "status": "not_started"})
                    continue
                if phase == "canonical_written":
                    self._restore_before(journal, record)
                    recovered.append({"journal": self.repository.rel(journal), "status": "rolled_back_before_source_removal"})
                    continue
                if phase in {"trusted_removed", "receipt_completed", "card_updated", "event_logged"}:
                    # With one stable id, the index can only be rebuilt after the
                    # Trusted copy is removed.  A valid final receipt is the sole
                    # authority for choosing roll-forward rather than rollback.
                    self.repository.rebuild_index()
                    receipt = self._valid_receipt(record, target)
                    if receipt:
                        self._roll_forward(journal, record, receipt)
                        recovered.append({"journal": self.repository.rel(journal), "status": "rolled_forward"})
                    else:
                        self._restore_before(journal, record)
                        recovered.append({"journal": self.repository.rel(journal), "status": "rolled_back_without_valid_receipt"})
                    continue
                if phase == "finalized":
                    journal.unlink()
                    recovered.append({"journal": self.repository.rel(journal), "status": "finalized"})
                else:
                    blocked.append({"journal": self.repository.rel(journal), "error": f"unknown canonical recovery phase: {phase}"})
            except Exception as exc:
                blocked.append({"journal": self.repository.rel(journal), "error": str(exc)})
        return {"recovered": recovered, "blocked": blocked}


@dataclass(frozen=True)
class PromotionEvaluation:
    object_id: str
    eligible: bool
    trust_score: int
    reasons: list[str]
    failed_conditions: list[str]
    supporting_sources: list[str]
    contradictions: list[str]

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


class PromotionService:
    def __init__(self, repository: Repository, failure_hook: Any | None = None):
        self.repository = repository
        self.directory = repository.root / "vault" / "promotions"
        self.exceptions = ExceptionService(repository)
        self.recovery = TrustedPromotionRecoveryManager(repository)
        self.canonical_recovery = CanonicalPromotionRecoveryManager(repository)
        self.failure_hook = failure_hook

    def _fail_if_requested(self, phase: str) -> None:
        if callable(self.failure_hook):
            self.failure_hook(phase)

    def evaluate(self, object_id: str, *, for_requalification: bool = False) -> PromotionEvaluation:
        path, metadata, body = self.repository.find_document(object_id)
        if not self.repository.rel(path).startswith("vault/memory/"):
            raise ValidationError("trusted promotion only evaluates working memory")
        reasons: list[str] = []
        failed: list[str] = []
        contradictions = [
            str(relation.get("target_id")) for relation in metadata.get("relations", [])
            if relation.get("type") == "contradicts" and relation.get("status") not in {"rejected", "superseded"}
        ]
        try:
            indexed_contradictions = [
                relation for relation in self.repository.related(object_id)
                if relation.get("relation_type") == "contradicts"
            ]
        except Exception as exc:
            indexed_contradictions = []
            failed.append(f"relation index unavailable: {exc}")
        contradictions = sorted({
            *contradictions,
            *[
                str(item["target_id"] if item["source_id"] == object_id else item["source_id"])
                for item in indexed_contradictions
            ],
        })
        object_type = str(metadata.get("type"))
        if object_type not in AUTO_TRUSTED_TYPES and not for_requalification:
            failed.append(f"automatic trusted promotion is paused for {object_type}")
        if metadata.get("user_locked") and metadata.get("status") != "trusted":
            failed.append("user_locked object cannot be automatically changed")
        from .consolidation import ConsolidationReceiptService
        receipt = ConsolidationReceiptService(self.repository).valid_for(object_id)
        if receipt is None:
            failed.append("requires a valid hash-bound consolidation receipt")
        else:
            reasons.append("valid consolidation receipt matches current object")
            semantic_failures = ConsolidationReceiptService.semantic_qualification_failures(object_type, receipt)
            if semantic_failures:
                failed.extend(semantic_failures)
            elif object_type == "claim":
                reasons.append("receipt records a semantic evidence-entailment recheck")
            elif object_type == "concept":
                reasons.append("receipt establishes concept independence by logical work")
        if contradictions:
            failed.append("unresolved direct contradiction")
        if metadata.get("unresolved_contradictions"):
            failed.append("unresolved contradiction metadata")
        if metadata.get("needs_revalidation") or metadata.get("pending_revision_id"):
            failed.append("working revision awaits revalidation")
        if metadata.get("user_rejected"):
            failed.append("user rejected promotion")
        if object_type == "claim":
            checks = {
                "atomic claim": metadata.get("atomicity_status") == "atomic",
                "full evidence coverage": metadata.get("evidence_coverage") == "full",
                "full evidence entailment": metadata.get("evidence_entailment") == "full",
                "good extraction": metadata.get("extraction_quality") == "good",
                "primary or official authority": metadata.get("epistemic_source_authority") in {"primary", "official", "peer_reviewed"},
                "explicit applicability": bool(metadata.get("applicability")),
                "supporting evidence exists": any(item.get("stance") == "supports" for item in metadata.get("evidence", [])),
                "drift audit has no high risk": not metadata.get("high_risk_drift"),
            }
            for label, passed in checks.items():
                (reasons if passed else failed).append(label)
        elif object_type == "concept":
            work_ids = {str(item) for item in metadata.get("reuse_work_ids", []) if item}
            for source_id in metadata.get("source_ids", []):
                try:
                    _, source, _ = self.repository.find_document(str(source_id))
                    work_id = source.get("work_id")
                    if work_id:
                        work_ids.add(str(work_id))
                except Exception:
                    continue
            if len(work_ids) >= 2:
                reasons.append("concept reused by two independent works")
            else:
                failed.append("concept requires two independent work_ids")
            if metadata.get("duplicate_of"):
                failed.append("unresolved duplicate concept")
        elif object_type not in AUTO_TRUSTED_TYPES:
            # These objects can still be manually promoted with an explicit reason.
            pass
        else:
            failed.append(f"automatic trusted policy is not defined for {object_type}")
        score = max(0, min(100, 50 + 8 * len(reasons) - 12 * len(failed)))
        return PromotionEvaluation(
            object_id, not failed, score, reasons, failed,
            [str(item) for item in metadata.get("source_ids", [])], contradictions,
        )

    def requalify_trusted(self, object_id: str, *, rebuild_index: bool = True) -> dict[str, Any]:
        """Qualify an existing Trusted object under the current policy without demoting it."""
        path, metadata, body = self.repository.find_document(object_id)
        if metadata.get("status") != "trusted" or metadata.get("memory_tier") != "trusted":
            raise ValidationError("policy requalification only applies to Trusted memory")
        if not metadata.get("needs_policy_requalification"):
            return {"requalified": False, "reason": "object is already policy-qualified"}

        from .consolidation import ConsolidationReceiptService
        receipts = ConsolidationReceiptService(self.repository)
        preliminary = receipts.valid_for(object_id) or receipts.consolidate(
            object_id,
            result="requalification_candidate",
            change_summary="Trusted memory checked under the current Receipt v2 boundary",
        )
        evaluation = self.evaluate(object_id, for_requalification=True)
        if not evaluation.eligible:
            return {
                "requalified": False,
                "receipt_id": preliminary["consolidation_id"],
                "evaluation": evaluation.as_dict(),
            }

        # The qualification fields change the governed bytes, so complete a second
        # Receipt against the final state. The recovery journal makes that boundary
        # restart-safe and never invents a demotion event.
        _, metadata, body = self.repository.find_document(object_id)
        before = path.read_bytes()
        timestamp = now_iso()
        qualification_id = "requalification_" + hashlib.sha256(
            f"{object_id}:{timestamp}:{POLICY_VERSION}".encode("utf-8")
        ).hexdigest()[:24]
        metadata.update({
            "needs_policy_requalification": False,
            "trust_policy_version": POLICY_VERSION,
            "last_policy_qualified_at": timestamp,
            "last_valid_receipt_id": None,
            "policy_requalification_failed_conditions": [],
            "trust_score": evaluation.trust_score,
            "trust_reasons": evaluation.reasons,
            "qualification_scope": qualification_scope(str(metadata.get("type"))),
            "updated_at": timestamp,
            "updated_by": POLICY_VERSION,
        })
        staged_text = render_document(metadata, body)
        event = {
            "event": "trusted-policy-requalified", "requalification_id": qualification_id,
            "object_id": object_id, "policy_version": POLICY_VERSION,
        }
        journal = self.recovery.prepare(
            qualification_id, path, before, staged_text,
            operation="trusted_requalification", event=event,
        )
        try:
            atomic_write_text(path, staged_text)
            self.recovery.checkpoint(journal, "staged")
            self.repository.rebuild_index()
            final_receipt = receipts.consolidate(
                object_id,
                result="requalified",
                change_summary=f"Trusted memory qualified under {POLICY_VERSION}",
                rebuild_index=False,
            )
            if not receipts.complete(final_receipt) or receipts.valid_for(object_id) is None:
                raise ValidationError("Trusted requalification receipt v2 did not complete")
            self.recovery.checkpoint(journal, "receipt_completed", final_receipt["consolidation_id"])
        except Exception:
            path.write_bytes(before)
            self.repository.rebuild_index()
            journal.unlink(missing_ok=True)
            raise
        # last_valid_receipt_id is intentionally not written back into the governed
        # object: doing so would change its hash and immediately stale the receipt.
        if rebuild_index:
            self.repository.rebuild_index()
        self.repository.append_event("memory-events", {
            **event, "receipt_id": final_receipt["consolidation_id"],
            "recovery_operation_id": qualification_id,
        })
        self.recovery.checkpoint(journal, "event_logged")
        self.recovery.checkpoint(journal, "finalized")
        journal.unlink(missing_ok=True)
        return {
            "requalified": True,
            "requalification_id": qualification_id,
            "receipt_id": final_receipt["consolidation_id"],
            "evaluation": evaluation.as_dict(),
            "path": self.repository.rel(path),
        }

    def _assert_canonical_gate(self, object_id: str, metadata: dict[str, Any]) -> None:
        from .consolidation import ConsolidationReceiptService
        failures: list[str] = []
        if metadata.get("needs_policy_requalification"):
            failures.append("Trusted object still awaits current-policy requalification")
        if metadata.get("trust_policy_version") != POLICY_VERSION:
            failures.append(f"Trusted object is not qualified under {POLICY_VERSION}")
        if ConsolidationReceiptService(self.repository).valid_for(object_id) is None:
            failures.append("Trusted object has no current Receipt v2")
        if metadata.get("high_risk_drift"):
            failures.append("Trusted object has high-risk drift")
        if metadata.get("unresolved_contradictions"):
            failures.append("Trusted object has unresolved contradictions")
        try:
            if any(item.get("relation_type") == "contradicts" for item in self.repository.related(object_id)):
                failures.append("Trusted object has an incoming or outgoing contradiction relation")
        except Exception as exc:
            failures.append(f"relation index unavailable: {exc}")
        if failures:
            raise ValidationError("canonical gate failed: " + "; ".join(failures))

    def promote_trusted(
        self, object_id: str, *, automatic: bool = True, reason: str = "",
        rebuild_index: bool = True,
    ) -> dict[str, Any]:
        path, metadata, body = self.repository.find_document(object_id)
        evaluation = self.evaluate(object_id)
        if automatic and not evaluation.eligible:
            return {"promoted": False, "evaluation": evaluation.as_dict()}
        if not automatic and not reason.strip():
            raise ValidationError("manual trusted promotion requires a reason")
        if metadata.get("user_locked") and automatic:
            raise ValidationError("user locked object cannot be automatically promoted")
        timestamp = now_iso()
        history = list(metadata.get("promotion_history", []))
        promotion_id = "promotion_" + hashlib.sha256(f"{object_id}:trusted:{timestamp}".encode()).hexdigest()[:24]
        history.append({
            "promotion_id": promotion_id, "object_id": object_id,
            "from_status": metadata.get("status"), "to_status": "trusted",
            "policy_version": POLICY_VERSION, "promotion_mode": "automatic" if automatic else "user_approved",
            "reasons": evaluation.reasons + ([reason.strip()] if reason.strip() else []),
            "failed_conditions": evaluation.failed_conditions, "supporting_sources": evaluation.supporting_sources,
            "contradictions": evaluation.contradictions, "promoted_at": timestamp,
            "promoted_by": "promotion-policy" if automatic else "user",
        })
        epistemic_status = metadata.get("epistemic_status") or default_epistemic_status(str(metadata.get("type")), "trusted")
        if metadata.get("type") == "claim" and epistemic_status in {"unknown", "provisional"}:
            epistemic_status = "supported"
        metadata.update({
            "status": "trusted", "memory_tier": "trusted", "updated_at": timestamp,
            "epistemic_status": epistemic_status,
            "updated_by": "promotion-policy", "trust_score": evaluation.trust_score,
            "trust_reasons": evaluation.reasons, "promotion_history": history,
            "needs_policy_requalification": False,
            "trust_policy_version": POLICY_VERSION,
            "last_policy_qualified_at": timestamp,
            "qualification_scope": qualification_scope(str(metadata.get("type"))),
        })
        # Stage the promotion, verify it under its *new* bytes, and roll back
        # atomically if Receipt v2 cannot be completed.
        before = path.read_bytes()
        staged_text = render_document(metadata, body)
        event = {"event": "promoted-trusted", "promotion_id": promotion_id, "object_id": object_id}
        journal = self.recovery.prepare(
            promotion_id, path, before, staged_text,
            operation="trusted_promotion", event=event,
        )
        try:
            atomic_write_text(path, staged_text)
            self.recovery.checkpoint(journal, "staged")
            self.repository.rebuild_index()
            from .consolidation import ConsolidationReceiptService
            receipt = ConsolidationReceiptService(self.repository).consolidate(
                object_id, result="promotion_candidate", change_summary="Trusted promotion requalified under Receipt v2",
                rebuild_index=False,
            )
            if not ConsolidationReceiptService.complete(receipt):
                raise ValidationError("Trusted promotion receipt v2 did not complete")
            self.recovery.checkpoint(journal, "receipt_completed", receipt["consolidation_id"])
        except Exception:
            path.write_bytes(before)
            self.repository.rebuild_index()
            journal.unlink(missing_ok=True)
            raise
        if rebuild_index:
            self.repository.rebuild_index()
        self.repository.append_event("memory-events", {**event, "recovery_operation_id": promotion_id})
        self.recovery.checkpoint(journal, "event_logged")
        self.recovery.checkpoint(journal, "finalized")
        journal.unlink(missing_ok=True)
        return {"promoted": True, "promotion_id": promotion_id, "receipt_id": receipt["consolidation_id"], "evaluation": evaluation.as_dict(), "path": self.repository.rel(path)}

    def recommend_canonical(self, object_id: str, why_important: str = "") -> dict[str, Any]:
        path, metadata, object_body = self.repository.find_document(object_id)
        if metadata.get("status") != "trusted":
            raise ValidationError("canonical candidates must first be trusted")
        self._assert_canonical_gate(object_id, metadata)
        stable = f"canonical:{object_id}:{hashlib.sha256(object_body.encode('utf-8')).hexdigest()}"
        promotion_id = "promotion_" + hashlib.sha256(stable.encode()).hexdigest()[:24]
        card_path = self.directory / f"promotion-{promotion_id}.md"
        if not card_path.exists():
            timestamp = now_iso()
            card = {
                "id": promotion_id, "type": "promotion", "status": "pending", "title": f"Canonical: {metadata['title']}",
                "created_at": timestamp, "updated_at": timestamp, "aliases": [], "tags": ["canonical-candidate"],
                "domains": list(metadata.get("domains", [])), "confidence": "unknown",
                "source_ids": list(metadata.get("source_ids", [])), "relations": [],
                "object_id": object_id, "from_status": "trusted", "to_status": "canonical",
                "policy_version": POLICY_VERSION, "why_important": why_important.strip(),
            }
            body = (
                f"# Canonical Promotion Card\n\n- 对象：`{object_id}`\n- 当前状态：trusted\n"
                f"- 建议晋升为：canonical\n- 为什么重要：{why_important or '待用户判断'}\n"
                f"- 证据：{', '.join(metadata.get('source_ids', []))}\n"
                f"- 可能改变什么：进入少量、稳定、由用户控制的 canonical 层\n"
                f"- 仍有不确定性：{metadata.get('uncertainty', '见对象正文')}\n"
            )
            atomic_write_text(card_path, render_document(card, body))
        return {"promotion_id": promotion_id, "path": self.repository.rel(card_path), "object_id": object_id}

    def approve_canonical(self, promotion_id: str, *, lock: bool = False) -> dict[str, Any]:
        card_path, card, card_body = self.repository.find_document(promotion_id)
        if card.get("type") != "promotion" or card.get("status") not in {"pending", "deferred"}:
            raise ValidationError("promotion card is not reviewable")
        memory_path, metadata, body = self.repository.find_document(str(card["object_id"]))
        if metadata.get("status") != "trusted":
            raise ValidationError("promotion target is no longer trusted")
        self._assert_canonical_gate(str(card["object_id"]), metadata)
        object_type = str(metadata["type"])
        target_dir = CANONICAL_DIRECTORIES.get(object_type)
        if not target_dir:
            raise ValidationError(f"object type cannot become canonical: {object_type}")
        target = self.repository.root / target_dir / memory_path.name
        if target.exists():
            raise ValidationError("canonical target already exists")
        before = memory_path.read_bytes()
        card_before = card_path.read_bytes()
        timestamp = now_iso()
        approval_event_id = "canonical_approval_" + hashlib.sha256(
            f"{promotion_id}:{timestamp}".encode("utf-8")
        ).hexdigest()[:24]
        metadata.update({
            "status": "canonical", "memory_tier": "canonical", "updated_at": timestamp,
            "epistemic_status": infer_epistemic_status(metadata, "canonical"),
            "updated_by": "user", "user_locked": lock, "canonical_promotion_id": promotion_id,
            "user_approved": True, "approval_event_id": approval_event_id,
        })
        card["status"] = "approved"
        card["updated_at"] = timestamp
        card["approved_at"] = timestamp
        event = {
            "event": "promoted-canonical", "promotion_id": promotion_id,
            "approval_event_id": approval_event_id, "object_id": metadata["id"], "locked": lock,
        }
        canonical_text = render_document(metadata, body)
        card_after_text = render_document(card, card_body)
        journal = self.canonical_recovery.prepare(
            promotion_id, memory_path=memory_path, target_path=target, card_path=card_path,
            memory_before=before, card_before=card_before, canonical_text=canonical_text,
            card_after_text=card_after_text, event=event,
        )
        try:
            atomic_write_text(target, canonical_text)
            self.canonical_recovery.checkpoint(journal, "canonical_written")
            self._fail_if_requested("canonical_written")
            # The SQLite index enforces one stable object id. Keep the original
            # bytes in the transaction buffer, then remove the Trusted path only
            # for the final Canonical indexing/Receipt boundary.
            memory_path.unlink()
            self.canonical_recovery.checkpoint(journal, "trusted_removed")
            self._fail_if_requested("trusted_removed")
            self.repository.rebuild_index()
            from .consolidation import ConsolidationReceiptService

            receipt = ConsolidationReceiptService(self.repository).consolidate(
                str(metadata["id"]), result="canonical_approved",
                change_summary="User approved this exact final Canonical version",
                rebuild_index=False,
            )
            if not ConsolidationReceiptService.complete(receipt) or ConsolidationReceiptService(self.repository).valid_for(str(metadata["id"])) is None:
                raise ValidationError("Canonical final Receipt v2 did not complete")
            self.canonical_recovery.checkpoint(journal, "receipt_completed", receipt["consolidation_id"])
            self._fail_if_requested("canonical_receipt_completed")
            atomic_write_text(card_path, card_after_text)
            self.canonical_recovery.checkpoint(journal, "card_updated")
            self._fail_if_requested("canonical_card_updated")
            self.repository.rebuild_index()
        except Exception:
            # Do not guess after a final Receipt has reached disk.  Recovery uses
            # that Receipt to choose the only safe direction, and otherwise
            # restores the exact pre-image.
            recovered = self.canonical_recovery.recover_all()
            if recovered["blocked"]:
                raise ValidationError(f"canonical promotion recovery blocked: {recovered['blocked']}")
            from .consolidation import ConsolidationReceiptService

            recovered_receipt = ConsolidationReceiptService(self.repository).valid_for(str(metadata["id"]))
            if (
                target.exists() and not memory_path.exists() and recovered_receipt is not None
                and recovered_receipt.get("result") == "canonical_approved"
            ):
                return {
                    "promotion_id": promotion_id, "approval_event_id": approval_event_id,
                    "object_id": metadata["id"], "path": self.repository.rel(target), "locked": lock,
                    "receipt_id": recovered_receipt["consolidation_id"],
                    "recovered_after_interruption": True,
                }
            raise
        event["receipt_id"] = receipt["consolidation_id"]
        self.repository.append_event("memory-events", {**event, "recovery_operation_id": promotion_id})
        self.canonical_recovery.checkpoint(journal, "event_logged")
        self.canonical_recovery.checkpoint(journal, "finalized")
        journal.unlink(missing_ok=True)
        return {
            "promotion_id": promotion_id, "approval_event_id": approval_event_id,
            "object_id": metadata["id"], "path": self.repository.rel(target), "locked": lock,
            "receipt_id": receipt["consolidation_id"],
        }

    def decide(self, promotion_id: str, decision: str, reason: str) -> dict[str, Any]:
        if decision not in {"rejected", "deferred"} or not reason.strip():
            raise ValidationError("promotion rejection or deferral requires a reason")
        card_path, card, body = self.repository.find_document(promotion_id)
        if card.get("type") != "promotion" or card.get("status") not in {"pending", "deferred"}:
            raise ValidationError("promotion card is not reviewable")
        card["status"] = decision
        card["decision_reason"] = reason.strip()
        card["updated_at"] = now_iso()
        atomic_write_text(card_path, render_document(card, body))
        self.repository.append_event("memory-events", {
            "event": f"promotion-{decision}", "promotion_id": promotion_id,
            "object_id": card.get("object_id"), "reason": reason.strip(),
        })
        return {"promotion_id": promotion_id, "status": decision}

    def demote_working(self, object_id: str, reason: str) -> dict[str, Any]:
        if not reason.strip():
            raise ValidationError("demotion requires a reason")
        path, metadata, body = self.repository.find_document(object_id)
        if not self.repository.rel(path).startswith("vault/memory/") or metadata.get("status") != "trusted":
            raise ValidationError("only trusted memory can be demoted to working")
        timestamp = now_iso()
        before = path.read_bytes()
        before_sha = sha256_bytes(before)
        version_path = self.repository.root / "vault" / "archive" / "versions" / object_id / f"{before_sha}.md"
        self.repository.immutable_write(version_path, before)
        from_epistemic = infer_epistemic_status(metadata, "trusted")
        demotion_id = "demotion_" + hashlib.sha256(f"{object_id}:{before_sha}:{reason.strip()}".encode()).hexdigest()[:24]
        history = list(metadata.get("promotion_history", []))
        history.append({
            "promotion_id": demotion_id,
            "object_id": object_id, "from_status": "trusted", "to_status": "working",
            "promotion_mode": "user_approved", "policy_version": POLICY_VERSION,
            "reasons": [reason.strip()], "promoted_at": timestamp, "promoted_by": "user",
        })
        metadata.update({
            "status": "working", "memory_tier": "working", "updated_at": timestamp,
            "epistemic_status": from_epistemic,
            "updated_by": "user", "trust_score": 0, "trust_reasons": [],
            "promotion_history": history,
        })
        atomic_write_text(path, render_document(metadata, body))
        event = {
            "id": demotion_id, "type": "demotion_event", "status": "recorded",
            "title": f"Demotion: {metadata.get('title', object_id)}",
            "created_at": timestamp, "updated_at": timestamp,
            "demotion_id": demotion_id, "object_id": object_id,
            "from_tier": "trusted", "to_tier": "working",
            "from_epistemic_status": from_epistemic,
            "to_epistemic_status": from_epistemic,
            "trigger_source_ids": list(metadata.get("source_ids", [])),
            "reason": reason.strip(), "previous_version": self.repository.rel(version_path),
            "new_revision": self.repository.rel(path), "created_by": "user",
            "exception_id": None,
        }
        event_path = self.repository.root / "vault" / "receipts" / "demotions" / f"demotion-{demotion_id}.md"
        self.repository.immutable_write(event_path, render_document(event, "# Demotion Event\n").encode("utf-8"))
        self.repository.rebuild_index()
        self.repository.append_event("memory-events", {
            "event": "demoted-working", "object_id": object_id, "reason": reason.strip(),
        })
        return {
            "demotion_id": demotion_id, "object_id": object_id, "status": "working",
            "memory_tier": "working", "epistemic_status": from_epistemic,
            "path": self.repository.rel(path), "event_path": self.repository.rel(event_path),
            "previous_version": self.repository.rel(version_path),
        }

    def list_cards(self, statuses: set[str] | None = None) -> list[dict[str, Any]]:
        cards: list[dict[str, Any]] = []
        if not self.directory.exists():
            return cards
        for path in sorted(self.directory.glob("promotion-*.md")):
            metadata, _ = read_document(path)
            if statuses and metadata.get("status") not in statuses:
                continue
            cards.append({**metadata, "path": self.repository.rel(path)})
        return cards

    def rollback(self, change_id: str, reason: str) -> dict[str, Any]:
        """Rollback only the latest trusted promotion; canonical rollback stays explicit/manual."""
        if not reason.strip():
            raise ValidationError("rollback requires a reason")
        for path in self.repository.memory_documents():
            metadata, _ = read_document(path)
            history = list(metadata.get("promotion_history", []))
            if not history or history[-1].get("promotion_id") != change_id:
                continue
            if metadata.get("status") != "trusted" or history[-1].get("to_status") != "trusted":
                raise ValidationError("only the latest trusted promotion can be rolled back safely")
            result = self.demote_working(str(metadata["id"]), f"rollback {change_id}: {reason.strip()}")
            result["rolled_back_change_id"] = change_id
            return result
        raise ValidationError("change is not the latest reversible trusted promotion")

    def explain(self, object_id: str) -> dict[str, Any]:
        _, metadata, _ = self.repository.find_document(object_id)
        evaluation = self.evaluate(object_id) if metadata.get("status") == "working" else None
        return {
            "object_id": object_id, "status": metadata.get("status"), "trust_score": metadata.get("trust_score"),
            "trust_reasons": metadata.get("trust_reasons", []), "promotion_history": metadata.get("promotion_history", []),
            "current_evaluation": evaluation.as_dict() if evaluation else None,
        }
