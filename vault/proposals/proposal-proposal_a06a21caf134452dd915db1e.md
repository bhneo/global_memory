---
id: "proposal_a06a21caf134452dd915db1e"
type: "proposal"
status: "superseded"
title: "模型提议：该文以光流与隧道/洞穴类比解释错觉：大脑预测环境将变暗并提前扩大瞳孔作为补偿"
created_at: "2026-07-16T01:40:40+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_38756ea977001ddb8594f144"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_expanding_hole_optic_flow_20260716"
target_path: "vault/knowledge/claims/claim_wechat_expanding_hole_optic_flow_20260716-该文以光流与隧道-洞穴类比解释错觉-大脑预测环境将变暗并提前扩大瞳孔作为补偿.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_a06a21caf134452dd915db1e.md"
candidate_sha256: "a20b90350ea38328fdd325f74d992374995ed654d2dfde93501d0a32ec0648ee"
change_reason: "导入 claim_wechat_expanding_hole_optic_flow_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_38756ea977001ddb8594f144", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "uncertainty": "知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文以光流与隧道/洞穴类比解释错觉：大脑预测环境将变暗并提前扩大瞳孔作为补偿

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_38756ea977001ddb8594f144`
- Input SHA-256：`fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86`
- 不确定性：知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。
- 提议理由：导入 claim_wechat_expanding_hole_optic_flow_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_expanding_hole_optic_flow_20260716-该文以光流与隧道-洞穴类比解释错觉-大脑预测环境将变暗并提前扩大瞳孔作为补偿.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_expanding_hole_optic_flow_20260716"
+title: "该文以光流与隧道/洞穴类比解释错觉：大脑预测环境将变暗并提前扩大瞳孔作为补偿"
+tags: ["optic-flow", "predictive-processing", "evolution"]
+domains: ["psychology", "neuroscience"]
+confidence: "medium"
+applicability: ["Gibson 光流概念科普", "隧道进入类比"]
+uncertainty: "光流解释为主观理论框架；Laeng 教授引述需回原文。"
+evidence: [{"evidence_id": "ev_1413", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 1413, "span_end": 1427, "original_text": "光流”（optic flow", "section": "光流概念", "stance": "supports", "verification_status": "verified", "reason": "文内对光流定义与引入。"}, {"evidence_id": "ev_1342", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 1342, "span_end": 1398, "original_text": "走进一条隧道或是一处山洞。在这样的情况下，大脑可以预测出下一刻环境会变得更暗，然后提前扩大瞳孔，作为一种补偿机制", "section": "隧道类比", "stance": "supports", "verification_status": "verified", "reason": "文内对预测变暗与瞳孔补偿的解释。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:41:00+08:00"
+updated_at: "2026-07-16T01:41:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 expanding hole 视错觉科普；等待人工核验"
+source_ids: ["source_38756ea977001ddb8594f144"]
+relations: [{"type": "derived_from", "target_id": "source_38756ea977001ddb8594f144", "reason": "由环球科学/中科院物理所转载的 expanding hole 研究科普；原论文 Frontiers 2022 未 capture"}]
+---
+
+# 光流预测
+
+静态渐变阴影触发进入隧道式预测；演化适应解释。
```
