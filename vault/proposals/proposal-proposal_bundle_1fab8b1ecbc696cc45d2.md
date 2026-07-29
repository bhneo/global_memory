---
id: "proposal_bundle_1fab8b1ecbc696cc45d2"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:41:29+08:00"
updated_at: "2026-07-21T17:41:29+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e2614742b0c3ee7cf985d616"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56sol-readmission-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_9b4583595ba685f207389410"
input_sha256: "1745ce117de5b359f955d1da910a830661d5d80a2781c7dd50cf67fb3fe43990"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_action_centered_joint_world_action_model", "target_path": "vault/knowledge/concepts/concept_action_centered_joint_world_action_model-动作中心的联合世界-动作模型.md", "base_sha256": null, "candidate_sha256": "d3b54ec759c2c5269630a70679234f0f5be8f6226048b2162794ce1165d40f27", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_1fab8b1ecbc696cc45d2-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_action_centered_joint_world_action_model.md", "working_at": "2026-07-21T17:41:29+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e2614742b0c3ee7cf985d616"}
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

- Provider：`agent-semantic-daily-gpt56sol-readmission-v1`
- Extraction：`extraction_9b4583595ba685f207389410`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_action_centered_joint_world_action_model-动作中心的联合世界-动作模型.md
@@ -0,0 +1,20 @@
+---
+id: "concept_action_centered_joint_world_action_model"
+type: "concept"
+status: "proposal"
+title: "动作中心的联合世界—动作模型"
+created_at: "2026-07-21T17:41:29+08:00"
+updated_at: "2026-07-21T17:41:29+08:00"
+aliases: ["Action-Centered Joint World-Action Model", "GigaWorld-Policy-0.5", "动作中心 WAM"]
+tags: []
+domains: ["embodied-ai", "world-action-model", "vla"]
+confidence: "medium"
+source_ids: ["source_e2614742b0c3ee7cf985d616"]
+relations: [{"type": "derived_from", "target_id": "source_e2614742b0c3ee7cf985d616", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "联合预测架构需要以未来预测质量、闭环控制收益和计算成本分别验收。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e2614742b0c3ee7cf985d616"
+reflection_context: {"reflection_ids": ["reflection_aeafd32447e03d5456e70a02"], "importance": "high", "changed_belief": "联合未来视觉损失不能直接视为世界模型能力；必须分别检查动作成功率、预测质量、延迟和自动搜索选择的可复现性。", "surprising": "作者报告六类水果采摘平均成功率 0.85、三项长程任务平均 0.80，以及特定设置下 17.5% 推理加速，但贡献拆分依赖论文内部消融。", "connections": [{"shared_mechanism": "都用未来状态或结果预测约束动作表示。", "boundary": "联合预测损失不等于具有可规划、因果一致的完整世界模型。", "difference": "该工作端到端联合生成动作与视觉；世界模型评测概念要求把预测质量与闭环控制收益分开验证。"}], "open_questions": ["AutoResearch 选出的配方在不同机器人、数据规模和延迟预算下是否稳定？"]}
+---
+
+# 动作中心的联合世界—动作模型
+
+GigaWorld-Policy-0.5 以视觉专家和动作专家构成 Mixture-of-Transformers，在因果注意力约束下从当前多视角观察、机器人状态和语言同时预测动作块与未来视觉 token，并配合 KV cache 等推理加速。它提供的是特定系统中联合世界—动作监督与闭环表现的关联证据，不能单凭未来帧损失推断可规划性或因果世界模型能力。
```
