---
id: "proposal_bundle_455f79945d183512f000"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T19:03:58+08:00"
updated_at: "2026-07-27T19:04:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_1ee2c3fae53a9d05689cd143"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-m91-weekly-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_1998a230ecf9a34970134363"
input_sha256: "705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_2ce226e08d585158c1dfbb18", "target_path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "base_sha256": "1ea0dae94b6cad5dee3b4989ee0180d9faeb10d6162a062b5aeb51af06a08ab4", "candidate_sha256": "723174f814eaaf3f240b812126760e3b3fe4fcb7197cf38ef2cba15628702ac5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_455f79945d183512f000-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_455f79945d183512f000-concept-1.md", "working_path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-27T19:04:48+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_bd1bc1b00ef5304ee9d29e9c", "type": "reflection", "title": "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens", "path": "vault/reflections/reflection-reflection_bd1bc1b00ef5304ee9d29e9c.md", "status": "active", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into [memory] tokens\n\n## Why important\n\nFM-VLA 以预训练 VAE…", "match_reason": "metadata:title"}, {"id": "concept_c37ccf2640da63192432d5d5", "type": "concept", "title": "VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation", "path": "vault/memory/concept/concept_c37ccf2640da63192432d5d5.md", "status": "working", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# VLA 的力历史记忆用于非 Markov 接触操作 / force-history [memory] for non-Markov contact-rich VLA manipulation\n\n在接触丰富、视觉事件含糊的非 Markov 操作中…", "match_reason": "metadata:title"}, {"id": "synthesis_3a3249675668a93b9087ee43", "type": "synthesis", "title": "边界先于统一：视界热力学、Kakeya、动力学极限与流式接触控制的四条机制链", "path": "vault/synthesis/synthesis-synthesis_3a3249675668a93b9087ee43.md", "status": "active", "source_ids": ["source_086150581c4c39aee0813d57", "source_1ee2c3fae53a9d05689cd143", "source_299adfe6dd42f97b6f75b777", "source_323f116c3573f26f4af7785d", "source_32ee0cb3589fdf1de3cb8542", "source_3851b9ffbfbae3ca166308fd", "source_396cec9f720ec3afa4a7e9ad", "source_3c493939fefd8cf6ca2e4ba2", "source_408691502cdb43e7e2ea5c3b", "source_443db75c1157e4ee28fb3ea0", "source_4757ec1a2e8a0b678a350ee1", "source_4be2cb176dad6fdd8673bd31", "source_60c6677de9abc0b4e62a7dbe", "source_63ea95cc7031bab39a9b7461", "source_6b6bf6a9d857d2e74c2037ba", "source_6c565d5532cc4f2d0020ba4f", "source_7ab41149787a9cd99bd2fe58", "source_84c8c0edd41364ae0542b7ca", "source_9ec7a0dfcdc6c43339383f13", "source_a44d98212ed6d44a4998646e", "source_a9cfdeabfce614c49a3a92a1", "source_ad785f5be8067788394ec708", "source_b6d55666cda69c2a1c407986", "source_bd59f7e9cadcd7af4910d1e9", "source_bee998153a82cd2a92db045b", "source_cf15e6b90aaf4c6584d5efe2", "source_d211d7e773bf278ce50a7ac8", "source_ddde97eaf66d06d61a930ffa", "source_e67cd99ac31c7017d6f7f7c7", "source_e8651a193623cbe2b86becb0", "source_ebf287b4d71ccdc41101466e"], "snippet": "…[FM-VLA] 把更长的 wrench 历史压缩为 force-memory tokens，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。\",\n    \"reason\": \"[FM]…", "match_reason": "full-text:body"}, {"id": "reflection_7952be977c24d5dfe1da2072", "type": "reflection", "title": "图式 Agent Memory：生命周期完整不等于证据闭环完整", "path": "vault/reflections/reflection-reflection_7952be977c24d5dfe1da2072.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92"], "snippet": "# 图式 Agent [Memory]：生命周期完整不等于证据闭环完整\n\n## Why important\n\n这份综述把 Agent [Memory] 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测…", "match_reason": "metadata:title"}, {"id": "synthesis_7084bca907043e3cba4afb7e", "type": "synthesis", "title": "Agent Memory 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界", "path": "vault/synthesis/synthesis-synthesis_7084bca907043e3cba4afb7e.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92", "source_11bc6c51fa038191e33bc9a7", "source_6ada1b3b0033883b83a3bf40", "source_6b52a51e2b4a3be43c97c386"], "snippet": "# Agent [Memory] 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界\n\n## Emerging patterns\n\n- 长期 Agent [Memory] 与物理 Agent 基础设施共享同一结构要求：状态必须可外化、更新必须可定位、失败必须能回到产生它的感知…", "match_reason": "metadata:title"}, {"id": "concept_language_corrective_memory_data_flywheel", "type": "concept", "title": "语言纠错记忆驱动的机器人数据飞轮", "path": "vault/memory/concept/concept_language_corrective_memory_data_flywheel.md", "status": "working", "source_ids": ["source_5e14510061220db7f2344913"], "snippet": "# 语言纠错记忆驱动的机器人数据飞轮\n\nZero2Skill 让自主 Agent 采集演示，在失败复现时接收简短人类语言修正，将其持久化为 Corrective [Memory]，并用视觉验证和轨迹认证决定重试与入库；随后用合格数据微调策略并部署。该闭环可降低持续遥操作负担，但其数据质量取决于工具执行、视觉验证器和任务分布，采集成功率不能替代下游策略评测。", "match_reason": "metadata:aliases"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:aliases"}, {"id": "concept_f35cd7f55e4108ce45ec35d7", "type": "concept", "title": "面向异构机器人策略的能力边界路由与记忆交接", "path": "vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md", "status": "working", "source_ids": ["source_cc2f2812863ca6751c223b54"], "snippet": "# 面向异构机器人策略的能力边界路由与记忆交接\n\nRoboHarness 将独立开发的 VLA、强化学习和任务运动规划控制器封装为可路由模块，并用多模态执行记忆和在线证据估计各策略在当前子任务中的适用边界；在策略切换前，其 [Memory] Bridge 检索与下一策略相关的执行轨迹、估计该策略的分布内状态区域，并引导机器人接近该区域，以降低未经联合训练的控制器之间的状态分布错配。该机制的效果仍取决于能力估计、状态表示和检索轨迹对实际交接条件的覆盖。", "match_reason": "metadata:aliases"}, {"id": "concept_native_action_aligned_vla_memory", "type": "concept", "title": "动作对齐的 VLA 原生视觉记忆压缩", "path": "vault/memory/concept/concept_native_action_aligned_vla_memory.md", "status": "working", "source_ids": ["source_748cef2215ddc958568e6368"], "snippet": "# 动作对齐的 VLA 原生视觉记忆压缩\n\nNativeMEM 将每个历史帧—相机视角压缩为一个与预训练 VLA token 维度兼容的记忆 token；第一阶段冻结 VLA，仅以原动作预测损失训练由视觉编码器初始化的 [memory] tokenizer，第二阶段缓存 token 并微调策略…", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# Latent [Memory] Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language]-Action Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_76b68fdb85fc376d2226e524", "type": "input", "title": "[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents", "path": "vault/inputs/input-input_76b68fdb85fc376d2226e524.md", "status": "active", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "…Physics-based World Modeling with [Vision-Language] Agents\n\nInput Episode for `source_4ceaa5243dd0d99116547dda`. The immutable Source remains authoritative…", "match_reason": "full-text:body"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for [Vision-Language]-Action Models with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_adaptive_interleaved_multimodal_planning", "type": "concept", "title": "自适应交错多模态规划", "path": "vault/memory/concept/concept_adaptive_interleaved_multimodal_planning.md", "status": "working", "source_ids": ["source_4ac7cf9f4fce43551683a04b"], "snippet": "# 自适应交错多模态规划\n\n长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_1ee2c3fae53a9d05689cd143"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "4db87857dd0056f1b4665760b1ad95fa89b74c0cb33946ea371f11e94c06d933"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-m91-weekly-v2`
- Extraction：`extraction_1998a230ecf9a34970134363`
- 编译前召回已有对象：16
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md
+++ candidate:vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_2ce226e08d585158c1dfbb18"
 type: "concept"
-status: "working"
-title: "保留视觉语言先验的块内反应式力注入"
+status: "proposal"
+title: "接触反馈应区分短时反应、事件记忆与概率后验"
 created_at: "2026-07-24T18:06:12+08:00"
-updated_at: "2026-07-26T12:33:29+08:00"
+updated_at: "2026-07-27T19:03:58+08:00"
 aliases: ["Late Reactive Force Injection", "LIFT", "反应式力注入 VLA 后训练"]
 tags: []
 domains: ["vla", "force-control", "contact-rich-manipulation"]
 confidence: "medium"
-source_ids: ["source_4e06d1b1cdcd0d07eff47909"]
-relations: [{"type": "derived_from", "target_id": "source_4e06d1b1cdcd0d07eff47909", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_637cf7264723c03955c719e2", "reason": "两者都使用交互中的附加信号缓解视觉歧义；本概念采用显式力记忆和反应分支，既有概念采用遥操作跟踪偏差这一隐式 proxy。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_4e06d1b1cdcd0d07eff47909"
-reflection_context: {"reflection_ids": ["reflection_1f5ecace3c0b5fd265b9d846"], "importance": "high", "changed_belief": "接触传感并非只能作为全模型重训的额外输入；若初始化时严格保持原动作输出，稀缺的在线力纠正可以针对策略实际访问的接触失败状态进行局部适配。", "surprising": "", "connections": [{"shared_mechanism": "两者都通过补充交互信号来弥补纯视觉在接触状态中的可观测性缺口。", "boundary": "该连接适用于力、力矩或跟踪偏差能可靠反映接触变化的控制系统，不说明任一 proxy 在所有硬件上等价于测得六维力。", "difference": "LIFT 显式编码近期六维末端力并在动作块内反应；既有概念讨论遥操作 leader–follower 的跟踪偏差作为隐式线索。"}], "open_questions": []}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-26T12:33:29+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_22e03e8c0d0697f12bc0"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_22e03e8c0d0697f12bc0-concept-1.md"
-origin_candidate_sha256: "b2388e92015056e7b66a969bfa97c7d87752f7109cfbaf4954b5921bad16185c"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_e13d2e635e0a7fba7ce66948"
+source_ids: ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"]
+relations: [{"type": "derived_from", "target_id": "source_4e06d1b1cdcd0d07eff47909", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_637cf7264723c03955c719e2", "reason": "两者都使用交互中的附加信号缓解视觉歧义；本概念采用显式力记忆和反应分支，既有概念采用遥操作跟踪偏差这一隐式 proxy。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_c37ccf2640da63192432d5d5", "reason": "LIFT 的近期力窗口服务动作块内反应，FM-VLA 的压缩力历史服务非 Markov 接触事件记忆；两者共享 wrench 信号，但时间范围和功能边界不同。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_bb69fa188e0417143c3277cf", "reason": "力历史与姿态粒子后验都缓解接触状态的部分可观测性；前者编码已发生的事件，后者表示当前几何不确定性，不能互相替代。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_1ee2c3fae53a9d05689cd143"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_438aaa4e8fa10fc299c05d87", "reflection_bd1bc1b00ef5304ee9d29e9c"], "importance": "weekly", "changed_belief": "我会要求接触融合方法明确说明后验表示、仿真前向模型和新几何/环境下的适用边界，而不把仿真推断自动等同于无训练泛化。\n我会把力传感视为接触事件进度的专用时序记忆，而不把它当成对视觉记忆或一般 VLA 长时推理的无条件替代。", "surprising": "", "connections": [{"shared_mechanism": "两者都用视觉和接触信息缩小接触操作中的状态不确定性。", "boundary": "本文限于 peg-in-hole、粒子 belief、深度和 force/torque 接触证据以及仿真前向模型。", "difference": "深度单独估计输出单一几何匹配；本文用 simulation-based inference 对多个候选位姿加权。"}, {"shared_mechanism": "两者都以额外时序表征弥补单帧 VLA 的 Markov 假设。", "boundary": "本文限于可获得的 wrench 信号、VAE 压缩、三个记忆依赖任务和论文评测。", "difference": "视觉记忆存储图像帧且可能模糊昂贵；本文将接触/重复事件编码为紧凑 force token。"}], "open_questions": ["接触模型失配和未见材料摩擦下，后验校准如何影响闭环插入成功率？", "传感漂移、不同末端执行器和新接触材料下，force memory 的后验事件语义如何校准？"]}
+proposed_status: "working"
 ---
 
 # 保留视觉语言先验的块内反应式力注入
 
 对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。
+
+## 新增来源材料
+
+- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM-VLA 把更长的 wrench 历史压缩为 force-memory tokens，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。
```
