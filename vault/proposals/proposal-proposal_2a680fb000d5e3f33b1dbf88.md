---
id: "proposal_2a680fb000d5e3f33b1dbf88"
type: "proposal"
status: "approved"
title: "更新 来自《quickstart-note.md》的待确认主张"
created_at: "2026-07-15T11:52:03+08:00"
updated_at: "2026-07-15T11:52:30+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_b361ac9cddb531dba17c360e"]
relations: []
proposal_kind: "knowledge_update"
processor: "explicit-candidate-v1"
action: "update"
target_id: "claim_7f62757ed57fd38ba06e3309"
target_path: "vault/knowledge/claims/claim_7f62757ed57fd38ba06e3309-quickstart-note-md.md"
base_path: "vault/proposals/base-proposal_2a680fb000d5e3f33b1dbf88.md"
base_sha256: "6e849b26a67ebbd79f09ca27b7b8db3b2a3cbbd241716b67f90f5f3d5ea98991"
candidate_path: "vault/proposals/candidate-proposal_2a680fb000d5e3f33b1dbf88.md"
candidate_sha256: "ead1dde1da2f0671186f8da7647871b32d96fc0d592edc7c3932303a08cd8d4e"
change_reason: "移除首轮端到端验收测试 claim，不再作为有效知识；保留 raw 与审计历史"
reviewed_at: "2026-07-15T11:52:30+08:00"
review_reason: "人工通过 CLI 明确批准"
---

# 更新 来自《quickstart-note.md》的待确认主张

## 更新说明

- Target：`claim_7f62757ed57fd38ba06e3309`
- Base SHA-256：`6e849b26a67ebbd79f09ca27b7b8db3b2a3cbbd241716b67f90f5f3d5ea98991`
- Candidate SHA-256：`ead1dde1da2f0671186f8da7647871b32d96fc0d592edc7c3932303a08cd8d4e`
- 变更理由：移除首轮端到端验收测试 claim，不再作为有效知识；保留 raw 与审计历史
- 并发策略：审批时 target 必须仍等于 base；不自动合并。

## Base → Candidate Diff

```diff
--- base:vault/knowledge/claims/claim_7f62757ed57fd38ba06e3309-quickstart-note-md.md
+++ candidate:vault/knowledge/claims/claim_7f62757ed57fd38ba06e3309-quickstart-note-md.md
@@ -1,34 +1,24 @@
 ---
 id: "claim_7f62757ed57fd38ba06e3309"
 type: "claim"
-status: "confirmed"
-title: "来自《quickstart-note.md》的待确认主张"
+status: "proposal"
+proposed_status: "archived"
+title: "归档：quickstart 端到端验收测试主张"
 created_at: "2026-07-14T17:09:53+08:00"
 updated_at: "2026-07-14T17:09:53+08:00"
 aliases: []
-tags: []
+tags: ["test-fixture"]
 domains: []
 confidence: "unknown"
 source_ids: ["source_b361ac9cddb531dba17c360e"]
-relations: [{"type": "derived_from", "target_id": "source_b361ac9cddb531dba17c360e", "reason": "由该原始来源的规则编译结果提出"}]
+relations: [{"type": "derived_from", "target_id": "source_b361ac9cddb531dba17c360e", "reason": "由初始 quickstart 验收 source 的规则编译结果产生"}]
 superseded_by: null
 valid_during: null
-change_reason: "人工批准 proposal proposal_1f3f00a6c9298f264dec2820"
-approved_via: "proposal_1f3f00a6c9298f264dec2820"
+change_reason: "该对象仅用于首轮 capture → compile → approve → search 端到端验收，不属于需要长期保留在有效知识视图中的真实知识"
 ---
 
-# 来自《quickstart-note.md》的待确认主张
+# 归档：quickstart 端到端验收测试主张
 
-## 候选主张
+该 claim 是 Global Memory 第一轮端到端流程验证产生的测试对象，不是正式导入的长期知识，现归档退出有效知识视图。
 
-# 示例输入：为什么需要来源链 长期知识系统的价值不只在于快速返回答案，也在于答案可以回到当时保存的原文、时间和保存理由。索引可以重建，证据链不能凭空重建。
-
-## 证据与位置
-
-- 来源：[[vault/raw/files/source-source_b361ac9cddb531dba17c360e|source_b361ac9cddb531dba17c360e]]
-- 位置：正文开头（第一版规则编译器截取）
-- 证据方向：待人工判断支持或反对
-
-## 不确定性
-
-该内容由确定性规则生成，尚未经过模型解释或人工事实核验。批准仅表示纳入知识库，不自动将置信度提升为高。
+原始 source、candidate、proposal 与 approval 记录继续保留，用于验证来源链和审计历史；不得将其作为当前知识回答的依据。
```
