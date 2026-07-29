---
id: "concept_9d0aea7bfb560c703b51d683"
type: "concept"
status: "working"
title: "从第一视角采集到跨本体训练的具身数据工具链"
created_at: "2026-07-23T18:06:56+08:00"
updated_at: "2026-07-26T12:33:41+08:00"
aliases: ["Egocentric Data-to-Embodiment Toolchain", "Open-AoE", "第一视角具身数据工具链"]
tags: []
domains: ["embodied-data", "egocentric-learning"]
confidence: "medium"
source_ids: ["source_1f84f8abfca8810ebd19d85b"]
relations: [{"type": "derived_from", "target_id": "source_1f84f8abfca8810ebd19d85b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_embodied_data_loop", "reason": "两者都将数据价值定义为采集、处理和下游复用的闭环；本概念具体限定第一视角和跨本体转换接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_1f84f8abfca8810ebd19d85b"
reflection_context: {"reflection_ids": ["reflection_92e2e830397ee035b1ab0a8d"], "importance": "high", "changed_belief": "不能把开放视频库直接等同于机器人训练数据；可复用性需要明确的重建、标注、质量检查和跨本体转换接口。", "surprising": "", "connections": [], "open_questions": ["手机采集的手部、相机和动作标注在跨场景与跨本体重定向时，哪些误差会主导下游策略退化？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:41+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_f71684f9590125e4bea4"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_f71684f9590125e4bea4-concept-1.md"
origin_candidate_sha256: "1c5d9724cab903b3743bd113bf9799fb89ea6cefbe861b093b18374b8f9bbeb9"
memory_schema_version: 2
last_consolidation_id: "consolidation_36eef696391a51a2e3d66531"
---

# 从第一视角采集到跨本体训练的具身数据工具链

具身数据基础设施将连续第一视角采集转为可训练样本：除视频外，还通过动作时间分段、语义标注、手部重建和相机轨迹重建产生结构化信号，并提供可视化、跨本体重定向、模型格式转换和训练配方。其下游价值依赖于采集质量、标注准确性和目标本体的适配方式。
