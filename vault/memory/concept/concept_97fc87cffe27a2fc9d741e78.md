---
id: "concept_97fc87cffe27a2fc9d741e78"
type: "concept"
status: "working"
title: "Block-causal dense patch policy / 区块因果的密集视觉策略"
created_at: "2026-07-27T18:14:46+08:00"
updated_at: "2026-07-27T19:06:45+08:00"
aliases: ["Patch Policy", "block-causal attention", "密集 ViT patch 控制"]
tags: []
domains: ["robotics", "visual-representations", "control"]
confidence: "medium"
source_ids: ["source_e8651a193623cbe2b86becb0"]
relations: [{"type": "derived_from", "target_id": "source_e8651a193623cbe2b86becb0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_e8651a193623cbe2b86becb0"
reflection_context: {"reflection_ids": ["reflection_963ef2c3818ac53b780d8b29"], "importance": "high", "changed_belief": "我会把其优势限定为论文的视觉 backbone、掩码、模拟与真实任务设置，而不将相对改进泛化为任何 dense-feature 控制器。", "surprising": "", "connections": [{"shared_mechanism": "两者都保留细粒度视觉表征以支持反应式控制。", "boundary": "本文依赖预训练 ViT patch、block-causal mask 与所报告七个环境套件。", "difference": "大 VLA 借完整 VLM 获得 dense tokens；本文以最小策略扩展避开该骨干计算开销。"}], "open_questions": ["遮挡、相机变化和长期多任务上下文下，dense patch 的收益是否仍超过全局表示？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-27T19:06:45+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_11dc3ab1e457fcbc5481"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_11dc3ab1e457fcbc5481-concept-1.md"
origin_candidate_sha256: "ff45646a414652f563dadd6fdfa0cc37965018f01c36ca36a9fb6bcf81a7f487"
origin_cognitive_artifact_sha256: "854c6e1ba595ee3115a57ecd4b72f9ebb5c24242e8ab24d406895e0c1d5883f4"
memory_schema_version: 2
last_consolidation_id: "consolidation_5ade1001b519b74eb8edc9cc"
---

# Block-causal dense patch policy / 区块因果的密集视觉策略

对基于 transformer 的机器人策略，可将预训练 ViT 的密集 patch tokens 与状态共同输入，并以 block-causal attention mask 保持跨时刻动作因果性；这在论文设置中避免全局池化损失空间细节且不承担完整 VLM 骨干开销。结论依赖具体视觉表示、掩码与评测任务，未保证任意相机或控制分布下的增益。
