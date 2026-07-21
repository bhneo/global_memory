---
id: "concept_ac0f0527a9c7bdba44eb37b8"
type: "concept"
status: "working"
title: "未来语义—几何变化监督的可执行 Latent Action"
created_at: "2026-07-20T12:33:32+08:00"
updated_at: "2026-07-20T12:33:32+08:00"
aliases: ["Semantic-geometric executable latent action", "WALA", "未来动力学 Latent Action"]
tags: []
domains: ["embodied-ai", "vla", "latent-action", "human-video", "future-dynamics"]
confidence: "high"
source_ids: ["source_2d5d59db178b1a20c9213220"]
relations: [{"type": "derived_from", "target_id": "source_2d5d59db178b1a20c9213220", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}]
change_reason: "compile bundle from source_2d5d59db178b1a20c9213220"
reflection_context: {"reflection_ids": ["reflection_3eda5d913d6a736393b8cd9c"], "importance": "high", "changed_belief": "此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。", "surprising": "论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。", "boundary": "WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。", "difference": "跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。"}], "open_questions": ["未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-daily-batch-b-20260720"
updated_by: "working-ingestion-v1"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-daily-batch-b-20260720"
consolidation_count: 0
last_consolidated_at: null
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_8f490857ade5069cef6e"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_8f490857ade5069cef6e-concept-1.md"
origin_candidate_sha256: "da55b7c05d3f4a7ddcfe7dde8ea7f7c4bbe7ced9c8440b293c7fb98ea6105ac6"
memory_schema_version: 2
---

# 未来语义—几何变化监督的可执行 Latent Action

从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent action target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。
