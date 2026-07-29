---
id: "concept_native_action_aligned_vla_memory"
type: "concept"
status: "proposal"
title: "动作对齐的 VLA 原生视觉记忆压缩"
created_at: "2026-07-21T17:41:17+08:00"
updated_at: "2026-07-21T17:41:17+08:00"
aliases: ["Native Action-Aligned VLA Memory Compression", "NativeMEM", "原生动作对齐记忆"]
tags: []
domains: ["embodied-ai", "vla", "agent-memory"]
confidence: "medium"
source_ids: ["source_748cef2215ddc958568e6368"]
relations: [{"type": "derived_from", "target_id": "source_748cef2215ddc958568e6368", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都冻结基础 VLA 以约束增量模块，但分别扩展历史表征与外部技能执行边界。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
change_reason: "compile bundle from source_748cef2215ddc958568e6368"
reflection_context: {"reflection_ids": ["reflection_65ee736483d758905945535d"], "importance": "high", "changed_belief": "长时视觉记忆不一定需要独立记忆模型；在该设定中，冻结策略反而构成迫使压缩分支保留动作相关信息的训练约束。", "surprising": "作者报告单 token/帧仍可在 32GB 内保留 5000 帧，并在所测任务中把模拟平均成功率由 Mem-0 的 32.4% 提至 84.0%；这是特定 π0.5、任务和复现基线下的结果。", "connections": [{"shared_mechanism": "都通过冻结基础 VLA 限定新增模块的职责。", "boundary": "这里只比较能力扩展接口，不把记忆 token 等同于高层技能编排。", "difference": "NativeMEM 把历史观测压入 VLA 原生 token；非对称技能编排在 VLA 外部管理重试、验证和运输。"}], "open_questions": ["单 token 压缩在遮挡、多对象身份交换和失败恢复中会丢失哪些不可恢复信息？"]}
---

# 动作对齐的 VLA 原生视觉记忆压缩

NativeMEM 将每个历史帧—相机视角压缩为一个与预训练 VLA token 维度兼容的记忆 token；第一阶段冻结 VLA，仅以原动作预测损失训练由视觉编码器初始化的 memory tokenizer，第二阶段缓存 token 并微调策略。其目标是在不增加外部记忆推理器的情况下兼顾高频更新与长时间跨度；现有证据来自作者在特定 π0.5、模拟及三项真机任务上的预印本实验。
