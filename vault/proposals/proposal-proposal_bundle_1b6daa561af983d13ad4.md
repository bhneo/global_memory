---
id: "proposal_bundle_1b6daa561af983d13ad4"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T18:58:12+08:00"
updated_at: "2026-08-02T18:58:13+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_8c84c595f1a48ba498b2074e"]
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
extraction_id: "extraction_a8e38002edf1d6ad67a17742"
input_sha256: "7aa885d7579449d3b366f636ec0ae7da77ec07cad24011f6e6b2c6f167789075"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_ca2e18a64c50dab0d08b3f1a", "target_path": "vault/knowledge/concepts/concept_ca2e18a64c50dab0d08b3f1a-依赖闭包的组件准入与新鲜作用域恢复-dependency-closed-component-admission-and-fres.md", "base_sha256": null, "candidate_sha256": "335152d923bab54d2cf84cc9a226c50a1384c90576b842403827585d813cd20e", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_1b6daa561af983d13ad4-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_ca2e18a64c50dab0d08b3f1a.md", "working_at": "2026-08-02T18:58:13+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "synthesis_4cda1c2094e661cde05160ef", "type": "synthesis", "title": "Agent capability lifecycles: verify frozen skills, then compile mature experience", "path": "vault/synthesis/synthesis-synthesis_4cda1c2094e661cde05160ef.md", "status": "active", "source_ids": ["source_38375a0f6ddc91f3bfde47d3", "source_d0908c8e9c58809dd2665c1e"], "snippet": "…updates\n\n[]\n\n## New connections\n\n[\n  {\n    \"shared_mechanism\": \"Both systems keep [heterogeneous] motor capabilities behind an orchestrator that observes outcomes, routes…", "match_reason": "full-text:body"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The common design question is where [heterogeneous] embodiments should be normalized.\n\n## What changed\n\nA robot foundation-model suite…", "match_reason": "full-text:body"}, {"id": "concept_8f574f03117d21adf127d23f", "type": "concept", "title": "以世界模型想象迭代修正动作计划 / Iterative action-plan refinement through world-model imagination", "path": "vault/memory/concept/concept_8f574f03117d21adf127d23f.md", "status": "working", "source_ids": ["source_a54ea0123fbadf6d7012c9fb"], "snippet": "# 以世界模型想象迭代修正动作计划 / Iterative action-plan refinement [through] world-model imagination\n\n长时机器人规划可以把语言模型的动作计划视为待验证初稿：先由 VLM 提出候选步骤，再通过正向运动学把机器人名义运动渲染成关节骨架 pose image，作为动作条件输入多任务世界模型；随后依据想象…", "match_reason": "metadata:title"}, {"id": "reflection_d8d4183ecacf40814756f4c2", "type": "reflection", "title": "Reflex 流式 VLA：缓存正确性来自上下文分区 / Reflex streaming VLA preserves caching through context partitioning", "path": "vault/reflections/reflection-reflection_d8d4183ecacf40814756f4c2.md", "status": "active", "source_ids": ["source_e67cd99ac31c7017d6f7f7c7"], "snippet": "# Reflex 流式 VLA：缓存正确性来自上下文分区 / Reflex streaming VLA preserves caching [through] context partitioning\n\n## Why important\n\nReflex 将 flow-matching…", "match_reason": "metadata:title"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…dexterous teleoperation [through] consecutive hand-object subgoals\n\n## Why important\n\nTELEDEXTER represents operator intent as consecutive hand-object co…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_8c84c595f1a48ba498b2074e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "657c678864cc62b59756149a9ec6bfc0bba843ef086c9aebe7435a73f19fcf3f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_a8e38002edf1d6ad67a17742`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_ca2e18a64c50dab0d08b3f1a-依赖闭包的组件准入与新鲜作用域恢复-dependency-closed-component-admission-and-fres.md
@@ -0,0 +1,20 @@
+---
+id: "concept_ca2e18a64c50dab0d08b3f1a"
+type: "concept"
+status: "proposal"
+title: "依赖闭包的组件准入与新鲜作用域恢复 / Dependency-closed component admission and fresh scoped recovery"
+created_at: "2026-08-02T18:58:12+08:00"
+updated_at: "2026-08-02T18:58:12+08:00"
+aliases: ["HALO", "support-closure admission", "one-dispatch token", "依赖闭包运行时准入"]
+tags: []
+domains: ["agent-safety", "robotics", "runtime-admission", "authorization"]
+confidence: "high"
+source_ids: ["source_8c84c595f1a48ba498b2074e"]
+relations: [{"type": "derived_from", "target_id": "source_8c84c595f1a48ba498b2074e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_protocol_hri_agent_execution_boundary", "reason": "两者都分离 Agent 交互、授权和能力派发；HALO 进一步定义回复组件在支持漂移下的闭包准入、摘要见证与最终门。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都用类型图、依赖和恢复结构约束机器人执行；技能图是长期 workflow，HALO 面向一次回复的运行时最大支持闭包和新鲜授权。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_8c84c595f1a48ba498b2074e"
+reflection_context: {"reflection_ids": ["reflection_0c154d1167b819af9040f0f9"], "importance": "high", "changed_belief": "我原先会把部分接受主要理解为 schema 过滤；该工作显示，单个组件即使本身受支持，也可能因依赖的结果、参考或前置条件失效而必须被闭包删除，而且闭包后仍需一次独立的实时授权。", "surprising": "恢复建议本身被建模为无权限 obligation：它能记录作用域、原因和恢复路线，却不能重放旧组件；只有重新生成的新候选通过完整准入后才可执行。", "connections": [{"shared_mechanism": "HALO 与 concept_dual_protocol_hri_agent_execution_boundary 都把 Agent 通信、授权和物理能力派发分层。", "boundary": "协议或准入门都不替代设备控制器的实时稳定性、碰撞避免与下游物理安全。", "difference": "既有节点描述 ACP/MCP 的通信职责，HALO 定义回复组件图在支持漂移下的保留闭包、摘要见证和单次派发 token。"}, {"shared_mechanism": "HALO 与 concept_typed_verified_robot_skill_graph 都以类型化图、依赖和恢复结构约束执行。", "boundary": "HALO 针对一次异构 Agent 回复的运行时准入，不等同于长期技能图的仿真验证和任务编排。", "difference": "技能图外化可复用 workflow；HALO 计算当前支持下的最大依赖闭包，并在最后一刻重新验证授权。"}], "open_questions": ["当支持目录、授权账本和执行适配器分布在多节点时，如何保持最终门的原子消费与当前闭包见证，而不把延迟变成新的竞态窗口？"]}
+---
+
+# 依赖闭包的组件准入与新鲜作用域恢复 / Dependency-closed component admission and fresh scoped recovery
+
+当一次 Agent 回复包含文本、建议、动作和恢复等异构组件时，保留与执行必须分成两层。先把回复视为不可信类型化组件图，依据可信能力目录为每个组件计算支持足迹，并迭代删除不受支持或依赖已删除组件的节点，得到当前支持下的最大依赖闭包。随后对保留组件生成确定性的规范摘要与见证，只签发绑定具体组件的一次性派发 token；唯一最终门在调用适配器前重新计算当前闭包、检查依赖处理阶段和摘要、原子消费 token。恢复 obligation 只记录作用域、原因、支持条件与路线，不携带旧动作权限；恢复必须生成新候选并重新经历完整准入。该协议依赖可信目录、支持提供者、授权账本和适配器，不能发现未声明依赖、证明语义真值、提供分布式 exactly-once 或替代下游物理安全。
```
