---
id: "concept_event_sensitive_task_progress_memory"
type: "concept"
status: "proposal"
title: "事件敏感的任务进度记忆"
created_at: "2026-07-19T12:18:53+08:00"
updated_at: "2026-07-19T12:18:53+08:00"
aliases: ["event-sensitive task-progress memory", "Temporally Conditioned Memory-Fusion Policy", "TFP", "dynamics-aware belief tracking"]
tags: []
domains: ["embodied-ai", "vla", "robot-memory", "visuomotor-control"]
confidence: "medium"
source_ids: ["source_011483b15aae65e849a3772e"]
relations: [{"type": "derived_from", "target_id": "source_011483b15aae65e849a3772e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "DEHP 决定动作块何时重新查询，TFP 用真实经过时间和不规则查询间隔更新任务 belief；两者分别控制外部重规划节奏与内部记忆节奏。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都让快速事件响应与慢速上下文保持共存，但 TFP 跟踪视觉/本体任务进度，后者建模触觉预测与反应控制。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_011483b15aae65e849a3772e"
uncertainty: "循环全量微调代价高，最大实验需 4 张 H200 约 80 小时；真机验证限于桌面单臂，不能直接外推到移动、全身或灵巧手。"
---

# 事件敏感的任务进度记忆

用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。
