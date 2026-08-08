# Architecture

Galois is a **local-first memory engine**: Markdown and immutable raw files are
the truth; indexes and views can be deleted and rebuilt; AI assistants think
outside the core and write only through gated paths.

This page is the map. Object fields live in [DATA_MODEL.md](DATA_MODEL.md);
Daily/Weekly cognition in [COGNITIVE_CONSOLIDATION.md](COGNITIVE_CONSOLIDATION.md);
assistant wiring in [AGENT_INTEGRATION.md](AGENT_INTEGRATION.md) and
[MCP_INTEGRATION.md](MCP_INTEGRATION.md).

## Big picture

```text
                    ┌─────────────────────────────────────┐
  URL / file / text │  Capture                            │
                    └─────────────────┬───────────────────┘
                                      ▼
                         Immutable Raw + Source
                                      │
              ┌───────────────────────┴───────────────────────┐
              ▼                                               ▼
     Evidence path                                   Cognition path
  (what we may treat as knowledge)              (how we think about it)
              │                                               │
              ▼                                               ▼
         Working ──► Trusted ──► Canonical*            Input → Reflection
              │         │                                   → Synthesis
              │         └── Exceptions / Promotions              │
              │                                                  │
              └────────── optional candidates ◄──────────────────┘
                                      │
                                      ▼
              SQLite / FTS / Obsidian views  (rebuildable)
                                      │
                                      ▼
              CLI + MCP read surface  (bounded Context Packs)
```

\*Canonical writes require an explicit human promotion approval. Automatic
jobs never gain that authority.

**Core rule:** the memory core does **not** call models, run tools, or manage
agent lifecycles. Assistants (or you) author artifacts; Galois validates,
stores, retrieves, and enforces write policy.

## The two paths

| Path | Purpose | Becomes “fact”? |
|---|---|---|
| **Evidence** | Source → Evidence → Working → Trusted → Canonical | Only as far as tier + your approval allow |
| **Cognition** | Source → Input → Reflection → Direction / cross-direction Synthesis | **Never by itself.** May propose Working candidates |

Research reads may include Reflection/Synthesis **with labels**. Strict
execution reads exclude them.

Memory Tier (“is this worth keeping?”) and Epistemic Status (“what do we
actually know?”) are independent. A Trusted open question is still an open
question.

## Layers (what lives where)

| Layer | Role | Durable? |
|---|---|---|
| **Input boundary** | Explicit URL, pasted text, or local path you authorize | Event |
| **Truth** | Source Markdown + content-addressed raw bytes | Yes — append-only |
| **Derived extraction** | Text/pages pulled from HTML/PDF for search and quotes | No — rebuildable |
| **Memory** | Working / Trusted objects under `vault/memory/` | Yes |
| **Canonical** | Scarce committed knowledge under `knowledge/` / `frontier/` / `action/` | Yes — gated |
| **Cognition** | Inputs, Reflections, Syntheses | Yes as research artifacts, not Evidence |
| **Governance** | Receipts, demotions, exceptions, promotion cards | Yes — beside knowledge, not inside it |
| **Derived index / views** | SQLite, FTS, Obsidian navigation | No — rebuildable |
| **Read boundary** | `search` / `show` / `related` / `context` / MCP | Read-only by default |

### Truth layer (short form)

- Raw bytes live at `vault/raw/objects/sha256/...`, named only by content hash.
- Each **Source** is its own Markdown record (identity, time, reason, MIME,
  hash, path). Same bytes can be shared; Source records are never merged away.
- Refresh creates a **new** immutable Source version; it does not overwrite.
- Extraction errors and warnings stay in derived storage; they never rewrite Raw.

Details: identity rules and versioning → [DATA_MODEL.md](DATA_MODEL.md).

## How material moves

### 1. Capture (cheap by default)

```text
authorize input → write raw object → write Source → index
```

A captured Source can stay **searchable and source-only** forever. Expensive
compilation is for value, conflict, reuse, or promotion — not for every URL.

### 2. Cognition loop (assistant outside, core validates)

```text
Source → Input Episode → Reflection → (optional) Working bundle
                              ↓
                    Direction Synthesis
                              ↓
              optional Cross-direction candidate
              (mechanism, boundary, difference,
               counterarguments, gap, verification)
```

- **Daily** digests a small Input queue; every candidate gets an explicit
  disposition (create / update / reuse / source-only / review / defer).
- **Weekly** is a review *cadence*, not the identity of a Synthesis. Scope
  follows registered research directions
  ([RESEARCH_DIRECTIONS.md](RESEARCH_DIRECTIONS.md)).

### 3. Knowledge evolution (trust without laundering doubt)

```text
Working  →  periodic consolidation + policy  →  Trusted
Trusted  →  promotion card  →  your approval  →  Canonical
                ↘ exception queue when judgement is required
```

- Working may be created/updated cheaply by the compiler.
- Trusted changes need hash-bound receipts and explicit support / refine /
  limit / contradict / supersede semantics.
- Policy updates do **not** bulk-demote Trusted; drift and Canonical conflict
  go to Exceptions, not silent mutation.
- Proposals and candidates are audit material; they are not a license to skip
  the Canonical gate.

### 4. Read path

```text
query + profile + budget
  → FTS / metadata hits
  → bounded relation expansion
  → optional extraction / source check
  → Context Pack (paths, sources, evidence, selection reasons, labels)
```

Profiles (examples): **research** favors claims/concepts/sources;
**exploration** favors tensions/analogies/hypotheses; **execution** favors
project decisions and failures, and excludes non-factual cognition layers.

`galois context` and the default MCP tools are **read-only**. They do not
promote anything they return.

## Write gates (non-negotiable)

| Action | Allowed writer |
|---|---|
| Raw / Source | Capture (and opt-in text capture via explicit MCP flag) |
| Working | Compiler / consolidator under schema + provenance rules |
| Trusted | Consolidation with Receipt; never silent semantic overwrite |
| Canonical | **Human** `promotion approve` only |
| Indexes / Obsidian views | Rebuild tools only (`maintain --rebuild-derived`, etc.) |

Interrupted Canonical/Trusted writes use a recovery journal: resume only if
on-disk bytes match the expected before- or after-image; otherwise stay
**blocked** rather than guess.

## Integration surface

Assistants talk to Galois through the **Agent Memory Gateway**
(`galois mcp stdio|http`):

| Default (read-only) | Opt-in |
|---|---|
| `memory_capabilities` | Explicit-consent text capture only |
| `memory_context` | (still cannot compile, promote, or rebuild) |
| `memory_search` | |
| `memory_show` | |
| `memory_source` | |

Ordinary MCP answers omit internal paths, hashes, and maintenance noise; full
diagnostics stay on the local CLI. HTTP binds to localhost by default and
checks Origin / size; non-loopback requires a bearer token.

Host templates: [`adapters/hosts/`](../adapters/hosts/).

## Integrity and maintenance

| Command | Role |
|---|---|
| `galois doctor` | Sources, raw hashes, index, recovery journal |
| `galois lint` | References, provenance, proposal/candidate lineage (no writes) |
| `galois maintain` | Read-only health + backlog summary |
| `galois maintain --rebuild-derived` | Rebuild SQLite / Obsidian views only |
| `galois recover` | Continue or report blocked approval journals |
| `galois backup` / `restore` | External raw backup; restore is dry-run unless `--apply` |

Losing the index never loses the truth layer.

## Threat and privacy model

- Only URLs or paths you explicitly provide are fetched or read.
- No private upload by the core, no page-script execution, no cloud database.
- Path fields must resolve inside the repository (explicit local capture is the
  authorized exception).
- Git-ignoring binary raw ≠ backed up; use the backup commands for integrity.
- “Local-first” is about storage ownership. Context sent to a **cloud**
  assistant still follows that provider’s retention rules.

## Where to go next

| If you need… | Read |
|---|---|
| Field-level object shapes | [DATA_MODEL.md](DATA_MODEL.md) |
| Daily / Weekly Dream contracts | [COGNITIVE_CONSOLIDATION.md](COGNITIVE_CONSOLIDATION.md) |
| Distillation / claim rules | [SEMANTIC_DISTILLATION.md](SEMANTIC_DISTILLATION.md) |
| Trust / Receipt / demotion | ADRs under `docs/decisions/` |
| Assistant operating contract | [AGENT_INTEGRATION.md](AGENT_INTEGRATION.md) |
| MCP protocol details | [MCP_INTEGRATION.md](MCP_INTEGRATION.md) |
| Public vs private vault boundary | [RELEASE_BOUNDARY.md](RELEASE_BOUNDARY.md) |
| Current engineering status | [../PROJECT_STATE.md](../PROJECT_STATE.md) |
