---
id: "proposal_bundle_8198bb05589e4ee0b976"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:34:05+08:00"
updated_at: "2026-07-20T12:34:05+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_4df1017326dd7cc4786f4218"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-b-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_1d5e9ba42e986397f6b1524a"
input_sha256: "34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_3d739e54fe54c8a5205d2301", "target_path": "vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md", "base_sha256": "fb03f0f8e95784beed18e05b54d1b97e713219e22131fe59db5581d14276fa0c", "candidate_sha256": "37ee9c15a02e9f31b6fd10de1d82f014243a0788355121a1e53ae835aa6272e8", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_8198bb05589e4ee0b976-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_8198bb05589e4ee0b976-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "reflection_a4abd223b36c137fb9bd6ae4", "type": "reflection", "title": "Mixture of Frames：动作分布复杂度部分来自坐标系选择", "path": "vault/reflections/reflection-reflection_a4abd223b36c137fb9bd6ae4.md", "status": "active", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "# Mixture of [Frames]：动作分布复杂度部分来自坐标系选择\n\n## Why important\n\nMoF 说明同一操作动作在夹爪、基座或相对轨迹坐标系中具有不同统计复杂度，且最合适坐标系会随任务阶段变化；策略可以并行去噪多个 frame 专家而非固定一个表示。\n\n## What changed\n\n此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture…", "match_reason": "metadata:title"}, {"id": "concept_3d739e54fe54c8a5205d2301", "type": "concept", "title": "多坐标系同步动作去噪", "path": "vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md", "status": "working", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "# 多坐标系同步动作去噪\n\n在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选…", "match_reason": "metadata:aliases"}, {"id": "concept_sensor_conditional_expert_routing", "type": "concept", "title": "传感器条件化专家路由", "path": "vault/memory/concept/concept_sensor_conditional_expert_routing.md", "status": "working", "source_ids": ["source_5d8306b5caf7371feeacbc09"], "snippet": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "match_reason": "metadata:domains"}, {"id": "reflection_0078f804e87c7ed12f88876d", "type": "reflection", "title": "B-spline Policy：把动作表示与执行速度从固定采样率中解耦", "path": "vault/reflections/reflection-reflection_0078f804e87c7ed12f88876d.md", "status": "active", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# B-spline [Policy]：把动作表示与执行速度从固定采样率中解耦\n\n## Why important\n\nBSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。\n\n## What changed\n\n此前动作块加速常被理解为少重规划或少执行几步…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_4df1017326dd7cc4786f4218"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-b-20260720`
- Extraction：`extraction_1d5e9ba42e986397f6b1524a`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md
+++ candidate:vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_3d739e54fe54c8a5205d2301"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "多坐标系同步动作去噪"
 created_at: "2026-07-20T12:33:09+08:00"
-updated_at: "2026-07-20T12:33:09+08:00"
+updated_at: "2026-07-20T12:34:05+08:00"
 aliases: ["Synchronized multi-frame action denoising", "Mixture of Frames Policy", "MoF", "多 Frame 扩散策略"]
 tags: []
 domains: ["embodied-ai", "diffusion-policy", "coordinate-frames", "bimanual-manipulation"]
 confidence: "high"
 source_ids: ["source_4df1017326dd7cc4786f4218"]
-relations: [{"type": "derived_from", "target_id": "source_4df1017326dd7cc4786f4218", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "二者都处理动作参考系差异；前者在单一本体内融合多 frame，后者在多本体间寻求统一动作接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_4df1017326dd7cc4786f4218", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "二者都处理动作参考系差异；前者在单一本体内融合多 frame，后者在多本体间寻求统一动作接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "二者都处理动作参考系差异；前者在单一本体内融合多 frame，后者在多本体间寻求统一动作接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}]
 change_reason: "compile bundle from source_4df1017326dd7cc4786f4218"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_a4abd223b36c137fb9bd6ae4"], "importance": "high", "changed_belief": "此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture axis，表明动作模型难度有一部分是参数化造成的，而非任务本身不可约复杂度。", "surprising": "MoF 在部分任务上超过按整项任务选择最佳单 frame 的 oracle；路由权重随阶段变化较大的任务收益更高，论文报告两者具有正相关。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都需要把不同运动学参考系映射到统一的可执行动作接口。", "boundary": "MoF 依赖预先给定的候选 frame 和准确的 proprioceptive frame transform，当前证据集中于双臂移动操作，不能直接推出未知本体上的 frame 自动发现。", "difference": "跨本体通用 VLA 追求不同机器人共享输入输出协议；MoF 在单个机器人内部同时维护多个坐标系专家，并在同一扩散轨迹上融合噪声预测。"}], "open_questions": ["能否从数据中发现任务相关 frame，并把 frame transform 不确定性传播进扩散去噪与执行风险？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-daily-batch-b-20260720"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-daily-batch-b-20260720"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_8955521c41a78fff2979"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_8955521c41a78fff2979-concept-1.md"
-origin_candidate_sha256: "fb18d0827371558432fc8b750d6c66b58b8615daeeec82e38effa632551509e1"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 多坐标系同步动作去噪
```
