---
id: "proposal_bundle_c49d606ae9d958a34374"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:41:17+08:00"
updated_at: "2026-07-21T17:41:17+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_748cef2215ddc958568e6368"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56sol-readmission-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_6cc6e7d8b1ad1a6f40f2ae14"
input_sha256: "ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_native_action_aligned_vla_memory", "target_path": "vault/knowledge/concepts/concept_native_action_aligned_vla_memory-动作对齐的-vla-原生视觉记忆压缩.md", "base_sha256": null, "candidate_sha256": "3570cdc887d8bcd9409ae223e0e3b52ff880a79a29b781f00554bfdf5bc6fd68", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_c49d606ae9d958a34374-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_native_action_aligned_vla_memory.md", "working_at": "2026-07-21T17:41:17+08:00"}]
existing_context: [{"id": "concept_59f92bcb786f695ddcd47f7f", "type": "concept", "title": "视频原生的光流动作接口", "path": "vault/memory/concept/concept_59f92bcb786f695ddcd47f7f.md", "status": "working", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "# 视频原生的光流动作接口\n\n用连续光流视频表示机器人动作，使同一稠密运动接口既可由世界动作模型生成并解码为控制，也可作为未来视频生成条件，还能从无动作标签视频提取预训练监督。该接口覆盖可见跨帧运动，但不天然包含力、遮挡后状态或完整本体动力学。", "match_reason": "metadata:aliases"}, {"id": "reflection_7952be977c24d5dfe1da2072", "type": "reflection", "title": "图式 Agent Memory：生命周期完整不等于证据闭环完整", "path": "vault/reflections/reflection-reflection_7952be977c24d5dfe1da2072.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92"], "snippet": "# 图式 Agent [Memory]：生命周期完整不等于证据闭环完整\n\n## Why important\n\n这份综述把 Agent [Memory] 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测…", "match_reason": "metadata:title"}, {"id": "synthesis_7084bca907043e3cba4afb7e", "type": "synthesis", "title": "Agent Memory 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界", "path": "vault/synthesis/synthesis-synthesis_7084bca907043e3cba4afb7e.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92", "source_11bc6c51fa038191e33bc9a7", "source_6ada1b3b0033883b83a3bf40", "source_6b52a51e2b4a3be43c97c386"], "snippet": "# Agent [Memory] 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界\n\n## Emerging patterns\n\n- 长期 Agent [Memory] 与物理 Agent 基础设施共享同一结构要求：状态必须可外化、更新必须可定位、失败必须能回到产生它的感知…", "match_reason": "metadata:title"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# Latent [Memory] Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "experiment_7101e03fb065226e65f388a5", "type": "experiment", "title": "Cursor M7 真实读取与 receipt 回写验收", "path": "vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md", "status": "working", "source_ids": ["source_113d589e6dadf14b5fa8edea"], "snippet": "# Cursor M7 真实读取与 receipt 回写验收\n\n## 验收路径\n\nCursor 按协议读取了 `AGENTS.md`、`.cursor/rules/global-[memory].mdc` 和 `vault/INDEX…", "match_reason": "metadata:domains"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…Like RPent, it decomposes perception, reasoning, [memory], and execution into composable physical-agent services.\n  Boundary: This is an…", "match_reason": "metadata:domains"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "reflection_4430cc70fe95425f717c1e71", "type": "reflection", "title": "RPent：把冻结 VLA 放进可递归反思的具身 Agent 外壳", "path": "vault/reflections/reflection-reflection_4430cc70fe95425f717c1e71.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "# RPent：把冻结 VLA 放进可递归反思的具身 Agent 外壳\n\n## Why important\n\nRPent 把 perception、reasoning、[memory]、execution 与 self-evolution 组织成服务化…", "match_reason": "metadata:domains"}, {"id": "concept_hierarchical_mathematical_compression", "type": "concept", "title": "数学兴趣的层级压缩模型", "path": "vault/memory/concept/concept_hierarchical_mathematical_compression.md", "status": "working", "source_ids": ["source_e753604a46350e066a104918"], "snippet": "…human mathematics 的代理，观察到展开长度随深度和包装长度近似指数增长，而包装长度跨深度大致稳定；据此提出 reductive [compression]、deductive [compression] 与 [compression]-biased PageRank 可作为自动数学探索的方向信号。该模型是预印本提出并在单一形式库上检验的启发式，不是数学兴趣的既定定义，也不提供正确性证据。", "match_reason": "metadata:aliases"}, {"id": "question_compression_biased_mathematical_search", "type": "question", "title": "压缩偏置会把自动数学探索引向真正有价值的结果吗？", "path": "vault/memory/question/question_compression_biased_mathematical_search.md", "status": "working", "source_ids": ["source_e753604a46350e066a104918"], "snippet": "# 压缩偏置会把自动数学探索引向真正有价值的结果吗？\n\n若以 reductive/deductive [compression] 和依赖图 PageRank 为自动推理的探索奖励，需要验证它是否能预测专家兴趣与搜索收益，同时避免偏爱抽象、库工程热点或可人为构造的高压缩对象。关键检验应跨形式库、定义粒度与历史时间切片，并与简单图统计和证明长度基线比较。", "match_reason": "metadata:aliases"}, {"id": "reflection_81c9fd8c2a3fe78fb40e0e68", "type": "reflection", "title": "数学兴趣的层级压缩模型：可计算方向信号与代理偏差", "path": "vault/reflections/reflection-reflection_81c9fd8c2a3fe78fb40e0e68.md", "status": "active", "source_ids": ["source_e753604a46350e066a104918"], "snippet": "…reductive [compression] 衡量定义对表达长度的缩减，deductive [compression] 衡量短陈述背后的证明负担；PageRank-style refinement 再加入对象对其他高压缩对象的承重作用。\n\n## Conflicts\n\n- 论文将 Mathlib 作为 human mathematics 的代理，但…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_748cef2215ddc958568e6368"}
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

- Provider：`agent-semantic-daily-gpt56sol-readmission-v1`
- Extraction：`extraction_6cc6e7d8b1ad1a6f40f2ae14`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_native_action_aligned_vla_memory-动作对齐的-vla-原生视觉记忆压缩.md
@@ -0,0 +1,20 @@
+---
+id: "concept_native_action_aligned_vla_memory"
+type: "concept"
+status: "proposal"
+title: "动作对齐的 VLA 原生视觉记忆压缩"
+created_at: "2026-07-21T17:41:17+08:00"
+updated_at: "2026-07-21T17:41:17+08:00"
+aliases: ["Native Action-Aligned VLA Memory Compression", "NativeMEM", "原生动作对齐记忆"]
+tags: []
+domains: ["embodied-ai", "vla", "agent-memory"]
+confidence: "medium"
+source_ids: ["source_748cef2215ddc958568e6368"]
+relations: [{"type": "derived_from", "target_id": "source_748cef2215ddc958568e6368", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都冻结基础 VLA 以约束增量模块，但分别扩展历史表征与外部技能执行边界。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_748cef2215ddc958568e6368"
+reflection_context: {"reflection_ids": ["reflection_65ee736483d758905945535d"], "importance": "high", "changed_belief": "长时视觉记忆不一定需要独立记忆模型；在该设定中，冻结策略反而构成迫使压缩分支保留动作相关信息的训练约束。", "surprising": "作者报告单 token/帧仍可在 32GB 内保留 5000 帧，并在所测任务中把模拟平均成功率由 Mem-0 的 32.4% 提至 84.0%；这是特定 π0.5、任务和复现基线下的结果。", "connections": [{"shared_mechanism": "都通过冻结基础 VLA 限定新增模块的职责。", "boundary": "这里只比较能力扩展接口，不把记忆 token 等同于高层技能编排。", "difference": "NativeMEM 把历史观测压入 VLA 原生 token；非对称技能编排在 VLA 外部管理重试、验证和运输。"}], "open_questions": ["单 token 压缩在遮挡、多对象身份交换和失败恢复中会丢失哪些不可恢复信息？"]}
+---
+
+# 动作对齐的 VLA 原生视觉记忆压缩
+
+NativeMEM 将每个历史帧—相机视角压缩为一个与预训练 VLA token 维度兼容的记忆 token；第一阶段冻结 VLA，仅以原动作预测损失训练由视觉编码器初始化的 memory tokenizer，第二阶段缓存 token 并微调策略。其目标是在不增加外部记忆推理器的情况下兼顾高频更新与长时间跨度；现有证据来自作者在特定 π0.5、模拟及三项真机任务上的预印本实验。
```
