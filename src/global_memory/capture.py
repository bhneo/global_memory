from __future__ import annotations

import hashlib
import html
import mimetypes
import os
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .errors import ValidationError
from .markdown import render_document
from .repository import Repository, now_iso, sha256_bytes


TRACKING_PARAMETERS = {"fbclid", "gclid", "dclid", "mc_cid", "mc_eid", "igshid"}


def canonicalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    if parts.scheme.lower() not in {"http", "https"} or not parts.hostname:
        raise ValidationError(f"不是有效的 HTTP(S) URL: {url}")
    scheme = parts.scheme.lower()
    host = parts.hostname.lower()
    port = parts.port
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_PARAMETERS
    ]
    return urlunsplit((scheme, host, parts.path or "/", urlencode(sorted(query)), ""))


def _decode_text(content: bytes, content_type: str = "") -> str | None:
    match = re.search(r"charset=([\w.\-]+)", content_type, re.I)
    candidates = [match.group(1)] if match else []
    candidates.extend(["utf-8", "utf-8-sig"])
    for encoding in candidates:
        try:
            return content.decode(encoding)
        except (UnicodeDecodeError, LookupError):
            continue
    return None


def _html_title(text: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
    if not match:
        return None
    title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", match.group(1))).strip()
    return html.unescape(title)[:200] or None


def _preview(text: str | None, limit: int = 600) -> str:
    if not text:
        return "（二进制内容；请通过相对路径打开原始文件。）"
    plain = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", text, flags=re.I | re.S)
    plain = html.unescape(re.sub(r"<[^>]+>", " ", plain))
    plain = re.sub(r"\s+", " ", plain).strip()
    return plain[:limit] + ("…" if len(plain) > limit else "")


@dataclass(frozen=True)
class CaptureResult:
    source_id: str
    content_id: str
    source_path: str
    raw_content_path: str
    duplicate_source: bool
    duplicate_content: bool


class CaptureService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def _existing_locator(self, canonical_locator: str) -> tuple[str, str, str] | None:
        for path in self.repository.source_documents():
            from .markdown import read_document

            metadata, _ = read_document(path)
            if metadata.get("canonical_locator") == canonical_locator:
                return metadata["id"], self.repository.rel(path), metadata["raw_content_path"]
        return None

    def _write_source(
        self,
        *,
        kind: str,
        original_locator: str,
        canonical_locator: str,
        content: bytes,
        title: str,
        author: str = "",
        published_at: str | None = None,
        comment: str = "",
        import_method: str,
        content_type: str = "text/plain; charset=utf-8",
    ) -> CaptureResult:
        self.repository.ensure_initialized()
        existing = self._existing_locator(canonical_locator)
        if existing:
            source_id, source_path, raw_path = existing
            self.repository.append_event(
                "capture-events",
                {"event": "duplicate-source", "source_id": source_id, "locator": original_locator},
            )
            return CaptureResult(
                source_id, Path(raw_path).stem, source_path, raw_path, True, True
            )

        digest = sha256_bytes(content)
        content_id = f"content_{digest}"
        source_digest = hashlib.sha256(f"{kind}\n{canonical_locator}".encode("utf-8")).hexdigest()
        source_id = f"source_{source_digest[:24]}"
        decoded = _decode_text(content, content_type)
        is_text = decoded is not None and (
            content_type.lower().startswith("text/") or kind == "personal-notes"
        )
        if is_text:
            extension = ".html" if "html" in content_type.lower() else ".txt"
            raw_path = self.repository.root / "vault" / "raw" / kind / "content" / f"{content_id}{extension}"
        else:
            extension = Path(urlsplit(original_locator).path).suffix or mimetypes.guess_extension(content_type.split(";", 1)[0]) or ".bin"
            raw_path = self.repository.root / "vault" / "raw" / kind / "blobs" / f"{content_id}{extension}"
        created_content = self.repository.immutable_write(raw_path, content)

        timestamp = now_iso()
        source_path = self.repository.root / "vault" / "raw" / kind / f"source-{source_id}.md"
        metadata = {
            "id": source_id,
            "type": "source",
            "status": "captured",
            "title": title[:200] or source_id,
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": [],
            "relations": [],
            "source_kind": kind,
            "original_title": title[:200],
            "author": author,
            "original_locator": original_locator,
            "canonical_locator": canonical_locator,
            "captured_at": timestamp,
            "published_at": published_at,
            "content_sha256": digest,
            "content_id": content_id,
            "raw_content_path": self.repository.rel(raw_path),
            "save_reason": comment,
            "import_method": import_method,
            "processing_status": "inbox",
            "content_type": content_type,
        }
        body = (
            f"# {metadata['title']}\n\n"
            f"> 原始内容：[{self.repository.rel(raw_path)}](./{raw_path.relative_to(source_path.parent).as_posix()})\n\n"
            "## 保存理由\n\n"
            f"{comment or '（未填写）'}\n\n"
            "## 内容预览\n\n"
            f"{_preview(decoded)}\n"
        )
        self.repository.immutable_write(source_path, render_document(metadata, body).encode("utf-8"))
        self.repository.append_event(
            "capture-events",
            {
                "event": "captured", "source_id": source_id, "content_id": content_id,
                "source_path": self.repository.rel(source_path), "raw_content_path": self.repository.rel(raw_path),
                "duplicate_content": not created_content,
            },
        )
        self.repository.rebuild_index()
        return CaptureResult(
            source_id=source_id,
            content_id=content_id,
            source_path=self.repository.rel(source_path),
            raw_content_path=self.repository.rel(raw_path),
            duplicate_source=False,
            duplicate_content=not created_content,
        )

    def capture_text(self, text: str, comment: str = "", title: str = "人工输入") -> CaptureResult:
        if not text or not text.strip():
            raise ValidationError("文本内容不能为空")
        content = text.encode("utf-8")
        digest = sha256_bytes(content)
        locator = f"text:sha256:{digest}"
        return self._write_source(
            kind="personal-notes", original_locator=locator, canonical_locator=locator,
            content=content, title=title, comment=comment, import_method="cli-text",
        )

    def capture_file(self, path: Path | str, comment: str = "") -> CaptureResult:
        source_path = Path(path).expanduser().resolve()
        if not source_path.is_file():
            raise ValidationError(f"本地文件不存在: {source_path}")
        try:
            source_path.relative_to(self.repository.root)
        except ValueError:
            pass
        canonical = f"file:{os.path.normcase(str(source_path))}"
        content_type = mimetypes.guess_type(source_path.name)[0] or "application/octet-stream"
        return self._write_source(
            kind="files", original_locator=str(source_path), canonical_locator=canonical,
            content=source_path.read_bytes(), title=source_path.name, comment=comment,
            import_method="cli-file", content_type=content_type,
        )

    def capture_url(self, url: str, comment: str = "") -> CaptureResult:
        canonical = canonicalize_url(url)
        existing = self._existing_locator(canonical)
        if existing:
            source_id, source_path, raw_path = existing
            self.repository.append_event(
                "capture-events", {"event": "duplicate-source", "source_id": source_id, "locator": url}
            )
            return CaptureResult(source_id, Path(raw_path).stem, source_path, raw_path, True, True)
        request = urllib.request.Request(url, headers={"User-Agent": "GlobalMemory/0.1 (+local-first)"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                content = response.read(20_000_001)
                if len(content) > 20_000_000:
                    raise ValidationError("URL 内容超过第一版 20 MB 限制")
                content_type = response.headers.get("Content-Type", "application/octet-stream")
                final_url = response.geturl()
        except OSError as exc:
            raise ValidationError(f"URL 获取失败: {exc}") from exc
        decoded = _decode_text(content, content_type)
        title = _html_title(decoded or "") or urlsplit(final_url).hostname or "网页来源"
        return self._write_source(
            kind="web", original_locator=url, canonical_locator=canonicalize_url(final_url),
            content=content, title=title, comment=comment, import_method="cli-url",
            content_type=content_type,
        )

    def capture(self, target: str, comment: str = "") -> CaptureResult:
        if urlsplit(target).scheme.lower() in {"http", "https"}:
            return self.capture_url(target, comment)
        return self.capture_file(target, comment)
