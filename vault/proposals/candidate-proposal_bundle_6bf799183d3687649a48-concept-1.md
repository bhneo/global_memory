---
id: "concept_149582520594364a508516c6"
type: "concept"
status: "proposal"
title: "查询介导的 VLA 动作表征塑形"
created_at: "2026-07-22T18:12:08+08:00"
updated_at: "2026-07-22T18:12:08+08:00"
aliases: ["Query-Mediated VLA Action Representation Shaping", "Action QFormer", "动作 QFormer"]
tags: []
domains: ["vla", "representation-learning"]
confidence: "medium"
source_ids: ["source_9b0d550203c4d7bd7acf8a36"]
relations: [{"type": "derived_from", "target_id": "source_9b0d550203c4d7bd7acf8a36", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_action_centric_embodied_vlm_taxonomy", "reason": "两者关注把多模态表征组织成可行动信息；本概念额外限定训练时动作梯度的接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_9b0d550203c4d7bd7acf8a36"
reflection_context: {"reflection_ids": ["reflection_63063bb66f27ff296bc9d7d2"], "importance": "high", "changed_belief": "动作接口不只是从表征读取控制量的末端模块，它还决定动作损失如何回写视觉语言通路。", "surprising": "", "connections": [{"shared_mechanism": "两者都通过显式中间接口约束高层表示如何影响动作。", "boundary": "该连接不说明接口设计可替代障碍规避、规划或真实接触验证。", "difference": "Action QFormer 是训练时查询接口；现有分类概念描述的是具身 VLM 的功能组织。"}], "open_questions": ["查询接口在接触操作和长时程重规划中是否仍能避免语言侧表征退化？"]}
---

# 查询介导的 VLA 动作表征塑形

在预训练多模态骨干和动作策略头之间插入由指令条件化查询构成的动作接口，以先重组继承表征再预测动作，并让部分动作损失经该接口传播。该机制在论文的零样本仿真到真实导航设置中改善闭环结果，但不单独解决障碍感知规划。
