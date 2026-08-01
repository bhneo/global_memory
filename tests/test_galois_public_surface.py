from __future__ import annotations

import json
from pathlib import Path

from global_memory.cli import build_parser
from global_memory.mcp_server import SERVER_INFO


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_READ_TOOLS = [
    "memory_capabilities",
    "memory_context",
    "memory_search",
    "memory_show",
    "memory_source",
]


def test_public_cli_and_mcp_identity_are_galois() -> None:
    assert build_parser().prog == "galois"
    assert SERVER_INFO["name"] == "galois-agent-gateway"


def test_host_manifest_is_read_only_and_machine_independent() -> None:
    manifest_path = ROOT / "adapters" / "hosts" / "galois.mcp-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert manifest["product"] == "galois"
    assert manifest["server_id"] == "galois"
    assert manifest["required_tools"] == REQUIRED_READ_TOOLS
    assert manifest["default_authority"] == "read-only"
    assert manifest["validated_platforms"] == ["windows"]
    assert manifest["template_scope"] == "machine-path-neutral-windows"
    assert manifest["acceptance"][
        "server_tools_must_match_required_tools_exactly"
    ] is True
    assert manifest["acceptance"]["host_namespacing_allowed"] is True
    assert manifest["acceptance"]["host_mapping_must_be_one_to_one"] is True
    assert manifest["acceptance"]["host_mapping_must_not_add_write_tools"] is True
    assert manifest["acceptance"]["static_config_is_not_live_proof"] is True
    assert manifest["acceptance"]["bounded_probe"]["budget_exhausted_is_valid"] is True


def test_host_templates_have_no_developer_specific_paths_or_legacy_server_key() -> None:
    templates = [
        "claude-desktop.mcp.json",
        "codex.config.toml",
        "hermes.config.yaml",
        "openclaw.mcp-server.json",
        "openhuman.config.toml",
    ]
    for name in templates:
        text = (ROOT / "adapters" / "hosts" / name).read_text(encoding="utf-8")
        assert "bhneo" not in text.lower()
        assert "miniconda3" not in text.lower()
        assert '"global-memory"' not in text
        assert 'name = "global-memory"' not in text
        assert "{{GALOIS_PYTHON}}" in text
        assert "{{GALOIS_ROOT}}" in text


def test_current_entry_docs_do_not_instruct_the_deprecated_cli() -> None:
    for name in ["README.md", "AGENTS.md", "CLAUDE.md", "INDEX.md"]:
        text = (ROOT / name).read_text(encoding="utf-8")
        assert ".\\scripts\\gm.ps1" not in text
        assert "`gm " not in text


def test_readme_preserves_capability_and_release_boundaries() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    compact = " ".join(text.split())

    assert "Your AI can read thousands of documents" not in text
    assert "original Source material" not in text
    assert "reviewed, path-neutral templates" not in text
    assert "machine-path-neutral Windows templates" in text
    assert "server-level tools/list" in text
    assert "host may prefix or wrap tool names" in text
    assert "no accepted active cross-direction synthesis yet" in compact
    assert "formal open-source distribution" in compact
    assert "project's research vault or any user's knowledge" in compact
    assert "subject to that provider's privacy and retention terms" in compact
