from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any

from .errors import ValidationError
from .epistemics import infer_epistemic_status, infer_tier, truth_layer
from .governance import POLICY_VERSION
from .extraction import ExtractionService
from .markdown import read_document
from .repository import Repository, SearchResult, sha256_bytes
from .quality import SourceQualityService


MIN_TOKEN_BUDGET = 128
MAX_TOKEN_BUDGET = 20_000
SEARCH_LIMIT = 50
PROFILE_PRIORITIES = {
    "execution": {
        "project": 100, "goal": 95, "architecture": 90, "decision": 88,
        "failure": 86, "experiment": 82, "opportunity": 75, "question": 70,
        "tension": 68, "concept": 60, "claim": 55, "source": 30, "annotation": 20,
    },
    "research": {
        "concept": 100, "claim": 95, "synthesis": 90, "question": 86,
        "tension": 84, "hypothesis": 78, "work": 72, "annotation": 68, "source": 60,
    },
    "exploration": {
        "intuition": 100, "tension": 95, "analogy": 92, "anomaly": 90,
        "hypothesis": 88, "question": 82, "annotation": 80, "concept": 65, "claim": 45,
    },
}


@dataclass(frozen=True)
class ContextPack:
    query: str
    token_budget: int
    estimated_tokens: int
    items: list[dict[str, Any]]
    omitted: list[dict[str, Any]]
    profiles: list[str]
    filters: dict[str, Any]
    route_trace: dict[str, Any]

    def as_dict(self) -> dict[str, Any]:
        return {
            "context_pack_version": 1,
            "query": self.query,
            "token_budget": self.token_budget,
            "estimated_tokens": self.estimated_tokens,
            "items": self.items,
            "omitted": self.omitted,
            "profiles": self.profiles,
            "filters": self.filters,
            "route_trace": self.route_trace,
            "truncation_report": {
                "selected_items": len(self.items),
                "omitted_items": len(self.omitted),
                "budget_exhausted": any("budget" in str(item.get("reason", "")) for item in self.omitted),
            },
            "selection_policy": {
                "kind": "profiled-read-only-query-context-v2",
                "notes": [
                    "Context Pack 是临时读取视图，不写入 Markdown、索引或日志。",
                    "它不替代检索，不把命中或摘录升级为事实，也不改变 canonical 状态。",
                    "provisional 表示已通过自动门禁但尚未人工确认；调用方必须保留该信任标记。",
                    "token 为保守估算；每项保留路径、哈希、来源和入选理由，供调用方回溯。",
                ],
            },
        }

    def as_markdown(self) -> str:
        data = self.as_dict()
        lines = [
            "---\ncontext_pack_version: 1\ntruth_layer: derived_read_only\n---\n\n",
            "# Global Memory Context Pack\n\n",
            f"- Query: {self.query}\n- Profiles: {', '.join(self.profiles)}\n",
            f"- Token budget: {self.token_budget}\n- Estimated tokens: {self.estimated_tokens}\n\n",
        ]
        lines.append("## Route trace\n\n```json\n" + json.dumps(self.route_trace, ensure_ascii=False, indent=2) + "\n```\n\n")
        for item in self.items:
            lines.append(f"## {item.get('title', item.get('id'))}\n\n")
            lines.append(f"- ID: `{item.get('id')}`\n- Type/status: `{item.get('type')}` / `{item.get('knowledge_status')}`\n")
            lines.append(
                f"- Memory tier: `{item.get('memory_tier')}`\n"
                f"- Epistemic status: `{item.get('epistemic_status')}`\n"
                f"- Truth layer: `{item.get('truth_layer')}`\n- Path: `{item.get('path')}`\n"
            )
            lines.append(f"- Sources: {', '.join(item.get('source_ids', [])) or 'none'}\n")
            if item.get("truth_layer") == "user_annotation":
                lines.append(f"- User authored: `{str(item.get('user_authored', False)).lower()}`\n")
                annotation = item.get("annotation") or {}
                lines.append(f"- Annotation kind: `{annotation.get('annotation_kind')}`\n")
                lines.append(f"- Targets: {', '.join(annotation.get('target_ids', [])) or 'none'}\n")
                lines.append(f"- Why saved: {annotation.get('why_saved') or 'none'}\n")
                lines.append(f"- Surprised by: {annotation.get('what_surprised_me') or 'none'}\n")
                lines.append(f"- Possible connections: {', '.join(annotation.get('possible_connections', [])) or 'none'}\n")
                lines.append(f"- Salience: `{annotation.get('personal_salience')}`\n")
                lines.append("- Epistemic note: user intent/value signal, not factual claim\n")
            if item.get("evidence"):
                lines.append(f"- Evidence: `{item['evidence']}`\n")
            if item.get("verification"):
                lines.append(f"- Verification: `{item['verification']}`\n")
            if item.get("activation"):
                lines.append(f"- Activation (usage only, not trust): `{item['activation']}`\n")
            lines.append(f"- Selection: {item.get('selection_reason', item.get('match_reason', 'ranked match'))}\n\n")
            lines.append(str(item.get("content", item.get("snippet", ""))).strip() + "\n\n")
        report = data["truncation_report"]
        lines.append("## Truncation report\n\n")
        lines.append(f"- Selected: {report['selected_items']}\n- Omitted: {report['omitted_items']}\n- Budget exhausted: {str(report['budget_exhausted']).lower()}\n")
        return "".join(lines)


class ContextPackService:
    """Build a small, deterministic, provenance-preserving read-only view."""

    def __init__(self, repository: Repository):
        self.repository = repository

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """Conservative mixed Chinese/Latin token estimate, without a model tokenizer."""
        cjk = len(re.findall(r"[\u3400-\u9fff]", text))
        non_cjk = re.sub(r"[\u3400-\u9fff]", " ", text)
        latin_words = len(re.findall(r"\S+", non_cjk))
        return max(1, cjk + (latin_words * 2 + 2) // 3)

    @staticmethod
    def _clip_to_budget(text: str, token_budget: int) -> str:
        if ContextPackService._estimate_tokens(text) <= token_budget:
            return text
        if token_budget <= 1:
            return "…"
        clipped: list[str] = []
        cjk = 0
        latin_words = 0
        in_latin_word = False
        for character in text:
            next_cjk = cjk
            next_latin_words = latin_words
            next_in_latin_word = in_latin_word
            if re.match(r"[\u3400-\u9fff]", character):
                next_cjk += 1
                next_in_latin_word = False
            elif character.isspace():
                next_in_latin_word = False
            elif not next_in_latin_word:
                next_latin_words += 1
                next_in_latin_word = True
            estimated = next_cjk + (next_latin_words * 2 + 2) // 3
            # Reserve one token for the visible truncation marker.
            if estimated + 1 > token_budget:
                break
            clipped.append(character)
            cjk, latin_words, in_latin_word = next_cjk, next_latin_words, next_in_latin_word
        return ("".join(clipped).rstrip() + "…") if clipped else "…"

    def _content(self, metadata: dict[str, Any], body: str) -> str:
        if metadata.get("type") != "source":
            return body.strip()
        try:
            _, extraction, extracted = ExtractionService(self.repository).latest_for_source(str(metadata["id"]))
            if extraction.get("status") == "ready" and extracted.strip():
                return extracted.strip()
        except Exception:
            pass
        raw_path = self.repository.resolve_inside(str(metadata["raw_content_path"]))
        try:
            return raw_path.read_text(encoding="utf-8").strip()
        except UnicodeDecodeError:
            return body.strip()

    @staticmethod
    def _evidence_view(metadata: dict[str, Any]) -> list[dict[str, Any]]:
        view: list[dict[str, Any]] = []
        for item in metadata.get("evidence", []):
            if not isinstance(item, dict):
                continue
            text = item.get("original_text") or item.get("interpretation") or item.get("excerpt") or ""
            view.append({
                "evidence_id": item.get("evidence_id"),
                "evidence_kind": item.get("evidence_kind", "legacy_excerpt"),
                "source_id": item.get("source_id"), "stance": item.get("stance"),
                "page": item.get("page"), "section": item.get("section"),
                "text": str(text)[:240], "verification_status": item.get("verification_status"),
                "quote_verification": metadata.get("quote_verification"),
                "extraction_quality": metadata.get("extraction_quality"),
                "evidence_entailment": metadata.get("evidence_entailment"),
            })
        return view

    def _source_authority(self, metadata: dict[str, Any]) -> str:
        if metadata.get("type") != "source":
            explicit = metadata.get("source_authority") or metadata.get("epistemic_source_authority")
            if explicit:
                return str(explicit)
            authorities: set[str] = set()
            for source_id in metadata.get("source_ids", []):
                try:
                    assessment = SourceQualityService(self.repository).load(str(source_id))
                    if assessment is None:
                        assessment = SourceQualityService(self.repository).assess(str(source_id), persist=False)
                    authorities.add(assessment.source_authority)
                except Exception:
                    continue
            if len(authorities) == 1:
                return authorities.pop()
            if authorities:
                return "mixed:" + ",".join(sorted(authorities))
            return "unknown"
        try:
            assessment = SourceQualityService(self.repository).load(str(metadata["id"]))
            if assessment is None:
                assessment = SourceQualityService(self.repository).assess(str(metadata["id"]), persist=False)
            return assessment.source_authority
        except Exception:
            return "unknown"

    def _proposal_candidates(
        self, query: str, *, profiles: list[str], allowed_types: set[str],
        statuses: set[str] | None, domains: set[str] | None,
    ) -> list[tuple[int, int, dict[str, Any]]]:
        """Return bounded bundle candidates only when proposal visibility is explicit."""
        terms = [term.casefold() for term in re.findall(r"[\w\u3400-\u9fff-]+", query) if term]
        if not terms:
            return []
        ranked: list[tuple[int, int, dict[str, Any]]] = []
        seen: set[str] = set()
        proposal_rank = 0
        for proposal_path in sorted(self.repository.proposal_documents()):
            proposal, _ = read_document(proposal_path)
            if proposal.get("status") not in {"pending", "deferred"}:
                continue
            if statuses and proposal.get("status") not in statuses and "proposal" not in statuses:
                continue
            for bundle_item in proposal.get("bundle_items", []):
                if not isinstance(bundle_item, dict) or bundle_item.get("decision") not in {"pending", "deferred"}:
                    continue
                candidate_path_value = bundle_item.get("candidate_path")
                if not candidate_path_value:
                    continue
                candidate_path = self.repository.resolve_inside(str(candidate_path_value))
                if not candidate_path.exists():
                    continue
                candidate, body = read_document(candidate_path)
                candidate_id = str(candidate.get("id", ""))
                object_type = str(candidate.get("type", bundle_item.get("object_type", "")))
                if not candidate_id or candidate_id in seen or object_type not in allowed_types:
                    continue
                candidate_domains = {str(item) for item in candidate.get("domains", [])}
                if domains and not (domains & candidate_domains):
                    continue
                haystack = " ".join([
                    str(candidate.get("title", "")), body,
                    *map(str, candidate.get("aliases", [])),
                    *map(str, candidate.get("tags", [])),
                    *map(str, candidate.get("domains", [])),
                ]).casefold()
                matched_terms = [term for term in terms if term in haystack]
                if not matched_terms:
                    continue
                seen.add(candidate_id)
                proposal_rank += 1
                source_ids = [str(item) for item in candidate.get("source_ids", proposal.get("source_ids", []))]
                item = {
                    "id": candidate_id,
                    "type": object_type,
                    "knowledge_status": "proposal",
                    "truth_layer": "proposal",
                    "memory_tier": "working",
                    "epistemic_status": candidate.get("epistemic_status", "provisional"),
                    "confidence": candidate.get("confidence", "unknown"),
                    "evidence_coverage": candidate.get("evidence_coverage"),
                    "evidence_entailment": candidate.get("evidence_entailment", "unknown"),
                    "unresolved_contradictions": candidate.get("unresolved_contradictions", []),
                    "last_consolidated_at": candidate.get("last_consolidated_at"),
                    "proposal_id": str(proposal["id"]),
                    "title": str(candidate.get("title", candidate_id)),
                    "path": self.repository.rel(candidate_path),
                    "document_sha256": sha256_bytes(candidate_path.read_bytes()),
                    "source_ids": source_ids,
                    "user_authored": metadata.get("user_authored") if object_type == "annotation" else None,
                    "annotation": ({
                        "annotation_kind": metadata.get("annotation_kind"),
                        "why_saved": metadata.get("why_saved"),
                        "what_surprised_me": metadata.get("what_surprised_me"),
                        "possible_connections": metadata.get("possible_connections", []),
                        "research_projects": metadata.get("research_projects", []),
                        "domains": metadata.get("domains", []),
                        "personal_salience": metadata.get("personal_salience"),
                        "feedback_label": metadata.get("feedback_label"),
                        "note": metadata.get("note"),
                    } if object_type == "annotation" else None),
                    "raw_content_sha256": None,
                    "source_version": None,
                    "source_authority": self._source_authority(candidate),
                    "verification": {
                        "quote_verification": candidate.get("quote_verification", "not_applicable"),
                        "extraction_quality": candidate.get("extraction_quality", "unknown"),
                        "evidence_entailment": candidate.get("evidence_entailment", "unknown"),
                        "claim_confidence": candidate.get("claim_confidence", candidate.get("confidence", "unknown")),
                        "publication_gate": candidate.get("publication_gate", "needs_review"),
                        "atomicity_status": candidate.get("atomicity_status"),
                        "evidence_coverage": candidate.get("evidence_coverage"),
                    },
                    "evidence": self._evidence_view(candidate) if object_type == "claim" else [],
                    "match_reason": f"proposal candidate text: {', '.join(matched_terms[:3])}",
                    "content": body.strip(),
                    "selection_reason": (
                        f"显式 include_proposals；候选类型={object_type}；proposal={proposal['id']}；"
                        f"命中={','.join(matched_terms[:3])}；未提升为 canonical。"
                    ),
                }
                priority = self._type_priority(object_type, profiles, "pending")
                # A typed knowledge candidate is more useful than the enclosing
                # proposal document or a duplicate source summary.
                ranked.append((-(1_200 + priority), proposal_rank, item))
                if len(ranked) >= SEARCH_LIMIT:
                    return ranked
        return ranked

    @staticmethod
    def _type_priority(object_type: str, profiles: list[str], status: str) -> int:
        priority = max(PROFILE_PRIORITIES[profile].get(object_type, 0) for profile in profiles)
        if status in {"canonical", "confirmed"}:
            priority += 12
        elif status == "trusted":
            priority += 8
        elif status in {"working", "provisional"}:
            priority += 2
        elif status in {"contested", "pending", "deferred"}:
            priority -= 2
        if object_type in {"decision", "failure", "goal", "project"}:
            priority += 8
        return priority

    def _latest_source_ids(self) -> set[str]:
        """Return the current source record for every append-only source family."""
        latest: dict[str, tuple[tuple[int, str, str], str]] = {}
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            family = str(metadata.get("canonical_locator", metadata["id"]))
            version_key = (
                int(metadata.get("version_number", 1)),
                str(metadata.get("captured_at", "")),
                str(metadata["id"]),
            )
            existing = latest.get(family)
            if existing is None or version_key > existing[0]:
                latest[family] = (version_key, str(metadata["id"]))
        return {item[1] for item in latest.values()}

    def _archived_only_source_ids(self) -> set[str]:
        """Return sources referenced by archived canonical knowledge and no active canonical."""
        archived: set[str] = set()
        active: set[str] = set()
        for path in [*self.repository.canonical_documents(), *self.repository.archive_documents()]:
            metadata, _ = read_document(path)
            destination = archived if metadata.get("status") == "archived" else active
            destination.update(str(item) for item in metadata.get("source_ids", []))
        return archived - active

    def build(
        self, query: str, token_budget: int = 1_200, *, profiles: list[str] | None = None,
        project: str | None = None, domains: set[str] | None = None,
        object_types: set[str] | None = None, statuses: set[str] | None = None,
        updated_since: str | None = None, source_kinds: set[str] | None = None,
        include_proposals: bool = False, relation_depth: int = 1,
        strict_execution: bool = False,
    ) -> ContextPack:
        query = query.strip()
        if not query:
            raise ValidationError("Context Pack query 不能为空")
        if not MIN_TOKEN_BUDGET <= token_budget <= MAX_TOKEN_BUDGET:
            raise ValidationError(
                f"Context Pack token budget 必须介于 {MIN_TOKEN_BUDGET} 和 {MAX_TOKEN_BUDGET}"
            )
        profiles = profiles or ["research"]
        invalid_profiles = set(profiles) - PROFILE_PRIORITIES.keys()
        if invalid_profiles:
            raise ValidationError(f"未知 Context Pack profile: {', '.join(sorted(invalid_profiles))}")
        from .research import ResearchRouterService
        route = ResearchRouterService(self.repository).plan(
            query, project=project, domains=domains, relation_depth=min(relation_depth, 2)
        )
        effective_project = project or route.selected_project
        if domains is None and route.selected_domains:
            domains = set(route.selected_domains)
        allowed_types = set().union(*(PROFILE_PRIORITIES[profile].keys() for profile in profiles))
        if object_types:
            allowed_types &= object_types
        if include_proposals:
            allowed_types.add("proposal")
        filter_report = {
            "project": effective_project, "domains": sorted(domains or []),
            "object_types": sorted(object_types or []), "statuses": sorted(statuses or []),
            "updated_since": updated_since, "source_kinds": sorted(source_kinds or []),
            "include_proposals": include_proposals, "relation_depth": relation_depth,
            "strict_execution": strict_execution,
        }
        from .consolidation import ConsolidationReceiptService
        receipt_service = ConsolidationReceiptService(self.repository)
        from .research import ActivationService
        activation_by_id = {
            item["object_id"]: item for item in ActivationService(self.repository).aggregate()
        }
        from .research import ResearchAnnotationService
        active_annotation_ids = {item["id"] for item in ResearchAnnotationService(self.repository).active()}

        latest_source_ids = self._latest_source_ids()
        archived_only_source_ids = self._archived_only_source_ids()
        ranked: list[tuple[int, int, dict[str, Any]]] = []
        omitted: list[dict[str, Any]] = []
        results = self.repository.search_with_relations(
            query, SEARCH_LIMIT, max_depth=relation_depth, max_nodes=SEARCH_LIMIT,
            object_types=allowed_types, statuses=statuses, include_proposals=include_proposals,
            domains=domains, source_kinds=source_kinds,
        )
        seen_result_ids = {result.id for result in results}
        for seed_id in route.seed_objects[:20]:
            if seed_id in seen_result_ids:
                continue
            try:
                seed_path, seed_metadata, seed_body = self.repository.find_document(seed_id)
            except Exception:
                continue
            seed_type = str(seed_metadata.get("type", ""))
            seed_status = str(seed_metadata.get("status", ""))
            if seed_type not in allowed_types or (statuses and seed_status not in statuses):
                continue
            if domains and not (domains & set(map(str, seed_metadata.get("domains", [])))) and seed_type != "source":
                continue
            seed_sources = [str(item) for item in seed_metadata.get("source_ids", [])]
            if seed_type == "source":
                seed_sources = [seed_id]
            results.append(SearchResult(
                id=seed_id, type=seed_type, title=str(seed_metadata.get("title", seed_id)),
                path=self.repository.rel(seed_path), status=seed_status, source_ids=seed_sources,
                snippet=seed_body[:240], match_reason="research route seed from Project/Domain/Annotation",
            ))
            seen_result_ids.add(seed_id)
        if not any(result.type not in {"source", "proposal"} for result in results):
            fallback_terms = []
            for term in query.split():
                cleaned = term.strip("，。！？；：,.!?;:()[]{}\"'")
                if len(cleaned) >= 3 and cleaned.casefold() not in {
                    "what", "which", "how", "the", "and", "是什么",
                }:
                    fallback_terms.append(cleaned)
            expanded_by = []
            seen_result_ids = {result.id for result in results}
            for term in fallback_terms[:4]:
                expanded = self.repository.search_with_relations(
                    term, SEARCH_LIMIT, max_depth=relation_depth, max_nodes=SEARCH_LIMIT,
                    object_types=allowed_types, statuses=statuses,
                    include_proposals=include_proposals, domains=domains,
                    source_kinds=source_kinds,
                )
                new_results = [item for item in expanded if item.id not in seen_result_ids]
                if new_results:
                    results.extend(new_results)
                    seen_result_ids.update(item.id for item in new_results)
                    expanded_by.append(term)
                if any(result.type not in {"source", "proposal"} for result in results):
                    break
            if expanded_by:
                filter_report["query_expansion"] = expanded_by
                if len(results) == len(new_results):
                    filter_report["query_fallback"] = expanded_by[0]
        for search_rank, result in enumerate(results, start=1):
            path, metadata, body = self.repository.find_document(result.id)
            object_type = str(metadata.get("type"))
            if object_type not in allowed_types:
                continue
            if object_type == "annotation" and str(metadata.get("id")) not in active_annotation_ids:
                omitted.append({"id": str(metadata["id"]), "reason": "superseded annotation is excluded by default"})
                continue
            status = str(metadata.get("status"))
            tier = infer_tier(metadata, path)
            epistemic = infer_epistemic_status(metadata, tier)
            non_governed = object_type in {"source", "annotation"}
            current_receipt = None if non_governed else receipt_service.valid_for(str(metadata["id"]))
            receipt_state = "not_applicable" if non_governed else ("current_v2" if current_receipt else "missing_or_stale")
            semantic_failures = [] if non_governed else receipt_service.semantic_qualification_failures(object_type, current_receipt)
            policy_version = metadata.get("trust_policy_version") if not non_governed else None
            policy_qualified = bool(
                tier == "trusted" and policy_version == POLICY_VERSION
                and not metadata.get("needs_policy_requalification") and current_receipt is not None
                and not semantic_failures and epistemic != "contested" and not metadata.get("high_risk_drift")
            )
            qualification_failures = [] if non_governed else [
                *([] if policy_version == POLICY_VERSION else ["policy_version_not_current"]),
                *([] if not metadata.get("needs_policy_requalification") else ["awaiting_requalification"]),
                *([] if current_receipt is not None else ["receipt_missing_or_stale"]),
                *semantic_failures,
                *([] if epistemic != "contested" else ["contested"]),
                *([] if not metadata.get("high_risk_drift") else ["high_risk_drift"]),
            ]
            if statuses is None and object_type not in {"source", "proposal"} and status != "archived":
                visible = False
                if "research" in profiles:
                    visible = tier in {"working", "trusted", "canonical"}
                if "exploration" in profiles:
                    visible = visible or epistemic in {
                        "user_intuition", "observed_anomaly", "exploratory_analogy",
                        "hypothetical", "open_question", "partially_answered", "contested",
                    } or object_type in {"intuition", "tension", "analogy", "anomaly", "hypothesis"}
                if "execution" in profiles:
                    execution_safe = (
                        (tier == "canonical" and epistemic not in {"contested", "hypothetical", "exploratory_analogy", "unknown"})
                        or (tier == "trusted" and epistemic in {"established", "supported"})
                        or (tier == "trusted" and object_type in {"question", "tension"} and epistemic in {"open_question", "partially_answered", "contested"})
                        or (tier == "working" and bool(metadata.get("execution_blocker")))
                    )
                    degraded = metadata.get("extraction_quality") in {"degraded", "failed"}
                    visible = visible or (execution_safe and not degraded)
                if not visible:
                    omitted.append({"id": str(metadata["id"]), "reason": "profile trust policy excluded this memory tier"})
                    continue
            if strict_execution and "execution" in profiles and object_type != "source" and tier in {"trusted", "canonical"}:
                try:
                    has_relation_contradiction = any(
                        relation.get("relation_type") == "contradicts"
                        for relation in self.repository.related(str(metadata["id"]))
                    )
                except Exception:
                    has_relation_contradiction = True
                if has_relation_contradiction:
                    omitted.append({"id": str(metadata["id"]), "reason": "strict execution excludes unresolved incoming or outgoing contradiction relations"})
                    continue
                if metadata.get("needs_policy_requalification"):
                    omitted.append({"id": str(metadata["id"]), "reason": "strict execution excludes Trusted memory awaiting policy requalification"})
                    continue
                if current_receipt is None:
                    omitted.append({"id": str(metadata["id"]), "reason": "strict execution requires current Receipt v2"})
                    continue
                if semantic_failures:
                    omitted.append({"id": str(metadata["id"]), "reason": "strict execution requires type-specific semantic Receipt qualification"})
                    continue
            if updated_since and str(metadata.get("updated_at", "")) < updated_since:
                omitted.append({"id": str(metadata["id"]), "reason": "早于 updated_since filter"})
                continue
            if effective_project:
                related_projects = {
                    str(metadata.get("project_id", "")), str(metadata.get("id", "")),
                    *(str(item) for item in metadata.get("research_projects", [])),
                    *(str(relation.get("target_id")) for relation in metadata.get("relations", []) if isinstance(relation, dict)),
                }
                if (
                    effective_project not in related_projects
                    and str(metadata.get("id")) not in route.seed_objects
                    and effective_project.casefold() not in str(metadata.get("title", "")).casefold()
                ):
                    omitted.append({"id": str(metadata["id"]), "reason": "不满足 project filter"})
                    continue
            if object_type != "source" and metadata.get("status") == "archived":
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "canonical 对象已归档；Context Pack 默认排除非活动知识",
                })
                continue
            if object_type == "proposal" and not statuses and metadata.get("status") not in {"pending", "deferred"}:
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "历史 proposal 默认排除；可用 status filter 显式请求",
                })
                continue
            if object_type == "source" and str(metadata["id"]) not in latest_source_ids:
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "同一 source family 的旧版本；Context Pack 默认只选最新版本",
                })
                continue
            if object_type == "source" and str(metadata["id"]) in archived_only_source_ids:
                omitted.append({
                    "id": str(metadata["id"]),
                    "reason": "source 仅被已归档 canonical 引用；Context Pack 默认排除",
                })
                continue
            content = self._content(metadata, body)
            if not content:
                continue
            source_ids = [str(item) for item in metadata.get("source_ids", [])]
            if object_type == "source":
                source_ids = [str(metadata["id"])]
            activation_record = activation_by_id.get(str(metadata["id"]), {})
            activation_view = {
                "use_count": int(activation_record.get("used_count", 0)),
                "last_used_at": activation_record.get("last_used_at"),
                "project_use_count": int(
                    activation_record.get("projects", {}).get(effective_project, 0)
                    if effective_project else 0
                ),
            }
            ranked.append((
                -(1_000 - search_rank + self._type_priority(object_type, profiles, str(metadata.get("status")))),
                search_rank,
                {
                    "id": str(metadata["id"]),
                    "type": object_type,
                    "knowledge_status": str(metadata.get("status")),
                    "truth_layer": truth_layer(metadata, path),
                    "memory_tier": None if non_governed else tier,
                    "epistemic_status": "user_annotation" if object_type == "annotation" else ("unknown" if object_type == "source" else epistemic),
                    "confidence": metadata.get("claim_confidence", metadata.get("confidence", "unknown")),
                    "evidence_coverage": metadata.get("evidence_coverage"),
                    "evidence_entailment": metadata.get("evidence_entailment", "unknown"),
                    "unresolved_contradictions": metadata.get("unresolved_contradictions", []),
                    "last_consolidated_at": metadata.get("last_consolidated_at"),
                    "receipt_state": receipt_state,
                    "receipt_current": current_receipt is not None if not non_governed else None,
                    "policy_version": policy_version,
                    "policy_qualified": policy_qualified,
                    "execution_safe": False if object_type == "annotation" else bool(
                        object_type == "source" or policy_qualified or (
                            tier == "canonical" and current_receipt is not None and not semantic_failures
                            and epistemic not in {"contested", "hypothetical", "exploratory_analogy", "unknown"}
                            and not metadata.get("high_risk_drift")
                        )
                    ),
                    "qualification_reasons": ["current policy and Receipt v2"] if policy_qualified else [],
                    "qualification_failures": qualification_failures,
                    "qualification_scope": metadata.get("qualification_scope"),
                    "policy_state": "execution_strict" if strict_execution and "execution" in profiles else "default",
                    "proposal_id": str(metadata["id"]) if object_type == "proposal" else None,
                    "title": str(metadata["title"]),
                    "path": self.repository.rel(path),
                    "document_sha256": sha256_bytes(path.read_bytes()),
                    "source_ids": source_ids,
                    "raw_content_sha256": metadata.get("content_sha256") if object_type == "source" else None,
                    "source_version": int(metadata.get("version_number", 1)) if object_type == "source" else None,
                    "source_authority": self._source_authority(metadata),
                    "user_authored": metadata.get("user_authored") if object_type == "annotation" else None,
                    "annotation": ({
                        "annotation_id": metadata.get("id"),
                        "annotation_kind": metadata.get("annotation_kind"),
                        "target_ids": metadata.get("target_ids", []),
                        "unresolved_target_ids": metadata.get("unresolved_target_ids", []),
                        "why_saved": metadata.get("why_saved"),
                        "what_surprised_me": metadata.get("what_surprised_me"),
                        "possible_connections": metadata.get("possible_connections", []),
                        "research_projects": metadata.get("research_projects", []),
                        "domains": metadata.get("domains", []),
                        "personal_salience": metadata.get("personal_salience"),
                        "note": metadata.get("note"),
                        "feedback_label": metadata.get("feedback_label"),
                        "feedback_note": metadata.get("feedback_note"),
                        "supersedes_annotation_id": metadata.get("supersedes_annotation_id"),
                        "created_at": metadata.get("created_at"),
                    } if object_type == "annotation" else None),
                    "verification": {
                        "quote_verification": metadata.get("quote_verification", "not_applicable"),
                        "extraction_quality": metadata.get("extraction_quality", "unknown"),
                        "evidence_entailment": metadata.get("evidence_entailment", "unknown"),
                        "claim_confidence": metadata.get("claim_confidence", metadata.get("confidence", "unknown")),
                        "publication_gate": metadata.get("publication_gate"),
                        "atomicity_status": metadata.get("atomicity_status"),
                        "evidence_coverage": metadata.get("evidence_coverage"),
                    },
                    "activation": activation_view,
                    "evidence": self._evidence_view(metadata) if object_type == "claim" else [],
                    "match_reason": result.match_reason,
                    "content": content,
                    "selection_reason": (
                        f"全文检索命中第 {search_rank} 位；"
                        f"对象类型为 {object_type}；状态为 {metadata.get('status')}；"
                        f"profile={','.join(profiles)}；{result.match_reason}；保留其显式来源链。"
                    ),
                },
            ))
        if include_proposals:
            ranked.extend(self._proposal_candidates(
                query, profiles=profiles, allowed_types=allowed_types,
                statuses=statuses, domains=domains,
            ))
        canonical_source_ids = {
            source_id
            for _, _, item in ranked
            if item["truth_layer"] == "canonical"
            for source_id in item["source_ids"]
        }
        ranked = [
            (
                score - 25
                if item["type"] == "source" and item["id"] in canonical_source_ids
                else score,
                search_rank,
                item,
            )
            for score, search_rank, item in ranked
        ]
        ranked.sort(key=lambda item: (item[0], item[1], item[2]["id"]))

        available = token_budget - 48  # reserve room for outer query and policy metadata
        selected: list[dict[str, Any]] = []
        used = 0
        for _, _, item in ranked:
            metadata_text = " ".join(
                [item["id"], item["title"], item["path"], *item["source_ids"],
                 item["truth_layer"], item["source_authority"],
                 item["selection_reason"], str(item["verification"]), str(item["evidence"]),
                 str(item.get("annotation")), str(item.get("activation"))]
            )
            metadata_tokens = self._estimate_tokens(metadata_text)
            remaining = available - used - metadata_tokens
            if remaining < 24:
                omitted.append({"id": item["id"], "reason": "token budget 已耗尽"})
                continue
            content = self._clip_to_budget(item["content"], remaining)
            estimated_tokens = metadata_tokens + self._estimate_tokens(content)
            if used + estimated_tokens > available:
                omitted.append({"id": item["id"], "reason": "token budget 不足"})
                continue
            selected.append({**item, "content": content, "estimated_tokens": estimated_tokens})
            used += estimated_tokens
        trace = route.as_dict()
        trace["raw_opened"] = [item["id"] for item in selected if item.get("type") == "source"]
        trace["selection_reasons"] = [
            *trace.get("selection_reasons", []),
            *(f"{item['id']}: {item.get('selection_reason', '')}" for item in selected),
        ]
        return ContextPack(query, token_budget, used, selected, omitted, profiles, filter_report, trace)
