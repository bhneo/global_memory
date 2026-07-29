---
id: "concept_88f87ddc5dcf77113c5154c4"
type: "concept"
status: "working"
title: "面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽"
created_at: "2026-07-25T18:08:43+08:00"
updated_at: "2026-07-26T12:33:38+08:00"
aliases: ["Compositional Supervision and State-Conditioned Asymmetric Masking", "AC-VLA", "组合式动作学习"]
tags: []
domains: ["vla", "compositional-generalization", "robot-learning"]
confidence: "medium"
source_ids: ["source_0c017bf657a648ca70e9ae25"]
relations: [{"type": "derived_from", "target_id": "source_0c017bf657a648ca70e9ae25", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_90d52ab5e62d9847f9529875", "reason": "两者都关注视觉表征不能自动保证动作泛化；AC-VLA 提出训练期的子任务监督与状态遮蔽干预，该既有概念要求将注意力迁移和动作级成功分开评估。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_0c017bf657a648ca70e9ae25"
reflection_context: {"reflection_ids": ["reflection_4b0d86fae587571975ca7c09"], "importance": "high", "changed_belief": "此前容易将组合 OOD 失败归为缺少更多演示；本文提示，即使熟悉子技能都出现过，训练目标若保留完整轨迹关联和局部纹理捷径，模型仍可能无法按新对象—目标组合执行。", "surprising": "", "connections": [{"shared_mechanism": "两者都区分模型注意到任务相关区域与模型能否将该信息稳定转化为正确动作。", "boundary": "该连接适用于研究视觉语言动作模型在组合式操作任务中的表征与执行误差，不足以替代对真实机器人接触、控制频率或安全约束的评估。", "difference": "AC-VLA 通过分解监督和抓取阶段遮蔽改变训练信号；既有概念概括的是注意力迁移与动作成功之间的评测缺口。"}], "open_questions": []}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:38+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_28374ccd233af134718a"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_28374ccd233af134718a-concept-1.md"
origin_candidate_sha256: "765f4a17651a52733816a6681f7953a601846221e1b20b5571d7d565b26a5d55"
origin_cognitive_artifact_sha256: "d5db9ed65bb828213bb502386e14f4d8b86022e452da0964f4f87844c36a8354"
memory_schema_version: 2
last_consolidation_id: "consolidation_56aba085df9e1bb41a968b74"
---

# 面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽

AC-VLA 针对视觉语言动作模型在未见子任务组合中的轨迹过拟合和腕部视角感知捷径，将复杂指令和对应本体感觉轨迹对齐为稠密子任务监督，并与完整演示混合训练；同时在闭爪阶段按状态抑制腕部视角，以迫使模型更多利用全局空间语义。该方法在论文所述 π0.5 与 LIBERO 设置中报告组合 OOD 改善，但其可迁移性仍需在不同骨干、传感器和真实任务中独立验证。
