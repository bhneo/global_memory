---
id: "proposal_78599f5a7f6c86aa89458fe5"
type: "proposal"
status: "superseded"
title: "模型提议：该文称「粘液手错觉」是橡胶手幻觉变种：同步捏扯真手与假手可诱发假手归属感"
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
target_id: "claim_wechat_rubber_hand_slime_variant_20260715"
target_path: "vault/knowledge/claims/claim_wechat_rubber_hand_slime_variant_20260715-该文称-粘液手错觉-是橡胶手幻觉变种-同步捏扯真手与假手可诱发假手归属感.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_78599f5a7f6c86aa89458fe5.md"
candidate_sha256: "f1b076cd8bd5a869da61b272e978a656860f7ae3180dcdee20946c14a62d040e"
change_reason: "导入 claim_wechat_rubber_hand_slime_variant_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_046487376d500224386ff628", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "uncertainty": "科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称「粘液手错觉」是橡胶手幻觉变种：同步捏扯真手与假手可诱发假手归属感

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_046487376d500224386ff628`
- Input SHA-256：`591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7`
- 不确定性：科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。
- 提议理由：导入 claim_wechat_rubber_hand_slime_variant_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_rubber_hand_slime_variant_20260715-该文称-粘液手错觉-是橡胶手幻觉变种-同步捏扯真手与假手可诱发假手归属感.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_rubber_hand_slime_variant_20260715"
+title: "该文称「粘液手错觉」是橡胶手幻觉变种：同步捏扯真手与假手可诱发假手归属感"
+tags: ["rubber-hand-illusion", "body-ownership", "perception"]
+domains: ["psychology", "neuroscience"]
+confidence: "medium"
+applicability: ["镜子遮挡真手与粘液手的演示设定", "同步触觉刺激条件"]
+uncertainty: "文内称错觉未必每次成功且不一定影响所有人；非 peer-reviewed 实验报告。"
+evidence: [{"evidence_id": "ev_1164", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 1164, "span_end": 1237, "original_text": "一面镜子遮挡住了被试者的真手和粘液手，粘液手放在被试者的眼前，真手则完全被隔开：\n然后捏扯真手的同时，也用同样的方式捏扯粘液手，两边动作同步进行。", "section": "实验设置", "stance": "supports", "verification_status": "verified", "reason": "文内对粘液手错觉装置与同步操作的描述。"}, {"evidence_id": "ev_1285", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 1285, "span_end": 1377, "original_text": "这是错觉「橡胶手幻觉」的变种尝试。「橡胶手幻觉」就是用一个挡板隔开假手和真手，然后同时抚摸假手和真手，一般都用刷子轻轻接触：\n如果动作同步且方向相同，被试者也会把橡胶手当作自己的真手。", "section": "橡胶手机制", "stance": "supports", "verification_status": "verified", "reason": "文内对经典橡胶手幻觉机制的解释。"}, {"evidence_id": "ev_1415", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 1415, "span_end": 1441, "original_text": "当然，这是错觉未必每次都会成功，也不一定能影响所有人", "section": "适用边界", "stance": "supports", "verification_status": "verified", "reason": "文内对效应稳定性的限定。"}]
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
+# 粘液手 / 橡胶手
+
+同步触觉可诱发假手归属感；效应因人而异。
```
