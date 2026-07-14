# Global Memory

Global Memory 是一个本地优先、用户拥有、模型无关的个人长期认知基础设施。Markdown 与不可变 raw source 是长期真相源；SQLite、全文索引、缓存和未来的向量索引都只是可删除、可重建的派生层。

当前版本完成第一阶段最小纵向闭环：

```text
URL / 文本 / 本地文件
→ 不可变 raw content + source record
→ URL 与内容去重
→ SQLite FTS5 检索
→ 确定性规则 compile proposal + 内容级 diff
→ 人工 approve / reject
→ canonical knowledge
→ 来源回溯与索引重建
```

## 快速开始

要求 Python 3.11+。运行时只使用 Python 标准库；测试使用 pytest。

```powershell
cd C:\Users\bhneo\Desktop\project\超级大脑\global_memory
python -m pip install -e .
gm init
gm capture-text --text "人的原始文字会原样保留" --comment "验证最小闭环"
gm capture https://example.com/article --refresh --comment "显式检查网页是否更新"
gm inbox
gm compile <source-id>
gm proposal show <proposal-id>
gm proposal approve <proposal-id>
gm propose-update <canonical-id> --from-file candidate.md --reason "新证据改变了适用范围"
gm search "原始文字"
gm doctor
```

不安装 editable package 时，可以在 PowerShell 中使用：

```powershell
.\scripts\gm.ps1 status
```

所有命令都接受全局参数 `--root <仓库目录>`，也可以设置 `GM_ROOT`。

## CLI

- `gm init`：创建必要目录并建立空索引。
- `gm capture <url-or-path> --comment "..."`：捕获 URL 或本地文件。
- `gm capture <url> --refresh`：显式重新抓取；内容变化时追加 source version 和 review proposal。
- `gm capture-text [--text "..."]`：捕获文本；未提供 `--text` 时读取 stdin。
- `gm inbox`：列出尚未 compile 的 source。
- `gm compile <source-id>`：生成低置信度 proposal，不修改 canonical knowledge。
- `gm proposals [--status pending]`：列出 proposal。
- `gm proposal show|approve|reject <proposal-id>`：查看 diff 或明确审批。
- `gm propose-update <id> --from-file <candidate.md> --reason "..."`：创建受并发保护的 canonical update proposal。
- `gm search "<query>"`：搜索 source 与 canonical knowledge，结果携带 `source_ids`。
- `gm show <id>` / `gm related <id>`：读取对象与 typed relations。
- `gm rebuild-index`：从文件重建 SQLite FTS5。
- `gm status` / `gm doctor`：查看状态与一致性检查。

## 安全边界

- raw content 与 source record 通过独占创建写入，普通流程不能覆盖。
- compile 只写 `vault/proposals/`；只有明确 approve 才写 canonical knowledge。
- candidate 有 SHA-256 校验，审批前被改动会被拒绝。
- SQLite 位于 `data/indexes/`，不进入 Git，可随时重建。
- 二进制 raw payload 默认不进 Git；必须通过独立备份策略保护。
- URL 捕获当前限制 20 MB，不执行 JavaScript，也不绕过登录或付费墙。

## URL refresh 语义

普通 `gm capture URL` 不会重新访问已经存在的 canonical URL。只有显式 `--refresh` 才发起新请求：内容哈希未变时不创建新版本；内容变化时追加新的 source Markdown 和 raw content，并生成 `source_refresh` proposal，展示旧/新原文 diff。批准 refresh proposal 只确认新来源版本可进入后续知识处理，不会直接修改 canonical knowledge。随后可对新 `source_id` 单独执行 `gm compile`。

## Canonical update 语义

Candidate 必须是 UTF-8 Markdown，保持 target 的 `id`、`type`、`created_at`，使用 `status: proposal`；可用 `proposed_status` 建议 `confirmed`、`contested`、`superseded` 或 `archived`。Claim 必须保留至少一个 `source_id`。

`propose-update` 会不可变保存当时的 base snapshot 和 candidate，并记录两者 SHA-256。审批时 target 必须仍与 base 完全相同；如期间发生人工编辑，审批会失败且不写文件。再次运行 `proposal show` 可看到 Base→Candidate 和 Base→Current，随后应基于当前 canonical 重新创建 proposal。系统当前不自动合并冲突。

## 进一步阅读

从 [INDEX.md](INDEX.md) 开始。数据格式见 [SCHEMA.md](SCHEMA.md)，系统边界见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)，当前接管点见 [PROJECT_STATE.md](PROJECT_STATE.md)。
