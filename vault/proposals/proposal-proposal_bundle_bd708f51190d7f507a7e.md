---
id: "proposal_bundle_bd708f51190d7f507a7e"
type: "proposal"
status: "migrated"
title: "Compile bundle：2607.13017v1.pdf"
created_at: "2026-07-20T12:32:57+08:00"
updated_at: "2026-07-20T12:32:57+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ef80ef223077ef0855660839"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-b-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "2607.13017v1.pdf"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_d1d7aa64246eb77c47a4358f"
input_sha256: "a4dea6542be553e1bda65617085861650dab686b84014d6f50473f6d432a0283"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_59f92bcb786f695ddcd47f7f", "target_path": "vault/knowledge/concepts/concept_59f92bcb786f695ddcd47f7f-视频原生的光流动作接口.md", "base_sha256": null, "candidate_sha256": "c4cb25f77e71d58127a50ad8594c1eeac26a07bebce5fcf0b4da0c1555a70ec5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_bd708f51190d7f507a7e-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_59f92bcb786f695ddcd47f7f.md", "working_at": "2026-07-20T12:32:57+08:00"}]
existing_context: [{"id": "input_5f966e5ff15622edf0829255", "type": "input", "title": "2607.13017v1.pdf", "path": "vault/inputs/input-input_5f966e5ff15622edf0829255.md", "status": "active", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "…The immutable Source remains authoritative.\n\n# [2607.13017v1.pdf]\n\n> 原始内容：[vault/raw/objects/sha256/a4/de/a4dea6542be553e1bda65617085861650dab686b84014d6f50473f6d432a0283](../objects/sha256…", "match_reason": "metadata:title"}, {"id": "claim_parameter_symmetry_conserved_gradient_flow_20260716", "type": "claim", "title": "Parameter-space symmetry implies conserved quantities in gradient flow", "path": "vault/memory/claim/claim_parameter_symmetry_conserved_gradient_flow_20260716.md", "status": "trusted", "source_ids": ["source_6ae6c4bef52010f96ddb3dbf", "source_dbfef5ee180346812d6d9a99"], "snippet": "Parameter-space symmetry implies conserved quantities in gradient [flow].", "match_reason": "metadata:title"}, {"id": "reflection_0dd383cc873ce81c0afd3d06", "type": "reflection", "title": "EGOWAM：跨本体迁移应优先共享世界变化而不是动作", "path": "vault/reflections/reflection-reflection_0dd383cc873ce81c0afd3d06.md", "status": "active", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "…通用 VLA 侧重统一策略输入输出接口，EGOWAM 侧重用辅助世界预测通道改变共享骨干接收人类数据的方式\n\n## Conflicts\n\n- 世界表示越抽象越可能丢失接触级控制细节；3D [flow] 与 DINO 的优势可能随任务分布变化\n\n## Open questions\n\n- 什么 world target 能同时保留接触动力学…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ef80ef223077ef0855660839"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：2607.13017v1.pdf

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-b-20260720`
- Extraction：`extraction_d1d7aa64246eb77c47a4358f`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_59f92bcb786f695ddcd47f7f-视频原生的光流动作接口.md
@@ -0,0 +1,20 @@
+---
+id: "concept_59f92bcb786f695ddcd47f7f"
+type: "concept"
+status: "proposal"
+title: "视频原生的光流动作接口"
+created_at: "2026-07-20T12:32:57+08:00"
+updated_at: "2026-07-20T12:32:57+08:00"
+aliases: ["Video-native optical-flow action interface", "FlowWAM", "光流动作表示"]
+tags: []
+domains: ["embodied-ai", "world-action-model", "optical-flow", "action-representation"]
+confidence: "high"
+source_ids: ["source_ef80ef223077ef0855660839"]
+relations: [{"type": "derived_from", "target_id": "source_ef80ef223077ef0855660839", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "二者都统一动作生成与未来状态建模；光流接口规定共享的运动表征，双系统 WAM 规定快慢推理分工。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_ef80ef223077ef0855660839"
+reflection_context: {"reflection_ids": ["reflection_a74b334857543499d8111c64"], "importance": "high", "changed_belief": "此前容易把 World Action Model 的动作接口理解为数值动作或抽象 latent；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。", "surprising": "跨 50 个 RoboTwin 任务，预测光流误差与策略成功率呈较强负相关（论文报告 Pearson r=-0.81），说明收益至少部分跟随运动表示质量，而不只是下游解码器捷径。", "connections": [{"shared_mechanism": "与双系统 World Action Model 都让视频动力学模型同时支持动作生成和未来状态建模。", "boundary": "光流主要描述可见像素运动，遮挡、接触力、不可见关节和跨长时程意图并不天然可观测；论文结果也不能证明跨本体动作解码无需额外适配。", "difference": "双系统 WAM 强调快慢推理分工；FlowWAM 的核心贡献是用光流统一动作与视频模态，并由专门解码器恢复数值控制。"}], "open_questions": ["在遮挡、移动相机和接触丰富任务中，光流误差是否仍能稳定预测动作可执行性？"]}
+---
+
+# 视频原生的光流动作接口
+
+用连续光流视频表示机器人动作，使同一稠密运动接口既可由世界动作模型生成并解码为控制，也可作为未来视频生成条件，还能从无动作标签视频提取预训练监督。该接口覆盖可见跨帧运动，但不天然包含力、遮挡后状态或完整本体动力学。
```
