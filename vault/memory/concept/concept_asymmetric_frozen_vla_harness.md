---
id: "concept_asymmetric_frozen_vla_harness"
type: "concept"
status: "working"
title: "冻结 VLA 的非对称技能编排"
created_at: "2026-07-19T12:18:32+08:00"
updated_at: "2026-07-28T16:31:09+08:00"
aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA", "physical-agent service shell", "物理 Agent 服务化外壳", "agentic infrastructure for the physical world"]
tags: []
domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation", "agent-infrastructure", "robot-memory"]
confidence: "medium"
source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54", "source_40700e61702f4b5a5765e11d"]
relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "外壳编排和 RL 读出都保留基础 VLA，但分别吸收任务级执行反馈与标量奖励。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "外部原语重组与生成潜空间干预是两种不同适配位置，支持域与故障归因必须分别验证。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
change_reason: "compile bundle from source_40700e61702f4b5a5765e11d"
uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 4
last_consolidated_at: "2026-07-28T16:31:09+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_84924618ed7bb77a5704"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_84924618ed7bb77a5704-concept-1.md"
origin_candidate_sha256: "ca740123df7e1d552efc8343f658d1a9ead0389bf71134ba9696bb6be738e466"
memory_schema_version: 2
last_consolidation_id: "consolidation_1af6fb849e2a8335a3877c89"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_4430cc70fe95425f717c1e71", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_cd269bee56819aafec2fd5a3"], "importance": "weekly", "changed_belief": "此前容易把 VLA 后训练等同于更新策略参数；RPent 的工程路线提示，冻结 VLA 也可被上层 Agent 组织成可复用操作原语，但这类系统收益必须与底层 VLA 本身的能力分开评估。\nVLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。\n人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。", "surprising": "仓库把 Claude Code、Codex 或 API 模型作为可替换 cerebrum，并允许复用独立 VLA 与环境服务，说明其核心抽象是异构智能编排而非单一模型。\n收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。\n人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger 风格干预能够训练潜空间控制器。", "connections": [{"shared_mechanism": "与 VIA 都把基础机器人策略或控制能力封装成 Agent 可调用的界面，通过观察、规划、执行和再观察形成闭环。", "boundary": "当前 Source 是 RPent 官方 GitHub README，只能支持项目设计与安装接口；Harness VLA 的论文方法、实验和可靠性结论仍需回到 arXiv 2607.08448 核验。", "difference": "VIA 论文研究通用视觉 Agent 直接操纵工具接口；RPent 是包含记忆、VLA 服务、环境服务和可替换 cerebrum 的递归基础设施。"}, {"shared_mechanism": "与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。", "boundary": "RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。", "difference": "RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。"}, {"shared_mechanism": "与 RL Token 都把大模型保持为稳定行为先验，只训练小型中间接口。", "boundary": "FlowDAgger 限于可执行动作反演的流匹配或扩散生成策略，并依赖人类在分布偏移处提供纠正。", "difference": "FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 actor-critic；两者的信息来源和安全成本不同。"}], "open_questions": ["Harness VLA 中 memory-guided steering 的具体记忆单元、失败恢复机制和相对无记忆基线收益是什么？", "RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？", "动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？"]}
proposed_status: "working"
change_history: [{"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "changed_fields": [], "reason": "compile bundle from source_6b52a51e2b4a3be43c97c386", "trigger_source": "source_6b52a51e2b4a3be43c97c386", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。", "changed_fields": [], "reason": "compile bundle from source_cc2f2812863ca6751c223b54", "trigger_source": "source_cc2f2812863ca6751c223b54", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。\n\n## 新增来源材料\n\n- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。", "changed_fields": [], "reason": "compile bundle from source_40700e61702f4b5a5765e11d", "trigger_source": "source_40700e61702f4b5a5765e11d", "evidence_added": []}]
---

# 冻结 VLA 的非对称技能编排

把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。

## 新增来源材料

- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。

## 新增来源材料

- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。

## 新增来源材料

- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。
