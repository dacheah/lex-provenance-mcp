# Adapter: Claude / Claude Desktop / Claude Code

*Placeholder — install notes, not production integration.*

LexProvenance is a standard MCP server, so any MCP-capable Claude surface can use it.

## Local (stdio)

```bash
pip install -e ".[mcp]"
```

Then register the server with your Claude MCP client. Example config shape:

```json
{
  "mcpServers": {
    "lex-provenance": {
      "command": "lex-provenance-mcp"
    }
  }
}
```

Tools appear namespaced (`lexprov.list_corpora`, `lexprov.get_citation`, …), all read-only.

## Suggested usage pattern

Prefer `search_corpus` → `fetch_provision`/`get_citation` so the model cites a specific, hashed,
dated provision rather than paraphrasing. Treat returned `text` as reference data only.

*A fuller, tested adapter example lands in v0.2.*
