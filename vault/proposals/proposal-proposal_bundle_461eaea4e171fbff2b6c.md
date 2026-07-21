---
id: "proposal_bundle_461eaea4e171fbff2b6c"
type: "proposal"
status: "migrated"
title: "Compile bundle：TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation"
created_at: "2026-07-19T23:47:57+08:00"
updated_at: "2026-07-19T23:48:11+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-weekly-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_866e814ee1010452743e8b60"
input_sha256: "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_multitimescale_tactile_world_model", "target_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "base_sha256": "946c3fd238c193e284dda07048884fb1fe167b0d570463d069fc2550994b1552", "candidate_sha256": "cea43a9e36a349a1c20c4758b3e698d447fa1a934495fbf5973046b2bcbe1d4d", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_461eaea4e171fbff2b6c-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_461eaea4e171fbff2b6c-concept-1.md", "working_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T23:48:11+08:00"}]
existing_context: [{"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile [Foundation] Model for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "reflection_c5765c32f1c3dd7302da4906", "type": "reflection", "title": "TouchWorld：预测与反应必须处在不同控制时间尺度", "path": "vault/reflections/reflection-reflection_c5765c32f1c3dd7302da4906.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# TouchWorld：预测与反应必须处在不同控制时间尺度\n\n## Why important\n\nTouchWorld 把慢速语义规划、中频动作块、触觉子目标预测和高频残差纠错拆开，说明世界模型的价值不只是预测准确，而是为正确时间尺度的控制回路提供目标。\n\n## What changed\n\n此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。\n\n## Surprising…", "match_reason": "metadata:domains"}, {"id": "synthesis_fe1750531bf1b2a79846b657", "type": "synthesis", "title": "具身策略部署中的监督通道、动作接口与反馈时标", "path": "vault/synthesis/synthesis-synthesis_fe1750531bf1b2a79846b657.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_91072aa553af99e6ab97c6cd"], "snippet": "…真正可比较的是每层保留的信息、更新频率、失效信号和对下游动作的责任边界。\n\n## Knowledge updates\n\n[\n  {\n    \"target_id\": \"concept_[predictive]_vla_deployment\",\n    \"previous\": \"预测式 VLA 主要指在视觉—语言—动作映射中加入未来状态或动作后果预测。\",\n    \"proposed…", "match_reason": "full-text:body"}, {"id": "concept_multitimescale_tactile_world_model", "type": "concept", "title": "多时间尺度触觉世界模型控制", "path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "match_reason": "metadata:aliases"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "…NVIDIA Isaac GR00T N1.7 - A [Foundation] Model for Generalist Robots. · GitHub\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The…", "match_reason": "metadata:title"}]
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

- Provider：`codex-gpt56-m91-real-weekly-v2`
- Extraction：`extraction_866e814ee1010452743e8b60`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_multitimescale_tactile_world_model.md
+++ candidate:vault/memory/concept/concept_multitimescale_tactile_world_model.md
@@ -1,41 +1,20 @@
 ---
 id: "concept_multitimescale_tactile_world_model"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "多时间尺度触觉世界模型控制"
 created_at: "2026-07-19T03:02:53+08:00"
-updated_at: "2026-07-19T12:20:17+08:00"
+updated_at: "2026-07-19T23:47:57+08:00"
 aliases: ["multi-timescale tactile world model", "TouchWorld"]
 tags: []
-domains: ["embodied-ai", "vla", "world-model", "tactile", "dexterous-manipulation"]
+domains: ["embodied-ai", "vla", "world-model", "tactile"]
 confidence: "medium"
 source_ids: ["source_283911da72edc403d1b823fb"]
-relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "limits", "target_id": "concept_vla_action_cache_refinement", "reason": "接触状态快速变化时，历史动作即使视觉上下文相似也可能陈旧，高频触觉反馈构成动作缓存安全复用的边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-weekly-v2", "status": "proposal"}]
 change_reason: "compile bundle from source_283911da72edc403d1b823fb"
-uncertainty: "架构和结果局限于论文中的六项长时程接触任务，触觉硬件与标注成本可能影响迁移。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 5
-last_consolidated_at: "2026-07-19T12:20:17+08:00"
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
-last_consolidation_id: "consolidation_068e7f282c9ca37ea74eb328"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["aliases"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}]
+change_type: "metadata_only"
+reflection_context: {"reflection_ids": ["reflection_c5765c32f1c3dd7302da4906"], "importance": "weekly", "changed_belief": "此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。", "surprising": "触觉在同一架构中同时承担未来接触参考和即时误差反馈，两种角色共享模态但具有不同时间语义。", "connections": [{"shared_mechanism": "都将预测结果作为动作生成或校正的中间目标，而不是只用于离线评分", "boundary": "连接限于预测辅助控制；触觉接触闭环不能直接推广到无接触导航或只有视觉输入的任务", "difference": "TouchWorld 用高频触觉残差处理局部接触偏差，LingBot 用语义与深度未来查询改善较慢的动作表示"}], "open_questions": ["预测子目标的误差何时应触发高层重规划，而不是继续由高频残差策略吸收？"]}
+proposed_status: "working"
 ---
 
 # 多时间尺度触觉世界模型控制
```
