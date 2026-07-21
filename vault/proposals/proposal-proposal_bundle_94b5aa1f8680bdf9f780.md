---
id: "proposal_bundle_94b5aa1f8680bdf9f780"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:39:41+08:00"
updated_at: "2026-07-20T12:39:41+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_951559714c0383331b1b30ac"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-c-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_3d90e2c85075bed4343adef4"
input_sha256: "5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_fc70bfc09ac7d9473592f09c", "target_path": "vault/knowledge/concepts/concept_fc70bfc09ac7d9473592f09c-全身冗余的部分运动学嵌入.md", "base_sha256": null, "candidate_sha256": "732fb52eb94b16c20b85408ca34112fb468576da8ec3252c172241928d9c4ecf", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_94b5aa1f8680bdf9f780-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_fc70bfc09ac7d9473592f09c.md", "working_at": "2026-07-20T12:39:41+08:00"}]
existing_context: [{"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_951559714c0383331b1b30ac"}
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

- Provider：`codex-gpt56-m91-daily-batch-c-20260720`
- Extraction：`extraction_3d90e2c85075bed4343adef4`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_fc70bfc09ac7d9473592f09c-全身冗余的部分运动学嵌入.md
@@ -0,0 +1,20 @@
+---
+id: "concept_fc70bfc09ac7d9473592f09c"
+type: "concept"
+status: "proposal"
+title: "全身冗余的部分运动学嵌入"
+created_at: "2026-07-20T12:39:41+08:00"
+updated_at: "2026-07-20T12:39:41+08:00"
+aliases: ["Partial kinematic embedding", "PAKE", "Kinematic Normalizing Flow", "全身运动学冗余 Latent"]
+tags: []
+domains: ["embodied-ai", "whole-body-control", "loco-manipulation", "kinematic-redundancy"]
+confidence: "high"
+source_ids: ["source_951559714c0383331b1b30ac"]
+relations: [{"type": "derived_from", "target_id": "source_951559714c0383331b1b30ac", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_951559714c0383331b1b30ac"
+reflection_context: {"reflection_ids": ["reflection_070e73598e48429fb5eafe01"], "importance": "high", "changed_belief": "全身控制的冗余不必由单一 end-to-end RL 在原始关节空间从头搜索；可以先把运动学可行解分布编码成可导航 latent，再把动力学和稳定性留给低层。", "surprising": "框架把躯干高度、roll、pitch 当作额外手臂自由度来扩大工作空间，同时仍要求底盘速度跟踪，明确利用而非压制浮动基座冗余。", "connections": [{"shared_mechanism": "与 REGRIND 都先构造结构化参考/先验，再用 RL 学习闭环残差或选择。", "boundary": "PAKE 的硬件证据来自带六自由度机械臂的四足平台，8 个任务共 24 回合；不能外推到任意人形、本体或高冲击接触。", "difference": "PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。"}], "open_questions": ["怎样检测目标任务所需解落在 KNF 支持集之外，并安全扩展 reference 分布？"]}
+---
+
+# 全身冗余的部分运动学嵌入
+
+学习给定末端目标下的可行 partial reference 分布，把全身运动学冗余压缩为高层可导航 latent，再由低层 imitation controller 保证动力学可行执行。它利用浮动基座和躯干自由度扩大工作空间，但支持集受运动学数据覆盖约束。
```
