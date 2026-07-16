---
id: "tension_language_prior_action_control"
type: "tension"
status: "proposal"
title: "语言先验复用 vs 实时动作专用表示"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
relations: [{"type": "derived_from", "target_id": "source_f35b44d4bd383fb26ca49165", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
change_reason: "M6 controlled corpus distillation; requires human review"
left_view: "复用语言/视觉预训练先验"
right_view: "使用动作专用连续表示"
unresolved: "接口和训练信号如何分工"
validation_method: "延迟、泛化、稳定性联合消融"
---

# 语言先验复用 vs 实时动作专用表示

语言先验有助于泛化和任务理解，但连续控制需要低延迟、高带宽且具身化的动作表示。
