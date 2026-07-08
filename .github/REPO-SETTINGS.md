# Repo settings (reference)

Values to set on GitHub for `dacheah/lex-provenance-mcp`. Set via the UI (Settings / the
"About" gear on the repo home) or with the `gh` CLI (see below).

## Description (About)

> Verifiable, provenance-first legal corpora for AI systems — a read-only MCP connector (search, fetch, and hash-verifiable citations).

## Website (About)

https://danielcheah.com

## Topics

mcp, model-context-protocol, legal, legal-informatics, provenance, law, corpus,
citation, rag, retrieval-augmented-generation, ai, llm, international-law,
space-law, law-of-the-sea, open-data, python, legal-tech, machine-readable-law, treaties

## Labels

Ensure a `commercial` label exists (the issue form applies it automatically):
teal/green, description "Commercial enquiry or lead".

## Set it all with the gh CLI

```bash
gh repo edit dacheah/lex-provenance-mcp \
  --description "Verifiable, provenance-first legal corpora for AI systems — a read-only MCP connector (search, fetch, and hash-verifiable citations)." \
  --homepage "https://danielcheah.com" \
  --add-topic mcp --add-topic model-context-protocol --add-topic legal \
  --add-topic legal-informatics --add-topic provenance --add-topic law \
  --add-topic corpus --add-topic citation --add-topic rag \
  --add-topic retrieval-augmented-generation --add-topic ai --add-topic llm \
  --add-topic international-law --add-topic space-law --add-topic law-of-the-sea \
  --add-topic open-data --add-topic python --add-topic legal-tech \
  --add-topic machine-readable-law --add-topic treaties

gh label create commercial --color 0E8A16 --description "Commercial enquiry or lead" --force
```
