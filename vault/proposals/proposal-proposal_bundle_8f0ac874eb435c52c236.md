---
id: "proposal_bundle_8f0ac874eb435c52c236"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub"
created_at: "2026-07-20T13:33:11+08:00"
updated_at: "2026-07-20T13:33:31+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_6b52a51e2b4a3be43c97c386"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_2da6c109dd8922eb96a74733"
input_sha256: "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_asymmetric_frozen_vla_harness", "target_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "base_sha256": "71dfe3a232a857d46b735f2f16959ca4fbfe5232b1edc24ec94915e75fa93877", "candidate_sha256": "ce191352e03f7c6e1d9628b630d97ae49dfab60659345f01ce2149c9977feae0", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_8f0ac874eb435c52c236-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_8f0ac874eb435c52c236-concept-1.md", "working_path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-20T13:33:31+08:00"}]
existing_context: [{"id": "input_a070092fbe4bbba0a3effe85", "type": "input", "title": "GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub", "path": "vault/inputs/input-input_a070092fbe4bbba0a3effe85.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "# GitHub - RLinf/RPent: RPent: [Agentic] Infrastructure for the Physical World · GitHub\n\nInput Episode for `source_6b52a51e2b4a3be43c97c386`. The immutable…", "match_reason": "metadata:title"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "…NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · [GitHub]\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The…", "match_reason": "metadata:title"}, {"id": "reflection_4430cc70fe95425f717c1e71", "type": "reflection", "title": "RPent：把冻结 VLA 放进可递归反思的具身 Agent 外壳", "path": "vault/reflections/reflection-reflection_4430cc70fe95425f717c1e71.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "# [RPent]：把冻结 VLA 放进可递归反思的具身 Agent 外壳\n\n## Why important\n\n[RPent] 把 perception、reasoning、memory、execution 与 self-evolution 组织成服务化…", "match_reason": "metadata:title"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…Like [RPent], it decomposes perception, reasoning, memory, and execution into composable physical-agent services.\n  Boundary: This is an…", "match_reason": "full-text:body"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，[Agentic]-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_training_efficiency_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 上以 700 次迭代达到 90% 成功率，论文报告其相对 EVOLVE-VLA 收敛快 2.4×", "path": "vault/memory/claim/claim_agentic_vla_training_efficiency_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的训练效率\n\n在 LIBERO-Long 达到论文定义的 90% 成功率阈值时，[Agentic]-VLA 使用 700 次训练迭代和 22.4k rollouts；EVOLVE…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的跨任务适应结果\n\n论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_one_shot_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点", "path": "vault/memory/claim/claim_agentic_vla_one_shot_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# [Agentic]-VLA 的 one-shot 结果\n\n在每个任务仅使用一条 demonstration 做 SFT pre-training 的设定下，[Agentic]-VLA 在 LIBERO 四套件上的平均成功率为…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_6b52a51e2b4a3be43c97c386"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_2da6c109dd8922eb96a74733`
- 编译前召回已有对象：8
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md
+++ candidate:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_asymmetric_frozen_vla_harness"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "冻结 VLA 的非对称技能编排"
 created_at: "2026-07-19T12:18:32+08:00"
-updated_at: "2026-07-19T12:20:06+08:00"
-aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA"]
+updated_at: "2026-07-20T13:33:11+08:00"
+aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA", "physical-agent service shell", "物理 Agent 服务化外壳", "agentic infrastructure for the physical world"]
 tags: []
-domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation"]
+domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation", "agent-infrastructure", "robot-memory"]
 confidence: "medium"
-source_ids: ["source_4bff03c9d5adb3463b34f947"]
-relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
-change_reason: "compile bundle from source_4bff03c9d5adb3463b34f947"
-uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-19T12:20:06+08:00"
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
-last_consolidation_id: "consolidation_314019a3a8e7261df3f7bd23"
+source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386"]
+relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "冻结 VLA 外壳若要把反思和记忆转化为可靠改进，必须依赖可回放的执行结果、里程碑评分与动作流日志来区分模型能力、编排和恢复贡献。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_6b52a51e2b4a3be43c97c386"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_4430cc70fe95425f717c1e71", "reflection_7952be977c24d5dfe1da2072"], "importance": "weekly", "changed_belief": "此前容易把 VLA 后训练等同于更新策略参数；RPent 的工程路线提示，冻结 VLA 也可被上层 Agent 组织成可复用操作原语，但这类系统收益必须与底层 VLA 本身的能力分开评估。\n此前容易把图式记忆的价值概括为多跳检索；综述更重要的启发是，关系结构只有与选择性写入、冲突演化、环境反馈和可隔离的记忆评测结合，才构成长期认知系统。", "surprising": "仓库把 Claude Code、Codex 或 API 模型作为可替换 cerebrum，并允许复用独立 VLA 与环境服务，说明其核心抽象是异构智能编排而非单一模型。\n综述明确指出，许多基准擅长测回忆，却缺少对冲突事实更新、选择性写入、遗忘和隐私保留的系统监督；这意味着检索成绩不能替代记忆演化质量。", "connections": [{"shared_mechanism": "与 VIA 都把基础机器人策略或控制能力封装成 Agent 可调用的界面，通过观察、规划、执行和再观察形成闭环。", "boundary": "当前 Source 是 RPent 官方 GitHub README，只能支持项目设计与安装接口；Harness VLA 的论文方法、实验和可靠性结论仍需回到 arXiv 2607.08448 核验。", "difference": "VIA 论文研究通用视觉 Agent 直接操纵工具接口；RPent 是包含记忆、VLA 服务、环境服务和可替换 cerebrum 的递归基础设施。"}, {"shared_mechanism": "综述的 extraction-storage-retrieval-evolution 生命周期与 Global Memory 的 Raw/Input-Working-Context-governed evolution 都把记忆视为持续更新的结构系统。", "boundary": "综述是广域二手分类材料，不能证明 Global Memory 的具体门禁、数据模型或效果优于其他系统。", "difference": "综述主要按图结构与算法类别组织领域；Global Memory 用 Markdown 真相层和 typed relations 表达图，并把证据、Receipt 与 Canonical 审批作为独立治理边界。"}], "open_questions": ["Harness VLA 中 memory-guided steering 的具体记忆单元、失败恢复机制和相对无记忆基线收益是什么？", "怎样设计能独立测量冲突更新、选择性写入和长期复用收益，而不把规划器或基础模型能力混入结果的基准？"]}
+proposed_status: "working"
 ---
 
 # 冻结 VLA 的非对称技能编排
 
 把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。
+
+## 新增来源材料
+
+- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。
```
