---
id: "concept_progressive_vla_demonstration_curriculum"
type: "concept"
status: "proposal"
title: "由简到繁的 VLA 示范组织"
created_at: "2026-07-19T03:02:30+08:00"
updated_at: "2026-07-19T23:48:18+08:00"
aliases: ["simple-to-complex VLA demonstrations", "progressive demonstration curriculum"]
tags: []
domains: ["embodied-ai", "vla", "imitation-learning", "curriculum"]
confidence: "medium"
source_ids: ["source_91072aa553af99e6ab97c6cd"]
relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "它把数据闭环中的采集环节细化为具有课程结构的示范组织问题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "示范组织影响 VLA 的学习效率、训练稳定性和长时程泛化。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都分解长时程任务，但示范课程组织训练监督，类型化技能图组织部署时调用、验证与恢复。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-weekly-v2", "status": "proposal"}]
change_reason: "compile bundle from source_91072aa553af99e6ab97c6cd"
change_type: "metadata_only"
reflection_context: {"reflection_ids": ["reflection_61def8d05e0b6ddfb18b6f75"], "importance": "weekly", "changed_belief": "此前数据闭环更强调覆盖率、质量和回流速度；该材料增加了课程结构这一维度，即相同模型与近似数据规模也可能因示范顺序和组织方式产生不同结果。", "surprising": "研究声称仅改变示范组织就能改善训练稳定性与任务成功率，说明端到端完整轨迹未必是信息最有效的采集单位。", "connections": [{"shared_mechanism": "都通过阶段化结构减少策略一次性学习的组合复杂度", "boundary": "连接限于训练监督组织，不意味着示范课程等同于执行时的技能图或规划层", "difference": "由简到繁示范在数据采集阶段塑造学习分布；技能图在执行阶段显式组织可调用能力"}], "open_questions": ["课程结构带来的收益有多少来自子技能复用，有多少来自降低环境方差？"]}
proposed_status: "working"
---

# 由简到繁的 VLA 示范组织

通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。
