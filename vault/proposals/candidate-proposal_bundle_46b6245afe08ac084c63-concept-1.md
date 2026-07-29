---
id: "concept_98b7ebb5d2382b61dd11bab3"
type: "concept"
status: "proposal"
title: "带本体掩码的语义分组跨本体动作空间"
created_at: "2026-07-23T18:07:18+08:00"
updated_at: "2026-07-23T18:07:18+08:00"
aliases: ["Embodiment-Masked Unified Action Space", "RynnBrain-VLA", "本体掩码统一动作空间"]
tags: []
domains: ["cross-embodiment", "vla", "grounding"]
confidence: "medium"
source_ids: ["source_5c29f310c66b0fb5c6cb2758"]
relations: [{"type": "derived_from", "target_id": "source_5c29f310c66b0fb5c6cb2758", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "两者都试图在异构机器人之间建立可训练的共享表示；本概念以动作维度掩码保留控制接口的不兼容边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_5c29f310c66b0fb5c6cb2758"
reflection_context: {"reflection_ids": ["reflection_a4b214ba9367da2f36ca1c06"], "importance": "high", "changed_belief": "跨本体训练不必强迫不兼容的动作空间逐维对齐；共享语义分组可以与本体特定掩码配合，但仍需要对各平台的真实控制结果单独验证。", "surprising": "", "connections": [], "open_questions": ["身体部位语义分组在接触、灵巧手和全身协调任务中何时会掩盖关键的本体差异？"]}
---

# 带本体掩码的语义分组跨本体动作空间

跨本体 VLA 可将不同机器人的动作按语义对应的身体部位分组到共享动作空间，并用本体特定掩码仅激活每台机器人可用的维度，以支持联合训练而不要求不兼容控制接口逐维对齐。该设计仍须在具体机器人、任务和控制频率上验证其迁移收益。
