---
id: "concept_ac0f0527a9c7bdba44eb37b8"
type: "concept"
status: "working"
title: "未来语义—几何变化监督的可执行 Latent Action"
created_at: "2026-07-20T12:33:32+08:00"
updated_at: "2026-07-20T13:35:42+08:00"
aliases: ["Semantic-geometric executable latent action", "WALA", "未来动力学 Latent Action"]
tags: []
domains: ["embodied-ai", "vla", "latent-action", "human-video", "future-dynamics"]
confidence: "high"
source_ids: ["source_2d5d59db178b1a20c9213220"]
relations: [{"type": "derived_from", "target_id": "source_2d5d59db178b1a20c9213220", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_59f92bcb786f695ddcd47f7f", "reason": "WALA 用语义与深度未来 delta 学 latent action 并以机器人动作约束，FlowWAM 用光流统一视频先验与可解码动作；二者共享视频动力学中介但表征和执行锚点不同。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_2d5d59db178b1a20c9213220"
reflection_context: {"reflection_ids": ["reflection_3eda5d913d6a736393b8cd9c", "reflection_a74b334857543499d8111c64", "reflection_c3b3e3b0cbbc4d820aa25ce5"], "importance": "weekly", "changed_belief": "此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。\n此前容易把 World Action Model 的动作接口理解为数值动作或抽象 latent；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。\n人类视频规模本身不足以保证机器人迁移；若 latent space 没有机器人动作锚点，更多视频可能只增强视觉纠缠。对齐目标应明确表达物理可执行性。", "surprising": "论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。\n跨 50 个 RoboTwin 任务，预测光流误差与策略成功率呈较强负相关（论文报告 Pearson r=-0.81），说明收益至少部分跟随运动表示质量，而不只是下游解码器捷径。\n论文把 object generalization 与 fine-tuning 后的知识保持分开处理：CLAP-RF 负责连续低时延动作，Knowledge Matching 约束域适配时不要遗忘预训练语义。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。", "boundary": "WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。", "difference": "跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。"}, {"shared_mechanism": "与双系统 World Action Model 都让视频动力学模型同时支持动作生成和未来状态建模。", "boundary": "光流主要描述可见像素运动，遮挡、接触力、不可见关节和跨长时程意图并不天然可观测；论文结果也不能证明跨本体动作解码无需额外适配。", "difference": "双系统 WAM 强调快慢推理分工；FlowWAM 的核心贡献是用光流统一动作与视频模态，并由专门解码器恢复数值控制。"}, {"shared_mechanism": "与 WALA 都把无动作人类视频映射到由机器人数据约束的 latent action 空间。", "boundary": "CLAP 对新物体的已知任务泛化强于仅靠人类视频学习全新任务；人手到平行夹爪的形态差异仍造成不可消除歧义，且当前 extraction 含少量乱码。", "difference": "CLAP 用机器人 VQ 动作词表与对比对齐；WALA 用未来语义和深度变化目标及 world-model 解码监督。"}], "open_questions": ["未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？", "在遮挡、移动相机和接触丰富任务中，光流误差是否仍能稳定预测动作可执行性？", "何时应强制对齐到现有机器人动作词表，何时应保留尚不可执行但可用于未来本体的独立 latent？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-daily-batch-b-20260720"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-daily-batch-b-20260720"
consolidation_count: 1
last_consolidated_at: "2026-07-20T13:35:42+08:00"
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
change_type: "refine"
proposed_status: "working"
change_history: [{"change_type": "refine", "previous_statement": "# 未来语义—几何变化监督的可执行 Latent Action\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent action target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "new_statement": "# 未来语义—几何变化监督的可执行 Latent Action\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent action target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "changed_fields": [], "reason": "compile bundle from source_2d5d59db178b1a20c9213220", "trigger_source": "source_2d5d59db178b1a20c9213220", "evidence_added": []}]
last_consolidation_id: "consolidation_13199f416b79c3c8215ee13f"
---

# 未来语义—几何变化监督的可执行 Latent Action

从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent action target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。
