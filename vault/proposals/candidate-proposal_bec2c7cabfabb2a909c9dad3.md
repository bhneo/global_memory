---
id: "claim_wechat_skillevolver_skillsbench_results_20260716"
title: "该文报告 SkillEvolver R=2 在 SkillsBench 验证集 avg@5 达 56.87%，超 human-curated 43.6%；R=1→R=2 增 8.7pp，下游 token/turns/wall-clock 约降 15–24%"
tags: ["SkillsBench", "meta-skill", "efficiency"]
domains: ["agent-systems", "evaluation"]
confidence: "medium"
applicability: ["83 任务 15+ 领域", "R=2 成本 3.92 USD/task"]
uncertainty: "Claude Opus 4.6 配置与数字需回原文；KernelBench 3 任务探针作者称不可过度解读。"
evidence: [{"evidence_id": "ev_8694", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 8694, "span_end": 8727, "original_text": "SkillEvolver R=2:          56.87%", "section": "SkillsBench 主结果", "stance": "supports", "verification_status": "verified", "reason": "文内对比表格 R=2 聚合成功率。"}, {"evidence_id": "ev_9570", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 9570, "span_end": 9623, "original_text": "tokens:    -19.4% turns:     -15.3% wall-clock:-23.8%", "section": "下游效率", "stance": "supports", "verification_status": "verified", "reason": "文内对 evolved skill 降低下游成本的三项指标。"}]
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

# SkillEvolver 实验

one-shot Self-Gen 32% 未明显超 no-skill 29.9%。
