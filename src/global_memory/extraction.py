from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from .errors import NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .repository import Repository, now_iso, sha256_bytes
from .wechat import extract_js_content_html


EXTRACTOR_VERSION = "1.0"
WECHAT_EXTRACTOR = "wechat-article-v1"


class _ArticleHTMLParser(HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer", "aside", "noscript", "svg"}
    BLOCK = {"title", "h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "blockquote", "pre", "article", "main"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.current: list[str] = []
        self.blocks: list[str] = []
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in self.SKIP:
            self.skip_depth += 1
        if self.skip_depth:
            return
        if tag == "title":
            self.in_title = True
        if tag in self.BLOCK and self.current:
            self._flush()
        if tag == "br":
            self.current.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.SKIP and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.in_title = False
        if tag in self.BLOCK:
            self._flush()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = unescape(data)
        if self.in_title:
            self.title += text
        self.current.append(text)

    def _flush(self) -> None:
        text = re.sub(r"[ \t\r\f\v]+", " ", "".join(self.current))
        text = re.sub(r" *\n *", "\n", text).strip()
        if text and (not self.blocks or self.blocks[-1] != text):
            self.blocks.append(text)
        self.current = []

    def result(self) -> str:
        self._flush()
        title = re.sub(r"\s+", " ", self.title).strip()
        blocks = self.blocks
        if title and (not blocks or blocks[0] != title):
            blocks = [f"# {title}", *blocks]
        return "\n\n".join(blocks).strip()


def decode_text(payload: bytes, declared: str = "") -> tuple[str | None, str | None, list[str]]:
    warnings: list[str] = []
    match = re.search(r"charset=([\w.\-]+)", declared, re.I)
    candidates = [match.group(1)] if match else []
    candidates.extend(["utf-8-sig", "utf-8", "gb18030", "big5"])
    seen: set[str] = set()
    for encoding in candidates:
        normalized = encoding.lower()
        if normalized in seen:
            continue
        seen.add(normalized)
        try:
            text = payload.decode(encoding)
            if normalized not in {"utf-8", "utf-8-sig"}:
                warnings.append(f"使用编码降级解码: {encoding}")
            return text, encoding, warnings
        except (UnicodeDecodeError, LookupError):
            continue
    return None, None, ["无法使用 UTF-8、GB18030 或 Big5 解码文本"]


@dataclass(frozen=True)
class ExtractionResult:
    extraction_id: str
    extraction_path: str
    status: str
    extractor: str
    warnings: list[str]
    rebuilt: bool


class ExtractionService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "data" / "derived" / "extractions"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("extraction-*.md")) if self.directory.exists() else []

    def find(self, extraction_id: str) -> tuple[Path, dict[str, Any], str]:
        for path in self.documents():
            metadata, body = read_document(path)
            if metadata.get("extraction_id") == extraction_id:
                return path, metadata, body
        raise NotFoundError(f"未找到 extraction: {extraction_id}")

    def latest_for_source(self, source_id: str, create: bool = False) -> tuple[Path, dict[str, Any], str]:
        _, source, _ = self.repository.find_document(source_id)
        matches: list[tuple[Path, dict[str, Any], str]] = []
        for path in self.documents():
            metadata, body = read_document(path)
            if (
                metadata.get("source_id") == source_id
                and metadata.get("input_sha256") == source.get("content_sha256")
                and metadata.get("status") == "ready"
            ):
                matches.append((path, metadata, body))
        if matches:
            return sorted(matches, key=lambda item: str(item[1].get("extracted_at", "")))[-1]
        if create:
            result = self.extract(source_id)
            if result.status != "ready":
                raise ValidationError("source extraction 未就绪: " + "; ".join(result.warnings))
            return self.find(result.extraction_id)
        raise NotFoundError(f"source 没有可用 extraction: {source_id}")

    def _extract_pdf(self, payload: bytes) -> tuple[str, int | None, list[str], str]:
        try:
            from pypdf import PdfReader
        except ImportError:
            return "", None, ["PDF extractor 未安装；请运行 pip install -e .[pdf]"], "error"
        warnings: list[str] = []
        try:
            from io import BytesIO
            reader = PdfReader(BytesIO(payload))
            pages: list[str] = []
            nonempty = 0
            for number, page in enumerate(reader.pages, start=1):
                text = (page.extract_text() or "").strip()
                if text:
                    nonempty += 1
                else:
                    warnings.append(f"第 {number} 页没有可提取文本；可能是扫描页")
                pages.append(f"<!-- page: {number} -->\n\n{text}")
            if reader.pages and nonempty == 0:
                warnings.append("PDF 所有页面均无可提取文本；本轮不执行 OCR")
            return "\n\n".join(pages).rstrip(), len(reader.pages), warnings, "ready"
        except Exception as exc:
            return "", None, [f"PDF 提取失败: {exc}"], "error"

    def _extract_html(self, decoded: str, *, prefer_wechat: bool = False) -> tuple[str, str, list[str], str]:
        fragment = extract_js_content_html(decoded) if prefer_wechat else None
        if fragment is None and ("id=\"js_content\"" in decoded or "id='js_content'" in decoded):
            fragment = extract_js_content_html(decoded)
        parser = _ArticleHTMLParser()
        try:
            parser.feed(fragment or decoded)
            text = parser.result()
            extractor = WECHAT_EXTRACTOR if fragment else "html-article-v1"
            if not text:
                return "", extractor, ["HTML 未提取到正文"], "error"
            return text, extractor, [], "ready"
        except Exception as exc:
            return "", "html-article-v1", [f"HTML 提取失败: {exc}"], "error"

    def _extract_payload(
        self,
        payload: bytes,
        mime: str,
        content_type: str,
        *,
        source_kind: str = "",
    ) -> tuple[str, str, int | None, list[str], str, str | None]:
        if mime == "application/pdf":
            text, pages, warnings, status = self._extract_pdf(payload)
            return text, "pypdf", pages, warnings, status, None
        decoded, encoding, warnings = decode_text(payload, content_type)
        if decoded is None:
            return "", "text-decoder", None, warnings, "error", None
        if mime in {"text/html", "application/xhtml+xml"} or re.search(r"<html\b|<!doctype\s+html", decoded[:1000], re.I):
            text, extractor, warnings, status = self._extract_html(
                decoded, prefer_wechat=source_kind == "wechat"
            )
            return text, extractor, None, warnings, status, encoding
        return decoded, "text-decoder", None, warnings, "ready", encoding

    def extract(self, source_id: str, rebuild: bool = False) -> ExtractionResult:
        source_path, source, _ = self.repository.find_document(source_id)
        if source.get("type") != "source":
            raise ValidationError(f"extract 只接受 source: {source_id}")
        raw_path = self.repository.resolve_inside(str(source["raw_content_path"]))
        payload = raw_path.read_bytes()
        input_sha = sha256_bytes(payload)
        if input_sha != source.get("content_sha256"):
            raise ValidationError("extraction 输入与 source content_sha256 不一致")
        mime = str(source.get("mime_type") or source.get("content_type", "")).split(";", 1)[0].lower()
        content_type = str(source.get("content_type", mime))
        text, extractor, page_count, warnings, status, encoding = self._extract_payload(
            payload, mime, content_type, source_kind=str(source.get("source_kind", ""))
        )
        if re.search(r"[\ud800-\udfff]", text):
            # Some PDF extractors can return invalid Unicode scalar values.  Raw
            # bytes remain immutable; only this rebuildable text view is made
            # valid UTF-8 so downstream triage can record the extraction result.
            text = re.sub(r"[\ud800-\udfff]", "\ufffd", text)
            warnings.append("Extraction contained unpaired Unicode surrogates; replaced with U+FFFD in the derived view")
        digest = hashlib.sha256(
            f"{source_id}\n{input_sha}\n{extractor}\n{EXTRACTOR_VERSION}".encode("utf-8")
        ).hexdigest()
        extraction_id = f"extraction_{digest[:24]}"
        path = self.directory / f"extraction-{extraction_id}.md"
        if path.exists() and not rebuild:
            metadata, _ = read_document(path)
            return ExtractionResult(
                extraction_id, self.repository.rel(path), str(metadata["status"]),
                str(metadata["extractor"]), list(metadata.get("warnings", [])), False,
            )
        timestamp = now_iso()
        for old_path in self.documents():
            if old_path == path:
                continue
            old, old_body = read_document(old_path)
            if old.get("source_id") == source_id and old.get("status") == "ready" and old.get("input_sha256") != input_sha:
                old["status"] = "stale"
                old["updated_at"] = timestamp
                atomic_write_text(old_path, render_document(old, old_body))
        metadata = {
            "extraction_id": extraction_id, "source_id": source_id,
            "content_id": source.get("content_id"), "input_sha256": input_sha,
            "extractor": extractor, "extractor_version": EXTRACTOR_VERSION,
            "extracted_at": timestamp, "updated_at": timestamp,
            "mime_type": mime or "application/octet-stream", "encoding": encoding,
            "language": "und", "page_count": page_count,
            "character_count": len(text), "status": status, "warnings": warnings,
            "source_path": self.repository.rel(source_path),
        }
        atomic_write_text(path, render_document(metadata, text))
        return ExtractionResult(extraction_id, self.repository.rel(path), status, extractor, warnings, rebuild)

    def verify_span(self, extraction_id: str, start: int, end: int, original_text: str) -> bool:
        _, metadata, body = self.find(extraction_id)
        if metadata.get("status") != "ready" or not (0 <= start < end <= len(body)):
            return False
        return body[start:end] == original_text
