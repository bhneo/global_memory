---
id: "concept_abb38fe58cbeee09ce87a01d"
type: "concept"
status: "working"
title: "跨轨迹任务进度代理校正"
created_at: "2026-07-20T11:56:21+08:00"
updated_at: "2026-07-20T11:57:01+08:00"
aliases: ["UR-VC", "Unsupervised Robotic Value Correction", "time-derived progress correction"]
tags: []
domains: ["embodied-ai", "vla", "value-learning", "progress-estimation"]
confidence: "high"
source_ids: ["source_e326446389e083c6ba9c94c2"]
relations: [{"type": "derived_from", "target_id": "source_e326446389e083c6ba9c94c2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}]
change_reason: "compile bundle from source_e326446389e083c6ba9c94c2"
reflection_context: {"reflection_ids": ["reflection_052db872e2258b0e016c5ebf"], "importance": "weekly", "changed_belief": "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。", "surprising": "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。", "connections": [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}], "open_questions": ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
consolidation_count: 1
last_consolidated_at: "2026-07-20T11:57:01+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_96ad3d6da02d71c3c0a7"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_96ad3d6da02d71c3c0a7-concept-1.md"
origin_candidate_sha256: "4f4115e29baa8e8ece55d4d0f31ea51d688c4395bfbbd29f5b736d63216ca0ac"
memory_schema_version: 2
last_consolidation_id: "consolidation_4ed4c88b30f045e84f43619b"
---

# 跨轨迹任务进度代理校正

跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。
