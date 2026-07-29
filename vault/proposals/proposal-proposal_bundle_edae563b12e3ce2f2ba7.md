---
id: "proposal_bundle_edae563b12e3ce2f2ba7"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T10:46:45+08:00"
updated_at: "2026-07-28T10:46:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_d15eb994dab1398b83534ed1"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_62445f7e7b9f6cf4a3067bec"
input_sha256: "61cc39d44eabf2f119880a9f1bd0cbb9409382ac3f67beff4c952f69290a30ed"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_a6e832624a3a4b33fb48980a", "target_path": "vault/memory/concept/concept_a6e832624a3a4b33fb48980a.md", "base_sha256": "523b5abbff8a6deaac363a2f6e29d4d53b779cb8892aefbec0f96dcc418079af", "candidate_sha256": "607b6e303dd98c0a62dadc3d9f56f940d6b6270cbe1cdde4b246e6700cf0e2f5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_edae563b12e3ce2f2ba7-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_edae563b12e3ce2f2ba7-concept-1.md", "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_cdbe55276db1fb0eb0aa370a", "type": "concept", "title": "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere equilibrium fluctuations", "path": "vault/memory/concept/concept_cdbe55276db1fb0eb0aa370a.md", "status": "working", "source_ids": ["source_3851b9ffbfbae3ca166308fd", "source_323f116c3573f26f4af7785d"], "snippet": "# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-[time] control of hard-sphere fluctuations\n\n对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann…", "match_reason": "metadata:title"}, {"id": "input_8f16a3ad954bd05b1a2a7752", "type": "input", "title": "[2012.03813] Long-time correlations for a hard-sphere gas at equilibrium", "path": "vault/inputs/input-input_8f16a3ad954bd05b1a2a7752.md", "status": "active", "source_ids": ["source_a5f4d6734479eea71ff9a2a4"], "snippet": "# [2012.03813] Long-[time] correlations for a hard-sphere gas at equilibrium\n\nInput Episode for `source_a5f4d6734479eea71ff9a2a4`. The…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、[Long] 成功率分别为 `97.2…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_training_efficiency_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 上以 700 次迭代达到 90% 成功率，论文报告其相对 EVOLVE-VLA 收敛快 2.4×", "path": "vault/memory/claim/claim_agentic_vla_training_efficiency_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的训练效率\n\n在 LIBERO-[Long] 达到论文定义的 90% 成功率阈值时，Agentic-VLA 使用 700 次训练迭代和 22.4k rollouts；EVOLVE…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的跨任务适应结果\n\n论文在 LIBERO-[Long] 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "metadata:title"}, {"id": "reflection_2e36e252e77618ec2e7ba6b5", "type": "reflection", "title": "硬球到 Boltzmann 的长时导出综述：光滑解寿命是边界 / long-time derivation is bounded by smooth-solution lifespan", "path": "vault/reflections/reflection-reflection_2e36e252e77618ec2e7ba6b5.md", "status": "active", "source_ids": ["source_5455a1b96c9684e7ce041786"], "snippet": "# 硬球到 Boltzmann 的长时导出综述：光滑解寿命是边界 / long-[time] derivation is bounded by smooth-solution lifespan\n\n## Why important\n\n综述说明硬球动力学的收敛可延长到 Boltzmann 方程光滑解存在的时间…", "match_reason": "metadata:title"}, {"id": "reflection_3231f184af64cbede55c5e55", "type": "reflection", "title": "硬球平衡涨落：任意长时间的完整高斯极限 / equilibrium hard-sphere fluctuations have a full Gaussian long-time limit", "path": "vault/reflections/reflection-reflection_3231f184af64cbede55c5e55.md", "status": "active", "source_ids": ["source_323f116c3573f26f4af7785d"], "snippet": "# 硬球平衡涨落：任意长时间的完整高斯极限 / equilibrium hard-sphere fluctuations have a full Gaussian long-[time] limit\n\n## Why important\n\n该文将平衡硬球 Boltzmann--Grad…", "match_reason": "metadata:title"}, {"id": "reflection_46d4dcf890fae70ce354f2d4", "type": "reflection", "title": "长时波湍流严格导出：有效窗口由 WKE 寿命而非小动理学时间决定 / long-time wave-turbulence justification is bounded by WKE lifespan", "path": "vault/reflections/reflection-reflection_46d4dcf890fae70ce354f2d4.md", "status": "active", "source_ids": ["source_ebf287b4d71ccdc41101466e"], "snippet": "# 长时波湍流严格导出：有效窗口由 WKE 寿命而非小动理学时间决定 / long-[time] wave-turbulence justification is bounded by WKE lifespan\n\n## Why important\n\nDeng 与…", "match_reason": "metadata:title"}, {"id": "concept_a6e832624a3a4b33fb48980a", "type": "concept", "title": "稀薄硬球到非线性 Boltzmann 方程的任意固定时间极限 / arbitrary-fixed-time hard-sphere limit to nonlinear Boltzmann", "path": "vault/memory/concept/concept_a6e832624a3a4b33fb48980a.md", "status": "working", "source_ids": ["source_d15eb994dab1398b83534ed1"], "snippet": "# 稀薄硬球到非线性 Boltzmann 方程的任意固定时间极限 / arbitrary-fixed-time hard-sphere limit to nonlinear Boltzmann\n\n在 d≥2、论文规定的光滑初值、grand-canonical Boltzmann--Grad 稀薄硬球系综以及 Boltzmann 解存在并满足统一 Maxwellian 型界的条件下，作者证明经验分布在任意预先固定的有限终止时间内收敛到非线性 Boltzmann 方程。若 Bol", "match_reason": "metadata:aliases"}, {"id": "reflection_93b0ac37e90a8619ac72c25e", "type": "reflection", "title": "从可测时间膨胀到回到过去：相对论时间旅行的证据层级 / evidence tiers from time dilation to past-directed travel", "path": "vault/reflections/reflection-reflection_93b0ac37e90a8619ac72c25e.md", "status": "active", "source_ids": ["source_f4a5da629b6c1d876f6dbdef"], "snippet": "# 从可测时间膨胀到回到过去：相对论时间旅行的证据层级 / evidence tiers from [time] dilation to past-directed travel\n\n## Why important\n\n文章把高速运动造成的可测固有时差、广义相对论中允许闭合类时曲线的解，以及需要极端条件的虫洞设想并置；必须把“时间旅行…", "match_reason": "metadata:title"}, {"id": "concept_test_time_fast_weight_robot_memory", "type": "concept", "title": "机器人策略的测试时快速权重记忆", "path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "status": "working", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# 机器人策略的测试时快速权重记忆\n\nRoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮…", "match_reason": "metadata:aliases"}, {"id": "input_72936b45ec8a50ec68020711", "type": "input", "title": "[gr-qc/0602001] Non-equilibrium Thermodynamics of Spacetime", "path": "vault/inputs/input-input_72936b45ec8a50ec68020711.md", "status": "active", "source_ids": ["source_086150581c4c39aee0813d57"], "snippet": "# [gr-qc/0602001] Non-equilibrium Thermodynamics of Spacetime\n\nInput Episode for `source_086150581c4c39aee0813d57`. The immutable Source remains authoritative.\n\n# [gr-qc/0602001] Non-equilibrium Thermodynamics of Spacetime\n\n> 原始内容：[vault/ra", "match_reason": "full-text:body"}, {"id": "input_b6e3f29e044d376ac9465e43", "type": "input", "title": "[2504.06297] Comment on \"Hilbert's Sixth Problem: Derivation of Fluid Equations via Boltzmann's Kinetic Theory\" by Deng, Hani, and Ma", "path": "vault/inputs/input-input_b6e3f29e044d376ac9465e43.md", "status": "active", "source_ids": ["source_969253c160fba88bdba75603"], "snippet": "# [2504.06297] Comment on \"Hilbert's Sixth Problem: Derivation of Fluid Equations via Boltzmann's Kinetic Theory\" by Deng, Hani, and Ma\n\nInput Episode for `source_969253c160fba88bdba75603`. The immutable Source remains authoritative.\n\n# [25", "match_reason": "metadata:title"}, {"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "# [hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT\n\nInput Episode for `source_6c0e05be9fc0c544826d7f9b`. The immutable Source remains authoritative.\n\n# [hep-th/0603001] Holographic Derivation of Entanglement Entr", "match_reason": "metadata:title"}, {"id": "concept_abb38fe58cbeee09ce87a01d", "type": "concept", "title": "跨轨迹任务进度代理校正", "path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# 跨轨迹任务进度代理校正\n\n跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。", "match_reason": "metadata:aliases"}, {"id": "tension_bc930b97cbd3a0a443471b29", "type": "tension", "title": "Hilbert 第六问题中严格稀薄气体极限与物理完成度的张力 / rigorous dilute-gas limit versus physical completion of Hilbert VI", "path": "vault/memory/tension/tension_bc930b97cbd3a0a443471b29.md", "status": "working", "source_ids": ["source_54db4048fe0581a68c146634"], "snippet": "# Hilbert 第六问题中严格稀薄气体极限与物理完成度的张力 / rigorous dilute-gas limit versus physical completion of Hilbert VI\n\n一侧是：在明确的 Boltzmann--Grad 稀薄硬球、初值、解存在与迭代极限条件下，可以严格连接 Newtonian 粒子动力学、Boltzmann 方程和特定流体方程。另一侧是：批评者认为第一极限令体积分数趋零，molecular chaos 只在稀薄区间可信，因此", "match_reason": "metadata:aliases"}, {"id": "input_0b5fbfe5c9ecee3146dadce4", "type": "input", "title": "[gr-qc/0209088] Gravity from Spacetime Thermodynamics", "path": "vault/inputs/input-input_0b5fbfe5c9ecee3146dadce4.md", "status": "active", "source_ids": ["source_ad785f5be8067788394ec708"], "snippet": "# [gr-qc/0209088] Gravity from Spacetime Thermodynamics\n\nInput Episode for `source_ad785f5be8067788394ec708`. The immutable Source remains authoritative.\n\n# [gr-qc/0209088] Gravity from Spacetime Thermodynamics\n\n> 原始内容：[vault/raw/objects/sh", "match_reason": "full-text:body"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "# GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The immutable Source remains authoritative.\n\n# GitHub - NVIDIA/Isaac-GR00T: NV", "match_reason": "metadata:title"}, {"id": "input_30f3dd905ee97551e16138bd", "type": "input", "title": "Chelsea Finn & Perry Dong：真实场景强化学习实现VLA后训练", "path": "vault/inputs/input-input_30f3dd905ee97551e16138bd.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "# Chelsea Finn & Perry Dong：真实场景强化学习实现VLA后训练\n\nInput Episode for `source_8b41a014bee47c4239a2fa81`. The immutable Source remains authoritative.\n\n# Chelsea Finn & Perry Dong：真实场景强化学习实现VLA后训练\n\n> 原始内容：[vault/raw/objects/sha256/15/20/15201becf4f", "match_reason": "full-text:body"}, {"id": "input_3b2d4a128c5dcd00c6d756b5", "type": "input", "title": "[2210.03878] An improved restriction estimate in $\\mathbb{R}^3$", "path": "vault/inputs/input-input_3b2d4a128c5dcd00c6d756b5.md", "status": "active", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# [2210.03878] An improved restriction estimate in $\\mathbb{R}^3$\n\nInput Episode for `source_299adfe6dd42f97b6f75b777`. The immutable Source remains authoritative.\n\n# [2210.03878] An improved restriction estimate in $\\mathbb{R}^3$\n\n> 原始内容：[", "match_reason": "metadata:title"}, {"id": "input_3b93bb83f5c7407a5a03dcad", "type": "input", "title": "Building scalable AI agents with modular prompt transpilation - Google Developers Blog", "path": "vault/inputs/input-input_3b93bb83f5c7407a5a03dcad.md", "status": "active", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# Building scalable AI agents with modular prompt transpilation - Google Developers Blog\n\nInput Episode for `source_3521fe9ac8d8f054440ec0af`. The immutable Source remains authoritative.\n\n# Building scalable AI agents with modular prompt tr", "match_reason": "metadata:title"}, {"id": "input_41c7203faaf98b68b319eebc", "type": "input", "title": "GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub", "path": "vault/inputs/input-input_41c7203faaf98b68b319eebc.md", "status": "active", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "# GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub\n\nInput Episode for `source_a5f8ae2053", "match_reason": "metadata:title"}, {"id": "input_4846565da5dc1656c16a439a", "type": "input", "title": "[1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms", "path": "vault/inputs/input-input_4846565da5dc1656c16a439a.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms\n\nInput Episode for `source_f366554c5c3887de7c6ad29b`. The immutable Source remains authoritative.\n\n# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms\n\n> ", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_d15eb994dab1398b83534ed1"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "282e3a3fa513c853ee2951555889f101d9c1b8517a4b65c9e87831e97ed507a9"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_62445f7e7b9f6cf4a3067bec`
- 编译前召回已有对象：25
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_a6e832624a3a4b33fb48980a.md
+++ candidate:vault/memory/concept/concept_a6e832624a3a4b33fb48980a.md
@@ -1,10 +1,10 @@
 ---
 id: "concept_a6e832624a3a4b33fb48980a"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "稀薄硬球到非线性 Boltzmann 方程的任意固定时间极限 / arbitrary-fixed-time hard-sphere limit to nonlinear Boltzmann"
 created_at: "2026-07-28T10:04:28+08:00"
-updated_at: "2026-07-28T10:04:30+08:00"
+updated_at: "2026-07-28T10:46:45+08:00"
 aliases: ["long-time hard-sphere Boltzmann derivation", "arbitrary fixed time Boltzmann-Grad limit", "长时硬球 Boltzmann 极限", "Hilbert sixth problem hard-sphere scope"]
 tags: []
 domains: ["kinetic-theory", "boltzmann-equation", "mathematical-physics"]
@@ -12,28 +12,9 @@
 source_ids: ["source_d15eb994dab1398b83534ed1"]
 relations: [{"type": "derived_from", "target_id": "source_d15eb994dab1398b83534ed1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
 change_reason: "compile bundle from source_d15eb994dab1398b83534ed1"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_2feea84cb30c4bceb6d8165f"], "importance": "high", "changed_belief": "我会把本文首先读作对特定硬球模型第一动力学极限的作者主张，而不是已独立确证的普遍“Hilbert 第六问题已解决”事实。", "surprising": "", "connections": [{"shared_mechanism": "本文和既有尺度稳定性 Reflection 都把微观动力学到宏观方程视为需要逐段验证的极限链。", "boundary": "本文限于 Boltzmann--Grad 稀薄硬球、Boltzmann 解存在及 companion work 的流体衔接；既有 Reflection 讨论的是近似闭合的尺度和稳定性边界。", "difference": "本文主张长时硬球动力学到 Boltzmann 的控制；既有来源分析 Boltzmann 到流体近似在波数与稳定性边界内的成立条件。"}], "open_questions": ["companion work 的流体极限如何逐项满足本文硬球极限的条件，且哪些环节已有独立复核？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "gpt-5.6-sol-high-daily-v2-readmission"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "gpt-5.6-sol-high-daily-v2-readmission"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_2f5cd73c9b5e6e1bea53"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_2f5cd73c9b5e6e1bea53-concept-1.md"
-origin_candidate_sha256: "93c7f545e203261aeeebae573ef6707e45204abe2e1740659ac451960bb094cf"
-origin_cognitive_artifact_sha256: "282e3a3fa513c853ee2951555889f101d9c1b8517a4b65c9e87831e97ed507a9"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 稀薄硬球到非线性 Boltzmann 方程的任意固定时间极限 / arbitrary-fixed-time hard-sphere limit to nonlinear Boltzmann
```
