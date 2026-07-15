---
id: "proposal_dd90cb79a3e96422ce09d61c"
type: "proposal"
status: "pending"
title: "Work enrichment：VIA: Interface-first Robot Control"
created_at: "2026-07-15T16:18:43+08:00"
updated_at: "2026-07-15T16:18:43+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"]
relations: []
proposal_kind: "work_enrichment"
processor: "deterministic-work-identity-v1"
action: "create"
target_id: "work_arxiv_2607_11119"
target_path: "vault/knowledge/works/work_arxiv_2607_11119-via-interface-first-robot-control.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_dd90cb79a3e96422ce09d61c.md"
candidate_sha256: "6fa3f5588b01a0855aeecf611c64a18a16d72c82a6d4316342c9aaddef7abd59"
change_reason: "显式 work identity enrichment"
reviewed_at: null
review_reason: null
---

# Work enrichment：VIA: Interface-first Robot Control

Metadata enrichment 不修改 source capture；审批后只创建或更新 logical work。

## Diff

```diff
--- /dev/null
+++ vault/knowledge/works/work_arxiv_2607_11119-via-interface-first-robot-control.md
@@ -0,0 +1,35 @@
+---
+id: "work_arxiv_2607_11119"
+type: "work"
+status: "proposal"
+title: "VIA: Interface-first Robot Control"
+canonical_title: "VIA: Interface-first Robot Control"
+created_at: "2026-07-15T16:18:43+08:00"
+updated_at: "2026-07-15T16:18:43+08:00"
+aliases: [".tmp-via-2607.11119.pdf", "arxiv.org"]
+tags: []
+domains: []
+confidence: "medium"
+source_ids: ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"]
+relations: [{"type": "derived_from", "target_id": "source_5899fd47fd1a85ea3afcae99", "reason": "该 capture 属于此 logical work"}, {"type": "derived_from", "target_id": "source_86bad679192d3c34f728058b", "reason": "该 capture 属于此 logical work"}]
+work_type: "paper"
+authors: []
+published_at: null
+doi: null
+arxiv_id: "2607.11119"
+repository_url: null
+version: "v1"
+language: "und"
+same_work_as: []
+supersedes_version: null
+---
+
+# VIA: Interface-first Robot Control
+
+## Logical work identity
+
+- arXiv：`2607.11119`
+- Version：`v1`
+- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`
+
+此对象聚合现实世界作品身份，不替代任何 source capture 的 provenance。
```
