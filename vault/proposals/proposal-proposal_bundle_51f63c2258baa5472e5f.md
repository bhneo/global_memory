---
id: "proposal_bundle_51f63c2258baa5472e5f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:44:57+08:00"
updated_at: "2026-07-21T17:44:58+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_04477c8679bc779d8389a22e"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56sol-readmission-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_f2cf4437106881e82abedd25"
input_sha256: "49b7ef2140e16688ee5ddff887d03cb1406885129085031d90d7d3cbb4feb6ed"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_dual_timescale_lifelong_vla_adaptation", "target_path": "vault/knowledge/concepts/concept_dual_timescale_lifelong_vla_adaptation-双时间尺度的持续-vla-适配.md", "base_sha256": null, "candidate_sha256": "d111bf1f3c31501e1d7246cfbb7d4213e94c6ed969b209d2929c6c8f2a3b5eb7", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_51f63c2258baa5472e5f-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_dual_timescale_lifelong_vla_adaptation.md", "working_at": "2026-07-21T17:44:58+08:00"}]
existing_context: [{"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…shared workspace as a debuggability boundary for [physical] agents\n\n## Why important\n\nThe Jiuwen Symbiosis profile exposes perception, safe…", "match_reason": "metadata:title"}, {"id": "input_e69b286ace68f56c81ab185b", "type": "input", "title": "[2607.12894] Hy-Embodied-VLM-1.0: Efficient Physical-World Agents", "path": "vault/inputs/input-input_e69b286ace68f56c81ab185b.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "…Efficient [Physical]-World Agents\n\nInput Episode for `source_bd08e368730960f4f6ce19ca`. The immutable Source remains authoritative.\n\n# [2607.12894] Hy-Embodied…", "match_reason": "metadata:title"}, {"id": "input_a070092fbe4bbba0a3effe85", "type": "input", "title": "GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub", "path": "vault/inputs/input-input_a070092fbe4bbba0a3effe85.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "…Agentic Infrastructure for the [Physical] World · GitHub\n\nInput Episode for `source_6b52a51e2b4a3be43c97c386`. The immutable Source remains authoritative.\n\n# GitHub…", "match_reason": "metadata:title"}, {"id": "concept_asymmetric_frozen_vla_harness", "type": "concept", "title": "冻结 VLA 的非对称技能编排", "path": "vault/memory/concept/concept_asymmetric_frozen_vla_harness.md", "status": "working", "source_ids": ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386"], "snippet": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知…", "match_reason": "metadata:aliases"}, {"id": "work_arxiv_2601_03220", "type": "work", "title": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence", "path": "vault/memory/work/work_arxiv_2601_03220.md", "status": "working", "source_ids": ["source_deb313c98b03fc4d0b33794a", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "…Rethinking Information for Computationally Bounded [Intelligence]\n\n## Logical work identity\n\n- arXiv：`2601.03220`\n- Version：`unknown`\n- Captures：`source_deb313c98b03fc4d0b33794a`, `source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_04477c8679bc779d8389a22e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`agent-semantic-daily-gpt56sol-readmission-v1`
- Extraction：`extraction_f2cf4437106881e82abedd25`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_dual_timescale_lifelong_vla_adaptation-双时间尺度的持续-vla-适配.md
@@ -0,0 +1,20 @@
+---
+id: "concept_dual_timescale_lifelong_vla_adaptation"
+type: "concept"
+status: "proposal"
+title: "双时间尺度的持续 VLA 适配"
+created_at: "2026-07-21T17:44:57+08:00"
+updated_at: "2026-07-21T17:44:57+08:00"
+aliases: ["Dual-Timescale Lifelong VLA Adaptation", "LifelongVLA", "Continual VLA Learning", "持续视觉语言动作学习"]
+tags: []
+domains: ["embodied-ai", "vla", "continual-learning"]
+confidence: "medium"
+source_ids: ["source_04477c8679bc779d8389a22e"]
+relations: [{"type": "derived_from", "target_id": "source_04477c8679bc779d8389a22e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_skill_evolution", "reason": "两者都处理能力随经验累积的稳定更新，但一个发生在模型 adapter 内部，另一个强调外部技能工件与验证。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_04477c8679bc779d8389a22e"
+reflection_context: {"reflection_ids": ["reflection_eca8957906652e0850a7f644"], "importance": "high", "changed_belief": "持续 VLA 的关键接口不仅是保留多少数据，还包括哪些参数承担短期变化、何时合并到长期路径以及任务身份如何被识别。", "surprising": "作者报告相对基线成功率提升超过 13%、遗忘率降低超过 8.2%，真机任务均超过 80%；这些结论仍局限于其增量任务顺序和已知任务门控设置。", "connections": [{"shared_mechanism": "都把经验分成快速适应与稳定保留的不同时间尺度。", "boundary": "LoRA 门控的参数稳定性不等于跨形态技能语义已被正确迁移。", "difference": "技能进化强调外部技能版本和验证；LifelongVLA 在模型参数内部通过双 LoRA 路径和缓存 replay 管理遗忘。"}], "open_questions": ["未知任务边界、相似技能冲突和长序列任务到来时，门控是否仍能正确分配短长期适配？"]}
+---
+
+# 双时间尺度的持续 VLA 适配
+
+LifelongVLA 用短期 LoRA adapter 支持新任务可塑性、长期 LoRA adapter 保存稳定能力，并通过任务感知 gate 组合两条路径；缓存高效的随机 replay 在不保留完整轨迹的情况下提供旧技能信号。该机制显式处理 plasticity–stability trade-off，但依赖任务识别、缓存代表性和有限任务序列上的实验验证。
```
