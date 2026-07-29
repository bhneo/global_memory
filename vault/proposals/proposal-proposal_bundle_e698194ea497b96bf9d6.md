---
id: "proposal_bundle_e698194ea497b96bf9d6"
type: "proposal"
status: "migrated"
title: "Compile bundle：Robo-ValueRL"
created_at: "2026-07-28T16:27:52+08:00"
updated_at: "2026-07-28T16:27:53+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-strong-model-m91-weekly-v3"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Robo-ValueRL"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a288c4114d2d830f1678fd14"
input_sha256: "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_4739daf4ef7eacc9153c535f", "target_path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "base_sha256": "1426d12910a7c17df821bee46f27059c5c1a1ee45a62de5ef6c1a5b0111df9ad", "candidate_sha256": "8c63cac801a362efb3178de9efd101f5498d6c9cfae6e021ecd3743955501e6b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_e698194ea497b96bf9d6-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_e698194ea497b96bf9d6-concept-1.md", "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "input_bb9068321957f044c9f1310a", "type": "input", "title": "Robo-ValueRL", "path": "vault/inputs/input-input_bb9068321957f044c9f1310a.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "…Reliable Value Estimation for [Offline-to-Online] Reinforcement Learning Wenke Xia 1,* , Pei Ren 2,* , Wenbo Yu 3…", "match_reason": "full-text:body"}, {"id": "reflection_617843f93885fb6b0d3c5f52", "type": "reflection", "title": "Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口", "path": "vault/reflections/reflection-reflection_617843f93885fb6b0d3c5f52.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口\n\n## Why important\n\n它把价值函数从训练配件提升为贯穿数据筛选、质量条件策略学习和在线残差适应的接口，并强调历史条件价值对遮挡、重复动作和相似阶段歧义的处理。\n\n## What changed\n\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度…", "match_reason": "metadata:domains"}, {"id": "concept_4739daf4ef7eacc9153c535f", "type": "concept", "title": "可靠价值驱动的离线到在线策略改进", "path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "status": "working", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。", "match_reason": "metadata:aliases"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…mechanism\": \"[Robo-ValueRL] 与 UR-VC 都先提高进度或价值信号的可靠性，再让该信号参与策略改进。\",\n    \"boundary\": \"该连接只说明信号治理的共同位置，不表示训练式价值估计和无训练标签校正在方法或证据上等价。\",\n    \"difference\": \"UR-VC 校正离线时间代理；[Robo-ValueRL] 学习历史条件价值并延伸到在线数据筛选…", "match_reason": "full-text:body"}, {"id": "synthesis_a4a2bd5ddcee562f2574676f", "type": "synthesis", "title": "适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界", "path": "vault/synthesis/synthesis-synthesis_a4a2bd5ddcee562f2574676f.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_40700e61702f4b5a5765e11d", "source_6b52a51e2b4a3be43c97c386", "source_7b278ba348f2a8bb94cce1fc", "source_91072aa553af99e6ab97c6cd", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…[Robo-ValueRL] 与 ActionCache 都在允许后续优化或复用前，用一个中介分数判断状态进展、行为质量或上下文相似性。\",\n    \"boundary\": \"时间位置、历史价值与多模态相似度都只是代理；遮挡、接触状态、多解任务和动力学差异会让高分代理对应错误物理状态。\",\n    \"difference\": \"UR-VC 校正离线进度标签，[Robo]…", "match_reason": "full-text:body"}, {"id": "synthesis_1fdb28cc5ac38aa6f424e5e1", "type": "synthesis", "title": "精细与接触丰富操作中的 VLA 后训练：反馈接口、时间尺度与物理闭环", "path": "vault/synthesis/synthesis-synthesis_1fdb28cc5ac38aa6f424e5e1.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb", "source_37fe3c1f9d9fb7daa262fa91", "source_40700e61702f4b5a5765e11d", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_b7444ef42015f4f3b6f51032", "source_c79f943c818d06054ca5cf92", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…RL Token 与 PAC-ACT 对精密真机阶段或工业接触任务具有直接证据；FlowDAgger 提供可迁移的部署纠正机制；[Robo-ValueRL] 提供价值可靠性机制，但当前材料不足以把它限定为精细操作专用方法。\n- VLA 后训练主要改变跨回合或中低频策略适配，TouchWorld、TACTIC 与 TactiDex…", "match_reason": "full-text:body"}, {"id": "reflection_052db872e2258b0e016c5ebf", "type": "reflection", "title": "UR-VC：先纠正进度代理，再训练价值或优势条件策略", "path": "vault/reflections/reflection-reflection_052db872e2258b0e016c5ebf.md", "status": "active", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "…与 [Robo-ValueRL] 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。\n  Boundary: UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。\n  Difference: UR-VC 在训练前修正监督标签且不训练价值模型；[Robo]…", "match_reason": "full-text:body"}, {"id": "synthesis_60071a24c6e3071f6731c4e2", "type": "synthesis", "title": "VLA 后训练、动作观察接口与世界模型：分布、表示、反馈和可执行性", "path": "vault/synthesis/synthesis-synthesis_60071a24c6e3071f6731c4e2.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220", "source_4b25f596c34869693b9b8151", "source_4df1017326dd7cc4786f4218", "source_5b8c57a9bef3348109f3b7bb", "source_8b41a014bee47c4239a2fa81", "source_b64b4a539b8c17d0cfe662ba", "source_e6608d8f849ad472bbd95143", "source_ef80ef223077ef0855660839", "source_f4bd7390e1b485ab773f1446", "source_f9128ff3463cfaa7fa41ee7e", "source_fe986df678d73ef2b6234f0c"], "snippet": "…观察/世界表示决定哪些物理变化可被模型利用。\n- ExToken、RL Token、PAC-ACT、FlowDAgger、[Robo-ValueRL] 与 UR-VC 都把适配压力放到较小接口，但位置不同：行为条件、内部读出、动作块…", "match_reason": "full-text:body"}, {"id": "concept_abb38fe58cbeee09ce87a01d", "type": "concept", "title": "跨轨迹任务进度代理校正", "path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# 跨轨迹任务进度代理校正\n\n跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。", "match_reason": "metadata:aliases"}, {"id": "work_arxiv_1810_08647", "type": "work", "title": "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning", "path": "vault/memory/work/work_arxiv_1810_08647.md", "status": "working", "source_ids": ["source_e9ed0a3745aea832b64d7fa7", "source_c019c0a492cc659d7858134d"], "snippet": "# [1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep [Reinforcement] Learning\n\n## Logical work identity\n\n- arXiv：`1810…", "match_reason": "metadata:title"}, {"id": "claim_wechat_im_rl_framework_internal_rewards_20260716", "type": "claim", "title": "该文称经典 RL 虽常被视为仅处理外在奖励，但 Barto 等框架可将奖励生成机制置于「内部环境」，内在与外在奖励可统一建模", "path": "vault/memory/claim/claim_wechat_im_rl_framework_internal_rewards_20260716.md", "status": "working", "source_ids": ["source_91199da18f239c48bbcdd49f"], "snippet": "# RL 统一奖励\n\n内在奖励可在体内生成；RL 框架不必限定外部通道。", "match_reason": "metadata:tags"}, {"id": "concept_f9a9f1d1818632c0380b7942", "type": "concept", "title": "VLA 的强化学习读出接口", "path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "status": "working", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# VLA 的强化学习读出接口\n\nVLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 actor-critic 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。", "match_reason": "metadata:aliases"}, {"id": "claim_physo_rnn_reinforcement_learning_method_20260716", "type": "claim", "title": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式", "path": "vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。", "match_reason": "metadata:tags"}, {"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward…", "match_reason": "metadata:tags"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…That distinction helps organize post-training questions without treating [reinforcement] learning as one method.\n\n## What changed\n\nReliability gains…", "match_reason": "metadata:domains"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_4bec3f6febe9fd2b5e3f75e5", "type": "input", "title": "[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation", "path": "vault/inputs/input-input_4bec3f6febe9fd2b5e3f75e5.md", "status": "active", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# [2607.15982] Data and [Learning] Where it Matters for Contact-Rich Manipulation\n\nInput Episode for `source_42e52a18cc082f3af087d574`. The…", "match_reason": "metadata:title"}, {"id": "reflection_cf6022fc4f2c613119feca19", "type": "reflection", "title": "深度学习中的物理类比需要机制映射与可检验边界 / physical analogies in deep learning need testable mappings", "path": "vault/reflections/reflection-reflection_cf6022fc4f2c613119feca19.md", "status": "active", "source_ids": ["source_5047efa557dd30126284c9c2"], "snippet": "# 深度学习中的物理类比需要机制映射与可检验边界 / physical analogies in deep [learning] need testable mappings\n\n## Why important\n\n文章把最大似然、玻尔兹曼机、香农熵、热力学平衡与尺度重整化串联，说明物理词汇可帮助提出表征问题，却也容易把特定能量模型的形式对应泛化成所有深度学习方法的解释。\n\n## What…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_7b278ba348f2a8bb94cce1fc"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "9560d442d9287bd05f0f3be2b37fb85d2c91f26928051b806b8682e5f1a1ebc6"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Robo-ValueRL

## 编译边界

- Provider：`codex-strong-model-m91-weekly-v3`
- Extraction：`extraction_a288c4114d2d830f1678fd14`
- 编译前召回已有对象：18
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md
+++ candidate:vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md
@@ -1,39 +1,20 @@
 ---
 id: "concept_4739daf4ef7eacc9153c535f"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "可靠价值驱动的离线到在线策略改进"
 created_at: "2026-07-20T11:55:37+08:00"
-updated_at: "2026-07-20T11:56:59+08:00"
+updated_at: "2026-07-28T16:27:52+08:00"
 aliases: ["Robo-ValueRL", "value-guided offline-to-online adaptation"]
 tags: []
 domains: ["embodied-ai", "robot-rl", "vla", "value-learning"]
 confidence: "medium"
 source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
-relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}, {"type": "depends_on", "target_id": "concept_abb38fe58cbeee09ce87a01d", "reason": "当价值监督来自时间进度时，先校正跨轨迹进度代理是避免下游选择偏差自强化的上游条件。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
 change_reason: "compile bundle from source_7b278ba348f2a8bb94cce1fc"
-reflection_context: {"reflection_ids": ["reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
-consolidation_count: 1
-last_consolidated_at: "2026-07-20T11:56:59+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_4b54c5c2979985532fa7"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_4b54c5c2979985532fa7-concept-1.md"
-origin_candidate_sha256: "95db7958cead1edd694b45998b7c0f21f1921311c766c8fc3f0203026af8b8ff"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_bc26ef979b149316e780adba"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_052db872e2258b0e016c5ebf", "reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。\n同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}, {"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？", "价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
+proposed_status: "working"
 ---
 
 # 可靠价值驱动的离线到在线策略改进
```
