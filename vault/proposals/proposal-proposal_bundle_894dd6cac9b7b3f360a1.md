---
id: "proposal_bundle_894dd6cac9b7b3f360a1"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T19:26:55+08:00"
updated_at: "2026-08-02T19:27:19+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ddd2f65020c2e556f2b93330"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_d1a2ed0c9276e5a263c88b57"
input_sha256: "add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_asymmetric_frozen_vla_harness", "target_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "base_sha256": "29099b8a9b3e65d6df98e68a1b69f26ad1143ae4459be25f9446a3477263427e", "candidate_sha256": "664a2f33947eda1830d86d7ec834f8a624ea1bcfd5a6135505a0610a7b86152c", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_894dd6cac9b7b3f360a1-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_894dd6cac9b7b3f360a1-concept-1.md", "working_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-08-02T19:27:19+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_3b93bb83f5c7407a5a03dcad", "type": "input", "title": "Building scalable AI agents with modular prompt transpilation - Google Developers Blog", "path": "vault/inputs/input-input_3b93bb83f5c7407a5a03dcad.md", "status": "active", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# Building scalable AI agents with [modular] prompt transpilation - Google Developers Blog\n\nInput Episode for `source_3521fe9ac8d8f054440ec0af`. The immutable…", "match_reason": "metadata:title"}, {"id": "concept_318dd9fc807b1f13620238ec", "type": "concept", "title": "可构建与可审计的模块化 Agent 提示", "path": "vault/memory/concept/concept_318dd9fc807b1f13620238ec.md", "status": "working", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# 可构建与可审计的模块化 Agent 提示\n\n将 Agent 提示拆为可组合的模块和参数模板，在部署前解析依赖、检查缺失变量与循环导入，并把渲染结果作为可测试、可差异比较的构建产物；Agent 对指令的建议修改仍应经代码审查和评估后发布。", "match_reason": "metadata:aliases"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…layer.\n\n## What changed\n\nEnd-to-end VLA and [modular]-agent designs differ not only in performance: fault attribution…", "match_reason": "full-text:body"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "…Generation 2.4 Warm-Starting for VLAs 3 Method 3.1 [Framework] Overview 3.2 Cache Representation an…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ddd2f65020c2e556f2b93330"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "3ee720dcf76473c8bdf3f9e55997b7137bd19c75a9d06a4fd6b68b164312a25f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_d1a2ed0c9276e5a263c88b57`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md
+++ candidate:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md
@@ -1,43 +1,20 @@
 ---
 id: "concept_asymmetric_frozen_vla_harness"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "冻结 VLA 的非对称技能编排"
 created_at: "2026-07-19T12:18:32+08:00"
-updated_at: "2026-07-28T16:31:09+08:00"
+updated_at: "2026-08-02T19:26:55+08:00"
 aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA", "physical-agent service shell", "物理 Agent 服务化外壳", "agentic infrastructure for the physical world"]
 tags: []
 domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation", "agent-infrastructure", "robot-memory"]
 confidence: "medium"
-source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54", "source_40700e61702f4b5a5765e11d"]
-relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "外壳编排和 RL 读出都保留基础 VLA，但分别吸收任务级执行反馈与标量奖励。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "外部原语重组与生成潜空间干预是两种不同适配位置，支持域与故障归因必须分别验证。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
-change_reason: "compile bundle from source_40700e61702f4b5a5765e11d"
-uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 4
-last_consolidated_at: "2026-07-28T16:31:09+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_84924618ed7bb77a5704"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_84924618ed7bb77a5704-concept-1.md"
-origin_candidate_sha256: "ca740123df7e1d552efc8343f658d1a9ead0389bf71134ba9696bb6be738e466"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_1af6fb849e2a8335a3877c89"
+source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54", "source_40700e61702f4b5a5765e11d", "source_ddd2f65020c2e556f2b93330"]
+relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "外壳编排和 RL 读出都保留基础 VLA，但分别吸收任务级执行反馈与标量奖励。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "外部原语重组与生成潜空间干预是两种不同适配位置，支持域与故障归因必须分别验证。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都在执行中验证预期后果；CheckVLA 使用动作条件检查和可部署后缀修复，ROBOBRIDGE 使用轻量成功检查、失败诊断和跨层级恢复。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_3b83de1641240159d66c23d4", "reason": "两者都把感知状态更新与控制执行置于不同节奏；ROBOBRIDGE 的单槽最新感知缓冲是一个具体实现，但不替代显式时间戳、一致性与过期状态语义。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_ddd2f65020c2e556f2b93330"
 change_type: "refine"
-reflection_context: {"reflection_ids": ["reflection_4430cc70fe95425f717c1e71", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_cd269bee56819aafec2fd5a3"], "importance": "weekly", "changed_belief": "此前容易把 VLA 后训练等同于更新策略参数；RPent 的工程路线提示，冻结 VLA 也可被上层 Agent 组织成可复用操作原语，但这类系统收益必须与底层 VLA 本身的能力分开评估。\nVLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。\n人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。", "surprising": "仓库把 Claude Code、Codex 或 API 模型作为可替换 cerebrum，并允许复用独立 VLA 与环境服务，说明其核心抽象是异构智能编排而非单一模型。\n收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。\n人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger 风格干预能够训练潜空间控制器。", "connections": [{"shared_mechanism": "与 VIA 都把基础机器人策略或控制能力封装成 Agent 可调用的界面，通过观察、规划、执行和再观察形成闭环。", "boundary": "当前 Source 是 RPent 官方 GitHub README，只能支持项目设计与安装接口；Harness VLA 的论文方法、实验和可靠性结论仍需回到 arXiv 2607.08448 核验。", "difference": "VIA 论文研究通用视觉 Agent 直接操纵工具接口；RPent 是包含记忆、VLA 服务、环境服务和可替换 cerebrum 的递归基础设施。"}, {"shared_mechanism": "与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。", "boundary": "RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。", "difference": "RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。"}, {"shared_mechanism": "与 RL Token 都把大模型保持为稳定行为先验，只训练小型中间接口。", "boundary": "FlowDAgger 限于可执行动作反演的流匹配或扩散生成策略，并依赖人类在分布偏移处提供纠正。", "difference": "FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 actor-critic；两者的信息来源和安全成本不同。"}], "open_questions": ["Harness VLA 中 memory-guided steering 的具体记忆单元、失败恢复机制和相对无记忆基线收益是什么？", "RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？", "动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？"]}
+reflection_context: {"reflection_ids": ["reflection_094021136751760eac7be536"], "importance": "high", "changed_belief": "我原先会把“规划器加策略外壳”视为一个足够的抽象；该工作表明，外壳还必须明确快速检测放在哪个时钟、诊断何时阻断执行、异步感知如何只发布最新状态，以及恢复应先局部改参数还是重做高层计划。", "surprising": "场景偏离阈值触发后，系统可以保留高层动作序列，只用最新对象状态重新生成当前及后续 primitive 参数；同时 RoboCasa 的相对增益并未消除大量零成功或退化任务，说明恢复外壳能放大已有能力但不能创造基础策略支持域之外的能力。", "connections": [{"shared_mechanism": "ROBOBRIDGE 与 concept_asymmetric_frozen_vla_harness 都把动作策略视为能力有界的局部专家，由外部编排层承担分解、验证和恢复。", "boundary": "外部编排只能利用策略、感知器与 primitive 已支持的能力；它不证明基础 VLA 得到改进，也不保证接触丰富或不可逆失败可以恢复。", "difference": "现有节点描述非对称技能与适配接口，ROBOBRIDGE 进一步给出五模块运行时、两阶段监控、异步最新状态缓冲和重试—重生成—重规划—重感知的升级顺序。"}, {"shared_mechanism": "ROBOBRIDGE 与 concept_2db7edf95d63ca80702f042e 都在执行期间比较预期结果与真实观察，并在偏离后尝试修复。", "boundary": "两者都依赖感知与检查器的校准，不能把高置信失败诊断等同于事实，也不能绕过机器人接口层的物理安全。", "difference": "CheckVLA 以动作条件后果验证和可部署后缀修复为中心；ROBOBRIDGE 先做轻量成功检查，再诊断并在多个恢复层级间选择。"}, {"shared_mechanism": "ROBOBRIDGE 与 concept_3b83de1641240159d66c23d4 都把机器人闭环中的状态更新与控制执行拆成不同节奏。", "boundary": "异步最新值缓冲减少阻塞，但不自动提供一致快照、时间戳因果性或过期状态检测。", "difference": "显式时钟节点强调并发程序的时间语义；ROBOBRIDGE 给出一个具体的单槽最新感知结果和 primitive 后场景偏离检查。"}], "open_questions": ["成功检查置信度、场景偏离阈值和恢复升级停止条件，能否从失败代价与状态不确定性中联合校准，而不是继续手工设定？"]}
 proposed_status: "working"
-change_history: [{"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "changed_fields": [], "reason": "compile bundle from source_6b52a51e2b4a3be43c97c386", "trigger_source": "source_6b52a51e2b4a3be43c97c386", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。", "changed_fields": [], "reason": "compile bundle from source_cc2f2812863ca6751c223b54", "trigger_source": "source_cc2f2812863ca6751c223b54", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。\n\n## 新增来源材料\n\n- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。", "changed_fields": [], "reason": "compile bundle from source_40700e61702f4b5a5765e11d", "trigger_source": "source_40700e61702f4b5a5765e11d", "evidence_added": []}]
 ---
 
 # 冻结 VLA 的非对称技能编排
@@ -55,3 +32,7 @@
 ## 新增来源材料
 
 - `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。
+
+## 新增来源材料
+
+- `source_ddd2f65020c2e556f2b93330`：ROBOBRIDGE 为基础策略外部的编排边界补充一个控制器无关的五模块运行时：Perceptor 维护对象中心状态，Planner 生成参数化 primitive，Controller 可替换为 VLA、微调适配器或 IK，Robot Interface 吸收具身 API、坐标变换与安全约束，Monitor 则把周期性轻量成功检查与失败诊断分成两阶段。高置信失败先停止机器人，再按重试、重生成轨迹、基于最新异步感知重规划、重新感知后重规划的最小代价顺序升级；primitive 后若对象集合或三维位置超过偏离阈值，则保留高层动作序列并只刷新当前及后续 primitive 参数。该增量支持“能力有界策略加外部恢复外壳”，但不证明基础 VLA 得到提升：RoboCasa 绝对成功率仍低且存在零结果与退化任务，阈值和规则主要手工设定，遮挡、相似物体、接触丰富或不可逆失败仍可能超出恢复范围，论文也未给出定量真实机器人成功率表。
```
