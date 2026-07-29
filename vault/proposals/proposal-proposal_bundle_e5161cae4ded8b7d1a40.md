---
id: "proposal_bundle_e5161cae4ded8b7d1a40"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T17:19:55+08:00"
updated_at: "2026-07-27T17:19:57+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e67cd99ac31c7017d6f7f7c7"]
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
extraction_id: "extraction_87395cad2f1d5fa88a1f4db4"
input_sha256: "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_30d85c442682f6afd96c3022", "target_path": "vault/knowledge/concepts/concept_30d85c442682f6afd96c3022-flow-matching-vla-的流式上下文分区与-kv-缓存-streaming-context-partitioning.md", "base_sha256": null, "candidate_sha256": "b64433036b3d7ef5a94f4612c74c3eba1b561f6d85638382c54221532de07d92", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_e5161cae4ded8b7d1a40-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_30d85c442682f6afd96c3022.md", "working_at": "2026-07-27T17:19:57+08:00"}]
existing_context: [{"id": "concept_a858f8d191d3afdd69418471", "type": "concept", "title": "陈旧性对齐的异步慢上下文—快控制接口", "path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "status": "working", "source_ids": ["source_d4762e0cf2330ab6ea00a521"], "snippet": "# 陈旧性对齐的异步慢上下文—快控制接口\n\n在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。", "match_reason": "metadata:aliases"}, {"id": "reflection_743b2d2d30d2f822bf2bfb9f", "type": "reflection", "title": "FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口", "path": "vault/reflections/reflection-reflection_743b2d2d30d2f822bf2bfb9f.md", "status": "active", "source_ids": ["source_d4762e0cf2330ab6ea00a521"], "snippet": "# FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口\n\n## Why important\n\n该工作把慢速语言与历史聚合、快速当前帧动作预测通过逐层 KV cache 接口解耦，并用随机陈旧性训练匹配异步部署分布；它把实时控制从单纯模型压缩问题改写为时间尺度、缓存一致性与新鲜观测融合的接口问题。\n\n## What changed\n\n此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支…", "match_reason": "metadata:domains"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…embodiment constraints.\n\n## Surprising\n\nOne co-tracking controller supports [real-time] teleoperation across two dexterous hands and seven tasks…", "match_reason": "full-text:body"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…do the repository's workspace schema, failure traces, [real-time] deadlines, and safety refusal mechanisms work in code…", "match_reason": "full-text:body"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language-Action] Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for [Vision-Language-Action] Models with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "input_ece052248dd2c432913efd3a", "type": "input", "title": "[2607.18236] Patch Policy: Efficient Embodied Control via Dense Visual Representations", "path": "vault/inputs/input-input_ece052248dd2c432913efd3a.md", "status": "active", "source_ids": ["source_e8651a193623cbe2b86becb0"], "snippet": "…Efficient Embodied [Control] via Dense Visual Representations\n\nInput Episode for `source_e8651a193623cbe2b86becb0`. The immutable Source remains authoritative.\n\n# [2607…", "match_reason": "metadata:title"}, {"id": "work_arxiv_2607_11119", "type": "work", "title": "VIA: Interface-first Robot Control", "path": "vault/memory/work/work_arxiv_2607_11119.md", "status": "working", "source_ids": ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"], "snippet": "…Interface-first Robot [Control]\n\n## Logical work identity\n\n- arXiv：`2607.11119`\n- Version：`v1`\n- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`\n\n此对象聚合现实世界作品身份…", "match_reason": "metadata:title"}, {"id": "concept_cdbe55276db1fb0eb0aa370a", "type": "concept", "title": "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere equilibrium fluctuations", "path": "vault/memory/concept/concept_cdbe55276db1fb0eb0aa370a.md", "status": "working", "source_ids": ["source_3851b9ffbfbae3ca166308fd", "source_323f116c3573f26f4af7785d"], "snippet": "# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time [control] of hard-sphere fluctuations\n\n对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann…", "match_reason": "metadata:title"}, {"id": "reflection_70e994e4dbf7cffe990580af", "type": "reflection", "title": "硬球长时相关：全时控制只落在平衡二阶涨落层 / global control is for equilibrium second-order fluctuations", "path": "vault/reflections/reflection-reflection_70e994e4dbf7cffe990580af.md", "status": "active", "source_ids": ["source_a5f4d6734479eea71ff9a2a4"], "snippet": "# 硬球长时相关：全时控制只落在平衡二阶涨落层 / global [control] is for equilibrium second-order fluctuations\n\n## Why important\n\n可复用的认知价值是将“突破 Lanford 短时限制”限定为平衡附近协方差的线性化描述：这避免把全时二阶结果误读成任意初值的非线性…", "match_reason": "metadata:title"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "concept_2d8e08b8d8ace05431e064a0", "type": "concept", "title": "接触中心的混合预测控制", "path": "vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md", "status": "working", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# 接触中心的混合预测控制\n\n把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics…", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e67cd99ac31c7017d6f7f7c7"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "1455236f0a4d9df8583ac3fcfb3204cac5edd86890be677fbc7cb43441170854"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_87395cad2f1d5fa88a1f4db4`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_30d85c442682f6afd96c3022-flow-matching-vla-的流式上下文分区与-kv-缓存-streaming-context-partitioning.md
@@ -0,0 +1,20 @@
+---
+id: "concept_30d85c442682f6afd96c3022"
+type: "concept"
+status: "proposal"
+title: "Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs"
+created_at: "2026-07-27T17:19:55+08:00"
+updated_at: "2026-07-27T17:19:55+08:00"
+aliases: ["Reflex 流式 VLA", "Reflex streaming VLA", "flow-matching VLA KV caching", "流式上下文分区"]
+tags: []
+domains: ["robotics", "vision-language-action", "systems"]
+confidence: "medium"
+source_ids: ["source_e67cd99ac31c7017d6f7f7c7"]
+relations: [{"type": "derived_from", "target_id": "source_e67cd99ac31c7017d6f7f7c7", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e67cd99ac31c7017d6f7f7c7"
+reflection_context: {"reflection_ids": ["reflection_d8d4183ecacf40814756f4c2"], "importance": "high", "changed_belief": "我会把实时性归因于缓存有效性与异步执行的系统契约，而不把任何 flow-matching VLA 的缓存复用或论文基准速度泛化为普遍部署保证。", "surprising": "", "connections": [{"shared_mechanism": "两者都以异步执行和复用不随当前采样步变化的计算来减少控制等待。", "boundary": "本文限于其 timestep-invariance 分区、固定输入下的 attention 等价性及 LIBERO/Kinetix 报告设置。", "difference": "一般异步推理只重叠预测与执行；Reflex 还主张通过静态/滑动/动态上下文分区保持增量 KV 缓存的数学正确性。"}], "open_questions": ["感知输入变化、动作反馈和长时闭环分布漂移下，哪些区域仍可安全缓存且保持端到端控制稳定？"]}
+---
+
+# Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs
+
+在论文所述 flow-matching VLA 中，将注意力上下文划分为不随去噪步变化的 static、滑动的 sliding 和随去噪变化的 dynamic 区域，可在固定输入下对 static/sliding 部分增量更新 KV 缓存并保持与全批 attention 等价；结合异步视觉编码与动作生成可减少阻塞。该结论依赖论文的 timestep-invariance 假设、数值稳定化和报告的基准设置，未证明任意闭环部署的稳定性。
```
