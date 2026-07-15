from __future__ import annotations

import json
from contextlib import nullcontext
import uuid
from pathlib import Path

from global_memory.bundle import BundleCompiler, BundleReviewService
from global_memory.capture import CaptureService
from global_memory.context import ContextPackService
from global_memory.extraction import ExtractionService
from global_memory.raw_store import RawStoreService
from global_memory.repository import Repository


def make_pdf(pages: list[list[str]]) -> bytes:
    objects: list[bytes] = []
    page_ids = [3 + index * 2 for index in range(len(pages))]
    font_id = 3 + len(pages) * 2
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    objects.append(f"<< /Type /Pages /Kids [{' '.join(f'{item} 0 R' for item in page_ids)}] /Count {len(pages)} >>".encode())
    for index, lines in enumerate(pages):
        page_id = page_ids[index]
        content_id = page_id + 1
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>".encode()
        )
        commands = ["BT /F1 10 Tf 60 740 Td 14 TL"]
        for line_index, line in enumerate(lines):
            escaped = line.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
            commands.append(f"({escaped}) Tj" if line_index == 0 else f"T* ({escaped}) Tj")
        commands.append("ET")
        stream = " ".join(commands).encode()
        objects.append(f"<< /Length {len(stream)} >>\nstream\n".encode() + stream + b"\nendstream")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    payload = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for number, obj in enumerate(objects, start=1):
        offsets.append(len(payload))
        payload.extend(f"{number} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n".encode() + b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode())
    payload.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(payload)


def main() -> None:
    temp_parent = Path.cwd() / "data" / "derived"
    temp_parent.mkdir(parents=True, exist_ok=True)
    temp = temp_parent / f"m5-acceptance-{uuid.uuid4().hex}"
    temp.mkdir()
    root = temp / "中文-Vault"
    with nullcontext(temp):
        repo = Repository(root)
        repo.init()
        pdf = make_pdf([
            ["Project: M5 memory demo", "Decision: Raw and extraction remain separate", "Failure: Hidden provenance breaks trust"],
            ["Concept: Rebuildable memory view", "Claim: Derived indexes can be rebuilt from source truth", "Question: When should consolidation run?", "Tension: automation versus human confirmation"],
        ])
        local_file = Path(temp) / "同一论文.pdf"
        local_file.write_bytes(pdf)
        remote = CaptureService(repo)._write_source(
            kind="web", original_locator="https://example.test/paper",
            canonical_locator="https://example.test/paper", content=pdf,
            title="M5 demo paper", import_method="acceptance-demo", content_type="application/pdf",
        )
        local = CaptureService(repo).capture_file(local_file, "cross-entry dedup demo")
        extraction = ExtractionService(repo).extract(remote.source_id)
        bundle = BundleCompiler(repo).compile(remote.source_id)
        review = BundleReviewService(repo).approve(bundle.proposal_id)
        context = ContextPackService(repo).build(
            "M5 memory demo", 5000, profiles=["execution", "research", "exploration"], relation_depth=1,
        ).as_dict()
        repo.index_path.unlink()
        extraction_path = repo.root / extraction.extraction_path
        extraction_path.unlink()
        rebuilt_index = repo.rebuild_index()
        rebuilt_extraction = ExtractionService(repo).extract(remote.source_id, rebuild=True)
        report = {
            "cross_entry_dedup": {
                "different_sources": remote.source_id != local.source_id,
                "same_content_id": remote.content_id == local.content_id,
                "same_object_path": remote.raw_content_path == local.raw_content_path,
            },
            "raw_integrity": RawStoreService(repo).verify(),
            "pdf_extraction": {"status": rebuilt_extraction.status, "warnings": rebuilt_extraction.warnings},
            "bundle": {"items": bundle.item_count, **review},
            "context": {"profiles": context["profiles"], "types": sorted({item["type"] for item in context["items"]})},
            "rebuild": {"indexed_documents": rebuilt_index, "extraction_rebuilt": rebuilt_extraction.status == "ready"},
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
