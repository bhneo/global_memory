---
id: "claim_wechat_model_merge_linear_connectivity_20260716"
title: "该文将模型合并/参数算术与线性模式连接作为不同训练模型共享潜在流形的证据"
tags: ["model-merging", "mode-connectivity", "weight-space"]
domains: ["machine-learning", "optimization"]
confidence: "low"
applicability: ["模型合并与权重插值讨论", "线性模式连接作为共享结构证据的科普语境"]
uncertainty: "从合并成功推断共享流形为哲学性跳跃；[8] 未 capture，与参数对称性等因素未区分。"
evidence: [{"evidence_id": "ev_1592", "evidence_kind": "quote", "source_id": "source_f35b44d4bd383fb26ca49165", "content_id": "content_0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "extraction_id": "extraction_5175d74685def36cf73e75c3", "input_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "span_start": 1592, "span_end": 1614, "original_text": "两个模型相加，从而获得一个能同时胜任两种任务", "section": "模型合并", "stance": "supports", "verification_status": "verified", "reason": "文内对参数级模型合并可行性的表述。"}, {"evidence_id": "ev_1772", "evidence_kind": "quote", "source_id": "source_f35b44d4bd383fb26ca49165", "content_id": "content_0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "extraction_id": "extraction_5175d74685def36cf73e75c3", "input_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "span_start": 1772, "span_end": 1836, "original_text": "线性模式连接的存在——即在不同微调模型的权重之间存在一条损失保持不变的路径——是另一个关键证据，它指向了一个连贯的、潜在智能图景", "section": "模式连接", "stance": "supports", "verification_status": "verified", "reason": "文内将线性模式连接作为共享结构证据。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T00:26:00+08:00"
updated_at: "2026-07-16T00:26:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 LLM 表征趋同观点文；等待人工核验"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
relations: [{"type": "derived_from", "target_id": "source_f35b44d4bd383fb26ca49165", "reason": "由智能情报所转载 Lukas Nel 2025-07 观点文归纳；vec2vec/柏拉图表征等原论文未 capture"}]
---

# 模型合并与模式连接

合并/连接被解释为共享流形；推断性强。
