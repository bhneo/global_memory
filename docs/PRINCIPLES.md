# Principles

1. **用户拥有记忆。** 本地文件是长期载体，聊天上下文和服务端记忆不是。
2. **Markdown 优先。** 人可读、Git 可追踪、Agent 可编辑、工具可迁移。
3. **Obsidian-ready，Obsidian-optional。** 使用 Frontmatter、相对附件和 wikilinks，但核心不依赖插件数据库。
4. **raw 只追加。** 修正通过新版本、补充记录或状态变化表达，不静默覆盖旧证据。
5. **来源与解释分层。** 原文、人的直觉、Agent 解释、人工确认知识、认知前沿、行动对象和派生索引职责分离。
6. **Agent 不能静默升级事实。** Agent 可在显式、可审计的自动门禁下把合格 claim 发布为 `provisional`，但不得自行晋升为 `confirmed`、合并概念或批量重写。
7. **保留认知演化。** 使用 contested、superseded、archived、valid_during、superseded_by、change_reason 表达变化。
8. **未知用途合法。** intuition、anomaly、tension、analogy、hypothesis 都有长期位置。
9. **关系重质量。** 每条边有类型和理由，不设固定链接配额。
10. **Wiki 与检索互补。** 先定位候选，再沿关系扩展，必要时回到 raw source。
11. **派生层可删除。** SQLite、FTS、未来 embedding 和图索引必须能从真相层重建。
12. **知识修改像代码。** 显示 diff、记录理由、测试行为、审计批准、用 Git 保留历史。
