from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any

from .errors import ValidationError


def _yaml_value(value: Any) -> str:
    """Emit a conservative YAML subset using JSON-compatible values."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


def render_document(metadata: dict[str, Any], body: str) -> str:
    lines = ["---"]
    lines.extend(f"{key}: {_yaml_value(value)}" for key, value in metadata.items())
    lines.extend(["---", "", body.rstrip(), ""])
    return "\n".join(lines)


def parse_document_text(text: str) -> tuple[dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValidationError("Markdown 文件缺少 YAML Frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValidationError("Markdown Frontmatter 未闭合") from exc
    metadata: dict[str, Any] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValidationError(f"无法解析 Frontmatter 行: {line}")
        key, raw = line.split(":", 1)
        key, raw = key.strip(), raw.strip()
        try:
            metadata[key] = json.loads(raw)
        except json.JSONDecodeError:
            metadata[key] = raw
    body = "\n".join(lines[end + 1 :]).lstrip("\n")
    return metadata, body


def read_document(path: Path) -> tuple[dict[str, Any], str]:
    return parse_document_text(path.read_text(encoding="utf-8"))


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)


def write_document(path: Path, metadata: dict[str, Any], body: str) -> None:
    atomic_write_text(path, render_document(metadata, body))
