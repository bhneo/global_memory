---
id: "proposal_1f3f00a6c9298f264dec2820"
type: "proposal"
status: "approved"
title: "编译 quickstart-note.md"
created_at: "2026-07-14T17:09:53+08:00"
updated_at: "2026-07-14T17:09:53+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_b361ac9cddb531dba17c360e"]
relations: []
processor: "deterministic-excerpt-v1"
action: "create"
target_id: "claim_7f62757ed57fd38ba06e3309"
target_path: "vault/knowledge/claims/claim_7f62757ed57fd38ba06e3309-quickstart-note-md.md"
candidate_path: "vault/proposals/candidate-proposal_1f3f00a6c9298f264dec2820.md"
candidate_sha256: "63435a54e49f1162727e5ce48a163796b3c0b132d661a13db161c70a780e6372"
reviewed_at: "2026-07-14T17:09:53+08:00"
review_reason: "人工通过 CLI 明确批准"
---

# 编译 quickstart-note.md

## 编译说明

- 读取来源：[[vault/raw/files/source-source_b361ac9cddb531dba17c360e|source_b361ac9cddb531dba17c360e]]
- 建议操作：`create` `vault/knowledge/claims/claim_7f62757ed57fd38ba06e3309-quickstart-note-md.md`
- 矛盾：第一版规则处理器未自动判定，必须人工复核
- 原因：将来源开头转换为一个低置信度候选主张，验证审批闭环

## 内容级 Diff

```diff
--- /dev/null
+++ vault/knowledge/claims/claim_7f62757ed57fd38ba06e3309-quickstart-note-md.md
@@ -0,0 +1,33 @@
+---
+id: "claim_7f62757ed57fd38ba06e3309"
+type: "claim"
+status: "proposal"
+title: "来自《quickstart-note.md》的待确认主张"
+created_at: "2026-07-14T17:09:53+08:00"
+updated_at: "2026-07-14T17:09:53+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_b361ac9cddb531dba17c360e"]
+relations: [{"type": "derived_from", "target_id": "source_b361ac9cddb531dba17c360e", "reason": "由该原始来源的规则编译结果提出"}]
+superseded_by: null
+valid_during: null
+change_reason: "由规则编译器提出，等待人工核验"
+---
+
+# 来自《quickstart-note.md》的待确认主张
+
+## 候选主张
+
+# 示例输入：为什么需要来源链 长期知识系统的价值不只在于快速返回答案，也在于答案可以回到当时保存的原文、时间和保存理由。索引可以重建，证据链不能凭空重建。
+
+## 证据与位置
+
+- 来源：[[vault/raw/files/source-source_b361ac9cddb531dba17c360e|source_b361ac9cddb531dba17c360e]]
+- 位置：正文开头（第一版规则编译器截取）
+- 证据方向：待人工判断支持或反对
+
+## 不确定性
+
+该内容由确定性规则生成，尚未经过模型解释或人工事实核验。批准仅表示纳入知识库，不自动将置信度提升为高。
```
