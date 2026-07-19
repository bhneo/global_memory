# ADR 0057: Cognitive Consolidation Is a Non-Factual Layer

- Status: accepted
- Date: 2026-07-19

## Decision

Input Episodes, Reflections and Weekly Cognitive Synthesis are first-class local
Markdown objects, but they are not Evidence or governed knowledge tiers.
Reflection and Cognitive Synthesis carry explicit truth layers, are never
execution-safe, and cannot carry Memory Tier. Their content may inform an
external Agent's Semantic Bundle, but knowledge still enters only through the
existing Working compiler boundary.

Daily and Weekly Dream are provider-neutral artifact protocols. The core queues,
validates, stores and compiles explicit artifacts; it does not call a model,
manage an Agent lifecycle, execute tools, or run experiments. Both pipelines
assert zero Canonical writes. Hypothesis candidates must be falsifiable, cite
supporting Reflections and Sources, retain counterarguments, and remain
hypothetical.

Daily artifacts are fully schema-checked before the first cognitive write and
use deterministic immutable Reflection identities so an interrupted run can be
resumed safely. Daily rejects Hypothesis, Analogy and Synthesis semantic items.
Weekly Synthesis identity binds every cognitive field, and each Working bundle
must name the exact supporting Reflection subset whose Sources cover the bundle
Source. Attaching all weekly Reflections to every knowledge item is forbidden.

Research/Exploration Context may include labeled Reflection and Cognitive
Synthesis. Execution Context excludes both. Third-party Agents submit Session
Experience as Input and never write Knowledge directly.

## Consequences

Global Memory can preserve cognitive change and cross-source insight without
laundering interpretation into fact or weakening the M8.1.2 Trust boundary.
The architecture remains a scientific memory layer rather than an Agent runtime.
