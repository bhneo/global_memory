---
id: "proposal_bundle_e231d1eaf0d303698229"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:18:02+08:00"
updated_at: "2026-07-19T12:18:03+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_3e845794fed758f1dda5248e"]
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
extraction_id: "extraction_ed1f2b197a76f04ac4d8cf87"
input_sha256: "ba214821335d7ee7e23d1c4e9e792bdf2fd3ac9711d08ace0c06eff8d4016eed"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_real_robot_deployment_iteration_loop", "target_path": "vault/knowledge/concepts/concept_real_robot_deployment_iteration_loop-真机部署评估迭代闭环.md", "base_sha256": null, "candidate_sha256": "578066e560ea1336ef9aa4f91f6254668a5aa0dcec63fce8a4d81ff6e8a5f14f", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_e231d1eaf0d303698229-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "working_at": "2026-07-19T12:18:03+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_3e845794fed758f1dda5248e"}
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
- Extraction：`extraction_ed1f2b197a76f04ac4d8cf87`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_real_robot_deployment_iteration_loop-真机部署评估迭代闭环.md
@@ -0,0 +1,20 @@
+---
+id: "concept_real_robot_deployment_iteration_loop"
+type: "concept"
+status: "proposal"
+title: "真机部署评估迭代闭环"
+created_at: "2026-07-19T12:18:02+08:00"
+updated_at: "2026-07-19T12:18:02+08:00"
+aliases: ["real-robot deployment-evaluation loop", "physical robot iteration loop", "deployment, evaluation and data-collection loop"]
+tags: []
+domains: ["embodied-ai", "robotics", "real-robot-evaluation", "data-collection"]
+confidence: "medium"
+source_ids: ["source_3e845794fed758f1dda5248e"]
+relations: [{"type": "derived_from", "target_id": "source_3e845794fed758f1dda5248e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "part_of", "target_id": "concept_end_to_end_embodied_reproducibility", "reason": "端到端复现不仅要复现模型，还要固定观测、预测、平滑和实际执行命令之间的真机协议与日志。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_portable_embodied_inference_runtime", "reason": "可移植推理运行时解决模型侧异构执行，EVA-Client 解决机器人侧调度、逆解、采集和评估；两者是互补而非重复的部署层。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "refines", "target_id": "claim_wechat_embodied_eval_bottleneck_20260715", "reason": "EVA-Client 把笼统的真机评估瓶颈具体化为场景协议、里程碑评分以及原始预测、平滑动作、实际命令三路可归因日志。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_3e845794fed758f1dda5248e"
+uncertainty: "EVA-Client 是基础设施而非策略或 benchmark；文中任务结果是说明性部署观察，不能当作受控方法优越性实验。"
+---
+
+# 真机部署评估迭代闭环
+
+用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。
```
