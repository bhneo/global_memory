from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .errors import ValidationError
from .extraction import ExtractionService
from .markdown import atomic_write_text
from .repository import Repository, now_iso


AVAILABILITY_STATUSES = {
    "available", "deleted", "access_denied", "login_required", "anti_bot",
    "partial", "unknown",
}
CONTENT_QUALITIES = {
    "valid", "boilerplate_only", "too_short", "corrupted",
    "extraction_failed", "degraded",
}
SOURCE_AUTHORITIES = {
    "primary", "official", "peer_reviewed", "preprint", "secondary_analysis",
    "industry_commentary", "marketing", "social_post", "anecdotal", "unknown",
}

_DELETED = ("内容已删除", "该内容已被发布者删除", "此内容因违规无法查看", "page has been removed")
_LOGIN = ("登录后继续", "请先登录", "扫码登录", "sign in to continue", "login required")
_ANTI_BOT = ("访问过于频繁", "环境异常", "安全验证", "captcha", "verify you are human", "anti-bot")
_ACCESS = ("access denied", "无权访问", "forbidden", "permission denied")
_BOILERPLATE = ("微信公众平台", "javascript is disabled", "enable javascript", "点击阅读全文")
_PRIMARY_LOCATOR = re.compile(
    r"https?://(?:arxiv\.org/(?:abs|pdf)/[^\s\]\)]+|doi\.org/[^\s\]\)]+|github\.com/[^\s\]\)]+)",
    re.I,
)


@dataclass(frozen=True)
class QualityAssessment:
    source_id: str
    assessed_at: str
    availability_status: str
    content_quality: str
    extraction_quality: str
    source_authority: str
    compile_allowed: bool
    reasons: list[str]
    character_count: int
    primary_source_locators: list[str]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


class SourceQualityService:
    """Deterministic, rebuildable source/extraction quality gate."""

    def __init__(self, repository: Repository, minimum_article_chars: int = 120):
        self.repository = repository
        self.minimum_article_chars = minimum_article_chars
        self.directory = repository.root / "data/derived/quality"

    def path_for(self, source_id: str) -> Path:
        return self.directory / f"{source_id}.json"

    @staticmethod
    def _contains(text: str, patterns: tuple[str, ...]) -> bool:
        lowered = text.casefold()
        return any(pattern.casefold() in lowered for pattern in patterns)

    @staticmethod
    def _authority(source: dict[str, Any]) -> str:
        explicit = str(source.get("source_authority", ""))
        if explicit in SOURCE_AUTHORITIES:
            return explicit
        locator = str(source.get("canonical_locator", ""))
        host = urlsplit(locator).hostname or ""
        if host.endswith("arxiv.org"):
            return "preprint"
        if host.endswith(("doi.org", "acm.org", "ieee.org", "nature.com", "science.org")):
            return "peer_reviewed"
        if host.endswith(("github.com", "github.io")):
            return "official"
        if source.get("source_kind") == "wechat":
            return "secondary_analysis"
        if source.get("source_kind") == "personal-notes":
            return "primary"
        return "unknown"

    def assess(self, source_id: str, *, persist: bool = True) -> QualityAssessment:
        _, source, _ = self.repository.find_document(source_id)
        if source.get("type") != "source":
            raise ValidationError(f"quality gate 只接受 source: {source_id}")
        reasons: list[str] = []
        try:
            _, extraction, text = ExtractionService(self.repository).latest_for_source(source_id, create=True)
        except Exception as exc:
            extraction = {"status": "error", "warnings": [str(exc)], "character_count": 0}
            text = ""
        normalized = re.sub(r"\s+", " ", text).strip()
        status = str(extraction.get("status", "error"))
        warnings = [str(item) for item in extraction.get("warnings", [])]
        availability = "available"
        quality = "valid"
        extraction_quality = "good"
        if status != "ready":
            quality, extraction_quality = "extraction_failed", "failed"
            reasons.append("extraction status is not ready")
        elif self._contains(normalized, _DELETED):
            availability, quality = "deleted", "boilerplate_only"
            reasons.append("matched deleted-content marker")
        elif self._contains(normalized, _LOGIN):
            availability, quality = "login_required", "boilerplate_only"
            reasons.append("matched login wall marker")
        elif self._contains(normalized, _ANTI_BOT):
            availability, quality = "anti_bot", "boilerplate_only"
            reasons.append("matched anti-bot marker")
        elif self._contains(normalized, _ACCESS):
            availability, quality = "access_denied", "boilerplate_only"
            reasons.append("matched access-denied marker")
        elif not normalized:
            quality = "too_short"
            reasons.append("no usable extracted text")
        elif len(normalized) < self.minimum_article_chars and source.get("source_kind") in {"web", "wechat"}:
            quality = "too_short"
            reasons.append(f"article text shorter than {self.minimum_article_chars} characters")
        else:
            boilerplate_hits = sum(marker.casefold() in normalized.casefold() for marker in _BOILERPLATE)
            if boilerplate_hits >= 2 and len(normalized) < self.minimum_article_chars * 3:
                quality = "boilerplate_only"
                reasons.append("template markers dominate short extraction")
        if status == "ready" and warnings and quality == "valid":
            quality, extraction_quality = "degraded", "degraded"
            reasons.extend(warnings)
        locators = sorted(set(_PRIMARY_LOCATOR.findall(text)))
        allowed = availability in {"available", "partial"} and quality in {"valid", "degraded"}
        result = QualityAssessment(
            source_id=source_id, assessed_at=now_iso(), availability_status=availability,
            content_quality=quality, extraction_quality=extraction_quality,
            source_authority=self._authority(source), compile_allowed=allowed,
            reasons=reasons, character_count=len(normalized), primary_source_locators=locators,
        )
        if persist:
            self.directory.mkdir(parents=True, exist_ok=True)
            atomic_write_text(self.path_for(source_id), json.dumps(result.as_dict(), ensure_ascii=False, indent=2, sort_keys=True) + "\n")
            self.repository.append_event("source-processing-events", {
                "event": "quality-checked", "source_id": source_id,
                "availability_status": availability, "content_quality": quality,
                "compile_allowed": allowed,
            })
        return result

    def load(self, source_id: str) -> QualityAssessment | None:
        path = self.path_for(source_id)
        if not path.exists():
            return None
        return QualityAssessment(**json.loads(path.read_text(encoding="utf-8")))
