---
id: "proposal_bundle_b18ab3350b8ffc7decee"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:27:21+08:00"
updated_at: "2026-07-20T12:27:21+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5b8c57a9bef3348109f3b7bb"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-a-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_f37f0a88446ad9c24f3d2880"
input_sha256: "76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_9443d1789c9a179bd1611be3", "target_path": "vault/knowledge/concepts/concept_9443d1789c9a179bd1611be3-示范先验条件化的-vla-结构化探索.md", "base_sha256": null, "candidate_sha256": "17dee8a16d97e314a79dc0c31649cfc247a7c6cba6c8c18d7b94cfed6c6d48d5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b18ab3350b8ffc7decee-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_9443d1789c9a179bd1611be3.md", "working_at": "2026-07-20T12:27:21+08:00"}]
existing_context: [{"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex [Structured] Demonstrations for Vision-Language-Action Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "claim_wechat_skillevolver_k4_strategy_exploration_20260716", "type": "claim", "title": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略", "path": "vault/memory/claim/claim_wechat_skillevolver_k4_strategy_exploration_20260716.md", "status": "trusted", "source_ids": ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略。", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5b8c57a9bef3348109f3b7bb"}
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

- Provider：`codex-gpt56-m91-daily-batch-a-20260720`
- Extraction：`extraction_f37f0a88446ad9c24f3d2880`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_9443d1789c9a179bd1611be3-示范先验条件化的-vla-结构化探索.md
@@ -0,0 +1,20 @@
+---
+id: "concept_9443d1789c9a179bd1611be3"
+type: "concept"
+status: "proposal"
+title: "示范先验条件化的 VLA 结构化探索"
+created_at: "2026-07-20T12:27:21+08:00"
+updated_at: "2026-07-20T12:27:21+08:00"
+aliases: ["Structured exploration with demonstration priors", "RL Exploration Token", "ExToken", "示范行为模式探索"]
+tags: []
+domains: ["embodied-ai", "vla", "robot-rl", "exploration"]
+confidence: "high"
+source_ids: ["source_5b8c57a9bef3348109f3b7bb"]
+relations: [{"type": "derived_from", "target_id": "source_5b8c57a9bef3348109f3b7bb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "二者都以小型条件接口保护 VLA 先验；前者改变探索模式分布，后者暴露供 actor-critic 在线优化的内部读出。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_5b8c57a9bef3348109f3b7bb"
+reflection_context: {"reflection_ids": ["reflection_305130038ee9fd3cb9e18ec4"], "importance": "high", "changed_belief": "此前把样本效率主要理解为每条轨迹被更充分利用；该工作提示，先控制采样分布中的行为模式多样性，可能比单纯增加 rollout 或改进优化器更基础。", "surprising": "论文实验中保留 512 条最多样的轨迹可匹配 1024 条标准 rollout，而标准 512 条明显更差；这把轨迹多样性从直觉性目标提升为可直接影响训练效率的变量。", "connections": [{"shared_mechanism": "与 VLA 的强化学习读出接口都把大策略的在线适配压缩到一个小型条件接口，并尽量保留预训练行为先验。", "boundary": "ExToken 的证据来自论文所选仿真和真机操作任务，且 token 由离线示范视频聚类得到；不能外推到无示范、开放世界或长时程探索。", "difference": "RL 读出接口从 VLA 内部特征学习供 actor-critic 使用的任务表示；ExToken 用离线示范的行为模式 token 主动改变 rollout 分布，并另学状态条件选择器。"}], "open_questions": ["轨迹多样性应在动作、状态覆盖、接触模式还是任务结果空间中度量，哪个与真实样本效率最稳定相关？"]}
+---
+
+# 示范先验条件化的 VLA 结构化探索
+
+从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。
```
