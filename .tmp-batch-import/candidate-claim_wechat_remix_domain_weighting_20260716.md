---
id: "claim_wechat_remix_domain_weighting_20260716"
title: "该文引 Re-Mix 称学习到的 domain weight 比均匀混合高 38%，说明数据混合/recipe 比总量更关键"
tags: ["re-mix", "data-mixing", "open-x-embodiment"]
domains: ["robotics", "machine-learning"]
confidence: "medium"
applicability: ["Open X-Embodiment 混合策略讨论", "错误混数据可能比缺数据更糟语境"]
uncertainty: "38%/32% 数字来自作者转述 2024 Re-Mix 论文；原论文未 capture。"
evidence: [{"evidence_id": "ev_1436", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 1436, "span_end": 1557, "original_text": "Re-Mix 则进一步印证了这个直觉。斯坦福的 Dorsa Sadigh 团队在 2024 年的 Re-Mix 论文里用 Open X-Embodiment 检验数据混合策略，最后发现学出来的 domain weight 比均匀混合高 38%", "section": "Re-Mix 结果", "stance": "supports", "verification_status": "verified", "reason": "文内对 Re-Mix domain weight 提升的引述。"}, {"evidence_id": "ev_1548", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 1548, "span_end": 1571, "original_text": "均匀混合高 38%，比人工挑的权重还高 32%", "section": "相对人工权重", "stance": "supports", "verification_status": "verified", "reason": "文内对比 learned vs uniform/manual mixing。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T01:19:00+08:00"
updated_at: "2026-07-16T01:19:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入具身数据问题分析文；等待人工核验"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
relations: [{"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由杜伦文/青稞具身智能专栏归纳；引述 RT-2、Re-Mix、Covariant 等为二手分析"}]
---

# Re-Mix

混合权重/recipe 影响大；非仅数据总量。
