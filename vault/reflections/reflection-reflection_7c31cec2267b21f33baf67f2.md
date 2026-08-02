---
id: "reflection_7c31cec2267b21f33baf67f2"
type: "reflection"
status: "active"
title: "TacWAM：未来触觉监督必须与动作预测保持部署一致的信息边界"
created_at: "2026-08-02T18:22:39+08:00"
updated_at: "2026-08-02T18:22:39+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "tactile-manipulation", "world-action-model", "information-isolation"]
confidence: "high"
source_ids: ["source_7fa8acc5e021363b55491e3e"]
relations: []
target_ids: ["input_51866e9a991605566ddb6bf4", "source_7fa8acc5e021363b55491e3e"]
input_id: "input_51866e9a991605566ddb6bf4"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "TacWAM 的关键不只是多模态预测，而是信息拓扑：未来视觉和触觉是并行训练目标，动作 token 只能访问当前视觉、触觉锚点。若动作分支看到由未来真值派生的 token，训练会获得部署时不存在的捷径，世界监督反而破坏控制。"
what_changed: "我原先倾向认为更充分的跨模态注意力有利于联合世界-动作建模；该消融显示，对未来目标的访问必须按部署可得性严格隔离，信息更多并不等于监督更有效。"
surprising: "仅放松 action-to-future-tactile 的掩码就使两任务平均成功率从完整模型的 82.5% 降到 37.5%，完全双向未来信息则降到 7.5%。"
connections: [{"shared_mechanism": "TacWAM 与 concept_1920583cd9c7063491d45a40 都用未来触觉预测迫使动作模型学习接触相关的中间表征。", "boundary": "该连接只覆盖预测触觉作为训练信号；两者当前证据都不能自动推出在线力安全或开放世界接触泛化。", "difference": "TacWAM 把未来触觉作为与动作隔离的并行监督，既有概念把预测的紧凑触觉 latent token 注入 action expert。"}, {"shared_mechanism": "TacWAM 与 concept_c37ccf2640da63192432d5d5 都利用接触历史缓解单帧观测下的部分可观测性。", "boundary": "历史只在传感器时序与任务接触模式覆盖范围内有效，不能替代异常力监控或形式安全门。", "difference": "TacWAM 用触觉 latent 历史调制视觉、触觉与动作联合预测，既有概念压缩近期力历史并直接条件化动作。"}, {"shared_mechanism": "TacWAM 与 tension_bae77e2f84604668cacedd6c 都要求把预测质量和部署可用的动作对齐分开审计。", "boundary": "TacWAM 的掩码消融只证明其四项任务中的信息泄漏危害，不能独立验证所有 world-action 架构的安全性。", "difference": "既有 Tension 给出一般评估边界，TacWAM 通过 action-to-future-token 的注意力可达性给出具体结构实例。"}]
conflicts: ["未来触觉分支改善训练表征并不等于已经学习到 action-conditioned 后果模型；TacWAM 的动作不能读取未来 tactile token，解码预测也只用于离线分析。"]
open_questions: ["能否在不暴露未来真值 token 的前提下，让动作分支读取由自身候选动作因果生成的未来触觉预测，并保持训练与部署一致？"]
possible_mechanisms: ["以 SAF 编码外观、稠密力和形变流，利用触觉历史建模接触状态，再通过 AGT 掩码让未来视觉、触觉与动作共享当前锚点但彼此隔离。"]
future_directions: ["区分并评测并行未来监督、action-conditioned tactile consequence model 和在线触觉闭环修正三种能力，避免由共同术语造成能力外推。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# TacWAM：未来触觉监督必须与动作预测保持部署一致的信息边界

## Why important

TacWAM 的关键不只是多模态预测，而是信息拓扑：未来视觉和触觉是并行训练目标，动作 token 只能访问当前视觉、触觉锚点。若动作分支看到由未来真值派生的 token，训练会获得部署时不存在的捷径，世界监督反而破坏控制。

## What changed

我原先倾向认为更充分的跨模态注意力有利于联合世界-动作建模；该消融显示，对未来目标的访问必须按部署可得性严格隔离，信息更多并不等于监督更有效。

## Surprising

仅放松 action-to-future-tactile 的掩码就使两任务平均成功率从完整模型的 82.5% 降到 37.5%，完全双向未来信息则降到 7.5%。

## Connections

- Shared mechanism: TacWAM 与 concept_1920583cd9c7063491d45a40 都用未来触觉预测迫使动作模型学习接触相关的中间表征。
  Boundary: 该连接只覆盖预测触觉作为训练信号；两者当前证据都不能自动推出在线力安全或开放世界接触泛化。
  Difference: TacWAM 把未来触觉作为与动作隔离的并行监督，既有概念把预测的紧凑触觉 latent token 注入 action expert。
- Shared mechanism: TacWAM 与 concept_c37ccf2640da63192432d5d5 都利用接触历史缓解单帧观测下的部分可观测性。
  Boundary: 历史只在传感器时序与任务接触模式覆盖范围内有效，不能替代异常力监控或形式安全门。
  Difference: TacWAM 用触觉 latent 历史调制视觉、触觉与动作联合预测，既有概念压缩近期力历史并直接条件化动作。
- Shared mechanism: TacWAM 与 tension_bae77e2f84604668cacedd6c 都要求把预测质量和部署可用的动作对齐分开审计。
  Boundary: TacWAM 的掩码消融只证明其四项任务中的信息泄漏危害，不能独立验证所有 world-action 架构的安全性。
  Difference: 既有 Tension 给出一般评估边界，TacWAM 通过 action-to-future-token 的注意力可达性给出具体结构实例。

## Conflicts

- 未来触觉分支改善训练表征并不等于已经学习到 action-conditioned 后果模型；TacWAM 的动作不能读取未来 tactile token，解码预测也只用于离线分析。

## Open questions

- 能否在不暴露未来真值 token 的前提下，让动作分支读取由自身候选动作因果生成的未来触觉预测，并保持训练与部署一致？

## Possible mechanisms

- 以 SAF 编码外观、稠密力和形变流，利用触觉历史建模接触状态，再通过 AGT 掩码让未来视觉、触觉与动作共享当前锚点但彼此隔离。

## Future directions

- 区分并评测并行未来监督、action-conditioned tactile consequence model 和在线触觉闭环修正三种能力，避免由共同术语造成能力外推。
