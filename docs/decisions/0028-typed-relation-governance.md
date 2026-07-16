# ADR 0028：Typed Relation Governance

- 状态：accepted
- 日期：2026-07-16

## 决策

关系支持 supports、contradicts、refines、limits、supersedes、derived_from、defines、instantiates、raises、answers、applied_in、tested_by、failed_in、analogous_to、depends_on、part_of、related_to。每条关系必须记录 source、target、reason、confidence、created_by、status；关系修改进入 proposal，遍历受 depth/node 限制。

## 结果

知识图由有理由的结构关系形成；关键词重合不自动生成边，矛盾双方不会被覆盖。
