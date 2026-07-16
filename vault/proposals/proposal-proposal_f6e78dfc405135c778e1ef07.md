---
id: "proposal_f6e78dfc405135c778e1ef07"
type: "proposal"
status: "superseded"
title: "模型提议：该文称元胞自动机实验中 Class IV 规则 epiplexity 持续增长，可为涌现提供量化标准"
created_at: "2026-07-15T23:49:56+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_epiplexity_emergence_ca_20260715"
target_path: "vault/knowledge/claims/claim_wechat_epiplexity_emergence_ca_20260715-该文称元胞自动机实验中-class-iv-规则-epiplexity-持续增长-可为涌现提供量化标准.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f6e78dfc405135c778e1ef07.md"
candidate_sha256: "794c778690c352c03a76eb5b9393331a9502f5d35562ffa51e42365231cca944"
change_reason: "导入 claim_wechat_epiplexity_emergence_ca_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_494ab02c17c5f495f1ed29d0", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "uncertainty": "信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称元胞自动机实验中 Class IV 规则 epiplexity 持续增长，可为涌现提供量化标准

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_494ab02c17c5f495f1ed29d0`
- Input SHA-256：`40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d`
- 不确定性：信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。
- 提议理由：导入 claim_wechat_epiplexity_emergence_ca_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_epiplexity_emergence_ca_20260715-该文称元胞自动机实验中-class-iv-规则-epiplexity-持续增长-可为涌现提供量化标准.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_epiplexity_emergence_ca_20260715"
+title: "该文称元胞自动机实验中 Class IV 规则 epiplexity 持续增长，可为涌现提供量化标准"
+tags: ["emergence", "cellular-automata", "complex-systems"]
+domains: ["complex-systems", "information-theory"]
+confidence: "low"
+applicability: ["复杂系统涌现定性转定量讨论", "原论文元胞自动机实验科普"]
+uncertainty: "Class II/III/IV 分类结果为科普转述；涌现的 epiplexity 定义需回原文严格核验。"
+evidence: [{"evidence_id": "ev_4329", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 4329, "span_end": 4421, "original_text": "epiplexity 涌现」的严格定义：当系统的单步演化对不同算力的观察者有相同的 epiplexity，而多步演化的 epiplexity 差距随系统规模发散时，系统就出现了涌现现象", "section": "涌现定义", "stance": "supports", "verification_status": "verified", "reason": "文内对 epiplexity 涌现的形式化科普描述。"}, {"evidence_id": "ev_4588", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 4588, "span_end": 4642, "original_text": "Class IV（复杂型）规则 epiplexity 持续增长，这为复杂系统的分类与预测提供了统一的量化标准", "section": "元胞自动机", "stance": "supports", "verification_status": "verified", "reason": "文内对 CA 规则类别的 epiplexity 对比。"}]
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
+# 涌现量化
+
+Class IV epiplexity 增长；涌现可计算化。
```
