from __future__ import annotations

from typing import Any

from .bundle import BundleCompiler, DeterministicCompilerProvider
from .extraction import ExtractionService
from .markdown import read_document
from .repository import Repository


class SemanticDistillationQueue:
    """Expose bounded Source-only material for an external Agent model.

    The queue is read-only.  A model returns a normal JSON Bundle which still
    passes through ``gm compile --bundle-file`` and Working-memory governance.
    """

    COMPLETED_STATUSES = {"migrated", "approved", "published"}

    def __init__(self, repository: Repository):
        self.repository = repository
        self.extractions = ExtractionService(repository)

    def _state(self) -> tuple[set[str], set[str]]:
        source_only: set[str] = set()
        model_processed: set[str] = set()
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            source_ids = {str(item) for item in metadata.get("source_ids", [])}
            if metadata.get("status") == "source_only" or metadata.get("compile_disposition") == "source_only":
                source_only.update(
                    str(item)
                    for item in metadata.get("source_only_source_ids", metadata.get("source_ids", []))
                )
            processor = str(metadata.get("processor") or "")
            if (
                processor
                and processor != DeterministicCompilerProvider.name
                and metadata.get("status") in self.COMPLETED_STATUSES
                and metadata.get("bundle_items")
            ):
                model_processed.update(source_ids)
        return source_only, model_processed

    def queue(self, *, limit: int = 5, max_chars: int = 6000) -> dict[str, Any]:
        if limit < 1 or limit > 25:
            raise ValueError("semantic queue limit must be between 1 and 25")
        if max_chars < 1000 or max_chars > 20000:
            raise ValueError("semantic queue max_chars must be between 1000 and 20000")
        source_only, model_processed = self._state()
        candidates = []
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            source_id = str(metadata["id"])
            if source_id not in source_only or source_id in model_processed:
                continue
            candidates.append((path, metadata))
        candidates.sort(
            key=lambda item: str(item[1].get("captured_at") or item[1].get("created_at") or ""),
            reverse=True,
        )
        items = []
        compiler = BundleCompiler(self.repository)
        for path, metadata in candidates[:limit]:
            source_id = str(metadata["id"])
            try:
                _, extraction, text = self.extractions.latest_for_source(source_id)
            except Exception:
                continue
            items.append({
                "source_id": source_id,
                "title": str(metadata.get("title") or metadata.get("original_title") or source_id),
                "source_kind": metadata.get("source_kind"),
                "source_authority": metadata.get("source_authority", "unknown"),
                "captured_at": metadata.get("captured_at") or metadata.get("created_at"),
                "source_path": self.repository.rel(path),
                "reader_path": f"vault/views/readers/{source_id}.md",
                "extraction_id": extraction.get("extraction_id"),
                "input_sha256": extraction.get("input_sha256"),
                "excerpt": text[:max_chars],
                "existing_context": compiler._existing_context(metadata, text),
            })
        return {
            "mode": "semantic-distillation-queue",
            "pending_count": len(candidates),
            "selected_count": len(items),
            "omitted_count": max(0, len(candidates) - len(items)),
            "items": items,
            "provider_contract": {
                "apply": ".\\scripts\\gm.ps1 compile <source_id> --bundle-file <json> --provider-name agent-semantic-v1",
                "output": "JSON object with an items array; each item needs object_type, title and body",
                "allowed_actions": ["create", "update"],
                "update_requires": ["target_id", "change_type"],
                "relation_types": [
                    "supports", "contradicts", "refines", "analogous_to", "applied_in",
                    "raises", "related_to", "limits", "defines", "instantiates", "answers",
                    "tested_by", "failed_in", "depends_on", "part_of",
                ],
                "truth_boundary": "All model output enters Working; Trusted/Canonical gates are unchanged.",
            },
        }

