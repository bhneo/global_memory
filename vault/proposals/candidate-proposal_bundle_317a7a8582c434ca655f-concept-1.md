---
id: "concept_0ea689b9ff94e453dd23b64b"
type: "concept"
status: "proposal"
title: "R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements"
created_at: "2026-07-27T11:02:49+08:00"
updated_at: "2026-07-27T16:01:39+08:00"
aliases: ["多项式分割 restriction 改进", "polynomial-partitioning restriction improvement"]
tags: []
domains: ["harmonic-analysis", "restriction", "polynomial-partitioning"]
confidence: "high"
source_ids: ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986"]
relations: [{"type": "derived_from", "target_id": "source_299adfe6dd42f97b6f75b777", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_c0e590dd716efa867bc34cbd", "reason": "两者都连接 Kakeya 型几何控制与 restriction 估计；既有概念处理多线性横截性，本文记录线性 R3 中经 incidence/decoupling 得到的特定指数改进。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_b6d55666cda69c2a1c407986"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_0a086695ae3406f8c7c543a1"], "importance": "high", "changed_belief": "我会把该成果表述为带曲率、范数和指数门槛的 R3 线性估计，而不把它泛化为任意曲面或完整 restriction conjecture。", "surprising": "", "connections": [{"shared_mechanism": "两者都用管状波包的几何组织来控制 restriction 或 Kakeya 型重叠。", "boundary": "本文限于 R3 中紧致光滑且第二基本形式严格正的曲面，以及 L2(S) 到 Lp(R3) 的 p>3.25 估计。", "difference": "本文以多项式分割和 cell/零集二分推进线性 restriction；既有条目以 Kakeya incidence 与 refined decoupling 得到另一指数改进。"}], "open_questions": ["多项式分割中的 broad/cell--surface 分解还需要何种新控制，才能在该类曲面上达到预期的 p>3？"]}
proposed_status: "working"
---

# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3

Wang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。

## 新增来源材料

- `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。
