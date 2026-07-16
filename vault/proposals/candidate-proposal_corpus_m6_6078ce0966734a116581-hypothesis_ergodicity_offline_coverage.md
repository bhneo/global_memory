---
id: "hypothesis_ergodicity_offline_coverage"
type: "hypothesis"
status: "proposal"
title: "遍历性指标可能预测离线数据对部署轨迹的覆盖"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "low"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "depends_on", "target_id": "concept_ergodicity", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_offline_coverage_deployment", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
change_reason: "M6 controlled corpus distillation; requires human review"
---

# 遍历性指标可能预测离线数据对部署轨迹的覆盖

若任务具有强路径依赖和不可逆失败，群体分布覆盖可能高估单个 Agent 的时间轨迹覆盖；需要部署日志验证。
