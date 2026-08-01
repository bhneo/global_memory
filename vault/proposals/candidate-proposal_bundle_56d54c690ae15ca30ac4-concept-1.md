---
id: "concept_2db7edf95d63ca80702f042e"
type: "concept"
status: "proposal"
title: "动作条件的执行期后果验证与后缀修复 / Action-conditioned execution consequence verification and suffix repair"
created_at: "2026-08-01T18:22:06+08:00"
updated_at: "2026-08-01T18:22:06+08:00"
aliases: ["CheckVLA", "action-conditioned execution-time verification", "latency-aware suffix repair", "动作后果一致性验证"]
tags: []
domains: ["robotics", "mobile-manipulation", "execution-verification", "world-models"]
confidence: "high"
source_ids: ["source_da533f75e69c23b8eec387df"]
relations: [{"type": "derived_from", "target_id": "source_da533f75e69c23b8eec387df", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者都恢复动作块执行中的反馈；动态执行时域选择何时重新查询，CheckVLA 用动作后果偏差触发并重写延迟后仍可部署的后缀。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_769f84122571858ee48f9c48", "reason": "两者都在动作执行后验证状态并触发恢复；既有节点检查共享 RGB-D 对象记录和几何谓词，CheckVLA 检查动作条件的预测—观测一致性。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_da533f75e69c23b8eec387df"
reflection_context: {"reflection_ids": ["reflection_056997ffabc04566dafb3edd"], "importance": "high", "changed_belief": "执行验证不应只问当前画面是否异常；必须问在已提交动作条件下，观察到的变化是否仍符合预期，并把报警时间与剩余可部署后缀绑定。", "surprising": "论文明确把 conformal 保证限制为 exchangeable nominal-success episodes 上的不必要首次干预概率；它不保证故障召回、修复后安全、重复干预或分布外覆盖。", "connections": [{"shared_mechanism": "都在动作块执行后用新观测决定是否继续、重规划或恢复。", "boundary": "既有持久对象状态闭环依赖角色索引 RGB-D 对象记录和几何谓词；CheckVLA 依赖已提交动作的特征后果预测、风险校准和可部署后缀。", "difference": "前者验证显式对象状态，后者验证动作—后果一致性并把阈值超量映射为修复强度。"}], "open_questions": ["如何在真实硬件、非交换部署分布和多次修复后重新校准风险，而不把首次干预保证误写成安全保证？"]}
---

# 动作条件的执行期后果验证与后缀修复 / Action-conditioned execution consequence verification and suffix repair

把已提交动作块视为对近未来观测的可检验承诺：冻结监控编码器和短跨度滚动世界模型预测已提交动作的特征后果，因果风险头聚合预测—观测残差，并用 nominal-success 轨迹上的 functional conformal threshold 控制不必要首次干预的 episode-level 概率。触发后，同一 VLA 在推理期间继续执行的动作上施加 hard prefix，只重写仍可部署的后缀；标准化阈值超量决定对旧后缀的参考保留强度，事件驱动 keyframe bank 保留已完成进度。该校准不保证故障召回、修复后安全、重复干预、分布外覆盖或硬件迁移；这些必须分别用及时召回、可修复窗口、rescue、harm 和真实闭环结果验证。
