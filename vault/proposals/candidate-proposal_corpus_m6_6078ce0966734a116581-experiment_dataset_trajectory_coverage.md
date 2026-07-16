---
id: "experiment_dataset_trajectory_coverage"
type: "experiment"
status: "proposal"
title: "比较数据集覆盖与真实部署轨迹覆盖"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_9d39636775b188c87d6a001f", "source_0a113baae7ce4d1ab78da1a3"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "applied_in", "target_id": "project_embodied_agent_learning_candidate", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}, {"type": "tested_by", "target_id": "hypothesis_ergodicity_offline_coverage", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
change_reason: "M6 controlled corpus distillation; requires human review"
---

# 比较数据集覆盖与真实部署轨迹覆盖

记录单个 Agent 的时间轨迹、不可逆失败与恢复，比较其与离线数据集群体覆盖指标的偏差。
