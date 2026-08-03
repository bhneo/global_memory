from __future__ import annotations

import argparse
import hmac
import json
import os
import sys
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from .bundle import BundleRecoveryManager
from .capture import CaptureService
from .cognition import InputEpisodeService
from .context import ContextPack, ContextPackService
from .errors import GlobalMemoryError, ValidationError
from .extraction import ExtractionService
from .gateway_contract import (
    EVIDENCE_ITEM_VERSION,
    EVIDENCE_PACKET_VERSION,
    GATEWAY_CONTRACT_VERSION,
    blocker_code,
    evidence_item_from_context,
    evidence_item_from_document,
    public_source_reference,
)
from .governance import CanonicalPromotionRecoveryManager, TrustedPromotionRecoveryManager
from .recovery import ApprovalRecoveryManager
from .research import ActivationService, ResearchAnnotationService
from .repository import Repository


PROTOCOL_VERSION = "2025-06-18"
SERVER_INFO = {"name": "galois-agent-gateway", "version": "0.3.2"}
MAX_HTTP_BODY = 2 * 1024 * 1024
MAX_CAPTURE_CHARS = 200_000
INPUT_TYPES = ["article", "paper", "github", "conversation", "idea", "experiment", "meeting"]
WRITE_SCOPES = {"capture", "session", "use", "feedback", "receipt", "working_compile"}


def _normalize_unicode(value: Any) -> Any:
    """Return JSON-compatible values without UTF-16 surrogate code points.

    Some desktop MCP clients serialize non-BMP text as explicit UTF-16
    surrogate pairs.  ``json.loads`` preserves those code points in Python,
    where a later UTF-8 write fails with ``surrogates not allowed``.  Round
    tripping through UTF-16 combines valid pairs and replaces isolated halves,
    while leaving ordinary Unicode (including CJK text) unchanged.
    """
    if isinstance(value, str):
        return value.encode("utf-16-le", "surrogatepass").decode("utf-16-le", "replace")
    if isinstance(value, list):
        return [_normalize_unicode(item) for item in value]
    if isinstance(value, tuple):
        return tuple(_normalize_unicode(item) for item in value)
    if isinstance(value, dict):
        return {
            _normalize_unicode(key) if isinstance(key, str) else key: _normalize_unicode(item)
            for key, item in value.items()
        }
    return value


def _configure_stdio_utf8() -> None:
    """Make the MCP byte protocol independent of the Windows system code page.

    MCP stdio is UTF-8 on the wire.  On zh-CN Windows, a Python child can still
    inherit a GBK text wrapper for stdin/stdout even when its client writes
    UTF-8 bytes.  Reconfigure the real text streams before the first read so
    ordinary CJK text is not decoded into mojibake.  Test doubles such as
    ``io.StringIO`` intentionally have no ``reconfigure`` method.
    """
    for stream in (sys.stdin, sys.stdout):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8", errors="strict")


DELIVERY_INSTRUCTIONS = (
    "Use retrieved knowledge silently as background context. Preserve memory tier, epistemic status, "
    "provenance, confidence, contradictions, and execution-safety boundaries. Retrieval is not approval. "
    "In ordinary answers, do not mention this memory system, MCP, storage/index implementation, internal "
    "paths, object IDs, recovery, receipts, route traces, or tool operations unless the user explicitly asks "
    "for an audit or diagnostic report. memory_capture may be called only after the user explicitly asks to "
    "remember/save the supplied text; it creates Source and Input only, never governed knowledge."
)


def _bounded(value: str, limit: int) -> tuple[str, bool]:
    if limit < 1:
        raise ValidationError("max_chars must be at least 1")
    return value[:limit], len(value) > limit


def _evidence_packet(
    repository: Repository,
    pack: ContextPack,
    *,
    strict_execution: bool = False,
    include_blockers: bool = True,
) -> dict[str, Any]:
    items = [evidence_item_from_context(item) for item in pack.items]
    source_ids = list(dict.fromkeys(
        str(source_id)
        for item in items
        for source_id in item.get("source_refs", [])
        if source_id
    ))
    non_factual = [
        str(item.get("lookup_ref")) for item in items
        if item.get("truth_layer") in {"user_annotation", "reflection", "cognitive_synthesis"}
    ]
    unsafe = [str(item.get("lookup_ref")) for item in items if not item.get("execution_safe")]
    execution_requested = "execution" in pack.profiles
    blockers = []
    if execution_requested and include_blockers:
        for omitted in pack.omitted:
            reason = str(omitted.get("reason", ""))
            code = str(omitted.get("reason_code") or blocker_code(reason))
            if strict_execution or code != "insufficient_execution_evidence":
                blockers.append({
                    "blocker_version": 1,
                    "lookup_ref": omitted.get("id"),
                    "code": code,
                    "message": reason or "Execution evidence is not qualified.",
                })
    safe_count = sum(bool(item["execution"]["safe"]) for item in items)
    execution_ready = bool(items) and safe_count == len(items) and not blockers
    if execution_requested:
        outcome = "ready" if execution_ready else ("partial" if safe_count else "blocked")
    else:
        outcome = "ready" if items else "insufficient_evidence"
    return {
        "evidence_packet_version": EVIDENCE_PACKET_VERSION,
        "gateway_contract_version": GATEWAY_CONTRACT_VERSION,
        "question": pack.query,
        "profile": pack.profiles[0] if len(pack.profiles) == 1 else pack.profiles,
        "outcome": outcome,
        "result": "ok" if outcome in {"ready", "partial"} else outcome,
        "knowledge": items,
        "sources": [public_source_reference(repository, source_id) for source_id in source_ids],
        "execution_gate": {
            "requested": execution_requested,
            "strict": strict_execution,
            "ready": execution_ready if execution_requested else None,
            "safe_item_count": safe_count,
            "blockers": blockers,
        },
        "evidence_boundary": {
            "all_items_execution_safe": not unsafe,
            "non_execution_safe_refs": unsafe,
            "non_factual_refs": non_factual,
            "retrieval_is_approval": False,
        },
        "truncation": {
            "selected_items": len(items),
            "omitted_items": len(pack.omitted),
            "budget_exhausted": any("budget" in str(item.get("reason", "")) for item in pack.omitted),
        },
    }


@dataclass(frozen=True)
class GatewayPolicy:
    write_scopes: frozenset[str] = frozenset()

    @classmethod
    def from_legacy(cls, *, allow_capture: bool) -> "GatewayPolicy":
        return cls(frozenset({"capture"} if allow_capture else set()))


def _require_explicit_authorization(args: dict[str, Any]) -> None:
    authorization = args.get("authorization")
    if not isinstance(authorization, dict) or authorization.get("explicit") is not True:
        raise ValidationError("gateway write requires explicit user authorization")


def _actor_label(args: dict[str, Any]) -> str:
    actor = args.get("actor")
    if not isinstance(actor, dict):
        raise ValidationError("gateway write requires an actor object")
    unknown = set(actor) - {"provider", "product", "client_instance"}
    if unknown:
        raise ValidationError(f"unsupported actor fields: {', '.join(sorted(unknown))}")
    provider = str(actor.get("provider", "")).strip().casefold()
    product = str(actor.get("product", "")).strip().casefold()
    if not provider or not product or len(provider) > 80 or len(product) > 80:
        raise ValidationError("actor provider and product must contain 1 to 80 characters")
    return f"{provider}:{product}"


def _idempotency_key(args: dict[str, Any]) -> str:
    value = str(args.get("idempotency_key", "")).strip()
    if not value or len(value) > 200:
        raise ValidationError("idempotency_key must contain 1 to 200 characters")
    return value


def _recover_before_capture(repository: Repository) -> None:
    recovered = [
        ApprovalRecoveryManager(repository).recover_all(),
        BundleRecoveryManager(repository).recover_all(),
        TrustedPromotionRecoveryManager(repository).recover_all(),
        CanonicalPromotionRecoveryManager(repository).recover_all(),
    ]
    if any(result["blocked"] for result in recovered):
        raise ValidationError("capture unavailable until blocked repository recovery is reviewed")


class AgentMemoryTools:
    """Agent-facing evidence tools plus an explicitly enabled Capture-only boundary."""

    def __init__(
        self,
        repository: Repository,
        *,
        allow_capture: bool = False,
        policy: GatewayPolicy | None = None,
    ):
        self.repository = repository
        self.policy = policy or GatewayPolicy.from_legacy(allow_capture=allow_capture)
        self.allow_capture = "capture" in self.policy.write_scopes

    def capabilities(self) -> dict[str, Any]:
        scopes = sorted(self.policy.write_scopes)
        return {
            "gateway_contract_version": GATEWAY_CONTRACT_VERSION,
            "server_version": SERVER_INFO["version"],
            "evidence_item_version": EVIDENCE_ITEM_VERSION,
            "evidence_packet_version": EVIDENCE_PACKET_VERSION,
            "profiles": ["research", "execution", "exploration"],
            "strict_execution_supported": True,
            "enabled_write_scopes": scopes,
            "authority": {
                "source_input_write": "capture" in scopes or "session" in scopes,
                "annotation_write": "feedback" in scopes,
                "activation_write": "use" in scopes,
                "receipt_write": "receipt" in scopes,
                "working_write": "working_compile" in scopes,
                "trusted_write": False,
                "canonical_write": False,
            },
            "limits": {
                "max_capture_chars": MAX_CAPTURE_CHARS,
                "max_context_tokens": 20_000,
                "max_search_results": 50,
            },
            "idempotency_required_for": ["session", "use", "feedback", "receipt"],
        }

    def definitions(self) -> list[dict[str, Any]]:
        read_annotation = {
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        }
        definitions = [
            {
                "name": "memory_capabilities",
                "title": "Inspect memory gateway capabilities",
                "description": "Return the versioned evidence contract and exact write authority enabled for this server.",
                "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
                "annotations": read_annotation,
            },
            {
                "name": "memory_context",
                "title": "Get bounded evidence context",
                "description": (
                    "Return a delivery-safe Evidence Packet for a question. It preserves epistemic and source "
                    "boundaries but omits storage paths, route traces, indexes, and maintenance diagnostics."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "question": {"type": "string", "minLength": 1},
                        "token_budget": {"type": "integer", "minimum": 128, "maximum": 20000, "default": 1200},
                        "profile": {"type": "string", "enum": ["research", "execution", "exploration"], "default": "research"},
                        "relation_depth": {"type": "integer", "minimum": 0, "maximum": 3, "default": 1},
                        "strict_execution": {
                            "type": "boolean",
                            "default": False,
                            "description": "Fail closed and return structured blockers; valid only with profile=execution.",
                        },
                        "include_blockers": {"type": "boolean", "default": True},
                    },
                    "required": ["question"],
                    "additionalProperties": False,
                },
                "annotations": read_annotation,
            },
            {
                "name": "memory_search",
                "title": "Search evidence",
                "description": "Find bounded memory objects without exposing paths, ranking diagnostics, or maintenance state.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "minLength": 1},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 50, "default": 10},
                        "canonical_only": {"type": "boolean", "default": False},
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
                "annotations": read_annotation,
            },
            {
                "name": "memory_show",
                "title": "Read one evidence object",
                "description": "Read one object by lookup reference with its truth and provenance boundary, without filesystem details.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "object_id": {"type": "string", "minLength": 1},
                        "max_chars": {"type": "integer", "minimum": 1, "maximum": 50000, "default": 12000},
                    },
                    "required": ["object_id"],
                    "additionalProperties": False,
                },
                "annotations": read_annotation,
            },
            {
                "name": "memory_source",
                "title": "Read source evidence",
                "description": "Read a captured source and existing extraction without creating extraction or exposing local paths.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "source_id": {"type": "string", "minLength": 1},
                        "max_chars": {"type": "integer", "minimum": 1, "maximum": 50000, "default": 12000},
                    },
                    "required": ["source_id"],
                    "additionalProperties": False,
                },
                "annotations": read_annotation,
            },
        ]
        if self.allow_capture:
            definitions.append({
                "name": "memory_capture",
                "title": "Capture explicitly requested memory",
                "description": (
                    "Capture user-supplied text only after an explicit remember/save request. Writes immutable "
                    "Source and Input Episode only; it never creates Working, Trusted, or Canonical knowledge."
                ),
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "content": {"type": "string", "minLength": 1, "maxLength": MAX_CAPTURE_CHARS},
                        "title": {"type": "string", "minLength": 1, "maxLength": 200},
                        "input_type": {"type": "string", "enum": INPUT_TYPES, "default": "idea"},
                        "why_saved": {"type": "string", "minLength": 1, "maxLength": 1000},
                        "confirmed": {
                            "type": "boolean", "const": True,
                            "description": "Must be true only when the user explicitly requested this capture.",
                        },
                    },
                    "required": ["content", "title", "why_saved", "confirmed"],
                    "additionalProperties": False,
                },
                "annotations": {
                    "readOnlyHint": False,
                    "destructiveHint": False,
                    "idempotentHint": True,
                    "openWorldHint": False,
                },
            })
        write_annotation = {
            "readOnlyHint": False,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        }
        actor_schema = {
            "type": "object",
            "properties": {
                "provider": {"type": "string", "minLength": 1, "maxLength": 80},
                "product": {"type": "string", "minLength": 1, "maxLength": 80},
                "client_instance": {"type": "string", "maxLength": 120},
            },
            "required": ["provider", "product"],
            "additionalProperties": False,
        }
        authorization_schema = {
            "type": "object",
            "properties": {"explicit": {"type": "boolean", "const": True}},
            "required": ["explicit"],
            "additionalProperties": False,
        }
        if "session" in self.policy.write_scopes:
            definitions.append({
                "name": "memory_session_record",
                "title": "Record an explicitly authorized session episode",
                "description": "Store a bounded goal/result/lesson summary as Source + Input only; never writes governed knowledge.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "actor": actor_schema,
                        "session_ref": {"type": "string", "minLength": 1, "maxLength": 200},
                        "idempotency_key": {"type": "string", "minLength": 1, "maxLength": 200},
                        "authorization": authorization_schema,
                        "goal": {"type": "string", "minLength": 1, "maxLength": 4000},
                        "result": {"type": "string", "minLength": 1, "maxLength": 12000},
                        "lesson": {"type": "string", "minLength": 1, "maxLength": 8000},
                    },
                    "required": ["actor", "session_ref", "idempotency_key", "authorization", "goal", "result", "lesson"],
                    "additionalProperties": False,
                },
                "annotations": write_annotation,
            })
        if "use" in self.policy.write_scopes:
            definitions.append({
                "name": "memory_use_record",
                "title": "Record actual use of memory",
                "description": "Append an idempotent operational use event. Retrieval alone must not call this tool.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "actor": actor_schema,
                        "session_ref": {"type": "string", "minLength": 1, "maxLength": 200},
                        "idempotency_key": {"type": "string", "minLength": 1, "maxLength": 200},
                        "authorization": authorization_schema,
                        "object_id": {"type": "string", "minLength": 1},
                        "kind": {"type": "string", "enum": ["opened", "used", "cited", "coactivated"]},
                        "project_id": {"type": "string"},
                        "query": {"type": "string", "maxLength": 4000},
                        "reason": {"type": "string", "maxLength": 2000},
                        "coactivated_ids": {"type": "array", "items": {"type": "string"}, "maxItems": 50},
                    },
                    "required": ["actor", "session_ref", "idempotency_key", "authorization", "object_id", "kind"],
                    "additionalProperties": False,
                },
                "annotations": write_annotation,
            })
        if "feedback" in self.policy.write_scopes:
            definitions.append({
                "name": "memory_feedback_record",
                "title": "Record user connection-value feedback",
                "description": "Store explicit obvious/forced/interesting/actionable feedback as user_annotation, never as truth evidence.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "actor": actor_schema,
                        "session_ref": {"type": "string", "minLength": 1, "maxLength": 200},
                        "idempotency_key": {"type": "string", "minLength": 1, "maxLength": 200},
                        "authorization": authorization_schema,
                        "target_id": {"type": "string", "minLength": 1},
                        "label": {"type": "string", "enum": ["obvious", "forced", "interesting", "actionable"]},
                        "note": {"type": "string", "minLength": 1, "maxLength": 4000},
                        "projects": {"type": "array", "items": {"type": "string"}, "maxItems": 20},
                        "domains": {"type": "array", "items": {"type": "string"}, "maxItems": 20},
                    },
                    "required": ["actor", "session_ref", "idempotency_key", "authorization", "target_id", "label", "note"],
                    "additionalProperties": False,
                },
                "annotations": write_annotation,
            })
        return definitions

    def call(self, name: str, arguments: dict[str, Any] | None) -> dict[str, Any]:
        args = arguments or {}
        if name == "memory_capabilities":
            if args:
                raise ValidationError("memory_capabilities accepts no arguments")
            return self.capabilities()
        if name == "memory_context":
            profile = str(args.get("profile", "research"))
            strict_execution = bool(args.get("strict_execution", False))
            if strict_execution and profile != "execution":
                raise ValidationError("strict_execution requires profile=execution")
            pack = ContextPackService(self.repository).build(
                str(args["question"]), int(args.get("token_budget", 1200)),
                profiles=[profile],
                relation_depth=int(args.get("relation_depth", 1)),
                strict_execution=strict_execution,
            )
            return _evidence_packet(
                self.repository,
                pack,
                strict_execution=strict_execution,
                include_blockers=bool(args.get("include_blockers", True)),
            )
        if name == "memory_search":
            results = self.repository.search(
                str(args["query"]), int(args.get("limit", 10)),
                canonical_only=bool(args.get("canonical_only", False)),
                include_proposals=False,
            )
            public_results = []
            for item in results:
                snippet = item.snippet
                item_path, metadata, _ = self.repository.find_document(item.id)
                if item.type == "source":
                    source_payload = self.call("memory_source", {"source_id": item.id, "max_chars": 600})
                    extraction = source_payload.get("extraction") or {}
                    snippet = extraction.get("text") or source_payload["source"]["body"]
                public_results.append(evidence_item_from_document(
                    self.repository, item_path, metadata, snippet,
                ))
            return {"query": args["query"], "results": public_results}
        if name == "memory_show":
            path, metadata, body = self.repository.find_document(str(args["object_id"]))
            if metadata.get("type") == "source":
                return self.call("memory_source", {
                    "source_id": metadata["id"], "max_chars": int(args.get("max_chars", 12000)),
                })
            text, truncated = _bounded(body, int(args.get("max_chars", 12000)))
            source_ids = [str(item) for item in metadata.get("source_ids", [])]
            if metadata.get("type") == "source":
                source_ids = [str(metadata["id"])]
            item = evidence_item_from_document(self.repository, path, metadata, text)
            return {
                "item": item,
                "object": item,
                "sources": [public_source_reference(self.repository, source_id) for source_id in source_ids],
                "truncated": truncated,
            }
        if name == "memory_source":
            source_id = str(args["source_id"])
            source_path, metadata, _source_markdown_body = self.repository.find_document(source_id)
            if metadata.get("type") != "source":
                raise ValidationError(f"not a source object: {source_id}")
            limit = int(args.get("max_chars", 12000))
            try:
                raw_path = self.repository.resolve_inside(str(metadata["raw_content_path"]))
                raw_text = raw_path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError, KeyError, ValidationError):
                raw_text = "Binary or unavailable source content. Use the verified extraction when present."
            source_body, source_truncated = _bounded(raw_text, limit)
            extraction: dict[str, Any] | None = None
            try:
                _, extraction_metadata, extraction_body = ExtractionService(self.repository).latest_for_source(source_id)
                extraction_text, extraction_truncated = _bounded(extraction_body, limit)
                extraction = {
                    "status": extraction_metadata.get("status"), "text": extraction_text,
                    "truncated": extraction_truncated,
                }
            except Exception:
                extraction = None
            item = evidence_item_from_document(self.repository, source_path, metadata, source_body)
            return {
                "item": item,
                "source": {**public_source_reference(self.repository, source_id), "body": source_body,
                           "truncated": source_truncated, "execution_safe": False},
                "extraction": extraction,
            }
        if name == "memory_session_record":
            if "session" not in self.policy.write_scopes:
                raise ValidationError("session recording is not enabled for this server")
            _require_explicit_authorization(args)
            actor = _actor_label(args)
            _idempotency_key(args)
            result = InputEpisodeService(self.repository).record_agent_session(
                {key: args.get(key) for key in ("goal", "result", "lesson")},
                agent=actor,
                session_ref=str(args.get("session_ref", "")),
            )
            return {
                "operation": "session_record",
                "status": "accepted" if result["input"]["created"] else "duplicate",
                "source_ref": result["source"]["source_id"],
                "input_ref": result["input"]["object_id"],
                "reflection_queued": True,
                "working_writes": 0,
                "trusted_writes": 0,
                "canonical_writes": 0,
            }
        if name == "memory_use_record":
            if "use" not in self.policy.write_scopes:
                raise ValidationError("use recording is not enabled for this server")
            _require_explicit_authorization(args)
            actor = _actor_label(args)
            event_id = _idempotency_key(args)
            kind = str(args.get("kind", ""))
            if kind not in {"opened", "used", "cited", "coactivated"}:
                raise ValidationError("gateway use kind must be opened/used/cited/coactivated")
            result = ActivationService(self.repository).record(
                str(args.get("object_id", "")),
                kind=kind,
                project_id=str(args.get("project_id") or "") or None,
                query=str(args.get("query") or "") or None,
                context_pack_id=str(args.get("session_ref") or "") or None,
                reason=str(args.get("reason") or ""),
                source=f"gateway:{actor}",
                coactivated_ids=list(map(str, args.get("coactivated_ids", []))),
                event_id=event_id,
            )
            return {
                "operation": "use_record",
                "status": "duplicate" if result["duplicate"] else "accepted",
                **result,
                "working_writes": 0,
                "trusted_writes": 0,
                "canonical_writes": 0,
            }
        if name == "memory_feedback_record":
            if "feedback" not in self.policy.write_scopes:
                raise ValidationError("feedback recording is not enabled for this server")
            _require_explicit_authorization(args)
            _actor_label(args)
            event_id = _idempotency_key(args)
            result = ResearchAnnotationService(self.repository).create(
                "connection_feedback",
                target_ids=[str(args.get("target_id", ""))],
                feedback_label=str(args.get("label", "")),
                feedback_note=str(args.get("note", "")),
                research_projects=list(map(str, args.get("projects", []))),
                domains=list(map(str, args.get("domains", []))),
                created_by="user",
                external_event_id=event_id,
            )
            return {
                "operation": "feedback_record",
                "status": "duplicate" if result.get("duplicate") else "accepted",
                "annotation_ref": result["id"],
                "truth_layer": "user_annotation",
                "execution_safe": False,
                "working_writes": 0,
                "trusted_writes": 0,
                "canonical_writes": 0,
            }
        if name == "memory_capture":
            if not self.allow_capture:
                raise ValidationError("capture is not enabled for this server")
            if args.get("confirmed") is not True:
                raise ValidationError("capture requires explicit user confirmation")
            content = str(args.get("content", ""))
            title = str(args.get("title", "")).strip()
            why_saved = str(args.get("why_saved", "")).strip()
            input_type = str(args.get("input_type", "idea"))
            if not content.strip() or len(content) > MAX_CAPTURE_CHARS:
                raise ValidationError("capture content must contain 1 to 200000 characters")
            if not title or len(title) > 200 or not why_saved or len(why_saved) > 1000:
                raise ValidationError("capture requires bounded title and why_saved")
            if input_type not in INPUT_TYPES:
                raise ValidationError(f"invalid input_type: {input_type}")
            with self.repository.writer_lock():
                _recover_before_capture(self.repository)
                captured = CaptureService(self.repository).capture_text(content, why_saved, title)
                episode = InputEpisodeService(self.repository).create_from_source(
                    captured.source_id, input_type=input_type, title=title,
                    user_authored=True, submitted_by="agent-gateway",
                )
                self.repository.rebuild_index()
            return {
                "capture_status": "captured" if not captured.duplicate_source else "already_captured",
                "source_ref": captured.source_id,
                "input_ref": episode.object_id,
                "input_created": episode.created,
                "reflection_queued": True,
                "working_writes": 0,
                "trusted_writes": 0,
                "canonical_writes": 0,
            }
        raise ValidationError(f"unknown agent memory tool: {name}")


class ReadOnlyMemoryTools(AgentMemoryTools):
    """Compatibility name for the default no-write gateway."""

    def __init__(self, repository: Repository):
        super().__init__(repository, allow_capture=False)


class MCPApplication:
    def __init__(
        self,
        repository: Repository,
        *,
        allow_capture: bool = False,
        write_scopes: set[str] | None = None,
    ):
        scopes = set(write_scopes or set())
        if allow_capture:
            scopes.add("capture")
        unknown = scopes - WRITE_SCOPES
        if unknown:
            raise ValidationError(f"unknown gateway write scopes: {', '.join(sorted(unknown))}")
        self.tools = AgentMemoryTools(repository, policy=GatewayPolicy(frozenset(scopes)))

    @staticmethod
    def _result(request_id: Any, result: Any) -> dict[str, Any]:
        return {"jsonrpc": "2.0", "id": request_id, "result": result}

    @staticmethod
    def _error(request_id: Any, code: int, message: str) -> dict[str, Any]:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}

    def handle(self, message: dict[str, Any]) -> dict[str, Any] | None:
        message = _normalize_unicode(message)
        request_id = message.get("id")
        method = message.get("method")
        if request_id is None:
            return None
        try:
            if method == "initialize":
                return self._result(request_id, {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {"tools": {"listChanged": False}},
                    "serverInfo": SERVER_INFO,
                    "instructions": DELIVERY_INSTRUCTIONS,
                })
            if method == "ping":
                return self._result(request_id, {})
            if method == "tools/list":
                return self._result(request_id, {"tools": self.tools.definitions()})
            if method == "tools/call":
                params = message.get("params") or {}
                payload = _normalize_unicode(
                    self.tools.call(str(params.get("name", "")), params.get("arguments"))
                )
                serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True)
                return self._result(request_id, {
                    "content": [{"type": "text", "text": serialized}],
                    "structuredContent": payload,
                    "isError": False,
                })
            return self._error(request_id, -32601, f"method not found: {method}")
        except (GlobalMemoryError, KeyError, TypeError, ValueError) as exc:
            return self._result(request_id, {
                "content": [{"type": "text", "text": str(exc)}],
                "isError": True,
            })
        except Exception as exc:
            print(f"MCP internal error: {type(exc).__name__}: {exc}", file=sys.stderr)
            return self._result(request_id, {
                "content": [{"type": "text", "text": "memory service is temporarily unavailable"}],
                "isError": True,
            })


def serve_stdio(
    repository: Repository,
    *,
    allow_capture: bool = False,
    write_scopes: set[str] | None = None,
) -> None:
    _configure_stdio_utf8()
    app = MCPApplication(repository, allow_capture=allow_capture, write_scopes=write_scopes)
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            message = _normalize_unicode(json.loads(line))
            response = app.handle(message)
        except Exception:
            response = MCPApplication._error(None, -32700, "invalid JSON-RPC request")
        if response is not None:
            sys.stdout.write(
                json.dumps(_normalize_unicode(response), ensure_ascii=False, separators=(",", ":")) + "\n"
            )
            # stdio MCP clients keep the server process alive while waiting for
            # each response, so process-exit flushing is not sufficient.
            sys.stdout.flush()


def serve_http(
    repository: Repository,
    host: str,
    port: int,
    *,
    bearer_token: str | None,
    allowed_origins: set[str],
    allow_capture: bool = False,
    write_scopes: set[str] | None = None,
) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"} and not bearer_token:
        raise ValidationError("non-loopback MCP HTTP requires a bearer token")
    app = MCPApplication(repository, allow_capture=allow_capture, write_scopes=write_scopes)

    class Handler(BaseHTTPRequestHandler):
        server_version = "GlobalMemoryMCP/0.2"

        def _authorized(self) -> bool:
            if not bearer_token:
                return True
            supplied = self.headers.get("Authorization", "")
            return hmac.compare_digest(supplied, f"Bearer {bearer_token}")

        def _origin_allowed(self) -> bool:
            origin = self.headers.get("Origin")
            return not origin or origin in allowed_origins

        def _json(self, status: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self) -> None:  # noqa: N802
            if self.path != "/mcp":
                self.send_error(404)
                return
            if not self._origin_allowed():
                self.send_error(403, "Origin not allowed")
                return
            if not self._authorized():
                self.send_error(401, "Bearer token required")
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                self.send_error(400, "Invalid Content-Length")
                return
            if length < 1 or length > MAX_HTTP_BODY:
                self.send_error(413, "Invalid request size")
                return
            try:
                message = json.loads(self.rfile.read(length).decode("utf-8"))
                response = app.handle(message)
            except Exception:
                self._json(400, MCPApplication._error(None, -32700, "invalid JSON-RPC request"))
                return
            if response is None:
                self.send_response(202)
                self.end_headers()
            else:
                self._json(200, response)

        def do_GET(self) -> None:  # noqa: N802
            self.send_response(405)
            self.send_header("Allow", "POST")
            self.end_headers()

        def log_message(self, format: str, *args: Any) -> None:
            print(format % args, file=sys.stderr)

    ThreadingHTTPServer((host, port), Handler).serve_forever()


def add_mcp_arguments(parser: argparse.ArgumentParser) -> None:
    commands = parser.add_subparsers(dest="mcp_transport", required=True)
    stdio = commands.add_parser("stdio", help="serve the Agent Memory Gateway over stdio")
    stdio.add_argument("--allow-capture", action="store_true", help="enable explicit Capture-only text intake")
    stdio.add_argument("--write-scope", action="append", choices=sorted(WRITE_SCOPES), default=[])
    http = commands.add_parser("http", help="serve the Agent Memory Gateway over Streamable HTTP")
    http.add_argument("--host", default="127.0.0.1")
    http.add_argument("--port", type=int, default=8765)
    http.add_argument("--token-env", default="GM_MCP_TOKEN")
    http.add_argument("--allowed-origin", action="append", default=[])
    http.add_argument("--allow-capture", action="store_true", help="enable explicit Capture-only text intake")
    http.add_argument("--write-scope", action="append", choices=sorted(WRITE_SCOPES), default=[])


def run_mcp(repository: Repository, args: argparse.Namespace) -> None:
    if args.mcp_transport == "stdio":
        serve_stdio(repository, allow_capture=args.allow_capture, write_scopes=set(args.write_scope))
        return
    token = os.environ.get(args.token_env) if args.token_env else None
    serve_http(
        repository, args.host, args.port,
        bearer_token=token,
        allowed_origins=set(args.allowed_origin),
        allow_capture=args.allow_capture,
        write_scopes=set(args.write_scope),
    )
