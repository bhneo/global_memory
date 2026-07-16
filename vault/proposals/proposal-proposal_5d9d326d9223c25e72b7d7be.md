---
id: "proposal_5d9d326d9223c25e72b7d7be"
type: "proposal"
status: "pending"
title: "模型提议：该文称伪随机数在有限算力下熵高但 epiplexity 低，可解释随机噪声缺乏学习价值"
created_at: "2026-07-15T23:49:56+08:00"
updated_at: "2026-07-15T23:49:56+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_epiplexity_pseudorandom_theorem_20260715"
target_path: "vault/knowledge/claims/claim_wechat_epiplexity_pseudorandom_theorem_20260715-该文称伪随机数在有限算力下熵高但-epiplexity-低-可解释随机噪声缺乏学习价值.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5d9d326d9223c25e72b7d7be.md"
candidate_sha256: "14cd30d37b21f06bbdaa68cccae6854646a40ae8717af17442aad39cd147510e"
change_reason: "导入 claim_wechat_epiplexity_pseudorandom_theorem_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_494ab02c17c5f495f1ed29d0", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "uncertainty": "信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称伪随机数在有限算力下熵高但 epiplexity 低，可解释随机噪声缺乏学习价值

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_494ab02c17c5f495f1ed29d0`
- Input SHA-256：`40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d`
- 不确定性：信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。
- 提议理由：导入 claim_wechat_epiplexity_pseudorandom_theorem_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_epiplexity_pseudorandom_theorem_20260715-该文称伪随机数在有限算力下熵高但-epiplexity-低-可解释随机噪声缺乏学习价值.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_epiplexity_pseudorandom_theorem_20260715"
+title: "该文称伪随机数在有限算力下熵高但 epiplexity 低，可解释随机噪声缺乏学习价值"
+tags: ["epiplexity", "pseudorandom", "algorithmic-complexity"]
+domains: ["information-theory", "cryptography"]
+confidence: "medium"
+applicability: ["定理 1 科普表述", "区分 PRNG 与真随机"]
+uncertainty: "定理条件与证明细节在科普中被压缩；依赖原论文与密码学假设。"
+evidence: [{"evidence_id": "ev_1998", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 1998, "span_end": 2198, "original_text": "定理 1 伪随机数是低认知复杂度的\n\n伪随机数是用固定种子 + 固定公式生成的，在无限算力的神眼里，一眼就能看穿种子和规则，所以它的信息和种子一样少，根本没新东西（认知复杂度和时间有界熵都极低）。在有限算力的现实世界里，伪随机数看起来信息量爆炸（熵高），但完全没有可学习的结构（认知复杂度低）\n\n这就完美解释了「为什么随机噪声没有学习价值」，也解决了经典算法复杂度无法区分伪随机数与真随机数的核心痛点", "section": "定理 1", "stance": "supports", "verification_status": "verified", "reason": "文内对伪随机数低 epiplexity 的说明。"}, {"evidence_id": "ev_2039", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 2039, "span_end": 2143, "original_text": "无限算力的神眼里，一眼就能看穿种子和规则，所以它的信息和种子一样少，根本没新东西（认知复杂度和时间有界熵都极低）。在有限算力的现实世界里，伪随机数看起来信息量爆炸（熵高），但完全没有可学习的结构（认知复杂度低", "section": "有限 vs 无限算力", "stance": "supports", "verification_status": "verified", "reason": "文内对比无限算力与有限算力下的信息观。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T23:50:00+08:00"
+updated_at: "2026-07-15T23:50:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 epiplexity 科普；等待人工核验"
+source_ids: ["source_494ab02c17c5f495f1ed29d0"]
+relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "由伊芝冰对 arXiv:2601.03220 epiplexity 论文的科普解读归纳；原论文未 capture"}]
+---
+
+# 伪随机与 epiplexity
+
+高熵不等于可学习结构。
```
