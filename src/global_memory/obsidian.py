from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .markdown import atomic_write_text, read_document
from .repository import Repository


class ObsidianViewService:
    """Build disposable Obsidian navigation notes without changing truth-layer pages."""

    def __init__(self, repository: Repository):
        self.repository = repository

    def _documents(self) -> list[tuple[Path, dict[str, Any]]]:
        documents: list[tuple[Path, dict[str, Any]]] = []
        for path in self.repository.canonical_documents():
            metadata, _ = read_document(path)
            documents.append((path, metadata))
        return sorted(documents, key=lambda item: (str(item[1].get("type", "")), str(item[1].get("title", ""))))

    def _link(self, path: Path, metadata: dict[str, Any]) -> str:
        relative = self.repository.rel(path)
        if relative.startswith("vault/"):
            relative = relative[len("vault/"):]
        if relative.endswith(".md"):
            relative = relative[:-3]
        return f'[[{relative}|{metadata.get("title", metadata.get("id", path.stem))}]]'

    @staticmethod
    def _generated_header(title: str) -> str:
        return (
            "---\n"
            "generated: true\n"
            "generator: gm-obsidian-v1\n"
            "---\n\n"
            f"# {title}\n\n"
            "> Generated navigation view. Rebuild with `gm obsidian build`; do not treat it as a truth source.\n\n"
        )

    def build(self) -> dict[str, Any]:
        documents = self._documents()
        by_type: dict[str, list[tuple[Path, dict[str, Any]]]] = defaultdict(list)
        partial: list[tuple[Path, dict[str, Any]]] = []
        stale: list[tuple[Path, dict[str, Any]]] = []
        for path, metadata in documents:
            by_type[str(metadata.get("type", "unknown"))].append((path, metadata))
            if metadata.get("type") == "claim" and metadata.get("evidence_coverage") in {"partial", "missing"}:
                partial.append((path, metadata))
            if metadata.get("status") in {"contested", "superseded", "archived"} or metadata.get("stale_reason"):
                stale.append((path, metadata))

        views = self.repository.root / "vault" / "views"
        views.mkdir(parents=True, exist_ok=True)
        written: list[str] = []

        catalog_lines = [self._generated_header("Knowledge Catalog")]
        for object_type in sorted(by_type):
            catalog_lines.append(f"## {object_type}\n\n")
            for path, metadata in by_type[object_type]:
                catalog_lines.append(f"- {self._link(path, metadata)} — `{metadata.get('status', 'unknown')}`\n")
            catalog_lines.append("\n")
        catalog = views / "Knowledge Catalog.md"
        atomic_write_text(catalog, "".join(catalog_lines))
        written.append(self.repository.rel(catalog))

        pending = []
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            if metadata.get("status") in {"pending", "deferred"}:
                pending.append((metadata, path))
        pending.sort(key=lambda item: (str(item[0].get("status", "")), str(item[0].get("id", ""))))
        review_lines = [self._generated_header("Review Queues"), f"## Pending proposals ({len(pending)})\n\n"]
        for metadata, path in pending:
            review_lines.append(f"- `{metadata.get('id')}` — {metadata.get('title')} (`{self.repository.rel(path)}`)\n")
        review_lines.append(f"\n## Partial evidence ({len(partial)})\n\n")
        review_lines.extend(f"- {self._link(path, metadata)}\n" for path, metadata in partial)
        review_lines.append(f"\n## Stale or historical ({len(stale)})\n\n")
        review_lines.extend(f"- {self._link(path, metadata)}\n" for path, metadata in stale)
        review = views / "Review Queues.md"
        atomic_write_text(review, "".join(review_lines))
        written.append(self.repository.rel(review))

        home = self.repository.root / "vault" / "INDEX.md"
        home_text = self._generated_header("Global Memory") + (
            "## Start here\n\n"
            "- [[views/Knowledge Catalog|Knowledge Catalog]]\n"
            "- [[views/Review Queues|Review Queues]]\n"
            "- Agent guidance lives in repository-root `AGENTS.md` (outside this Obsidian vault).\n\n"
            "## Agent reading protocol\n\n"
            "1. Read this index, then call `gm context` for the current question.\n"
            "2. Open only the pages selected by the Context Pack and follow relevant links.\n"
            "3. Treat raw as immutable and generated views as disposable.\n"
            "4. Submit new memory through a receipt/proposal; never bypass the canonical gate.\n"
        )
        atomic_write_text(home, home_text)
        written.append(self.repository.rel(home))
        return {"ok": True, "documents": len(documents), "written": written}
