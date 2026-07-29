---
id: "concept_67c66e870e29ca11e24eaa5f"
type: "concept"
status: "working"
title: "以语言选择三维抓取种子的多本体抓取分解"
created_at: "2026-07-24T18:05:50+08:00"
updated_at: "2026-07-24T18:05:50+08:00"
aliases: ["Language-Guided Seeded Grasping", "SeededGrasp", "语言引导三维抓取种子"]
tags: []
domains: ["robot-grasping", "vla", "cross-embodiment"]
confidence: "medium"
source_ids: ["source_7efe67e4901341dddfe120ff"]
relations: [{"type": "derived_from", "target_id": "source_7efe67e4901341dddfe120ff", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都以共享语义接口服务多本体行为；本概念将共享部分具体限制为 seed-point 定位，并把抓取姿态保留给本体相关生成器。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_7efe67e4901341dddfe120ff"
reflection_context: {"reflection_ids": ["reflection_7398559837f1304988c5f5a7"], "importance": "high", "changed_belief": "语言引导抓取不必让 VLM 端到端输出抓取姿态；在杂乱场景中，让它指出目标对象或功能部位可把高层意图与低层接触可行性分给不同模块。", "surprising": "", "connections": [{"shared_mechanism": "两者都把跨本体复用建立在共享的高层表示与本体特定控制解码之间。", "boundary": "该连接适用于存在可定位目标区域的抓取任务，不说明单个 seed point 足以表达所有接触序列或灵巧手约束。", "difference": "SeededGrasp 使用显式三维 seed point 作为条件；既有跨本体 VLA 概念描述的是更一般的统一输入输出策略接口。"}], "open_questions": []}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "working-ingestion-v1"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 0
last_consolidated_at: null
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_16a3af460cb0ac5aa877"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_16a3af460cb0ac5aa877-concept-1.md"
origin_candidate_sha256: "85e5f18aed9035e9057d7677eb8f5baff3bc92207f1d6fde610cb14680427cd9"
memory_schema_version: 2
---

# 以语言选择三维抓取种子的多本体抓取分解

在杂乱场景的语言引导抓取中，VLM 可先从场景点云选择表征目标对象或功能部位的 seed point，再以该点为条件由轻量抓取生成模型预测本体相关抓取姿态；这种分解把任务语义与接触几何解耦，但其跨本体收益仍取决于目标定位、点云质量和各夹爪的训练覆盖。
