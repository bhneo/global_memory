---
id: "concept_3d739e54fe54c8a5205d2301"
type: "concept"
status: "working"
title: "多坐标系同步动作去噪"
created_at: "2026-07-20T12:33:09+08:00"
updated_at: "2026-07-20T12:33:09+08:00"
aliases: ["Synchronized multi-frame action denoising", "Mixture of Frames Policy", "MoF", "多 Frame 扩散策略"]
tags: []
domains: ["embodied-ai", "diffusion-policy", "coordinate-frames", "bimanual-manipulation"]
confidence: "high"
source_ids: ["source_4df1017326dd7cc4786f4218"]
relations: [{"type": "derived_from", "target_id": "source_4df1017326dd7cc4786f4218", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "二者都处理动作参考系差异；前者在单一本体内融合多 frame，后者在多本体间寻求统一动作接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}]
change_reason: "compile bundle from source_4df1017326dd7cc4786f4218"
reflection_context: {"reflection_ids": ["reflection_a4abd223b36c137fb9bd6ae4"], "importance": "high", "changed_belief": "此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture axis，表明动作模型难度有一部分是参数化造成的，而非任务本身不可约复杂度。", "surprising": "MoF 在部分任务上超过按整项任务选择最佳单 frame 的 oracle；路由权重随阶段变化较大的任务收益更高，论文报告两者具有正相关。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都需要把不同运动学参考系映射到统一的可执行动作接口。", "boundary": "MoF 依赖预先给定的候选 frame 和准确的 proprioceptive frame transform，当前证据集中于双臂移动操作，不能直接推出未知本体上的 frame 自动发现。", "difference": "跨本体通用 VLA 追求不同机器人共享输入输出协议；MoF 在单个机器人内部同时维护多个坐标系专家，并在同一扩散轨迹上融合噪声预测。"}], "open_questions": ["能否从数据中发现任务相关 frame，并把 frame transform 不确定性传播进扩散去噪与执行风险？"]}
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
origin_proposal_id: "proposal_bundle_8955521c41a78fff2979"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_8955521c41a78fff2979-concept-1.md"
origin_candidate_sha256: "fb18d0827371558432fc8b750d6c66b58b8615daeeec82e38effa632551509e1"
memory_schema_version: 2
---

# 多坐标系同步动作去噪

在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选 frame 与可靠变换。
