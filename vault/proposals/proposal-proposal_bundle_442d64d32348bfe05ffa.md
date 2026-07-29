---
id: "proposal_bundle_442d64d32348bfe05ffa"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-26T12:31:57+08:00"
updated_at: "2026-07-26T12:32:17+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_cc2f2812863ca6751c223b54"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-m91-weekly-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_fc1abc70524e79cc98092de2"
input_sha256: "5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_asymmetric_frozen_vla_harness", "target_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "base_sha256": "ac1925614d58ae6652df994544c68fea38f6af61b38fb22fa6abd16e09385758", "candidate_sha256": "99c1442415b8f155788b9ce25ac28b8d310f9086ad1b66a94e8078ecb08bf22c", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_442d64d32348bfe05ffa-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_442d64d32348bfe05ffa-concept-1.md", "working_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-26T12:32:17+08:00"}]
existing_context: [{"id": "reflection_d3da57bd40bcce58fcac3b37", "type": "reflection", "title": "RoboHarness：异构策略编排的关键是交接状态而非仅技能目录", "path": "vault/reflections/reflection-reflection_d3da57bd40bcce58fcac3b37.md", "status": "active", "source_ids": ["source_cc2f2812863ca6751c223b54"], "snippet": "# RoboHarness：异构策略编排的关键是交接状态而非仅技能目录\n\n## Why important\n\nRoboHarness 将长时程执行失败定位到两类可操作接口：策略在当前状态下的能力边界，以及前一策略终态是否落入下一策略的可行输入分布。这比把多策略系统描述成静态技能库更能指导何处需要观测、路由与恢复。\n\n## What changed\n\n此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。\n\n## Surprising\n\nNot…", "match_reason": "metadata:domains"}, {"id": "concept_f35cd7f55e4108ce45ec35d7", "type": "concept", "title": "面向异构机器人策略的能力边界路由与记忆交接", "path": "vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md", "status": "working", "source_ids": ["source_cc2f2812863ca6751c223b54"], "snippet": "# 面向异构机器人策略的能力边界路由与记忆交接\n\nRoboHarness 将独立开发的 VLA、强化学习和任务运动规划控制器封装为可路由模块，并用多模态执行记忆和在线证据估计各策略在当前子任务中的适用边界；在策略切换前，其 Memory Bridge 检索与下一策略相关的执行轨迹、估计该策略的分布内状态区域，并引导机器人接近该区域，以降低未经联合训练的控制器之间的状态分布错配。该机制的效果仍取决于能力估计、状态表示和检索轨迹对实际交接条件的覆盖。", "match_reason": "metadata:domains"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The common design question is where [heterogeneous] embodiments should be normalized.\n\n## What changed\n\nA robot foundation-model suite…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_cc2f2812863ca6751c223b54"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "a0ae1813c99ff1734e0b5885ddd78ca2bc6a811136320c85de991f476d74cefd"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-m91-weekly-v1`
- Extraction：`extraction_fc1abc70524e79cc98092de2`
- 编译前召回已有对象：3
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
-updated_at: "2026-07-20T13:33:22+08:00"
+updated_at: "2026-07-26T12:31:57+08:00"
 aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA", "physical-agent service shell", "物理 Agent 服务化外壳", "agentic infrastructure for the physical world"]
 tags: []
 domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation", "agent-infrastructure", "robot-memory"]
 confidence: "medium"
-source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386"]
-relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
-change_reason: "compile bundle from source_6b52a51e2b4a3be43c97c386"
-uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 2
-last_consolidated_at: "2026-07-20T13:33:22+08:00"
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
-last_consolidation_id: "consolidation_66f163c772d6c3083fcff831"
+source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54"]
+relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "RoboHarness 的支持域桥接处理策略交接状态，FORGE-plus 的快环权限处理恢复动作的物理安全上限；两者共同约束桥接，但状态兼容与力安全是不同门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_cc2f2812863ca6751c223b54"
 change_type: "refine"
-reflection_context: {"reflection_ids": ["reflection_4430cc70fe95425f717c1e71", "reflection_7952be977c24d5dfe1da2072"], "importance": "weekly", "changed_belief": "此前容易把 VLA 后训练等同于更新策略参数；RPent 的工程路线提示，冻结 VLA 也可被上层 Agent 组织成可复用操作原语，但这类系统收益必须与底层 VLA 本身的能力分开评估。\n此前容易把图式记忆的价值概括为多跳检索；综述更重要的启发是，关系结构只有与选择性写入、冲突演化、环境反馈和可隔离的记忆评测结合，才构成长期认知系统。", "surprising": "仓库把 Claude Code、Codex 或 API 模型作为可替换 cerebrum，并允许复用独立 VLA 与环境服务，说明其核心抽象是异构智能编排而非单一模型。\n综述明确指出，许多基准擅长测回忆，却缺少对冲突事实更新、选择性写入、遗忘和隐私保留的系统监督；这意味着检索成绩不能替代记忆演化质量。", "connections": [{"shared_mechanism": "与 VIA 都把基础机器人策略或控制能力封装成 Agent 可调用的界面，通过观察、规划、执行和再观察形成闭环。", "boundary": "当前 Source 是 RPent 官方 GitHub README，只能支持项目设计与安装接口；Harness VLA 的论文方法、实验和可靠性结论仍需回到 arXiv 2607.08448 核验。", "difference": "VIA 论文研究通用视觉 Agent 直接操纵工具接口；RPent 是包含记忆、VLA 服务、环境服务和可替换 cerebrum 的递归基础设施。"}, {"shared_mechanism": "综述的 extraction-storage-retrieval-evolution 生命周期与 Global Memory 的 Raw/Input-Working-Context-governed evolution 都把记忆视为持续更新的结构系统。", "boundary": "综述是广域二手分类材料，不能证明 Global Memory 的具体门禁、数据模型或效果优于其他系统。", "difference": "综述主要按图结构与算法类别组织领域；Global Memory 用 Markdown 真相层和 typed relations 表达图，并把证据、Receipt 与 Canonical 审批作为独立治理边界。"}], "open_questions": ["Harness VLA 中 memory-guided steering 的具体记忆单元、失败恢复机制和相对无记忆基线收益是什么？", "怎样设计能独立测量冲突更新、选择性写入和长期复用收益，而不把规划器或基础模型能力混入结果的基准？"]}
+reflection_context: {"reflection_ids": ["reflection_5eb9ba718b0b143e55d0b020", "reflection_d3da57bd40bcce58fcac3b37"], "importance": "weekly", "changed_belief": "此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。\n此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。", "surprising": "读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。", "connections": [{"shared_mechanism": "FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。", "boundary": "连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。", "difference": "FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。"}, {"shared_mechanism": "两者都把冻结或独立训练的控制模块置于更高层的适用范围管理与失败恢复接口之下。", "boundary": "该连接适用于存在可辨识子任务、可记录执行状态且能在切换前评估下一策略输入条件的长时程机器人系统。", "difference": "RoboHarness 以执行轨迹检索和空间分布学习来引导交接；既有冻结 VLA 编排概念以原语、验证与重试来约束局部专家。"}], "open_questions": ["如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？"]}
 proposed_status: "working"
-change_history: [{"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "changed_fields": [], "reason": "compile bundle from source_6b52a51e2b4a3be43c97c386", "trigger_source": "source_6b52a51e2b4a3be43c97c386", "evidence_added": []}]
 ---
 
 # 冻结 VLA 的非对称技能编排
@@ -47,3 +24,7 @@
 ## 新增来源材料
 
 - `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。
+
+## 新增来源材料
+
+- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。
```
