---
id: "concept_end_to_end_embodied_reproducibility"
type: "concept"
status: "working"
title: "端到端具身系统可复现性"
created_at: "2026-07-19T12:17:39+08:00"
updated_at: "2026-07-19T12:20:10+08:00"
aliases: ["end-to-end embodied-system reproducibility", "embodied AI full-stack reproducibility", "E2E embodied reproducibility"]
tags: []
domains: ["embodied-ai", "robotics", "reproducibility", "vla"]
confidence: "medium"
source_ids: ["source_650f616f1e641912e73115b1"]
relations: [{"type": "derived_from", "target_id": "source_650f616f1e641912e73115b1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "supports", "target_id": "concept_embodied_data_loop", "reason": "OpenEAI-Platform 把遥操作采集、统一数据转换、两阶段训练、控制与实机评估实现为一条可复现链路，是具身数据闭环的具体系统实例。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "统一状态与动作接口及 dataset-specific adapters 处理异构数据约定，为跨本体策略提供数据侧对齐机制，但论文实机验证仍集中在其自研机械臂。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_650f616f1e641912e73115b1"
uncertainty: "论文称代码、布局和模型将在录用后发布；当前材料能支持系统设计与实验报告，不能替代对全部发布资产可复现性的独立验证。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T12:20:10+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_2f0c3e579b6d4e1b0889"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_2f0c3e579b6d4e1b0889-concept-1.md"
origin_candidate_sha256: "cdb20dafd73bbc8161c49ff6d972bbd3bc177c85f4d705503a7d19a5d6561e8b"
memory_schema_version: 2
last_consolidation_id: "consolidation_79645d0d2219533e4752f760"
---

# 端到端具身系统可复现性

把机械设计与物料清单、低层控制、数据转换、训练配方和推理部署视为同一可复现边界；只开放模型权重或微调代码不足以复现实机具身系统。
