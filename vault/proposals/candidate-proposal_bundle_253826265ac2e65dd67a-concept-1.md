---
id: "concept_c37ccf2640da63192432d5d5"
type: "concept"
status: "proposal"
title: "VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation"
created_at: "2026-07-27T18:19:43+08:00"
updated_at: "2026-07-27T18:19:43+08:00"
aliases: ["FM-VLA", "force-based memory VLA", "力历史记忆 VLA"]
tags: []
domains: ["robotics", "vision-language-action", "force-sensing"]
confidence: "medium"
source_ids: ["source_1ee2c3fae53a9d05689cd143"]
relations: [{"type": "derived_from", "target_id": "source_1ee2c3fae53a9d05689cd143", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_1ee2c3fae53a9d05689cd143"
reflection_context: {"reflection_ids": ["reflection_bd1bc1b00ef5304ee9d29e9c"], "importance": "high", "changed_belief": "我会把力传感视为接触事件进度的专用时序记忆，而不把它当成对视觉记忆或一般 VLA 长时推理的无条件替代。", "surprising": "", "connections": [{"shared_mechanism": "两者都以额外时序表征弥补单帧 VLA 的 Markov 假设。", "boundary": "本文限于可获得的 wrench 信号、VAE 压缩、三个记忆依赖任务和论文评测。", "difference": "视觉记忆存储图像帧且可能模糊昂贵；本文将接触/重复事件编码为紧凑 force token。"}], "open_questions": ["传感漂移、不同末端执行器和新接触材料下，force memory 的后验事件语义如何校准？"]}
---

# VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation

在接触丰富、视觉事件含糊的非 Markov 操作中，可将力/力矩历史经预训练 VAE 压缩为 force-memory tokens，并连同短状态历史条件化 VLA 的 action expert，以保留接触事件和重复进度。该方法依赖可靠 wrench 传感、压缩器训练及论文任务，不保证替代视觉记忆或泛化到任意接触分布。
