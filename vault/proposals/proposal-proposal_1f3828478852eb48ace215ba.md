---
id: "proposal_1f3828478852eb48ace215ba"
type: "proposal"
status: "pending"
title: "模型提议：该文称 PhySO 研究来自斯特拉斯堡大学与 CSIRO Data61，历时约 1.5 年"
created_at: "2026-07-15T18:45:42+08:00"
updated_at: "2026-07-15T18:45:42+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_physo_provenance_20260715"
target_path: "vault/knowledge/claims/claim_wechat_physo_provenance_20260715-该文称-physo-研究来自斯特拉斯堡大学与-csiro-data61-历时约-1-5-年.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_1f3828478852eb48ace215ba.md"
candidate_sha256: "40336e745fa01b9a57009e44702166e71d847ed9c308c1aeac1d10a6514a4531"
change_reason: "导入 claim_wechat_physo_provenance_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_ef99e322cc662cffb7eb5c8f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "uncertainty": "科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 PhySO 研究来自斯特拉斯堡大学与 CSIRO Data61，历时约 1.5 年

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_ef99e322cc662cffb7eb5c8f`
- Input SHA-256：`fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58`
- 不确定性：科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。
- 提议理由：导入 claim_wechat_physo_provenance_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_physo_provenance_20260715-该文称-physo-研究来自斯特拉斯堡大学与-csiro-data61-历时约-1-5-年.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_physo_provenance_20260715"
+title: "该文称 PhySO 研究来自斯特拉斯堡大学与 CSIRO Data61，历时约 1.5 年"
+tags: ["physo", "provenance"]
+domains: ["physics", "machine-learning"]
+confidence: "medium"
+applicability: ["2023 量子位报道中的机构与周期信息", "arXiv:2303.03192 关联论文"]
+uncertainty: "1.5 年为「论文一作透露」的媒体转述；机构名与论文作者列表需与 arXiv 交叉验证。"
+evidence: [{"evidence_id": "ev_139", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 139, "span_end": 208, "original_text": "这项成果来自德国斯特拉斯堡大学与澳大利亚联邦科学与工业研究组织Data61部门，据论文一作透露，研究用了1.5年时间，受到学术界广泛关注。", "section": "机构与周期", "stance": "supports", "verification_status": "verified", "reason": "文内对来源机构与研究周期的描述。"}, {"evidence_id": "ev_804", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 804, "span_end": 840, "original_text": "论文：\nhttps://arxiv.org/abs/2303.03192", "section": "论文链接", "stance": "supports", "verification_status": "verified", "reason": "文内给出的 arXiv 链接。"}]
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
+# 研究出处
+
+斯特拉斯堡大学 + CSIRO Data61；报道称 1.5 年。
```
