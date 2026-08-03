"""Build a non-destructive public Galois release from an explicit allowlist."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path


def load_manifest(root: Path) -> dict:
    return json.loads((root / "release" / "release-manifest.json").read_text(encoding="utf-8"))


def selected_paths(root: Path, manifest: dict) -> list[Path]:
    selected: list[Path] = []
    excluded = set(manifest["exclude"])
    for entry in manifest["include"]:
        path = root / entry
        if not path.exists():
            if entry == "LICENSE":
                continue
            raise RuntimeError(f"allowlisted path is missing: {entry}")
        candidates = [path] if path.is_file() else [item for item in path.rglob("*") if item.is_file()]
        for item in candidates:
            if item.is_symlink():
                raise RuntimeError(f"release refuses symbolic link: {item.relative_to(root)}")
            resolved = item.resolve(strict=True)
            try:
                resolved.relative_to(root.resolve())
            except ValueError as exc:
                raise RuntimeError(f"release path escapes checkout: {item}") from exc
            relative = item.relative_to(root).as_posix()
            if "__pycache__/" in relative or relative.endswith((".pyc", ".pyo")):
                continue
            if relative not in excluded and not any(relative.startswith(value.rstrip("/") + "/") for value in excluded):
                selected.append(item)
    return sorted(set(selected))


def verify(paths: list[Path], root: Path, manifest: dict) -> None:
    prefixes = tuple(manifest["sensitive_prefixes"])
    violations = [path.relative_to(root).as_posix() for path in paths if path.relative_to(root).as_posix().startswith(prefixes)]
    if violations:
        raise RuntimeError("sensitive release paths: " + ", ".join(violations))
    included_top = {Path(value).parts[0] for value in manifest["include"]}
    excluded_top = set(manifest["known_excluded_top_levels"])
    actual_top = {item.name for item in root.iterdir()}
    unknown = sorted(actual_top - included_top - excluded_top)
    if unknown:
        raise RuntimeError("unknown top-level release boundary entries: " + ", ".join(unknown))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("dist") / "galois-public")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = load_manifest(root)
    paths = selected_paths(root, manifest)
    verify(paths, root, manifest)
    records = [{"path": item.relative_to(root).as_posix(), "sha256": hashlib.sha256(item.read_bytes()).hexdigest(), "bytes": item.stat().st_size} for item in paths]
    report = {"dry_run": args.dry_run, "files": records, "count": len(records), "license_present": (root / "LICENSE").exists()}
    if not args.dry_run:
        # A new temp directory is prepared before a replace; the checkout is never touched.
        with tempfile.TemporaryDirectory(prefix="galois-release-") as temporary:
            stage = Path(temporary) / "galois-public"
            for item in paths:
                target = stage / item.relative_to(root)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target)
            (stage / "release-manifest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            if args.output.exists():
                raise RuntimeError(f"refusing to overwrite existing release output: {args.output}")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(stage, args.output)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
