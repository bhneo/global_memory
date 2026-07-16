---
id: "proposal_a30e0203487f6059cd53e476"
type: "proposal"
status: "superseded"
title: "模型提议：该文对比两种当代图景：it-from-qubit 全息编码下粒子由纠缠量子比特涌现；振幅学家则用 amplituhedron 等几何对象直接编码散射振幅"
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
target_id: "claim_wechat_particle_modern_qubit_amplitude_20260716"
target_path: "vault/knowledge/claims/claim_wechat_particle_modern_qubit_amplitude_20260716-该文对比两种当代图景-it-from-qubit-全息编码下粒子由纠缠量子比特涌现-振幅学家则用-amplituhedron-等.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_a30e0203487f6059cd53e476.md"
candidate_sha256: "11d8421290430dc5c3244b8b87e5d177217193a8813e828f37c267e86ec9a754"
change_reason: "导入 claim_wechat_particle_modern_qubit_amplitude_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bcee8e0abc8386cbba43b87", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "uncertainty": "Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文对比两种当代图景：it-from-qubit 全息编码下粒子由纠缠量子比特涌现；振幅学家则用 amplituhedron 等几何对象直接编码散射振幅

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bcee8e0abc8386cbba43b87`
- Input SHA-256：`e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a`
- 不确定性：Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。
- 提议理由：导入 claim_wechat_particle_modern_qubit_amplitude_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_particle_modern_qubit_amplitude_20260716-该文对比两种当代图景-it-from-qubit-全息编码下粒子由纠缠量子比特涌现-振幅学家则用-amplituhedron-等.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_particle_modern_qubit_amplitude_20260716"
+title: "该文对比两种当代图景：it-from-qubit 全息编码下粒子由纠缠量子比特涌现；振幅学家则用 amplituhedron 等几何对象直接编码散射振幅"
+tags: ["quantum-gravity", "holography", "amplituhedron"]
+domains: ["physics", "quantum-information"]
+confidence: "medium"
+applicability: ["it-from-qubit 与全息时空", "振幅学对 QFT「方便虚构物」批评"]
+uncertainty: "两路线是否互补或矛盾文内称未定论；均为前沿研究非成熟理论。"
+evidence: [{"evidence_id": "ev_3993", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 3993, "span_end": 4014, "original_text": "it-from-qubit（它来自量子比特", "section": "it-from-qubit", "stance": "supports", "verification_status": "verified", "reason": "文内对量子比特涌现时空/粒子的介绍。"}, {"evidence_id": "ev_6198", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 6198, "span_end": 6286, "original_text": "amplituhedron ——一个几何对象，可对其体积中的粒子散射振幅进行编码。粒子在时空中碰撞并引发因果连锁反应的画面已经一去不复返了。阿卡尼·哈默德说：“我们试图在柏拉图", "section": "振幅几何", "stance": "supports", "verification_status": "verified", "reason": "文内对 amplituhedron 与振幅学方法的说明。"}]
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
+# 当代双图景
+
+全息量子比特 vs 振幅几何；恩格尔哈特：「我们不知道」仍是简短回答。
```
