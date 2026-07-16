---
id: "proposal_f0451612aafa346fb4579465"
type: "proposal"
status: "superseded"
title: "模型提议：该文描述 Scam Nation 演示可用白纸、棉填充、白噪音视频等家用物品在约 10–30 分钟后诱发强烈幻觉"
created_at: "2026-07-15T18:28:51+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_12432807660136b2471717f1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_scam_nation_diy_setup_20260715"
target_path: "vault/knowledge/claims/claim_wechat_scam_nation_diy_setup_20260715-该文描述-scam-nation-演示可用白纸-棉填充-白噪音视频等家用物品在约-10-30-分钟后诱发强烈幻觉.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f0451612aafa346fb4579465.md"
candidate_sha256: "18039d10d97f6ee30e3c6d5e80ab31e9d51995dd49eace688e481d19f67d8a7e"
change_reason: "导入 claim_wechat_scam_nation_diy_setup_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_12432807660136b2471717f1", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "uncertainty": "利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文描述 Scam Nation 演示可用白纸、棉填充、白噪音视频等家用物品在约 10–30 分钟后诱发强烈幻觉

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_12432807660136b2471717f1`
- Input SHA-256：`05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b`
- 不确定性：利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。
- 提议理由：导入 claim_wechat_scam_nation_diy_setup_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_scam_nation_diy_setup_20260715-该文描述-scam-nation-演示可用白纸-棉填充-白噪音视频等家用物品在约-10-30-分钟后诱发强烈幻觉.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_scam_nation_diy_setup_20260715"
+title: "该文描述 Scam Nation 演示可用白纸、棉填充、白噪音视频等家用物品在约 10–30 分钟后诱发强烈幻觉"
+tags: ["sensory-deprivation", "diy-experiment", "hallucination"]
+domains: ["psychology", "neuroscience"]
+confidence: "low"
+applicability: ["2016 Scam Nation YouTube 视频演示", "至少 30 分钟不间断白噪音/静电干扰音"]
+uncertainty: "效果时间窗与具体幻觉内容来自视频参与者自述，非对照实验；「只能采信视频中二人的说法」为文内自述。"
+evidence: [{"evidence_id": "ev_562", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 562, "span_end": 654, "original_text": "正如2016年Scam Nation频道在YouTube上发布的一段视频所演示的那样，如果用一些常见的家用物品制造出一种高度感官剥夺的情景，你就会产生足以扰乱你的视觉和听觉的强烈幻觉。", "section": "Scam Nation 演示", "stance": "supports", "verification_status": "verified", "reason": "文内对视频目的与效果的概述。"}, {"evidence_id": "ev_802", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 802, "span_end": 820, "original_text": "效果通常在10到30分钟后体现出来。", "section": "时间窗", "stance": "supports", "verification_status": "verified", "reason": "文内给出的典型起效时间。"}, {"evidence_id": "ev_989", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 989, "span_end": 1016, "original_text": "当然，就这个特定场景而言，我们只能采信视频中二人的说法", "section": "证据边界", "stance": "supports", "verification_status": "verified", "reason": "文内对证据强度的自我限定。"}]
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
+# Scam Nation DIY
+
+家用感官剥夺约 10–30 分钟可报告强烈视听扰动。
```
