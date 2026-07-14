# Current State

## Current milestone

M2.1：append-only URL/source version 与 refresh review 闭环已实现。

## What is working

- Python 标准库 CLI 与本地仓库初始化。
- 文本、本地文件和 HTTP(S) URL capture。
- 不可变 raw content、结构化 source Markdown、SHA-256 与 capture audit event。
- canonical URL 规范化、同来源去重、跨来源内容去重且不丢 source record。
- SQLite FTS5 + 中文子串 fallback；结果包含来源 ID。
- 确定性规则 compile proposal、candidate 哈希、内容级 unified diff。
- approve/reject gate；未批准 proposal 不触碰 canonical knowledge。
- typed relation 校验、show、related、status、doctor、索引全量重建。
- Windows 路径、中文文件名和索引文件原子替换测试。
- 显式 `gm capture <url> --refresh`；未变化时去重，变化时追加版本。
- Source family、连续 version、previous-version 链与内容回退历史。
- `source_refresh` proposal、原文 diff 和不触碰 canonical 的独立审批。
- `doctor` 对 source version chain 的一致性检查。

## What is being implemented

- 无进行中的功能；仓库处于可接管状态。

## Known defects

- URL 抓取只处理静态响应，不执行 JavaScript；网页正文仍可能包含 HTML 噪声。
- 第一版 compile 是确定性开头摘录，只验证治理闭环，不等同于高质量知识抽取。
- 第一版 proposal review 支持 show/approve/reject；受治理的 candidate 编辑与 defer 尚未实现。
- 跨文件 approve 无法获得真正的文件系统事务；`doctor` 可发现索引/文件问题，但尚无专用恢复日志。
- 二进制内容只保存和哈希，尚未提取 PDF、Office 或图片正文。
- 搜索目前会同时返回同一 family 的多个版本，尚无 latest/accepted 过滤视图。

## Unresolved architectural questions

- canonical knowledge 的更新 proposal 如何提供三方合并与并发编辑保护。
- 大型 raw payload 的本地备份、加密、完整性清单与 Git/LFS 边界。
- 未来模型处理器的隐私策略、可复现性记录和 provider-neutral 接口。
- 中文全文检索长期采用 tokenizer、n-gram 派生索引还是混合策略。

## Recent decisions

- Markdown/raw source 为真相源；SQLite 仅为可重建派生层。
- 第一版零运行时第三方依赖，使用 argparse、urllib 与 SQLite FTS5。
- 相同内容不同来源共享 content object，但保留独立 source record。
- compile 默认只生成低置信度 proposal；canonical 写入必须明确 approve。
- 真实示例已完成 capture → compile → diff → approve → search；`gm doctor` 返回 `ok: true`。
- ADR 0002 确定显式 refresh、append-only source version 和独立 refresh proposal。

## Next concrete task

实现 canonical knowledge update proposal 的基线哈希、乐观并发保护和三方 diff，继续禁止绕过人工审批。

## Do not do yet

- 不引入 embedding、向量数据库、图数据库、复杂前端或 Obsidian 插件。
- 不导入全部浏览器、微信或历史聊天。
- 不启动多 Agent 调度、夜间任务、全库自动重写或复杂本体工程。
