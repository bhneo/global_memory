from __future__ import annotations

import argparse
import hmac
import json
import os
import sys
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

from .context import ContextPackService
from .errors import GlobalMemoryError, ValidationError
from .extraction import ExtractionService
from .maintenance import MaintenanceService
from .repository import Repository


PROTOCOL_VERSION = "2025-06-18"
SERVER_INFO = {"name": "global-memory-readonly", "version": "0.1.0"}
MAX_HTTP_BODY = 2 * 1024 * 1024


def _bounded(value: str, limit: int) -> tuple[str, bool]:
    if limit < 1:
        raise ValidationError("max_chars must be at least 1")
    return value[:limit], len(value) > limit


class ReadOnlyMemoryTools:
    """Provider-neutral MCP tools that never mutate Global Memory."""

    def __init__(self, repository: Repository):
        self.repository = repository

    @staticmethod
    def definitions() -> list[dict[str, Any]]:
        annotation = {
            "readOnlyHint": True,
            "destructiveHint": False,
            "idempotentHint": True,
            "openWorldHint": False,
        }
        return [
            {
                "name": "memory_context",
                "title": "Build bounded memory context",
                "description": "Return a provenance-preserving Context Pack for a question. Retrieval does not promote any statement into fact.",
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
                "annotations": annotation,
            },
            {
                "name": "memory_search",
                "title": "Search Global Memory",
                "description": "Search canonical knowledge and captured sources while preserving status and provenance.",
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
                "annotations": annotation,
            },
            {
                "name": "memory_show",
                "title": "Show a memory object",
                "description": "Read one object by stable ID with metadata, truth-layer path, and bounded body.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "object_id": {"type": "string", "minLength": 1},
                        "max_chars": {"type": "integer", "minimum": 1, "maximum": 50000, "default": 12000},
                    },
                    "required": ["object_id"],
                    "additionalProperties": False,
                },
                "annotations": annotation,
            },
            {
                "name": "memory_source",
                "title": "Read captured source text",
                "description": "Read a source record and an existing derived extraction. It never creates or rebuilds extraction.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "source_id": {"type": "string", "minLength": 1},
                        "max_chars": {"type": "integer", "minimum": 1, "maximum": 50000, "default": 12000},
                    },
                    "required": ["source_id"],
                    "additionalProperties": False,
                },
                "annotations": annotation,
            },
            {
                "name": "memory_status",
                "title": "Inspect memory maintenance status",
                "description": "Return read-only backlog, evidence, receipt, follow-up, and capture-only inventory.",
                "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
                "annotations": annotation,
            },
        ]

    def call(self, name: str, arguments: dict[str, Any] | None) -> dict[str, Any]:
        args = arguments or {}
        if name == "memory_context":
            pack = ContextPackService(self.repository).build(
                str(args["question"]), int(args.get("token_budget", 1200)),
                profiles=[str(args.get("profile", "research"))],
                relation_depth=int(args.get("relation_depth", 1)),
            )
            return pack.as_dict()
        if name == "memory_search":
            results = self.repository.search(
                str(args["query"]), int(args.get("limit", 10)),
                canonical_only=bool(args.get("canonical_only", False)),
                include_proposals=False,
            )
            return {"query": args["query"], "results": [asdict(item) for item in results]}
        if name == "memory_show":
            path, metadata, body = self.repository.find_document(str(args["object_id"]))
            text, truncated = _bounded(body, int(args.get("max_chars", 12000)))
            return {"metadata": metadata, "path": self.repository.rel(path), "body": text, "truncated": truncated}
        if name == "memory_source":
            source_id = str(args["source_id"])
            path, metadata, body = self.repository.find_document(source_id)
            if metadata.get("type") != "source":
                raise ValidationError(f"not a source object: {source_id}")
            limit = int(args.get("max_chars", 12000))
            source_body, source_truncated = _bounded(body, limit)
            extraction: dict[str, Any] | None = None
            try:
                extraction_path, extraction_metadata, extraction_body = ExtractionService(self.repository).latest_for_source(source_id)
                extraction_text, extraction_truncated = _bounded(extraction_body, limit)
                extraction = {
                    "metadata": extraction_metadata,
                    "path": self.repository.rel(extraction_path),
                    "text": extraction_text,
                    "truncated": extraction_truncated,
                }
            except Exception:
                extraction = None
            return {
                "source": {"metadata": metadata, "path": self.repository.rel(path), "body": source_body, "truncated": source_truncated},
                "extraction": extraction,
            }
        if name == "memory_status":
            return MaintenanceService(self.repository).inventory()
        raise ValidationError(f"unknown read-only tool: {name}")


class MCPApplication:
    def __init__(self, repository: Repository):
        self.tools = ReadOnlyMemoryTools(repository)

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
                    "instructions": "Read-only Global Memory. Preserve truth layer, status, provenance, and uncertainty. Retrieval is not approval.",
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
            return self._error(request_id, -32603, f"internal error: {exc}")


def serve_stdio(repository: Repository) -> None:
    app = MCPApplication(repository)
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            message = json.loads(line)
            response = app.handle(message)
        except Exception as exc:
            response = MCPApplication._error(None, -32700, f"parse error: {exc}")
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
) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"} and not bearer_token:
        raise ValidationError("non-loopback MCP HTTP requires a bearer token")
    app = MCPApplication(repository)

    class Handler(BaseHTTPRequestHandler):
        server_version = "GlobalMemoryMCP/0.1"

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
            except Exception as exc:
                self._json(400, MCPApplication._error(None, -32700, f"parse error: {exc}"))
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
    commands.add_parser("stdio", help="serve read-only MCP over stdio")
    http = commands.add_parser("http", help="serve read-only MCP over Streamable HTTP")
    http.add_argument("--host", default="127.0.0.1")
    http.add_argument("--port", type=int, default=8765)
    http.add_argument("--token-env", default="GM_MCP_TOKEN")
    http.add_argument("--allowed-origin", action="append", default=[])


def run_mcp(repository: Repository, args: argparse.Namespace) -> None:
    if args.mcp_transport == "stdio":
        serve_stdio(repository)
        return
    token = os.environ.get(args.token_env) if args.token_env else None
    serve_http(
        repository, args.host, args.port,
        bearer_token=token,
        allowed_origins=set(args.allowed_origin),
    )
