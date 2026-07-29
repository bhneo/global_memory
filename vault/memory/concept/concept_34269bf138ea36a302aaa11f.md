---
id: "concept_34269bf138ea36a302aaa11f"
type: "concept"
status: "working"
title: "接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies"
created_at: "2026-07-27T18:15:24+08:00"
updated_at: "2026-07-27T19:06:34+08:00"
aliases: ["HCPG-Flow", "hierarchical contact-progress guidance", "接触进度候选选择"]
tags: []
domains: ["robotics", "reinforcement-learning", "flow-policies"]
confidence: "medium"
source_ids: ["source_bee998153a82cd2a92db045b"]
relations: [{"type": "derived_from", "target_id": "source_bee998153a82cd2a92db045b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_bee998153a82cd2a92db045b"
reflection_context: {"reflection_ids": ["reflection_93c4dfb77bd88bfdd67b84c8"], "importance": "high", "changed_belief": "我会把其收益归于显式对象几何、可用接触信号和任务距离，而不把解析 selector 当成对未知任务或缺少接触感知的普适替代。", "surprising": "", "connections": [{"shared_mechanism": "两者都在执行时利用非参数化的局部物理/几何结构改善生成式策略选择。", "boundary": "本文限于其 contact gate、对象中心距离、K=4 候选和 SAC-Flow 评测设置。", "difference": "critic ranking 依赖学习到的长程价值；HCPG 在接触前后使用分阶段的一阶局部进度。"}], "open_questions": ["接触判定噪声和任务进度不可由单一距离表示时，selector 如何退化或校准？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-27T19:06:34+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_644b8a6703a70f13ad7e"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_644b8a6703a70f13ad7e-concept-1.md"
origin_candidate_sha256: "ff76af3f8d7470df2a84b8703741abecab174f1c14f4fbd5b936b5629db30ef5"
origin_cognitive_artifact_sha256: "854c6e1ba595ee3115a57ecd4b72f9ebb5c24242e8ab24d406895e0c1d5883f4"
memory_schema_version: 2
last_consolidation_id: "consolidation_8d58c65959d86cc1a786509e"
---

# 接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies

对生成多个动作候选的 flow policy，可用接触阶段门控在接触前按 TCP 接近物体、接触后按物体向任务目标的一阶距离下降评分，并在候选集合内标准化后形成软动作；这在论文中保持 actor/critic 训练目标不变。方法依赖可靠接触、对象和任务几何及所用候选数量，不能替代任意任务的长期价值估计。
