"""Conservative network and local-file admission policy for Agent capture."""
from __future__ import annotations

import ipaddress
import socket
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .errors import ValidationError


Resolver = Callable[[str, int], list[Any]]


@dataclass(frozen=True)
class ValidatedTarget:
    scheme: str
    host: str
    port: int
    addresses: tuple[str, ...]


def _default_resolver(host: str, port: int) -> list[Any]:
    return socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)


def _blocked_address(value: str, *, allow_private_network: bool = False) -> bool:
    address = ipaddress.ip_address(value)
    # IPv4-mapped IPv6 must be judged using its IPv4 meaning.
    if isinstance(address, ipaddress.IPv6Address) and address.ipv4_mapped:
        address = address.ipv4_mapped
    if any((address.is_loopback, address.is_link_local, address.is_multicast,
            address.is_unspecified, address.is_reserved)):
        return True
    return address.is_private and not allow_private_network


@dataclass(frozen=True)
class CapturePolicy:
    """Explicit policy; no network or local-file capability is implied by MCP."""

    domain_allowlist: frozenset[str] = frozenset()
    import_roots: tuple[Path, ...] = ()
    allow_private_network: bool = False
    max_redirects: int = 5
    resolver: Resolver = field(default=_default_resolver, compare=False, repr=False)

    def resolve_url(self, url: str) -> ValidatedTarget:
        parts = urlsplit(url)
        if parts.scheme.lower() not in {"http", "https"} or not parts.hostname:
            raise ValidationError("capture policy only permits HTTP(S) URLs")
        host = parts.hostname.rstrip(".").casefold()
        if self.domain_allowlist and host not in self.domain_allowlist:
            raise ValidationError(f"capture policy rejects domain outside allowlist: {host}")
        try:
            port = parts.port or (443 if parts.scheme.lower() == "https" else 80)
        except ValueError as exc:
            raise ValidationError("capture policy rejects invalid URL port") from exc
        try:
            addresses = self.resolver(host, port)
        except OSError as exc:
            raise ValidationError(f"capture policy DNS resolution failed for {host}: {exc}") from exc
        if not addresses:
            raise ValidationError(f"capture policy DNS resolution returned no addresses for {host}")
        validated: list[str] = []
        for entry in addresses:
            ip = str(entry[4][0])
            if _blocked_address(ip, allow_private_network=self.allow_private_network):
                raise ValidationError(f"capture policy rejects non-public address for {host}: {ip}")
            if ip not in validated:
                validated.append(ip)
        return ValidatedTarget(parts.scheme.lower(), host, port, tuple(validated))

    def validate_url(self, url: str) -> None:
        self.resolve_url(url)

    def validate_file(self, path: Path | str, *, allow_unsafe: bool = False) -> Path:
        resolved = Path(path).expanduser().resolve(strict=True)
        if not resolved.is_file():
            raise ValidationError(f"local capture target is not a file: {resolved}")
        lowered = {part.casefold() for part in resolved.parts}
        sensitive_names = {".ssh", ".aws", ".gnupg", ".env", "credentials", "credential", "tokens", "token", "secrets", "secret"}
        if not allow_unsafe and (lowered & sensitive_names or any(part.casefold().endswith((".pem", ".key", ".p12")) for part in resolved.parts)):
            raise ValidationError("capture policy rejects a common sensitive file or directory")
        if allow_unsafe:
            return resolved
        roots = tuple(root.expanduser().resolve() for root in self.import_roots)
        if not roots:
            raise ValidationError("local capture requires an explicit import root; use the CLI dangerous override only for intentional manual import")
        if not any(_is_relative_to(resolved, root) for root in roots):
            raise ValidationError("local capture target is outside configured import roots")
        return resolved


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False
