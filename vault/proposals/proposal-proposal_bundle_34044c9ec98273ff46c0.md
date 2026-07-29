---
id: "proposal_bundle_34044c9ec98273ff46c0"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T16:30:52+08:00"
updated_at: "2026-07-28T16:31:09+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_40700e61702f4b5a5765e11d"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-strong-model-m91-weekly-v3"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_4fd58691d04124ef005981f1"
input_sha256: "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_asymmetric_frozen_vla_harness", "target_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "base_sha256": "03a7e9247486eb4450b88bd99d1febfec8bb300298ac3a56abf062d1f2f1d200", "candidate_sha256": "a4bef34d44b822ef8c7a1ff5b90f86422385aa1a0afb7f749cf3442978b68221", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_34044c9ec98273ff46c0-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_34044c9ec98273ff46c0-concept-1.md", "working_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-28T16:31:09+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "# VLA 后训练的反馈接口：价值、[Token]、动作块与潜空间干预\n\n## Emerging patterns\n\n- VLA 后训练的瓶颈不只是优化算法，而是基础策略向纠正过程暴露什么反馈接口：进度标签、价值、内部 [token]、动作块或生成潜变量。\n- 五条路径都试图保留预训练行为先验，只把学习压力放到较小的标签、读出…", "match_reason": "metadata:title"}, {"id": "reflection_5b4f45d757e5b256cdddfcfa", "type": "reflection", "title": "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口", "path": "vault/reflections/reflection-reflection_5b4f45d757e5b256cdddfcfa.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口\n\n## Why important\n\n它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 actor-critic 通过紧凑 RL token 在少量真机交互中适应精密阶段…", "match_reason": "metadata:domains"}, {"id": "reflection_bd1bc1b00ef5304ee9d29e9c", "type": "reflection", "title": "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens", "path": "vault/reflections/reflection-reflection_bd1bc1b00ef5304ee9d29e9c.md", "status": "active", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# FM-VLA：力历史将接触进度压缩为记忆 [token] / force history compresses contact progress into memory tokens\n\n## Why important\n\nFM-VLA 以预训练 VAE…", "match_reason": "metadata:title"}, {"id": "reflection_c3b3e3b0cbbc4d820aa25ce5", "type": "reflection", "title": "CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化", "path": "vault/reflections/reflection-reflection_c3b3e3b0cbbc4d820aa25ce5.md", "status": "active", "source_ids": ["source_f4bd7390e1b485ab773f1446"], "snippet": "# CLAP：人类视频需先对齐到机器人可执行 [token]，而不是直接重建视觉变化\n\n## Why important\n\nCLAP 先从机器人轨迹学习量化、可执行动作词表，再用对比学习把人类视觉转移对齐到该词表，试图避免 latent action 被背景变化和外观噪声主导。\n\n## What changed\n\n人类视频规模本身不足以保证机器人迁移；若…", "match_reason": "metadata:title"}, {"id": "reflection_65ee736483d758905945535d", "type": "reflection", "title": "NativeMEM：让记忆表征服从冻结 VLA 的动作接口", "path": "vault/reflections/reflection-reflection_65ee736483d758905945535d.md", "status": "active", "source_ids": ["source_748cef2215ddc958568e6368"], "snippet": "# NativeMEM：让记忆表征服从冻结 VLA 的动作接口\n\n## Why important\n\n它把长时记忆的瓶颈从外部存储容量转为与既有动作策略的表示兼容性：每个帧—视角只保留一个 [token]，但用冻结 VLA 的原动作损失训练该 [token]。\n\n## What changed\n\n长时视觉记忆不一定需要独立记忆模型；在该设定中…", "match_reason": "full-text:body"}, {"id": "synthesis_1fdb28cc5ac38aa6f424e5e1", "type": "synthesis", "title": "精细与接触丰富操作中的 VLA 后训练：反馈接口、时间尺度与物理闭环", "path": "vault/synthesis/synthesis-synthesis_1fdb28cc5ac38aa6f424e5e1.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb", "source_37fe3c1f9d9fb7daa262fa91", "source_40700e61702f4b5a5765e11d", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_b7444ef42015f4f3b6f51032", "source_c79f943c818d06054ca5cf92", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# 精细与接触丰富操作中的 VLA 后训练：反馈接口、时间尺度与物理闭环\n\n## Emerging patterns\n\n- 精细与接触丰富操作不是单一算法类别，而是同时要求任务进度或价值判断、可在线优化的策略表示、与动作时间尺度一致的信用分配、部署纠正入口以及高频物理接触闭环。\n- RL [Token] 与 PAC-ACT 对精密真机阶段或工业接触任务具有直接证据…", "match_reason": "full-text:body"}, {"id": "concept_f9a9f1d1818632c0380b7942", "type": "concept", "title": "VLA 的强化学习读出接口", "path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "status": "working", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# VLA 的强化学习读出接口\n\nVLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL [token]，供小型 actor-critic 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。", "match_reason": "metadata:aliases"}, {"id": "concept_9443d1789c9a179bd1611be3", "type": "concept", "title": "示范先验条件化的 VLA 结构化探索", "path": "vault/memory/concept/concept_9443d1789c9a179bd1611be3.md", "status": "working", "source_ids": ["source_5b8c57a9bef3348109f3b7bb"], "snippet": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 [token] 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。", "match_reason": "metadata:aliases"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…offline iteration and [online] off-policy VLA post-training are distinct paths\n\n## Why important\n\nThe notes separate an…", "match_reason": "metadata:title"}, {"id": "concept_4739daf4ef7eacc9153c535f", "type": "concept", "title": "可靠价值驱动的离线到在线策略改进", "path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "status": "working", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。", "match_reason": "metadata:aliases"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2…", "match_reason": "metadata:tags"}, {"id": "reflection_617843f93885fb6b0d3c5f52", "type": "reflection", "title": "Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口", "path": "vault/reflections/reflection-reflection_617843f93885fb6b0d3c5f52.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口\n\n## Why important\n\n它把价值函数从训练配件提升为贯穿数据筛选、质量条件策略学习和在线残差适应的接口，并强调历史条件价值对遮挡、重复动作和相似阶段歧义的处理。\n\n## What changed\n\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度…", "match_reason": "metadata:domains"}, {"id": "input_2ca715edb7e129a6233c5a92", "type": "input", "title": "[1005.3035] Building up spacetime with quantum entanglement", "path": "vault/inputs/input-input_2ca715edb7e129a6233c5a92.md", "status": "active", "source_ids": ["source_ddde97eaf66d06d61a930ffa"], "snippet": "# [1005.3035] Building up spacetime [with] quantum entanglement\n\nInput Episode for `source_ddde97eaf66d06d61a930ffa`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "input_3b93bb83f5c7407a5a03dcad", "type": "input", "title": "Building scalable AI agents with modular prompt transpilation - Google Developers Blog", "path": "vault/inputs/input-input_3b93bb83f5c7407a5a03dcad.md", "status": "active", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# Building scalable AI agents [with] modular prompt transpilation - Google Developers Blog\n\nInput Episode for `source_3521fe9ac8d8f054440ec0af`. The immutable…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_40700e61702f4b5a5765e11d"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "2be8f6b637647bb53d07bf3052361aa8c21535a0d138a25ac1c27b5c015c2055"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-strong-model-m91-weekly-v3`
- Extraction：`extraction_4fd58691d04124ef005981f1`
- 编译前召回已有对象：16
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md
+++ candidate:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md
@@ -1,43 +1,20 @@
 ---
 id: "concept_asymmetric_frozen_vla_harness"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "冻结 VLA 的非对称技能编排"
 created_at: "2026-07-19T12:18:32+08:00"
-updated_at: "2026-07-26T12:32:08+08:00"
+updated_at: "2026-07-28T16:30:52+08:00"
 aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA", "physical-agent service shell", "物理 Agent 服务化外壳", "agentic infrastructure for the physical world"]
 tags: []
 domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation", "agent-infrastructure", "robot-memory"]
 confidence: "medium"
-source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54"]
-relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}]
-change_reason: "compile bundle from source_cc2f2812863ca6751c223b54"
-uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 3
-last_consolidated_at: "2026-07-26T12:32:08+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_84924618ed7bb77a5704"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_84924618ed7bb77a5704-concept-1.md"
-origin_candidate_sha256: "ca740123df7e1d552efc8343f658d1a9ead0389bf71134ba9696bb6be738e466"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_2106b8ba77589a752cb82655"
+source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54", "source_40700e61702f4b5a5765e11d"]
+relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "外壳编排和 RL 读出都保留基础 VLA，但分别吸收任务级执行反馈与标量奖励。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "外部原语重组与生成潜空间干预是两种不同适配位置，支持域与故障归因必须分别验证。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
+change_reason: "compile bundle from source_40700e61702f4b5a5765e11d"
 change_type: "refine"
-reflection_context: {"reflection_ids": ["reflection_5eb9ba718b0b143e55d0b020", "reflection_d3da57bd40bcce58fcac3b37"], "importance": "weekly", "changed_belief": "此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。\n此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。", "surprising": "读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。", "connections": [{"shared_mechanism": "FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。", "boundary": "连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。", "difference": "FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。"}, {"shared_mechanism": "两者都把冻结或独立训练的控制模块置于更高层的适用范围管理与失败恢复接口之下。", "boundary": "该连接适用于存在可辨识子任务、可记录执行状态且能在切换前评估下一策略输入条件的长时程机器人系统。", "difference": "RoboHarness 以执行轨迹检索和空间分布学习来引导交接；既有冻结 VLA 编排概念以原语、验证与重试来约束局部专家。"}], "open_questions": ["如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？"]}
+reflection_context: {"reflection_ids": ["reflection_4430cc70fe95425f717c1e71", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_cd269bee56819aafec2fd5a3"], "importance": "weekly", "changed_belief": "此前容易把 VLA 后训练等同于更新策略参数；RPent 的工程路线提示，冻结 VLA 也可被上层 Agent 组织成可复用操作原语，但这类系统收益必须与底层 VLA 本身的能力分开评估。\nVLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。\n人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。", "surprising": "仓库把 Claude Code、Codex 或 API 模型作为可替换 cerebrum，并允许复用独立 VLA 与环境服务，说明其核心抽象是异构智能编排而非单一模型。\n收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。\n人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger 风格干预能够训练潜空间控制器。", "connections": [{"shared_mechanism": "与 VIA 都把基础机器人策略或控制能力封装成 Agent 可调用的界面，通过观察、规划、执行和再观察形成闭环。", "boundary": "当前 Source 是 RPent 官方 GitHub README，只能支持项目设计与安装接口；Harness VLA 的论文方法、实验和可靠性结论仍需回到 arXiv 2607.08448 核验。", "difference": "VIA 论文研究通用视觉 Agent 直接操纵工具接口；RPent 是包含记忆、VLA 服务、环境服务和可替换 cerebrum 的递归基础设施。"}, {"shared_mechanism": "与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。", "boundary": "RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。", "difference": "RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。"}, {"shared_mechanism": "与 RL Token 都把大模型保持为稳定行为先验，只训练小型中间接口。", "boundary": "FlowDAgger 限于可执行动作反演的流匹配或扩散生成策略，并依赖人类在分布偏移处提供纠正。", "difference": "FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 actor-critic；两者的信息来源和安全成本不同。"}], "open_questions": ["Harness VLA 中 memory-guided steering 的具体记忆单元、失败恢复机制和相对无记忆基线收益是什么？", "RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？", "动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？"]}
 proposed_status: "working"
-change_history: [{"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "changed_fields": [], "reason": "compile bundle from source_6b52a51e2b4a3be43c97c386", "trigger_source": "source_6b52a51e2b4a3be43c97c386", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。", "changed_fields": [], "reason": "compile bundle from source_cc2f2812863ca6751c223b54", "trigger_source": "source_cc2f2812863ca6751c223b54", "evidence_added": []}]
 ---
 
 # 冻结 VLA 的非对称技能编排
@@ -51,3 +28,7 @@
 ## 新增来源材料
 
 - `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。
+
+## 新增来源材料
+
+- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。
```
