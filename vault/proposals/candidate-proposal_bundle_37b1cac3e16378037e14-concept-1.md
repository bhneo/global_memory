---
id: "concept_318dd9fc807b1f13620238ec"
type: "concept"
status: "proposal"
title: "可构建与可审计的模块化 Agent 提示"
created_at: "2026-07-21T18:08:53+08:00"
updated_at: "2026-07-21T18:08:53+08:00"
aliases: ["Buildable and Auditable Modular Agent Prompts", "Modular Prompt Transpilation", "模块化提示转译"]
tags: []
domains: ["ai-agents", "prompt-engineering", "software-reliability"]
confidence: "medium"
source_ids: ["source_3521fe9ac8d8f054440ec0af"]
relations: [{"type": "derived_from", "target_id": "source_3521fe9ac8d8f054440ec0af", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者用模块边界和验证降低变更爆炸半径；前者面向提示构建依赖，后者面向可执行机器人任务节点。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_3521fe9ac8d8f054440ec0af"
reflection_context: {"reflection_ids": ["reflection_05b8445267e7e49fc5bc2e46"], "importance": "high", "changed_belief": "此前模块化技能常被当作减少上下文长度的组织技巧；这里更重要的是将编译后的提示与源模块建立可重建、可测试的部署对应关系。", "surprising": "", "connections": [{"shared_mechanism": "两者都将自然语言任务组织成具有显式边界和验证步骤的模块。", "boundary": "连接仅说明编译与审查模式相似，不表示提示模块本身拥有机器人技能图的运行时类型或物理验证。", "difference": "提示转译验证依赖、变量和生成物漂移；可验证机器人技能图验证任务节点、检查点和恢复语义。"}], "open_questions": ["当按任务动态披露技能模块时，怎样验证组合后的提示仍覆盖全局安全约束且不会引入顺序依赖？"]}
---

# 可构建与可审计的模块化 Agent 提示

将 Agent 提示拆为可组合的模块和参数模板，在部署前解析依赖、检查缺失变量与循环导入，并把渲染结果作为可测试、可差异比较的构建产物；Agent 对指令的建议修改仍应经代码审查和评估后发布。
