---
id: "concept_vla_action_cache_refinement"
type: "concept"
status: "proposal"
title: "VLA 动作缓存与上下文复用"
created_at: "2026-07-19T03:02:11+08:00"
updated_at: "2026-07-19T03:37:56+08:00"
aliases: ["VLA action caching and refinement", "ActionCache"]
tags: []
domains: ["embodied-ai", "vla", "inference-efficiency"]
confidence: "medium"
source_ids: ["source_291d6174cf92660287138f47"]
relations: [{"type": "derived_from", "target_id": "source_291d6174cf92660287138f47", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它在不改变通用 VLA 主干的情况下优化连续动作头的实时执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都面向真实部署的时延与闭环执行，但缓存复用不等同于未来动力学预测。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_291d6174cf92660287138f47"
change_type: "metadata_only"
proposed_status: "working"
---

# VLA 动作缓存与上下文复用

为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。
