---
id: "claim_wechat_epiplexity_pseudorandom_theorem_20260715"
title: "该文称伪随机数在有限算力下熵高但 epiplexity 低，可解释随机噪声缺乏学习价值"
tags: ["epiplexity", "pseudorandom", "algorithmic-complexity"]
domains: ["information-theory", "cryptography"]
confidence: "medium"
applicability: ["定理 1 科普表述", "区分 PRNG 与真随机"]
uncertainty: "定理条件与证明细节在科普中被压缩；依赖原论文与密码学假设。"
evidence: [{"evidence_id": "ev_1998", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 1998, "span_end": 2198, "original_text": "定理 1 伪随机数是低认知复杂度的\n\n伪随机数是用固定种子 + 固定公式生成的，在无限算力的神眼里，一眼就能看穿种子和规则，所以它的信息和种子一样少，根本没新东西（认知复杂度和时间有界熵都极低）。在有限算力的现实世界里，伪随机数看起来信息量爆炸（熵高），但完全没有可学习的结构（认知复杂度低）\n\n这就完美解释了「为什么随机噪声没有学习价值」，也解决了经典算法复杂度无法区分伪随机数与真随机数的核心痛点", "section": "定理 1", "stance": "supports", "verification_status": "verified", "reason": "文内对伪随机数低 epiplexity 的说明。"}, {"evidence_id": "ev_2039", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 2039, "span_end": 2143, "original_text": "无限算力的神眼里，一眼就能看穿种子和规则，所以它的信息和种子一样少，根本没新东西（认知复杂度和时间有界熵都极低）。在有限算力的现实世界里，伪随机数看起来信息量爆炸（熵高），但完全没有可学习的结构（认知复杂度低", "section": "有限 vs 无限算力", "stance": "supports", "verification_status": "verified", "reason": "文内对比无限算力与有限算力下的信息观。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-15T23:50:00+08:00"
updated_at: "2026-07-15T23:50:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 epiplexity 科普；等待人工核验"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "由伊芝冰对 arXiv:2601.03220 epiplexity 论文的科普解读归纳；原论文未 capture"}]
---

# 伪随机与 epiplexity

高熵不等于可学习结构。
