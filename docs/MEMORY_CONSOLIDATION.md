# Trustworthy consolidation and promotion governance

## 原则

Working 可自动演化；Trusted 的变化必须可验证、可解释、可回滚。Consolidation 是重新读取 Raw、Evidence、相关知识和冲突后生成可审计 Receipt，不是更新时间或增加计数。

## 单对象复核

```powershell
.\scripts\gm.ps1 consolidate object <object-id>
```

流程：

1. 绑定当前对象 SHA-256、Source IDs、Raw hashes 和 Evidence IDs。
2. 验证 schema、Raw、provenance、Evidence/entailment。
3. 完成 duplicate、related-object、contradiction、freshness、source-independence 和 drift 检查。
4. 生成不可变 Consolidation Receipt。
5. Receipt 仅在其 `object_sha256_after` 仍等于当前对象时有效。

Claim 额外复核 atomicity、coverage、entailment、extraction、authority、applicability、conflict 与 confidence。Concept 的独立复用按不同 `work_id` 计算，不按两个 URL 计算。Question/Tension/Hypothesis/Analogy/Synthesis 保持其类型特有边界，不因被长期保留而变成事实。

## Promotion Policy v2

自动 Trusted 当前只开放 Claim 与 Concept：

- Claim：atomic、full coverage、full entailment、good extraction、足够 authority、明确 applicability、存在 supporting evidence、无 unresolved contradiction、无高风险 drift、无待验证 Revision，并有当前有效 Receipt。
- Concept：至少两个真正独立的 `work_id`、无 duplicate/merge conflict、定义稳定且有当前有效 Receipt。
- Question、Tension、Hypothesis、Analogy、Anomaly、Intuition、Synthesis：只进入 Candidate/Queue，默认不自动 Trusted。

手工 Trusted 需要明确 reason。Canonical 仍需 promotion card + 用户 approve：

```powershell
.\scripts\gm.ps1 promote <id> --to trusted --reason "长期值得保留"
.\scripts\gm.ps1 promote <id> --to canonical --reason "高影响稳定知识"
.\scripts\gm.ps1 promotion approve <promotion-id> --lock
```

## Trusted 更新

- `support` / `metadata_only`：保留 Trusted、合并来源/Evidence、保留 trust、创建版本快照与新 Receipt。
- `refine` / `limit` / `supersede`：原 Trusted 文件保持不变；创建 Working Revision、对象级 diff 与 `needs_revalidation`。
- `contradict`：保留原对象和双方 Evidence；tier 不变，`epistemic_status: contested`；创建 Exception 和 Receipt；暂停自动晋升。
- `demote`：只允许显式用户操作，必须产生 Demotion Event 和旧版本快照。
- Canonical 冲突：标记 contested 并创建 Canonical Exception；绝不自动降级。

## Weekly

```powershell
.\scripts\gm.ps1 consolidate weekly
```

`consolidate weekly` first runs a bounded Daily admission catch-up (25 sources
by default), then reviews the resulting Working/Trusted set. Use
`--admit-limit N` to change the bound or `--skip-daily-admission` for an
audit-only review of already admitted memory. The catch-up preserves the same
Working-only and zero-Canonical-write boundaries as `consolidate daily`.

Long unstructured sources without explicit `Claim:`, `Concept:`, `Question:` or
other typed markers do not use the deterministic first-paragraph fallback.
They remain searchable as immutable sources and receive a terminal
`source_only` compile record. Weekly also emits a read-only
`working_quality_review` for legacy deterministic fallbacks; remediation must
use an explicit recompile or governed source-only migration.

Use `gm migrate working-quality --dry-run` to inspect the deterministic set and
`gm migrate working-quality` to apply it. Apply stores exact pre-images under
`data/backups/`, adds immutable version snapshots, marks affected Working
objects `historical + archived`, and appends audit events. It never edits Raw or
Canonical.

Weekly 报告区分真正完成 Receipt、仅扫描、复核失败、语义变化、Promotion、Demotion、Conflict、Exception 和 Drift Warning。核心字段包括 sources processed、objects considered、receipts completed/failed、unchanged/supported/refined/limited/contradicted/superseded、promotions/demotions、canonical exceptions、working revisions、review time。

## Drift

```powershell
.\scripts\gm.ps1 audit drift
```

检测 uncertainty erasure、correlation→causation、secondary→primary、analogy→fact、unsupported synthesis additions 和 translation strengthening。Audit 本身 `writes: 0`；Weekly 只把 high severity 项送入 Exception。

## Migration

```powershell
.\scripts\gm.ps1 migrate epistemic-status --dry-run
.\scripts\gm.ps1 migrate epistemic-status
.\scripts\gm.ps1 migrate epistemic-status --verify
```

迁移自动备份、保存 `legacy_status`、幂等重跑，不修改 Canonical 正文。未知旧状态降级到 `working + unknown`；Trusted Question/Hypothesis/Analogy 分别保留 open_question/hypothetical/exploratory_analogy。
