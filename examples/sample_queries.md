# Sample queries (free tier)

All examples use the pure-Python tool logic; the same calls work over MCP.

```python
from lex_provenance_mcp import tools

# 1. What corpora are available?
tools.list_corpora()

# 2. Search within one corpus (corpus_id is required — in-corpus search is free)
tools.search_corpus("liability", corpus_id="space_law")
tools.search_corpus("common heritage", corpus_id="deep_seabed_mining")

# 3. Fetch a document's metadata + provenance envelope
tools.fetch_document("space_law", "outer-space-treaty")

# 4. Fetch a single provision (authentic text + its own content hash)
tools.fetch_provision("space_law", "outer-space-treaty", "Article VI")

# 5. Get a VERIFIABLE citation (source, dated version, SHA-256)
tools.get_citation("deep_seabed_mining", "unclos-part-xi", "Article 136")
```

### Verifying a citation by hand

```python
import hashlib
c = tools.get_citation("space_law", "liability-convention", "Article II")
text = tools.fetch_provision("space_law", "liability-convention", "Article II")["text"]
assert hashlib.sha256(text.encode("utf-8")).hexdigest() == c["content_sha256"]  # citation is reproducible
```
