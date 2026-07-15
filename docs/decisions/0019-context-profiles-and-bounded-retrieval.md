# ADR 0019：Context Profiles 与有界混合检索

- 状态：accepted
- 日期：2026-07-15

## 决策

Context Pack 支持 execution、research、exploration profile 及组合。召回先使用 metadata/加权 FTS，再按最大深度和节点数沿 typed relations 扩展；最后回到 extraction/source 并按 token budget 裁剪。支持 project/domain/type/status/time/source-kind filter。每项输出 status、match/selection reason、source_ids、hash 和紧凑 evidence。

Proposal 默认排除；显式包含时保持 proposal 类型和 pending/deferred 状态。关系遍历上限固定为 depth 3、nodes 100。旧词汇重合发现功能改称 related-content，不声明真正 serendipity。

## 结果

同一 truth/index layer 可以为执行、研究和探索提供不同上下文，而无需复制知识或引入 embedding。排序仍是确定性启发式，真实语料验收后再决定是否增加更复杂召回。
