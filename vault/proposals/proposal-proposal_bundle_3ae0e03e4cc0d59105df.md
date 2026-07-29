---
id: "proposal_bundle_3ae0e03e4cc0d59105df"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T19:02:43+08:00"
updated_at: "2026-07-27T19:03:31+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e67cd99ac31c7017d6f7f7c7"]
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
extraction_id: "extraction_87395cad2f1d5fa88a1f4db4"
input_sha256: "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_a858f8d191d3afdd69418471", "target_path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "base_sha256": "bde8f1c73d6783882225367e8b2fd4de43db7224ec3503f015848299f6267042", "candidate_sha256": "7596ef34a5aad1b92a78e653e0514f7eeeb3cb1b2efc36f02360aeeda36bc9ae", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3ae0e03e4cc0d59105df-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_3ae0e03e4cc0d59105df-concept-1.md", "working_path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-27T19:03:31+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_d8d4183ecacf40814756f4c2", "type": "reflection", "title": "Reflex 流式 VLA：缓存正确性来自上下文分区 / Reflex streaming VLA preserves caching through context partitioning", "path": "vault/reflections/reflection-reflection_d8d4183ecacf40814756f4c2.md", "status": "active", "source_ids": ["source_e67cd99ac31c7017d6f7f7c7"], "snippet": "# [Reflex] 流式 VLA：缓存正确性来自上下文分区 / [Reflex] streaming VLA preserves caching through context partitioning\n\n## Why important\n\n[Reflex] 将 flow-matching…", "match_reason": "metadata:title"}, {"id": "concept_30d85c442682f6afd96c3022", "type": "concept", "title": "Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs", "path": "vault/memory/concept/concept_30d85c442682f6afd96c3022.md", "status": "working", "source_ids": ["source_e67cd99ac31c7017d6f7f7c7"], "snippet": "# Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs\n\n在论文所述 flow…", "match_reason": "metadata:domains"}, {"id": "concept_a858f8d191d3afdd69418471", "type": "concept", "title": "陈旧性对齐的异步慢上下文—快控制接口", "path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "status": "working", "source_ids": ["source_d4762e0cf2330ab6ea00a521"], "snippet": "# 陈旧性对齐的异步慢上下文—快控制接口\n\n在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。", "match_reason": "metadata:aliases"}, {"id": "reflection_743b2d2d30d2f822bf2bfb9f", "type": "reflection", "title": "FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口", "path": "vault/reflections/reflection-reflection_743b2d2d30d2f822bf2bfb9f.md", "status": "active", "source_ids": ["source_d4762e0cf2330ab6ea00a521"], "snippet": "# FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口\n\n## Why important\n\n该工作把慢速语言与历史聚合、快速当前帧动作预测通过逐层 KV cache 接口解耦，并用随机陈旧性训练匹配异步部署分布；它把实时控制从单纯模型压缩问题改写为时间尺度、缓存一致性与新鲜观测融合的接口问题。\n\n## What changed\n\n此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支…", "match_reason": "metadata:domains"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…embodiment constraints.\n\n## Surprising\n\nOne co-tracking controller supports [real-time] teleoperation across two dexterous hands and seven tasks…", "match_reason": "full-text:body"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…do the repository's workspace schema, failure traces, [real-time] deadlines, and safety refusal mechanisms work in code…", "match_reason": "full-text:body"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language-Action] Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for [Vision-Language-Action] Models with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_c37ccf2640da63192432d5d5", "type": "concept", "title": "VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation", "path": "vault/memory/concept/concept_c37ccf2640da63192432d5d5.md", "status": "working", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation\n\n在接触丰富、视觉事件含糊的非 Markov 操作中…", "match_reason": "metadata:domains"}, {"id": "reflection_bd1bc1b00ef5304ee9d29e9c", "type": "reflection", "title": "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens", "path": "vault/reflections/reflection-reflection_bd1bc1b00ef5304ee9d29e9c.md", "status": "active", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens\n\n## Why important\n\nFM-VLA 以预训练 VAE…", "match_reason": "metadata:domains"}, {"id": "input_ece052248dd2c432913efd3a", "type": "input", "title": "[2607.18236] Patch Policy: Efficient Embodied Control via Dense Visual Representations", "path": "vault/inputs/input-input_ece052248dd2c432913efd3a.md", "status": "active", "source_ids": ["source_e8651a193623cbe2b86becb0"], "snippet": "…Efficient Embodied [Control] via Dense Visual Representations\n\nInput Episode for `source_e8651a193623cbe2b86becb0`. The immutable Source remains authoritative.\n\n# [2607…", "match_reason": "metadata:title"}, {"id": "work_arxiv_2607_11119", "type": "work", "title": "VIA: Interface-first Robot Control", "path": "vault/memory/work/work_arxiv_2607_11119.md", "status": "working", "source_ids": ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"], "snippet": "…Interface-first Robot [Control]\n\n## Logical work identity\n\n- arXiv：`2607.11119`\n- Version：`v1`\n- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`\n\n此对象聚合现实世界作品身份…", "match_reason": "metadata:title"}, {"id": "concept_cdbe55276db1fb0eb0aa370a", "type": "concept", "title": "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere equilibrium fluctuations", "path": "vault/memory/concept/concept_cdbe55276db1fb0eb0aa370a.md", "status": "working", "source_ids": ["source_3851b9ffbfbae3ca166308fd", "source_323f116c3573f26f4af7785d"], "snippet": "# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time [control] of hard-sphere fluctuations\n\n对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann…", "match_reason": "metadata:title"}, {"id": "reflection_70e994e4dbf7cffe990580af", "type": "reflection", "title": "硬球长时相关：全时控制只落在平衡二阶涨落层 / global control is for equilibrium second-order fluctuations", "path": "vault/reflections/reflection-reflection_70e994e4dbf7cffe990580af.md", "status": "active", "source_ids": ["source_a5f4d6734479eea71ff9a2a4"], "snippet": "# 硬球长时相关：全时控制只落在平衡二阶涨落层 / global [control] is for equilibrium second-order fluctuations\n\n## Why important\n\n可复用的认知价值是将“突破 Lanford 短时限制”限定为平衡附近协方差的线性化描述：这避免把全时二阶结果误读成任意初值的非线性…", "match_reason": "metadata:title"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "concept_2d8e08b8d8ace05431e064a0", "type": "concept", "title": "接触中心的混合预测控制", "path": "vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md", "status": "working", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# 接触中心的混合预测控制\n\n把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics…", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e67cd99ac31c7017d6f7f7c7"}
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
- Extraction：`extraction_87395cad2f1d5fa88a1f4db4`
- 编译前召回已有对象：18
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_a858f8d191d3afdd69418471.md
+++ candidate:vault/memory/concept/concept_a858f8d191d3afdd69418471.md
@@ -1,42 +1,26 @@
 ---
 id: "concept_a858f8d191d3afdd69418471"
 type: "concept"
-status: "working"
-title: "陈旧性对齐的异步慢上下文—快控制接口"
+status: "proposal"
+title: "陈旧性对齐与上下文分区共同约束异步快慢控制接口"
 created_at: "2026-07-26T12:18:41+08:00"
-updated_at: "2026-07-26T12:33:42+08:00"
+updated_at: "2026-07-27T19:02:43+08:00"
 aliases: ["Staleness-Aligned Asynchronous Slow-Context Fast-Control Interface", "FastSlow-LMDrive", "异步快慢 VLA 接口"]
 tags: []
 domains: ["vla", "real-time-control", "autonomous-driving"]
 confidence: "medium"
-source_ids: ["source_d4762e0cf2330ab6ea00a521"]
-relations: [{"type": "derived_from", "target_id": "source_d4762e0cf2330ab6ea00a521", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都在保留慢速预训练表示的同时增加读取新鲜局部传感的快分支；前者面向视觉驾驶缓存，后者面向动作块内力反馈。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都依赖非对称接口使冻结主干可被复用；FastSlow 在单策略内部复用缓存，既有概念在多原语编排中复用冻结局部专家。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_d4762e0cf2330ab6ea00a521"
-reflection_context: {"reflection_ids": ["reflection_743b2d2d30d2f822bf2bfb9f"], "importance": "high", "changed_belief": "此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支 token、缓存可增量等价更新且快分支在训练中见过滞后上下文时，异步复用才是可验证的系统契约。", "surprising": "同一 action expert 从 10 Hz 提升到 20 Hz 主要提高路线完成率与减少偏航/超时，而综合 driving score 未同步提高并伴随更多车辆碰撞暴露；控制新鲜度和安全驾驶质量不是同一指标。", "connections": [{"shared_mechanism": "FastSlow-LMDrive 与块内反应式力注入都保留慢速预训练先验，同时用更快、更新鲜的局部观测驱动轻量动作分支。", "boundary": "连接适用于慢上下文在多个控制 tick 内仍有用、快路径可独立读取当前传感且延迟分布可在训练中覆盖的任务。", "difference": "FastSlow-LMDrive 通过逐层视觉语言 KV cache 服务驾驶 waypoint expert；力注入概念通过近期六维力记忆修正接触动作块，安全变量与传感动力学不同。"}], "open_questions": ["能否用快慢分支分歧和缓存年龄共同触发安全降级，并在长路线密集交通中减少完成率上升带来的碰撞暴露？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt-5.6-sol-m91-weekly-daily-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt-5.6-sol-m91-weekly-daily-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-26T12:33:42+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_21a3d976042f2d38be49"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_21a3d976042f2d38be49-concept-1.md"
-origin_candidate_sha256: "0cddb098247b5d0be61626e25961b5a980817764ff04dee957399b7b9eee4c34"
-origin_cognitive_artifact_sha256: "7496b4e69979dfc80abc6121b1c8f5e68cd245d00d654caada8eb5124e6839a5"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_706e5a41bcafbd013bca0544"
+source_ids: ["source_d4762e0cf2330ab6ea00a521", "source_e67cd99ac31c7017d6f7f7c7"]
+relations: [{"type": "derived_from", "target_id": "source_d4762e0cf2330ab6ea00a521", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都在保留慢速预训练表示的同时增加读取新鲜局部传感的快分支；前者面向视觉驾驶缓存，后者面向动作块内力反馈。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都依赖非对称接口使冻结主干可被复用；FastSlow 在单策略内部复用缓存，既有概念在多原语编排中复用冻结局部专家。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_30d85c442682f6afd96c3022", "reason": "两者都复用慢表示并让快路径读取新鲜信息；前者用训练覆盖缓存陈旧性，后者用 static、sliding、dynamic 分区证明部分 KV 复用的正确性，适用边界并不相同。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_e67cd99ac31c7017d6f7f7c7"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_d8d4183ecacf40814756f4c2"], "importance": "weekly", "changed_belief": "我会把实时性归因于缓存有效性与异步执行的系统契约，而不把任何 flow-matching VLA 的缓存复用或论文基准速度泛化为普遍部署保证。", "surprising": "", "connections": [{"shared_mechanism": "两者都以异步执行和复用不随当前采样步变化的计算来减少控制等待。", "boundary": "本文限于其 timestep-invariance 分区、固定输入下的 attention 等价性及 LIBERO/Kinetix 报告设置。", "difference": "一般异步推理只重叠预测与执行；Reflex 还主张通过静态/滑动/动态上下文分区保持增量 KV 缓存的数学正确性。"}], "open_questions": ["感知输入变化、动作反馈和长时闭环分布漂移下，哪些区域仍可安全缓存且保持端到端控制稳定？"]}
+proposed_status: "working"
 ---
 
 # 陈旧性对齐的异步慢上下文—快控制接口
 
 在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。
+
+## 新增来源材料
+
+- `source_e67cd99ac31c7017d6f7f7c7`：在需要高频闭环控制的 VLA 系统中，慢上下文与快动作接口应同时声明缓存内容的时间角色和有效期。FastSlow-LMDrive 用训练时随机截断覆盖部署缓存陈旧性；Reflex 则把 flow-matching 注意力分成 static、sliding 与 dynamic 区域，并仅对去噪步不变的部分做增量 KV 更新。两种机制都要求固定输入下与完整前向的等价性或可检验一致性，但训练时陈旧性对齐不能替代 Reflex 的 timestep-invariance 分区，缓存加速也不能证明长时闭环稳定或部署安全。
```
