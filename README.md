# Galois

**Find the hidden structure.**

Local scientific memory for the AI assistants you already use.

Galois helps you keep research notes, papers, open questions and changing
beliefs in one place — with sources, contradictions and trust levels kept
visible — so Claude, Cursor, Codex and similar tools can reason over *your*
long-term knowledge instead of a chat window that forgets.

[Quick start](#quick-start) ·
[How it works](#how-it-works) ·
[Connect an assistant](#connect-an-assistant) ·
[Docs](#documentation)

<p align="center">
  <a href="./assets/hero/hero-hidden-structure.png">
    <img src="./assets/hero/hero-hidden-structure.png"
         alt="A scientific memory graph revealing structure across research directions."
         width="1200" />
  </a>
</p>

## What problem does this solve?

Most “AI memory” products remember **chat facts**: preferences, tickets, what
you said last week. That is useful for assistants and customer bots.

Researchers and builders often need something else:

- a paper you saved six months ago
- a belief that later evidence weakened
- an analogy that looks exciting but may only share vocabulary
- a question that is still open on purpose

Chat history and vector RAG blur those together. Galois is built so **sources,
interpretations and authority stay separate**, and so several assistants can
share one governed memory without silently rewriting what you believe.

> The goal is not to remember everything.  
> It is to notice what becomes visible when memory has structure.

## Who is it for?

- People who read papers, notes and project docs across weeks or months
- Users who already work with AI assistants and want those assistants to use a
  durable personal knowledge base
- Anyone who cares that “this is a hypothesis” is not treated as “this is a fact”

It is **not** a drop-in chat-memory API, a note app replacement, or an agent
that runs experiments for you.

## In one picture

| You do this | Galois keeps |
|---|---|
| Import a paper or article | The original source + provenance |
| Ask an assistant to reflect | Non-factual reflections and open questions |
| Review over time | Working → Trusted knowledge; Canonical only with your approval |
| Ask across topics | Bounded context with trust labels, not a blended summary |

Two paths stay separate on purpose:

<p align="center">
  <img src="./assets/architecture/trust-and-cognition.svg"
       alt="Evidence path: Source to Working to Trusted to human-approved Canonical. Cognition path: Source to Input to Reflection to Synthesis, which may suggest Working candidates but is never fact by itself."
       width="920" />
</p>

| Layer | Plain meaning |
|---|---|
| **Source** | What you captured (paper, page, note). Searchable ≠ accepted. |
| **Reflection / Synthesis** | Thinking aids. Useful, but **not facts**. |
| **Working** | Active knowledge under development |
| **Trusted** | Evidence-backed and policy-qualified |
| **Canonical** | Promoted only when **you** approve |

## How it works

<p align="center">
  <img src="./assets/architecture/from-fragments-to-structure.svg"
       alt="Fragments flow into structured memory, then into research directions, patterns and questions, then into qualified candidates and verification."
       width="920" />
</p>

1. **Capture** a URL or local PDF/HTML/text into an immutable source record.
2. **Daily reflection** — an assistant digests a small queue of new inputs
   (create / update / reuse / leave as source-only / review / defer).
3. **Weekly / direction review** — update durable research directions; propose
   cross-field links only when mechanism, boundary, difference and a
   verification path are stated. Zero new links is a valid outcome.
4. **Ask** through MCP: the assistant gets bounded context with truth and trust
   labels intact.

The **assistant does the thinking**. Galois does not call a model inside the
memory core. It stores, validates, retrieves and enforces write rules.

## Quick start

Requires **Python 3.11–3.13**.

```bash
git clone https://github.com/bhneo/global_memory.git
cd global_memory
python -m pip install -e ".[pdf]"
galois --help
galois doctor
```

Then connect an assistant (see below) and try:

```text
Use my Galois memory to answer this question.
Separate memory evidence, non-factual synthesis, uncertainty,
and your own interpretation.
```

Or import something concrete (give the assistant this repo and a URL or absolute path):

```text
Import this article or paper into my Galois memory:
<URL or absolute local file path>

Capture once, triage the returned Source, and report Source ID,
Input ID, duplicate status and warnings. Do not invent knowledge.
```

<details>
<summary><strong>Commands the assistant typically runs for import</strong></summary>

```powershell
.\scripts\galois.ps1 recover
.\scripts\galois.ps1 capture "<URL-or-path>" --input-type article   # or: paper
.\scripts\galois.ps1 triage <source-id> --limit 1
.\scripts\galois.ps1 show <source-id>
.\scripts\galois.ps1 doctor
```

</details>

<details>
<summary><strong>Daily / Weekly reflection (assistant-authored artifacts)</strong></summary>

Galois validates and applies JSON artifacts; it does not call a model itself.
Full operating contracts live in
[Cognitive consolidation](docs/COGNITIVE_CONSOLIDATION.md) and
[Agent integration](docs/AGENT_INTEGRATION.md).

```powershell
# Daily
.\scripts\galois.ps1 recover
.\scripts\galois.ps1 triage --limit 25
.\scripts\galois.ps1 consolidate daily --limit 25
.\scripts\galois.ps1 reflection queue --limit 5 --max-chars 6000
.\scripts\galois.ps1 dream daily --bundle-file <daily-dream.json> --limit 5

# Weekly
.\scripts\galois.ps1 recover
.\scripts\galois.ps1 dream audit-daily --from-date <YYYY-MM-DD> --to-date <YYYY-MM-DD>
.\scripts\galois.ps1 dream weekly --bundle-file <weekly-dream.json>
.\scripts\galois.ps1 consolidate weekly --skip-daily-admission
```

</details>

## Connect an assistant

Galois is meant to be used **through your existing assistant**, not as a
terminal-first wiki.

Default MCP access is **read-only**. Five tools:

`memory_capabilities` · `memory_context` · `memory_search` · `memory_show` · `memory_source`

| Assistant | Status |
|---|---|
| **Claude Desktop** | Windows installer + template; live validated |
| **Cursor** | Compatible via project MCP / host templates; verify live |
| **Codex** | Read-only template; live validated on Windows |
| **Hermes** | Template; host-prefixed tool names expected |
| **OpenClaw / OpenHuman** | Templates; prefer each host’s managed MCP path |
| Other MCP clients | Same stdio contract; prove with a live tool call |

Templates and acceptance checks:
[`adapters/hosts/`](adapters/hosts/).

**Claude Desktop on Windows:**

```powershell
.\scripts\install-galois-claude-desktop.ps1
```

**Let the assistant wire itself up** (paste into a code-capable session with
this repo open):

```text
Read README.md and adapters/hosts/galois.mcp-manifest.json.
Connect this assistant to Galois (read-only). Discover paths on this machine,
back up existing MCP config, merge the matching template, restart if needed,
then prove the link with memory_capabilities and one Chinese memory_context query.
```

You can also browse the Markdown vault in **Obsidian** (`vault/`). Generated
views under `vault/views/` are rebuildable; do not hand-edit `vault/raw/` or
approved Canonical pages.

## How Galois differs from typical AI memory

| Typical AI memory | Galois |
|---|---|
| Remembers chat facts and preferences | Remembers sources, evidence and belief history |
| Retrieves similar text | Returns bounded context with trust labels |
| Overwrites yesterday’s answer | Records support, limit, contradict, supersede |
| One blob of “memory” | Separates research / exploration / strict execution |
| Tied to one chat product | One local memory shared by several assistants |
| Model confidence ≈ authority | Canonical changes require **your** approval |

## Documentation

| Topic | Link |
|---|---|
| Vision | [docs/VISION.md](docs/VISION.md) |
| Architecture | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Cognitive consolidation | [docs/COGNITIVE_CONSOLIDATION.md](docs/COGNITIVE_CONSOLIDATION.md) |
| Agent / MCP integration | [docs/AGENT_INTEGRATION.md](docs/AGENT_INTEGRATION.md) · [docs/MCP_INTEGRATION.md](docs/MCP_INTEGRATION.md) |
| Research directions | [docs/RESEARCH_DIRECTIONS.md](docs/RESEARCH_DIRECTIONS.md) |
| Host adapters | [adapters/hosts/README.md](adapters/hosts/README.md) |
| Security | [SECURITY.md](SECURITY.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Project state | [PROJECT_STATE.md](PROJECT_STATE.md) |

## License

Engine and protocols in this repository are under the **Apache License 2.0**
([LICENSE](LICENSE)).

Private vault content (captured sources and personal knowledge) is **not** part
of the intended public distribution and should not be treated as reusable under
that license when present in an evaluation checkout. See
[docs/RELEASE_BOUNDARY.md](docs/RELEASE_BOUNDARY.md).

The Galois name and logo are not licensed as trademarks and may not be used to
imply endorsement or to brand a fork as the official project.

---

<p align="center">
  <img src="./assets/icon.png" alt="Galois" width="44" /><br /><br />
  <strong>Find the hidden structure.</strong><br />
  Preserve the evidence. Connect the ideas. Ask a better question.
</p>
