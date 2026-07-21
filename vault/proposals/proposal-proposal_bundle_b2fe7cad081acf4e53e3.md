---
id: "proposal_bundle_b2fe7cad081acf4e53e3"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T13:34:04+08:00"
updated_at: "2026-07-20T13:34:22+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5b8c57a9bef3348109f3b7bb"]
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
extraction_id: "extraction_f37f0a88446ad9c24f3d2880"
input_sha256: "76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_9443d1789c9a179bd1611be3", "target_path": "vault/memory/concept/concept_9443d1789c9a179bd1611be3.md", "base_sha256": "0e813ab305558c549294ed9d4b64f7cf458f236e46e0b1a961b4055676efc010", "candidate_sha256": "0697f3e115a24355a4aea36bdf98d3937b597baaea02e61ac9637d84b1aa2c67", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b2fe7cad081acf4e53e3-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_b2fe7cad081acf4e53e3-concept-1.md", "working_path": "vault/memory/concept/concept_9443d1789c9a179bd1611be3.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-20T13:34:22+08:00"}]
existing_context: [{"id": "reflection_305130038ee9fd3cb9e18ec4", "type": "reflection", "title": "ExToken：探索预算的关键变量可能是行为模式覆盖而非 rollout 数量", "path": "vault/reflections/reflection-reflection_305130038ee9fd3cb9e18ec4.md", "status": "active", "source_ids": ["source_5b8c57a9bef3348109f3b7bb"], "snippet": "# ExToken：探索预算的关键变量可能是行为模式覆盖而非 rollout 数量\n\n## Why important\n\nExToken 直接针对 VLA-RL 中动作模式坍缩，把离线示范聚类得到的离散行为先验变成 rollout 条件，从而用结构化多样性提升有限交互预算下的状态-动作覆盖。\n\n## What changed…", "match_reason": "metadata:domains"}, {"id": "concept_9443d1789c9a179bd1611be3", "type": "concept", "title": "示范先验条件化的 VLA 结构化探索", "path": "vault/memory/concept/concept_9443d1789c9a179bd1611be3.md", "status": "working", "source_ids": ["source_5b8c57a9bef3348109f3b7bb"], "snippet": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。", "match_reason": "metadata:aliases"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex [Structured] Demonstrations for Vision-Language-Action Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "reflection_bfb923cbbf75ed8a49f9df44", "type": "reflection", "title": "Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎", "path": "vault/reflections/reflection-reflection_bfb923cbbf75ed8a49f9df44.md", "status": "active", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "…What changed\n\n此前常把具身 world model 视为预测下一帧或规划 rollout；该工作把 [structured] multi-view editing 也纳入世界模型接口，强调数据生成与动力学建模可以共享基础模型但需要不同一致性约束。\n\n## Surprising\n\n论文报告用零样本生成的多视角关键帧扩增数据后，π0.5…", "match_reason": "full-text:body"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…safety refusal mechanisms work in code?\n\n## Possible mechanisms\n\n- [Structured] world state and post-action observation make deviations measurable…", "match_reason": "full-text:body"}, {"id": "claim_wechat_skillevolver_k4_strategy_exploration_20260716", "type": "claim", "title": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略", "path": "vault/memory/claim/claim_wechat_skillevolver_k4_strategy_exploration_20260716.md", "status": "trusted", "source_ids": ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略。", "match_reason": "metadata:tags"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…post-training can hide materially different assumptions about [exploration] safety, reset access, and data stationarity.\n\n## Open questions\n\n- Which…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5b8c57a9bef3348109f3b7bb"}
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
- Extraction：`extraction_f37f0a88446ad9c24f3d2880`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_9443d1789c9a179bd1611be3.md
+++ candidate:vault/memory/concept/concept_9443d1789c9a179bd1611be3.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_9443d1789c9a179bd1611be3"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "示范先验条件化的 VLA 结构化探索"
 created_at: "2026-07-20T12:27:21+08:00"
-updated_at: "2026-07-20T12:27:21+08:00"
+updated_at: "2026-07-20T13:34:04+08:00"
 aliases: ["Structured exploration with demonstration priors", "RL Exploration Token", "ExToken", "示范行为模式探索"]
 tags: []
 domains: ["embodied-ai", "vla", "robot-rl", "exploration"]
 confidence: "high"
 source_ids: ["source_5b8c57a9bef3348109f3b7bb"]
-relations: [{"type": "derived_from", "target_id": "source_5b8c57a9bef3348109f3b7bb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "二者都以小型条件接口保护 VLA 先验；前者改变探索模式分布，后者暴露供 actor-critic 在线优化的内部读出。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_5b8c57a9bef3348109f3b7bb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "二者都以小型条件接口保护 VLA 先验；前者改变探索模式分布，后者暴露供 actor-critic 在线优化的内部读出。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_f67f822ee20789d74d7b75e3", "reason": "ExToken 改变有限交互预算中的行为覆盖，DenseReward 改变失败轨迹上的信用信号；二者共同影响样本效率但风险分别是示范支持集偏置与奖励漏洞。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_5b8c57a9bef3348109f3b7bb"
-reflection_context: {"reflection_ids": ["reflection_305130038ee9fd3cb9e18ec4"], "importance": "high", "changed_belief": "此前把样本效率主要理解为每条轨迹被更充分利用；该工作提示，先控制采样分布中的行为模式多样性，可能比单纯增加 rollout 或改进优化器更基础。", "surprising": "论文实验中保留 512 条最多样的轨迹可匹配 1024 条标准 rollout，而标准 512 条明显更差；这把轨迹多样性从直觉性目标提升为可直接影响训练效率的变量。", "connections": [{"shared_mechanism": "与 VLA 的强化学习读出接口都把大策略的在线适配压缩到一个小型条件接口，并尽量保留预训练行为先验。", "boundary": "ExToken 的证据来自论文所选仿真和真机操作任务，且 token 由离线示范视频聚类得到；不能外推到无示范、开放世界或长时程探索。", "difference": "RL 读出接口从 VLA 内部特征学习供 actor-critic 使用的任务表示；ExToken 用离线示范的行为模式 token 主动改变 rollout 分布，并另学状态条件选择器。"}], "open_questions": ["轨迹多样性应在动作、状态覆盖、接触模式还是任务结果空间中度量，哪个与真实样本效率最稳定相关？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-daily-batch-a-20260720"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-daily-batch-a-20260720"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_b18ab3350b8ffc7decee"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b18ab3350b8ffc7decee-concept-1.md"
-origin_candidate_sha256: "17dee8a16d97e314a79dc0c31649cfc247a7c6cba6c8c18d7b94cfed6c6d48d5"
-memory_schema_version: 2
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_305130038ee9fd3cb9e18ec4", "reflection_cb246940931502d077f687f5"], "importance": "weekly", "changed_belief": "此前把样本效率主要理解为每条轨迹被更充分利用；该工作提示，先控制采样分布中的行为模式多样性，可能比单纯增加 rollout 或改进优化器更基础。\n此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。", "surprising": "论文实验中保留 512 条最多样的轨迹可匹配 1024 条标准 rollout，而标准 512 条明显更差；这把轨迹多样性从直觉性目标提升为可直接影响训练效率的变量。\n两帧历史优于一帧，而三帧又略差，提示奖励估计既需要时间上下文，也会受到冗余或噪声历史的影响。", "connections": [{"shared_mechanism": "与 VLA 的强化学习读出接口都把大策略的在线适配压缩到一个小型条件接口，并尽量保留预训练行为先验。", "boundary": "ExToken 的证据来自论文所选仿真和真机操作任务，且 token 由离线示范视频聚类得到；不能外推到无示范、开放世界或长时程探索。", "difference": "RL 读出接口从 VLA 内部特征学习供 actor-critic 使用的任务表示；ExToken 用离线示范的行为模式 token 主动改变 rollout 分布，并另学状态条件选择器。"}, {"shared_mechanism": "与 VLA 动作评估蒸馏都学习一个轻量评估信号，为原策略的候选动作或后训练提供长期结果信息。", "boundary": "DenseReward 依赖仿真中的阶段标签和定向扰动，论文只证明其所选操作任务上的奖励预测与下游指导效果；合成失败分布仍可能遗漏真机罕见故障。", "difference": "动作评估蒸馏从仿真树搜索回报学习候选动作 Q 值；DenseReward 从视觉历史和语言预测逐时刻进度，并显式训练多类失败轨迹。"}], "open_questions": ["轨迹多样性应在动作、状态覆盖、接触模式还是任务结果空间中度量，哪个与真实样本效率最稳定相关？", "合成失败与真实失败的分布差异应如何检测，并在策略开始利用奖励漏洞前触发人工或真机校准？"]}
+proposed_status: "working"
 ---
 
 # 示范先验条件化的 VLA 结构化探索
```
