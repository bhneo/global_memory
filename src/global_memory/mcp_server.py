from __future__ import annotations

import argparse
import hmac
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from .bundle import BundleRecoveryManager
from .capture import CaptureService
from .cognition import InputEpisodeService
from .context import ContextPack, ContextPackService
from .epistemics import infer_epistemic_status, infer_tier, truth_layer
from .errors import GlobalMemoryError, ValidationError
from .extraction import ExtractionService
from .governance import CanonicalPromotionRecoveryManager, TrustedPromotionRecoveryManager
from .recovery import ApprovalRecoveryManager
from .repository import Repository
from .quality import SourceQualityService


PROTOCOL_VERSION = "2025-06-18"
SERVER_INFO = {"name": "global-memory-agent-gateway", "version": "0.2.0"}
MAX_HTTP_BODY = 2 * 1024 * 1024
MAX_CAPTURE_CHARS = 200_000
INPUT_TYPES = ["article", "paper", "github", "conversation", "idea", "experiment", "meeting"]
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


def _public_locator(metadata: dict[str, Any]) -> str | None:
    locator = str(metadata.get("canonical_locator") or metadata.get("original_locator") or "")
    return locator if locator.startswith(("https://", "http://")) else None


def _source_reference(repository: Repository, source_id: str) -> dict[str, Any]:
    try:
        path, metadata, _ = repository.find_document(source_id)
        if metadata.get("type") != "source":
            raise ValidationError("not a source")
        assessment = SourceQualityService(repository).load(source_id)
        if assessment is None:
            assessment = SourceQualityService(repository).assess(source_id, persist=False)
        return {
            "ref": source_id,
            "title": metadata.get("title") or source_id,
            "author": metadata.get("author") or None,
            "published_at": metadata.get("published_at"),
            "source_kind": metadata.get("source_kind"),
            "locator": _public_locator(metadata),
            "status": metadata.get("status"),
            "source_authority": assessment.source_authority,
            "available": path.exists(),
        }
    except Exception:
        return {"ref": source_id, "title": "Referenced source", "available": False}


def _public_evidence(items: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        text = item.get("text") or item.get("original_text") or item.get("interpretation") or item.get("excerpt") or ""
        result.append({
            "source_ref": item.get("source_ref") or item.get("source_id"),
            "stance": item.get("stance"),
            "evidence_kind": item.get("evidence_kind", "legacy_excerpt"),
            "page": item.get("page"),
            "section": item.get("section"),
            "text": str(text)[:240],
            "verification_status": item.get("verification_status"),
        })
    return result


def _public_item(item: dict[str, Any]) -> dict[str, Any]:
    """Keep semantic/evidence boundaries while excluding operational diagnostics."""
    result = {
        "lookup_ref": item.get("id"),
        "title": item.get("title"),
        "object_type": item.get("type"),
        "knowledge_status": item.get("knowledge_status"),
        "memory_tier": item.get("memory_tier"),
        "epistemic_status": item.get("epistemic_status"),
        "truth_layer": item.get("truth_layer"),
        "confidence": item.get("confidence"),
        "source_authority": item.get("source_authority"),
        "evidence_coverage": item.get("evidence_coverage"),
        "evidence_entailment": item.get("evidence_entailment"),
        "unresolved_contradictions": item.get("unresolved_contradictions", []),
        "execution_safe": bool(item.get("execution_safe", False)),
        "source_refs": list(item.get("source_ids", [])),
        "content": item.get("content", item.get("snippet", "")),
    }
    if item.get("evidence"):
        result["evidence"] = _public_evidence(item["evidence"])
    for optional in ("verification", "annotation", "reflection", "cognitive_synthesis"):
        if item.get(optional):
            result[optional] = item[optional]
    return result


def _evidence_packet(repository: Repository, pack: ContextPack) -> dict[str, Any]:
    items = [_public_item(item) for item in pack.items]
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
    return {
        "evidence_packet_version": 1,
        "question": pack.query,
        "profile": pack.profiles[0] if len(pack.profiles) == 1 else pack.profiles,
        "result": "ok" if items else "insufficient_evidence",
        "knowledge": items,
        "sources": [_source_reference(repository, source_id) for source_id in source_ids],
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

    def __init__(self, repository: Repository, *, allow_capture: bool = False):
        self.repository = repository
        self.allow_capture = allow_capture

    def definitions(self) -> list[dict[str, Any]]:
        read_annotation = {
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        }
        definitions = [
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
        return definitions

    def call(self, name: str, arguments: dict[str, Any] | None) -> dict[str, Any]:
        args = arguments or {}
        if name == "memory_context":
            pack = ContextPackService(self.repository).build(
                str(args["question"]), int(args.get("token_budget", 1200)),
                profiles=[str(args.get("profile", "research"))],
                relation_depth=int(args.get("relation_depth", 1)),
            )
            return _evidence_packet(self.repository, pack)
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
                public_results.append({
                    "lookup_ref": item.id, "object_type": item.type, "title": item.title,
                    "knowledge_status": item.status,
                    "memory_tier": None if item.type in {"source", "input", "reflection", "annotation"} else infer_tier(metadata, item_path),
                    "epistemic_status": infer_epistemic_status(metadata, item_path),
                    "truth_layer": truth_layer(metadata, item_path),
                    "confidence": metadata.get("claim_confidence", metadata.get("confidence", "unknown")),
                    "source_refs": item.source_ids, "snippet": snippet,
                })
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
            item = {
                "id": metadata.get("id"), "title": metadata.get("title"), "type": metadata.get("type"),
                "knowledge_status": metadata.get("status"), "memory_tier": metadata.get("memory_tier"),
                "epistemic_status": infer_epistemic_status(metadata, path),
                "truth_layer": truth_layer(metadata, path),
                "confidence": metadata.get("claim_confidence", metadata.get("confidence", "unknown")),
                "evidence_coverage": metadata.get("evidence_coverage"),
                "evidence_entailment": metadata.get("evidence_entailment", "unknown"),
                "unresolved_contradictions": metadata.get("unresolved_contradictions", []),
                "execution_safe": metadata.get("execution_safe", False), "source_ids": source_ids,
                "content": text, "evidence": metadata.get("evidence", []),
            }
            return {
                "object": _public_item(item),
                "sources": [_source_reference(self.repository, source_id) for source_id in source_ids],
                "truncated": truncated,
            }
        if name == "memory_source":
            source_id = str(args["source_id"])
            _, metadata, _ = self.repository.find_document(source_id)
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
            return {
                "source": {**_source_reference(self.repository, source_id), "body": source_body,
                           "truncated": source_truncated},
                "extraction": extraction,
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
    def __init__(self, repository: Repository, *, allow_capture: bool = False):
        self.tools = AgentMemoryTools(repository, allow_capture=allow_capture)

    @staticmethod
    def _result(request_id: Any, result: Any) -> dict[str, Any]:
        return {"jsonrpc": "2.0", "id": request_id, "result": result}

    @staticmethod
    def _error(request_id: Any, code: int, message: str) -> dict[str, Any]:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}

    def handle(self, message: dict[str, Any]) -> dict[str, Any] | None:
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
                payload = self.tools.call(str(params.get("name", "")), params.get("arguments"))
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


def serve_stdio(repository: Repository, *, allow_capture: bool = False) -> None:
    app = MCPApplication(repository, allow_capture=allow_capture)
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
            response = app.handle(message)
        except Exception:
            response = MCPApplication._error(None, -32700, "invalid JSON-RPC request")
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False, separators=(",", ":")) + "\n")
            sys.stdout.flush()


def serve_http(
    repository: Repository,
    host: str,
    port: int,
    *,
    bearer_token: str | None,
    allowed_origins: set[str],
    allow_capture: bool = False,
) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"} and not bearer_token:
        raise ValidationError("non-loopback MCP HTTP requires a bearer token")
    app = MCPApplication(repository, allow_capture=allow_capture)

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
    http = commands.add_parser("http", help="serve the Agent Memory Gateway over Streamable HTTP")
    http.add_argument("--host", default="127.0.0.1")
    http.add_argument("--port", type=int, default=8765)
    http.add_argument("--token-env", default="GM_MCP_TOKEN")
    http.add_argument("--allowed-origin", action="append", default=[])
    http.add_argument("--allow-capture", action="store_true", help="enable explicit Capture-only text intake")


def run_mcp(repository: Repository, args: argparse.Namespace) -> None:
    if args.mcp_transport == "stdio":
        serve_stdio(repository, allow_capture=args.allow_capture)
        return
    token = os.environ.get(args.token_env) if args.token_env else None
    serve_http(
        repository, args.host, args.port,
        bearer_token=token,
        allowed_origins=set(args.allowed_origin),
        allow_capture=args.allow_capture,
    )
