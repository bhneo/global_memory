---
id: "proposal_bundle_253826265ac2e65dd67a"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T18:19:43+08:00"
updated_at: "2026-07-27T18:19:44+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_1ee2c3fae53a9d05689cd143"]
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
extraction_id: "extraction_1998a230ecf9a34970134363"
input_sha256: "705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_c37ccf2640da63192432d5d5", "target_path": "vault/knowledge/concepts/concept_c37ccf2640da63192432d5d5-vla-的力历史记忆用于非-markov-接触操作-force-history-memory-for-non-markov-co.md", "base_sha256": null, "candidate_sha256": "0af4212e8de78ac9def5803a4c56eca6d0d456024dd2ee47b35ff18cd6342dea", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_253826265ac2e65dd67a-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_c37ccf2640da63192432d5d5.md", "working_at": "2026-07-27T18:19:44+08:00"}]
existing_context: [{"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_7952be977c24d5dfe1da2072", "type": "reflection", "title": "图式 Agent Memory：生命周期完整不等于证据闭环完整", "path": "vault/reflections/reflection-reflection_7952be977c24d5dfe1da2072.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92"], "snippet": "# 图式 Agent [Memory]：生命周期完整不等于证据闭环完整\n\n## Why important\n\n这份综述把 Agent [Memory] 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测…", "match_reason": "metadata:title"}, {"id": "synthesis_7084bca907043e3cba4afb7e", "type": "synthesis", "title": "Agent Memory 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界", "path": "vault/synthesis/synthesis-synthesis_7084bca907043e3cba4afb7e.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92", "source_11bc6c51fa038191e33bc9a7", "source_6ada1b3b0033883b83a3bf40", "source_6b52a51e2b4a3be43c97c386"], "snippet": "# Agent [Memory] 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界\n\n## Emerging patterns\n\n- 长期 Agent [Memory] 与物理 Agent 基础设施共享同一结构要求：状态必须可外化、更新必须可定位、失败必须能回到产生它的感知…", "match_reason": "metadata:title"}, {"id": "concept_language_corrective_memory_data_flywheel", "type": "concept", "title": "语言纠错记忆驱动的机器人数据飞轮", "path": "vault/memory/concept/concept_language_corrective_memory_data_flywheel.md", "status": "working", "source_ids": ["source_5e14510061220db7f2344913"], "snippet": "# 语言纠错记忆驱动的机器人数据飞轮\n\nZero2Skill 让自主 Agent 采集演示，在失败复现时接收简短人类语言修正，将其持久化为 Corrective [Memory]，并用视觉验证和轨迹认证决定重试与入库；随后用合格数据微调策略并部署。该闭环可降低持续遥操作负担，但其数据质量取决于工具执行、视觉验证器和任务分布，采集成功率不能替代下游策略评测。", "match_reason": "metadata:aliases"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:aliases"}, {"id": "concept_f35cd7f55e4108ce45ec35d7", "type": "concept", "title": "面向异构机器人策略的能力边界路由与记忆交接", "path": "vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md", "status": "working", "source_ids": ["source_cc2f2812863ca6751c223b54"], "snippet": "# 面向异构机器人策略的能力边界路由与记忆交接\n\nRoboHarness 将独立开发的 VLA、强化学习和任务运动规划控制器封装为可路由模块，并用多模态执行记忆和在线证据估计各策略在当前子任务中的适用边界；在策略切换前，其 [Memory] Bridge 检索与下一策略相关的执行轨迹、估计该策略的分布内状态区域，并引导机器人接近该区域，以降低未经联合训练的控制器之间的状态分布错配。该机制的效果仍取决于能力估计、状态表示和检索轨迹对实际交接条件的覆盖。", "match_reason": "metadata:aliases"}, {"id": "concept_native_action_aligned_vla_memory", "type": "concept", "title": "动作对齐的 VLA 原生视觉记忆压缩", "path": "vault/memory/concept/concept_native_action_aligned_vla_memory.md", "status": "working", "source_ids": ["source_748cef2215ddc958568e6368"], "snippet": "# 动作对齐的 VLA 原生视觉记忆压缩\n\nNativeMEM 将每个历史帧—相机视角压缩为一个与预训练 VLA token 维度兼容的记忆 token；第一阶段冻结 VLA，仅以原动作预测损失训练由视觉编码器初始化的 [memory] tokenizer，第二阶段缓存 token 并微调策略…", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# Latent [Memory] Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "experiment_7101e03fb065226e65f388a5", "type": "experiment", "title": "Cursor M7 真实读取与 receipt 回写验收", "path": "vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md", "status": "working", "source_ids": ["source_113d589e6dadf14b5fa8edea"], "snippet": "# Cursor M7 真实读取与 receipt 回写验收\n\n## 验收路径\n\nCursor 按协议读取了 `AGENTS.md`、`.cursor/rules/global-[memory].mdc` 和 `vault/INDEX…", "match_reason": "metadata:domains"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language]-Action Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_76b68fdb85fc376d2226e524", "type": "input", "title": "[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents", "path": "vault/inputs/input-input_76b68fdb85fc376d2226e524.md", "status": "active", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "…Physics-based World Modeling with [Vision-Language] Agents\n\nInput Episode for `source_4ceaa5243dd0d99116547dda`. The immutable Source remains authoritative…", "match_reason": "full-text:body"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for [Vision-Language]-Action Models with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_adaptive_interleaved_multimodal_planning", "type": "concept", "title": "自适应交错多模态规划", "path": "vault/memory/concept/concept_adaptive_interleaved_multimodal_planning.md", "status": "working", "source_ids": ["source_4ac7cf9f4fce43551683a04b"], "snippet": "# 自适应交错多模态规划\n\n长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_1ee2c3fae53a9d05689cd143"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "50c19c606256143de366d87e3677e9ec9e115e13823d820bc2d905bed192d9d0"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_1998a230ecf9a34970134363`
- 编译前召回已有对象：13
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_c37ccf2640da63192432d5d5-vla-的力历史记忆用于非-markov-接触操作-force-history-memory-for-non-markov-co.md
@@ -0,0 +1,20 @@
+---
+id: "concept_c37ccf2640da63192432d5d5"
+type: "concept"
+status: "proposal"
+title: "VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation"
+created_at: "2026-07-27T18:19:43+08:00"
+updated_at: "2026-07-27T18:19:43+08:00"
+aliases: ["FM-VLA", "force-based memory VLA", "力历史记忆 VLA"]
+tags: []
+domains: ["robotics", "vision-language-action", "force-sensing"]
+confidence: "medium"
+source_ids: ["source_1ee2c3fae53a9d05689cd143"]
+relations: [{"type": "derived_from", "target_id": "source_1ee2c3fae53a9d05689cd143", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_1ee2c3fae53a9d05689cd143"
+reflection_context: {"reflection_ids": ["reflection_bd1bc1b00ef5304ee9d29e9c"], "importance": "high", "changed_belief": "我会把力传感视为接触事件进度的专用时序记忆，而不把它当成对视觉记忆或一般 VLA 长时推理的无条件替代。", "surprising": "", "connections": [{"shared_mechanism": "两者都以额外时序表征弥补单帧 VLA 的 Markov 假设。", "boundary": "本文限于可获得的 wrench 信号、VAE 压缩、三个记忆依赖任务和论文评测。", "difference": "视觉记忆存储图像帧且可能模糊昂贵；本文将接触/重复事件编码为紧凑 force token。"}], "open_questions": ["传感漂移、不同末端执行器和新接触材料下，force memory 的后验事件语义如何校准？"]}
+---
+
+# VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation
+
+在接触丰富、视觉事件含糊的非 Markov 操作中，可将力/力矩历史经预训练 VAE 压缩为 force-memory tokens，并连同短状态历史条件化 VLA 的 action expert，以保留接触事件和重复进度。该方法依赖可靠 wrench 传感、压缩器训练及论文任务，不保证替代视觉记忆或泛化到任意接触分布。
```
