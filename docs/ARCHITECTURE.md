# Architecture

## 分层

```text
输入边界        URL | stdin/text | explicit local path
                    ↓
真相层          capture event → source Markdown → immutable content object
                    ↓
提议层          deterministic/model processor → proposal + candidate + diff
                    ↓ 人工批准
canonical 层    knowledge | frontier | action
                    ↓
派生层          SQLite metadata + typed relations + FTS5
                    ↓
读取边界        search → show → related → raw provenance
```

### 真相层

Raw content 以 bytes 的 SHA-256 命名并独占创建。Source record 是独立 Markdown，保存来源身份、捕获时间、保存理由、content hash 和相对路径。同内容不同来源共用 content object，但 source record 不合并。

同一 canonical URL 属于一个 source family。普通 capture 只做已有来源去重；显式 `--refresh` 才重新抓取。变化内容产生带 `version_number` 和 `previous_version_id` 的新 immutable source record；即使内容回到旧 hash，也保留为新的时间版本。

### Proposal gate

Processor 无权直接写 canonical。它写入一个 proposal record 和一个不可变 candidate，proposal 内嵌 unified diff。Approve 校验 pending 状态、candidate ID、类型、关系和 SHA-256 后才创建或更新 canonical，并写 `approved_via`。

Proposal 可暂缓为 `deferred`，之后仍可继续批准、拒绝或修订。Candidate revision 创建新的不可变 candidate/proposal，旧 proposal 标记为 `superseded`，双向记录 `revision_of`/`superseded_by` 并保留 typed `supersedes` relation。Update revision 以修订时的 current canonical 重新建立 base snapshot，不继承过期并发令牌。

Source refresh 也生成 proposal，但语义是“确认新证据版本”，没有 canonical candidate。批准后新 source 才进入常规 compile/review 流程；refresh approval 本身不修改 knowledge、frontier 或 action。

Canonical update 使用三份材料：不可变 base snapshot、不可变 candidate、审批时的 current target。Proposal 保存 base/candidate SHA-256。Current 与 base 不一致时审批必须失败；`proposal show` 动态附加 Base→Current diff，与已保存的 Base→Candidate diff 共同构成三方审阅材料。系统不自动选择或合并任一方。

### 派生索引

索引重建先在同目录创建临时 SQLite，关闭连接后用原子替换发布，避免半写数据库。索引包含对象元数据、typed relations 和 FTS5；中文短语额外使用局部 `LIKE` fallback。任何索引丢失都不损害真相层。

### 只读完整性检查

`gm doctor` 侧重 source version、raw hash、索引和 recovery journal；`gm lint` 扩展检查对象引用、claim provenance、wikilink、proposal candidate/base/target/hash 和 revision lineage。Lint 不重建索引、不改变对象；断链和哈希不一致是 error，孤立 canonical 页面与未引用的审阅快照是 warning。

### Raw backup

Raw manifest 从 `vault/raw/` 的全部文件生成 SHA-256 清单，包含 source record 和 content/blob。`gm backup create <外部目录>` 将缺失文件独占复制到备份目录，相同 hash 跳过，同路径不同 hash 停止为 conflict；只有无 conflict 时才发布新的备份 manifest。`gm backup restore` 默认 dry-run，`--apply` 先验证备份，再只恢复本地缺失文件；任一冲突阻止全部写入。恢复后 SQLite 由真相层重建，Git 仍负责 canonical Markdown 与代码历史。

## 一致性边界

- Capture 顺序：raw content → source Markdown → append audit event → rebuild index。索引失败时文件仍可重建，调用者会看到错误。
- Approve 顺序：完整校验 candidate → 创建 recovery journal → 原子写 canonical → 原子更新 proposal → audit → rebuild；中断后由 `gm recover` 幂等续做。
- Source record 目前不可就地更新，因此 processing state 由 proposal 集合推导，`inbox` 不修改 raw metadata。
- Refresh 顺序：重新抓取 → 比较最新 hash → 追加 content/source → 重建索引 → 幂等创建 refresh proposal。若 proposal 创建中断，再次 refresh 同一内容会补建同一个 proposal。
- Update 顺序：验证 candidate → 保存 base/candidate → 显示 diff → 审批时重验两份 hash 与 current → 原子写 target → 更新 proposal → audit → 重建索引。并发冲突保持 pending，必须重新提案。
- Canonical approve 在 target 写入前先创建单文件 recovery journal，随后阶段化写 target、proposal、audit、index。每一步都可重复；audit 用 operation ID 去重。全部成功后才删除 journal。

### Approval recovery

Recovery journal 保存写前 hash 和确定的写后 payload。`gm recover` 只接受当前文件等于写前或写后 hash，并继续完成剩余阶段；第三种状态视为外部并发修改，保持 blocked。该机制不提供跨文件原子性，而是提供可检测、可续做、不会静默覆盖的最终一致性。

## 可插拔边界

第一版 processor 是 `deterministic-excerpt-v1`，只为验证治理闭环。未来模型处理器必须接收 source/context pack，输出同一 proposal schema，并记录 provider、model、prompt/version、时间和不确定性；不得绕过审批。

## 威胁与隐私模型

- 默认只访问用户显式提供的 URL 或路径。
- 不上传私人资料，不执行网页脚本，不使用云数据库。
- 路径字段必须解析在仓库内；输入文件读取是用户通过命令明确授权的例外。
- 二进制 raw 默认 Git ignore，但“被忽略”不等于“已备份”，需要单独完整性与备份策略。
