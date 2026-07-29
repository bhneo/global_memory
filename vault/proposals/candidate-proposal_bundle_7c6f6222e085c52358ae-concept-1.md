---
id: "concept_648a44e346f991eab5956e55"
type: "concept"
status: "proposal"
title: "不可提升力预算下的语义恢复与快环权限分离"
created_at: "2026-07-26T12:18:55+08:00"
updated_at: "2026-07-26T12:18:55+08:00"
aliases: ["Semantic Recovery with Immutable Force Budget and Fast-Loop Authority", "FORGE-plus", "力预算恢复权限分离"]
tags: []
domains: ["contact-rich-manipulation", "robot-safety", "failure-recovery"]
confidence: "medium"
source_ids: ["source_45c4de28acb4ba36642f1594"]
relations: [{"type": "derived_from", "target_id": "source_45c4de28acb4ba36642f1594", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都让慢速代理只选择有界恢复原语并保留底层专家；FORGE-plus 进一步把不可提升的力预算和硬控制权限写成显式安全契约。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都使用快速力反馈处理接触失败；FORGE-plus 强调预算与恢复权限，既有概念强调在保留视觉语言先验时注入近期力记忆。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_45c4de28acb4ba36642f1594"
reflection_context: {"reflection_ids": ["reflection_5eb9ba718b0b143e55d0b020"], "importance": "high", "changed_belief": "此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。", "surprising": "读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。", "connections": [{"shared_mechanism": "FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。", "boundary": "连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。", "difference": "FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。"}], "open_questions": ["如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？"]}
---

# 不可提升力预算下的语义恢复与快环权限分离

接触丰富装配可让慢速语义模块依据对象身份提出每对象力预算，并在失败时依据紧凑力与接触签名从固定恢复菜单中选择动作；实际命令饱和、全局硬上限和力权限必须留在高频控制环，恢复过程不得提高原始预算。该架构仍需测量命令力与接触峰值之间的 overshoot，并以仿真限定、注入故障和代理 baseline 的边界解释结果，不能把硬 clamp 当作真实接触力保证。
