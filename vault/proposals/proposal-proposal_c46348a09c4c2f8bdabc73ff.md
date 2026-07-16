---
id: "proposal_c46348a09c4c2f8bdabc73ff"
type: "proposal"
status: "pending"
title: "模型提议：该文称 Φ-SO 在笔记本上约 4 小时可恢复爱因斯坦质能方程"
created_at: "2026-07-15T18:45:41+08:00"
updated_at: "2026-07-15T18:45:41+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_physo_laptop_runtime_20260715"
target_path: "vault/knowledge/claims/claim_wechat_physo_laptop_runtime_20260715-该文称-φ-so-在笔记本上约-4-小时可恢复爱因斯坦质能方程.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_c46348a09c4c2f8bdabc73ff.md"
candidate_sha256: "299a82b99ae3c7d181953c42eccebc1e1156d78ac212b8222fa7baa79bb719a3"
change_reason: "导入 claim_wechat_physo_laptop_runtime_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_ef99e322cc662cffb7eb5c8f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "uncertainty": "科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 Φ-SO 在笔记本上约 4 小时可恢复爱因斯坦质能方程

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_ef99e322cc662cffb7eb5c8f`
- Input SHA-256：`fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58`
- 不确定性：科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。
- 提议理由：导入 claim_wechat_physo_laptop_runtime_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_physo_laptop_runtime_20260715-该文称-φ-so-在笔记本上约-4-小时可恢复爱因斯坦质能方程.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_physo_laptop_runtime_20260715"
+title: "该文称 Φ-SO 在笔记本上约 4 小时可恢复爱因斯坦质能方程"
+tags: ["physo", "runtime", "symbolic-regression"]
+domains: ["physics", "machine-learning"]
+confidence: "low"
+applicability: ["文内爱因斯坦能量公式实验叙述", "无需超算、普通笔记本设定"]
+uncertainty: "4 小时为媒体报道的单点案例，未给出硬件规格、数据量或随机种子；不能外推为所有公式的一般运行时间。"
+evidence: [{"evidence_id": "ev_99", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 99, "span_end": 137, "original_text": "整个过程也不需要动用超算，一台笔记本大概4个小时就能搞定爱因斯坦的质能方程。", "section": "运行时间", "stance": "supports", "verification_status": "verified", "reason": "文内对硬件需求与耗时的表述。"}]
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
+# 笔记本运行时间
+
+报道称约 4 小时恢复质能方程。
```
