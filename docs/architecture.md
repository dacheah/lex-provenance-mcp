# Architecture

LexProvenance is an **interface layer**, not a data store. It sits *above* the canonical corpus
repositories and exposes a small, read-only, corpus-agnostic tool surface for AI agents.

```
                  +---------------------------------------------+
   AI agents  ->  |   lex-provenance-mcp  (this repo)           |
 (Claude,         |   read-only tools + schemas + sample data   |
  OpenAI,         +----------------------+----------------------+
  Cursor)                                | source_pointer.json per corpus
                                         v
        +--------------------+---------------------+--------------------+
        | space-law-corpus   | deep-seabed-corpus  | bbnj-corpus        |  <- canonical repos
        | (github + HF)      | (github + HF)       | (github + HF)      |     (source of truth)
        +--------------------+---------------------+--------------------+
```

## Layers (kept separate on purpose)

| Layer | Where | Role |
|---|---|---|
| Canonical corpora | their own repos + datasets | source of truth; full instruments, verified hashes |
| **Connector (this)** | `lex-provenance-mcp` | AI access layer - search / fetch / cite |
| Enriched / hosted | private, commercial | cross-corpus intelligence, monitoring, hosted API |
| Adapters | `adapters/` | thin per-ecosystem install notes |

## Corpus-agnostic by construction

The connector hard-codes nothing about any corpus. `registry.py` discovers corpora by scanning
`corpora/*/source_pointer.json`. To add a corpus - including a private commercial one in a separate
deployment - you drop in a folder with a `source_pointer.json` and a manifest. No code change.

This is what makes the connector a reusable *razor* over swappable *blades*: the same interface can
front the open commons corpora today and enriched or private corpora later.

## What this repo deliberately excludes

- The full corpora (pointers only).
- Any corpus-construction, ingestion, verification, or provenance-building methodology. This repo
  describes **what you fetch**, never **how the record is built**. That construction discipline is a
  separate, private toolkit.
- Embeddings, cross-reference graphs, monitoring, scoring, hosted indexes, credentials.

## Read-only posture

There are no write, edit, ingest, delete, or shell tools - see [`security.md`](security.md). The
tool registry (`tools.TOOL_SPECS`) is asserted read-only by the test suite.
