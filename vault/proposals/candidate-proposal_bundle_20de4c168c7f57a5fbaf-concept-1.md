---
id: "concept_3b83de1641240159d66c23d4"
type: "concept"
status: "proposal"
title: "显式时钟的异步机器人闭环程序"
created_at: "2026-07-22T18:11:31+08:00"
updated_at: "2026-07-22T18:11:31+08:00"
aliases: ["Explicit-Clock Asynchronous Robot Programs", "Retriever", "异步机器人闭环程序"]
tags: []
domains: ["robot-systems", "embodied-ai"]
confidence: "medium"
source_ids: ["source_5260f9244a5030c2143c36e4"]
relations: [{"type": "derived_from", "target_id": "source_5260f9244a5030c2143c36e4", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "二者都要求把组合边界显式化；前者规定时间与数据消费，后者规定任务验证与恢复。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_5260f9244a5030c2143c36e4"
reflection_context: {"reflection_ids": ["reflection_11d7846e1ebfa021b7ef74ac"], "importance": "high", "changed_belief": "此前容易把异步执行当作部署细节；该工作表明输入消费语义和运行时钟会改变闭环行为，因而必须成为程序接口的一部分。", "surprising": "", "connections": [{"shared_mechanism": "两者都把机器人任务拆成带明确接口与验证点的可组合节点。", "boundary": "该连接只涉及运行时调度与输入同步，不证明任意技能节点的物理正确性。", "difference": "Retriever 定义多速率流和同步策略；技能图关注任务前置条件、验证与恢复语义。"}], "open_questions": ["对感知延迟或时钟漂移的最小可复现测试集应如何定义？"]}
---

# 显式时钟的异步机器人闭环程序

将感知、状态更新、规划和控制表示为有状态因果流图；每个节点声明运行时钟，每条边声明同步或缓冲策略，使多速率闭环在固定时钟、同步策略和输入轨迹下可重放与调试。该抽象不能替代对单个模块感知精度、控制稳定性或实机安全的验证。
