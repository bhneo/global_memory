---
id: "proposal_3da31aa93e0a1483305f3084"
type: "proposal"
status: "pending"
title: "模型提议：该文称 Φ-SO 对阻尼谐振子、爱因斯坦能量与万有引力等经典公式实验均 100% 还原且各方法缺一不可"
created_at: "2026-07-15T18:45:42+08:00"
updated_at: "2026-07-15T18:45:42+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_physo_classic_recovery_20260715"
target_path: "vault/knowledge/claims/claim_wechat_physo_classic_recovery_20260715-该文称-φ-so-对阻尼谐振子-爱因斯坦能量与万有引力等经典公式实验均-100-还原且各方法缺一不可.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_3da31aa93e0a1483305f3084.md"
candidate_sha256: "a271189ddbc0ac8501e1071044e887c6b0bed7fb29177b26bc2e53cf58f39741"
change_reason: "导入 claim_wechat_physo_classic_recovery_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_ef99e322cc662cffb7eb5c8f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "uncertainty": "科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 Φ-SO 对阻尼谐振子、爱因斯坦能量与万有引力等经典公式实验均 100% 还原且各方法缺一不可

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_ef99e322cc662cffb7eb5c8f`
- Input SHA-256：`fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58`
- 不确定性：科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。
- 提议理由：导入 claim_wechat_physo_classic_recovery_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_physo_classic_recovery_20260715-该文称-φ-so-对阻尼谐振子-爱因斯坦能量与万有引力等经典公式实验均-100-还原且各方法缺一不可.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_physo_classic_recovery_20260715"
+title: "该文称 Φ-SO 对阻尼谐振子、爱因斯坦能量与万有引力等经典公式实验均 100% 还原且各方法缺一不可"
+tags: ["physo", "benchmark", "symbolic-regression"]
+domains: ["physics", "machine-learning"]
+confidence: "low"
+applicability: ["文内列举的三类经典公式实验", "作者通过媒体报道给出的结果概述"]
+uncertainty: "100% 与「缺一不可」为报道转述论文结论，未给出 ablation 细节、噪声水平或失败案例；需回 arXiv 原文核验。"
+evidence: [{"evidence_id": "ev_586", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 586, "span_end": 630, "original_text": "研究团队用阻尼谐振子解析表达式、爱因斯坦能量公式，牛顿的万有引力公式等经典公式来做实验。", "section": "实验对象", "stance": "supports", "verification_status": "verified", "reason": "文内列举的 benchmark 公式。"}, {"evidence_id": "ev_632", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 632, "span_end": 665, "original_text": "Φ-SO都能100%的从数据中还原这些公式，并且以上方法缺一不可。", "section": "实验结果", "stance": "supports", "verification_status": "verified", "reason": "文内对还原率与 ablation 结论的转述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T18:45:00+08:00"
+updated_at: "2026-07-15T18:45:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入微信科技报道；等待人工核验"
+source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
+relations: [{"type": "derived_from", "target_id": "source_ef99e322cc662cffb7eb5c8f", "reason": "由量子位公众号对 PhySO/Φ-SO 论文报道归纳；非 arXiv 原文 capture"}]
+---
+
+# 经典公式 benchmark
+
+报道称 100% 还原且方法组件缺一不可。
```
