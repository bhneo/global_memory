---
id: "concept_0ea689b9ff94e453dd23b64b"
type: "concept"
status: "proposal"
title: "R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements"
created_at: "2026-07-27T11:02:49+08:00"
updated_at: "2026-07-28T10:05:00+08:00"
aliases: ["broom restriction estimate", "p greater than 3 plus 3 over 13", "扫帚结构 restriction", "R3 截断抛物面估计"]
tags: []
domains: ["harmonic-analysis", "restriction-theory", "polynomial-partitioning"]
confidence: "medium"
source_ids: ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986", "source_f366554c5c3887de7c6ad29b"]
relations: [{"type": "derived_from", "target_id": "source_299adfe6dd42f97b6f75b777", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_c0e590dd716efa867bc34cbd", "reason": "两者都连接 Kakeya 型几何控制与 restriction 估计；既有概念处理多线性横截性，本文记录线性 R3 中经 incidence/decoupling 得到的特定指数改进。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_f366554c5c3887de7c6ad29b"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_3d3296633fe4d9256a88672c"], "importance": "high", "changed_belief": "我会把这项结果与后续 p>3+3/14 的摘要级改进并列而不合并，也不会从摘要把 brooms 推广为通用波包分类。", "surprising": "", "connections": [{"shared_mechanism": "本文与既有多线性 restriction/Kakeya 概念都用管或波包几何组织对 extension 叠加的控制。", "boundary": "本源只断言截断抛物面上的 L∞→Lp 估计及 p>3+3/13；摘要没有定义 brooms 的完整机制。", "difference": "既有概念是多线性横截性的一般框架；本文是单一线性 R3 的定量界，并结合 two-ends 与多项式划分。"}], "open_questions": ["broom 结构在完整证明中如何限制波包聚集，并与后续 refined-decoupling 路线形成何种可比较的几何不变量？"]}
proposed_status: "working"
---

# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3

Wang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。

## 新增来源材料

- `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。

## 新增来源材料

- `source_f366554c5c3887de7c6ad29b`：在后续 p>3+3/14 的 Kakeya incidence 与 refined-decoupling 改进之前，Wang 的论文摘要对 R3 截断抛物面给出 L∞ 到 Lp restriction 估计的 p>3+3/13 范围，并把证明路线标记为 polynomial partitioning、two-ends reduction 和 brooms。该来源仅为摘要，因而这里只保存精确指数、范数和方法标签；不能据此把 broom 解释扩展为一般波包聚集定理，也不能把该界与后续更强指数合并。
