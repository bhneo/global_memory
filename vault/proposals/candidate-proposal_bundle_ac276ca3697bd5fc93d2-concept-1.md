---
id: "concept_fdb5ce439cbb603e19af8653"
type: "concept"
status: "proposal"
title: "前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens"
created_at: "2026-07-28T18:37:16+08:00"
updated_at: "2026-07-28T18:37:16+08:00"
aliases: ["Ordered Action Tokenization", "OAT", "ordered action tokens", "有序动作令牌"]
tags: []
domains: ["robotics", "vision-language-action", "action-tokenization", "adaptive-compute"]
confidence: "high"
source_ids: ["source_ba71396b5fc37637b125a89f"]
relations: [{"type": "derived_from", "target_id": "source_ba71396b5fc37637b125a89f", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者都提供按预算改变策略粒度的接口；OAT 调节表示精度和生成调用数，动态执行时域调节实际执行的动作前缀，二者可组合但不可混同。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_ba71396b5fc37637b125a89f"
reflection_context: {"reflection_ids": ["reflection_734dd1ab9b6d593e5af1f262"], "importance": "high", "changed_belief": "动作离散化不再只是词表大小或重建误差问题；token 的顺序、任意前缀的可执行性，以及训练和推理的生成分组是否一致，都会改变策略的精度—延迟前沿。", "surprising": "把单 token OAT 在推理期事后分块并不能复现训练时采用匹配 block-causal mask 的 OATpow2；相同五次前向预算下，匹配训练的结果明显更好。", "connections": [{"shared_mechanism": "都允许根据预算改变一次策略调用所承担的计算或执行粒度。", "boundary": "现有 dynamic execution horizon 改变的是动作块实际执行的前缀长度；OAT 改变的是动作表示的逐级精化和生成调用数。", "difference": "执行时域自适应与表示精度自适应互补，但不是同一个控制量。"}], "open_questions": ["能否让策略按观测不确定性动态选择 OAT 前缀或 block 数，而不是使用固定推理预算？"]}
---

# 前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens

动作 tokenizer 同时满足高压缩、任意前缀都可解码为完整可执行动作块，以及由粗到细的有序精化。实现上以 transformer registers 和有限标量量化形成令牌，并用 nested dropout 训练各长度前缀重建整段动作，使早期令牌承载全局粗动作、后续令牌补充残差；OATsing 逐令牌生成，OATpow2 则用与训练匹配的幂次 block-causal 分组减少自回归前向调用。论文在限定操作基准中报告较强的精度—延迟前沿，但不同视觉语言骨干并非一致受益，且更长时域、更多本体与动态预算仍未充分验证。
