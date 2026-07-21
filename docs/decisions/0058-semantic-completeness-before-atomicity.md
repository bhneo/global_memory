# ADR 0058: Semantic Completeness Precedes Atomicity

- Status: accepted
- Date: 2026-07-19

## Decision

Global Memory does not infer atomic Claim boundaries by splitting prose at
punctuation or conjunctions. Regex inspection may identify that a statement is
compound, but the statement remains proposal-gated until a model or human
provides explicit, self-contained semantic items.

Every proposed Claim records semantic completeness. Headings, continuations,
trailing clauses and other sentence fragments receive `fragment` plus missing
coverage and cannot enter Working. Literal occurrence in an Extraction proves
only textual location; it does not prove that a substring is a proposition or
that evidence entails it.

Working-quality review examines actual fallback markers and object structure,
not only `compiler_version`. Therefore Agent-labeled objects cannot bypass the
same source-only remediation applied to deterministic fallbacks. Remediation is
reversible and preserves exact pre-images, version snapshots, Source/Raw links
and immutable events.

Operational Agent-acceptance Experiments remain auditable knowledge objects but
are excluded from the default human semantic graph. The `all` graph profile and
technical review views retain them.

## Consequences

Daily and Weekly models must emit fewer, better formed Claims rather than one
compound paragraph that the core mechanically expands. Some candidate bundles
will stop at proposal review instead of producing Working nodes; this is the
intended cost of preventing false knowledge structure. No change is made to
Trusted/Canonical policy, immutable Raw, or the explicit Canonical gate.
