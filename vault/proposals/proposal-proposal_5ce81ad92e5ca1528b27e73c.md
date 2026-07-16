---
id: "proposal_5ce81ad92e5ca1528b27e73c"
type: "proposal"
status: "superseded"
title: "模型提议：该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住"
created_at: "2026-07-15T18:11:29+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_embodied_eval_bottleneck_20260715"
target_path: "vault/knowledge/claims/claim_wechat_embodied_eval_bottleneck_20260715-该文称具身-vla-迭代速度常被真机评估流程而非训练本身卡住.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5ce81ad92e5ca1528b27e73c.md"
candidate_sha256: "7b419f9b5692e164a8517895eb9ed50882bf9dd3ea00f96f2d57343c62d1cb11"
change_reason: "导入 claim_wechat_embodied_eval_bottleneck_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_2d4f3a7d3525782c8ff503ee", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "uncertainty": "公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_2d4f3a7d3525782c8ff503ee`
- Input SHA-256：`2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e`
- 不确定性：公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。
- 提议理由：导入 claim_wechat_embodied_eval_bottleneck_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_embodied_eval_bottleneck_20260715-该文称具身-vla-迭代速度常被真机评估流程而非训练本身卡住.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_embodied_eval_bottleneck_20260715"
+title: "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住"
+tags: ["real-robot", "evaluation", "vla"]
+domains: ["robotics", "robot-learning"]
+confidence: "medium"
+applicability: ["作者描述的具身 VLA 真机评测流程", "需要排队、人工摆场、逐次记录的场景"]
+uncertainty: "来自作者基于行业经验的论断，未给出量化对比实验；「一两天出分」为顺利情况下的经验描述。"
+evidence: [{"evidence_id": "ev_597", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 597, "span_end": 677, "original_text": "具身的 VLA 训完一版，想知道行不行，得提交给真机评测团队，先排队，再由人一件件把测试道具摆到场地上，守着机器人一遍遍跑、一次次记，顺利的话一两天后才出个分。", "section": "真机评测流程", "stance": "supports", "verification_status": "verified", "reason": "作者对评估流程耗时的具体描述。"}, {"evidence_id": "ev_692", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 692, "span_end": 718, "original_text": "迭代速度，很多时候不是被训练卡住的，是被评估卡住的。", "section": "瓶颈判断", "stance": "supports", "verification_status": "verified", "reason": "作者对瓶颈来源的判断句。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T18:12:00+08:00"
+updated_at: "2026-07-15T18:12:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入微信文章知识；等待人工核验"
+source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
+relations: [{"type": "derived_from", "target_id": "source_2d4f3a7d3525782c8ff503ee", "reason": "由微信公众号评论文章归纳；非独立 peer-reviewed 论文正文"}]
+---
+
+# 评估瓶颈
+
+真机评测排队与人工摆场使迭代受评估而非训练限制。
```
