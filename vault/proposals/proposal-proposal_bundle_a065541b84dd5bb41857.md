---
id: "proposal_bundle_a065541b84dd5bb41857"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:18:42+08:00"
updated_at: "2026-07-19T12:18:43+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_531bafa56ff63468797ac69e"]
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
extraction_id: "extraction_a62cff443eddb173166ba05a"
input_sha256: "1b21418e1ebdcf6b2d1889b3ca1364cdf63f0edd75ab1c668e37ecc9c2466694"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_dynamic_execution_horizon", "target_path": "vault/knowledge/concepts/concept_dynamic_execution_horizon-动态动作块执行时域.md", "base_sha256": null, "candidate_sha256": "6d4704c2f91d802bd993cf84ef9865a56e5b13bee1484bf013c3b87d7e46e9d8", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_a065541b84dd5bb41857-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_dynamic_execution_horizon.md", "working_at": "2026-07-19T12:18:43+08:00"}]
existing_context: [{"id": "claim_wechat_non_ergodic_coin_game_20260716", "type": "claim", "title": "该文以 +80%/-50% 公平硬币复利游戏说明：群体平均财富可增长但多数个体长期变穷，属非遍历性陷阱", "path": "vault/memory/claim/claim_wechat_non_ergodic_coin_game_20260716.md", "status": "working", "source_ids": ["source_9d39636775b188c87d6a001f"], "snippet": "# 非遍历硬币游戏\n\n群体平均↑ vs 多数个体↓；+80%/-50% 例。", "match_reason": "metadata:tags"}, {"id": "concept_typed_verified_robot_skill_graph", "type": "concept", "title": "类型化可验证机器人技能图", "path": "vault/memory/concept/concept_typed_verified_robot_skill_graph.md", "status": "working", "source_ids": ["source_6fb6f0a30a013fd1ada42b57"], "snippet": "# 类型化可验证机器人技能图\n\n把自然语言任务编译为带类型、检查点和恢复语义的模块化技能计算图，在仿真中验证与改进后执行该图本身，使跨对象几何和姿态变化的持续任务保留可审计控制结构。", "match_reason": "metadata:domains"}, {"id": "claim_bcc3a0fe69a9b845834b4324", "type": "claim", "title": "Across six long-horizon", "path": "vault/memory/claim/claim_bcc3a0fe69a9b845834b4324.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# Across six long-[horizon]\n\nAcross six long-[horizon]", "match_reason": "metadata:title"}, {"id": "claim_wechat_kairos_sim2real_training_20260716", "type": "claim", "title": "该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期", "path": "vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md", "status": "working", "source_ids": ["source_a20c5fb22d91216503d413e1"], "snippet": "# Sim-to-real\n\n跨房间/全屋整理训练；迁移周期声称待量化。", "match_reason": "metadata:tags"}, {"id": "concept_implicit_behavior_coordination", "type": "concept", "title": "隐式行为协调", "path": "vault/memory/concept/concept_implicit_behavior_coordination.md", "status": "working", "source_ids": ["source_8aa5e06bac422cb3319b94e6"], "snippet": "# 隐式行为协调\n\n从未标注的子任务示范中学习多模态候选动作块，再由价值函数按当前状态和任务目标选择候选，从而避免显式技能标签、边界和固定切换逻辑。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_531bafa56ff63468797ac69e"}
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
- Extraction：`extraction_a62cff443eddb173166ba05a`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_dynamic_execution_horizon-动态动作块执行时域.md
@@ -0,0 +1,20 @@
+---
+id: "concept_dynamic_execution_horizon"
+type: "concept"
+status: "proposal"
+title: "动态动作块执行时域"
+created_at: "2026-07-19T12:18:42+08:00"
+updated_at: "2026-07-19T12:18:42+08:00"
+aliases: ["dynamic execution horizon", "Dynamic Execution Horizon Prediction", "DEHP"]
+tags: []
+domains: ["embodied-ai", "robot-control", "action-chunking", "reinforcement-learning"]
+confidence: "medium"
+source_ids: ["source_531bafa56ff63468797ac69e"]
+relations: [{"type": "derived_from", "target_id": "source_531bafa56ff63468797ac69e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "part_of", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "动作块执行长度、重查询时机与时延补偿共同属于从策略预测到实际命令的部署调度层。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_cache_refinement", "reason": "两者都在不改生成主干的情况下优化动作块推理；缓存方法复用生成中间态，DEHP 调整已生成动作块的执行前缀。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_531bafa56ff63468797ac69e"
+uncertainty: "受控实验主要使用 state-based Diffusion Policy；方法声称可黑盒扩展到图像策略，但该扩展尚未由本文实验证实，且能力上限仍由冻结基础策略决定。"
+---
+
+# 动态动作块执行时域
+
+在保持动作块生成策略冻结的条件下，按当前观测和预测动作块动态决定执行多少步再重规划：自由空间运动使用较长前缀，精细对齐与接触阶段缩短前缀以提高反应性。
```
