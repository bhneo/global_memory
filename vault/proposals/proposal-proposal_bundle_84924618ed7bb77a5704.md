---
id: "proposal_bundle_84924618ed7bb77a5704"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:18:32+08:00"
updated_at: "2026-07-19T12:18:33+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_4bff03c9d5adb3463b34f947"]
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
extraction_id: "extraction_2aa9c0a522a7dadd79fbdc6c"
input_sha256: "b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_asymmetric_frozen_vla_harness", "target_path": "vault/knowledge/concepts/concept_asymmetric_frozen_vla_harness-冻结-vla-的非对称技能编排.md", "base_sha256": null, "candidate_sha256": "ca740123df7e1d552efc8343f658d1a9ead0389bf71134ba9696bb6be738e466", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_84924618ed7bb77a5704-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "working_at": "2026-07-19T12:18:33+08:00"}]
existing_context: [{"id": "claim_ed202cdc4c79d46f2ac31913", "type": "claim", "title": "该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选", "path": "vault/memory/claim/claim_ed202cdc4c79d46f2ac31913.md", "status": "working", "source_ids": ["source_ff90ad99bd47043e812cce9e"], "snippet": "# 该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选\n\nA diagnostic pass@k study confirms that frozen [VLAs] already contain competent…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_4bff03c9d5adb3463b34f947"}
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
- Extraction：`extraction_2aa9c0a522a7dadd79fbdc6c`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_asymmetric_frozen_vla_harness-冻结-vla-的非对称技能编排.md
@@ -0,0 +1,20 @@
+---
+id: "concept_asymmetric_frozen_vla_harness"
+type: "concept"
+status: "proposal"
+title: "冻结 VLA 的非对称技能编排"
+created_at: "2026-07-19T12:18:32+08:00"
+updated_at: "2026-07-19T12:18:32+08:00"
+aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA"]
+tags: []
+domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation"]
+confidence: "medium"
+source_ids: ["source_4bff03c9d5adb3463b34f947"]
+relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_4bff03c9d5adb3463b34f947"
+uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
+---
+
+# 冻结 VLA 的非对称技能编排
+
+把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。
```
