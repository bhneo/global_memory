# ADR 0013：可检索的 provisional knowledge 与人工确认晋升

- 状态：accepted
- 日期：2026-07-15

## 背景

逐条 proposal 人工批准把两个不同动作绑在了一起：让通过结构校验的导入内容可被系统使用，以及由用户确认它是可信事实。批量导入文章时，这会制造不必要的点击，也容易让“批准进入索引”被误解为“人工背书内容”。

## 决策

采用两级信任模型：

1. 结构化 claim 在来源、evidence、applicability、uncertainty 和 confidence 完整，至少有一条支持证据，且没有反证或高风险领域标签时，可以由 `gm proposal publish` 写入 canonical，状态固定为 `provisional`。
2. `provisional` 立即进入全文检索与 Context Pack。所有读取接口必须返回其状态，不得静默表现为 `confirmed`。
3. 只有用户显式执行 `gm promote` 或人工 `gm proposal approve`，知识才成为 `confirmed`。
4. 医疗、法律、金融等高风险领域，包含反证的 claim，非 claim 对象，以及 source refresh、relation discovery、deterministic synthesis 继续要求人工批准。
5. Proposal 使用 `published` 和 `approved` 区分自动门禁发布与人工批准；审计日志保留 `published-provisional` 与 `promoted-confirmed` 事件。

## 结果

批量导入不再因每条知识都需要人工点击而停滞，同时系统仍能区分机器整理结果与用户确认事实。Proposal 继续承担差异审阅、冲突拦截和高风险治理，而不再是所有可检索知识的强制人工瓶颈。
