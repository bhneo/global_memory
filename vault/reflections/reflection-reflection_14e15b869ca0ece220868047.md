---
id: "reflection_14e15b869ca0ece220868047"
type: "reflection"
status: "active"
title: "N0-VTLA：可逆地把预测触觉通道接到既有 VLA"
created_at: "2026-08-02T18:22:59+08:00"
updated_at: "2026-08-02T18:22:59+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "vla", "tactile-manipulation", "software-interface"]
confidence: "high"
source_ids: ["source_4963925ed69479e192fb5055"]
relations: []
target_ids: ["input_781b51ea551a3fea59fa668b", "source_4963925ed69479e192fb5055"]
input_id: "input_781b51ea551a3fea59fa668b"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "官方实现仓库把未来触觉 grounding 落成一个可关闭、零初始化的窄接口：预测下一动作块的紧凑触觉 token，并只在 action expert 内融合。它强调新模态增量应保持基础策略的兼容路径，而不是要求重做大规模预训练。"
what_changed: "相比论文级机制描述，仓库把安全集成边界具体化为 tactile-off 路径的 state key、loss 与 action 等价检查，以及零初始化门控。"
surprising: "跨机器人触觉先进入固定 32 维容器，真正注入 action expert 的只有五个 latent token；接口稳定性优先于保留原始传感器维度。"
connections: [{"shared_mechanism": "官方仓库与 active stable concept_1920583cd9c7063491d45a40 描述同一 N0-VTLA 工作，均以紧凑未来触觉 latent token 约束 action expert。", "boundary": "仓库补充实现与发布边界，但不构成独立科学复制，也不应把同一工作重复建成新 Concept。", "difference": "既有节点保存论文级可复用机制，当前来源提供代码接口、checkpoint、tactile-off 等价检查和预训练未发布范围。"}, {"shared_mechanism": "N0-VTLA 的零初始化可关闭路径与 concept_2ce226e08d585158c1dfbb18 都先保持基础策略行为，再渐进吸收新增触觉信号。", "boundary": "该连接限于增量接口的兼容性原则；仓库自检不能证明跨硬件触觉语义等价，也不能替代闭环安全验证。", "difference": "N0-VTLA 以预测的下一动作块触觉 latent 条件化 action expert，既有概念以近期力残差形成快速反应接口。"}]
conflicts: ["仓库发布后训练、推理和 checkpoint，并未发布大规模预训练；实现可复现性不能替代论文结果的独立验证。"]
open_questions: ["固定 32 维跨机器人触觉容器在传感器分布、接触频率和安装方式大幅变化时，能否保持语义一致而不把适配负担转移给 encoder？"]
possible_mechanisms: ["冻结或保持基础 VLA 路径，以 DINOv2 差分触觉特征预测下一动作块的少量 latent token，经零初始化门控注入 flow action expert。"]
future_directions: ["把 tactile-off 等价性、门控幅度和跨机器人容器分布漂移纳入部署前回归测试。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# N0-VTLA：可逆地把预测触觉通道接到既有 VLA

## Why important

官方实现仓库把未来触觉 grounding 落成一个可关闭、零初始化的窄接口：预测下一动作块的紧凑触觉 token，并只在 action expert 内融合。它强调新模态增量应保持基础策略的兼容路径，而不是要求重做大规模预训练。

## What changed

相比论文级机制描述，仓库把安全集成边界具体化为 tactile-off 路径的 state key、loss 与 action 等价检查，以及零初始化门控。

## Surprising

跨机器人触觉先进入固定 32 维容器，真正注入 action expert 的只有五个 latent token；接口稳定性优先于保留原始传感器维度。

## Connections

- Shared mechanism: 官方仓库与 active stable concept_1920583cd9c7063491d45a40 描述同一 N0-VTLA 工作，均以紧凑未来触觉 latent token 约束 action expert。
  Boundary: 仓库补充实现与发布边界，但不构成独立科学复制，也不应把同一工作重复建成新 Concept。
  Difference: 既有节点保存论文级可复用机制，当前来源提供代码接口、checkpoint、tactile-off 等价检查和预训练未发布范围。
- Shared mechanism: N0-VTLA 的零初始化可关闭路径与 concept_2ce226e08d585158c1dfbb18 都先保持基础策略行为，再渐进吸收新增触觉信号。
  Boundary: 该连接限于增量接口的兼容性原则；仓库自检不能证明跨硬件触觉语义等价，也不能替代闭环安全验证。
  Difference: N0-VTLA 以预测的下一动作块触觉 latent 条件化 action expert，既有概念以近期力残差形成快速反应接口。

## Conflicts

- 仓库发布后训练、推理和 checkpoint，并未发布大规模预训练；实现可复现性不能替代论文结果的独立验证。

## Open questions

- 固定 32 维跨机器人触觉容器在传感器分布、接触频率和安装方式大幅变化时，能否保持语义一致而不把适配负担转移给 encoder？

## Possible mechanisms

- 冻结或保持基础 VLA 路径，以 DINOv2 差分触觉特征预测下一动作块的少量 latent token，经零初始化门控注入 flow action expert。

## Future directions

- 把 tactile-off 等价性、门控幅度和跨机器人容器分布漂移纳入部署前回归测试。
