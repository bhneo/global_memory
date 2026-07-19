---
id: "concept_d7111f304971448401a57f3b"
type: "concept"
status: "proposal"
title: "冻结技能库与轻量路由适应"
created_at: "2026-07-19T17:16:36+08:00"
updated_at: "2026-07-19T22:43:13+08:00"
aliases: ["Frozen Skill Library with Lightweight Routing", "无监督技能挖掘", "Unsupervised Skill Mining", "SkillPlug"]
tags: []
domains: ["embodied-ai", "robot-learning", "skill-learning"]
confidence: "medium"
source_ids: ["source_d83bb2c45bcaf70906e9ac96"]
relations: [{"type": "derived_from", "target_id": "source_d83bb2c45bcaf70906e9ac96", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都建立可复用技能中间层，但分别强调数据驱动技能先验与显式类型、验证和恢复边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都建立可复用技能中间层，但分别强调数据驱动技能先验与显式类型、验证和恢复边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_d83bb2c45bcaf70906e9ac96"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_38154c8ff43c2bbbd3d979b5"], "importance": "high", "changed_belief": "此前更强调由语言或类型系统显式编译技能；该材料表明可复用中间层也可以从行为数据中学习，并把新任务适应限制在路由与执行接口。", "surprising": "技能库被冻结后仍可通过少量示范适应未见任务，说明可迁移性可能更多来自技能表示的分离与路由，而非持续改写整个策略。", "connections": [{"shared_mechanism": "都把端到端控制拆成可复用技能单元与面向任务的组合或路由层", "boundary": "连接只涉及技能复用结构，不假设无监督技能天然具有可读类型、前置条件或后置条件", "difference": "SkillPlug 的技能是从轨迹学习的连续隐变量先验，类型化技能图是显式、可检查并带恢复语义的符号控制结构"}], "open_questions": ["如何把无监督技能的激活区域转化为可验证的前置条件、后置条件和失效信号？"]}
proposed_status: "working"
---

# 冻结技能库与轻量路由适应

从多任务示范中学习紧凑、可复用且尽量非冗余的技能库，在迁移时冻结技能表示，只更新轻量路由器和动作头，以减少新任务少样本适应所需的参数与数据。
