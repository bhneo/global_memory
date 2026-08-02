---
id: "concept_asymmetric_frozen_vla_harness"
type: "concept"
status: "proposal"
title: "冻结 VLA 的非对称技能编排"
created_at: "2026-07-19T12:18:32+08:00"
updated_at: "2026-08-02T19:26:55+08:00"
aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA", "physical-agent service shell", "物理 Agent 服务化外壳", "agentic infrastructure for the physical world"]
tags: []
domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation", "agent-infrastructure", "robot-memory"]
confidence: "medium"
source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54", "source_40700e61702f4b5a5765e11d", "source_ddd2f65020c2e556f2b93330"]
relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "外壳编排和 RL 读出都保留基础 VLA，但分别吸收任务级执行反馈与标量奖励。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "外部原语重组与生成潜空间干预是两种不同适配位置，支持域与故障归因必须分别验证。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都在执行中验证预期后果；CheckVLA 使用动作条件检查和可部署后缀修复，ROBOBRIDGE 使用轻量成功检查、失败诊断和跨层级恢复。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_3b83de1641240159d66c23d4", "reason": "两者都把感知状态更新与控制执行置于不同节奏；ROBOBRIDGE 的单槽最新感知缓冲是一个具体实现，但不替代显式时间戳、一致性与过期状态语义。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_ddd2f65020c2e556f2b93330"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_094021136751760eac7be536"], "importance": "high", "changed_belief": "我原先会把“规划器加策略外壳”视为一个足够的抽象；该工作表明，外壳还必须明确快速检测放在哪个时钟、诊断何时阻断执行、异步感知如何只发布最新状态，以及恢复应先局部改参数还是重做高层计划。", "surprising": "场景偏离阈值触发后，系统可以保留高层动作序列，只用最新对象状态重新生成当前及后续 primitive 参数；同时 RoboCasa 的相对增益并未消除大量零成功或退化任务，说明恢复外壳能放大已有能力但不能创造基础策略支持域之外的能力。", "connections": [{"shared_mechanism": "ROBOBRIDGE 与 concept_asymmetric_frozen_vla_harness 都把动作策略视为能力有界的局部专家，由外部编排层承担分解、验证和恢复。", "boundary": "外部编排只能利用策略、感知器与 primitive 已支持的能力；它不证明基础 VLA 得到改进，也不保证接触丰富或不可逆失败可以恢复。", "difference": "现有节点描述非对称技能与适配接口，ROBOBRIDGE 进一步给出五模块运行时、两阶段监控、异步最新状态缓冲和重试—重生成—重规划—重感知的升级顺序。"}, {"shared_mechanism": "ROBOBRIDGE 与 concept_2db7edf95d63ca80702f042e 都在执行期间比较预期结果与真实观察，并在偏离后尝试修复。", "boundary": "两者都依赖感知与检查器的校准，不能把高置信失败诊断等同于事实，也不能绕过机器人接口层的物理安全。", "difference": "CheckVLA 以动作条件后果验证和可部署后缀修复为中心；ROBOBRIDGE 先做轻量成功检查，再诊断并在多个恢复层级间选择。"}, {"shared_mechanism": "ROBOBRIDGE 与 concept_3b83de1641240159d66c23d4 都把机器人闭环中的状态更新与控制执行拆成不同节奏。", "boundary": "异步最新值缓冲减少阻塞，但不自动提供一致快照、时间戳因果性或过期状态检测。", "difference": "显式时钟节点强调并发程序的时间语义；ROBOBRIDGE 给出一个具体的单槽最新感知结果和 primitive 后场景偏离检查。"}], "open_questions": ["成功检查置信度、场景偏离阈值和恢复升级停止条件，能否从失败代价与状态不确定性中联合校准，而不是继续手工设定？"]}
proposed_status: "working"
---

# 冻结 VLA 的非对称技能编排

把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。

## 新增来源材料

- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。

## 新增来源材料

- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。

## 新增来源材料

- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。

## 新增来源材料

- `source_ddd2f65020c2e556f2b93330`：ROBOBRIDGE 为基础策略外部的编排边界补充一个控制器无关的五模块运行时：Perceptor 维护对象中心状态，Planner 生成参数化 primitive，Controller 可替换为 VLA、微调适配器或 IK，Robot Interface 吸收具身 API、坐标变换与安全约束，Monitor 则把周期性轻量成功检查与失败诊断分成两阶段。高置信失败先停止机器人，再按重试、重生成轨迹、基于最新异步感知重规划、重新感知后重规划的最小代价顺序升级；primitive 后若对象集合或三维位置超过偏离阈值，则保留高层动作序列并只刷新当前及后续 primitive 参数。该增量支持“能力有界策略加外部恢复外壳”，但不证明基础 VLA 得到提升：RoboCasa 绝对成功率仍低且存在零结果与退化任务，阈值和规则主要手工设定，遮挡、相似物体、接触丰富或不可逆失败仍可能超出恢复范围，论文也未给出定量真实机器人成功率表。
