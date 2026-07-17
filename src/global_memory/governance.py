from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .memory import ExceptionService
from .proposals import CANONICAL_DIRECTORIES
from .repository import Repository, now_iso


POLICY_VERSION = "trusted-promotion-v1"


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
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "promotions"
        self.exceptions = ExceptionService(repository)

    def evaluate(self, object_id: str) -> PromotionEvaluation:
        path, metadata, body = self.repository.find_document(object_id)
        if not self.repository.rel(path).startswith("vault/memory/"):
            raise ValidationError("trusted promotion only evaluates working memory")
        reasons: list[str] = []
        failed: list[str] = []
        contradictions = [
            str(relation.get("target_id")) for relation in metadata.get("relations", [])
            if relation.get("type") == "contradicts" and relation.get("status") not in {"rejected", "superseded"}
        ]
        object_type = str(metadata.get("type"))
        if metadata.get("user_locked") and metadata.get("status") != "trusted":
            failed.append("user_locked object cannot be automatically changed")
        if int(metadata.get("consolidation_count", 0)) < 1:
            failed.append("requires at least one consolidation review")
        else:
            reasons.append("completed consolidation review")
        if contradictions:
            failed.append("unresolved direct contradiction")
        if object_type == "claim":
            checks = {
                "atomic claim": metadata.get("atomicity_status") == "atomic",
                "full evidence coverage": metadata.get("evidence_coverage") == "full",
                "full evidence entailment": metadata.get("evidence_entailment") == "full",
                "good extraction": metadata.get("extraction_quality") == "good",
                "primary or official authority": metadata.get("epistemic_source_authority") in {"primary", "official", "peer_reviewed"},
                "explicit applicability": bool(metadata.get("applicability")),
                "supporting evidence exists": any(item.get("stance") == "supports" for item in metadata.get("evidence", [])),
            }
            for label, passed in checks.items():
                (reasons if passed else failed).append(label)
        elif object_type == "concept":
            reuse = int(metadata.get("reuse_count", 0))
            if reuse >= 2 or len(set(metadata.get("source_ids", []))) >= 2:
                reasons.append("concept reused by independent material")
            else:
                failed.append("concept requires two independent uses or sources")
            if metadata.get("duplicate_of"):
                failed.append("unresolved duplicate concept")
        elif object_type == "analogy":
            if metadata.get("shared_structure") and metadata.get("where_it_breaks"):
                reasons.append("analogy records shared structure and break boundary")
            else:
                failed.append("analogy requires shared_structure and where_it_breaks")
        elif object_type in {"question", "tension", "hypothesis", "anomaly", "intuition"}:
            if metadata.get("source_ids"):
                reasons.append(f"{object_type} is durable and source-linked")
            else:
                failed.append(f"{object_type} has no source")
        elif object_type == "synthesis":
            if len(set(metadata.get("source_ids", []))) >= 2 and metadata.get("unresolved_tensions") is not None:
                reasons.append("multi-source synthesis preserves unresolved tensions")
            else:
                failed.append("synthesis requires multiple sources and unresolved_tensions")
        else:
            failed.append(f"automatic trusted policy is not defined for {object_type}")
        score = max(0, min(100, 50 + 8 * len(reasons) - 12 * len(failed)))
        return PromotionEvaluation(
            object_id, not failed, score, reasons, failed,
            [str(item) for item in metadata.get("source_ids", [])], contradictions,
        )

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
        metadata.update({
            "status": "trusted", "memory_tier": "trusted", "updated_at": timestamp,
            "updated_by": "promotion-policy", "trust_score": evaluation.trust_score,
            "trust_reasons": evaluation.reasons, "promotion_history": history,
        })
        atomic_write_text(path, render_document(metadata, body))
        if rebuild_index:
            self.repository.rebuild_index()
        self.repository.append_event("memory-events", {"event": "promoted-trusted", "promotion_id": promotion_id, "object_id": object_id})
        return {"promoted": True, "promotion_id": promotion_id, "evaluation": evaluation.as_dict(), "path": self.repository.rel(path)}

    def recommend_canonical(self, object_id: str, why_important: str = "") -> dict[str, Any]:
        path, metadata, object_body = self.repository.find_document(object_id)
        if metadata.get("status") != "trusted":
            raise ValidationError("canonical candidates must first be trusted")
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
        metadata.update({
            "status": "canonical", "memory_tier": "canonical", "updated_at": timestamp,
            "updated_by": "user", "user_locked": lock, "canonical_promotion_id": promotion_id,
        })
        card["status"] = "approved"
        card["updated_at"] = timestamp
        card["approved_at"] = timestamp
        try:
            atomic_write_text(target, render_document(metadata, body))
            atomic_write_text(card_path, render_document(card, card_body))
            memory_path.unlink()
            self.repository.rebuild_index()
        except Exception:
            target.unlink(missing_ok=True)
            memory_path.write_bytes(before)
            card_path.write_bytes(card_before)
            self.repository.rebuild_index()
            raise
        self.repository.append_event("memory-events", {"event": "promoted-canonical", "promotion_id": promotion_id, "object_id": metadata["id"], "locked": lock})
        return {"promotion_id": promotion_id, "object_id": metadata["id"], "path": self.repository.rel(target), "locked": lock}

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
        history = list(metadata.get("promotion_history", []))
        history.append({
            "promotion_id": "demotion_" + hashlib.sha256(f"{object_id}:{timestamp}".encode()).hexdigest()[:24],
            "object_id": object_id, "from_status": "trusted", "to_status": "working",
            "promotion_mode": "user_approved", "policy_version": POLICY_VERSION,
            "reasons": [reason.strip()], "promoted_at": timestamp, "promoted_by": "user",
        })
        metadata.update({
            "status": "working", "memory_tier": "working", "updated_at": timestamp,
            "updated_by": "user", "trust_score": 0, "trust_reasons": [],
            "promotion_history": history,
        })
        atomic_write_text(path, render_document(metadata, body))
        self.repository.rebuild_index()
        self.repository.append_event("memory-events", {
            "event": "demoted-working", "object_id": object_id, "reason": reason.strip(),
        })
        return {"object_id": object_id, "status": "working", "path": self.repository.rel(path)}

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
