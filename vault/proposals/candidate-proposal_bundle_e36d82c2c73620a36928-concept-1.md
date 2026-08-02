---
id: "concept_c5189a551eabdd0550bacd70"
type: "concept"
status: "proposal"
title: "未来触觉监督的部署一致信息隔离 / Deployment-consistent isolation of future-tactile supervision"
created_at: "2026-08-02T18:22:41+08:00"
updated_at: "2026-08-02T18:22:41+08:00"
aliases: ["TacWAM", "AGT attention", "Anchor-Guided Tri-Modal Attention", "SAF tactile encoder"]
tags: []
domains: ["robotics", "tactile-manipulation", "world-action-model", "information-isolation"]
confidence: "high"
source_ids: ["source_7fa8acc5e021363b55491e3e"]
relations: [{"type": "derived_from", "target_id": "source_7fa8acc5e021363b55491e3e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_1920583cd9c7063491d45a40", "reason": "两者都以未来触觉预测增强动作学习；TacWAM 把未来触觉作为与动作隔离的并行监督，既有概念把预测的紧凑触觉潜变量注入 action expert。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_c37ccf2640da63192432d5d5", "reason": "两者都用接触历史缓解部分可观测性；TacWAM 的触觉 latent 历史调制联合预测，既有概念的力历史压缩直接条件化动作。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "tension_bae77e2f84604668cacedd6c", "reason": "TacWAM 的掩码消融给出预测-动作对齐张力的结构性实例：未来目标泄漏可降低训练难度，却破坏部署一致性。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_7fa8acc5e021363b55491e3e"
reflection_context: {"reflection_ids": ["reflection_7c31cec2267b21f33baf67f2"], "importance": "high", "changed_belief": "我原先倾向认为更充分的跨模态注意力有利于联合世界-动作建模；该消融显示，对未来目标的访问必须按部署可得性严格隔离，信息更多并不等于监督更有效。", "surprising": "仅放松 action-to-future-tactile 的掩码就使两任务平均成功率从完整模型的 82.5% 降到 37.5%，完全双向未来信息则降到 7.5%。", "connections": [{"shared_mechanism": "TacWAM 与 concept_1920583cd9c7063491d45a40 都用未来触觉预测迫使动作模型学习接触相关的中间表征。", "boundary": "该连接只覆盖预测触觉作为训练信号；两者当前证据都不能自动推出在线力安全或开放世界接触泛化。", "difference": "TacWAM 把未来触觉作为与动作隔离的并行监督，既有概念把预测的紧凑触觉 latent token 注入 action expert。"}, {"shared_mechanism": "TacWAM 与 concept_c37ccf2640da63192432d5d5 都利用接触历史缓解单帧观测下的部分可观测性。", "boundary": "历史只在传感器时序与任务接触模式覆盖范围内有效，不能替代异常力监控或形式安全门。", "difference": "TacWAM 用触觉 latent 历史调制视觉、触觉与动作联合预测，既有概念压缩近期力历史并直接条件化动作。"}, {"shared_mechanism": "TacWAM 与 tension_bae77e2f84604668cacedd6c 都要求把预测质量和部署可用的动作对齐分开审计。", "boundary": "TacWAM 的掩码消融只证明其四项任务中的信息泄漏危害，不能独立验证所有 world-action 架构的安全性。", "difference": "既有 Tension 给出一般评估边界，TacWAM 通过 action-to-future-token 的注意力可达性给出具体结构实例。"}], "open_questions": ["能否在不暴露未来真值 token 的前提下，让动作分支读取由自身候选动作因果生成的未来触觉预测，并保持训练与部署一致？"]}
---

# 未来触觉监督的部署一致信息隔离 / Deployment-consistent isolation of future-tactile supervision

在视觉-触觉世界-动作联合训练中，未来目标应按部署可得性隔离：未来视觉、未来触觉和动作分支可以共享当前视觉与触觉锚点，但动作 token 不得读取由未来真值派生的目标 token，否则训练会利用部署时不存在的信息捷径。TacWAM 以 SAF 编码触觉外观、稠密力与形变流，并用触觉历史表征接触状态；AGT 掩码让未来视觉和未来触觉成为与动作并行的辅助目标。该未来触觉不是 action-conditioned 后果模型，解码预测也不用于在线闭环；证据目前限于一台机器人、四个任务和有限试验。
