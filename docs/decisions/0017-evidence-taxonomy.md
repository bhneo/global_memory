# ADR 0017：Evidence Taxonomy 与逐字回验

- 状态：accepted
- 日期：2026-07-15

## 决策

Evidence 明确区分 quote、paraphrase、translation、table_value、figure 和 calculation。Quote 必须绑定 extraction/input hash 并逐字匹配 span；paraphrase 明示转述；translation 同时保存原文与译文；表格值保留单位和行列/页码；figure 区分可见信息与解释；calculation 引用输入 evidence 并保留方法。旧 evidence schema 兼容读取。

## 结果

系统不再用语义模糊的 excerpt 混合逐字原文、翻译和解释。更强 schema 增加 candidate 生成成本，但为 PDF 页码证据、矛盾审计与长期回溯提供稳定基础。
