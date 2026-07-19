---
id: "architecture_simple_simulation_policy_loop"
type: "architecture"
status: "proposal"
title: "SIMPLE 仿真策略学习与评测环境"
created_at: "2026-07-19T02:51:33+08:00"
updated_at: "2026-07-19T02:51:33+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "simulation", "vla", "humanoid"]
confidence: "medium"
source_ids: ["source_d75524a9040845cdc76db35c"]
relations: [{"type": "derived_from", "target_id": "source_d75524a9040845cdc76db35c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "该环境提供将异构数据训练配方落到仿真数据生成、策略微调和评测的工程载体。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_sim_to_real_scene_infrastructure", "reason": "SIMPLE 使用大规模场景和任务进行策略学习与仿真评测，属于 Sim-to-Real 场景基础设施。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
change_reason: "compile bundle from source_d75524a9040845cdc76db35c"
uncertainty: "仓库页面证明其功能范围，但不能单独证明仿真成绩能预测真实机器人表现。"
---

# SIMPLE 仿真策略学习与评测环境

SIMPLE 是面向具身策略的数据生成、微调和仿真评测环境，覆盖多种机器人、场景资产和人形全身移动操作任务，并集成多类 VLA 与 World Action Model。
