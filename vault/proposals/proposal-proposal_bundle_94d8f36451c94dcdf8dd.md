---
id: "proposal_bundle_94d8f36451c94dcdf8dd"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T13:11:47+08:00"
updated_at: "2026-07-28T13:11:56+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_01ed2f19e91bb0eb1ec3ee92"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-legacy-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_7d89b66ae99258c52fd33577"
input_sha256: "f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_f5d1ef9eaed1cd6bec4d4c52", "target_path": "vault/knowledge/concepts/concept_f5d1ef9eaed1cd6bec4d4c52-图式-agent-memory-的生命周期与评测闭环-lifecycle-and-evaluation-closure-for-.md", "base_sha256": null, "candidate_sha256": "ae450c5d0a7fe10cb2e9fb93eb60a5a20d0e0f61f92be5868740bfb85dd177c1", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_94d8f36451c94dcdf8dd-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_f5d1ef9eaed1cd6bec4d4c52.md", "working_at": "2026-07-28T13:11:56+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "synthesis_7084bca907043e3cba4afb7e", "type": "synthesis", "title": "Agent Memory 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界", "path": "vault/synthesis/synthesis-synthesis_7084bca907043e3cba4afb7e.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92", "source_11bc6c51fa038191e33bc9a7", "source_6ada1b3b0033883b83a3bf40", "source_6b52a51e2b4a3be43c97c386"], "snippet": "# Agent [Memory] 与物理 Agent 基础设施：可观测状态、记忆演化与冻结策略边界\n\n## Emerging patterns\n\n- 长期 Agent [Memory] 与物理 Agent 基础设施共享同一结构要求：状态必须可外化、更新必须可定位、失败必须能回到产生它的感知…", "match_reason": "metadata:title"}, {"id": "concept_dual_protocol_hri_agent_execution_boundary", "type": "concept", "title": "人机客户端与 Agent 执行的双协议边界", "path": "vault/memory/concept/concept_dual_protocol_hri_agent_execution_boundary.md", "status": "working", "source_ids": ["source_a0c7811ba12c9cf80bfd26c9"], "snippet": "# 人机客户端与 [Agent] 执行的双协议边界\n\n在三层机器人 [Agent] 架构中，以 [Agent]-Client Protocol（ACP）连接人类界面与推理 [Agent]，承载流式可观察性、显式授权和任务中断；以 Model Context…", "match_reason": "metadata:title"}, {"id": "claim_via_interface_first_robot_control_20260715", "type": "claim", "title": "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人", "path": "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md", "status": "canonical", "source_ids": ["source_86bad679192d3c34f728058b"], "snippet": "# VIA 表明通用视觉 [Agent] 可在限定仿真任务中通过工具界面零样本闭环控制机器人\n\n## 论文主张\n\nVIA 把机器人控制转换为视觉 [Agent] 的工具使用任务：未经机器人专项微调的前沿通用 [Agent] 观察浏览器中的三维点云和相机画面，通过 MCP 工具设置虚拟目标夹爪，显式执行 waypoint，再根据新观察纠错和继续规划…", "match_reason": "metadata:title"}, {"id": "reflection_4430cc70fe95425f717c1e71", "type": "reflection", "title": "RPent：把冻结 VLA 放进可递归反思的具身 Agent 外壳", "path": "vault/reflections/reflection-reflection_4430cc70fe95425f717c1e71.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "# RPent：把冻结 VLA 放进可递归反思的具身 [Agent] 外壳\n\n## Why important\n\nRPent 把 perception、reasoning、memory、execution 与 self-evolution 组织成服务化…", "match_reason": "metadata:title"}, {"id": "concept_318dd9fc807b1f13620238ec", "type": "concept", "title": "可构建与可审计的模块化 Agent 提示", "path": "vault/memory/concept/concept_318dd9fc807b1f13620238ec.md", "status": "working", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# 可构建与可审计的模块化 [Agent] 提示\n\n将 [Agent] 提示拆为可组合的模块和参数模板，在部署前解析依赖、检查缺失变量与循环导入，并把渲染结果作为可测试、可差异比较的构建产物；[Agent] 对指令的建议修改仍应经代码审查和评估后发布。", "match_reason": "metadata:title"}, {"id": "concept_asymmetric_frozen_vla_harness", "type": "concept", "title": "冻结 VLA 的非对称技能编排", "path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "status": "working", "source_ids": ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54"], "snippet": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 [Agent] 外壳把感知…", "match_reason": "metadata:aliases"}, {"id": "reflection_7952be977c24d5dfe1da2072", "type": "reflection", "title": "图式 Agent Memory：生命周期完整不等于证据闭环完整", "path": "vault/reflections/reflection-reflection_7952be977c24d5dfe1da2072.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92"], "snippet": "# 图式 Agent [Memory]：生命周期完整不等于证据闭环完整\n\n## Why important\n\n这份综述把 Agent [Memory] 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测…", "match_reason": "metadata:title"}, {"id": "concept_c37ccf2640da63192432d5d5", "type": "concept", "title": "VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation", "path": "vault/memory/concept/concept_c37ccf2640da63192432d5d5.md", "status": "working", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# VLA 的力历史记忆用于非 Markov 接触操作 / force-history [memory] for non-Markov contact-rich VLA manipulation\n\n在接触丰富、视觉事件含糊的非 Markov 操作中…", "match_reason": "metadata:title"}, {"id": "concept_language_corrective_memory_data_flywheel", "type": "concept", "title": "语言纠错记忆驱动的机器人数据飞轮", "path": "vault/memory/concept/concept_language_corrective_memory_data_flywheel.md", "status": "working", "source_ids": ["source_5e14510061220db7f2344913"], "snippet": "# 语言纠错记忆驱动的机器人数据飞轮\n\nZero2Skill 让自主 Agent 采集演示，在失败复现时接收简短人类语言修正，将其持久化为 Corrective [Memory]，并用视觉验证和轨迹认证决定重试与入库；随后用合格数据微调策略并部署。该闭环可降低持续遥操作负担，但其数据质量取决于工具执行、视觉验证器和任务分布，采集成功率不能替代下游策略评测。", "match_reason": "metadata:aliases"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:aliases"}, {"id": "reflection_bd1bc1b00ef5304ee9d29e9c", "type": "reflection", "title": "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens", "path": "vault/reflections/reflection-reflection_bd1bc1b00ef5304ee9d29e9c.md", "status": "active", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into [memory] tokens\n\n## Why important\n\nFM-VLA 以预训练 VAE…", "match_reason": "metadata:title"}, {"id": "concept_f35cd7f55e4108ce45ec35d7", "type": "concept", "title": "面向异构机器人策略的能力边界路由与记忆交接", "path": "vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md", "status": "working", "source_ids": ["source_cc2f2812863ca6751c223b54"], "snippet": "# 面向异构机器人策略的能力边界路由与记忆交接\n\nRoboHarness 将独立开发的 VLA、强化学习和任务运动规划控制器封装为可路由模块，并用多模态执行记忆和在线证据估计各策略在当前子任务中的适用边界；在策略切换前，其 [Memory] Bridge 检索与下一策略相关的执行轨迹、估计该策略的分布内状态区域，并引导机器人接近该区域，以降低未经联合训练的控制器之间的状态分布错配。该机制的效果仍取决于能力估计、状态表示和检索轨迹对实际交接条件的覆盖。", "match_reason": "metadata:aliases"}, {"id": "concept_native_action_aligned_vla_memory", "type": "concept", "title": "动作对齐的 VLA 原生视觉记忆压缩", "path": "vault/memory/concept/concept_native_action_aligned_vla_memory.md", "status": "working", "source_ids": ["source_748cef2215ddc958568e6368"], "snippet": "# 动作对齐的 VLA 原生视觉记忆压缩\n\nNativeMEM 将每个历史帧—相机视角压缩为一个与预训练 VLA token 维度兼容的记忆 token；第一阶段冻结 VLA，仅以原动作预测损失训练由视觉编码器初始化的 [memory] tokenizer，第二阶段缓存 token 并微调策略…", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# Latent [Memory] Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "concept_action_centric_embodied_vlm_taxonomy", "type": "concept", "title": "动作中心的具身 VLM 能力分类", "path": "vault/memory/concept/concept_action_centric_embodied_vlm_taxonomy.md", "status": "working", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "# 动作中心的具身 VLM 能力分类\n\nHy-Embodied-VLM-1.0 将具身视觉语言能力划分为动作相关状态理解、动作转移推理、序列与自适应推理，并据此组织预训练和后训练数据；其稀疏 MoE 架构面向延迟敏感部署。该分类描述的是动作前置的视觉语言推理能力，不应与连续动作生成、闭环…", "match_reason": "metadata:aliases"}, {"id": "reflection_d622c6d4e908ef7dae5470b8", "type": "reflection", "title": "Hy-Embodied-VLM：动作中心能力分类约束数据配方，而非直接输出控制", "path": "vault/reflections/reflection-reflection_d622c6d4e908ef7dae5470b8.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "…Hy-Embodied-VLM 输出状态与动作推理表征；VLA 概念进一步要求将观察和语言映射为可执行动作。\n\n## Conflicts\n\nNone recorded.\n\n## Open questions\n\n- 动作中心 [taxonomy] 的每一维对下游真实机器人成功率分别贡献多少？\n\n## Possible mechanisms\n\n- 按动作相关层次筛选数据可减少通用 VLM…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_01ed2f19e91bb0eb1ec3ee92"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "c2b05d2462ceda90d223e257abd0b18283744ad3aabe8b3ca42099eb1533c6c2"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-legacy-readmission`
- Extraction：`extraction_7d89b66ae99258c52fd33577`
- 编译前召回已有对象：18
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_f5d1ef9eaed1cd6bec4d4c52-图式-agent-memory-的生命周期与评测闭环-lifecycle-and-evaluation-closure-for-.md
@@ -0,0 +1,20 @@
+---
+id: "concept_f5d1ef9eaed1cd6bec4d4c52"
+type: "concept"
+status: "proposal"
+title: "图式 Agent Memory 的生命周期与评测闭环 / lifecycle and evaluation closure for graph-based agent memory"
+created_at: "2026-07-28T13:11:47+08:00"
+updated_at: "2026-07-28T13:11:47+08:00"
+aliases: ["graph-based agent memory lifecycle", "agent memory extraction storage retrieval evolution", "图记忆演化闭环", "图式记忆评测"]
+tags: []
+domains: ["agent-memory", "knowledge-graph", "memory-evolution", "evaluation"]
+confidence: "medium"
+source_ids: ["source_01ed2f19e91bb0eb1ec3ee92"]
+relations: [{"type": "derived_from", "target_id": "source_01ed2f19e91bb0eb1ec3ee92", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-legacy-readmission", "status": "proposal"}]
+change_reason: "compile bundle from source_01ed2f19e91bb0eb1ec3ee92"
+reflection_context: {"reflection_ids": ["reflection_7952be977c24d5dfe1da2072"], "importance": "high", "changed_belief": "此前容易把图式记忆的价值概括为多跳检索；综述更重要的启发是，关系结构只有与选择性写入、冲突演化、环境反馈和可隔离的记忆评测结合，才构成长期认知系统。", "surprising": "综述明确指出，许多基准擅长测回忆，却缺少对冲突事实更新、选择性写入、遗忘和隐私保留的系统监督；这意味着检索成绩不能替代记忆演化质量。", "connections": [{"shared_mechanism": "综述的 extraction-storage-retrieval-evolution 生命周期与 Global Memory 的 Raw/Input-Working-Context-governed evolution 都把记忆视为持续更新的结构系统。", "boundary": "综述是广域二手分类材料，不能证明 Global Memory 的具体门禁、数据模型或效果优于其他系统。", "difference": "综述主要按图结构与算法类别组织领域；Global Memory 用 Markdown 真相层和 typed relations 表达图，并把证据、Receipt 与 Canonical 审批作为独立治理边界。"}], "open_questions": ["怎样设计能独立测量冲突更新、选择性写入和长期复用收益，而不把规划器或基础模型能力混入结果的基准？"]}
+---
+
+# 图式 Agent Memory 的生命周期与评测闭环 / lifecycle and evaluation closure for graph-based agent memory
+
+图式 Agent Memory 可被组织为持续循环：从交互或外部材料中选择性抽取记忆单元，将实体、事件、概念或文本块及其语义、时间、因果关系写入图结构；在任务中通过语义相似、图遍历或二者组合检索相关子图；再依据新观察、动作和环境反馈增量增加、修改、失效或冲突化节点与关系。关系图能够支持多跳和层级推理，但结构存在本身不等于长期记忆质量。评测至少要分开测量检索相关性、图的一致性与完整性、冗余和时间一致性、下游任务效用，以及冲突事实更新、选择性写入、遗忘、外部真实性校验、隐私泄漏与来源可追溯性。综述指出现有基准常偏重回忆，难以隔离记忆模块、规划器和基础模型的贡献；因此，高召回或高连接度不能替代记忆演化与证据闭环的验证。该来源是领域综述，提供分类框架而非证明某一实现优于其他系统。
```
