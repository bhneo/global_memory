---
id: "proposal_bundle_820eb9855d71d12a13ca"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T03:39:13+08:00"
updated_at: "2026-07-19T03:39:27+08:00"
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
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_dual_system_world_action_model", "target_path": "vault/memory/concept/concept_dual_system_world_action_model.md", "base_sha256": "1d0c3ecbb98fba3af25f3d23f422e53f3d04127d703125d5f41f5190a983ebcf", "candidate_sha256": "219763026c27f70ec2726a2d2758392b187ba6172ce62ae5f0734119e22a23ab", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_820eb9855d71d12a13ca-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_820eb9855d71d12a13ca-concept-1.md", "working_path": "vault/memory/concept/concept_dual_system_world_action_model.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:39:27+08:00"}]
existing_context: [{"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "claim_6ed5013981fdc75c87eb19c9", "type": "claim", "title": "real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×", "path": "vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# real-[world] environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference…", "match_reason": "metadata:title"}, {"id": "concept_multitimescale_tactile_world_model", "type": "concept", "title": "多时间尺度触觉世界模型控制", "path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ba057c2c11df2a5eba107870"}
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_4dc5b57f1f392591c651eddf`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_dual_system_world_action_model.md
+++ candidate:vault/memory/concept/concept_dual_system_world_action_model.md
@@ -1,41 +1,19 @@
 ---
 id: "concept_dual_system_world_action_model"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "双系统 World Action Model"
 created_at: "2026-07-19T03:03:07+08:00"
-updated_at: "2026-07-19T03:30:14+08:00"
-aliases: []
+updated_at: "2026-07-19T03:39:13+08:00"
+aliases: ["dual-system world-action model", "DSWAM"]
 tags: []
 domains: ["embodied-ai", "world-action-model", "vla", "planning"]
 confidence: "medium"
 source_ids: ["source_ba057c2c11df2a5eba107870"]
 relations: [{"type": "derived_from", "target_id": "source_ba057c2c11df2a5eba107870", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都将预测性世界表征接入动作系统，但 DSWAM 以 WAM 执行为默认路径。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两种架构都用双速或多速层级分离语义规划与动作执行。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "raises", "target_id": "tension_world_model_eval_action", "reason": "DSWAM 直接比较 WAM 与 VLA 执行路径，触及世界模型应作为评估器还是动作生成器的边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_ba057c2c11df2a5eba107870"
-uncertainty: "是否优于单体 VLA 取决于公平数据、机器人本体、任务协议和实时系统实现。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 3
-last_consolidated_at: "2026-07-19T03:30:14+08:00"
-last_verified_at: "2026-07-19T03:30:06+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_6eccb3b8a64c69fe1836"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_6eccb3b8a64c69fe1836-concept-1.md"
-origin_candidate_sha256: "5ced4e982782653e5e4f9f97f7086ab5478c17d667f40eb20011da720d7de8b4"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_2354cd6bfca2786fcbb1f49c"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "new_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ba057c2c11df2a5eba107870", "trigger_source": "source_ba057c2c11df2a5eba107870", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "new_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ba057c2c11df2a5eba107870", "trigger_source": "source_ba057c2c11df2a5eba107870", "evidence_added": []}]
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # 双系统 World Action Model
```
