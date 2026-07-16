---
id: "proposal_10c6a97cc381d2200ed04c94"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 Veritasium 主持人在 45 分钟漆黑静音房间中主要体验到心脏搏动感被放大，而非完整幻觉"
created_at: "2026-07-15T18:28:51+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_12432807660136b2471717f1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_veritasium_sensory_deprivation_20260715"
target_path: "vault/knowledge/claims/claim_wechat_veritasium_sensory_deprivation_20260715-该文称-veritasium-主持人在-45-分钟漆黑静音房间中主要体验到心脏搏动感被放大-而非完整幻觉.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_10c6a97cc381d2200ed04c94.md"
candidate_sha256: "1fcd056ed4edb77cbfbb9cf8693a56a2f611c3597f64291347c1fe51c8bd8a32"
change_reason: "导入 claim_wechat_veritasium_sensory_deprivation_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_12432807660136b2471717f1", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "uncertainty": "利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 Veritasium 主持人在 45 分钟漆黑静音房间中主要体验到心脏搏动感被放大，而非完整幻觉

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_12432807660136b2471717f1`
- Input SHA-256：`05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b`
- 不确定性：利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。
- 提议理由：导入 claim_wechat_veritasium_sensory_deprivation_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_veritasium_sensory_deprivation_20260715-该文称-veritasium-主持人在-45-分钟漆黑静音房间中主要体验到心脏搏动感被放大-而非完整幻觉.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_veritasium_sensory_deprivation_20260715"
+title: "该文称 Veritasium 主持人在 45 分钟漆黑静音房间中主要体验到心脏搏动感被放大，而非完整幻觉"
+tags: ["sensory-deprivation", "interoception"]
+domains: ["neuroscience", "psychology"]
+confidence: "medium"
+applicability: ["Veritasium 频道德里克·穆勒的感官剥夺试验", "45 分钟漆黑、极度安静且无回音房间"]
+uncertainty: "体验报告来自科普视频转述；文内称「并不完全是幻觉」，属主观感受描述。"
+evidence: [{"evidence_id": "ev_1230", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1230, "span_end": 1360, "original_text": "当“真理元素”频道（Veritasium）的主持人德里克·穆勒（Derek Muller）用他自己的方式试验“感官剥夺”时——他把自己关在一个漆黑、极度安静并且没有回音的房间里45分钟——他破除了“丧失刺激致人疯狂”的传言，但同时也表明确实会有一些奇怪的感受。", "section": "Veritasium 试验设定", "stance": "supports", "verification_status": "verified", "reason": "文内对试验条件与部分结论的描述。"}, {"evidence_id": "ev_1361", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1361, "span_end": 1390, "original_text": "“或许我注意到的最奇怪的事情就是对自己心脏的感觉，”他说。", "section": "心脏感受", "stance": "supports", "verification_status": "verified", "reason": "穆勒对最显著体验的直接引语。"}, {"evidence_id": "ev_1470", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1470, "span_end": 1529, "original_text": "在这种情况下，德里克体验到的并不完全是幻觉，但是他所描述的心脏的感受说明他的大脑确实在缺乏刺激的情况下放大了某些感受。", "section": "作者解读", "stance": "supports", "verification_status": "verified", "reason": "文内对体验性质的判断。"}]
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
+# Veritasium 感官剥夺
+
+45 分钟静音暗室中主要报告内感受（心跳）被放大。
```
