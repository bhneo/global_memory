---
id: "proposal_bundle_0b860431d41b8b40c196"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T13:36:20+08:00"
updated_at: "2026-07-20T13:36:21+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b7444ef42015f4f3b6f51032"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_5fe5b07135b6bb9c46cb8cd5"
input_sha256: "dfc4374df92563b036857591570080537e3c6dfb2c7ad8235ef6f1c12b986a4f"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_interaction_structure_preserving_demonstration_prior", "target_path": "vault/knowledge/concepts/concept_interaction_structure_preserving_demonstration_prior-手-物交互结构保真的示范先验.md", "base_sha256": null, "candidate_sha256": "02eea85fd143a7a975c1c0b2778b71a2c64d08d1f6190ea98d1973cdee219f60", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0b860431d41b8b40c196-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_interaction_structure_preserving_demonstration_prior.md", "working_at": "2026-07-20T13:36:21+08:00"}]
existing_context: [{"id": "work_arxiv_1810_08647", "type": "work", "title": "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning", "path": "vault/memory/work/work_arxiv_1810_08647.md", "status": "working", "source_ids": ["source_e9ed0a3745aea832b64d7fa7", "source_c019c0a492cc659d7858134d"], "snippet": "# [1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep [Reinforcement] Learning\n\n## Logical work identity\n\n- arXiv：`1810…", "match_reason": "metadata:title"}, {"id": "claim_wechat_im_rl_framework_internal_rewards_20260716", "type": "claim", "title": "该文称经典 RL 虽常被视为仅处理外在奖励，但 Barto 等框架可将奖励生成机制置于「内部环境」，内在与外在奖励可统一建模", "path": "vault/memory/claim/claim_wechat_im_rl_framework_internal_rewards_20260716.md", "status": "working", "source_ids": ["source_91199da18f239c48bbcdd49f"], "snippet": "# RL 统一奖励\n\n内在奖励可在体内生成；RL 框架不必限定外部通道。", "match_reason": "metadata:tags"}, {"id": "concept_f9a9f1d1818632c0380b7942", "type": "concept", "title": "VLA 的强化学习读出接口", "path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "status": "working", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# VLA 的强化学习读出接口\n\nVLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 actor-critic 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。", "match_reason": "metadata:aliases"}, {"id": "claim_physo_rnn_reinforcement_learning_method_20260716", "type": "claim", "title": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式", "path": "vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。", "match_reason": "metadata:tags"}, {"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward…", "match_reason": "metadata:tags"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…That distinction helps organize post-training questions without treating [reinforcement] learning as one method.\n\n## What changed\n\nReliability gains…", "match_reason": "metadata:domains"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b7444ef42015f4f3b6f51032"}
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_5fe5b07135b6bb9c46cb8cd5`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_interaction_structure_preserving_demonstration_prior-手-物交互结构保真的示范先验.md
@@ -0,0 +1,20 @@
+---
+id: "concept_interaction_structure_preserving_demonstration_prior"
+type: "concept"
+status: "proposal"
+title: "手—物交互结构保真的示范先验"
+created_at: "2026-07-20T13:36:20+08:00"
+updated_at: "2026-07-20T13:36:20+08:00"
+aliases: ["interaction-structure-preserving demonstration prior", "手—物交互结构保真先验", "REGRIND", "hand-object interaction mesh", "object-centric keypoint reference"]
+tags: []
+domains: ["embodied-ai", "dexterous-manipulation", "demonstration-transfer", "retargeting", "sim-to-real"]
+confidence: "high"
+source_ids: ["source_b7444ef42015f4f3b6f51032"]
+relations: [{"type": "derived_from", "target_id": "source_b7444ef42015f4f3b6f51032", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_5b49f7afd60ba18d35ca58e8", "reason": "二者都保留手—物交互结构；REGRIND 的 keypoint mesh 表达空间关系，TactiDex 进一步显式表达接触时序、区域和力。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_64c23c660c9017a5bf73d012", "reason": "二者都用 hand-object relational targets 代替逐关节复制；REGRIND 离线构造 reference 并训练 residual RL，TELEDEXTER 在线传递连续子目标。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_b1b62d103e0a768399664d9d", "reason": "二者都把人类示范转成允许机器人重求可行解的中间表示；REGRIND 保持交互 keypoints，DemoBridge 优化碰撞约束轨迹并在仿真中分阶段回退。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_fc70bfc09ac7d9473592f09c", "reason": "二者都用结构化 reference 缩小 RL 搜索；手—物先验围绕单示范交互拓扑，PAKE 的 KNF 表达给定末端目标下的运动学多解分布。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b7444ef42015f4f3b6f51032"
+reflection_context: {"reflection_ids": ["reflection_070e73598e48429fb5eafe01", "reflection_631ecd2479bd127e62730569", "reflection_65fb6fe12e2291077f28900c", "reflection_70226423f917bfceeef74a93", "reflection_e8e62c04da8ad9f420c37be4"], "importance": "weekly", "changed_belief": "全身控制的冗余不必由单一 end-to-end RL 在原始关节空间从头搜索；可以先把运动学可行解分布编码成可导航 latent，再把动力学和稳定性留给低层。\nA teleoperation interface need not copy every human joint. Sparse joint hand-object targets can preserve task intent while leaving the robot freedom to reorganize contacts, perform finger gaiting, and satisfy embodiment constraints.\nSingle-view video transfer is best treated as a closed inference-and-validation loop. Perception proposes geometry and phase, planning checks embodiment feasibility, and simulation backtracks when the proposed motion fails.\n此前 retargeting 成败常归因于手部姿态匹配精度；该工作提示，真正影响下游 RL 的是手指与物体之间的空间—接触关系是否被保留，以及 reference 是否为探索提供物理可行邻域。\n此前人到机器人 dexterous transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。", "surprising": "框架把躯干高度、roll、pitch 当作额外手臂自由度来扩大工作空间，同时仍要求底盘速度跟踪，明确利用而非压制浮动基座冗余。\nOne co-tracking controller supports real-time teleoperation across two dexterous hands and seven tasks, and the collected demonstrations train autonomous policies; however, autonomous evaluation uses simplified task subsets.\nThe paper reports transfer from three real demonstrations with repeated trials, yet the most consequential bottleneck is still basic object tracking under occlusion rather than policy scale.\n简洁 pipeline 能在两种多指手、剪刀和螺丝刀任务上零样本 sim-to-real，但其成功依赖 mocap object state 与逐平台系统辨识，远非免工程的通用方案。\n纯运动学 baseline 的 kinematic success 明显高于 tactile-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。", "connections": [{"shared_mechanism": "与 REGRIND 都先构造结构化参考/先验，再用 RL 学习闭环残差或选择。", "boundary": "PAKE 的硬件证据来自带六自由度机械臂的四足平台，8 个任务共 24 回合；不能外推到任意人形、本体或高冲击接触。", "difference": "PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。"}, {"shared_mechanism": "Like progressive VLA demonstration curricula, it decomposes complex skills into intermediate targets that are easier to learn than a complete end-to-end trajectory.", "boundary": "The system depends on reliable MoCap estimates of hand and object pose, and simulation does not cover all tool-environment interactions. Contact jams, stalls, and out-of-distribution disturbances remain failure modes.", "difference": "A curriculum organizes data and task difficulty, whereas TELEDEXTER's consecutive subgoals are a live control interface executed by a low-level reinforcement-learning policy."}, {"shared_mechanism": "Like TELEDEXTER, DemoBridge preserves task-level geometric relations rather than directly retargeting every human joint.", "boundary": "Evidence is limited to a single arm, small demonstration counts, and the tested objects and scenes. Occlusion, reconstruction error, and bimanual interaction remain outside the demonstrated boundary.", "difference": "TELEDEXTER is live hand-object teleoperation with an RL contact controller; DemoBridge is offline single-view trajectory reconstruction with collision planning and simulator validation."}, {"shared_mechanism": "与 TactiDex 都试图把人类示范从几何轨迹提升为交互结构监督。", "boundary": "REGRIND 仅覆盖四个 task-hand setting，并依赖动作捕捉、object pose 与细致系统辨识；在野视觉和未知物体状态仍未解决。", "difference": "REGRIND 用 hand-object keypoint mesh 和 residual RL 保留空间交互；TactiDex 进一步显式记录并监督接触压力与时序。"}, {"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态。", "boundary": "TactiSkill 的真实部署当前主要继承仿真中学习的触觉约束，传感噪声、分辨率与柔顺性差异会削弱 sim-to-real 力对齐；闭环真机触觉适配仍是未来工作。", "difference": "多时间尺度触觉世界模型强调运行时分层预测与残差；TactiDex/TactiSkill 首先提供人类触觉 reference、三分量奖励与接触保真评测。"}], "open_questions": ["怎样检测目标任务所需解落在 KNF 支持集之外，并安全扩展 reference 分布？", "How should subgoal tolerance encode completion, operator intent, and contact safety simultaneously?", "Can phase validation remain reliable when objects are deformable, heavily occluded, or jointly manipulated by two arms?", "何时 keypoint interaction mesh 已足够，何时必须加入触觉、力或多示范来辨别接触模式？", "哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？"]}
+---
+
+# 手—物交互结构保真的示范先验
+
+从人类示范中保留手指、物体与任务关键点之间的空间—接触关系，把该关系作为机器人 reference 与探索邻域，再由本体特定的运动学、残差控制或仿真门禁求解可执行动作。该先验比逐关节姿态更接近任务结构，但受物体状态可观测性、示范接触拓扑和系统辨识范围限制。
```
