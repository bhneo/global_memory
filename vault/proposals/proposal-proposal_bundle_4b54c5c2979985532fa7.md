---
id: "proposal_bundle_4b54c5c2979985532fa7"
type: "proposal"
status: "migrated"
title: "Compile bundle：Robo-ValueRL"
created_at: "2026-07-20T11:55:37+08:00"
updated_at: "2026-07-20T11:55:41+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Robo-ValueRL"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a288c4114d2d830f1678fd14"
input_sha256: "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_4739daf4ef7eacc9153c535f", "target_path": "vault/knowledge/concepts/concept_4739daf4ef7eacc9153c535f-可靠价值驱动的离线到在线策略改进.md", "base_sha256": null, "candidate_sha256": "95db7958cead1edd694b45998b7c0f21f1921311c766c8fc3f0203026af8b8ff", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_4b54c5c2979985532fa7-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "working_at": "2026-07-20T11:55:41+08:00"}]
existing_context: [{"id": "input_bb9068321957f044c9f1310a", "type": "input", "title": "Robo-ValueRL", "path": "vault/inputs/input-input_bb9068321957f044c9f1310a.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "…Reliable Value Estimation for [Offline-to-Online] Reinforcement Learning Wenke Xia 1,* , Pei Ren 2,* , Wenbo Yu 3…", "match_reason": "full-text:body"}, {"id": "reflection_617843f93885fb6b0d3c5f52", "type": "reflection", "title": "Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口", "path": "vault/reflections/reflection-reflection_617843f93885fb6b0d3c5f52.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口\n\n## Why important\n\n它把价值函数从训练配件提升为贯穿数据筛选、质量条件策略学习和在线残差适应的接口，并强调历史条件价值对遮挡、重复动作和相似阶段歧义的处理。\n\n## What changed\n\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度…", "match_reason": "metadata:domains"}, {"id": "reflection_052db872e2258b0e016c5ebf", "type": "reflection", "title": "UR-VC：先纠正进度代理，再训练价值或优势条件策略", "path": "vault/reflections/reflection-reflection_052db872e2258b0e016c5ebf.md", "status": "active", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "…与 [Robo-ValueRL] 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。\n  Boundary: UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。\n  Difference: UR-VC 在训练前修正监督标签且不训练价值模型；[Robo]…", "match_reason": "full-text:body"}, {"id": "work_arxiv_1810_08647", "type": "work", "title": "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning", "path": "vault/memory/work/work_arxiv_1810_08647.md", "status": "working", "source_ids": ["source_e9ed0a3745aea832b64d7fa7", "source_c019c0a492cc659d7858134d"], "snippet": "# [1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep [Reinforcement] Learning\n\n## Logical work identity\n\n- arXiv：`1810…", "match_reason": "metadata:title"}, {"id": "claim_wechat_im_rl_framework_internal_rewards_20260716", "type": "claim", "title": "该文称经典 RL 虽常被视为仅处理外在奖励，但 Barto 等框架可将奖励生成机制置于「内部环境」，内在与外在奖励可统一建模", "path": "vault/memory/claim/claim_wechat_im_rl_framework_internal_rewards_20260716.md", "status": "working", "source_ids": ["source_91199da18f239c48bbcdd49f"], "snippet": "# RL 统一奖励\n\n内在奖励可在体内生成；RL 框架不必限定外部通道。", "match_reason": "metadata:tags"}, {"id": "claim_physo_rnn_reinforcement_learning_method_20260716", "type": "claim", "title": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式", "path": "vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。", "match_reason": "metadata:tags"}, {"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward…", "match_reason": "metadata:tags"}, {"id": "concept_implicit_behavior_coordination", "type": "concept", "title": "隐式行为协调", "path": "vault/memory/concept/concept_implicit_behavior_coordination.md", "status": "working", "source_ids": ["source_8aa5e06bac422cb3319b94e6"], "snippet": "# 隐式行为协调\n\n从未标注的子任务示范中学习多模态候选动作块，再由价值函数按当前状态和任务目标选择候选，从而避免显式技能标签、边界和固定切换逻辑。", "match_reason": "metadata:domains"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_7b278ba348f2a8bb94cce1fc"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Robo-ValueRL

## 编译边界

- Provider：`codex-gpt56-m91-vla-posttraining-weekly-20260720`
- Extraction：`extraction_a288c4114d2d830f1678fd14`
- 编译前召回已有对象：9
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_4739daf4ef7eacc9153c535f-可靠价值驱动的离线到在线策略改进.md
@@ -0,0 +1,20 @@
+---
+id: "concept_4739daf4ef7eacc9153c535f"
+type: "concept"
+status: "proposal"
+title: "可靠价值驱动的离线到在线策略改进"
+created_at: "2026-07-20T11:55:37+08:00"
+updated_at: "2026-07-20T11:55:37+08:00"
+aliases: ["Robo-ValueRL", "value-guided offline-to-online adaptation"]
+tags: []
+domains: ["embodied-ai", "robot-rl", "vla", "value-learning"]
+confidence: "medium"
+source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
+relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_7b278ba348f2a8bb94cce1fc"
+reflection_context: {"reflection_ids": ["reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
+---
+
+# 可靠价值驱动的离线到在线策略改进
+
+可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。
```
