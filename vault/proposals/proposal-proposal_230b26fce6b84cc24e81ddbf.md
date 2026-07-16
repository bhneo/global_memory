---
id: "proposal_230b26fce6b84cc24e81ddbf"
type: "proposal"
status: "superseded"
title: "模型提议：该文引述量子场论：粒子是全空间量子场的离散量子激发，相互作用由场论精确计算"
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
target_id: "claim_wechat_particle_field_quantum_20260716"
target_path: "vault/knowledge/claims/claim_wechat_particle_field_quantum_20260716-该文引述量子场论-粒子是全空间量子场的离散量子激发-相互作用由场论精确计算.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_230b26fce6b84cc24e81ddbf.md"
candidate_sha256: "ebb1b62574164a18f45a0e1d8833806f5c2aac680601c9e762e848bcfdfb5d41"
change_reason: "导入 claim_wechat_particle_field_quantum_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bcee8e0abc8386cbba43b87", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "uncertainty": "Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文引述量子场论：粒子是全空间量子场的离散量子激发，相互作用由场论精确计算

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bcee8e0abc8386cbba43b87`
- Input SHA-256：`e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a`
- 不确定性：Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。
- 提议理由：导入 claim_wechat_particle_field_quantum_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_particle_field_quantum_20260716-该文引述量子场论-粒子是全空间量子场的离散量子激发-相互作用由场论精确计算.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_particle_field_quantum_20260716"
+title: "该文引述量子场论：粒子是全空间量子场的离散量子激发，相互作用由场论精确计算"
+tags: ["quantum-field-theory", "particle-physics"]
+domains: ["physics"]
+confidence: "medium"
+applicability: ["QFT 标准语言", "光子/电子等场量子化"]
+uncertainty: "概念性综述；未涉及 QFT 数学细节或引力耦合。"
+evidence: [{"evidence_id": "ev_1318", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 1318, "span_end": 1363, "original_text": "狄拉克等人发现，该思想可以外推到电子和其他所有粒子：根据量子场论，粒子是全空间量子场的激发", "section": "场量子化", "stance": "supports", "verification_status": "verified", "reason": "文内对狄拉克等人场论外推的叙述。"}, {"evidence_id": "ev_1402", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 1402, "span_end": 1471, "original_text": "扰动场的小份能量。尽管量子场论无处不在，但它却成了粒子物理学的通用语言，因为它可以极其精确地计算粒子相互作用时的情况，而粒子之间的相互作用", "section": "激发与相互作用", "stance": "supports", "verification_status": "verified", "reason": "文内对粒子作为场激发的功能说明。"}]
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
+# 场量子激发
+
+粒子是量子场的离散振荡；QFT 为粒子物理通用计算语言。
```
