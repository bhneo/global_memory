from __future__ import annotations

from pathlib import Path
from typing import Any

from .bundle import BundleCompiler
from .capture import CaptureService
from .errors import NotFoundError, ValidationError
from .markdown import read_document, render_document
from .repository import Repository, now_iso, sha256_bytes, slugify


SUPPORTED_AGENTS = {"codex", "cursor", "claude"}


class ReceiptService:
    """Create immutable session receipts and route write-back through normal proposals."""

    def __init__(self, repository: Repository):
        self.repository = repository

    def create(self, agent: str, project: str, task: str, input_file: Path | str) -> dict[str, Any]:
        normalized_agent = agent.strip().lower()
        if normalized_agent not in SUPPORTED_AGENTS:
            raise ValidationError(f"unsupported receipt agent: {agent}")
        body = Path(input_file).expanduser().resolve().read_text(encoding="utf-8").strip()
        if not body:
            raise ValidationError("receipt body must not be empty")
        digest = sha256_bytes(f"{normalized_agent}\n{project}\n{task}\n{body}".encode("utf-8"))
        receipt_id = f"receipt_{digest[:20]}"
        path = self.repository.root / "vault" / "receipts" / f"receipt-{receipt_id}-{slugify(task)}.md"
        if path.exists():
            existing, _ = read_document(path)
            return {
                "receipt_id": receipt_id, "path": self.repository.rel(path),
                "content_sha256": existing["content_sha256"],
            }
        created_at = now_iso()
        metadata = {
            "id": receipt_id, "type": "receipt", "status": "captured",
            "title": task.strip(), "created_at": created_at, "updated_at": created_at,
            "agent": normalized_agent, "project": project.strip(), "task": task.strip(),
            "receipt_version": 1, "content_sha256": sha256_bytes(body.encode("utf-8")),
        }
        self.repository.immutable_write(path, render_document(metadata, body).encode("utf-8"))
        return {"receipt_id": receipt_id, "path": self.repository.rel(path), "content_sha256": metadata["content_sha256"]}

    def _find(self, receipt_id: str) -> tuple[Path, dict[str, Any], str]:
        for path in (self.repository.root / "vault" / "receipts").glob("receipt-*.md"):
            metadata, body = read_document(path)
            if metadata.get("id") == receipt_id:
                return path, metadata, body
        raise NotFoundError(f"receipt not found: {receipt_id}")

    def propose(self, receipt_id: str) -> dict[str, Any]:
        path, metadata, body = self._find(receipt_id)
        captured = CaptureService(self.repository).capture_text(
            body,
            comment=f"session receipt {receipt_id} from {metadata['agent']} for {metadata['project']}",
            title=f"Session receipt: {metadata['title']}",
        )
        bundle = BundleCompiler(self.repository).compile(captured.source_id)
        if not bundle.proposal_id or not bundle.proposal_path:
            raise ValidationError(
                f"receipt did not produce a knowledge proposal: {bundle.compile_disposition}"
            )
        return {
            "receipt_id": receipt_id, "receipt_path": self.repository.rel(path),
            "source_id": captured.source_id, "proposal_id": bundle.proposal_id,
            "proposal_path": bundle.proposal_path,
        }
