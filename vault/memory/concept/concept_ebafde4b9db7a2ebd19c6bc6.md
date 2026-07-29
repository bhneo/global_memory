---
id: "concept_ebafde4b9db7a2ebd19c6bc6"
type: "concept"
status: "working"
title: "以休眠锚点和意图激活驱动的即时场景图生长"
created_at: "2026-07-25T18:08:58+08:00"
updated_at: "2026-07-26T12:33:48+08:00"
aliases: ["Just-In-Time Scene Graph Growth", "JITOMA", "即时按需场景图增长"]
tags: []
domains: ["scene-graphs", "robot-memory", "long-horizon-robotics"]
confidence: "medium"
source_ids: ["source_e8650c5afb7548268f649fb8"]
relations: [{"type": "derived_from", "target_id": "source_e8650c5afb7548268f649fb8", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都用结构化图承载长时程机器人任务；JITOMA 按意图选择何时增长环境子图，而该既有概念用类型、检查点和恢复语义组织可执行技能图。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_e8650c5afb7548268f649fb8"
reflection_context: {"reflection_ids": ["reflection_96809e9d9bffed57b211681f"], "importance": "high", "changed_belief": "此前可能把场景图的任务相关性理解为构建完成后的查询或筛选问题；本文使我更重视资源分配时序本身，即哪些信息应只保留可唤醒索引，哪些信息值得在尚无任务需求时立即语义化。", "surprising": "", "connections": [{"shared_mechanism": "两者都要求把机器人内部结构组织成可按任务激活、且能保留验证边界的局部图。", "boundary": "该连接适用于长时程机器人在有限计算预算下维护结构化环境或技能状态的设计讨论，不证明 JITOMA 已在所有硬件和场景中带来端到端执行收益。", "difference": "JITOMA 管理的是场景观察到 3D 子图的感知与描述成本；既有技能图概念管理的是任务原语、检查点和恢复语义。"}], "open_questions": []}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:48+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_76c6bfb139fbf9a53151"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_76c6bfb139fbf9a53151-concept-1.md"
origin_candidate_sha256: "6b7b9a52cdaafaf397e7826a19d56fbc3d864939325ed9ebb058f8509a011b55"
origin_cognitive_artifact_sha256: "d5db9ed65bb828213bb502386e14f4d8b86022e452da0964f4f87844c36a8354"
memory_schema_version: 2
last_consolidation_id: "consolidation_7fc88ee7c1c53df74942abc9"
---

# 以休眠锚点和意图激活驱动的即时场景图生长

JITOMA 不在进入环境时为全部观测建立高成本的稠密三维语义图，而是先从连续观测维护低成本全局休眠锚点；当任务查询出现时，系统解析机器人意图，唤醒相关局部锚点，并只在该子图内执行节点描述、功能推断等高成本操作。该设计旨在减少长期任务切换中的活动图规模、描述延迟和无关语义噪声，其收益受任务热图质量、锚点覆盖和遗漏关键细节风险约束。
