---
id: "proposal_bundle_c8181a6c545b74c2e642"
type: "proposal"
status: "migrated"
title: "Compile bundle：Session receipt: M7 Cursor real acceptance"
created_at: "2026-07-16T22:16:57+08:00"
updated_at: "2026-07-17T11:59:33+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_113d589e6dadf14b5fa8edea"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Session receipt: M7 Cursor real acceptance"
source_authority: "primary"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_beed2aa2edcb076d1706db84"
input_sha256: "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"
bundle_items: [{"item_id": "experiment-1", "object_type": "experiment", "action": "create", "target_id": "experiment_7101e03fb065226e65f388a5", "target_path": "vault/action/experiments/experiment_7101e03fb065226e65f388a5-cursor-completed-the-m7-real-acceptance-run-on-2026-07-16-using-.md", "base_sha256": null, "candidate_sha256": "20b9ef612f5d4bbfa3fefa323d64c68a72ab3888b0e90455b98d6ac43c90e0d4", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_c8181a6c545b74c2e642-experiment-1-rev-20b9ef612f5d.md", "base_path": null, "revision_history": [{"candidate_path": "vault/proposals/candidate-proposal_bundle_c8181a6c545b74c2e642-experiment-1.md", "candidate_sha256": "b83182040db7a221960b99c29f304007d1babbb3571c990966829e064e47e2b8", "reason": "补全 Cursor M7 验收步骤、Context Pack 边界、故障和结果，避免只保留 deterministic fallback 首句", "revised_at": "2026-07-16T22:19:28+08:00"}], "review_reason": "补全 Cursor M7 验收步骤、Context Pack 边界、故障和结果，避免只保留 deterministic fallback 首句", "working_path": "vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md", "working_at": "2026-07-17T11:59:33+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_113d589e6dadf14b5fa8edea"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "primary", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Session receipt: M7 Cursor real acceptance

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_beed2aa2edcb076d1706db84`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型标记或保留第一段逐字材料，不补齐无意义对象。

## Items and diffs

### experiment-1 (create experiment)

```diff
--- /dev/null
+++ candidate:vault/action/experiments/experiment_7101e03fb065226e65f388a5-cursor-completed-the-m7-real-acceptance-run-on-2026-07-16-using-.md
@@ -0,0 +1,19 @@
+---
+id: "experiment_7101e03fb065226e65f388a5"
+type: "experiment"
+status: "proposal"
+title: "Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval."
+created_at: "2026-07-16T22:16:57+08:00"
+updated_at: "2026-07-16T22:16:57+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_113d589e6dadf14b5fa8edea"]
+relations: [{"type": "derived_from", "target_id": "source_113d589e6dadf14b5fa8edea", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_113d589e6dadf14b5fa8edea"
+---
+
+# Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval.
+
+Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval.
```

## Item revision: experiment-1

- Reason: 补全 Cursor M7 验收步骤、Context Pack 边界、故障和结果，避免只保留 deterministic fallback 首句

```diff
--- previous-candidate
+++ revised-candidate
@@ -2,18 +2,41 @@
 id: "experiment_7101e03fb065226e65f388a5"
 type: "experiment"
 status: "proposal"
-title: "Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval."
+title: "Cursor M7 真实读取与 receipt 回写验收"
 created_at: "2026-07-16T22:16:57+08:00"
 updated_at: "2026-07-16T22:16:57+08:00"
 aliases: []
-tags: []
-domains: []
-confidence: "unknown"
+tags: ["m7", "agent-acceptance", "cursor"]
+domains: ["global-memory"]
+confidence: "high"
 source_ids: ["source_113d589e6dadf14b5fa8edea"]
-relations: [{"type": "derived_from", "target_id": "source_113d589e6dadf14b5fa8edea", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
-change_reason: "compile bundle from source_113d589e6dadf14b5fa8edea"
+relations: [{"type": "derived_from", "target_id": "source_113d589e6dadf14b5fa8edea", "reason": "由 Cursor M7 acceptance receipt 提出", "confidence": "high", "created_by": "cursor-acceptance-review", "status": "proposal"}]
+change_reason: "补全真实验收步骤、Context Pack 边界、故障和结果，避免只保留 deterministic fallback 的首句"
 ---
 
-# Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval.
+# Cursor M7 真实读取与 receipt 回写验收
 
-Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval.
+## 验收路径
+
+Cursor 按协议读取了 `AGENTS.md`、`.cursor/rules/global-memory.mdc` 和 `vault/INDEX.md`，随后执行 `gm maintain` 与 `gm context`（通过 `python -m global_memory`，因 PowerShell 将 `gm` 别名为 `Get-Member`）。任务是从限定 Context Pack 回答 VIA 实验结论和适用边界，没有扫描整个 vault，也没有直接修改 canonical。
+
+## Context Pack 结果
+
+- 查询成功返回 1 项、0 省略、预算未耗尽。
+- 选中的是先前 Codex M7 验收 receipt（`source_46d0aad5afd18dd21899796f`），而非 confirmed VIA claim 或论文 source。
+- 证据边界为 second-hand：答案来自 receipt 中对 VIA 的摘要，缺少 claim ID 与论文 source ID 的直接链接。
+
+## 任务回答（受 receipt 内容约束）
+
+- 主要结论：VIA 在六项 robosuite 仿真任务中通过 browser visual/tool interface 实现 zero-shot closed-loop manipulation；最小提示总体成功率 60%–88%；CC-Fable 在三项 LIBERO-Goal 任务 29/30、Rainbow 100%。
+- 适用边界：仅限仿真、多为 quasi-static 任务、每配置 ten seeds、主设置 cross-episode memory disabled。
+- 不能从论文推出：真实机器人部署、动态控制、长期记忆、持续学习、替代通用 robot-control policy。
+
+## 发现的问题
+
+- PowerShell `gm` 别名冲突，需使用 `.\scripts\gm.ps1` 或 `python -m global_memory`。
+- Context Pack 检索可能回归或排序问题：完整 VIA 查询返回 Codex receipt 而非 VIA claim/source（与 Codex 修复后报告不一致）。
+
+## 决定
+
+Cursor read → task → receipt → proposal 路径已执行。未编辑或批准 canonical。该结论仍是 pending experiment proposal；是否进入 canonical 由用户审阅决定。
```
