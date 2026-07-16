---
id: "proposal_0904fd4e253b405f84e39954"
type: "proposal"
status: "superseded"
title: "模型提议：该文称「Oh La La 盒子」由两片纸片在特定角度观看可产生立方体错觉"
created_at: "2026-07-15T21:30:15+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_046487376d500224386ff628"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_oh_la_la_box_20260715"
target_path: "vault/knowledge/claims/claim_wechat_oh_la_la_box_20260715-该文称-oh-la-la-盒子-由两片纸片在特定角度观看可产生立方体错觉.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_0904fd4e253b405f84e39954.md"
candidate_sha256: "aa9252e74938ca3808c6bcd036b49bc8566953afae973025d39905ced2d0e1f7"
change_reason: "导入 claim_wechat_oh_la_la_box_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_046487376d500224386ff628", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "uncertainty": "科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称「Oh La La 盒子」由两片纸片在特定角度观看可产生立方体错觉

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_046487376d500224386ff628`
- Input SHA-256：`591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7`
- 不确定性：科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。
- 提议理由：导入 claim_wechat_oh_la_la_box_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_oh_la_la_box_20260715-该文称-oh-la-la-盒子-由两片纸片在特定角度观看可产生立方体错觉.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_oh_la_la_box_20260715"
+title: "该文称「Oh La La 盒子」由两片纸片在特定角度观看可产生立方体错觉"
+tags: ["optical-illusion", "3d-from-2d"]
+domains: ["perception"]
+confidence: "medium"
+applicability: ["Oh La La 盒子作品描述", "两纸片特定视角观看"]
+uncertainty: "仅为简短演示说明，未给出精确几何参数或作者信息。"
+evidence: [{"evidence_id": "ev_1032", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 1032, "span_end": 1058, "original_text": "乍一看，这是一个立方体。\n但其实它只是两个纸片而已：", "section": "立方体 vs 纸片", "stance": "supports", "verification_status": "verified", "reason": "文内对物体真实构成的对比。"}, {"evidence_id": "ev_1072", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 1072, "span_end": 1108, "original_text": "两个纸壳贴近后，只要找到一个特定的角度，就能创造出这样的错觉，非常巧妙。", "section": "观看角度", "stance": "supports", "verification_status": "verified", "reason": "文内对产生错觉所需视角条件的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T21:25:00+08:00"
+updated_at: "2026-07-15T21:25:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入视错觉科普；等待人工核验"
+source_ids: ["source_046487376d500224386ff628"]
+relations: [{"type": "derived_from", "target_id": "source_046487376d500224386ff628", "reason": "由中科院物理所转载的 2021 最佳视错觉大赛科普文章归纳；非原始实验论文"}]
+---
+
+# Oh La La 盒子
+
+两纸片特定角度产生立方体错觉。
```
