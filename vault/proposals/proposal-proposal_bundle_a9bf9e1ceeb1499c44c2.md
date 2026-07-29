---
id: "proposal_bundle_a9bf9e1ceeb1499c44c2"
type: "proposal"
status: "migrated"
title: "Compile bundle：[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents"
created_at: "2026-07-23T18:06:36+08:00"
updated_at: "2026-07-23T18:06:36+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_4ceaa5243dd0d99116547dda"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_e3312f42256bfd1c30ba713b"
input_sha256: "9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_4b29abb8c07d6365b04b97c3", "target_path": "vault/knowledge/concepts/concept_4b29abb8c07d6365b04b97c3-面向策略学习的可运行交互孪生.md", "base_sha256": null, "candidate_sha256": "a653682330de05b7c5dbca0278f06ec582f184fde76d4563c7fee81edd2e13ff", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_a9bf9e1ceeb1499c44c2-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_4b29abb8c07d6365b04b97c3.md", "working_at": "2026-07-23T18:06:36+08:00"}]
existing_context: [{"id": "input_76b68fdb85fc376d2226e524", "type": "input", "title": "[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents", "path": "vault/inputs/input-input_76b68fdb85fc376d2226e524.md", "status": "active", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "…Physics-based World [Modeling] with Vision-Language Agents\n\nInput Episode for `source_4ceaa5243dd0d99116547dda`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，[Agentic]-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2…", "match_reason": "metadata:title"}, {"id": "input_a070092fbe4bbba0a3effe85", "type": "input", "title": "GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub", "path": "vault/inputs/input-input_a070092fbe4bbba0a3effe85.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "…Agentic Infrastructure for the Physical [World] · GitHub\n\nInput Episode for `source_6b52a51e2b4a3be43c97c386`. The immutable Source remains authoritative.\n\n# GitHub…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_training_efficiency_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 上以 700 次迭代达到 90% 成功率，论文报告其相对 EVOLVE-VLA 收敛快 2.4×", "path": "vault/memory/claim/claim_agentic_vla_training_efficiency_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的训练效率\n\n在 LIBERO-Long 达到论文定义的 90% 成功率阈值时，[Agentic]-VLA 使用 700 次训练迭代和 22.4k rollouts；EVOLVE…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的跨任务适应结果\n\n论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_one_shot_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点", "path": "vault/memory/claim/claim_agentic_vla_one_shot_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的 one-shot 结果\n\n在每个任务仅使用一条 demonstration 做 SFT pre-training 的设定下，[Agentic]-VLA 在 LIBERO 四套件上的平均成功率为…", "match_reason": "metadata:title"}, {"id": "concept_asymmetric_frozen_vla_harness", "type": "concept", "title": "冻结 VLA 的非对称技能编排", "path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "status": "working", "source_ids": ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386"], "snippet": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知…", "match_reason": "metadata:aliases"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The [world] component and dual-system [world]-action models both use predictive representations to connect perception with possible…", "match_reason": "metadata:title"}, {"id": "concept_09dc6e910b167ba474c89c38", "type": "concept", "title": "世界动作模型的激活空间鲁棒性 steering", "path": "vault/memory/concept/concept_09dc6e910b167ba474c89c38.md", "status": "working", "source_ids": ["source_38cba686373b003398483ab2"], "snippet": "# 世界动作模型的激活空间鲁棒性 steering\n\n对世界动作模型在标称与扰动 rollout 的内部激活进行对比，若鲁棒性相关特征在低维子空间中具有可分离结构，可据此构造对比激活方向，并利用局部线性动态在推理时以受惩罚的闭环控制调节激活；该可操控性需要按模型架构和扰动类型分别验证。", "match_reason": "metadata:aliases"}, {"id": "input_e69b286ace68f56c81ab185b", "type": "input", "title": "[2607.12894] Hy-Embodied-VLM-1.0: Efficient Physical-World Agents", "path": "vault/inputs/input-input_e69b286ace68f56c81ab185b.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "…Efficient Physical-[World] Agents\n\nInput Episode for `source_bd08e368730960f4f6ce19ca`. The immutable Source remains authoritative.\n\n# [2607.12894] Hy-Embodied…", "match_reason": "metadata:title"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied Foundation Models for Real-[World] Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "concept_f67f822ee20789d74d7b75e3", "type": "concept", "title": "物理失败合成驱动的稠密机器人奖励建模", "path": "vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md", "status": "working", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# 物理失败合成驱动的稠密机器人奖励建模\n\n通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。", "match_reason": "metadata:aliases"}, {"id": "reflection_cb246940931502d077f687f5", "type": "reflection", "title": "DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配", "path": "vault/reflections/reflection-reflection_cb246940931502d077f687f5.md", "status": "active", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配\n\n## Why important\n\nDenseReward 把机器人奖励学习的两个薄弱环节放在同一数据管线中：用定向扰动合成碰撞、漏抓、掉落和恢复等物理失败，再学习带历史帧的逐时刻任务进度奖励。\n\n## What changed\n\n此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。\n\n## Surprising\n\n两帧历史优于一帧…", "match_reason": "metadata:domains"}, {"id": "reflection_4b63a8834e11b28db3cf2fdc", "type": "reflection", "title": "TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心", "path": "vault/reflections/reflection-reflection_4b63a8834e11b28db3cf2fdc.md", "status": "active", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心\n\n## Why important\n\nTACTIC 不只把触觉追加到 observation，而是让 distributed tactile、proximity map、contact Jacobian sampling 和 hybrid…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_4ceaa5243dd0d99116547dda"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_e3312f42256bfd1c30ba713b`
- 编译前召回已有对象：16
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_4b29abb8c07d6365b04b97c3-面向策略学习的可运行交互孪生.md
@@ -0,0 +1,20 @@
+---
+id: "concept_4b29abb8c07d6365b04b97c3"
+type: "concept"
+status: "proposal"
+title: "面向策略学习的可运行交互孪生"
+created_at: "2026-07-23T18:06:36+08:00"
+updated_at: "2026-07-23T18:06:36+08:00"
+aliases: ["Runnable Interaction Twin", "Simulatable Episodic Twin", "可模拟情节孪生"]
+tags: []
+domains: ["real2sim", "robotics", "world-modeling"]
+confidence: "medium"
+source_ids: ["source_4ceaa5243dd0d99116547dda"]
+relations: [{"type": "derived_from", "target_id": "source_4ceaa5243dd0d99116547dda", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_4ceaa5243dd0d99116547dda"
+reflection_context: {"reflection_ids": ["reflection_c8a3c97a77f64d38720a8539"], "importance": "high", "changed_belief": "此前容易把 Real2Sim 当成资产重建问题；该来源表明，面向机器人下游使用时，状态、物理和交互轨迹的可执行组合才是关键交付物。", "surprising": "", "connections": [], "open_questions": ["在不同材质、接触和传感噪声条件下，怎样衡量 episodic twin 对真实闭环策略评测的保真度？"]}
+---
+
+# 面向策略学习的可运行交互孪生
+
+将真实对象—机器人交互记录组织为可在物理仿真器中重放的 episodic twin：它需要联合保留场景几何、对象状态、推断的物理参数、参与者、相机、位姿和轨迹，使该记录可用于下游策略学习或评测。该概念不保证视觉重建、物理参数估计或跨场景泛化已经充分准确。
```
