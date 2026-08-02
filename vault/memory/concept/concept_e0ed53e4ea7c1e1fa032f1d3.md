---
id: "concept_e0ed53e4ea7c1e1fa032f1d3"
type: "concept"
status: "working"
title: "行为对齐中间表征桥接跨本体数据 / Behavior-aligned intermediate representations for cross-embodiment transfer"
created_at: "2026-08-02T18:22:22+08:00"
updated_at: "2026-08-02T19:55:27+08:00"
aliases: ["BARX", "behavior-aligned representations", "2D end-effector traces", "action-free cross-embodiment transfer"]
tags: []
domains: ["robotics", "vla", "cross-embodiment", "representation-learning", "imitation-learning"]
confidence: "medium"
source_ids: ["source_b8c45bfccc9646f938cb564c"]
relations: [{"type": "derived_from", "target_id": "source_b8c45bfccc9646f938cb564c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "该概念细化通用跨本体 VLA 的数据桥接机制：除共享模型外，还需选择兼具本体不变性与动作预测性的训练中间目标。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}, {"type": "related_to", "target_id": "concept_ab253cb9064bc1b550d5e973", "reason": "两者都用跨本体可共享的辅助监督桥接异构动作；BARX 强调当前行为轨迹、框或语言，既有节点强调未来世界状态预测。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "working"}]
change_reason: "compile bundle from source_b8c45bfccc9646f938cb564c"
reflection_context: {"reflection_ids": ["reflection_c8d6f6c9b73c9c3072c8d132"], "importance": "high", "changed_belief": "我原先更偏向通过统一 action tokenizer 或显式本体适配器解决跨本体迁移；该结果显示，训练时预测二维末端轨迹等行为中间量，即使推理时不再需要，也能显著改善目标动作学习。", "surprising": "网站报告二维末端执行器轨迹在边界框、语言动作描述等候选中最好，而且随着外部跨本体数据从 300 增至 1000 条，其收益继续扩大。", "connections": [{"shared_mechanism": "BARX 与 concept_generalist_cross_embodiment_vla 都通过共享表征或模型，把不同机器人本体的数据转化为目标本体可用的训练信号。", "boundary": "该连接只说明跨本体数据桥接；二维行为线索不能自动解决接触力、关节冗余、控制频率或部署接口差异。", "difference": "通用节点描述广义跨本体 VLA 框架，BARX 明确选择训练时的二维末端轨迹、框或语言动作作为中间监督并允许 action-free 数据参与。"}, {"shared_mechanism": "BARX 与 concept_ab253cb9064bc1b550d5e973 都用跨本体较稳定的辅助预测目标桥接异构动作空间。", "boundary": "两类辅助目标都不是天然可执行动作，其价值依赖目标本体数据把共享表征重新绑定到控制。", "difference": "BARX 预测当前行为轨迹、框或语言动作，既有节点预测未来世界状态；二者在时间语义和保留的物理信息上不同。"}], "open_questions": ["行为表征的本体不变性与动作充分性之间能否按任务阶段自适应权衡，而不是固定使用一种二维中间目标？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt-5.6-sol-strong-daily-v2"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt-5.6-sol-strong-daily-v2"
consolidation_count: 1
last_consolidated_at: "2026-08-02T19:55:27+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_2f32d1facf0de6ddeaf5"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_2f32d1facf0de6ddeaf5-concept-1.md"
origin_candidate_sha256: "4ecb50aaa9b9928029833b13d32c728711c5b7c6113c3b443fb4e9e94c7d656d"
origin_cognitive_artifact_sha256: "b03e5f1947ccaed1e1b3adc09c3ecb192fee63304f21a4aad4f0b8380edd730f"
memory_schema_version: 2
last_consolidation_id: "consolidation_4fb05846d1d0f10269564fc4"
---

# 行为对齐中间表征桥接跨本体数据 / Behavior-aligned intermediate representations for cross-embodiment transfer

跨本体数据不必先统一为同一动作空间；训练时可先从观测预测在不同机器人间更稳定、又对控制有预测力的行为中间量，例如二维末端执行器轨迹、目标边界框或语言动作，再由该表征生成目标本体动作。中间表征只承担训练监督，推理时无需外部提供，因此也能利用缺少目标动作标签的数据。二维末端轨迹在该工作中表现最好且收益随额外跨本体数据增大，但它可能遗漏接触力、关节冗余和三维动态；表示的不变性与动作充分性需按任务验证。
