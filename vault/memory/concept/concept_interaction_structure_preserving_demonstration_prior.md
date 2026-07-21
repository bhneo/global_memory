---
id: "concept_interaction_structure_preserving_demonstration_prior"
type: "concept"
status: "working"
title: "手—物交互结构保真的示范先验"
created_at: "2026-07-20T13:36:20+08:00"
updated_at: "2026-07-20T13:37:47+08:00"
aliases: ["interaction-structure-preserving demonstration prior", "手—物交互结构保真先验", "REGRIND", "hand-object interaction mesh", "object-centric keypoint reference"]
tags: []
domains: ["embodied-ai", "dexterous-manipulation", "demonstration-transfer", "retargeting", "sim-to-real"]
confidence: "high"
source_ids: ["source_b7444ef42015f4f3b6f51032"]
relations: [{"type": "derived_from", "target_id": "source_b7444ef42015f4f3b6f51032", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_5b49f7afd60ba18d35ca58e8", "reason": "二者都保留手—物交互结构；REGRIND 的 keypoint mesh 表达空间关系，TactiDex 进一步显式表达接触时序、区域和力。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_64c23c660c9017a5bf73d012", "reason": "二者都用 hand-object relational targets 代替逐关节复制；REGRIND 离线构造 reference 并训练 residual RL，TELEDEXTER 在线传递连续子目标。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_b1b62d103e0a768399664d9d", "reason": "二者都把人类示范转成允许机器人重求可行解的中间表示；REGRIND 保持交互 keypoints，DemoBridge 优化碰撞约束轨迹并在仿真中分阶段回退。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_fc70bfc09ac7d9473592f09c", "reason": "二者都用结构化 reference 缩小 RL 搜索；手—物先验围绕单示范交互拓扑，PAKE 的 KNF 表达给定末端目标下的运动学多解分布。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_b7444ef42015f4f3b6f51032"
reflection_context: {"reflection_ids": ["reflection_070e73598e48429fb5eafe01", "reflection_631ecd2479bd127e62730569", "reflection_65fb6fe12e2291077f28900c", "reflection_70226423f917bfceeef74a93", "reflection_e8e62c04da8ad9f420c37be4"], "importance": "weekly", "changed_belief": "全身控制的冗余不必由单一 end-to-end RL 在原始关节空间从头搜索；可以先把运动学可行解分布编码成可导航 latent，再把动力学和稳定性留给低层。\nA teleoperation interface need not copy every human joint. Sparse joint hand-object targets can preserve task intent while leaving the robot freedom to reorganize contacts, perform finger gaiting, and satisfy embodiment constraints.\nSingle-view video transfer is best treated as a closed inference-and-validation loop. Perception proposes geometry and phase, planning checks embodiment feasibility, and simulation backtracks when the proposed motion fails.\n此前 retargeting 成败常归因于手部姿态匹配精度；该工作提示，真正影响下游 RL 的是手指与物体之间的空间—接触关系是否被保留，以及 reference 是否为探索提供物理可行邻域。\n此前人到机器人 dexterous transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。", "surprising": "框架把躯干高度、roll、pitch 当作额外手臂自由度来扩大工作空间，同时仍要求底盘速度跟踪，明确利用而非压制浮动基座冗余。\nOne co-tracking controller supports real-time teleoperation across two dexterous hands and seven tasks, and the collected demonstrations train autonomous policies; however, autonomous evaluation uses simplified task subsets.\nThe paper reports transfer from three real demonstrations with repeated trials, yet the most consequential bottleneck is still basic object tracking under occlusion rather than policy scale.\n简洁 pipeline 能在两种多指手、剪刀和螺丝刀任务上零样本 sim-to-real，但其成功依赖 mocap object state 与逐平台系统辨识，远非免工程的通用方案。\n纯运动学 baseline 的 kinematic success 明显高于 tactile-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。", "connections": [{"shared_mechanism": "与 REGRIND 都先构造结构化参考/先验，再用 RL 学习闭环残差或选择。", "boundary": "PAKE 的硬件证据来自带六自由度机械臂的四足平台，8 个任务共 24 回合；不能外推到任意人形、本体或高冲击接触。", "difference": "PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。"}, {"shared_mechanism": "Like progressive VLA demonstration curricula, it decomposes complex skills into intermediate targets that are easier to learn than a complete end-to-end trajectory.", "boundary": "The system depends on reliable MoCap estimates of hand and object pose, and simulation does not cover all tool-environment interactions. Contact jams, stalls, and out-of-distribution disturbances remain failure modes.", "difference": "A curriculum organizes data and task difficulty, whereas TELEDEXTER's consecutive subgoals are a live control interface executed by a low-level reinforcement-learning policy."}, {"shared_mechanism": "Like TELEDEXTER, DemoBridge preserves task-level geometric relations rather than directly retargeting every human joint.", "boundary": "Evidence is limited to a single arm, small demonstration counts, and the tested objects and scenes. Occlusion, reconstruction error, and bimanual interaction remain outside the demonstrated boundary.", "difference": "TELEDEXTER is live hand-object teleoperation with an RL contact controller; DemoBridge is offline single-view trajectory reconstruction with collision planning and simulator validation."}, {"shared_mechanism": "与 TactiDex 都试图把人类示范从几何轨迹提升为交互结构监督。", "boundary": "REGRIND 仅覆盖四个 task-hand setting，并依赖动作捕捉、object pose 与细致系统辨识；在野视觉和未知物体状态仍未解决。", "difference": "REGRIND 用 hand-object keypoint mesh 和 residual RL 保留空间交互；TactiDex 进一步显式记录并监督接触压力与时序。"}, {"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态。", "boundary": "TactiSkill 的真实部署当前主要继承仿真中学习的触觉约束，传感噪声、分辨率与柔顺性差异会削弱 sim-to-real 力对齐；闭环真机触觉适配仍是未来工作。", "difference": "多时间尺度触觉世界模型强调运行时分层预测与残差；TactiDex/TactiSkill 首先提供人类触觉 reference、三分量奖励与接触保真评测。"}], "open_questions": ["怎样检测目标任务所需解落在 KNF 支持集之外，并安全扩展 reference 分布？", "How should subgoal tolerance encode completion, operator intent, and contact safety simultaneously?", "Can phase validation remain reliable when objects are deformable, heavily occluded, or jointly manipulated by two arms?", "何时 keypoint interaction mesh 已足够，何时必须加入触觉、力或多示范来辨别接触模式？", "哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-20T13:37:47+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_0b860431d41b8b40c196"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0b860431d41b8b40c196-concept-1.md"
origin_candidate_sha256: "02eea85fd143a7a975c1c0b2778b71a2c64d08d1f6190ea98d1973cdee219f60"
memory_schema_version: 2
last_consolidation_id: "consolidation_5988f005855dd9f24dd99b32"
---

# 手—物交互结构保真的示范先验

从人类示范中保留手指、物体与任务关键点之间的空间—接触关系，把该关系作为机器人 reference 与探索邻域，再由本体特定的运动学、残差控制或仿真门禁求解可执行动作。该先验比逐关节姿态更接近任务结构，但受物体状态可观测性、示范接触拓扑和系统辨识范围限制。
