---
id: "architecture_simple_simulation_policy_loop"
type: "architecture"
status: "working"
title: "SIMPLE 仿真策略学习与评测环境"
created_at: "2026-07-19T02:51:33+08:00"
updated_at: "2026-07-19T03:05:25+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "simulation", "vla", "humanoid"]
confidence: "medium"
source_ids: ["source_d75524a9040845cdc76db35c"]
relations: [{"type": "derived_from", "target_id": "source_d75524a9040845cdc76db35c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "该环境提供将异构数据训练配方落到仿真数据生成、策略微调和评测的工程载体。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_sim_to_real_scene_infrastructure", "reason": "SIMPLE 使用大规模场景和任务进行策略学习与仿真评测，属于 Sim-to-Real 场景基础设施。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}]
change_reason: "compile bundle from source_d75524a9040845cdc76db35c"
uncertainty: "仓库页面证明其功能范围，但不能单独证明仿真成绩能预测真实机器人表现。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56terra-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56terra-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T03:05:25+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_05cb4178c96bcb7ee2a6"
origin_item_id: "architecture-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_05cb4178c96bcb7ee2a6-architecture-1.md"
origin_candidate_sha256: "17b5db0a1140481078beb2ef9698009ffd69263a2dda4417bacf64e5720ad87e"
memory_schema_version: 2
last_consolidation_id: "consolidation_92e7fe6ed9e1be11a8d50269"
---

# SIMPLE 仿真策略学习与评测环境

SIMPLE 是面向具身策略的数据生成、微调和仿真评测环境，覆盖多种机器人、场景资产和人形全身移动操作任务，并集成多类 VLA 与 World Action Model。
