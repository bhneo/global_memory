"""Policy-bound HTTP transport that pins the DNS answer used by the socket."""
from __future__ import annotations

import http.client
import socket
import ssl
from dataclasses import dataclass
from urllib.parse import urljoin, urlsplit, urlunsplit

from .capture_policy import CapturePolicy
from .errors import ValidationError


@dataclass(frozen=True)
class FetchResult:
    content: bytes
    headers: http.client.HTTPMessage
    final_url: str


class _PinnedHTTPConnection(http.client.HTTPConnection):
    def __init__(self, host: str, port: int, address: str, *, timeout: float):
        super().__init__(host, port, timeout=timeout)
        self._address = address

    def connect(self) -> None:
        self.sock = socket.create_connection((self._address, self.port), self.timeout)


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(self, host: str, port: int, address: str, *, timeout: float):
        self._ssl_context = ssl.create_default_context()
        super().__init__(host, port, context=self._ssl_context, timeout=timeout)
        self._address = address

    def connect(self) -> None:
        raw = socket.create_connection((self._address, self.port), self.timeout)
        self.sock = self._ssl_context.wrap_socket(raw, server_hostname=self.host)


def fetch_url(
    url: str,
    policy: CapturePolicy,
    *,
    headers: dict[str, str] | None = None,
    timeout: float = 20,
    max_bytes: int = 20_000_000,
) -> FetchResult:
    current = url
    request_headers = {"User-Agent": "GlobalMemory/0.2 (+local-first)", **(headers or {})}
    for redirect_count in range(policy.max_redirects + 1):
        target = policy.resolve_url(current)
        parts = urlsplit(current)
        request_path = urlunsplit(("", "", parts.path or "/", parts.query, ""))
        response: http.client.HTTPResponse | None = None
        last_error: OSError | None = None
        for address in target.addresses:
            connection = (
                _PinnedHTTPSConnection(target.host, target.port, address, timeout=timeout)
                if target.scheme == "https"
                else _PinnedHTTPConnection(target.host, target.port, address, timeout=timeout)
            )
            try:
                host_header = target.host
                if target.port not in {80, 443}:
                    host_header = f"{host_header}:{target.port}"
                connection.request("GET", request_path, headers={"Host": host_header, **request_headers})
                response = connection.getresponse()
                break
            except OSError as exc:
                last_error = exc
                connection.close()
        if response is None:
            raise last_error or OSError("no validated address was reachable")
        if response.status in {301, 302, 303, 307, 308}:
            location = response.headers.get("Location")
            response.close()
            if not location:
                raise ValidationError("capture redirect is missing Location")
            if redirect_count >= policy.max_redirects:
                raise ValidationError(f"capture policy redirect limit exceeded ({policy.max_redirects})")
            current = urljoin(current, location)
            continue
        content = response.read(max_bytes + 1)
        response_headers = response.headers
        response.close()
        if len(content) > max_bytes:
            raise ValidationError(f"URL content exceeds the {max_bytes} byte limit")
        return FetchResult(content, response_headers, current)
    raise ValidationError("capture redirect limit exceeded")
