---
id: "proposal_bundle_08c1b1375adc6c92f2e9"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-26T12:32:27+08:00"
updated_at: "2026-07-26T12:32:45+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
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
extraction_id: "extraction_e98976f6b17c4f967f55c0f7"
input_sha256: "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_relation_triggered_process_safety", "target_path": "vault/memory/concept/concept_relation_triggered_process_safety.md", "base_sha256": "c4a46ece8b912f58c09fbfc799a545ad32eeb4afab50c841b82bec1790ab1a4d", "candidate_sha256": "b34bb10250299d98e8023e54d9eb0c7e9864e098899fbbe9a35d54cc20b82cb7", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_08c1b1375adc6c92f2e9-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_08c1b1375adc6c92f2e9-concept-1.md", "working_path": "vault/memory/concept/concept_relation_triggered_process_safety.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-26T12:32:45+08:00"}]
existing_context: [{"id": "reflection_ee2dc3e5679d14ca67d9f5df", "type": "reflection", "title": "SafeRelBench：安全必须在风险动作之前验证关系前置条件", "path": "vault/reflections/reflection-reflection_ee2dc3e5679d14ca67d9f5df.md", "status": "active", "source_ids": ["source_b470fe87f9d09df2b7d3b5fd"], "snippet": "…类型化技能图面向执行前验证契约；[SafeRelBench] 衡量 Agent 是否在风险动作发生前主动满足关系条件。\n\n## Conflicts\n\nNone recorded.\n\n## Open questions\n\n- 关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？\n\n## Possible mechanisms\n\n- 把每个安全条件绑定到具体 risk-prone action，可检测动作顺序中的过程失败…", "match_reason": "metadata:title"}, {"id": "concept_relation_triggered_process_safety", "type": "concept", "title": "关系触发的具身过程安全", "path": "vault/memory/concept/concept_relation_triggered_process_safety.md", "status": "working", "source_ids": ["source_b470fe87f9d09df2b7d3b5fd"], "snippet": "# 关系触发的具身过程安全\n\n将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。", "match_reason": "metadata:aliases"}, {"id": "synthesis_180dbd6bb5b146e333818008", "type": "synthesis", "title": "按需语义、状态交接与快环权限：具身系统的时序化接口边界", "path": "vault/synthesis/synthesis-synthesis_180dbd6bb5b146e333818008.md", "status": "active", "source_ids": ["source_45c4de28acb4ba36642f1594", "source_4e06d1b1cdcd0d07eff47909", "source_4f709a2f26b6_v0002_cb9f3e56f3e6", "source_b470fe87f9d09df2b7d3b5fd", "source_cc2f2812863ca6751c223b54", "source_d4762e0cf2330ab6ea00a521", "source_d90b4e9bf278dfc5e68d1bb5", "source_e8650c5afb7548268f649fb8"], "snippet": "…mechanism\": \"[SafeRelBench]、LIFT、FastSlow-LMDrive 与 FORGE-plus 都把慢语义或预训练上下文限制在提议层，并要求执行时读取更新鲜的局部状态。\",\n    \"boundary\": \"语义关系、六维力、驾驶视觉与接触峰值具有不同传感延迟和危险变量；共同的快慢结构不能让一种模态的安全结论外推到另一模态。\",\n    \"difference\": \"[SafeRelBench] 检查风险动作前的离散关系…", "match_reason": "full-text:body"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…This is a WeChat launch report, not the Qwen technical reports, model cards, repositories, or [benchmark] artifacts. Dataset…", "match_reason": "full-text:body"}, {"id": "reflection_9f1bface11ec7ba8723e8def", "type": "reflection", "title": "HY-Embodied 仓库：为论文主张补充可运行工件而非第二份事实", "path": "vault/reflections/reflection-reflection_9f1bface11ec7ba8723e8def.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "# HY-Embodied 仓库：为论文主张补充可运行工件而非第二份事实\n\n## Why important\n\n仓库提供模型权重、推理代码、[benchmark] 表和技术报告，可用于核对可用性与复现入口，但与 arXiv 论文属于同一项目来源。\n\n## What changed\n\n配套 GitHub…", "match_reason": "full-text:body"}, {"id": "reflection_d622c6d4e908ef7dae5470b8", "type": "reflection", "title": "Hy-Embodied-VLM：动作中心能力分类约束数据配方，而非直接输出控制", "path": "vault/reflections/reflection-reflection_d622c6d4e908ef7dae5470b8.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "…具身 VLM [benchmark] 不等于连续动作生成、低层控制或真实安全验证。\n  Difference: Hy-Embodied-VLM 输出状态与动作推理表征；VLA 概念进一步要求将观察和语言映射为可执行动作。\n\n## Conflicts\n\nNone recorded.\n\n## Open questions\n\n- 动作中心…", "match_reason": "full-text:body"}, {"id": "reflection_59bfe9d29f3ebbb4c8a6b162", "type": "reflection", "title": "Secondary architecture commentary: autoregression versus flow matching is an interface question", "path": "vault/reflections/reflection-reflection_59bfe9d29f3ebbb4c8a6b162.md", "status": "active", "source_ids": ["source_e6608d8f849ad472bbd95143"], "snippet": "…of G0.5, not the official technical report. [Benchmark] numbers, training-data descriptions, tokenizer details, and causal claims…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b470fe87f9d09df2b7d3b5fd"}
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
- Extraction：`extraction_e98976f6b17c4f967f55c0f7`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_relation_triggered_process_safety.md
+++ candidate:vault/memory/concept/concept_relation_triggered_process_safety.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_relation_triggered_process_safety"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "关系触发的具身过程安全"
 created_at: "2026-07-21T17:42:01+08:00"
-updated_at: "2026-07-21T17:42:02+08:00"
+updated_at: "2026-07-26T12:32:27+08:00"
 aliases: ["Relation-Triggered Embodied Process Safety", "SafeRelBench", "Spatial-Relation-Aware Process Safety", "空间关系过程安全"]
 tags: []
 domains: ["embodied-ai", "robot-safety", "spatial-reasoning"]
 confidence: "medium"
 source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
-relations: [{"type": "derived_from", "target_id": "source_b470fe87f9d09df2b7d3b5fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都要求在动作执行前检查类型化前置条件；该基准提供过程安全评测，而技能图提供执行结构。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_b470fe87f9d09df2b7d3b5fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都要求在动作执行前检查类型化前置条件；该基准提供过程安全评测，而技能图提供执行结构。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "SafeRelBench 约束风险动作前的关系条件，FORGE-plus 约束动作中的物理力权限；两者形成顺序安全与连续安全的双门禁，但任一门禁都不能替代另一门禁。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_b470fe87f9d09df2b7d3b5fd"
-reflection_context: {"reflection_ids": ["reflection_ee2dc3e5679d14ca67d9f5df"], "importance": "high", "changed_belief": "完成任务与安全完成任务必须分开计量；即使最终目标正确，错误动作顺序仍可能造成不可见于终态指标的危险。", "surprising": "七个 VLM Agent 在匹配控制中安全成功率最高达 0.91，而加入空间关系风险后降至 0.16–0.40；增加安全提示仍不足以解决动作落地。", "connections": [{"shared_mechanism": "都用类型化前置条件约束动作序列。", "boundary": "基准中的符号关系和模拟器检查不能替代真实传感、动力学和控制级安全。", "difference": "类型化技能图面向执行前验证契约；SafeRelBench 衡量 Agent 是否在风险动作发生前主动满足关系条件。"}], "open_questions": ["关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-daily-gpt56sol-readmission-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-daily-gpt56sol-readmission-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_3d280267fd5befffee7d"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_3d280267fd5befffee7d-concept-1.md"
-origin_candidate_sha256: "64f1d6e27809397688bd00a33be5810f286e16e371c88a8bc1c55b6401f8defe"
-memory_schema_version: 2
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_5eb9ba718b0b143e55d0b020", "reflection_ee2dc3e5679d14ca67d9f5df"], "importance": "weekly", "changed_belief": "此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。\n完成任务与安全完成任务必须分开计量；即使最终目标正确，错误动作顺序仍可能造成不可见于终态指标的危险。", "surprising": "读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。\n七个 VLM Agent 在匹配控制中安全成功率最高达 0.91，而加入空间关系风险后降至 0.16–0.40；增加安全提示仍不足以解决动作落地。", "connections": [{"shared_mechanism": "FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。", "boundary": "连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。", "difference": "FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。"}, {"shared_mechanism": "都用类型化前置条件约束动作序列。", "boundary": "基准中的符号关系和模拟器检查不能替代真实传感、动力学和控制级安全。", "difference": "类型化技能图面向执行前验证契约；SafeRelBench 衡量 Agent 是否在风险动作发生前主动满足关系条件。"}], "open_questions": ["如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？", "关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？"]}
+proposed_status: "working"
 ---
 
 # 关系触发的具身过程安全
```
