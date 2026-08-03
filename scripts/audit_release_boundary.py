"""Read-only audit of tracked files and optional Git history for vault exposure."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

SENSITIVE = ("vault/", "system/", "data/", "objects/", "artifacts/", "artifacts-local/")

def git(root: Path, *args: str) -> list[str]:
    completed = subprocess.run(["git", "-C", str(root), *args], text=True, capture_output=True, check=True)
    return [line for line in completed.stdout.splitlines() if line]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--history", action="store_true", help="also scan every reachable commit path (read-only; can be slow)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    tracked = git(root, "ls-files")
    content_findings = []
    marker = re.compile(r"BEGIN (?:[A-Z ]+ )?PRIVATE KEY|(?:api[_-]?key|access[_-]?token|secret)\s*[:=]", re.I)
    for relative in tracked:
        path = root / relative
        if path.is_file() and path.stat().st_size <= 1_000_000:
            try:
                if marker.search(path.read_text(encoding="utf-8", errors="ignore")):
                    content_findings.append(relative)
            except OSError:
                pass
    report = {
        "head_sensitive_paths": [path for path in tracked if path.startswith(SENSITIVE)],
        "head_potential_secret_markers": content_findings,
        "history_sensitive_paths": [],
        "ignore_cannot_retract_history": "A .gitignore rule only affects untracked future files; it cannot remove tracked HEAD content or any reachable Git history.",
        "recommended_split": "Create a new public engine repository from scripts/build_release.py output; retain the existing repository as the private Vault and do not rewrite it until owners complete a separate secret/history review.",
    }
    if args.history:
        names = git(root, "log", "--all", "--pretty=format:", "--name-only")
        report["history_sensitive_paths"] = sorted(set(path for path in names if path.startswith(SENSITIVE)))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
