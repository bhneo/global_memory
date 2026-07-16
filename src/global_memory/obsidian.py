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

    def render(self) -> dict[str, str]:
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

        catalog_lines = [self._generated_header("Knowledge Catalog")]
        for object_type in sorted(by_type):
            catalog_lines.append(f"## {object_type}\n\n")
            for path, metadata in by_type[object_type]:
                catalog_lines.append(f"- {self._link(path, metadata)} — `{metadata.get('status', 'unknown')}`\n")
            catalog_lines.append("\n")
        catalog_text = "".join(catalog_lines)

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
        review_text = "".join(review_lines)

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
        return {
            "vault/views/Knowledge Catalog.md": catalog_text,
            "vault/views/Review Queues.md": review_text,
            "vault/INDEX.md": home_text,
        }

    def status(self) -> dict[str, Any]:
        rendered = self.render()
        missing = []
        stale = []
        for relative, expected in rendered.items():
            path = self.repository.root / relative
            if not path.exists():
                missing.append(relative)
            elif path.read_text(encoding="utf-8") != expected:
                stale.append(relative)
        return {"current": not missing and not stale, "missing": missing, "stale": stale}

    def build(self) -> dict[str, Any]:
        rendered = self.render()
        for relative, content in rendered.items():
            atomic_write_text(self.repository.root / relative, content)
        return {
            "ok": True,
            "documents": len(self._documents()),
            "written": list(rendered),
        }
