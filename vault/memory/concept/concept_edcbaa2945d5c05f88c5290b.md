---
id: "concept_edcbaa2945d5c05f88c5290b"
type: "concept"
status: "working"
title: "阶段歧义驱动的扩散控制频率切换 / Phase-ambiguity-driven diffusion control-frequency switching"
created_at: "2026-08-02T18:56:47+08:00"
updated_at: "2026-08-02T19:55:29+08:00"
aliases: ["FA-RDP", "frequency-adaptive residual diffusion policy", "ambiguity-conditioned frequency switching", "歧义条件的多频扩散控制"]
tags: []
domains: ["robotics", "diffusion-policy", "force-control", "multi-rate-control"]
confidence: "high"
source_ids: ["source_1fa826244c5f3d4ea7f41541"]
relations: [{"type": "derived_from", "target_id": "source_1fa826244c5f3d4ea7f41541", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者都按阶段调节开环承诺；动态执行时域改变已生成动作块的执行前缀，FA-RDP 联动控制频率、预测长度和生成器。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都分离慢速语义与快速接触反馈；FA-RDP 以视觉歧义门切换视觉—力扩散采样频率，而既有节点以触觉子目标和残差层组织闭环。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}, {"type": "related_to", "target_id": "concept_34269bf138ea36a302aaa11f", "reason": "两者都显式利用接触阶段改变生成式策略执行；既有节点在候选间做几何进度选择，FA-RDP 在低频多步与高频单步生成间切换。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}]
change_reason: "compile bundle from source_1fa826244c5f3d4ea7f41541"
reflection_context: {"reflection_ids": ["reflection_1ca77990ff946c0288b7704c"], "importance": "high", "changed_belief": "我原先把高频控制主要理解为更频繁地重规划；该工作表明，频率切换还必须同步改变预测序列长度和采样器，否则高频多步扩散的计算预算会失控。", "surprising": "频率门由低频视觉 token 学习，而高频阶段每步刷新力输入并复用缓存的慢速上下文；快速反馈并不要求重算全部视觉语义。", "connections": [{"shared_mechanism": "FA-RDP 与 concept_dynamic_execution_horizon 都按任务阶段改变开环承诺长度，以平衡吞吐和反馈反应。", "boundary": "连接限于执行调度；两者都不保证基础策略支持域外的恢复或力安全。", "difference": "动态执行时域改变一个已生成动作块执行多少步，FA-RDP 同时切换 10/30 Hz、16/48 步预测和多步/单步生成器。"}, {"shared_mechanism": "FA-RDP 与 concept_multitimescale_tactile_world_model 都把慢速语义上下文和快速接触反馈分层。", "boundary": "FA-RDP 使用视觉与六维力，不能直接外推到触觉图像、长时任务分解或跨硬件触觉语义。", "difference": "既有概念以触觉子目标和残差控制组织多时间尺度，FA-RDP 以阶段歧义门切换扩散采样频率。"}], "open_questions": ["当视觉歧义在接触后重新出现，或力信号在接触前已经关键时，二阶段门应如何校准和回退？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt-5.6-sol-strong-daily-v2"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt-5.6-sol-strong-daily-v2"
consolidation_count: 1
last_consolidated_at: "2026-08-02T19:55:29+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_89c4aa8c597472793a3e"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_89c4aa8c597472793a3e-concept-1.md"
origin_candidate_sha256: "c397af42d07551a335c656a0dd198534ab0b9bea92799297b2a0ac156031f58f"
origin_cognitive_artifact_sha256: "657c678864cc62b59756149a9ec6bfc0bba843ef086c9aebe7435a73f19fcf3f"
memory_schema_version: 2
last_consolidation_id: "consolidation_55ddb78bbd4c1da8aead74d6"
---

# 阶段歧义驱动的扩散控制频率切换 / Phase-ambiguity-driven diffusion control-frequency switching

对接触操作中的扩散策略，可让任务歧义而非固定时钟决定控制模式：共享视觉—力 Transformer 以频率自适应位置编码把 10 Hz 的 16 步序列与 30 Hz 的 48 步序列对齐到同一 1.6 秒物理时域。接触前保留低频多步扩散的多模态规划；视觉门判断歧义消退后，切换到高频单步蒸馏并每步刷新力输入，同时缓存慢速视觉上下文以控制计算量。该结构不同于只改变动作块执行前缀，也不同于只在固定策略上叠加高频力补偿；其边界是门依赖视觉阶段线索并假设歧义通常随接触下降，证据目前限于单任务、单机器人和三项视觉—力任务。
