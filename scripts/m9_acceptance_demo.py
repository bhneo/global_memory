from __future__ import annotations

import argparse
import json
from pathlib import Path

from global_memory.capture import CaptureService
from global_memory.context import ContextPackService
from global_memory.markdown import atomic_write_text, render_document
from global_memory.mcp_server import ReadOnlyMemoryTools
from global_memory.metrics import ProjectMetricsService
from global_memory.repository import Repository, now_iso, sha256_bytes
from global_memory.research import (
    ActivationService, ResearchAnnotationService, ResearchDigestService,
    ResearchMapService,
)


def _object(repo: Repository, object_id: str, object_type: str, title: str, body: str) -> None:
    roots = {"project": "vault/action/projects", "question": "vault/frontier/questions", "analogy": "vault/frontier/analogies"}
    path = repo.root / roots[object_type] / f"{object_id}.md"
    timestamp = now_iso()
    metadata = {
        "id": object_id, "type": object_type, "status": "confirmed", "title": title,
        "created_at": timestamp, "updated_at": timestamp, "aliases": [], "tags": [],
        "domains": [], "confidence": "unknown", "source_ids": [], "relations": [],
    }
    atomic_write_text(path, render_document(metadata, body))


def _truth_snapshot(repo: Repository) -> dict[str, object]:
    metrics = ProjectMetricsService(repo).collect()
    hashes = {
        repo.rel(path): sha256_bytes(path.read_bytes())
        for path in sorted(repo.canonical_documents())
    }
    return {
        "working": metrics["working"], "trusted": metrics["trusted"],
        "canonical": metrics["canonical"], "canonical_hashes": hashes,
        "receipts": metrics["consolidation_receipts"],
    }


def run(root: Path) -> dict[str, object]:
    if root.exists() and any(root.iterdir()):
        raise SystemExit(f"refusing to reuse non-empty demo root: {root}")
    repo = Repository(root)
    repo.init()
    capture = CaptureService(repo)
    sources = [
        capture._write_source(
            kind="web", original_locator=f"https://example.test/m9/{name}",
            canonical_locator=f"https://example.test/m9/{name}", content=body.encode("utf-8"),
            title=title, comment="M9 synthetic acceptance", import_method="m9-acceptance",
            content_type="text/plain; charset=utf-8",
        )
        for name, title, body in (
            ("skill", "具身技能下沉", "昂贵规划可以沉淀为低成本技能，并需要可逆失效条件。"),
            ("habit", "人类习惯形成", "重复决策可以转化为自动化习惯，但环境变化需要重新控制。"),
            ("view", "数据库物化视图", "昂贵查询可被物化为低成本读取，并依靠失效与刷新保持正确。"),
        )
    ]
    _object(repo, "project_embodied_agent", "project", "embodied-agent", "具身智能研究")
    _object(repo, "project_scientific_memory", "project", "scientific-memory", "科研记忆研究")
    _object(repo, "question_skill_compilation", "question", "技能何时应该固化", "何时把昂贵规划固化为技能？")
    _object(repo, "analogy_computation_compression", "analogy", "计算压缩类比", "技能、习惯和物化视图都压缩重复计算，但失效条件不同。")
    repo.rebuild_index()
    before = _truth_snapshot(repo)

    annotations = ResearchAnnotationService(repo)
    capture_intent = annotations.create(
        "capture_intent", target_ids=[sources[0].source_id],
        why_saved="它可能解释 Agent 如何把昂贵规划固化成技能。",
        what_surprised_me="技能固化可能需要可逆和失效机制。",
        possible_connections=["人类习惯形成", "数据库物化视图"],
        research_projects=["embodied-agent"], personal_salience="high",
    )
    interesting = annotations.create(
        "connection_feedback", target_ids=["analogy_computation_compression"],
        feedback_label="interesting",
        feedback_note="共同结构是压缩重复昂贵计算，但三种系统的失效条件不同。",
        research_projects=["embodied-agent", "scientific-memory"],
    )
    forced = annotations.create(
        "connection_feedback", target_ids=["analogy_computation_compression"],
        feedback_label="forced", feedback_note="只共享压缩一词时没有共同机制。",
        research_projects=["scientific-memory"],
    )
    route_pack = ContextPackService(repo).build(
        "技能何时应该固化", profiles=["research"], project="embodied-agent",
        relation_depth=1,
    )
    activation = ActivationService(repo)
    used = activation.record(
        sources[0].source_id, kind="used", project_id="embodied-agent",
        reason="用于技能固化架构决策", event_id="activation_m9_demo_source_used",
    )
    cited = activation.record(
        "question_skill_compilation", kind="cited", project_id="embodied-agent",
        reason="用于形成下一步研究问题", event_id="activation_m9_demo_question_cited",
    )
    digest = ResearchDigestService(repo).write()
    research_map = ResearchMapService(repo).build()

    activation_path = repo.root / "system" / "logs" / "activation-events.jsonl"
    activation_before_mcp = activation_path.read_bytes()
    mcp_context = ReadOnlyMemoryTools(repo).call(
        "memory_context", {"question": "技能固化", "profile": "research", "token_budget": 600}
    )
    activation_after_mcp = activation_path.read_bytes()
    after = _truth_snapshot(repo)
    return {
        "ok": before == after and activation_before_mcp == activation_after_mcp,
        "sources": [item.source_id for item in sources],
        "annotations": [capture_intent["id"], interesting["id"], forced["id"]],
        "route_trace": route_pack.route_trace,
        "activation": {"used": used, "cited": cited, "top": activation.aggregate()},
        "research_digest": digest,
        "research_map": research_map,
        "truth_before": before,
        "truth_after": after,
        "receipt_validity_unchanged": before["receipts"] == after["receipts"],
        "canonical_hashes_unchanged": before["canonical_hashes"] == after["canonical_hashes"],
        "mcp_read_only": activation_before_mcp == activation_after_mcp,
        "mcp_selected": len(mcp_context.get("items", [])),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.root.resolve())
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
