---
id: "concept_30d85c442682f6afd96c3022"
type: "concept"
status: "proposal"
title: "Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs"
created_at: "2026-07-27T17:19:55+08:00"
updated_at: "2026-07-27T17:19:55+08:00"
aliases: ["Reflex 流式 VLA", "Reflex streaming VLA", "flow-matching VLA KV caching", "流式上下文分区"]
tags: []
domains: ["robotics", "vision-language-action", "systems"]
confidence: "medium"
source_ids: ["source_e67cd99ac31c7017d6f7f7c7"]
relations: [{"type": "derived_from", "target_id": "source_e67cd99ac31c7017d6f7f7c7", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_e67cd99ac31c7017d6f7f7c7"
reflection_context: {"reflection_ids": ["reflection_d8d4183ecacf40814756f4c2"], "importance": "high", "changed_belief": "我会把实时性归因于缓存有效性与异步执行的系统契约，而不把任何 flow-matching VLA 的缓存复用或论文基准速度泛化为普遍部署保证。", "surprising": "", "connections": [{"shared_mechanism": "两者都以异步执行和复用不随当前采样步变化的计算来减少控制等待。", "boundary": "本文限于其 timestep-invariance 分区、固定输入下的 attention 等价性及 LIBERO/Kinetix 报告设置。", "difference": "一般异步推理只重叠预测与执行；Reflex 还主张通过静态/滑动/动态上下文分区保持增量 KV 缓存的数学正确性。"}], "open_questions": ["感知输入变化、动作反馈和长时闭环分布漂移下，哪些区域仍可安全缓存且保持端到端控制稳定？"]}
---

# Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs

在论文所述 flow-matching VLA 中，将注意力上下文划分为不随去噪步变化的 static、滑动的 sliding 和随去噪变化的 dynamic 区域，可在固定输入下对 static/sliding 部分增量更新 KV 缓存并保持与全批 attention 等价；结合异步视觉编码与动作生成可减少阻塞。该结论依赖论文的 timestep-invariance 假设、数值稳定化和报告的基准设置，未证明任意闭环部署的稳定性。
