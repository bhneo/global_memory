---
id: "proposal_bundle_5c56317b0a0df19a19fc"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:18:13+08:00"
updated_at: "2026-07-19T12:18:13+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_4ac7cf9f4fce43551683a04b"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_86d431fcc2035d3dcf479bca"
input_sha256: "1d7a7bf7394675cae2b8ac02a51348972c77c68f3ed39d2e19432a339ccb0d58"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_adaptive_interleaved_multimodal_planning", "target_path": "vault/knowledge/concepts/concept_adaptive_interleaved_multimodal_planning-自适应交错多模态规划.md", "base_sha256": null, "candidate_sha256": "385eec27b29bf7abb766c2f77ca4e6b6ceb82d911b0f0d4479715e2f44b05056", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_5c56317b0a0df19a19fc-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_adaptive_interleaved_multimodal_planning.md", "working_at": "2026-07-19T12:18:13+08:00"}]
existing_context: [{"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:domains"}, {"id": "concept_vla_action_evaluation_distillation", "type": "concept", "title": "VLA 动作评估蒸馏", "path": "vault/memory/concept/concept_vla_action_evaluation_distillation.md", "status": "working", "source_ids": ["source_ff90ad99bd47043e812cce9e"], "snippet": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_4ac7cf9f4fce43551683a04b"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_86d431fcc2035d3dcf479bca`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_adaptive_interleaved_multimodal_planning-自适应交错多模态规划.md
@@ -0,0 +1,20 @@
+---
+id: "concept_adaptive_interleaved_multimodal_planning"
+type: "concept"
+status: "proposal"
+title: "自适应交错多模态规划"
+created_at: "2026-07-19T12:18:13+08:00"
+updated_at: "2026-07-19T12:18:13+08:00"
+aliases: ["adaptive interleaved vision-language planning", "adaptive multimodal planning", "APIVOT"]
+tags: []
+domains: ["embodied-ai", "robot-planning", "multimodal-reasoning", "long-horizon"]
+confidence: "medium"
+source_ids: ["source_4ac7cf9f4fce43551683a04b"]
+relations: [{"type": "derived_from", "target_id": "source_4ac7cf9f4fce43551683a04b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都区分低频语义结构与几何/动作执行；APIVOT 在单个规划轨迹内交错模态，DSWAM 则在规划器与 WAM 执行器之间分工。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "tension_internal_reasoning_external_skills", "reason": "APIVOT 把几何验证内化为模型的视觉思维，明确落在该 tension 的内部推理一侧，并保留与外部验证式技能图比较的研究边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_4ac7cf9f4fce43551683a04b"
+uncertainty: "证据来自 KitchenWorlds 仿真；OOD 物体更密集时下降较大，真实几何与外观泛化尚未验证。"
+---
+
+# 自适应交错多模态规划
+
+长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。
```
