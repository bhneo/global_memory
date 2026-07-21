---
id: "concept_9443d1789c9a179bd1611be3"
type: "concept"
status: "proposal"
title: "示范先验条件化的 VLA 结构化探索"
created_at: "2026-07-20T12:27:21+08:00"
updated_at: "2026-07-20T12:27:21+08:00"
aliases: ["Structured exploration with demonstration priors", "RL Exploration Token", "ExToken", "示范行为模式探索"]
tags: []
domains: ["embodied-ai", "vla", "robot-rl", "exploration"]
confidence: "high"
source_ids: ["source_5b8c57a9bef3348109f3b7bb"]
relations: [{"type": "derived_from", "target_id": "source_5b8c57a9bef3348109f3b7bb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "二者都以小型条件接口保护 VLA 先验；前者改变探索模式分布，后者暴露供 actor-critic 在线优化的内部读出。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_5b8c57a9bef3348109f3b7bb"
reflection_context: {"reflection_ids": ["reflection_305130038ee9fd3cb9e18ec4"], "importance": "high", "changed_belief": "此前把样本效率主要理解为每条轨迹被更充分利用；该工作提示，先控制采样分布中的行为模式多样性，可能比单纯增加 rollout 或改进优化器更基础。", "surprising": "论文实验中保留 512 条最多样的轨迹可匹配 1024 条标准 rollout，而标准 512 条明显更差；这把轨迹多样性从直觉性目标提升为可直接影响训练效率的变量。", "connections": [{"shared_mechanism": "与 VLA 的强化学习读出接口都把大策略的在线适配压缩到一个小型条件接口，并尽量保留预训练行为先验。", "boundary": "ExToken 的证据来自论文所选仿真和真机操作任务，且 token 由离线示范视频聚类得到；不能外推到无示范、开放世界或长时程探索。", "difference": "RL 读出接口从 VLA 内部特征学习供 actor-critic 使用的任务表示；ExToken 用离线示范的行为模式 token 主动改变 rollout 分布，并另学状态条件选择器。"}], "open_questions": ["轨迹多样性应在动作、状态覆盖、接触模式还是任务结果空间中度量，哪个与真实样本效率最稳定相关？"]}
---

# 示范先验条件化的 VLA 结构化探索

从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。
