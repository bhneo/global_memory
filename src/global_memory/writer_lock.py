"""Repository-wide, OS-released writer lock.

The lock is deliberately advisory: every Galois writer takes it at its public
boundary, while journals continue to provide crash recovery for multi-file work.
"""
from __future__ import annotations

import os
import threading
import time
from collections.abc import Iterator
from contextlib import contextmanager
from functools import wraps
from typing import Any, BinaryIO
from pathlib import Path

from .errors import ValidationError


def repository_writer(method: Any) -> Any:
    """Apply the shared writer boundary to a public mutating service method."""
    @wraps(method)
    def locked(self: Any, *args: Any, **kwargs: Any) -> Any:
        repository = getattr(self, "repository", self)
        with repository.writer_lock():
            return method(self, *args, **kwargs)
    return locked


class RepositoryWriterLock:
    _local = threading.local()

    def __init__(self, root: Path):
        self.path = root / "system" / "locks" / "repository-write.lock"

    @contextmanager
    def acquire(self, *, timeout: float = 0.0) -> Iterator[None]:
        key = str(self.path.resolve())
        held = getattr(self._local, "held", {})
        if key in held:
            held[key] += 1
            self._local.held = held
            try:
                yield
            finally:
                held[key] -= 1
                if not held[key]:
                    del held[key]
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        handle = self.path.open("r+b") if self.path.exists() else self.path.open("w+b")
        deadline = time.monotonic() + max(timeout, 0.0)
        try:
            while True:
                try:
                    self._lock(handle)
                    break
                except OSError as exc:
                    if time.monotonic() >= deadline:
                        raise ValidationError("repository is busy: another writer holds system/locks/repository-write.lock") from exc
                    time.sleep(min(0.05, max(0.0, deadline - time.monotonic())))
            held[key] = 1
            self._local.held = held
            yield
        finally:
            if key in getattr(self._local, "held", {}):
                del self._local.held[key]
                self._unlock(handle)
            handle.close()

    @staticmethod
    def _lock(handle: BinaryIO) -> None:
        if os.name == "nt":
            import msvcrt
            handle.seek(0)
            if handle.read(1) == b"":
                handle.write(b"0")
                handle.flush()
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)

    @staticmethod
    def _unlock(handle: BinaryIO) -> None:
        if os.name == "nt":
            import msvcrt
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
