---
id: "concept_generalist_cross_embodiment_vla"
type: "concept"
status: "proposal"
title: "跨本体通用 VLA 的共享动作接口边界 / shared-action-interface boundary for generalist cross-embodiment VLAs"
created_at: "2026-07-19T03:01:52+08:00"
updated_at: "2026-07-28T13:02:45+08:00"
aliases: ["relative EEF cross-embodiment action", "GR00T relative action representation", "跨本体相对末端动作"]
tags: []
domains: ["embodied-ai", "vla", "cross-embodiment", "action-representation"]
confidence: "medium"
source_ids: ["source_34d6513b0522739d0b25e303"]
relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "跨本体通用策略需要处理共享表征与本体专属控制之间的对齐。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_34d6513b0522739d0b25e303"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_0db16c2a58084d442087245e"], "importance": "high", "changed_belief": "此前跨本体通用 VLA 主要被描述为数据混合和统一接口问题；该材料进一步表明，动作坐标系本身决定不同本体的数据能否形成一致监督。", "surprising": "官方说明把相对 EEF 表示列为跨本体表现的关键因素，而不是只把改进归因于更大的 VLM 或更多数据。", "connections": [{"shared_mechanism": "通过选择跨本体更稳定的中间监督变量，减少形态差异进入共享表示", "boundary": "相对 EEF 只适用于可映射到末端位姿变化的操作，不覆盖全身接触、灵巧手内部自由度或不可比动作空间", "difference": "GR00T 共享的是相对动作坐标，跨本体世界监督共享的是未来场景变化；前者靠近控制输出，后者靠近环境表征"}], "open_questions": ["相对 EEF、对象中心动作和未来世界表示在不同任务中各自承担多少跨本体迁移收益？"]}
proposed_status: "working"
---

# 跨本体通用 VLA 策略

以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。
