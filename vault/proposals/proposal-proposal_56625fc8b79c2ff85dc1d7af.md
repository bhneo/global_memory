---
id: "proposal_56625fc8b79c2ff85dc1d7af"
type: "proposal"
status: "superseded"
title: "模型提议：该文引 No free lunch 称神经网络虽具通用近似能力，但并非适合所有任务，泛化至未见环境是关键"
created_at: "2026-07-16T01:31:08+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_68161c78067d7b4add05ba1a"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_wangjun_no_free_lunch_generalization_20260716"
target_path: "vault/knowledge/claims/claim_wechat_wangjun_no_free_lunch_generalization_20260716-该文引-no-free-lunch-称神经网络虽具通用近似能力-但并非适合所有任务-泛化至未见环境是关键.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_56625fc8b79c2ff85dc1d7af.md"
candidate_sha256: "b048c0ecbdaa57b1c008e33424af7f9eb2cd05d7c97ffe4657ad598b21ef85bf"
change_reason: "导入 claim_wechat_wangjun_no_free_lunch_generalization_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_68161c78067d7b4add05ba1a", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "uncertainty": "2023 演讲整理；IIT/意识主张为理论观点，非共识事实。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文引 No free lunch 称神经网络虽具通用近似能力，但并非适合所有任务，泛化至未见环境是关键

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_68161c78067d7b4add05ba1a`
- Input SHA-256：`9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45`
- 不确定性：2023 演讲整理；IIT/意识主张为理论观点，非共识事实。
- 提议理由：导入 claim_wechat_wangjun_no_free_lunch_generalization_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_wangjun_no_free_lunch_generalization_20260716-该文引-no-free-lunch-称神经网络虽具通用近似能力-但并非适合所有任务-泛化至未见环境是关键.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_wangjun_no_free_lunch_generalization_20260716"
+title: "该文引 No free lunch 称神经网络虽具通用近似能力，但并非适合所有任务，泛化至未见环境是关键"
+tags: ["no-free-lunch", "generalization", "universal-approximation"]
+domains: ["machine-learning", "learning-theory"]
+confidence: "medium"
+applicability: ["通用近似定理与 NFL 对照讨论", "变化环境适应语境"]
+uncertainty: "为标准 ML 理论科普化表述；与具体架构能力边界需细分。"
+evidence: [{"evidence_id": "ev_1457", "evidence_kind": "quote", "source_id": "source_68161c78067d7b4add05ba1a", "content_id": "content_9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "extraction_id": "extraction_fe8826e067e84de0741c77af", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "span_start": 1457, "span_end": 1606, "original_text": "No free lunch」理论，我们在用神经网络或其他功能进行学习时，它对有些任务拟合得非常好。但是在有先验知识的情况下，如果拟合符合当前的先验知识，你必然能找到一类或一个任务无法学习。也就是说，虽然神经网络具有普适性且逼近如何拟合，但它并不适合所有任务。在有些任务上成功必然会在另一些任务上失败", "section": "NFL 定理", "stance": "supports", "verification_status": "verified", "reason": "文内对 No free lunch 的说明。"}, {"evidence_id": "ev_1682", "evidence_kind": "quote", "source_id": "source_68161c78067d7b4add05ba1a", "content_id": "content_9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "extraction_id": "extraction_fe8826e067e84de0741c77af", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "span_start": 1682, "span_end": 1719, "original_text": "泛化性，如果无法泛化到一个以前没有见过的环境，它的学习能力显然也是有限制的", "section": "泛化要求", "stance": "supports", "verification_status": "verified", "reason": "文内对泛化至新环境的强调。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:30:00+08:00"
+updated_at: "2026-07-16T01:30:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入汪军机器意识演讲；等待人工核验"
+source_ids: ["source_68161c78067d7b4add05ba1a"]
+relations: [{"type": "derived_from", "target_id": "source_68161c78067d7b4add05ba1a", "reason": "由机器之心对 UCL 汪军 2023 AI 科技年会演讲整理归纳；非原始讲稿 capture"}]
+---
+
+# NFL 与泛化
+
+普适近似≠所有任务；泛化是智能关键。
```
