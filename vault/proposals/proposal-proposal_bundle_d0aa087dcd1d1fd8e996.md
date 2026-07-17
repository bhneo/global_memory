---
id: "proposal_bundle_d0aa087dcd1d1fd8e996"
type: "proposal"
status: "migrated"
title: "Compile bundle：Session receipt: M7 Codex real acceptance"
created_at: "2026-07-16T21:57:20+08:00"
updated_at: "2026-07-17T11:59:38+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_46d0aad5afd18dd21899796f"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Session receipt: M7 Codex real acceptance"
source_authority: "primary"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_b300427e7baf3c62dc7bd34d"
input_sha256: "2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e"
bundle_items: [{"item_id": "experiment-1", "object_type": "experiment", "action": "create", "target_id": "experiment_b6f1e1956690ac08fd56a5da", "target_path": "vault/action/experiments/experiment_b6f1e1956690ac08fd56a5da-codex-completed-the-first-real-m7-agent-acceptance-run-on-2026-0.md", "base_sha256": null, "candidate_sha256": "90b64a245da2cdb633df33e8597ccddeacccb7d917acca9cf20f11e34f7e8508", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_d0aa087dcd1d1fd8e996-experiment-1-rev-90b64a245da2.md", "base_path": null, "revision_history": [{"candidate_path": "vault/proposals/candidate-proposal_bundle_d0aa087dcd1d1fd8e996-experiment-1.md", "candidate_sha256": "8691fc9c4bd70a9d84c4651ecd92bf121d0176e12e3268ded89a1d5302457180", "reason": "补全真实验收步骤、故障、修复和结果", "revised_at": "2026-07-16T21:58:50+08:00"}], "review_reason": "补全真实验收步骤、故障、修复和结果", "working_path": "vault/memory/experiment/experiment_b6f1e1956690ac08fd56a5da.md", "working_at": "2026-07-17T11:59:38+08:00"}]
existing_context: [{"id": "claim_via_interface_first_robot_control_20260715", "type": "claim", "title": "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人", "path": "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md", "status": "confirmed", "source_ids": ["source_86bad679192d3c34f728058b"], "snippet": "…示例后，其三个 LIBERO-Goal 任务平均成功率从 77% 提高到 100%；[Codex]-5.5 没有从同类详细提示中获益。\n\n## 适用边界\n\n- 论文没有报告真实机器人实验，真实机器人部署被列为未来工作。\n- 推理速度限制 VIA 处理准静态任务…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_46d0aad5afd18dd21899796f"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "primary", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Session receipt: M7 Codex real acceptance

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_b300427e7baf3c62dc7bd34d`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型标记或保留第一段逐字材料，不补齐无意义对象。

## Items and diffs

### experiment-1 (create experiment)

```diff
--- /dev/null
+++ candidate:vault/action/experiments/experiment_b6f1e1956690ac08fd56a5da-codex-completed-the-first-real-m7-agent-acceptance-run-on-2026-0.md
@@ -0,0 +1,19 @@
+---
+id: "experiment_b6f1e1956690ac08fd56a5da"
+type: "experiment"
+status: "proposal"
+title: "Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry."
+created_at: "2026-07-16T21:57:20+08:00"
+updated_at: "2026-07-16T21:57:20+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_46d0aad5afd18dd21899796f"]
+relations: [{"type": "derived_from", "target_id": "source_46d0aad5afd18dd21899796f", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_46d0aad5afd18dd21899796f"
+---
+
+# Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry.
+
+Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry.
```

## Item revision: experiment-1

- Reason: 补全真实验收步骤、故障、修复和结果

```diff
--- previous-candidate
+++ revised-candidate
@@ -2,18 +2,33 @@
 id: "experiment_b6f1e1956690ac08fd56a5da"
 type: "experiment"
 status: "proposal"
-title: "Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry."
+title: "Codex M7 真实读取与 receipt 回写验收"
 created_at: "2026-07-16T21:57:20+08:00"
 updated_at: "2026-07-16T21:57:20+08:00"
 aliases: []
-tags: []
-domains: []
-confidence: "unknown"
+tags: ["m7", "agent-acceptance", "codex"]
+domains: ["global-memory"]
+confidence: "high"
 source_ids: ["source_46d0aad5afd18dd21899796f"]
-relations: [{"type": "derived_from", "target_id": "source_46d0aad5afd18dd21899796f", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
-change_reason: "compile bundle from source_46d0aad5afd18dd21899796f"
+relations: [{"type": "derived_from", "target_id": "source_46d0aad5afd18dd21899796f", "reason": "由 Codex M7 acceptance receipt 提出", "confidence": "high", "created_by": "codex-acceptance-review", "status": "proposal"}]
+change_reason: "补全真实验收步骤、故障、修复和结果，避免只保留 deterministic fallback 的首句"
 ---
 
-# Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry.
+# Codex M7 真实读取与 receipt 回写验收
 
-Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry.
+## 验收路径
+
+Codex 按 `vault/INDEX.md` 的入口执行了真实的 `gm context → task → receipt → proposal` 流程。任务是从限定 Context Pack 回答 VIA 论文的实验结论和适用边界，没有默认扫描整个 vault，也没有直接修改 canonical。
+
+## 发现并修复的问题
+
+- 完整自然语言问题最初因严格 all-term FTS 匹配返回空包；修复后只在主查询空召回时逐项尝试有区分度的空白分词，并在 Context Pack filters 中记录 `query_fallback`。
+- Markdown Context Pack 最初从不存在的 `status` 字段渲染状态，显示为 `None`；修复为读取契约字段 `knowledge_status`。
+
+## 修复后结果
+
+原始完整问题成功选择 confirmed VIA claim 和相关 source，并保留 truth layer、状态、路径、evidence、verification、选择理由与截断报告。Codex 从该包得出有边界的回答：结果来自六项 robosuite 仿真任务，最小提示总体成功率 60%–88%；不能外推到真实机器人、动态控制、长期记忆或持续学习。
+
+## 决定
+
+Codex 第一条真实验收在上述两项修复后通过。该结论仍是 pending experiment proposal；是否进入 canonical 由用户审阅决定。Cursor 和 Claude 的真实验收尚未执行。
```
