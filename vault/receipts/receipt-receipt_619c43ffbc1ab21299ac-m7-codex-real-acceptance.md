---
id: "receipt_619c43ffbc1ab21299ac"
type: "receipt"
status: "captured"
title: "M7 Codex real acceptance"
created_at: "2026-07-16T21:57:04+08:00"
updated_at: "2026-07-16T21:57:04+08:00"
agent: "codex"
project: "global-memory"
task: "M7 Codex real acceptance"
receipt_version: 1
content_sha256: "2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e"
---

Experiment: Codex completed the first real M7 agent acceptance run on 2026-07-16 using the repository-root protocol and the generated Obsidian entry.

Task: answer “VIA interface-first robot control 的实验结论和适用边界是什么” from a bounded Context Pack rather than scanning the vault.

Observed read path:

- Codex read `vault/INDEX.md` and invoked `gm context` with the research profile and a finite token budget.
- The first full natural-language query returned no items even though `gm search VIA` found the confirmed VIA claim. The cause was strict all-term matching with only an exact whole-query substring fallback.
- The Markdown renderer also displayed `status: None` because it read `status` instead of the Context Pack contract field `knowledge_status`.
- The implementation was corrected to retry distinctive whitespace-delimited terms only after an empty primary query, record the chosen `query_fallback`, and render `knowledge_status`.
- After correction, the original full query selected the confirmed canonical VIA claim and source material, preserved evidence, truth layer, paths, selection reason, and truncation state.

Task result:

- VIA reported zero-shot closed-loop manipulation through a browser visual/tool interface in six robosuite simulation tasks. Overall minimal-prompt success ranged from 60% to 88%; CC-Fable reached 29/30 on three LIBERO-Goal tasks and 100% on Rainbow.
- The result is bounded to simulation, mostly quasi-static tasks, ten seeds per configuration, and a main setup with cross-episode memory disabled. It is not evidence of real-robot deployment, dynamic control, long-term memory, continuous learning, or replacement of general robot-control policies.

Acceptance decision: Codex read → task → receipt → proposal is accepted after the two retrieval-contract repairs. No canonical knowledge was edited or approved during this run. Cursor and Claude acceptance remain outstanding.
