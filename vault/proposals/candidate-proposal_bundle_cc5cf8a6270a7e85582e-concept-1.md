---
id: "concept_705dff5d5d3ebdcb87f1564f"
type: "concept"
status: "proposal"
title: "形态可重构机器人的跨本体控制边界"
created_at: "2026-07-21T18:08:44+08:00"
updated_at: "2026-07-21T18:08:44+08:00"
aliases: ["Morphology-Reconfigurable Robot Cross-Embodiment Control Boundary", "Handroid", "形态可重构跨本体控制"]
tags: []
domains: ["embodied-ai", "dexterous-manipulation", "humanoid-robotics"]
confidence: "medium"
source_ids: ["source_adcddc61e96d32f765d29c90"]
relations: [{"type": "derived_from", "target_id": "source_adcddc61e96d32f765d29c90", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_end_to_end_embodied_reproducibility", "reason": "二者均把硬件、控制和部署视为能力声明的一部分；前者聚焦形态切换带来的接口变化，后者强调完整可复现边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_adcddc61e96d32f765d29c90"
reflection_context: {"reflection_ids": ["reflection_b36ae3f4f0dfb6a2942e94ab"], "importance": "high", "changed_belief": "此前把手部灵巧性和人形移动操作当作独立平台问题；该平台表明可复用关节模块可以形成共同实验边界，但重构后仍会改变自由度的功能分配和控制目标。", "surprising": "", "connections": [{"shared_mechanism": "两者都要求在明确本体和控制接口的条件下验证端到端具身能力。", "boundary": "连接不表示一个可重构硬件平台已经证明通用跨形态策略迁移。", "difference": "Handroid在物理模块层重构手与人形；端到端具身系统可复现性覆盖从机械设计到训练和部署的完整工程发布边界。"}], "open_questions": ["哪些表示或控制模块能够在形态切换时复用，哪些必须因接触几何、可达性和稳定性约束而重新训练？"]}
---

# 形态可重构机器人的跨本体控制边界

将同一组可重用机电关节模块配置为灵巧手或人形身体，并在各形态下采用相应遥操作、抓取、在手操作、步态或全身控制接口的实验平台；共享硬件不消除由接触几何、任务角色和稳定性约束导致的控制差异。
