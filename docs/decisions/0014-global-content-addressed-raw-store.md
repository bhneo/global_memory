# ADR 0014：全局 Content-Addressed Raw Store

- 状态：accepted
- 日期：2026-07-15

## 背景

旧实现把 raw payload 放在 `web/files/personal-notes` 各自的 `content` 或 `blobs` 目录。即使 metadata 使用相同 `content_id`，不同 capture channel 仍可能产生多份物理对象；URL path 的尾部还可能被误识别为扩展名，例如 arXiv `/pdf/2607.11119`。

## 决策

1. 物理对象路径固定为 `vault/raw/objects/sha256/<前2位>/<次2位>/<完整SHA-256>`，不带扩展名。
2. capture kind、locator、MIME、文件名和显示扩展名只属于 source record，不参与 content identity。
3. 同一 bytes 的多个 capture 保留不同 source record，并指向同一个 `content_id` 和对象路径。
4. 新对象使用独占创建；已有同路径不同 bytes 立即失败。
5. `gm raw verify` 校验每个 source 的 content ID、路径和磁盘 hash。
6. 旧布局通过 journal 化迁移更新 source 引用。迁移前自动备份 source record，保留旧 payload，不提供隐式删除。

## 结果

跨入口去重成为磁盘级不变量，source provenance 与物理存储解耦。对象没有可读扩展名，因此打开方式必须使用 source metadata；这是确保路径只由哈希决定的有意取舍。
