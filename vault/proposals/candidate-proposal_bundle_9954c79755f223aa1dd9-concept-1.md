---
id: "concept_sensor_conditional_expert_routing"
type: "concept"
status: "proposal"
title: "传感器条件化专家路由"
created_at: "2026-07-19T03:03:29+08:00"
updated_at: "2026-07-19T03:25:05+08:00"
aliases: ["sensor-conditional expert routing", "CoRE-VLA"]
tags: []
domains: ["embodied-ai", "vla", "mixture-of-experts", "robustness"]
confidence: "medium"
source_ids: ["source_5d8306b5caf7371feeacbc09"]
relations: [{"type": "derived_from", "target_id": "source_5d8306b5caf7371feeacbc09", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它解决跨机器人形态和部署条件下传感器集合不一致这一通用 VLA 难题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_5d8306b5caf7371feeacbc09"
change_type: "metadata_only"
proposed_status: "working"
---

# 传感器条件化专家路由

根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。
