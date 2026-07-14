# ADR 0002: Append-only source versioning

- Status: Accepted
- Date: 2026-07-14

## Context

同一网页会随时间变化。把 canonical URL 永久视为一条 source 会丢失变化，把最新正文覆盖旧正文则破坏 raw 不可变性；每次无条件抓取又会制造大量无意义重复。知识层是否需要随新证据变化，也不能由 capture 流程自动决定。

## Decision

1. `source_family_id` 表示 `source kind + canonical locator`，source version 表示某次内容发生变化后的不可变证据。
2. 普通 `gm capture URL` 保持快速去重，不重新访问网络；只有显式 `--refresh` 才抓取。
3. 最新 content hash 未变化时只记录审计事件，不创建新 source。
4. 内容变化时追加 content object 和 source record，写 `version_number`、`previous_version_id`；不得修改旧版本。
5. 如果内容回到历史 hash，复用 content object，但仍创建新的 source version，以保留时间事实。
6. 每个变化版本自动生成 `source_refresh` proposal，包含旧/新 hash 和原文 diff。
7. 批准 refresh proposal 只确认新证据版本，不修改 canonical knowledge；知识变化仍必须经过独立 compile proposal。
8. v1 的既有 source ID 与文件保持不变；缺少显式 version 字段时按 v1 读取。

## Consequences

变化历史、内容回退和知识审批被清晰分离，旧仓库无需迁移 raw 文件。代价是搜索会看到多个 source version，后续需要 latest/accepted 视图；网页的“结构变化但语义未变”当前仍按 bytes hash 识别为新版本。

## Rejected alternatives

- 覆盖旧 source/raw：违反不可变性并丢失证据时间线。
- 每次 capture 都刷新：引入网络延迟和不可预期外部访问。
- 内容 hash 直接作为 source ID：无法表达同一内容在时间线上再次出现。
- Refresh 自动更新 canonical：把新证据和知识判断错误地合并成一步。
