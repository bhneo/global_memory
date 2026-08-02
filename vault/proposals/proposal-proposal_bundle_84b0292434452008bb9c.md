---
id: "proposal_bundle_84b0292434452008bb9c"
type: "proposal"
status: "migrated"
title: "Compile bundle：World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models"
created_at: "2026-08-02T18:57:50+08:00"
updated_at: "2026-08-02T18:57:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a54ea0123fbadf6d7012c9fb"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_9709f5455eff7da7f7874ef5"
input_sha256: "532cb0229e7aa0963713e65c394dd4296065aacfca10bb97fb2aa0afad469cfe"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_8f574f03117d21adf127d23f", "target_path": "vault/knowledge/concepts/concept_8f574f03117d21adf127d23f-以世界模型想象迭代修正动作计划-iterative-action-plan-refinement-through-world-m.md", "base_sha256": null, "candidate_sha256": "65974c6d81321b012be13bfffc709f1e07b361bcb94bd55fad8bbfb99c6a45d5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_84b0292434452008bb9c-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_8f574f03117d21adf127d23f.md", "working_at": "2026-08-02T18:57:51+08:00"}]
existing_context: [{"id": "input_cde49d7c9071270dc3fb8348", "type": "input", "title": "World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models", "path": "vault/inputs/input-input_cde49d7c9071270dc3fb8348.md", "status": "active", "source_ids": ["source_a54ea0123fbadf6d7012c9fb"], "snippet": "…Generalizable [Decision-Making] with Action-Conditioned World Models World Action Planner: Generalizable [Decision-Making] with Action-Conditioned World…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "concept_6de58085da65839ab392094c", "type": "concept", "title": "触觉原生的三流联合世界—动作生成 / Tactile-native tri-stream joint world-action generation", "path": "vault/memory/concept/concept_6de58085da65839ab392094c.md", "status": "working", "source_ids": ["source_d319d5007779569f8f786413"], "snippet": "# 触觉原生的三流联合世界—动作生成 / Tactile-native tri-stream joint [world]-action generation\n\n在 [world]-action model 中，可把未来视觉、未来触觉和动作建模为三个同级生成流：视觉…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The [world] component and dual-system [world]-action models both use predictive representations to connect perception with possible…", "match_reason": "metadata:title"}, {"id": "concept_fdb5ce439cbb603e19af8653", "type": "concept", "title": "前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens", "path": "vault/memory/concept/concept_fdb5ce439cbb603e19af8653.md", "status": "working", "source_ids": ["source_ba71396b5fc37637b125a89f"], "snippet": "# 前缀可解码的有序动作令牌 / Prefix-decodable ordered [action] tokens\n\n动作 tokenizer 同时满足高压缩、任意前缀都可解码为完整可执行动作块，以及由粗到细的有序精化。实现上以 transformer registers 和有限标量量化形成令牌，并用 nested dropout…", "match_reason": "metadata:title"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 Latent [Action]\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent [action] target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "synthesis_9ae225f58ef80075a6a8fdcf", "type": "synthesis", "title": "VLA execution interfaces: adaptive action precision without an LLM inner loop", "path": "vault/synthesis/synthesis-synthesis_9ae225f58ef80075a6a8fdcf.md", "status": "active", "source_ids": ["source_ba71396b5fc37637b125a89f", "source_feaf5bf5a081e27b445c569c"], "snippet": "…which still may require a sparse upper-layer [planner].\n- OAT's adaptive-budget opportunity remains prospective, and TurboVLA…", "match_reason": "full-text:body"}, {"id": "concept_913857cf6907564640fd669c", "type": "concept", "title": "无 LLM 中心的执行级 VLA 直连通路 / LLM-free execution-path VLA", "path": "vault/memory/concept/concept_913857cf6907564640fd669c.md", "status": "working", "source_ids": ["source_feaf5bf5a081e27b445c569c"], "snippet": "…V+L→A 重构不同于剪枝、缓存、量化或只优化 action head，也不否认语言语义本身的必要性。论文的消融显示去语言会显著损害目标条件任务，而轻量语义编码和双向交互足以支撑其所测执行任务。适用边界是具体执行指令、现有视觉语义与动作监督；开放式任务分解、复杂推理和未见组合语言仍可能需要上层 LLM [planner]，但不必让其驻留在每个控制步的执行内环。", "match_reason": "full-text:body"}, {"id": "input_ab5a33edd49eec243cb3862f", "type": "input", "title": "DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting", "path": "vault/inputs/input-input_ab5a33edd49eec243cb3862f.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…Solver V-A Event extraction V-B Simulation-in-the-loop coordinator V-C Motion [planner] VI Experiment…", "match_reason": "full-text:body"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…Subtask [Planner] Training 3.2 Stage 2: Tactile World Model Training 3.3 Stage 3: Visuo-Ta…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_a54ea0123fbadf6d7012c9fb"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "657c678864cc62b59756149a9ec6bfc0bba843ef086c9aebe7435a73f19fcf3f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_9709f5455eff7da7f7874ef5`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_8f574f03117d21adf127d23f-以世界模型想象迭代修正动作计划-iterative-action-plan-refinement-through-world-m.md
@@ -0,0 +1,20 @@
+---
+id: "concept_8f574f03117d21adf127d23f"
+type: "concept"
+status: "proposal"
+title: "以世界模型想象迭代修正动作计划 / Iterative action-plan refinement through world-model imagination"
+created_at: "2026-08-02T18:57:50+08:00"
+updated_at: "2026-08-02T18:57:50+08:00"
+aliases: ["World Action Planner", "WAP", "world-model-guided plan search", "世界模型引导计划搜索"]
+tags: []
+domains: ["robotics", "world-model", "planning", "visual-language-model"]
+confidence: "medium"
+source_ids: ["source_a54ea0123fbadf6d7012c9fb"]
+relations: [{"type": "derived_from", "target_id": "source_a54ea0123fbadf6d7012c9fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_1bc84fc99981d367b712d161", "reason": "两者都以动作条件 rollout 支持决策；既有节点聚焦单次前向吞吐，WAP 将 rollout 置于反复改写计划的搜索内循环。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都验证动作条件后果；WAP 在执行前搜索整体计划，CheckVLA 在执行中依据真实偏差修复可部署后缀。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都分离语义规划与动作生成；WAP 进一步让世界模型想象结果反向迭代修正 VLM 计划。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_474b5f9742996e9fc68609b6", "reason": "两者都把机器人名义运动渲染为部署可计算的视觉动作条件；WAP 使用关节骨架 pose image 并将其用于计划搜索。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_a54ea0123fbadf6d7012c9fb"
+reflection_context: {"reflection_ids": ["reflection_d4da03127a4726ff3f567d63"], "importance": "high", "changed_belief": "我原先会把 action-conditioned world model 主要放在候选排序或执行监控；该项目强调在执行前反复修改整份动作计划，而不是只选一个固定候选或报警后修复后缀。", "surprising": "动作条件不是低维控制向量，而是通过正向运动学渲染的机器人关节骨架 pose image；世界模型因此在视觉空间中同时看到场景与名义机器人运动。", "connections": [{"shared_mechanism": "WAP 与 concept_1bc84fc99981d367b712d161 都用动作条件世界模型生成候选未来以支持决策。", "boundary": "项目页没有给出捕获文本中的数值表格，不能从“outperforms”措辞推导具体提升或统计稳健性。", "difference": "DriftWorld 节点强调单次前向 rollout 吞吐量，WAP 强调 VLM 初稿、世界模型想象与计划搜索的迭代闭环。"}, {"shared_mechanism": "WAP 与 concept_2db7edf95d63ca80702f042e 都用动作条件未来验证动作计划。", "boundary": "WAP 在执行前优化计划，CheckVLA 在执行中按观测偏差修复剩余后缀，两者不应合并。", "difference": "WAP 搜索整体计划的想象结果，CheckVLA 监控已提交动作的真实后果并做延迟感知修复。"}], "open_questions": ["当世界模型在搜索中被反复利用时，如何检测计划对模型误差的投机，并把想象分数与真实闭环成功率校准？"]}
+---
+
+# 以世界模型想象迭代修正动作计划 / Iterative action-plan refinement through world-model imagination
+
+长时机器人规划可以把语言模型的动作计划视为待验证初稿：先由 VLM 提出候选步骤，再通过正向运动学把机器人名义运动渲染成关节骨架 pose image，作为动作条件输入多任务世界模型；随后依据想象 rollout 的任务进展与碰撞结果在计划空间中迭代搜索和改写，而不是一次生成后直接执行。该机制区别于只提高单次 rollout 吞吐，也区别于执行中发现偏差后修复动作后缀。其有效性依赖世界模型在搜索分布上的校准、运动学与渲染质量以及低层 primitive 可用性；官方项目页展示三类评测但未提供捕获文本中可核验的数值表，因此性能结论保持 Source 边界。
```
