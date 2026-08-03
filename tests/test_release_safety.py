from __future__ import annotations

import os
import threading
from pathlib import Path

import pytest

from global_memory.capture_policy import CapturePolicy
from global_memory.errors import ValidationError
from global_memory.writer_lock import RepositoryWriterLock


def resolver_for(address: str):
    return lambda _host, _port: [(None, None, None, None, (address, 443))]


@pytest.mark.parametrize("url,address", [
    ("http://localhost/", "127.0.0.1"),
    ("http://127.0.0.1/", "127.0.0.1"),
    ("http://[::1]/", "::1"),
    ("http://169.254.169.254/", "169.254.169.254"),
    ("http://private.test/", "10.0.0.7"),
    ("http://private-v6.test/", "fd00::7"),
    ("http://mapped.test/", "::ffff:127.0.0.1"),
])
def test_capture_policy_rejects_non_public_url_targets(url: str, address: str) -> None:
    with pytest.raises(ValidationError):
        CapturePolicy(resolver=resolver_for(address)).validate_url(url)


def test_capture_policy_permits_public_url_and_checks_domain_allowlist() -> None:
    CapturePolicy(resolver=resolver_for("8.8.8.8"), domain_allowlist=frozenset({"public.test"})).validate_url("https://public.test/x")
    with pytest.raises(ValidationError):
        CapturePolicy(resolver=resolver_for("8.8.8.8"), domain_allowlist=frozenset({"public.test"})).validate_url("https://other.test/x")


def test_private_network_override_never_opens_metadata_or_loopback() -> None:
    CapturePolicy(
        resolver=resolver_for("10.0.0.7"), allow_private_network=True,
    ).validate_url("http://private.test/")
    for address in ("127.0.0.1", "169.254.169.254", "::1"):
        with pytest.raises(ValidationError):
            CapturePolicy(
                resolver=resolver_for(address), allow_private_network=True,
            ).validate_url("http://blocked.test/")


def test_capture_policy_resolves_symlink_before_import_root_check() -> None:
    checkout = Path.cwd()
    root = checkout / "release"
    outside = checkout / "README.md"
    link = root / ".capture-policy-escape-test"
    try:
        os.symlink(outside, link)
    except OSError:
        pytest.skip("symlink unavailable in this environment")
    try:
        with pytest.raises(ValidationError):
            CapturePolicy(import_roots=(root,)).validate_file(link)
    finally:
        link.unlink(missing_ok=True)


def test_capture_policy_allows_file_inside_explicit_root() -> None:
    root = Path.cwd() / "release"
    target = root / "synthetic_vault.yaml"
    assert CapturePolicy(import_roots=(root,)).validate_file(target) == target.resolve()


def test_writer_lock_fails_nonblocking_and_allows_reentrant_use() -> None:
    first = RepositoryWriterLock(Path.cwd())
    second = RepositoryWriterLock(Path.cwd())
    result: list[bool] = []
    with first.acquire():
        with first.acquire():
            def contend() -> None:
                try:
                    with second.acquire():
                        pass
                except ValidationError:
                    result.append(True)
            thread = threading.Thread(target=contend)
            thread.start()
            thread.join()
    assert result == [True]
