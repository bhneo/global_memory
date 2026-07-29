---
id: "reflection_734dd1ab9b6d593e5af1f262"
type: "reflection"
status: "active"
title: "动作令牌的顺序应对应可执行精度，而不只是压缩码位置"
created_at: "2026-07-28T18:37:08+08:00"
updated_at: "2026-07-28T18:37:08+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "vision-language-action", "action-tokenization", "adaptive-compute"]
confidence: "high"
source_ids: ["source_ba71396b5fc37637b125a89f"]
relations: []
target_ids: ["input_4fc78f50c7e1a2edc8cc6813", "source_ba71396b5fc37637b125a89f"]
input_id: "input_4fc78f50c7e1a2edc8cc6813"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "Ordered Action Tokenization 把压缩、全前缀可解码和由粗到细的有序结构同时作为策略接口要求。它使自回归策略可按预算提前停止，同时仍输出完整可执行的动作块，并让训练时的分块因果结构与推理时的块级生成匹配。"
what_changed: "动作离散化不再只是词表大小或重建误差问题；token 的顺序、任意前缀的可执行性，以及训练和推理的生成分组是否一致，都会改变策略的精度—延迟前沿。"
surprising: "把单 token OAT 在推理期事后分块并不能复现训练时采用匹配 block-causal mask 的 OATpow2；相同五次前向预算下，匹配训练的结果明显更好。"
connections: [{"shared_mechanism": "都允许根据预算改变一次策略调用所承担的计算或执行粒度。", "boundary": "现有 dynamic execution horizon 改变的是动作块实际执行的前缀长度；OAT 改变的是动作表示的逐级精化和生成调用数。", "difference": "执行时域自适应与表示精度自适应互补，但不是同一个控制量。"}]
conflicts: []
open_questions: ["能否让策略按观测不确定性动态选择 OAT 前缀或 block 数，而不是使用固定推理预算？"]
possible_mechanisms: ["nested dropout 迫使早期寄存器承担全局粗动作，后续寄存器只编码残差细节，因此任意保留前缀都能解码完整动作块。"]
future_directions: ["在更长时域、更多本体和真实机器人混合数据上验证动态 token 预算与闭环安全性的关系。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 动作令牌的顺序应对应可执行精度，而不只是压缩码位置

## Why important

Ordered Action Tokenization 把压缩、全前缀可解码和由粗到细的有序结构同时作为策略接口要求。它使自回归策略可按预算提前停止，同时仍输出完整可执行的动作块，并让训练时的分块因果结构与推理时的块级生成匹配。

## What changed

动作离散化不再只是词表大小或重建误差问题；token 的顺序、任意前缀的可执行性，以及训练和推理的生成分组是否一致，都会改变策略的精度—延迟前沿。

## Surprising

把单 token OAT 在推理期事后分块并不能复现训练时采用匹配 block-causal mask 的 OATpow2；相同五次前向预算下，匹配训练的结果明显更好。

## Connections

- Shared mechanism: 都允许根据预算改变一次策略调用所承担的计算或执行粒度。
  Boundary: 现有 dynamic execution horizon 改变的是动作块实际执行的前缀长度；OAT 改变的是动作表示的逐级精化和生成调用数。
  Difference: 执行时域自适应与表示精度自适应互补，但不是同一个控制量。

## Conflicts

None recorded.

## Open questions

- 能否让策略按观测不确定性动态选择 OAT 前缀或 block 数，而不是使用固定推理预算？

## Possible mechanisms

- nested dropout 迫使早期寄存器承担全局粗动作，后续寄存器只编码残差细节，因此任意保留前缀都能解码完整动作块。

## Future directions

- 在更长时域、更多本体和真实机器人混合数据上验证动态 token 预算与闭环安全性的关系。
