# Changelog

All notable changes to this project are documented here. Dates are ISO-8601.

## [0.1.0] — 2026-07-08

Initial public scaffold — a deliberately thin, credible v0.1.

### Added
- Corpus-agnostic, read-only MCP connector (`mcp_server/`) with six tools:
  `list_corpora`, `search_corpus`, `fetch_document`, `fetch_provision`,
  `get_citation`, and `compare_provisions` (premium stub).
- Verifiable citations: `get_citation` returns a live SHA-256 content hash and a
  dated version, reproducible from the served text.
- Interface-only JSON Schemas (`corpus`, `document`, `citation`) — the shape of
  what a caller receives, not how the record is constructed.
- Sample manifests + source pointers for `space_law`, `deep_seabed_mining`,
  `bbnj_high_seas` (samples only; full corpora live at their canonical homes).
- Docs: architecture, corpus boundaries, citation model, commercial model,
  legal disclaimer, security.
- Adapter placeholders (Claude, OpenAI, Cursor) and example queries.
- Test suite enforcing read-only posture, schema conformance, verifiable
  citations, and the premium boundary.

### Deliberately excluded
- Full corpora, corpus-construction methodology, embeddings, cross-corpus
  intelligence, monitoring, hosted service, credentials.
