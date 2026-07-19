---
id: "concept_portable_embodied_inference_runtime"
type: "concept"
status: "working"
title: "可移植具身推理运行时"
created_at: "2026-07-19T12:17:50+08:00"
updated_at: "2026-07-19T12:20:19+08:00"
aliases: ["portable embodied inference runtime", "embodied AI inference runtime", "multi-rate embodied runtime"]
tags: []
domains: ["embodied-ai", "robotics", "inference-runtime", "edge-deployment"]
confidence: "medium"
source_ids: ["source_c46b1e0305ec5c9adba634f1"]
relations: [{"type": "derived_from", "target_id": "source_c46b1e0305ec5c9adba634f1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "part_of", "target_id": "concept_end_to_end_embodied_reproducibility", "reason": "可复现具身全栈必须包含从检查点到异构边缘设备闭环执行的明确运行时边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "Embodied.cpp 将 VLA 与 WAM 的共享执行路径放入稳定核心、把动作头和预测模块插件化，为双系统模型的多速率部署提供运行时结构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_c46b1e0305ec5c9adba634f1"
uncertainty: "论文给出两种 VLA 的闭环结果；WAM 证据仅是单个 Transformer block 的量化微基准，尚不是完整 WAM 闭环验证。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T12:20:19+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_05825e7660f5c3cb11c6"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_05825e7660f5c3cb11c6-concept-1.md"
origin_candidate_sha256: "490f798522d7604442ff846066c16198c3068d1c6eb980268ca009360e423e2a"
memory_schema_version: 2
last_consolidation_id: "consolidation_48dc5fcbe817827856b09cd1"
---

# 可移植具身推理运行时

面向闭环机器人控制的统一运行时契约：以多速率组件调度、低时延低抖动的 batch-1 执行、可插拔模型头与具身 I/O，把稳定推理核心和模型/机器人专属适配分离。
