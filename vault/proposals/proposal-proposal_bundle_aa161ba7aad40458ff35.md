---
id: "proposal_bundle_aa161ba7aad40458ff35"
type: "proposal"
status: "migrated"
title: "Compile bundle：TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation"
created_at: "2026-07-19T03:38:47+08:00"
updated_at: "2026-07-19T03:39:01+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_866e814ee1010452743e8b60"
input_sha256: "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_multitimescale_tactile_world_model", "target_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "base_sha256": "b815afa1c05d973c216faeee5d43c78677d4c87170826b375c62243cfd973ba3", "candidate_sha256": "762232ce533ad5a5779ee9bed9a8703965663d28f01c6fba3ffb6af2cec3b66c", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_aa161ba7aad40458ff35-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_aa161ba7aad40458ff35-concept-1.md", "working_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:39:01+08:00"}]
existing_context: [{"id": "claim_2fa0248b6e89ef9c5810d69d", "type": "claim", "title": "contact-rich dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean setting", "path": "vault/memory/claim/claim_2fa0248b6e89ef9c5810d69d.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# contact-rich dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean setting\n\ncontact-rich dexterous manipulation…", "match_reason": "metadata:domains"}, {"id": "claim_9af622d7162156b1ad40f640", "type": "claim", "title": "predictive capability.", "path": "vault/memory/claim/claim_9af622d7162156b1ad40f640.md", "status": "working", "source_ids": ["source_233c4bef3a727389ddf81ae2"], "snippet": "# [predictive] capability.\n\n[predictive] capability.", "match_reason": "metadata:title"}, {"id": "concept_multitimescale_tactile_world_model", "type": "concept", "title": "多时间尺度触觉世界模型控制", "path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "match_reason": "metadata:domains"}, {"id": "claim_bcc3a0fe69a9b845834b4324", "type": "claim", "title": "Across six long-horizon", "path": "vault/memory/claim/claim_bcc3a0fe69a9b845834b4324.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# Across six long-horizon\n\nAcross six long-horizon", "match_reason": "metadata:domains"}, {"id": "claim_93372fb57436c826769d8914", "type": "claim", "title": "18.5 percentage points, respectively.", "path": "vault/memory/claim/claim_93372fb57436c826769d8914.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 18.5 percentage points, respectively.\n\n18.5 percentage points, respectively.", "match_reason": "metadata:domains"}, {"id": "claim_6c93f48395d9852588c5c00f", "type": "claim", "title": "53.7% success under human perturbations, outperforming the strongest baseline by 15.7", "path": "vault/memory/claim/claim_6c93f48395d9852588c5c00f.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 53.7% success under human perturbations, outperforming the strongest baseline by 15.7\n\n53.7% success under human…", "match_reason": "metadata:domains"}, {"id": "claim_251ad28e5021bb5fb97a0f2b", "type": "claim", "title": "The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model", "path": "vault/memory/claim/claim_251ad28e5021bb5fb97a0f2b.md", "status": "working", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "# The neural network architecture of GR00T N1.7 is a combination of vision-language [foundation] model\n\nThe neural…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_283911da72edc403d1b823fb"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_866e814ee1010452743e8b60`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_multitimescale_tactile_world_model.md
+++ candidate:vault/memory/concept/concept_multitimescale_tactile_world_model.md
@@ -1,41 +1,19 @@
 ---
 id: "concept_multitimescale_tactile_world_model"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "多时间尺度触觉世界模型控制"
 created_at: "2026-07-19T03:02:53+08:00"
-updated_at: "2026-07-19T03:29:35+08:00"
-aliases: []
+updated_at: "2026-07-19T03:38:47+08:00"
+aliases: ["multi-timescale tactile world model", "TouchWorld"]
 tags: []
 domains: ["embodied-ai", "vla", "world-model", "tactile", "dexterous-manipulation"]
 confidence: "medium"
 source_ids: ["source_283911da72edc403d1b823fb"]
 relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_283911da72edc403d1b823fb"
-uncertainty: "架构和结果局限于论文中的六项长时程接触任务，触觉硬件与标注成本可能影响迁移。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 3
-last_consolidated_at: "2026-07-19T03:29:35+08:00"
-last_verified_at: "2026-07-19T03:29:27+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_2a787ee43ca54bc95b00"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_2a787ee43ca54bc95b00-concept-1.md"
-origin_candidate_sha256: "e6161d8a748e1a5dd54a5ac7254ede7a78d21d97fc25b7593f1b022e298b82fc"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_70d661783ebb70e2ff8347fe"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}]
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # 多时间尺度触觉世界模型控制
```
