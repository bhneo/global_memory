---
id: "tension_world_model_eval_action"
type: "tension"
status: "proposal"
title: "更好的世界模型评价 vs 直接优化动作结果"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: [{"type": "derived_from", "target_id": "source_2d4f3a7d3525782c8ff503ee", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
change_reason: "M6 controlled corpus distillation; requires human review"
left_view: "改进世界模型评价"
right_view: "直接优化真实动作结果"
unresolved: "评价与动作收益的稳定相关性"
validation_method: "跨任务前瞻相关性与干预实验"
---

# 更好的世界模型评价 vs 直接优化动作结果

代理评价可降低真实试验成本，但评价与动作收益可能脱钩；直接优化动作又可能缺少可诊断中间信号。
