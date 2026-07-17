---
id: "proposal_ed15e3a6bc9d3a320d6ce246"
type: "proposal"
status: "migrated"
title: "修订：模型提议：Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点"
created_at: "2026-07-15T14:27:48+08:00"
updated_at: "2026-07-17T12:00:37+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: [{"type": "supersedes", "target_id": "proposal_2c7561e3342ca73fe93ee396", "reason": "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"}]
proposal_kind: "knowledge_revision"
processor: "human-candidate-revision-v1"
action: "create"
target_id: "claim_agentic_vla_one_shot_20260715"
target_path: "vault/knowledge/claims/claim_agentic_vla_one_shot_20260715-agentic-vla-在-libero-one-shot-设定下平均成功率-70-5-相对-openvla-oft-sft-基.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_ed15e3a6bc9d3a320d6ce246.md"
candidate_sha256: "f969f6b79b1e9749ccb64e7842db6338815162da3433ea7950efdf382495b19c"
change_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
revision_of: "proposal_2c7561e3342ca73fe93ee396"
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# 修订：模型提议：Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点

## 修订说明

- 被替代 proposal：`proposal_2c7561e3342ca73fe93ee396`
- 修订理由：人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份
- 建议操作：`create` `vault/knowledge/claims/claim_agentic_vla_one_shot_20260715-agentic-vla-在-libero-one-shot-设定下平均成功率-70-5-相对-openvla-oft-sft-基.md`
- 原 candidate 保持不可变；本 proposal 使用新的 candidate。

## Base → Revised Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_agentic_vla_one_shot_20260715-agentic-vla-在-libero-one-shot-设定下平均成功率-70-5-相对-openvla-oft-sft-基.md
@@ -0,0 +1,26 @@
+---
+id: "claim_agentic_vla_one_shot_20260715"
+type: "claim"
+status: "proposal"
+title: "Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["vla", "one-shot", "libero"]
+domains: ["robot-learning"]
+confidence: "medium"
+source_ids: ["source_2c21320690e566fbbf80fd75"]
+relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["每任务 1 demo SFT 预训练", "LIBERO 四套件"]
+uncertainty: "摘要 +28.5% 与 Table 2 +26.9% 不一致，批准时以 Table 2 为准。"
+evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7-8 页 Table 2", "excerpt": "Agentic-VLA 70.5 ... OpenVLA-OFT 43.6 ... Δ vs. SFT +26.9", "stance": "supports", "reason": "Table 2 one-shot 对比。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Section 4.3", "excerpt": "only a single demonstration per task is available for SFT pre-training", "stance": "context", "reason": "one-shot 协议。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "+28.5% in 1-shot learning", "stance": "context", "reason": "与 Table 2 数字差异，待核对。"}]
+---
+
+# Agentic-VLA 的 one-shot 结果
+
+在每个任务仅使用一条 demonstration 做 SFT pre-training 的设定下，Agentic-VLA 在 LIBERO 四套件上的平均成功率为 70.5%，OpenVLA-OFT 为 43.6%，Table 2 给出的差值是 26.9 个百分点；相对 EVOLVE-VLA 的 61.3% 提高 9.2 个百分点。
+
+论文摘要同时写作 `+28.5% in 1-shot learning`，与 Table 2 的 26.9 个百分点不一致。当前主张采用可直接复算的 Table 2 数字，并保留摘要差异等待作者版本更新或进一步解释。
```
