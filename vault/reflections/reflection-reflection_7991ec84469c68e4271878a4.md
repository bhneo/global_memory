---
id: "reflection_7991ec84469c68e4271878a4"
type: "reflection"
status: "active"
title: "X-NavDP：用同状态相对价值稳定扩散导航后训练"
created_at: "2026-08-02T18:22:02+08:00"
updated_at: "2026-08-02T18:22:02+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "navigation", "diffusion-policy", "reinforcement-learning", "cross-embodiment"]
confidence: "high"
source_ids: ["source_bdb17eb4583ec8af52f28dfb"]
relations: []
target_ids: ["input_2d985fe9bd26ad1f4cec0cfb", "source_bdb17eb4583ec8af52f28dfb"]
input_id: "input_2d985fe9bd26ad1f4cec0cfb"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "X-NavDP 把连续扩散策略的探索与价值学习都约束在预训练策略附近，并用同一状态内的候选相对排序代替跨状态的绝对 Q 尺度。这使低回报困难状态也能提供训练信号，是跨本体导航在线 RL 的可复用稳定化结构。"
what_changed: "我原先把候选动作 Q 值重加权理解为全局优势过滤；该方法显示，在不同状态回报尺度差异大时，应先在同状态候选组内归一化，避免简单状态垄断梯度。"
surprising: "无目标候选并非随机噪声，而是沿带目标预测相对当前策略动作做有符号外推，从而扩大探索又保留动作流形。"
connections: [{"shared_mechanism": "X-NavDP 与 concept_generalist_cross_embodiment_vla 都把不同机器人形态的数据或策略经验汇入共享高层决策模型。", "boundary": "该连接限于高层导航策略共享；X-NavDP 仍依赖每种形态的 embodiment 条件与预训练低层控制器，不能据此推断控制接口无关。", "difference": "通用跨本体 VLA 节点描述广义数据与本体适配框架，X-NavDP 具体以 FiLM 条件化、结构化扩散候选和在线 Q 重加权处理导航。"}, {"shared_mechanism": "X-NavDP 与 concept_6a559a41722de87986c350e7 都保留预训练生成策略的行为先验，并用价值信号集中改进较小的生成接口。", "boundary": "该连接要求基础策略已在候选邻域提供可行行为；critic 排序错误或先验无覆盖时，两者都不保证安全改进。", "difference": "X-NavDP 在线更新 diffusion score matching，RLMM-Flow 冻结 flow decoder 并由 latent actor-critic 转向初始噪声。"}]
conflicts: ["组内相对 Q 排序能稳定梯度，却不能消除 critic 的系统性误估；候选都处于错误支持域时，相对最优仍可能是危险动作。"]
open_questions: ["如何在保持同状态相对归一化优点的同时，加入跨状态的风险校准，使困难状态的高相对分数不掩盖绝对安全下界？"]
possible_mechanisms: ["从当前扩散策略生成带目标与无目标的结构化候选，在同状态候选组内归一化 Q 并仅强化相对高价值样本，再以 FiLM 注入本体条件。"]
future_directions: ["在透明障碍、动态遮挡和长时记忆场景中分别评估候选生成、critic 校准与 embodiment 条件化的贡献。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# X-NavDP：用同状态相对价值稳定扩散导航后训练

## Why important

X-NavDP 把连续扩散策略的探索与价值学习都约束在预训练策略附近，并用同一状态内的候选相对排序代替跨状态的绝对 Q 尺度。这使低回报困难状态也能提供训练信号，是跨本体导航在线 RL 的可复用稳定化结构。

## What changed

我原先把候选动作 Q 值重加权理解为全局优势过滤；该方法显示，在不同状态回报尺度差异大时，应先在同状态候选组内归一化，避免简单状态垄断梯度。

## Surprising

无目标候选并非随机噪声，而是沿带目标预测相对当前策略动作做有符号外推，从而扩大探索又保留动作流形。

## Connections

- Shared mechanism: X-NavDP 与 concept_generalist_cross_embodiment_vla 都把不同机器人形态的数据或策略经验汇入共享高层决策模型。
  Boundary: 该连接限于高层导航策略共享；X-NavDP 仍依赖每种形态的 embodiment 条件与预训练低层控制器，不能据此推断控制接口无关。
  Difference: 通用跨本体 VLA 节点描述广义数据与本体适配框架，X-NavDP 具体以 FiLM 条件化、结构化扩散候选和在线 Q 重加权处理导航。
- Shared mechanism: X-NavDP 与 concept_6a559a41722de87986c350e7 都保留预训练生成策略的行为先验，并用价值信号集中改进较小的生成接口。
  Boundary: 该连接要求基础策略已在候选邻域提供可行行为；critic 排序错误或先验无覆盖时，两者都不保证安全改进。
  Difference: X-NavDP 在线更新 diffusion score matching，RLMM-Flow 冻结 flow decoder 并由 latent actor-critic 转向初始噪声。

## Conflicts

- 组内相对 Q 排序能稳定梯度，却不能消除 critic 的系统性误估；候选都处于错误支持域时，相对最优仍可能是危险动作。

## Open questions

- 如何在保持同状态相对归一化优点的同时，加入跨状态的风险校准，使困难状态的高相对分数不掩盖绝对安全下界？

## Possible mechanisms

- 从当前扩散策略生成带目标与无目标的结构化候选，在同状态候选组内归一化 Q 并仅强化相对高价值样本，再以 FiLM 注入本体条件。

## Future directions

- 在透明障碍、动态遮挡和长时记忆场景中分别评估候选生成、critic 校准与 embodiment 条件化的贡献。
