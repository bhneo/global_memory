---
id: "proposal_8f90af7ca8c7a8459f583cd8"
type: "proposal"
status: "superseded"
title: "模型提议：该文将粒子表述为观测后坍缩的波函数，并指出测量为何选出特定结果近一个世纪仍无共识答案"
created_at: "2026-07-16T10:52:31+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9bcee8e0abc8386cbba43b87"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_particle_collapsed_wavefunction_20260716"
target_path: "vault/knowledge/claims/claim_wechat_particle_collapsed_wavefunction_20260716-该文将粒子表述为观测后坍缩的波函数-并指出测量为何选出特定结果近一个世纪仍无共识答案.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_8f90af7ca8c7a8459f583cd8.md"
candidate_sha256: "605125e3e512cdc4b55585b8a21d5e3e15dfae6e90930f5ab229476e6109543d"
change_reason: "导入 claim_wechat_particle_collapsed_wavefunction_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bcee8e0abc8386cbba43b87", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "uncertainty": "Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文将粒子表述为观测后坍缩的波函数，并指出测量为何选出特定结果近一个世纪仍无共识答案

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bcee8e0abc8386cbba43b87`
- Input SHA-256：`e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a`
- 不确定性：Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。
- 提议理由：导入 claim_wechat_particle_collapsed_wavefunction_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_particle_collapsed_wavefunction_20260716-该文将粒子表述为观测后坍缩的波函数-并指出测量为何选出特定结果近一个世纪仍无共识答案.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_particle_collapsed_wavefunction_20260716"
+title: "该文将粒子表述为观测后坍缩的波函数，并指出测量为何选出特定结果近一个世纪仍无共识答案"
+tags: ["quantum-mechanics", "measurement-problem", "wavefunction"]
+domains: ["physics", "quantum-mechanics"]
+confidence: "medium"
+applicability: ["波粒二象性科普", "测量问题开放状态"]
+uncertainty: "为一种诠释性表述；测量问题有多派解释未展开。"
+evidence: [{"evidence_id": "ev_1090", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 1090, "span_end": 1111, "original_text": "粒子是坍缩后的波函数。但这究竟意味着什么呢", "section": "坍缩定义", "stance": "supports", "verification_status": "verified", "reason": "文内对粒子=坍缩波函数的核心句。"}, {"evidence_id": "ev_1158", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 1158, "span_end": 1175, "original_text": "将近一个世纪，物理学家仍旧没有答案", "section": "测量未解", "stance": "supports", "verification_status": "verified", "reason": "文内对测量问题状态的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T10:48:00+08:00"
+updated_at: "2026-07-16T10:48:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入「何谓粒子」科普；等待人工核验"
+source_ids: ["source_9bcee8e0abc8386cbba43b87"]
+relations: [{"type": "derived_from", "target_id": "source_9bcee8e0abc8386cbba43b87", "reason": "中科院物理所转载 Natalie Wolchover / Quanta 2020《What Is a Particle?》；原刊未 capture"}]
+---
+
+# 坍缩波函数
+
+观测使波函数坍缩为探测器上的局域事件；为何如此仍开放。
```
