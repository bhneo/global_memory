---
id: "proposal_48e9a22cca2b3dd74cb3abc4"
type: "proposal"
status: "superseded"
title: "模型提议：Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点"
created_at: "2026-07-15T12:25:12+08:00"
updated_at: "2026-07-15T14:27:44+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_agentic_vla_libero_main_20260715"
target_path: "vault/knowledge/claims/claim_agentic_vla_libero_main_20260715-agentic-vla-在-libero-上报告平均成功率-97-8-long-套件相对-sft-基线提升-12-3-个百分点.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_48e9a22cca2b3dd74cb3abc4.md"
candidate_sha256: "aec5bcea7711d79d2edd568e7b8e596c0460fa53609b681c174a5ce002b98dad"
change_reason: "Agentic-VLA LIBERO"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_2c21320690e566fbbf80fd75", "input_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:27:44+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_a99124724d635b4102390d75"
---

# 模型提议：Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_2c21320690e566fbbf80fd75`
- Input SHA-256：`8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Agentic-VLA LIBERO
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_agentic_vla_libero_main_20260715-agentic-vla-在-libero-上报告平均成功率-97-8-long-套件相对-sft-基线提升-12-3-个百分点.md
@@ -0,0 +1,24 @@
+---
+id: "claim_agentic_vla_libero_main_20260715"
+type: "claim"
+status: "proposal"
+title: "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: ["Agentic-VLA LIBERO"]
+tags: ["vla", "libero", "online-adaptation"]
+domains: ["robot-learning"]
+confidence: "medium"
+source_ids: ["source_2c21320690e566fbbf80fd75"]
+relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["LIBERO 四套件", "OpenVLA-OFT 基线", "5 seeds mean±std"]
+uncertainty: "LIBERO 仿真 benchmark；+12.3% 相对 SFT baseline（Table 1 Δ 列）。"
+evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "+12.3% on long-horizon tasks", "stance": "supports", "reason": "摘要 Long 提升。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7 页 Table 1", "excerpt": "Agentic-VLA† 97.8±0.4 ... Δ vs. SFT baseline +12.3", "stance": "supports", "reason": "Table 1 平均与 Long 差值。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7 页 Section 4.2", "excerpt": "Reporting mean ± std over 5 independent seeds", "stance": "context", "reason": "统计协议。"}]
+---
+
+# LIBERO 主结果
+
+Table 1。
```
