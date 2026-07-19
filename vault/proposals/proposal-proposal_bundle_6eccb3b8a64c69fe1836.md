---
id: "proposal_bundle_6eccb3b8a64c69fe1836"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T03:03:07+08:00"
updated_at: "2026-07-19T03:03:08+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ba057c2c11df2a5eba107870"]
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
extraction_id: "extraction_4dc5b57f1f392591c651eddf"
input_sha256: "1e3360df13a89572110bfc6149bda1dffb183a50fcd0ce2b0e1888731ddef9d3"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_dual_system_world_action_model", "target_path": "vault/knowledge/concepts/concept_dual_system_world_action_model-双系统-world-action-model.md", "base_sha256": null, "candidate_sha256": "5ced4e982782653e5e4f9f97f7086ab5478c17d667f40eb20011da720d7de8b4", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_6eccb3b8a64c69fe1836-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_dual_system_world_action_model.md", "working_at": "2026-07-19T03:03:08+08:00"}]
existing_context: [{"id": "claim_6ed5013981fdc75c87eb19c9", "type": "claim", "title": "real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×", "path": "vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# real-[world] environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ba057c2c11df2a5eba107870"}
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
- Extraction：`extraction_4dc5b57f1f392591c651eddf`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_dual_system_world_action_model-双系统-world-action-model.md
@@ -0,0 +1,20 @@
+---
+id: "concept_dual_system_world_action_model"
+type: "concept"
+status: "proposal"
+title: "双系统 World Action Model"
+created_at: "2026-07-19T03:03:07+08:00"
+updated_at: "2026-07-19T03:03:07+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "world-action-model", "vla", "planning"]
+confidence: "medium"
+source_ids: ["source_ba057c2c11df2a5eba107870"]
+relations: [{"type": "derived_from", "target_id": "source_ba057c2c11df2a5eba107870", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都将预测性世界表征接入动作系统，但 DSWAM 以 WAM 执行为默认路径。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两种架构都用双速或多速层级分离语义规划与动作执行。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "raises", "target_id": "tension_world_model_eval_action", "reason": "DSWAM 直接比较 WAM 与 VLA 执行路径，触及世界模型应作为评估器还是动作生成器的边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_ba057c2c11df2a5eba107870"
+uncertainty: "是否优于单体 VLA 取决于公平数据、机器人本体、任务协议和实时系统实现。"
+---
+
+# 双系统 World Action Model
+
+默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。
```
