# LexProvenance - `lex-provenance-mcp`

[![tests](https://github.com/dacheah/lex-provenance-mcp/actions/workflows/tests.yml/badge.svg)](https://github.com/dacheah/lex-provenance-mcp/actions/workflows/tests.yml)

> **Verifiable, provenance-first legal corpora for AI systems.**
> A read-only [Model Context Protocol](https://modelcontextprotocol.io) connector that lets
> AI agents *search, fetch, and cite* neutral, provenance-tracked bodies of law - with a
> tamper-evident content hash on every citation.

**Status: v0.1 - public scaffold.** This is a deliberately thin, credible interface layer, not
a finished product. See the [roadmap](#roadmap) and [what this is not](#what-this-is-not).

---

## Why this exists

A dataset says *"here are some documents."* This connector says *"here is how an AI agent can
search, fetch, and **cite** these documents safely, with each answer traceable to an official
source and verifiable against a content hash."*

The connector is **corpus-agnostic**. It speaks to any provenance-first legal corpus that
exposes a standard manifest - today three public "global-commons" corpora, tomorrow any body of
law or regulation. The connector is the interface; the corpora are the asset.

## What it connects (today)

| Corpus | Domain | Canonical home |
|---|---|---|
| `space_law` | International & national space law | [github](https://github.com/dacheah/space-law-corpus) | [dataset](https://huggingface.co/datasets/dacheah/space-law-corpus) |
| `deep_seabed_mining` | Deep seabed mining law (UNCLOS Part XI, ISA, US regime) | [github](https://github.com/dacheah/deep-seabed-mining-law-corpus) | [dataset](https://huggingface.co/datasets/dacheah/deep-seabed-mining-law-corpus) |
| `bbnj_high_seas` | BBNJ / High Seas Treaty & framework | [github](https://github.com/dacheah/bbnj-high-seas-treaty-corpus) | [dataset](https://huggingface.co/datasets/dacheah/bbnj-high-seas-treaty-corpus) |

This repo ships only **sample manifests** (a few records each) that point to those canonical
sources. It does **not** contain the full corpora.

## Tools (read-only)

| Tool | What it does | Tier |
|---|---|---|
| `list_corpora` | List available corpora + coverage | Free |
| `search_corpus` | Keyword search *within one corpus* | Free |
| `fetch_document` | Return one document's metadata + provenance | Free |
| `fetch_provision` | Return one provision (article/section) | Free |
| `get_citation` | Return a **verifiable citation** (source, date, **SHA-256 hash**, version) | Free |
| `compare_provisions` | Relate/compare provisions **across corpora** | **Stub -> premium** |

Every tool is **read-only**. There are no write, edit, ingest, delete, or shell tools - by
design, and enforced by a test (`tests/test_read_only.py`). See [`docs/security.md`](docs/security.md).

## Verifiable citations (the differentiator)

`get_citation` returns the content **SHA-256 hash** and the **dated version** of the exact text
it cites. An agent's citation therefore points not just at "Article 14" but at *a specific,
reproducible, tamper-checkable state* of Article 14. If the stored text changes by one
character, the hash changes - so a citation can be re-verified later. See
[`docs/citation-model.md`](docs/citation-model.md).

## Quickstart

```bash
pip install -e ".[dev]"          # pure-Python tool logic + tests, no MCP SDK needed
python -m pytest -q              # all green

# To actually serve over MCP (stdio):
pip install -e ".[mcp]"
lex-provenance-mcp               # or:  python -m lex_provenance_mcp.server
```

Try the tool logic directly (no SDK required):

```python
from lex_provenance_mcp import tools
print(tools.list_corpora())
print(tools.search_corpus("liability", corpus_id="space_law"))
print(tools.get_citation("space_law", document_id="outer-space-treaty", provision="Article VI"))
```

## Commercial boundary

This connector is the **free razor**. The enriched, connected, and hosted layers are a separate
paid offering - see [`docs/commercial.md`](docs/commercial.md). In short:

- **Free / open:** the connector, schemas, sample manifests, docs, in-corpus search/fetch/cite.
- **Not in this repo (premium):** full enriched corpora, cross-corpus reasoning, embeddings,
  monitoring / treaty-status intelligence, hosted search, private-corpus onboarding.

## What this is not

- Not the corpora (those live in their own repositories and datasets).
- Not the corpus-construction methodology (that is a separate, private toolkit - this repo
  reveals *what you fetch*, never *how the record is built*).
- Not legal advice. See [`docs/legal-disclaimer.md`](docs/legal-disclaimer.md).

## Roadmap

- **v0.1 (this):** read-only connector scaffold, schemas, sample manifests, in-corpus tools,
  verifiable citations, adapter placeholders. No hosted service, no full corpus, no premium layer.
- **v0.2:** local search over selected public corpora; adapter examples that actually run.
- **v0.3:** richer citation model + corpus manifests consumed directly from canonical repos.
- **Later (premium, not here):** hosted MCP endpoint, cross-corpus intelligence, monitoring,
  institutional access.

## Renaming

The public identity lives in one file - [`mcp_server/identity.py`](mcp_server/identity.py).
Change `BRAND_NAME`, `REPO_SLUG`, `TOOL_NAMESPACE`, `PACKAGE_NAME` there (and rename the folder)
to switch to any alternative name; nothing else hard-codes it.

## Licence

Code and schemas: **Apache-2.0** ([`LICENSE`](LICENSE)). Docs: **CC BY 4.0** unless stated.
Source legal texts are official public documents and are never relicensed. See [`NOTICE`](NOTICE).
