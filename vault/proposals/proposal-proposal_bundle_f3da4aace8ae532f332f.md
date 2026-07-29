---
id: "proposal_bundle_f3da4aace8ae532f332f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-24T18:38:09+08:00"
updated_at: "2026-07-24T18:38:10+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ce00fba8d7127c890fdcc46e"]
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
extraction_id: "extraction_06f48faebe5a304f8a1bd31d"
input_sha256: "37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_1bc84fc99981d367b712d161", "target_path": "vault/memory/concept/concept_1bc84fc99981d367b712d161.md", "base_sha256": "33309496f8a5405b2cfbe36d8ff2bffc272a315870f3235ca16942fda7965e35", "candidate_sha256": "4325ca69c8bdca7dca5933049c3d9aa5d356945dbe9c4df8e9b767a633739c7b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_f3da4aace8ae532f332f-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_f3da4aace8ae532f332f-concept-1.md", "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "reflection_754995a5fd604aa50ec30b29", "type": "reflection", "title": "DriftWorld：世界模型的控制价值受 rollout 吞吐量约束", "path": "vault/reflections/reflection-reflection_754995a5fd604aa50ec30b29.md", "status": "active", "source_ids": ["source_ce00fba8d7127c890fdcc46e"], "snippet": "# DriftWorld：世界模型的控制价值受 rollout 吞吐量约束\n\n## Why important\n\nDriftWorld 将动作条件未来帧生成从迭代去噪改为一次前向生成，直接针对候选动作搜索需要大量 rollout 的推理瓶颈；它把世界模型评价从单帧保真扩展到能否支持实时决策。\n\n## What changed\n\n世界模型速度不只是工程优化；当采样速度限制候选动作数量时，生成吞吐量会改变规划和离线策略排序是否可实际使用。\n\n## Surprising…", "match_reason": "metadata:domains"}, {"id": "concept_1bc84fc99981d367b712d161", "type": "concept", "title": "单次前向动作条件世界模型的 rollout 吞吐量接口", "path": "vault/memory/concept/concept_1bc84fc99981d367b712d161.md", "status": "working", "source_ids": ["source_ce00fba8d7127c890fdcc46e"], "snippet": "# 单次前向动作条件世界模型的 rollout 吞吐量接口\n\n动作条件世界模型若在训练中学习从先验到未来帧的漂移映射，可在推理时以单次前向生成候选动作序列的 rollout，从而为在线动作搜索或离线策略排序释放采样预算；其控制价值仍需分别验证预测保真、长时程误差和候选排序与真实结果的一致性。", "match_reason": "metadata:domains"}, {"id": "reflection_245f74ef295bd04767608b26", "type": "reflection", "title": "RoboTTT：把长序列经验写入策略 fast weights", "path": "vault/reflections/reflection-reflection_245f74ef295bd04767608b26.md", "status": "active", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# RoboTTT：把长序列经验写入策略 [fast] weights\n\n## Why important\n\n它不是简单增加历史帧，而是在推理过程中用 TTT 层的 [fast] weights 吸收序列，试图把示范、纠正和自身执行历史变成在线适应状态。\n\n## What changed\n\n长上下文能力既可通过显式记忆…", "match_reason": "metadata:title"}, {"id": "concept_test_time_fast_weight_robot_memory", "type": "concept", "title": "机器人策略的测试时快速权重记忆", "path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "status": "working", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# 机器人策略的测试时快速权重记忆\n\nRoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT [fast]-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮…", "match_reason": "metadata:aliases"}, {"id": "concept_17750931a381f8453b27ccba", "type": "concept", "title": "连续曲线动作接口与执行重定时", "path": "vault/memory/concept/concept_17750931a381f8453b27ccba.md", "status": "working", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。", "match_reason": "metadata:domains"}, {"id": "reflection_0078f804e87c7ed12f88876d", "type": "reflection", "title": "B-spline Policy：把动作表示与执行速度从固定采样率中解耦", "path": "vault/reflections/reflection-reflection_0078f804e87c7ed12f88876d.md", "status": "active", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# B-spline Policy：把动作表示与执行速度从固定采样率中解耦\n\n## Why important\n\nBSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。\n\n## What changed\n\n此前动作块加速常被理解为少重规划或少执行几步…", "match_reason": "metadata:domains"}, {"id": "input_bb0b9df051571c4e2beb584c", "type": "input", "title": "终于有人来挑战PI的flow matching的叙事了", "path": "vault/inputs/input-input_bb0b9df051571c4e2beb584c.md", "status": "active", "source_ids": ["source_e6608d8f849ad472bbd95143"], "snippet": "…自回归先行，为什么流匹配后来居上 这波具身发展的起点，其实是由VLM点燃的。VLM极其强大，可以针对未见的场景做出规划，具备直接输出动作的潜力。RT-2、OpenVLA、π0-[FAST] 都把连续动作离散成 token，附到语言词表后面，让视觉-语言模型像预测下一个字一样预测下一个动作。 VLM预训练得来的世界知…", "match_reason": "full-text:body"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The [world] component and dual-system [world]-action models both use predictive representations to connect perception with possible…", "match_reason": "metadata:title"}, {"id": "concept_09dc6e910b167ba474c89c38", "type": "concept", "title": "世界动作模型的激活空间鲁棒性 steering", "path": "vault/memory/concept/concept_09dc6e910b167ba474c89c38.md", "status": "working", "source_ids": ["source_38cba686373b003398483ab2"], "snippet": "# 世界动作模型的激活空间鲁棒性 steering\n\n对世界动作模型在标称与扰动 rollout 的内部激活进行对比，若鲁棒性相关特征在低维子空间中具有可分离结构，可据此构造对比激活方向，并利用局部线性动态在推理时以受惩罚的闭环控制调节激活；该可操控性需要按模型架构和扰动类型分别验证。", "match_reason": "metadata:aliases"}, {"id": "input_76b68fdb85fc376d2226e524", "type": "input", "title": "[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents", "path": "vault/inputs/input-input_76b68fdb85fc376d2226e524.md", "status": "active", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "…Physics-based World [Modeling] with Vision-Language Agents\n\nInput Episode for `source_4ceaa5243dd0d99116547dda`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "input_e69b286ace68f56c81ab185b", "type": "input", "title": "[2607.12894] Hy-Embodied-VLM-1.0: Efficient Physical-World Agents", "path": "vault/inputs/input-input_e69b286ace68f56c81ab185b.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "…Efficient Physical-[World] Agents\n\nInput Episode for `source_bd08e368730960f4f6ce19ca`. The immutable Source remains authoritative.\n\n# [2607.12894] Hy-Embodied…", "match_reason": "metadata:title"}, {"id": "input_a070092fbe4bbba0a3effe85", "type": "input", "title": "GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub", "path": "vault/inputs/input-input_a070092fbe4bbba0a3effe85.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "…Agentic Infrastructure for the Physical [World] · GitHub\n\nInput Episode for `source_6b52a51e2b4a3be43c97c386`. The immutable Source remains authoritative.\n\n# GitHub…", "match_reason": "metadata:title"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied Foundation Models for Real-[World] Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "concept_f67f822ee20789d74d7b75e3", "type": "concept", "title": "物理失败合成驱动的稠密机器人奖励建模", "path": "vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md", "status": "working", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# 物理失败合成驱动的稠密机器人奖励建模\n\n通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。", "match_reason": "metadata:aliases"}, {"id": "concept_4b29abb8c07d6365b04b97c3", "type": "concept", "title": "面向策略学习的可运行交互孪生", "path": "vault/memory/concept/concept_4b29abb8c07d6365b04b97c3.md", "status": "working", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "# 面向策略学习的可运行交互孪生\n\n将真实对象—机器人交互记录组织为可在物理仿真器中重放的 episodic twin：它需要联合保留场景几何、对象状态、推断的物理参数、参与者、相机、位姿和轨迹，使该记录可用于下游策略学习或评测。该概念不保证视觉重建、物理参数估计或跨场景泛化已经充分准确。", "match_reason": "metadata:domains"}, {"id": "reflection_c8a3c97a77f64d38720a8539", "type": "reflection", "title": "Agentic Real2Sim：可运行孪生把视觉重建扩展为物理任务接口", "path": "vault/reflections/reflection-reflection_c8a3c97a77f64d38720a8539.md", "status": "active", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "# Agentic Real2Sim：可运行孪生把视觉重建扩展为物理任务接口\n\n## Why important\n\n该工作将真实交互录像转换为可模拟的 episodic twin，明确要求同时保存几何、对象状态、物理参数、相机、位姿与轨迹；这把 Real2Sim 的成功条件从视觉相似性推进到能否为策略学习和评测提供可运行接口。\n\n## What changed…", "match_reason": "metadata:domains"}, {"id": "reflection_cb246940931502d077f687f5", "type": "reflection", "title": "DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配", "path": "vault/reflections/reflection-reflection_cb246940931502d077f687f5.md", "status": "active", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配\n\n## Why important\n\nDenseReward 把机器人奖励学习的两个薄弱环节放在同一数据管线中：用定向扰动合成碰撞、漏抓、掉落和恢复等物理失败，再学习带历史帧的逐时刻任务进度奖励。\n\n## What changed\n\n此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。\n\n## Surprising\n\n两帧历史优于一帧…", "match_reason": "metadata:domains"}, {"id": "reflection_4b63a8834e11b28db3cf2fdc", "type": "reflection", "title": "TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心", "path": "vault/reflections/reflection-reflection_4b63a8834e11b28db3cf2fdc.md", "status": "active", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心\n\n## Why important\n\nTACTIC 不只把触觉追加到 observation，而是让 distributed tactile、proximity map、contact Jacobian sampling 和 hybrid…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ce00fba8d7127c890fdcc46e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_06f48faebe5a304f8a1bd31d`
- 编译前召回已有对象：20
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_1bc84fc99981d367b712d161.md
+++ candidate:vault/memory/concept/concept_1bc84fc99981d367b712d161.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_1bc84fc99981d367b712d161"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "单次前向动作条件世界模型的 rollout 吞吐量接口"
 created_at: "2026-07-24T18:06:01+08:00"
-updated_at: "2026-07-24T18:06:01+08:00"
+updated_at: "2026-07-24T18:38:09+08:00"
 aliases: ["Single-Pass Drifting World Model", "DriftWorld", "单次前向漂移世界模型"]
 tags: []
 domains: ["world-modeling", "robot-planning"]
 confidence: "medium"
 source_ids: ["source_ce00fba8d7127c890fdcc46e"]
-relations: [{"type": "derived_from", "target_id": "source_ce00fba8d7127c890fdcc46e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都把预测模型置于动作决策接口中；本概念聚焦候选 rollout 的生成吞吐量，而既有概念聚焦高频动作与低频语义规划的职责分离。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_ce00fba8d7127c890fdcc46e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都把预测模型置于动作决策接口中；本概念聚焦候选 rollout 的生成吞吐量，而既有概念聚焦高频动作与低频语义规划的职责分离。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都把预测模型置于动作决策接口中；本概念聚焦候选 rollout 的生成吞吐量，而既有概念聚焦高频动作与低频语义规划的职责分离。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_ce00fba8d7127c890fdcc46e"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_754995a5fd604aa50ec30b29"], "importance": "high", "changed_belief": "世界模型速度不只是工程优化；当采样速度限制候选动作数量时，生成吞吐量会改变规划和离线策略排序是否可实际使用。", "surprising": "", "connections": [], "open_questions": ["单步高速生成在长时程接触、遮挡和分布外动作下的误差累积，何时会抵消其增加候选 rollout 数量带来的决策收益？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_84c0fe1fb69b55f93614"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_84c0fe1fb69b55f93614-concept-1.md"
-origin_candidate_sha256: "aae2ece45dd082eb4b021092d00783cda398715bb5111e8cc469d94cfad0c834"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 单次前向动作条件世界模型的 rollout 吞吐量接口
```
