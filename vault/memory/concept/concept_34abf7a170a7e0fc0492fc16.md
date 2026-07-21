---
id: "concept_34abf7a170a7e0fc0492fc16"
type: "concept"
status: "working"
title: "指向式视觉导航接口"
created_at: "2026-07-19T17:17:03+08:00"
updated_at: "2026-07-19T23:49:35+08:00"
aliases: ["Pointing-Based Visual Navigation Interface", "Visual Pointing Navigation", "单目指向导航", "Robostral Navigate"]
tags: []
domains: ["embodied-ai", "visual-navigation", "robot-interface"]
confidence: "low"
source_ids: ["source_886372de22c708b28cd11e4b"]
relations: [{"type": "derived_from", "target_id": "source_886372de22c708b28cd11e4b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "claim_via_interface_first_robot_control_20260715", "reason": "二者都使用可观察视觉目标接口形成闭环，但一个是专用导航动作表示，另一个是通用 Agent 的仿真工具控制。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_886372de22c708b28cd11e4b"
reflection_context: {"reflection_ids": ["reflection_6a9092352b95c1ab440d2274"], "importance": "medium", "changed_belief": "此前容易把导航鲁棒性主要归因于更多传感器或更大模型；该材料提示视觉坐标系中的指向接口本身就是一种跨相机与跨本体归纳偏置。", "surprising": "官方页面报告单 RGB、仿真训练的 8B 模型在 R2R-CE validation unseen 达到 76.6%，但真实环境泛化叙述来自厂商页面，尚需独立论文与评测核验。", "connections": [{"shared_mechanism": "都把机器人控制转换为模型可观察、可反复修正的视觉目标接口", "boundary": "连接只覆盖视觉接口与闭环更新，不把专用导航策略等同于通用视觉 Agent 工具控制", "difference": "Robostral 直接预测图像目标点和局部位移，VIA 由通用 Agent 通过显式工具设置并执行虚拟夹爪 waypoint"}], "open_questions": ["指向与局部位移的切换条件能否用不确定性或可见性显式校准？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T23:49:35+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_e1795614dab57cbde78b"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_e1795614dab57cbde78b-concept-1.md"
origin_candidate_sha256: "9f3cf1f163198a887dc141f9e56cea83e61cf63a0a954be1d5df43530f62d959"
memory_schema_version: 2
last_consolidation_id: "consolidation_a846a5dcdd8df6febeac4a83"
---

# 指向式视觉导航接口

导航策略优先在当前 RGB 图像中预测目标位置与到达朝向，用视觉坐标减少对相机内参和世界尺度的依赖；当目标不可见时，再回退到机器人局部坐标位移。
