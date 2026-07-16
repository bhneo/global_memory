---
id: "proposal_5172af061fedb7539fc7129d"
type: "proposal"
status: "pending"
title: "模型提议：该文转述 2015 年实验：志愿者互相直视 10 分钟后报告「前所未有的强烈感受」"
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
target_id: "claim_wechat_mutual_gaze_2015_20260715"
target_path: "vault/knowledge/claims/claim_wechat_mutual_gaze_2015_20260715-该文转述-2015-年实验-志愿者互相直视-10-分钟后报告-前所未有的强烈感受.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5172af061fedb7539fc7129d.md"
candidate_sha256: "1cd42e0ab0f9bc3839d5dc13bf33e844ba5d45de779737b64d79070931b01824"
change_reason: "导入 claim_wechat_mutual_gaze_2015_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_12432807660136b2471717f1", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "uncertainty": "利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文转述 2015 年实验：志愿者互相直视 10 分钟后报告「前所未有的强烈感受」

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_12432807660136b2471717f1`
- Input SHA-256：`05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b`
- 不确定性：利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。
- 提议理由：导入 claim_wechat_mutual_gaze_2015_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_mutual_gaze_2015_20260715-该文转述-2015-年实验-志愿者互相直视-10-分钟后报告-前所未有的强烈感受.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_mutual_gaze_2015_20260715"
+title: "该文转述 2015 年实验：志愿者互相直视 10 分钟后报告「前所未有的强烈感受」"
+tags: ["mutual-gaze", "perception", "psychology"]
+domains: ["psychology", "neuroscience"]
+confidence: "low"
+applicability: ["2015 年互相直视实验", "英国心理学会 Research Digest 报道转述"]
+uncertainty: "文内自述「不是一门严谨的科学」；具体实验设计、样本量与原论文未在文中给出；仅经 Research Digest 二次报道。"
+evidence: [{"evidence_id": "ev_1530", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1530, "span_end": 1585, "original_text": "有趣的是，研究人员在2015年的一项实验中也证明了类似的效果，当时他们让志愿者互相直视对方的眼睛保持10分钟。", "section": "2015 实验设定", "stance": "supports", "verification_status": "verified", "reason": "文内对实验的基本描述。"}, {"evidence_id": "ev_1606", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1606, "span_end": 1707, "original_text": "“参与了对视实验的人说，他们产生了前所未有的强烈感受，”克里斯蒂安·贾勒特（Christian Jarrett）在当时发表在英国心理学会《研究文摘》（Research Digest）上的报告中如此提到。", "section": "参与者报告", "stance": "supports", "verification_status": "verified", "reason": "文内引述 Research Digest 报道。"}, {"evidence_id": "ev_1817", "evidence_kind": "quote", "source_id": "source_12432807660136b2471717f1", "content_id": "content_05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "extraction_id": "extraction_b2b09f628e4a2fab15043dd6", "input_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "span_start": 1817, "span_end": 1855, "original_text": "当然，这不是一门严谨的科学，因为每个人的大脑都会对奇怪的东西产生不一样的反应", "section": "证据边界", "stance": "supports", "verification_status": "verified", "reason": "文内对实验严谨性的自我限定。"}]
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
+# 2015 对视实验
+
+10 分钟互相直视后参与者报告强烈 unusual 感受。
```
