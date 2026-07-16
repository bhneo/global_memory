---
id: "proposal_5181346d0175269d5f27cec9"
type: "proposal"
status: "pending"
title: "模型提议：该文称即使 recipe 正确，物理世界仍有评测不稳定、环境变异性、长程记忆与在线精度等 LLM 未遇瓶颈"
created_at: "2026-07-16T01:20:00+08:00"
updated_at: "2026-07-16T01:20:00+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_physical_world_generalization_walls_20260716"
target_path: "vault/knowledge/claims/claim_wechat_physical_world_generalization_walls_20260716-该文称即使-recipe-正确-物理世界仍有评测不稳定-环境变异性-长程记忆与在线精度等-llm-未遇瓶颈.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5181346d0175269d5f27cec9.md"
candidate_sha256: "f099dd8943f01c9650fc268a5c16cc96267bb046dbd119545fc68110e560200d"
change_reason: "导入 claim_wechat_physical_world_generalization_walls_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_0a113baae7ce4d1ab78da1a3", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "uncertainty": "观点/分析文；Re-Mix/RT-2 等数字需回论文；含融资叙事批判。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称即使 recipe 正确，物理世界仍有评测不稳定、环境变异性、长程记忆与在线精度等 LLM 未遇瓶颈

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_0a113baae7ce4d1ab78da1a3`
- Input SHA-256：`5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c`
- 不确定性：观点/分析文；Re-Mix/RT-2 等数字需回论文；含融资叙事批判。
- 提议理由：导入 claim_wechat_physical_world_generalization_walls_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_physical_world_generalization_walls_20260716-该文称即使-recipe-正确-物理世界仍有评测不稳定-环境变异性-长程记忆与在线精度等-llm-未遇瓶颈.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_physical_world_generalization_walls_20260716"
+title: "该文称即使 recipe 正确，物理世界仍有评测不稳定、环境变异性、长程记忆与在线精度等 LLM 未遇瓶颈"
+tags: ["generalization", "evaluation", "online-adaptation"]
+domains: ["robotics", "embodied-ai"]
+confidence: "low"
+applicability: ["Levine AutoEval、Finn DROID、PI Memory/RLT 引述语境", "闭环控制 vs 开环录像类比"]
+uncertainty: "为综述性观点；具体 PI 项目细节为作者解读，需回原始材料。"
+evidence: [{"evidence_id": "ev_6859", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 6859, "span_end": 6892, "original_text": "开环轨迹，而控制真正要解决的却是一个会被自己动作不断改写的闭环世界", "section": "闭环 vs 开环", "stance": "supports", "verification_status": "verified", "reason": "文内对机器人控制与录像本质差异的说明。"}, {"evidence_id": "ev_7020", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 7020, "span_end": 7046, "original_text": "cook shrimp in any kitchen", "section": "Finn 引述", "stance": "supports", "verification_status": "verified", "reason": "文内对跨厨房迁移困难的 Finn 引述。"}, {"evidence_id": "ev_7911", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 7911, "span_end": 8011, "original_text": "在线改进。\n\n注意这里隐含的判断非常重要。它不是继续往总数据集里多追加一些日志，也不是再扩大一点 web pretraining，而是直接承认某些能力瓶颈必须靠在线闭环、靠实时修正、靠非常紧扣执行本身", "section": "在线适应", "stance": "supports", "verification_status": "verified", "reason": "文内对 RLT/在线修正必要性的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:19:00+08:00"
+updated_at: "2026-07-16T01:19:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入具身数据问题分析文；等待人工核验"
+source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
+relations: [{"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由杜伦文/青稞具身智能专栏归纳；引述 RT-2、Re-Mix、Covariant 等为二手分析"}]
+---
+
+# 物理世界之墙
+
+评测/变异性/记忆/精度/在线适应；非 LLM 式 scaling。
```
