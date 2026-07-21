---
id: "reflection_0db16c2a58084d442087245e"
type: "reflection"
status: "active"
title: "GR00T N1.7：跨本体迁移依赖共享动作语义而非仅共享骨干"
created_at: "2026-07-19T23:43:39+08:00"
updated_at: "2026-07-19T23:43:39+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "cross-embodiment", "action-representation"]
confidence: "medium"
source_ids: ["source_34d6513b0522739d0b25e303"]
relations: []
target_ids: ["input_0cf0fb98f9d994c03625746f", "source_34d6513b0522739d0b25e303"]
input_id: "input_0cf0fb98f9d994c03625746f"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "GR00T N1.7 把相对末端执行器动作空间与人类视频预训练放在同一迁移链路中：只有当人类与机器人数据能够共享动作变化的参照语义时，人类视觉经验才更可能转化为机器人控制先验。"
what_changed: "此前跨本体通用 VLA 主要被描述为数据混合和统一接口问题；该材料进一步表明，动作坐标系本身决定不同本体的数据能否形成一致监督。"
surprising: "官方说明把相对 EEF 表示列为跨本体表现的关键因素，而不是只把改进归因于更大的 VLM 或更多数据。"
connections: [{"shared_mechanism": "通过选择跨本体更稳定的中间监督变量，减少形态差异进入共享表示", "boundary": "相对 EEF 只适用于可映射到末端位姿变化的操作，不覆盖全身接触、灵巧手内部自由度或不可比动作空间", "difference": "GR00T 共享的是相对动作坐标，跨本体世界监督共享的是未来场景变化；前者靠近控制输出，后者靠近环境表征"}]
conflicts: ["相对动作表示降低坐标差异，但不能消除动力学、时序、接触几何和硬件能力差异"]
open_questions: ["相对 EEF、对象中心动作和未来世界表示在不同任务中各自承担多少跨本体迁移收益？"]
possible_mechanisms: ["相对位姿变化为人类手部运动与机器人末端运动提供弱共享坐标，使人类视频先验更容易进入动作学习"]
future_directions: ["在相同数据和骨干下消融绝对动作、相对 EEF、对象中心动作与世界监督通道"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# GR00T N1.7：跨本体迁移依赖共享动作语义而非仅共享骨干

## Why important

GR00T N1.7 把相对末端执行器动作空间与人类视频预训练放在同一迁移链路中：只有当人类与机器人数据能够共享动作变化的参照语义时，人类视觉经验才更可能转化为机器人控制先验。

## What changed

此前跨本体通用 VLA 主要被描述为数据混合和统一接口问题；该材料进一步表明，动作坐标系本身决定不同本体的数据能否形成一致监督。

## Surprising

官方说明把相对 EEF 表示列为跨本体表现的关键因素，而不是只把改进归因于更大的 VLM 或更多数据。

## Connections

- Shared mechanism: 通过选择跨本体更稳定的中间监督变量，减少形态差异进入共享表示
  Boundary: 相对 EEF 只适用于可映射到末端位姿变化的操作，不覆盖全身接触、灵巧手内部自由度或不可比动作空间
  Difference: GR00T 共享的是相对动作坐标，跨本体世界监督共享的是未来场景变化；前者靠近控制输出，后者靠近环境表征

## Conflicts

- 相对动作表示降低坐标差异，但不能消除动力学、时序、接触几何和硬件能力差异

## Open questions

- 相对 EEF、对象中心动作和未来世界表示在不同任务中各自承担多少跨本体迁移收益？

## Possible mechanisms

- 相对位姿变化为人类手部运动与机器人末端运动提供弱共享坐标，使人类视频先验更容易进入动作学习

## Future directions

- 在相同数据和骨干下消融绝对动作、相对 EEF、对象中心动作与世界监督通道
