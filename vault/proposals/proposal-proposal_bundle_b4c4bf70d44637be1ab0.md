---
id: "proposal_bundle_b4c4bf70d44637be1ab0"
type: "proposal"
status: "migrated"
title: "Compile bundle：DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting"
created_at: "2026-07-20T12:48:07+08:00"
updated_at: "2026-07-20T12:48:08+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_513a527cb4d410e4f94a9bb5"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-d-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_00e9389a8c89d1b7b3eba377"
input_sha256: "2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_b1b62d103e0a768399664d9d", "target_path": "vault/knowledge/concepts/concept_b1b62d103e0a768399664d9d-simulator-validated-single-view-demonstration-transfer.md", "base_sha256": null, "candidate_sha256": "a4a9ab8a4d3579c42b9950e905f3c4674b49e8b3c59db3de1bf794848666153c", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b4c4bf70d44637be1ab0-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_b1b62d103e0a768399664d9d.md", "working_at": "2026-07-20T12:48:08+08:00"}]
existing_context: [{"id": "input_ab5a33edd49eec243cb3862f", "type": "input", "title": "DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting", "path": "vault/inputs/input-input_ab5a33edd49eec243cb3862f.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…A Simulation-in-the-Loop Toolkit for Single-View [Human] Demonstration Retargeting\n\nInput Episode for `source_513a527cb4d410e4f94a9bb5`. The…", "match_reason": "metadata:title"}, {"id": "concept_5b49f7afd60ba18d35ca58e8", "type": "concept", "title": "触觉对齐的人到机器人接触迁移", "path": "vault/memory/concept/concept_5b49f7afd60ba18d35ca58e8.md", "status": "working", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "# 触觉对齐的人到机器人接触迁移\n\n在人类示范中同步手部运动学、物体状态和全手压力，把接触形成、接触区域时序、力幅值与安全约束作为独立监督和评测维度。该范式纠正纯运动学模仿的接触缺口，但跨本体时不应假设人类接触分布可无条件照搬。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_513a527cb4d410e4f94a9bb5"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-d-20260720`
- Extraction：`extraction_00e9389a8c89d1b7b3eba377`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_b1b62d103e0a768399664d9d-simulator-validated-single-view-demonstration-transfer.md
@@ -0,0 +1,20 @@
+---
+id: "concept_b1b62d103e0a768399664d9d"
+type: "concept"
+status: "proposal"
+title: "Simulator-validated single-view demonstration transfer"
+created_at: "2026-07-20T12:48:07+08:00"
+updated_at: "2026-07-20T12:48:07+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_513a527cb4d410e4f94a9bb5"]
+relations: [{"type": "derived_from", "target_id": "source_513a527cb4d410e4f94a9bb5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-d-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_513a527cb4d410e4f94a9bb5"
+reflection_context: {"reflection_ids": ["reflection_65fb6fe12e2291077f28900c"], "importance": "high", "changed_belief": "Single-view video transfer is best treated as a closed inference-and-validation loop. Perception proposes geometry and phase, planning checks embodiment feasibility, and simulation backtracks when the proposed motion fails.", "surprising": "The paper reports transfer from three real demonstrations with repeated trials, yet the most consequential bottleneck is still basic object tracking under occlusion rather than policy scale.", "connections": [{"shared_mechanism": "Like TELEDEXTER, DemoBridge preserves task-level geometric relations rather than directly retargeting every human joint.", "boundary": "Evidence is limited to a single arm, small demonstration counts, and the tested objects and scenes. Occlusion, reconstruction error, and bimanual interaction remain outside the demonstrated boundary.", "difference": "TELEDEXTER is live hand-object teleoperation with an RL contact controller; DemoBridge is offline single-view trajectory reconstruction with collision planning and simulator validation."}], "open_questions": ["Can phase validation remain reliable when objects are deformable, heavily occluded, or jointly manipulated by two arms?"]}
+---
+
+# Simulator-validated single-view demonstration transfer
+
+Convert a single-view human demonstration into a robot plan through stereo reconstruction, object tracking, collision-aware whole-arm planning, and simulator phase validation with backtracking. The simulator is a feasibility filter, not proof that the reconstructed plan will execute reliably in reality.
```
