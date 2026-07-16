---
id: "receipt_3647991d1ef5027a284f"
type: "receipt"
status: "captured"
title: "M7 Cursor real acceptance"
created_at: "2026-07-16T22:15:57+08:00"
updated_at: "2026-07-16T22:15:57+08:00"
agent: "cursor"
project: "global-memory"
task: "M7 Cursor real acceptance"
receipt_version: 1
content_sha256: "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"
---

Experiment: Cursor completed the M7 real acceptance run on 2026-07-16 using the repository-root protocol and bounded Context Pack retrieval.

Task: answer "VIA interface-first robot control 的实验结论和适用边界是什么" from a bounded Context Pack rather than scanning the vault.

Observed read path:

- Cursor read `AGENTS.md`, `.cursor/rules/global-memory.mdc`, and `vault/INDEX.md` before memory work.
- `gm maintain` via `.\scripts\gm.ps1 maintain` (PowerShell aliases `gm` to `Get-Member`; used project script instead).
- `gm context "VIA interface-first robot control 的实验结论和适用边界是什么" --profile research --format markdown --token-budget 900` via `python -m global_memory`.
- Context Pack succeeded (1 selected, 0 omitted, budget not exhausted) but selected only the prior Codex M7 acceptance receipt, not the confirmed VIA claim or paper source.

Context Pack selection:

- ID: `source_46d0aad5afd18dd21899796f`
- Type/status: `source` / `captured`
- Truth layer: `source_capture`
- Path: `vault/raw/personal-notes/source-source_46d0aad5afd18dd21899796f.md`
- No canonical VIA claim ID was returned; no paper source ID in this pack.

Task result (evidence bounded to receipt content, not direct paper extraction):

- Main experimental conclusions: VIA reported zero-shot closed-loop manipulation through a browser visual/tool interface in six robosuite simulation tasks; overall minimal-prompt success ranged from 60% to 88%; CC-Fable reached 29/30 on three LIBERO-Goal tasks and 100% on Rainbow.
- Applicable boundaries: simulation only, mostly quasi-static tasks, ten seeds per configuration, main setup with cross-episode memory disabled.
- Not inferable from paper (per receipt): real-robot deployment, dynamic control, long-term memory, continuous learning, replacement of general robot-control policies.

Issues:

- PowerShell `gm` alias conflict required `.\scripts\gm.ps1` or `python -m global_memory`.
- Context Pack retrieval regression or ranking issue: full VIA query returned the Codex acceptance receipt instead of the confirmed VIA claim and paper source that Codex run reported after retrieval fixes.

Acceptance decision: Cursor read → task → receipt → proposal path executed. No canonical knowledge edited or approved. Context Pack evidence boundary is second-hand (session receipt summarizing VIA), not direct claim/source linkage.
