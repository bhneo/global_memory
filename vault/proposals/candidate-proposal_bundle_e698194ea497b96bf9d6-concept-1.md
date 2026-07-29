---
id: "concept_4739daf4ef7eacc9153c535f"
type: "concept"
status: "proposal"
title: "可靠价值驱动的离线到在线策略改进"
created_at: "2026-07-20T11:55:37+08:00"
updated_at: "2026-07-28T16:27:52+08:00"
aliases: ["Robo-ValueRL", "value-guided offline-to-online adaptation"]
tags: []
domains: ["embodied-ai", "robot-rl", "vla", "value-learning"]
confidence: "medium"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}, {"type": "depends_on", "target_id": "concept_abb38fe58cbeee09ce87a01d", "reason": "当价值监督来自时间进度时，先校正跨轨迹进度代理是避免下游选择偏差自强化的上游条件。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
change_reason: "compile bundle from source_7b278ba348f2a8bb94cce1fc"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_052db872e2258b0e016c5ebf", "reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。\n同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}, {"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？", "价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
proposed_status: "working"
---

# 可靠价值驱动的离线到在线策略改进

可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。
