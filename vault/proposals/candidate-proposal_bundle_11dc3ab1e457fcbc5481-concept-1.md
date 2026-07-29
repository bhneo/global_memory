---
id: "concept_97fc87cffe27a2fc9d741e78"
type: "concept"
status: "proposal"
title: "Block-causal dense patch policy / 区块因果的密集视觉策略"
created_at: "2026-07-27T18:14:46+08:00"
updated_at: "2026-07-27T18:14:46+08:00"
aliases: ["Patch Policy", "block-causal attention", "密集 ViT patch 控制"]
tags: []
domains: ["robotics", "visual-representations", "control"]
confidence: "medium"
source_ids: ["source_e8651a193623cbe2b86becb0"]
relations: [{"type": "derived_from", "target_id": "source_e8651a193623cbe2b86becb0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_e8651a193623cbe2b86becb0"
reflection_context: {"reflection_ids": ["reflection_963ef2c3818ac53b780d8b29"], "importance": "high", "changed_belief": "我会把其优势限定为论文的视觉 backbone、掩码、模拟与真实任务设置，而不将相对改进泛化为任何 dense-feature 控制器。", "surprising": "", "connections": [{"shared_mechanism": "两者都保留细粒度视觉表征以支持反应式控制。", "boundary": "本文依赖预训练 ViT patch、block-causal mask 与所报告七个环境套件。", "difference": "大 VLA 借完整 VLM 获得 dense tokens；本文以最小策略扩展避开该骨干计算开销。"}], "open_questions": ["遮挡、相机变化和长期多任务上下文下，dense patch 的收益是否仍超过全局表示？"]}
---

# Block-causal dense patch policy / 区块因果的密集视觉策略

对基于 transformer 的机器人策略，可将预训练 ViT 的密集 patch tokens 与状态共同输入，并以 block-causal attention mask 保持跨时刻动作因果性；这在论文设置中避免全局池化损失空间细节且不承担完整 VLM 骨干开销。结论依赖具体视觉表示、掩码与评测任务，未保证任意相机或控制分布下的增益。
