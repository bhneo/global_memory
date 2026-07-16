---
id: "proposal_73b82cfa1f3563da3333b365"
type: "proposal"
status: "pending"
title: "模型提议：该文介绍维格纳观点：粒子是庞加莱群不可约表示，自旋标签区分不同基本粒子；标准模型可写为 SU(3)×SU(2)×U(1)"
created_at: "2026-07-16T10:52:31+08:00"
updated_at: "2026-07-16T10:52:31+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9bcee8e0abc8386cbba43b87"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_particle_poincare_wigner_20260716"
target_path: "vault/knowledge/claims/claim_wechat_particle_poincare_wigner_20260716-该文介绍维格纳观点-粒子是庞加莱群不可约表示-自旋标签区分不同基本粒子-标准模型可写为-su-3-su-2-u-1.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_73b82cfa1f3563da3333b365.md"
candidate_sha256: "b0b69fad421c58d22466c06bfb0c7091f196b89ca454a27ab037ef93fd7ddd4b"
change_reason: "导入 claim_wechat_particle_poincare_wigner_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bcee8e0abc8386cbba43b87", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "uncertainty": "Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文介绍维格纳观点：粒子是庞加莱群不可约表示，自旋标签区分不同基本粒子；标准模型可写为 SU(3)×SU(2)×U(1)

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bcee8e0abc8386cbba43b87`
- Input SHA-256：`e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a`
- 不确定性：Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。
- 提议理由：导入 claim_wechat_particle_poincare_wigner_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_particle_poincare_wigner_20260716-该文介绍维格纳观点-粒子是庞加莱群不可约表示-自旋标签区分不同基本粒子-标准模型可写为-su-3-su-2-u-1.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_particle_poincare_wigner_20260716"
+title: "该文介绍维格纳观点：粒子是庞加莱群不可约表示，自旋标签区分不同基本粒子；标准模型可写为 SU(3)×SU(2)×U(1)"
+tags: ["group-theory", "standard-model", "spin"]
+domains: ["physics", "mathematics"]
+confidence: "medium"
+applicability: ["Wigner 1939 定义科普", "内部对称性「色」「味」"]
+uncertainty: "格拉肖等强调表示≠粒子；群论与粒子等同有争议。"
+evidence: [{"evidence_id": "ev_1816", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 1816, "span_end": 1828, "original_text": "庞加莱群的一个不可约表示", "section": "Wigner 式定义", "stance": "supports", "verification_status": "verified", "reason": "文内对群表示标准答案的叙述。"}, {"evidence_id": "ev_3114", "evidence_kind": "quote", "source_id": "source_9bcee8e0abc8386cbba43b87", "content_id": "content_e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "extraction_id": "extraction_2a34ca186d194f1ec87a6741", "input_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "span_start": 3114, "span_end": 3268, "original_text": "SU(3)的变换的表示，包含了无数种数学上混合这三种标签的方式。\n\n有“色”的粒子是对称群SU(3)的表示，而具有“味”和电荷这两种内部性质的粒子，分别是对称群SU(2)和U(1)表示。因此，粒子物理的标准模型——包含所有已知基本粒子及其相互作用的量子场论——通常被称为对称群SU(3)×SU(2)×U(1)", "section": "标准模型对称群", "stance": "supports", "verification_status": "verified", "reason": "文内对标准模型群结构的说明。"}]
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
+# 群表示
+
+时空庞加莱表示 + 内部 SU(3)×SU(2)×U(1)；自旋决定物质/力行为。
```
