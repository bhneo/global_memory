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
from .markdown import read_document, render_document
from .repository import Repository, now_iso, sha256_bytes


TRACKING_PARAMETERS = {"fbclid", "gclid", "dclid", "mc_cid", "mc_eid", "igshid"}


def _display_extension(content_type: str, original_filename: str = "") -> str:
    """Return presentation metadata only; it never participates in object identity."""
    mime = content_type.split(";", 1)[0].strip().lower()
    guessed = mimetypes.guess_extension(mime, strict=False)
    if guessed:
        return guessed
    return Path(original_filename).suffix.lower() if original_filename else ""


def _content_disposition_filename(value: str) -> str:
    match = re.search(r"filename\*?=(?:UTF-8''|\")?([^\";]+)", value, re.I)
    return Path(match.group(1).strip()).name if match else ""


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
    version_number: int = 1
    previous_source_id: str | None = None
    refresh_proposal_id: str | None = None


class CaptureService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def _versions_for_locator(self, canonical_locator: str) -> list[tuple[Path, dict[str, object]]]:
        versions: list[tuple[Path, dict[str, object]]] = []
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            if metadata.get("canonical_locator") == canonical_locator:
                versions.append((path, metadata))
        return sorted(
            versions,
            key=lambda item: (int(item[1].get("version_number", 1)), str(item[1].get("captured_at", ""))),
        )

    def _result_for_existing(
        self,
        path: Path,
        metadata: dict[str, object],
        *,
        refresh_proposal_id: str | None = None,
    ) -> CaptureResult:
        raw_path = str(metadata["raw_content_path"])
        return CaptureResult(
            source_id=str(metadata["id"]),
            content_id=str(metadata.get("content_id") or Path(raw_path).stem),
            source_path=self.repository.rel(path),
            raw_content_path=raw_path,
            duplicate_source=True,
            duplicate_content=True,
            version_number=int(metadata.get("version_number", 1)),
            previous_source_id=metadata.get("previous_version_id") or None,
            refresh_proposal_id=refresh_proposal_id,
        )

    def _ensure_refresh_proposal(
        self,
        previous_source_id: str | None,
        new_source_id: str,
    ) -> str | None:
        if not previous_source_id:
            return None
        from .proposals import ProposalService

        return ProposalService(self.repository).create_source_refresh(
            previous_source_id, new_source_id
        ).proposal_id

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
        original_filename: str = "",
        refresh: bool = False,
    ) -> CaptureResult:
        self.repository.ensure_initialized()
        versions = self._versions_for_locator(canonical_locator)
        latest_path, latest = versions[-1] if versions else (None, None)
        if latest is not None and not refresh:
            self.repository.append_event(
                "capture-events",
                {"event": "duplicate-source", "source_id": latest["id"], "locator": original_locator},
            )
            return self._result_for_existing(latest_path, latest)

        digest = sha256_bytes(content)
        if latest is not None and digest == latest.get("content_sha256"):
            proposal_id = self._ensure_refresh_proposal(
                latest.get("previous_version_id") or None, str(latest["id"])
            )
            self.repository.append_event(
                "capture-events",
                {
                    "event": "refresh-unchanged", "source_id": latest["id"],
                    "locator": original_locator, "content_sha256": digest,
                },
            )
            return self._result_for_existing(
                latest_path, latest, refresh_proposal_id=proposal_id
            )

        content_id = f"content_{digest}"
        source_digest = hashlib.sha256(f"{kind}\n{canonical_locator}".encode("utf-8")).hexdigest()
        source_family_id = f"source_family_{source_digest[:24]}"
        version_number = int(latest.get("version_number", 1)) + 1 if latest else 1
        source_id = (
            f"source_{source_digest[:24]}"
            if version_number == 1
            else f"source_{source_digest[:12]}_v{version_number:04d}_{digest[:12]}"
        )
        decoded = _decode_text(content, content_type)
        raw_path = self.repository.content_object_path(digest)
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
            "mime_type": content_type.split(";", 1)[0].strip().lower(),
            "original_filename": original_filename,
            "display_extension": _display_extension(content_type, original_filename),
            "source_family_id": source_family_id,
            "version_number": version_number,
            "previous_version_id": latest.get("id") if latest else None,
        }
        body = (
            f"# {metadata['title']}\n\n"
            f"> 原始内容：[{self.repository.rel(raw_path)}]({Path(os.path.relpath(raw_path, source_path.parent)).as_posix()})\n\n"
            "## 来源版本\n\n"
            f"- Family：`{source_family_id}`\n"
            f"- Version：`{version_number}`\n"
            f"- Previous：`{metadata['previous_version_id'] or 'none'}`\n\n"
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
                "duplicate_content": not created_content, "version_number": version_number,
                "previous_source_id": metadata["previous_version_id"],
            },
        )
        self.repository.rebuild_index()
        refresh_proposal_id = self._ensure_refresh_proposal(
            metadata["previous_version_id"], source_id
        )
        return CaptureResult(
            source_id=source_id,
            content_id=content_id,
            source_path=self.repository.rel(source_path),
            raw_content_path=self.repository.rel(raw_path),
            duplicate_source=False,
            duplicate_content=not created_content,
            version_number=version_number,
            previous_source_id=metadata["previous_version_id"],
            refresh_proposal_id=refresh_proposal_id,
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
            original_filename=source_path.name,
        )

    def capture_url(self, url: str, comment: str = "", refresh: bool = False) -> CaptureResult:
        canonical = canonicalize_url(url)
        versions = self._versions_for_locator(canonical)
        if versions and not refresh:
            latest_path, latest = versions[-1]
            self.repository.append_event(
                "capture-events", {"event": "duplicate-source", "source_id": latest["id"], "locator": url}
            )
            return self._result_for_existing(latest_path, latest)
        request = urllib.request.Request(url, headers={"User-Agent": "GlobalMemory/0.2 (+local-first)"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                content = response.read(20_000_001)
                if len(content) > 20_000_000:
                    raise ValidationError("URL 内容超过第一版 20 MB 限制")
                content_type = response.headers.get("Content-Type", "application/octet-stream")
                original_filename = _content_disposition_filename(
                    response.headers.get("Content-Disposition", "")
                )
                final_url = response.geturl()
        except OSError as exc:
            raise ValidationError(f"URL 获取失败: {exc}") from exc
        decoded = _decode_text(content, content_type)
        title = _html_title(decoded or "") or urlsplit(final_url).hostname or "网页来源"
        return self._write_source(
            kind="web", original_locator=url, canonical_locator=canonicalize_url(final_url),
            content=content, title=title, comment=comment, import_method="cli-url",
            content_type=content_type, original_filename=original_filename, refresh=refresh,
        )

    def capture(self, target: str, comment: str = "", refresh: bool = False) -> CaptureResult:
        if urlsplit(target).scheme.lower() in {"http", "https"}:
            return self.capture_url(target, comment, refresh=refresh)
        if refresh:
            raise ValidationError("--refresh 当前只支持 HTTP(S) URL")
        return self.capture_file(target, comment)
