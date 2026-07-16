---
id: "proposal_cdecaf71e3ed80af036ac9de"
type: "proposal"
status: "superseded"
title: "模型提议：该文引整合信息理论称传统前馈/Transformer 信息整合度为零，需反馈回路才可能有非零整合"
created_at: "2026-07-16T01:31:08+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_68161c78067d7b4add05ba1a"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_wangjun_iit_zero_integration_20260716"
target_path: "vault/knowledge/claims/claim_wechat_wangjun_iit_zero_integration_20260716-该文引整合信息理论称传统前馈-transformer-信息整合度为零-需反馈回路才可能有非零整合.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_cdecaf71e3ed80af036ac9de.md"
candidate_sha256: "05bd9693cb3b675919b8727e6c135245927c8518287dba41735dd97cf8fd736c"
change_reason: "导入 claim_wechat_wangjun_iit_zero_integration_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_68161c78067d7b4add05ba1a", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "uncertainty": "2023 演讲整理；IIT/意识主张为理论观点，非共识事实。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文引整合信息理论称传统前馈/Transformer 信息整合度为零，需反馈回路才可能有非零整合

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_68161c78067d7b4add05ba1a`
- Input SHA-256：`9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45`
- 不确定性：2023 演讲整理；IIT/意识主张为理论观点，非共识事实。
- 提议理由：导入 claim_wechat_wangjun_iit_zero_integration_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_wangjun_iit_zero_integration_20260716-该文引整合信息理论称传统前馈-transformer-信息整合度为零-需反馈回路才可能有非零整合.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_wangjun_iit_zero_integration_20260716"
+title: "该文引整合信息理论称传统前馈/Transformer 信息整合度为零，需反馈回路才可能有非零整合"
+tags: ["integrated-information-theory", "transformer", "recurrent"]
+domains: ["consciousness-studies", "machine-learning"]
+confidence: "low"
+applicability: ["IIT 与 NN 架构讨论", "global workspace / 回路必要性"]
+uncertainty: "「整合度为零」为演讲转述 IIT 测量结论，争议大且非共识；需回 IIT 原文。"
+evidence: [{"evidence_id": "ev_4819", "evidence_kind": "quote", "source_id": "source_68161c78067d7b4add05ba1a", "content_id": "content_9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "extraction_id": "extraction_fe8826e067e84de0741c77af", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "span_start": 4819, "span_end": 5026, "original_text": "Integrated information hypothesis，当信息整个集合的时候，整合起来的信息量大于单个个体。如果有系统可以产生这样的信息量以及信息的集成，也就是刚才所讲在整个大脑里面信息量得到了整合。同时也就摒弃了一切争论。确定的一点是，只有在信息整合充分的情况下大脑单元中才有主观意识。\n\n如果这样，我们用信息集成度来测量现在的神经网络、深度学习、Transformer，你会发现它们的信息整合度是零", "section": "IIT 测量", "stance": "supports", "verification_status": "verified", "reason": "文内对 Transformer/前馈网络整合度的判断。"}, {"evidence_id": "ev_5183", "evidence_kind": "quote", "source_id": "source_68161c78067d7b4add05ba1a", "content_id": "content_9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "extraction_id": "extraction_fe8826e067e84de0741c77af", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "span_start": 5183, "span_end": 5254, "original_text": "反馈回路。先从 global workspace 反馈到各个单独的模块，同时各个模块再把它整合的信息返回到系统中。当出现回路时，信息就有集成了", "section": "回路必要性", "stance": "supports", "verification_status": "verified", "reason": "文内对回路产生信息集成的说明。"}]
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
+# IIT 与架构
+
+前馈/Transformer 整合度为零（演讲引 IIT）；回路或 RNN 不同。
```
