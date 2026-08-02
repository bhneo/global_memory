---
id: "concept_1ce9ddde12ec6f4eec375139"
type: "concept"
status: "working"
title: "FRW 熵力 Friedmann 推导依赖屏幕温度闭合 / entropic-force Friedmann derivation depends on a screen-temperature closure"
created_at: "2026-07-28T11:59:04+08:00"
updated_at: "2026-08-02T12:30:29+08:00"
aliases: ["Friedmann equations from entropic force", "FRW holographic screen temperature ansatz", "熵力 Friedmann 方程", "FRW 屏幕温度闭合"]
tags: []
domains: ["gravity", "thermodynamics", "cosmology"]
confidence: "high"
source_ids: ["source_5f1181fbb50ffea7c3863e80"]
relations: [{"type": "derived_from", "target_id": "source_5f1181fbb50ffea7c3863e80", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
change_reason: "compile bundle from source_5f1181fbb50ffea7c3863e80"
reflection_context: {"reflection_ids": ["reflection_a9f1720db02942e41df73c4d"], "importance": "high", "changed_belief": "我不会把该形式推导当成熵力机制或动态时空 Unruh 温度的确证；它只说明在指定屏幕、能量识别和温度闭合下可重写 FRW 动力学。", "surprising": "", "connections": [{"shared_mechanism": "两者都以熵、温度和能量关系来组织引力场方程。", "boundary": "本文限于均匀各向同性 FRW、全息/equipartition 假设、Tolman--Komar active mass，以及非 proper-acceleration 的温度 ansatz。", "difference": "局部 Rindler Clausius 路线以因果视界热流与 Unruh 温度约束局部方程；本文以宇宙学屏幕和积分式 FRW 关系构造形式导出。"}], "open_questions": ["能否从动态 FRW 中可操作的探测器响应或局部视界构造独立导出本文所需的屏幕温度，而非把它作为闭合假设？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "gpt-5.6-sol-high-daily-v2-readmission"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "gpt-5.6-sol-high-daily-v2-readmission"
consolidation_count: 2
last_consolidated_at: "2026-08-02T12:30:29+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_0b1183cfa34f9eca0dd9"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0b1183cfa34f9eca0dd9-concept-1.md"
origin_candidate_sha256: "235cfc7337094ca1bb293044a6376f960cfab8bf4a5cd3331cc8110f76a84df2"
origin_cognitive_artifact_sha256: "c1ddb5bd06c051bc79dadffe2181e40ae5bcb0ca96d0d576c0797b05d88dfb7e"
memory_schema_version: 2
last_consolidation_id: "consolidation_0a3efe21ef2ad5177f2b750d"
---

# FRW 熵力 Friedmann 推导依赖屏幕温度闭合 / entropic-force Friedmann derivation depends on a screen-temperature closure

在均匀各向同性 FRW 时空中，可选取固定共动半径的球面作为全息屏，把屏幕 bit 数取为面积除以 Planck 面积，并以能量均分关系把屏幕温度连接到包围物质的能量。若再把物质能量识别为含压力项的 active gravitational mass，并假设屏幕温度与 -a-double-dot r 成正比，则可形式得到加速度 Friedmann 方程；配合连续性方程可得到通常的 Friedmann 积分关系。关键边界是：共动观察者的 proper acceleration 为零，论文使用的 -a-double-dot r 不是该观察者的 proper acceleration，作者因此把相应 Unruh 型温度关系明确称为 working ansatz。该结果证明的是一组全息屏、equipartition、active-mass 与温度闭合假设可以重写 FRW 动力学，而不是独立证明熵力机制或动态宇宙中的 Unruh 温度。
