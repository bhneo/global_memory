---
id: "claim_wechat_embodiskill_alfworld_results_20260716"
title: "该文报告 EmbodiSkill 在 ALFWorld 上达 93.28% 成功率（冻结 Qwen3.5-27B executor + GPT-5.2 演化 skill），消融显示 skill-aware 归因由 78.36% 提至 93.28%"
tags: ["ALFWorld", "benchmark", "ablation"]
domains: ["agent-systems", "evaluation"]
confidence: "medium"
applicability: ["vs G-Memory 74.62%", "Puttwo 100% 叙述"]
uncertainty: "数字来自博客转述 Ju et al. 2026；GPT-5.2 等命名需回原文核验。"
evidence: [{"evidence_id": "ev_4125", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 4125, "span_end": 4182, "original_text": "93.28% success rate。这个数字超过直接用 GPT-5.2 当无技能 Agent 的 70.89%", "section": "ALFWorld 主结果", "stance": "supports", "verification_status": "verified", "reason": "文内对 EmbodiSkill 与 direct agent 成功率对比。"}, {"evidence_id": "ev_4845", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 4845, "span_end": 4908, "original_text": "Skill-unaware evolution: 78.36% EmbodiSkill:             93.28%", "section": "消融对比", "stance": "supports", "verification_status": "verified", "reason": "文内同 executor 消融：skill-unaware 78.36% vs EmbodiSkill 93.28%。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:16:00+08:00"
updated_at: "2026-07-16T11:16:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 EmbodiSkill/SkillEvolver 综述；等待人工核验"
source_ids: ["source_d01f40e4896de2e186cbbe8a"]
relations: [{"type": "derived_from", "target_id": "source_d01f40e4896de2e186cbbe8a", "reason": "Gavin AI 记事本解读 EmbodiSkill (2605.10332) 与 SkillEvolver (2605.10500)；原论文未 capture"}]
---

# EmbodiSkill 实验

EB-Habitat/Navigation 亦报告超 memory baseline 双位数百分点。
