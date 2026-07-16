---
id: "proposal_511c1f3b3e1ef2b94402aa6b"
type: "proposal"
status: "pending"
title: "模型提议：该文称甘兹菲尔德效应下，大脑会在均匀感官剥夺场中放大神经元噪音以补偿缺失视觉信号"
created_at: "2026-07-15T18:28:51+08:00"
updated_at: "2026-07-15T18:28:51+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_12432807660136b2471717f1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_ganzfeld_mechanism_20260715"
target_path: "vault/knowledge/claims/claim_wechat_ganzfeld_mechanism_20260715-该文称甘兹菲尔德效应下-大脑会在均匀感官剥夺场中放大神经元噪音以补偿缺失视觉信号.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_511c1f3b3e1ef2b94402aa6b.md"
candidate_sha256: "bd829e26b27f2702ae1a637d13db41cbfad19e90bc7afde2516687d2ead3102a"
change_reason: "导入 claim_wechat_ganzfeld_mechanism_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_12432807660136b2471717f1", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "uncertainty": "利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称甘兹菲尔德效应下，大脑会在均匀感官剥夺场中放大神经元噪音以补偿缺失视觉信号

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_12432807660136b2471717f1`
- Input SHA-256：`05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b`
- 不确定性：利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。
- 提议理由：导入 claim_wechat_ganzfeld_mechanism_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_ganzfeld_mechanism_20260715-该文称甘兹菲尔德效应下-大脑会在均匀感官剥夺场中放大神经元噪音以补偿缺失视觉信号.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_ganzfeld_mechanism_20260715"
+title: "该文称甘兹菲尔德效应下，大脑会在均匀感官剥夺场中放大神经元噪音以补偿缺失视觉信号"
+tags: ["ganzfeld-effect", "sensory-deprivation", "neuroscience"]
+domains: ["neuroscience", "psychology"]
+confidence: "medium"
+applicability: ["2016 Scam Nation YouTube 演示的 DIY 感官剥夺设定", "眼前漆黑且持续听到电视白噪音的非结构化刺激场"]
+uncertainty: "机制描述来自科普译文对甘兹菲尔德效应的通俗解释，未引用原始实验论文；ScienceAlert 原文未 capture。"
+evidence: [{"evidence_id": "ev_1138", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1138, "span_end": 1163, "original_text": "你的大脑会通过放大神经元噪音来寻找缺失的视觉信号。", "section": "甘兹菲尔德机制", "stance": "supports", "verification_status": "verified", "reason": "文内对大脑补偿缺失视觉信号机制的描述。"}, {"evidence_id": "ev_1164", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1164, "span_end": 1199, "original_text": "这就会造成我们在视频里看到的那样，人们产生了视力上和听力上的双重幻觉。", "section": "效应结果", "stance": "supports", "verification_status": "verified", "reason": "作者对效应后果的归纳。"}, {"evidence_id": "evp_82629", "evidence_kind": "paraphrase", "source_id": "source_12432807660136b2471717f1", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "section": "效应名称", "interpretation": "文内将上述现象称为甘兹菲尔德效应（Ganzfeld effect）", "stance": "context", "verification_status": "verified", "reason": "补充效应名称与来源说明。"}]
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
+# 甘兹菲尔德效应
+
+均匀感官剥夺下，大脑放大神经噪音并可能诱发视听幻觉。
```
