# Security policy

## Scope and posture

LexProvenance (`lex-provenance-mcp`) is a **read-only** MCP connector. It exposes no write,
edit, ingest, delete, or shell tools, serves local sample data only, and returns retrieved
legal text as clearly-labelled reference data (never as executable instructions). See
[`docs/security.md`](docs/security.md) for the full posture.

## Reporting a vulnerability

Please report suspected security issues **privately** - do not open a public issue for anything
exploitable.

- Preferred: use GitHub's private vulnerability reporting (the repository's **Security** tab ->
  "Report a vulnerability"), or
- Contact the maintainer via the contact on **https://danielcheah.com**.

Include what you found, how to reproduce it, and any impact you foresee. You'll get an
acknowledgement as soon as practicable. Please give a reasonable window to remediate before any
public disclosure.

## Out of scope

- The correctness or currency of legal source texts (verify against the cited official source).
- The full corpora, enrichment, or hosted layers (not part of this repository).
