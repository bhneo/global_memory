---
id: "proposal_3db9cf4df6cccb6bb393d3f1"
type: "proposal"
status: "pending"
title: "模型提议：该文转述 Scam Nation 参与者在约 20 分钟后报告彩色光斑并形成恐龙、水母等形状幻觉"
created_at: "2026-07-15T18:28:51+08:00"
updated_at: "2026-07-15T18:28:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_12432807660136b2471717f1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_scam_nation_visuals_20260715"
target_path: "vault/knowledge/claims/claim_wechat_scam_nation_visuals_20260715-该文转述-scam-nation-参与者在约-20-分钟后报告彩色光斑并形成恐龙-水母等形状幻觉.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_3db9cf4df6cccb6bb393d3f1.md"
candidate_sha256: "19ed0361b26d497bc87cb919b11596dc7952b6a529213d3d0a5ef2d123101912"
change_reason: "导入 claim_wechat_scam_nation_visuals_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_12432807660136b2471717f1", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "uncertainty": "利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文转述 Scam Nation 参与者在约 20 分钟后报告彩色光斑并形成恐龙、水母等形状幻觉

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_12432807660136b2471717f1`
- Input SHA-256：`05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b`
- 不确定性：利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。
- 提议理由：导入 claim_wechat_scam_nation_visuals_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_scam_nation_visuals_20260715-该文转述-scam-nation-参与者在约-20-分钟后报告彩色光斑并形成恐龙-水母等形状幻觉.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_scam_nation_visuals_20260715"
+title: "该文转述 Scam Nation 参与者在约 20 分钟后报告彩色光斑并形成恐龙、水母等形状幻觉"
+tags: ["hallucination", "visual-perception"]
+domains: ["psychology"]
+confidence: "low"
+applicability: ["Scam Nation 节目 20 分钟节点", "两名视频参与者的自述"]
+uncertainty: "具体视觉内容（恐龙剪影、水母、索伦之眼）为参与者口述，无独立测量；一人报告尖叫、另一人报告笑声，个体差异大。"
+evidence: [{"evidence_id": "ev_821", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 821, "span_end": 855, "original_text": "实验进行20分钟后，参与Scam Nation节目的人说，他们看到了", "section": "视觉幻觉自述", "stance": "supports", "verification_status": "verified", "reason": "文内对 20 分钟节点视觉体验转述的起始句。"}, {"evidence_id": "ev_943", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 943, "span_end": 963, "original_text": "其中之一听到尖叫声，而另一个人听到笑声。", "section": "听觉差异", "stance": "supports", "verification_status": "verified", "reason": "文内对两名参与者听觉体验差异的描述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T18:23:00+08:00"
+updated_at: "2026-07-15T18:23:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入微信科普译文；等待人工核验"
+source_ids: ["source_12432807660136b2471717f1"]
+relations: [{"type": "derived_from", "target_id": "source_12432807660136b2471717f1", "reason": "由利维坦转载的 ScienceAlert 科普译文归纳；非原始研究论文"}]
+---
+
+# Scam Nation 视觉/听觉
+
+20 分钟后参与者自述彩色光斑与成形幻觉。
```
