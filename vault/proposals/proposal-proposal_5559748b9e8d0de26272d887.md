---
id: "proposal_5559748b9e8d0de26272d887"
type: "proposal"
status: "pending"
title: "模型提议：该文称遍历性指时间平均与群体平均等价；现实生活常非遍历，个体可能因一次失败出局"
created_at: "2026-07-16T00:35:52+08:00"
updated_at: "2026-07-16T00:35:52+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_ergodicity_time_vs_ensemble_20260716"
target_path: "vault/knowledge/claims/claim_wechat_ergodicity_time_vs_ensemble_20260716-该文称遍历性指时间平均与群体平均等价-现实生活常非遍历-个体可能因一次失败出局.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5559748b9e8d0de26272d887.md"
candidate_sha256: "7e4d4d0e89251b72be5a9657d17980e1812894adbb4c02fcb7de187ef1d45157"
change_reason: "导入 claim_wechat_ergodicity_time_vs_ensemble_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9d39636775b188c87d6a001f", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "uncertainty": "概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称遍历性指时间平均与群体平均等价；现实生活常非遍历，个体可能因一次失败出局

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9d39636775b188c87d6a001f`
- Input SHA-256：`0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33`
- 不确定性：概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。
- 提议理由：导入 claim_wechat_ergodicity_time_vs_ensemble_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_ergodicity_time_vs_ensemble_20260716-该文称遍历性指时间平均与群体平均等价-现实生活常非遍历-个体可能因一次失败出局.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_ergodicity_time_vs_ensemble_20260716"
+title: "该文称遍历性指时间平均与群体平均等价；现实生活常非遍历，个体可能因一次失败出局"
+tags: ["ergodicity", "time-average", "ensemble-average"]
+domains: ["statistical-physics", "decision-theory"]
+confidence: "medium"
+applicability: ["遍历性假设科普", "路径依赖与单次生命路径语境"]
+uncertainty: "玻尔兹曼遍历性为经典物理假设简化；向人生/金融决策的推广为科普类比。"
+evidence: [{"evidence_id": "ev_631", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 631, "span_end": 677, "original_text": "时间平均：描述一个个体在足够长的时间里，多次经历同一过程后所得的平均结果；\n\n右侧是群体平均", "section": "遍历性定义", "stance": "supports", "verification_status": "verified", "reason": "文内对时间平均与群体平均关系的说明。"}, {"evidence_id": "ev_844", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 844, "span_end": 881, "original_text": "非遍历的：个体的资源有限，往往在经历到所有可能的路径前就因某次失败直接出局", "section": "非遍历现实", "stance": "supports", "verification_status": "verified", "reason": "文内对资源有限与出局风险的表述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T00:36:00+08:00"
+updated_at: "2026-07-16T00:36:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入非遍历性/凯利公式科普；等待人工核验"
+source_ids: ["source_9d39636775b188c87d6a001f"]
+relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由 DataCafe/雪鹅经中科院物理所转载的非遍历性与凯利公式科普归纳；Thorp 等原书未 capture"}]
+---
+
+# 遍历 vs 非遍历
+
+时间平均≈群体平均仅在有遍历时；出局不可逆。
```
