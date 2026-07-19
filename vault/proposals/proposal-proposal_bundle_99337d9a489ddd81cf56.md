---
id: "proposal_bundle_99337d9a489ddd81cf56"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T22:43:13+08:00"
updated_at: "2026-07-19T22:43:14+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_d83bb2c45bcaf70906e9ac96"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_d1322beb597a1138a31ed4fe"
input_sha256: "e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_d7111f304971448401a57f3b", "target_path": "vault/memory/concept/concept_d7111f304971448401a57f3b.md", "base_sha256": "4663d2ac1fe4b559a27012ad7ff3b0a4c4685ac7cd21546de9c49f6ee407b017", "candidate_sha256": "02612a67ac63f872118904c9434229bf105ac4d6fd2ffaa14a779fcd5b84efd2", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_99337d9a489ddd81cf56-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_99337d9a489ddd81cf56-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "claim_wechat_kairos_sim2real_training_20260716", "type": "claim", "title": "该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期", "path": "vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md", "status": "working", "source_ids": ["source_a20c5fb22d91216503d413e1"], "snippet": "# Sim-to-real\n\n跨房间/全屋整理训练；迁移周期声称待量化。", "match_reason": "metadata:tags"}, {"id": "claim_wechat_embodied_eval_bottleneck_20260715", "type": "claim", "title": "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住", "path": "vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md", "status": "working", "source_ids": ["source_2d4f3a7d3525782c8ff503ee"], "snippet": "# 评估瓶颈\n\n真机评测排队与人工摆场使迭代受评估而非训练限制。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_structure_not_volume_20260716", "type": "claim", "title": "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe", "path": "vault/memory/claim/claim_wechat_embodied_data_structure_not_volume_20260716.md", "status": "working", "source_ids": ["source_0a113baae7ce4d1ab78da1a3"], "snippet": "# 结构 vs 数量\n\n缺的是把数据变成能力的结构，非单纯缺 TB 日志。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "type": "claim", "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线", "path": "vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md", "status": "working", "source_ids": ["source_cda5a1b9e036598aff53e5be"], "snippet": "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。", "match_reason": "metadata:domains"}, {"id": "concept_typed_verified_robot_skill_graph", "type": "concept", "title": "类型化可验证机器人技能图", "path": "vault/memory/concept/concept_typed_verified_robot_skill_graph.md", "status": "working", "source_ids": ["source_6fb6f0a30a013fd1ada42b57"], "snippet": "# 类型化可验证机器人技能图\n\n把自然语言任务编译为带类型、检查点和恢复语义的模块化技能计算图，在仿真中验证与改进后执行该图本身，使跨对象几何和姿态变化的持续任务保留可审计控制结构。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_d83bb2c45bcaf70906e9ac96"}
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

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_d1322beb597a1138a31ed4fe`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_d7111f304971448401a57f3b.md
+++ candidate:vault/memory/concept/concept_d7111f304971448401a57f3b.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_d7111f304971448401a57f3b"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "冻结技能库与轻量路由适应"
 created_at: "2026-07-19T17:16:36+08:00"
-updated_at: "2026-07-19T17:16:36+08:00"
+updated_at: "2026-07-19T22:43:13+08:00"
 aliases: ["Frozen Skill Library with Lightweight Routing", "无监督技能挖掘", "Unsupervised Skill Mining", "SkillPlug"]
 tags: []
 domains: ["embodied-ai", "robot-learning", "skill-learning"]
 confidence: "medium"
 source_ids: ["source_d83bb2c45bcaf70906e9ac96"]
-relations: [{"type": "derived_from", "target_id": "source_d83bb2c45bcaf70906e9ac96", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都建立可复用技能中间层，但分别强调数据驱动技能先验与显式类型、验证和恢复边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_d83bb2c45bcaf70906e9ac96", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都建立可复用技能中间层，但分别强调数据驱动技能先验与显式类型、验证和恢复边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都建立可复用技能中间层，但分别强调数据驱动技能先验与显式类型、验证和恢复边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_d83bb2c45bcaf70906e9ac96"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_38154c8ff43c2bbbd3d979b5"], "importance": "high", "changed_belief": "此前更强调由语言或类型系统显式编译技能；该材料表明可复用中间层也可以从行为数据中学习，并把新任务适应限制在路由与执行接口。", "surprising": "技能库被冻结后仍可通过少量示范适应未见任务，说明可迁移性可能更多来自技能表示的分离与路由，而非持续改写整个策略。", "connections": [{"shared_mechanism": "都把端到端控制拆成可复用技能单元与面向任务的组合或路由层", "boundary": "连接只涉及技能复用结构，不假设无监督技能天然具有可读类型、前置条件或后置条件", "difference": "SkillPlug 的技能是从轨迹学习的连续隐变量先验，类型化技能图是显式、可检查并带恢复语义的符号控制结构"}], "open_questions": ["如何把无监督技能的激活区域转化为可验证的前置条件、后置条件和失效信号？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_20af9df1cfa58a4921b7"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_20af9df1cfa58a4921b7-concept-1.md"
-origin_candidate_sha256: "6ecc5050230144b50287449b9cb5c2c9fd17080b83159afb3ee6fb12b633c2bb"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 冻结技能库与轻量路由适应
```
