# Architecture

## M8 trustworthy evolution pipeline

```text
immutable Raw/Source
  -> Working object
  -> revalidate schema + Raw + provenance + Evidence
  -> duplicate/related/contradiction/independence/drift checks
  -> immutable hash-bound Consolidation Receipt
  -> explicit support/refine/limit/contradict/supersede action
  -> safe Working evolution OR Trusted Revision/Exception
  -> narrow Claim/Concept Trusted Promotion
  -> human-only Canonical Promotion
```

Governance records live beside, not inside, the canonical truth directories: consolidation receipts in `vault/receipts/consolidation/`, demotion events in `vault/receipts/demotions/`, versions in `vault/archive/versions/`, exceptions in `vault/exceptions/`, and promotion cards in `vault/promotions/`. SQLite, reports and Obsidian views remain rebuildable.

The compiler may cheaply create or update Working. It may not silently reset Trusted, overwrite its semantic body, auto-demote it, or write Canonical. High-severity drift and Canonical conflict route to Exception rather than mutation.

## M7 consolidation pipeline

```text
immutable raw -> rebuildable derived -> validated Working
Working -> periodic consolidation + type policy -> Trusted
Trusted -> promotion card -> explicit human approval -> Canonical
                         \-> exception queue when judgement is required
```

Working and Trusted share stable IDs under `vault/memory/`. Proposals/candidates remain compiler audit records rather than the routine approval queue. Canonical stays in `vault/knowledge`, `vault/frontier`, and `vault/action`; automatic jobs and migrations have zero Canonical write authority. See ADR 0033-0041.

## M6 pipeline

```text
immutable capture
  -> bounded daily triage (derived extraction + quality assessment + lifecycle)
  -> capture-only searchable source OR explicit compile selection
  -> existing-knowledge lookup + atomicity/classification
  -> source/source-collection bundle proposal
  -> item-level review + recovery journal
  -> canonical knowledge (only after gate)

secondary source -> formal follow-up -> primary capture/verification
system/runs + SQLite + quality/lifecycle JSON = rebuildable derived layers
```

Routine article capture stops after bounded incremental triage by default. A source does not need to become a proposal or canonical object to remain useful and searchable. Expensive semantic compilation and primary-source verification are triggered by value, repeated use, conflict, or promotion rather than by capture itself; see ADR 0030.

M6 不引入 graph database：图仍由 Markdown typed relations 表达，SQLite 只做可重建检索/遍历。Corpus distillation 只生成候选图；它不得绕过 review gate。

## 分层

```text
输入边界        URL | stdin/text | explicit local path
                    ↓
真相层          capture event → source Markdown → immutable content object
                    ↓
派生抽取层      extraction (input hash + extractor version + page/span)
                    ↓
作品身份层      source captures → auditable work enrichment proposal
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

Raw content 以 bytes 的 SHA-256 命名并独占创建，统一存放在 `vault/raw/objects/sha256/<前2位>/<次2位>/<完整哈希>`。路径不含 capture kind、URL 后缀或显示扩展名。Source record 是独立 Markdown，保存来源身份、捕获时间、保存理由、content hash、MIME、原始文件名、建议显示扩展名和对象相对路径。同内容不同来源共用 content object，但 source record 不合并。

旧的 `raw/<kind>/content|blobs` 通过 `gm migrate raw-store` 迁移。迁移先备份 source record，再独占写全局对象，使用本地 journal 逐条更新 source，完成后校验全部引用。旧对象默认保留；只有独立、明确的清理动作才可删除。

同一 canonical URL 属于一个 source family。普通 capture 只做已有来源去重；显式 `--refresh` 才重新抓取。变化内容产生带 `version_number` 和 `previous_version_id` 的新 immutable source record；即使内容回到旧 hash，也保留为新的时间版本。

### Derived extraction

`data/derived/extractions/` 保存可删除、可重建的正文视图。每份 extraction 绑定 source/content/input SHA-256，并记录 extractor、version、MIME、编码、页数、字符数、warnings 与状态。HTML 抽取移除脚本和明显导航模板；PDF 使用 optional `pypdf` 并写入 `<!-- page: N -->` 边界。扫描 PDF 不做 OCR，而是产生明确 warning。任何提取错误只写 derived error record，不修改 raw/source。

### Source capture 与 logical work

Source 表达一次具体捕获，work 表达现实世界的论文、文章或项目身份。多个 capture 可通过 `work_enrichment` proposal 聚合到同一个 work；source provenance 永不被 work 合并覆盖。第一版只对显式 arXiv ID 或 source 中可靠 arXiv ID 做确定性识别，不用模糊标题自动合并。

### Proposal gate

Processor 无权直接写 canonical。它写入一个 proposal record 和一个不可变 candidate，proposal 内嵌 unified diff。Approve 校验 pending 状态、candidate ID、类型、关系和 SHA-256 后才创建或更新 canonical，并写 `approved_via`。

`gm compile` 的主要输出是 Compile Bundle Proposal。Compiler 先从 metadata/FTS 检索已有对象，再决定 create/update，并把 claim、concept、question、tension、hypothesis、analogy 等有意义候选放入一个 bundle。每个 item 有独立 candidate/base/hash/diff/decision；未审批 item 不写 canonical。按 item 或整体批准先校验全部目标，再创建多目标 recovery journal，固定执行 targets → proposal → audit → index。中断后只允许幂等 roll-forward，第三状态保持 blocked。

Provider 接口只返回结构化 bundle，不写文件、不批准。默认 deterministic fallback 能力有限且显式标记；外部 provider 可以实现同一接口，但核心不绑定 SDK。

Deterministic fallback 将 `Claim:`、`Experiment:`、`Decision:` 等显式标记解析为类型块：从标记后的标题开始，完整保留到下一个显式类型标记。多标记仍拆成多个 item；没有显式标记时仍只保留第一段逐字材料。该规则只做无损分块，不推断 receipt 的知识类型、重要性或真实性。

`JsonBundleProvider` 是第一条外部 adapter：它只读取用户显式提供的本地 JSON item 列表。Cursor、Claude 或其他模型调用、费用、授权与网络行为都发生在核心之外；导入后仍执行相同 schema、provenance、diff 和 proposal gate。

Proposal 可暂缓为 `deferred`，之后仍可继续批准、拒绝或修订。Candidate revision 创建新的不可变 candidate/proposal，旧 proposal 标记为 `superseded`，双向记录 `revision_of`/`superseded_by` 并保留 typed `supersedes` relation。Update revision 以修订时的 current canonical 重新建立 base snapshot，不继承过期并发令牌。

Source refresh 也生成 proposal，但语义是“确认新证据版本”，没有 canonical candidate。批准后新 source 才进入常规 compile/review 流程；refresh approval 本身不修改 knowledge、frontier 或 action。

Canonical update 使用三份材料：不可变 base snapshot、不可变 candidate、审批时的 current target。Proposal 保存 base/candidate SHA-256。Current 与 base 不一致时审批必须失败；`proposal show` 动态附加 Base→Current diff，与已保存的 Base→Candidate diff 共同构成三方审阅材料。系统不自动选择或合并任一方。

Claim candidate 的 `evidence[]` 区分 quote、paraphrase、translation、table_value、figure 与 calculation。Quote 必须能逐字回验 extraction span；翻译保留原文；表格值保留单位；计算保留输入 evidence 与方法。`applicability[]`、`confidence` 与 `uncertainty` 分别表达适用范围、当前判断强度和未决限制。旧 evidence schema 继续兼容读取。

### 派生索引

索引重建先在同目录创建临时 SQLite，关闭连接后用原子替换发布，避免半写数据库。索引包含对象元数据、typed relations 和 FTS5；中文短语额外使用局部 `LIKE` fallback。任何索引丢失都不损害真相层。

`vault/archive/` 保存从活动 canonical 目录物理移出的最小墓碑，不进入全文索引。墓碑保留原对象 ID、source_ids、归档理由和 approval 身份，使历史 proposal 的 target 可以被 lint 验证；raw source 与 proposal 审计材料不随 canonical 清理而删除。

### 只读完整性检查

`gm doctor` 侧重 source version、raw hash、索引和 recovery journal；`gm lint` 扩展检查对象引用、claim provenance、wikilink、proposal candidate/base/target/hash 和 revision lineage。Lint 不重建索引、不改变对象；断链和哈希不一致是 error，孤立 canonical 页面与未引用的审阅快照是 warning。

`gm maintain` 是维护入口而不是新的真相层。默认模式只组合 doctor、lint、raw integrity，并汇总 inbox、proposal、receipt、follow-up、弱证据、历史对象、建议动作和 Obsidian 视图新鲜度，不写任何文件。只有显式 `--rebuild-derived` 才重建 SQLite 与 Obsidian 导航；该模式仍不得修改 raw、proposal 或 canonical。

`gm audit contradictions` 是另一条只读治理路径：它扫描 canonical claim 的结构化 evidence 与 typed relation，报告内部 supports/contradicts 并存和跨 claim 的显式 `contradicts` 边。冲突本身是可保留的认知状态，不是自动修复项；audit 不写入 Markdown 或派生索引。

`gm synthesize` 是受治理的写入前阶段：它把多个 canonical claim 的显式材料整理为 `synthesis` candidate，并记录每个输入 claim 的完整 hash。它不推断新事实或裁决冲突；approval 之前重验输入 hash，随后仍通过普通 candidate/recovery gate 写入 canonical synthesis。当前没有自动调度。

`gm discover` 是可解释的关联发现阶段：共享来源、标签、relation target 和确定性关键词会成为候选信号，proposal 保留所有信号与输入 hash。它没有 canonical candidate；approve 只审计“已审阅”，不写 relation。关系采纳仍必须通过单独的 canonical update proposal。

### Context Pack

`gm context` 位于读取边界，不是 processor 或写入路径。它依据明确 query、profile、filters 与 token budget 对检索/关系命中做确定性裁剪；输出保留路径、文档 hash、来源 ID、evidence 和选择理由。直接入选的 source 默认只使用 family 最新版本；`archived` canonical 默认退出活动 Context Pack，只被 archived canonical 引用且没有活动 canonical 引用的 source 也随之退出。历史材料仍保留在真相层供 `search`/`show` 和审计回溯。Context Pack 不写入 Markdown、SQLite 或审计日志，不缓存为真相层，也不提升任何命中或摘录的认知状态。

M5 profile 层在同一读取边界上扩展：execution 优先 project/goal/architecture/decision/failure，research 优先 claim/concept/source/evidence/question，exploration 优先 intuition/tension/analogy/anomaly/hypothesis。Profile 可组合，并接受 project/domain/type/status/time/source-kind filter。召回顺序为分字段 FTS/metadata → 有界 typed relation traversal → extraction/source verification → token 裁剪。默认不含 proposal；显式包含时必须保留其 pending/deferred 等状态。

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

### Read-only MCP

`gm mcp stdio|http` 把既有 Context Pack、搜索、对象读取、source extraction 与维护 inventory 暴露为五个 provider-neutral 只读工具。MCP 不新增真相层，不暴露 capture/compile/approve/rebuild/delete/canonical write。stdio 用于本地助手；Streamable HTTP 默认仅绑定 localhost，并校验 Origin、限制请求大小，非 loopback 必须提供 bearer token。远程 ChatGPT 接入仍需要 TLS、认证及可信 tunnel/deployment；详见 ADR 0031。

第一版 processor 是 `deterministic-excerpt-v1`，只为验证治理闭环。`external-model-candidate-v1` 是 provider-neutral 导入边界：它接收用户明确提供的 candidate Markdown，而不在仓库内调用 SDK 或网络服务；输出仍是同一 proposal schema，并记录 provider、model、prompt version/hash、输入 source/content hash 和不确定性。未来实际模型适配器必须沿用该审计字段与 proposal gate，不得绕过审批或默认外传私有 raw。

## 威胁与隐私模型

- 默认只访问用户显式提供的 URL 或路径。
- 不上传私人资料，不执行网页脚本，不使用云数据库。
- 路径字段必须解析在仓库内；输入文件读取是用户通过命令明确授权的例外。
- 二进制 raw 默认 Git ignore，但“被忽略”不等于“已备份”，需要单独完整性与备份策略。
