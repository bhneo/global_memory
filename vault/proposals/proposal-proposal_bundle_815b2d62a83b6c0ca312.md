---
id: "proposal_bundle_815b2d62a83b6c0ca312"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T11:56:10+08:00"
updated_at: "2026-07-20T11:56:11+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9a6e63428ed93e1a99ea4c4d"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_dfb859e53fae61aa66a0c3f5"
input_sha256: "0f7fc3c1792ef4645ef866526736a83a5e2cf4f55be513158bb2e165c62df1dd"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_latent_space_intervention_adaptation", "target_path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "base_sha256": "4c18f7232276c8abec7370c0e477307c4fc3f7589da5409dc5e3bf5110d67081", "candidate_sha256": "22aa7919b6a27fa8ec9474eac9842d0d2f54c79610c9878058051bfc4022d607", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_815b2d62a83b6c0ca312-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_815b2d62a83b6c0ca312-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "reflection_cd269bee56819aafec2fd5a3", "type": "reflection", "title": "FlowDAgger：适配接口的位置决定能否保留生成策略先验", "path": "vault/reflections/reflection-reflection_cd269bee56819aafec2fd5a3.md", "status": "active", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# FlowDAgger：适配接口的位置决定能否保留生成策略先验\n\n## Why important\n\n它把人类纠正动作反演为冻结生成策略的噪声向量，再训练小型潜空间策略，避免全模型微调破坏已有技能，也避免无约束动作残差离开基础策略支持集。\n\n## What changed\n\n人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。\n\n## Surprising\n\n人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger…", "match_reason": "metadata:domains"}, {"id": "concept_latent_space_intervention_adaptation", "type": "concept", "title": "生成策略的潜空间干预适应", "path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "status": "working", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# 生成策略的潜空间干预适应\n\n把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。", "match_reason": "metadata:domains"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…Knowledge updates\n\n[\n  {\n    \"target_id\": \"concept_latent_space_intervention_[adaptation]\",\n    \"previous\": \"通过人类干预的动作反演，在冻结生成策略的潜空间中学习轻量适配。\",\n    \"proposed\": \"潜空间干预适配属于 VLA 后训练反馈接口的一种：它用人类纠正提供监督，在生成策略支持集内转向…", "match_reason": "full-text:body"}, {"id": "reflection_5b4f45d757e5b256cdddfcfa", "type": "reflection", "title": "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口", "path": "vault/reflections/reflection-reflection_5b4f45d757e5b256cdddfcfa.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "…与 [FlowDAgger] 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。\n  Boundary: RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。\n  Difference: RL Token 学习面向 actor-critic 的内部特征读出并用 RL…", "match_reason": "full-text:body"}, {"id": "concept_4739daf4ef7eacc9153c535f", "type": "concept", "title": "可靠价值驱动的离线到在线策略改进", "path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "status": "working", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。", "match_reason": "metadata:aliases"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2…", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9a6e63428ed93e1a99ea4c4d"}
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

- Provider：`codex-gpt56-m91-vla-posttraining-weekly-20260720`
- Extraction：`extraction_dfb859e53fae61aa66a0c3f5`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_latent_space_intervention_adaptation.md
+++ candidate:vault/memory/concept/concept_latent_space_intervention_adaptation.md
@@ -1,39 +1,20 @@
 ---
 id: "concept_latent_space_intervention_adaptation"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "生成策略的潜空间干预适应"
 created_at: "2026-07-19T12:19:04+08:00"
-updated_at: "2026-07-19T12:20:15+08:00"
-aliases: ["latent-space intervention adaptation", "noise-space policy adaptation", "FlowDAgger"]
+updated_at: "2026-07-20T11:56:10+08:00"
+aliases: ["FlowDAgger", "latent-space intervention adaptation", "noise-space policy adaptation"]
 tags: []
-domains: ["embodied-ai", "robot-learning", "human-in-the-loop", "generative-policy"]
-confidence: "medium"
+domains: ["embodied-ai", "vla", "human-in-the-loop", "generative-policy"]
+confidence: "high"
 source_ids: ["source_9a6e63428ed93e1a99ea4c4d"]
 relations: [{"type": "derived_from", "target_id": "source_9a6e63428ed93e1a99ea4c4d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "两者都冻结生成主干并增加轻量部署模块；动作评估蒸馏负责候选排序，潜空间干预适应则从人类纠正学习如何改变生成噪声。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都保留冻结 VLA 的已有能力；Harness VLA 在外部原语/规划层重组行为，FlowDAgger 在生成潜变量层内转向行为。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "该方法需要部署时捕获状态、人的纠正动作和对应策略执行，以形成可训练的干预对；可记录的真机迭代闭环是其数据入口。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_9a6e63428ed93e1a99ea4c4d"
-uncertainty: "适应能力受基础策略动作流形支持范围约束，并依赖人类干预的覆盖与一致性；高度多模态或病态生成动力学会降低反演保真度。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-19T12:20:15+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_915ac66f5af193cc3ec2"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_915ac66f5af193cc3ec2-concept-1.md"
-origin_candidate_sha256: "a1570eba4b9e88ec518093ddc5530da1f62b312f5dd1181cb52fd2a940f7096d"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_9bb6e83c9bd4c3d433713ed3"
+change_type: "needs_review"
+reflection_context: {"reflection_ids": ["reflection_cd269bee56819aafec2fd5a3"], "importance": "weekly", "changed_belief": "人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。", "surprising": "人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger 风格干预能够训练潜空间控制器。", "connections": [{"shared_mechanism": "与 RL Token 都把大模型保持为稳定行为先验，只训练小型中间接口。", "boundary": "FlowDAgger 限于可执行动作反演的流匹配或扩散生成策略，并依赖人类在分布偏移处提供纠正。", "difference": "FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 actor-critic；两者的信息来源和安全成本不同。"}], "open_questions": ["动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？"]}
+proposed_status: "working"
 ---
 
 # 生成策略的潜空间干预适应
```
