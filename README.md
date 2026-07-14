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
gm model-propose <source-id> --candidate model-candidate.md --provider local --model my-model --prompt-version v1 --prompt-file prompt.md --uncertainty "待人工核验" --reason "导入模型结果"
gm proposal show <proposal-id>
gm proposal approve <proposal-id>
gm proposal defer <proposal-id> --reason "等待补充证据"
gm proposal revise <proposal-id> --from-file revised-candidate.md --reason "人工修订候选主张"
gm recover
gm propose-update <canonical-id> --from-file candidate.md --reason "新证据改变了适用范围"
gm search "原始文字"
gm lint
gm backup manifest
gm backup create D:\GlobalMemoryRawBackup
gm backup verify D:\GlobalMemoryRawBackup
gm backup restore D:\GlobalMemoryRawBackup
gm backup restore D:\GlobalMemoryRawBackup --apply
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
- `gm model-propose <source-id> --candidate <Markdown> ...`：导入用户明确提供的外部模型 candidate；记录 provider/model/prompt version/输入哈希与不确定性，但命令自身不调用 provider。
- `gm proposals [--status pending]`：列出 proposal。
- `gm proposal show|approve|defer|reject <proposal-id>`：查看 diff、明确审批或暂缓处理。
- `gm proposal revise <id> --from-file <candidate.md> --reason "..."`：用新的不可变 candidate 替代待审 proposal。
- `gm propose-update <id> --from-file <candidate.md> --reason "..."`：创建受并发保护的 canonical update proposal。
- `gm search "<query>"`：搜索 source 与 canonical knowledge，结果携带 `source_ids`。
- `gm show <id>` / `gm related <id>`：读取对象与 typed relations。
- `gm rebuild-index`：从文件重建 SQLite FTS5。
- `gm lint`：只读检查 wikilink/relation、claim 来源、raw 哈希、proposal/candidate/base 完整性；孤立 canonical 页面以 warning 报告。
- `gm backup manifest [--output <path>]`：生成整个 `vault/raw/` 的 SHA-256 manifest；默认写入本地 `data/backups/`。
- `gm backup create <外部目录>`：增量复制 raw source record 与 content/blob；已存在同 hash 文件跳过，不覆盖冲突文件。
- `gm backup verify <外部目录>`：校验备份 manifest、文件大小和 SHA-256。
- `gm backup restore <外部目录> [--apply]`：默认只显示恢复计划；`--apply` 只写入本地缺失文件，冲突时不写入任何文件并重建索引。
- `gm status` / `gm doctor`：查看状态与一致性检查。
- `gm recover`：幂等续做中断的 canonical approval；遇到第三方修改时报告 blocked。

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

## Approval recovery

Canonical approve 在写入任何 target 前，会原子创建 `system/recovery/approve-<proposal-id>.json`。Journal 包含预期 target/proposal 完整文本、前后哈希和 audit operation ID。正常完成后 journal 自动删除；中断后 `gm doctor` 会报告，`gm recover` 按 target → proposal → audit → index 顺序幂等续做。

`defer` 不会修改 candidate 或 canonical，且 deferred proposal 以后仍可 approve、reject 或 revise。`revise` 不覆盖旧 candidate：它创建新的 candidate/proposal，把旧 proposal 标记为 `superseded`，并通过 `revision_of`、`superseded_by` 和 typed `supersedes` relation 保留完整审阅链。Update revision 总是以执行修订时的 current canonical 为新 base。

## Lint

`gm lint` 不写入文件、不重建索引。它把会破坏审阅或来源链的情况列为 `errors`，例如失效 relation/wikilink、无效 `source_id`、无来源 claim、raw 内容哈希不匹配，以及 proposal 的 candidate/base/target/hash 不一致；命令在存在 errors 时以非零状态退出。没有来源或关系的 canonical 页面、未被 proposal 引用的 candidate/base snapshot 则列为 `warnings`，方便人工判断是否确为孤立材料。

## Raw backup 与恢复

`vault/raw/` 同时包含不可变 raw payload 和 source Markdown；两者必须一起备份才能保留来源版本链。`gm backup create` 只接受仓库外、由用户明确指定的本地目录，备份内会写 `global-memory-raw-manifest.json`。增量运行会跳过已验证的相同文件；若目标目录出现同路径不同 hash，命令报告 conflict，且不会覆盖文件或更新 manifest。

恢复默认 dry-run。执行 `--apply` 前会先校验备份 manifest 与所有备份文件；只恢复本地缺失文件。若任一目标同路径但 hash 不同，恢复整体停止，不覆盖本地内容。恢复成功后自动重建 SQLite 索引。此机制不替代 Git：canonical Markdown、proposal 和文档仍应由 Git 或独立仓库备份保护。

## Provider-neutral model proposal

模型处理器的第一版是“外部 candidate 导入器”，而不是 SDK 或云端调用器。请在你选择的模型环境中生成 UTF-8 candidate Markdown，再通过 `gm model-propose` 显式导入。Candidate 必须使用 `status: proposal`，并在 `source_ids` 中保留输入 source；系统将不可变保存 candidate、生成 diff，并记录 `provider`、`model`、`prompt_version`、可选 `prompt_sha256`、输入 source/content hash 与不确定性。

若 candidate 类型为 `claim`，还必须填写 `evidence[]`、`applicability[]` 与 `uncertainty`。每条 evidence 需要来源、位置、摘录、`supports` / `contradicts` / `context` 方向和理由；详见 [SCHEMA.md](SCHEMA.md)。

这条命令默认不会发送 raw、prompt 或任何文件到 provider；它也不会自动批准模型结论。模型输出仍要经过 `show → approve/reject/defer/revise`，并适用现有并发保护和 approval recovery。

恢复采用 roll forward：当前文件必须仍是 journal 记录的写前或写后状态。若用户在中断后又修改了 target/proposal，恢复会返回 blocked 并保留 journal，不会覆盖第三种状态。Recovery journal 含可能敏感的候选正文，仅保存在本地并由 `.gitignore` 排除。

## 进一步阅读

从 [INDEX.md](INDEX.md) 开始。数据格式见 [SCHEMA.md](SCHEMA.md)，系统边界见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)，当前接管点见 [PROJECT_STATE.md](PROJECT_STATE.md)。
