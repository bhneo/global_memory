from __future__ import annotations

import html
import re
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .errors import ValidationError


WECHAT_ARTICLE_HOST = "mp.weixin.qq.com"
WECHAT_ARTICLE_PATH_RE = re.compile(r"^/s(?:/|$)")
WECHAT_IDENTITY_PARAMS = {"__biz", "mid", "idx", "sn"}
WECHAT_TRACKING_PARAMETERS = {"fbclid", "gclid", "dclid", "mc_cid", "mc_eid", "igshid", "scene", "sessionid", "chksm"}
WECHAT_MOBILE_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
    "MicroMessenger/8.0.42(0x18002a29) NetType/WIFI Language/zh_CN"
)


@dataclass(frozen=True)
class WechatArticleMetadata:
    title: str
    author: str
    account_name: str
    published_at: str | None


@dataclass(frozen=True)
class WechatFetchResult:
    content: bytes
    content_type: str
    final_url: str
    metadata: WechatArticleMetadata


def is_wechat_article_url(url: str) -> bool:
    parts = urlsplit(url.strip())
    return (
        parts.scheme.lower() in {"http", "https"}
        and (parts.hostname or "").lower() == WECHAT_ARTICLE_HOST
        and bool(WECHAT_ARTICLE_PATH_RE.match(parts.path or ""))
    )


def canonicalize_wechat_url(url: str) -> str:
    if not is_wechat_article_url(url):
        raise ValidationError(f"不是有效的微信公众号文章 URL: {url}")
    parts = urlsplit(url.strip())
    host = (parts.hostname or "").lower()
    path = parts.path or "/"
    if re.fullmatch(r"/s/[^/]+", path):
        return urlunsplit(("https", host, path, "", ""))
    query = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key.lower() in WECHAT_IDENTITY_PARAMS
    ]
    if not query:
        query = [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith("utm_") and key.lower() not in WECHAT_TRACKING_PARAMETERS
        ]
    return urlunsplit(("https", host, "/s", urlencode(sorted(query)), ""))


def _meta_content(text: str, key: str) -> str | None:
    pattern = rf'<meta[^>]+(?:property|name)=["\']{re.escape(key)}["\'][^>]+content=["\'](.*?)["\']'
    match = re.search(pattern, text, re.I | re.S)
    if not match:
        pattern = rf'<meta[^>]+content=["\'](.*?)["\'][^>]+(?:property|name)=["\']{re.escape(key)}["\']'
        match = re.search(pattern, text, re.I | re.S)
    if not match:
        return None
    value = html.unescape(re.sub(r"\s+", " ", match.group(1))).strip()
    return value[:200] or None


def _element_text(text: str, element_id: str) -> str | None:
    match = re.search(
        rf'<[^>]+id=["\']{re.escape(element_id)}["\'][^>]*>(.*?)</[^>]+>',
        text,
        re.I | re.S,
    )
    if not match:
        return None
    value = html.unescape(re.sub(r"<[^>]+>", " ", match.group(1)))
    value = re.sub(r"\s+", " ", value).strip()
    return value[:200] or None


def _script_var(text: str, name: str) -> str | None:
    patterns = [
        rf'{name}\s*=\s*htmlDecode\s*\(\s*"([^"]+)"',
        rf'{name}\s*=\s*"([^"]+)"',
        rf"var\s+{name}\s*=\s*'([^']+)'",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I)
        if match:
            value = html.unescape(match.group(1)).strip()
            return value[:200] or None
    return None


def _published_at_from_html(text: str) -> str | None:
    for pattern in (
        r'var\s+ct\s*=\s*"?(\d{10})"?',
        r'"create_time"\s*:\s*"?(\d{10})"?',
        r'publish_time\s*=\s*"?(\d{10})"?',
    ):
        match = re.search(pattern, text, re.I)
        if not match:
            continue
        timestamp = int(match.group(1))
        return datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone().isoformat(timespec="seconds")
    rich_time = _element_text(text, "publish_time")
    if rich_time:
        return rich_time
    return None


def parse_wechat_metadata(text: str) -> WechatArticleMetadata:
    title = (
        _meta_content(text, "og:title")
        or _element_text(text, "activity-name")
        or _script_var(text, "msg_title")
        or ""
    )
    author = _meta_content(text, "og:article:author") or _script_var(text, "author") or ""
    account_name = (
        _element_text(text, "js_name")
        or _script_var(text, "nickname")
        or _script_var(text, "nick_name")
        or _meta_content(text, "og:site_name")
        or ""
    )
    return WechatArticleMetadata(
        title=title,
        author=author,
        account_name=account_name,
        published_at=_published_at_from_html(text),
    )


def fetch_wechat_article(url: str) -> WechatFetchResult:
    if not is_wechat_article_url(url):
        raise ValidationError(f"不是有效的微信公众号文章 URL: {url}")
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": WECHAT_MOBILE_UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            content = response.read(20_000_001)
            if len(content) > 20_000_000:
                raise ValidationError("微信文章内容超过第一版 20 MB 限制")
            content_type = response.headers.get("Content-Type", "text/html; charset=utf-8")
            final_url = response.geturl()
    except OSError as exc:
        raise ValidationError(f"微信文章获取失败: {exc}") from exc
    decoded = content.decode("utf-8", errors="replace")
    return WechatFetchResult(
        content=content,
        content_type=content_type,
        final_url=final_url,
        metadata=parse_wechat_metadata(decoded),
    )


def extract_js_content_html(text: str) -> str | None:
    match = re.search(
        r'<div[^>]*\bid=["\']js_content["\'][^>]*>(.*)</div>',
        text,
        re.I | re.S,
    )
    if not match:
        return None
    return match.group(1).strip()
