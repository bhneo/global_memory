---
id: "analogy_ergodicity_dataset_coverage"
type: "analogy"
status: "proposal"
title: "遍历性 ↔ 离线数据对部署轨迹的覆盖"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "medium"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "analogous_to", "target_id": "concept_ergodicity", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "analogous_to", "target_id": "concept_embodied_data_loop", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
change_reason: "M6 controlled corpus distillation; requires human review"
source_domain: "stochastic processes"
target_domain: "offline embodied learning"
shared_structure: "ensemble coverage may differ from temporal trajectory coverage"
where_it_breaks: "部署策略和环境会共同改变分布"
---

# 遍历性 ↔ 离线数据对部署轨迹的覆盖

共同结构是群体样本与单个主体时间经历可能不等价；失效边界是 Agent 环境分布并非严格物理遍历过程。
