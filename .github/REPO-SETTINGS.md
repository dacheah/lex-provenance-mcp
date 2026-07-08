# Repo settings (reference)

Values for `dacheah/lex-provenance-mcp`, with **PowerShell** commands (Windows).
Set via the UI (the "About" gear on the repo home) or with the `gh` CLI below.

## Description (About)

> Verifiable, provenance-first legal corpora for AI systems - a read-only MCP connector (search, fetch, and hash-verifiable citations).

*(Plain hyphen, not an em dash - avoids PowerShell console encoding surprises.)*

## Website (About)

https://danielcheah.com

## Topics

mcp, model-context-protocol, legal, legal-informatics, provenance, law, corpus,
citation, rag, retrieval-augmented-generation, ai, llm, international-law,
space-law, law-of-the-sea, open-data, python, legal-tech, machine-readable-law, treaties

## Labels

A `commercial` label (colour 0E8A16) exists; the issue form applies it automatically.

---

## Set description + topics (PowerShell)

**One line (paste whole):**

```powershell
gh repo edit dacheah/lex-provenance-mcp --description "Verifiable, provenance-first legal corpora for AI systems - a read-only MCP connector (search, fetch, and hash-verifiable citations)." --homepage "https://danielcheah.com" --add-topic mcp --add-topic model-context-protocol --add-topic legal --add-topic legal-informatics --add-topic provenance --add-topic law --add-topic corpus --add-topic citation --add-topic rag --add-topic retrieval-augmented-generation --add-topic ai --add-topic llm --add-topic international-law --add-topic space-law --add-topic law-of-the-sea --add-topic open-data --add-topic python --add-topic legal-tech --add-topic machine-readable-law --add-topic treaties
```

**Multi-line (PowerShell backtick continuation - backtick, not backslash):**

```powershell
gh repo edit dacheah/lex-provenance-mcp `
  --description "Verifiable, provenance-first legal corpora for AI systems - a read-only MCP connector (search, fetch, and hash-verifiable citations)." `
  --homepage "https://danielcheah.com" `
  --add-topic mcp --add-topic model-context-protocol --add-topic legal `
  --add-topic legal-informatics --add-topic provenance --add-topic law `
  --add-topic corpus --add-topic citation --add-topic rag `
  --add-topic retrieval-augmented-generation --add-topic ai --add-topic llm `
  --add-topic international-law --add-topic space-law --add-topic law-of-the-sea `
  --add-topic open-data --add-topic python --add-topic legal-tech `
  --add-topic machine-readable-law --add-topic treaties
```

## Create the `commercial` label (PowerShell)

```powershell
gh label create commercial --color 0E8A16 --description "Commercial enquiry or lead" --force
```

## Publish the repo the first time (reference)

```powershell
gh repo create dacheah/lex-provenance-mcp --public --source . --remote origin --push
```
