---
id: "proposal_7774948d25d0e3304ea582b5"
type: "proposal"
status: "superseded"
title: "模型提议：该文称双环错觉在边缘重叠时运动知觉会改变，但实际旋转方式未变"
created_at: "2026-07-15T21:30:14+08:00"
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
target_id: "claim_wechat_double_ring_illusion_20260715"
target_path: "vault/knowledge/claims/claim_wechat_double_ring_illusion_20260715-该文称双环错觉在边缘重叠时运动知觉会改变-但实际旋转方式未变.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_7774948d25d0e3304ea582b5.md"
candidate_sha256: "268572747000ffec563482be24eade747480c98c24faee018991d019f8974eef"
change_reason: "导入 claim_wechat_double_ring_illusion_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_046487376d500224386ff628", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "uncertainty": "科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称双环错觉在边缘重叠时运动知觉会改变，但实际旋转方式未变

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_046487376d500224386ff628`
- Input SHA-256：`591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7`
- 不确定性：科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。
- 提议理由：导入 claim_wechat_double_ring_illusion_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_double_ring_illusion_20260715-该文称双环错觉在边缘重叠时运动知觉会改变-但实际旋转方式未变.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_double_ring_illusion_20260715"
+title: "该文称双环错觉在边缘重叠时运动知觉会改变，但实际旋转方式未变"
+tags: ["optical-illusion", "motion-perception"]
+domains: ["psychology", "perception"]
+confidence: "medium"
+applicability: ["Dawei Bai 与 Brent Strickland 作品介绍", "两圆环旋转知觉实验"]
+uncertainty: "为演示性描述，未给出定量实验参数；「大多数人」为概括性说法。"
+evidence: [{"evidence_id": "ev_570", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 570, "span_end": 588, "original_text": "在大多数人眼中，它们似乎在原地转圈：", "section": "初始知觉", "stance": "supports", "verification_status": "verified", "reason": "文内对默认旋转知觉的描述。"}, {"evidence_id": "ev_589", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 589, "span_end": 649, "original_text": "然而，只要让它们的边缘发生重叠，视觉效果就会出现变动，仿佛是在来回弹跳，只转了一半，然后就转了回去，生怕相互触碰到一样。", "section": "重叠后知觉", "stance": "supports", "verification_status": "verified", "reason": "文内对重叠后弹跳式知觉变化的描述。"}, {"evidence_id": "ev_651", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 651, "span_end": 701, "original_text": "但其实圆圈的运转方式并没有改变，例如如果给其中一个圆圈开个洞，让对方可以穿过去，这种错觉也就消失了。", "section": "物理未变", "stance": "supports", "verification_status": "verified", "reason": "文内强调实际运动未改变的说明。"}]
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
+# 双环错觉
+
+重叠改变知觉，不改变真实旋转。
```
