---
id: "tension_internal_reasoning_external_skills"
type: "tension"
status: "proposal"
title: "模型内部推理 vs 外部可审计技能"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_d01f40e4896de2e186cbbe8a"]
relations: [{"type": "derived_from", "target_id": "source_d01f40e4896de2e186cbbe8a", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_skill_evolution", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
change_reason: "M6 controlled corpus distillation; requires human review"
left_view: "依赖模型内部推理"
right_view: "沉淀外部可审计技能"
unresolved: "何时下沉及如何失效"
validation_method: "按复用次数和环境漂移比较成功率与维护成本"
---

# 模型内部推理 vs 外部可审计技能

内部推理更灵活，外部技能更可复用和审计；技能固化过早可能丢失适应性。
