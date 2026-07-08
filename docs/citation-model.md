# Citation model (output shape)

This describes the **shape of a citation a caller receives** — not how the underlying provenance is
produced. The construction discipline (how authoritative text is captured, verified, hashed, and
versioned) is a separate, private concern and is out of scope for this repo.

## Why citations carry a hash

A normal legal citation points at "Article VI". A LexProvenance citation points at *a specific,
dated, tamper-checkable state* of Article VI. Because the citation carries the **SHA-256 hash** of
the exact text and a **dated version**, a downstream system can later re-hash the official text and
confirm the citation still refers to identical content. Citations become reproducible and auditable —
which is exactly what retrieval-augmented and training pipelines need to lower hallucination and
source-drift risk.

## Fields (see `mcp_server/schemas/citation.schema.json`)

| Field | Meaning |
|---|---|
| `corpus_id`, `document_id`, `provision` | what is being cited |
| `citation_text` | human-readable official citation |
| `source_url`, `official_source` | where the authentic text lives |
| `content_sha256` | SHA-256 of the exact cited text (UTF-8) |
| `version` | dated version the citation is pinned to |
| `retrieved` | retrieval date |
| `authoritative_status` | `authoritative` / `derived` / `authoritative_missing` |
| `verify_hint` | how to independently re-verify the hash |
| `disclaimer` | research/reference only; not legal advice |

## How the hash is computed here

In this open connector the hash is computed **live** from the excerpt shipped in the corpus sample
(`sha256(text.encode("utf-8"))`). That makes every hash in the demo reproducible from data in the
repo. In the full corpora, each instrument carries a verified hash recorded at its canonical home.

Provision-level citations hash the provision text. Document-level citations (no `provision`) return a
**sample-scope** hash over the shipped sample provisions and say so — they do not claim to hash the
whole instrument.

## What this model does *not* expose

- How authoritative text is sourced, extracted, OCR-corrected, or fidelity-checked.
- The two-layer authoritative/derived construction mechanics.
- Concept-tagging or cross-reference construction.

Those belong to the private corpus-construction toolkit, not to this read interface.
