---
id: "concept_bfba032a868e0f7e1bcbe1d8"
type: "concept"
status: "working"
title: "接触关键段的数据聚焦学习"
created_at: "2026-07-22T18:11:50+08:00"
updated_at: "2026-07-26T12:33:45+08:00"
aliases: ["Data and Learning Where it Matters for Contact-Rich Manipulation", "Contact-Critical Data Focusing", "接触关键段学习"]
tags: []
domains: ["contact-rich-manipulation", "robot-learning"]
confidence: "medium"
source_ids: ["source_42e52a18cc082f3af087d574"]
relations: [{"type": "derived_from", "target_id": "source_42e52a18cc082f3af087d574", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "两者都将实机执行数据视为受边界约束的反馈；前者规定数据应集中在哪个任务阶段。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_42e52a18cc082f3af087d574"
reflection_context: {"reflection_ids": ["reflection_100e9d85ab1ae858496415ca"], "importance": "high", "changed_belief": "不应把端到端数据规模视作所有阶段同样受益；接触状态转换可能是需要高密度数据的局部瓶颈。", "surprising": "作者在四项实机任务中报告以 2–2.5 小时自主数据获得较高成功率，但这一结果受其任务、自动采集方案和离线 RL 设置约束。", "connections": [], "open_questions": ["关键接触段在未建模的新任务中能否可靠识别，而不遗漏决定成功的过渡状态？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:45+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_f2f284ebec42eb596d26"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_f2f284ebec42eb596d26-concept-1.md"
origin_candidate_sha256: "c888b084b8bc6b3657551d83ee169c235a68a48001802937e3768a0f19fb439c"
memory_schema_version: 2
last_consolidation_id: "consolidation_539467aa3e9534cbc68d2aed"
---

# 接触关键段的数据聚焦学习

在接触丰富操作中，用规划执行较简单的自由空间运动，并将自主数据采集与离线深度强化学习集中于决定接触成败的关键阶段。该设计的收益依赖于关键段划分、任务分布与采集系统，不能外推为所有操作任务都只需少量数据。
