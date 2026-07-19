---
id: "concept_adaptive_interleaved_multimodal_planning"
type: "concept"
status: "proposal"
title: "自适应交错多模态规划"
created_at: "2026-07-19T12:18:13+08:00"
updated_at: "2026-07-19T12:18:13+08:00"
aliases: ["adaptive interleaved vision-language planning", "adaptive multimodal planning", "APIVOT"]
tags: []
domains: ["embodied-ai", "robot-planning", "multimodal-reasoning", "long-horizon"]
confidence: "medium"
source_ids: ["source_4ac7cf9f4fce43551683a04b"]
relations: [{"type": "derived_from", "target_id": "source_4ac7cf9f4fce43551683a04b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都区分低频语义结构与几何/动作执行；APIVOT 在单个规划轨迹内交错模态，DSWAM 则在规划器与 WAM 执行器之间分工。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "tension_internal_reasoning_external_skills", "reason": "APIVOT 把几何验证内化为模型的视觉思维，明确落在该 tension 的内部推理一侧，并保留与外部验证式技能图比较的研究边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_4ac7cf9f4fce43551683a04b"
uncertainty: "证据来自 KitchenWorlds 仿真；OOD 物体更密集时下降较大，真实几何与外观泛化尚未验证。"
---

# 自适应交错多模态规划

长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。
