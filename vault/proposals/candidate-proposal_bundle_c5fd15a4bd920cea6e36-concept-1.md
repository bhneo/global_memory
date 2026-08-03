---
id: "concept_f33bda27e3f94822d9125aea"
type: "concept"
status: "proposal"
title: "连续视频进度门控的具身任务编排 / Continuous-video progress-gated embodied orchestration"
created_at: "2026-08-03T18:19:26+08:00"
updated_at: "2026-08-03T18:19:26+08:00"
aliases: ["continuous progress classification", "precision moment finding", "连续任务进度分类", "关键时刻定位", "Gemini Robotics ER 2 orchestration"]
tags: []
domains: ["robot-agents", "embodied-reasoning", "execution-monitoring", "video-understanding", "multi-robot"]
confidence: "medium"
source_ids: ["source_4ef330780a196b3bf1fdfc2c"]
relations: [{"type": "derived_from", "target_id": "source_4ef330780a196b3bf1fdfc2c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都在执行中以观察偏差触发继续或修复；CheckVLA 验证已提交动作的特征后果并重写后缀，连续视频门控估计语义进度与关键事件来切换工具。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都由高层 Agent 编排能力有界的 VLA/API；连续视频门控补充了何时 handoff 的语义时间信号，但不消除技能支持域与恢复权限边界。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_3b83de1641240159d66c23d4", "reason": "流式视频推理与动作执行构成多速率闭环；显式时钟节点提供可重放的同步语义，而进度门控定义跨时钟消费状态后的任务转换决策。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_4ef330780a196b3bf1fdfc2c"
reflection_context: {"reflection_ids": ["reflection_d519a6baa8b0ddc0fae0e793"], "importance": "high", "changed_belief": "我原先更容易把高层 embodied reasoning 看作低频 plan/verify 循环；该发布说明强调，高层模型也需要和物理执行共享连续时间，并将进度区间和关键事件帧变成动作交接门，而不是只在动作块末尾检查静态成功。", "surprising": "页面把 moment finding 的 0.96 秒平均距离和 4 倍执行速度直接与安全操作联系起来，但没有给出数据集、容差、硬件闭环或端到端 harm 协议；低延迟是必要接口，不等于安全结论。", "connections": [{"shared_mechanism": "连续视频进度门控与 concept_2db7edf95d63ca80702f042e 都在执行期间把观察与预期进展比较并触发修复。", "boundary": "两者都需要校准观测、延迟和触发阈值，不能把分类准确率或 conformal 首次干预界限当作硬件安全。", "difference": "CheckVLA 验证已提交动作的特征后果并重写可部署后缀；ER 2 的页面强调语义进度分级、关键事件定位和高层工具交接。"}, {"shared_mechanism": "ER 2 与 concept_asymmetric_frozen_vla_harness 都让高层 Agent 编排低层 VLA、导航或机器人 API。", "boundary": "编排能力仍受每个低层工具的支持域、交接状态与物理权限限制。", "difference": "现有 harness 节点聚焦能力有界技能与恢复层级；ER 2 增加连续流式视频推理和多机器人语义协作接口。"}], "open_questions": ["怎样把语义 progress bins 与 moment finding 的时间不确定性映射为可审计的 continue/stop/retry/handoff 权限，并在网络抖动、遮挡和多机器人异步状态下测量 harm？"]}
---

# 连续视频进度门控的具身任务编排 / Continuous-video progress-gated embodied orchestration

让高层具身模型在低层动作持续执行时通过双向流接收视频、音频与文本并并行规划下一步，用离散进度区间跟踪任务阶段、用 moment finding 定位完成或失败关键帧，再据此决定 continue、retry 或把控制交给下一项 VLA、导航或机器人 API。它补充了动作块末端静态成功检查，但不能替代低层安全控制：进度可视性、视频延迟、事件容差、工具支持域、交接状态和多机器人时序都需独立校准；官方产品页的内部指标缺少完整协议，不能直接视为硬件安全保证。
