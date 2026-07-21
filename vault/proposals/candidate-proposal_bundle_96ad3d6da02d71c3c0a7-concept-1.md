---
id: "concept_abb38fe58cbeee09ce87a01d"
type: "concept"
status: "proposal"
title: "跨轨迹任务进度代理校正"
created_at: "2026-07-20T11:56:21+08:00"
updated_at: "2026-07-20T11:56:21+08:00"
aliases: ["UR-VC", "Unsupervised Robotic Value Correction", "time-derived progress correction"]
tags: []
domains: ["embodied-ai", "vla", "value-learning", "progress-estimation"]
confidence: "high"
source_ids: ["source_e326446389e083c6ba9c94c2"]
relations: [{"type": "derived_from", "target_id": "source_e326446389e083c6ba9c94c2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_e326446389e083c6ba9c94c2"
reflection_context: {"reflection_ids": ["reflection_052db872e2258b0e016c5ebf"], "importance": "weekly", "changed_belief": "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。", "surprising": "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。", "connections": [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}], "open_questions": ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？"]}
---

# 跨轨迹任务进度代理校正

跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。
