# ADR 0026：Source Authority 与 Primary Source Follow-up

- 状态：accepted
- 日期：2026-07-16

## 决策

来源权威分级独立于真假判断，但影响 review priority、claim confidence 与 synthesis 权重。二手材料出现 arXiv、DOI、GitHub 或官方 locator 时，创建 `vault/followups/` 中的正式任务；capture/resolve 必须保留状态历史，不只写在 uncertainty 文本中。

Follow-up 身份使用规范化 locator：arXiv PDF/abstract/version 统一到无版本 abstract URL，普通 HTTP locator 去除 query、fragment 与尾部斜杠。既有记录迁移必须先 dry-run，应用时备份 follow-up 与受影响 proposal；旧任务不删除，而是标记 `superseded` 并指向规范任务。活动列表默认隐藏 superseded 历史。

## 结果

“需要回原文”成为可执行、可查询、可关闭且不会因引用格式差异重复的治理对象。代价是 locator 规则变化需要显式迁移，不能静默重算 ID。
