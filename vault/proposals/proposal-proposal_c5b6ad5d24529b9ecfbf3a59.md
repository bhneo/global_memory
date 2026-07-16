---
id: "proposal_c5b6ad5d24529b9ecfbf3a59"
type: "proposal"
status: "superseded"
title: "模型提议：该文称开源工具 Φ-SO 可直接从实验数据发现物理公式"
created_at: "2026-07-15T18:45:41+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_physo_overview_20260715"
target_path: "vault/knowledge/claims/claim_wechat_physo_overview_20260715-该文称开源工具-φ-so-可直接从实验数据发现物理公式.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_c5b6ad5d24529b9ecfbf3a59.md"
candidate_sha256: "41058f45384ff272e9c4e0747ad53eba563c215e6a5364b1db27a4ffb24f2b4a"
change_reason: "导入 claim_wechat_physo_overview_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_ef99e322cc662cffb7eb5c8f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "uncertainty": "科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称开源工具 Φ-SO 可直接从实验数据发现物理公式

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_ef99e322cc662cffb7eb5c8f`
- Input SHA-256：`fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58`
- 不确定性：科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。
- 提议理由：导入 claim_wechat_physo_overview_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_physo_overview_20260715-该文称开源工具-φ-so-可直接从实验数据发现物理公式.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_physo_overview_20260715"
+title: "该文称开源工具 Φ-SO 可直接从实验数据发现物理公式"
+tags: ["symbolic-regression", "physo", "physics-ai"]
+domains: ["physics", "machine-learning"]
+confidence: "medium"
+applicability: ["2023 量子位对 PhySO 开源报道", "GitHub: WassimTenachi/PhySO"]
+uncertainty: "为科技媒体报道而非论文正文；「一步到位」为媒体表述；实际性能需回 arXiv:2303.03192 核验。"
+evidence: [{"evidence_id": "ev_57", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 57, "span_end": 97, "original_text": "它名叫Φ-SO ，能直接从数据中找到隐藏的规律，而且一步到位，直接给出对应公式。", "section": "工具能力", "stance": "supports", "verification_status": "verified", "reason": "文内对 Φ-SO 功能的直接描述。"}, {"evidence_id": "ev_757", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 757, "span_end": 803, "original_text": "GitHub：\nhttps://github.com/WassimTenachi/PhySO", "section": "开源链接", "stance": "supports", "verification_status": "verified", "reason": "文内给出的代码仓库。"}, {"evidence_id": "evp_75188", "evidence_kind": "paraphrase", "source_id": "source_ef99e322cc662cffb7eb5c8f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "section": "来源层级", "interpretation": "报道链接 arXiv:2303.03192 但原文未 capture", "stance": "context", "verification_status": "verified", "reason": "提醒需回论文核验实验设置。"}]
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
+# Φ-SO 概述
+
+开源符号回归工具，从数据发现公式。
```
