---
id: "concept_vla_action_cache_refinement"
type: "concept"
status: "working"
title: "VLA 动作缓存与上下文复用"
created_at: "2026-07-19T03:02:11+08:00"
updated_at: "2026-07-19T23:47:41+08:00"
aliases: ["VLA action caching and refinement", "ActionCache"]
tags: []
domains: ["embodied-ai", "vla", "inference-efficiency", "memory"]
confidence: "medium"
source_ids: ["source_291d6174cf92660287138f47"]
relations: [{"type": "derived_from", "target_id": "source_291d6174cf92660287138f47", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它在不改变通用 VLA 主干的情况下优化连续动作头的实时执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都面向真实部署的时延与闭环执行，但缓存复用不等同于未来动力学预测。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_291d6174cf92660287138f47"
uncertainty: "复用安全性依赖上下文相似度和 refinement 能否修正陈旧动作。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 6
last_consolidated_at: "2026-07-19T23:47:41+08:00"
last_verified_at: "2026-07-19T03:28:10+08:00"
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_1f08ff1c3ffeadc964e2"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_1f08ff1c3ffeadc964e2-concept-1.md"
origin_candidate_sha256: "c6afce9c6035a67c01e1ee3156231b1f0032c611ee2d640c18f1780d2e9a48be"
memory_schema_version: 2
last_consolidation_id: "consolidation_b4f8f27ac76fd2573675bef6"
evidence: []
change_history: [{"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["aliases"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["domains"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}]
---

# VLA 动作缓存与上下文复用

为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。
