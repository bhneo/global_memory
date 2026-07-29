---
id: "proposal_bundle_11dc3ab1e457fcbc5481"
type: "proposal"
status: "migrated"
title: "Compile bundle：[2607.18236] Patch Policy: Efficient Embodied Control via Dense Visual Representations"
created_at: "2026-07-27T18:14:46+08:00"
updated_at: "2026-07-27T18:14:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e8651a193623cbe2b86becb0"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[2607.18236] Patch Policy: Efficient Embodied Control via Dense Visual Representations"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_e4d496289d0839c301597080"
input_sha256: "aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_97fc87cffe27a2fc9d741e78", "target_path": "vault/knowledge/concepts/concept_97fc87cffe27a2fc9d741e78-block-causal-dense-patch-policy-区块因果的密集视觉策略.md", "base_sha256": null, "candidate_sha256": "ff45646a414652f563dadd6fdfa0cc37965018f01c36ca36a9fb6bcf81a7f487", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_11dc3ab1e457fcbc5481-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_97fc87cffe27a2fc9d741e78.md", "working_at": "2026-07-27T18:14:48+08:00"}]
existing_context: [{"id": "input_ece052248dd2c432913efd3a", "type": "input", "title": "[2607.18236] Patch Policy: Efficient Embodied Control via Dense Visual Representations", "path": "vault/inputs/input-input_ece052248dd2c432913efd3a.md", "status": "active", "source_ids": ["source_e8651a193623cbe2b86becb0"], "snippet": "…Efficient Embodied [Control] via Dense Visual Representations\n\nInput Episode for `source_e8651a193623cbe2b86becb0`. The immutable Source remains authoritative.\n\n# [2607…", "match_reason": "metadata:title"}, {"id": "reflection_0078f804e87c7ed12f88876d", "type": "reflection", "title": "B-spline Policy：把动作表示与执行速度从固定采样率中解耦", "path": "vault/reflections/reflection-reflection_0078f804e87c7ed12f88876d.md", "status": "active", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# B-spline [Policy]：把动作表示与执行速度从固定采样率中解耦\n\n## Why important\n\nBSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。\n\n## What changed\n\n此前动作块加速常被理解为少重规划或少执行几步…", "match_reason": "metadata:title"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…offline iteration and online off-[policy] VLA post-training are distinct paths\n\n## Why important\n\nThe notes separate an…", "match_reason": "metadata:title"}, {"id": "input_e69b286ace68f56c81ab185b", "type": "input", "title": "[2607.12894] Hy-Embodied-VLM-1.0: Efficient Physical-World Agents", "path": "vault/inputs/input-input_e69b286ace68f56c81ab185b.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "# [2607.12894] Hy-Embodied-VLM-1.0: [Efficient] Physical-World Agents\n\nInput Episode for `source_bd08e368730960f4f6ce19ca`. The immutable…", "match_reason": "metadata:title"}, {"id": "concept_bcf39e7d937cfdf22e3c49e2", "type": "concept", "title": "面向真实零售人形机器人的数据高效 VLA 后训练闭环", "path": "vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md", "status": "working", "source_ids": ["source_3846f8c1451f8a12e0f87b33"], "snippet": "# 面向真实零售人形机器人的数据高效 VLA 后训练闭环\n\n在超市场景中部署预训练 VLA 时，可把控制频率对齐、数据筛选、任务相关视觉突出和降低对 VLA 主动作流依赖的后训练配方，与从当前策略失败状态收集的经验驱动细化结合；其目标是缩小实验室到门店的系统失配，而非证明这些组件可独立保证所有人形机器人任务的可靠性。", "match_reason": "metadata:aliases"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "# GitHub - Tencent-Hunyuan/HY-[Embodied]: HY-[Embodied]: [Embodied] Foundation Models for Real-World Agents · GitHub\n\nInput Episode for…", "match_reason": "metadata:title"}, {"id": "input_8a6718745ea2b254778ae2e6", "type": "input", "title": "GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub", "path": "vault/inputs/input-input_8a6718745ea2b254778ae2e6.md", "status": "active", "source_ids": ["source_956ae2aa178f0606fb84f943"], "snippet": "# GitHub - Xbotics-[Embodied]-AI-club/Xbotics-[Embodied]-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub\n\nInput Episode for `source_956ae2aa178f0606fb84f943`. The immutable…", "match_reason": "metadata:title"}, {"id": "input_57c3aecea736fc43a87546a6", "type": "input", "title": "GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。 · GitHub", "path": "vault/inputs/input-input_57c3aecea736fc43a87546a6.md", "status": "active", "source_ids": ["source_ff5ce793c0efda7112e73c86"], "snippet": "# GitHub - Xbotics-[Embodied]-AI-club/Xbotics-[Embodied]-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来…", "match_reason": "metadata:title"}, {"id": "work_arxiv_2607_11119", "type": "work", "title": "VIA: Interface-first Robot Control", "path": "vault/memory/work/work_arxiv_2607_11119.md", "status": "working", "source_ids": ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"], "snippet": "…Interface-first Robot [Control]\n\n## Logical work identity\n\n- arXiv：`2607.11119`\n- Version：`v1`\n- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`\n\n此对象聚合现实世界作品身份…", "match_reason": "metadata:title"}, {"id": "concept_cdbe55276db1fb0eb0aa370a", "type": "concept", "title": "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere equilibrium fluctuations", "path": "vault/memory/concept/concept_cdbe55276db1fb0eb0aa370a.md", "status": "working", "source_ids": ["source_3851b9ffbfbae3ca166308fd", "source_323f116c3573f26f4af7785d"], "snippet": "# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time [control] of hard-sphere fluctuations\n\n对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann…", "match_reason": "metadata:title"}, {"id": "reflection_70e994e4dbf7cffe990580af", "type": "reflection", "title": "硬球长时相关：全时控制只落在平衡二阶涨落层 / global control is for equilibrium second-order fluctuations", "path": "vault/reflections/reflection-reflection_70e994e4dbf7cffe990580af.md", "status": "active", "source_ids": ["source_a5f4d6734479eea71ff9a2a4"], "snippet": "# 硬球长时相关：全时控制只落在平衡二阶涨落层 / global [control] is for equilibrium second-order fluctuations\n\n## Why important\n\n可复用的认知价值是将“突破 Lanford 短时限制”限定为平衡附近协方差的线性化描述：这避免把全时二阶结果误读成任意初值的非线性…", "match_reason": "metadata:title"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "concept_a858f8d191d3afdd69418471", "type": "concept", "title": "陈旧性对齐的异步慢上下文—快控制接口", "path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "status": "working", "source_ids": ["source_d4762e0cf2330ab6ea00a521"], "snippet": "# 陈旧性对齐的异步慢上下文—快控制接口\n\n在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。", "match_reason": "metadata:aliases"}, {"id": "concept_2d8e08b8d8ace05431e064a0", "type": "concept", "title": "接触中心的混合预测控制", "path": "vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md", "status": "working", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# 接触中心的混合预测控制\n\n把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics…", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e8651a193623cbe2b86becb0"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "854c6e1ba595ee3115a57ecd4b72f9ebb5c24242e8ab24d406895e0c1d5883f4"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[2607.18236] Patch Policy: Efficient Embodied Control via Dense Visual Representations

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_e4d496289d0839c301597080`
- 编译前召回已有对象：14
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_97fc87cffe27a2fc9d741e78-block-causal-dense-patch-policy-区块因果的密集视觉策略.md
@@ -0,0 +1,20 @@
+---
+id: "concept_97fc87cffe27a2fc9d741e78"
+type: "concept"
+status: "proposal"
+title: "Block-causal dense patch policy / 区块因果的密集视觉策略"
+created_at: "2026-07-27T18:14:46+08:00"
+updated_at: "2026-07-27T18:14:46+08:00"
+aliases: ["Patch Policy", "block-causal attention", "密集 ViT patch 控制"]
+tags: []
+domains: ["robotics", "visual-representations", "control"]
+confidence: "medium"
+source_ids: ["source_e8651a193623cbe2b86becb0"]
+relations: [{"type": "derived_from", "target_id": "source_e8651a193623cbe2b86becb0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e8651a193623cbe2b86becb0"
+reflection_context: {"reflection_ids": ["reflection_963ef2c3818ac53b780d8b29"], "importance": "high", "changed_belief": "我会把其优势限定为论文的视觉 backbone、掩码、模拟与真实任务设置，而不将相对改进泛化为任何 dense-feature 控制器。", "surprising": "", "connections": [{"shared_mechanism": "两者都保留细粒度视觉表征以支持反应式控制。", "boundary": "本文依赖预训练 ViT patch、block-causal mask 与所报告七个环境套件。", "difference": "大 VLA 借完整 VLM 获得 dense tokens；本文以最小策略扩展避开该骨干计算开销。"}], "open_questions": ["遮挡、相机变化和长期多任务上下文下，dense patch 的收益是否仍超过全局表示？"]}
+---
+
+# Block-causal dense patch policy / 区块因果的密集视觉策略
+
+对基于 transformer 的机器人策略，可将预训练 ViT 的密集 patch tokens 与状态共同输入，并以 block-causal attention mask 保持跨时刻动作因果性；这在论文设置中避免全局池化损失空间细节且不承担完整 VLM 骨干开销。结论依赖具体视觉表示、掩码与评测任务，未保证任意相机或控制分布下的增益。
```
