# Adapter: OpenAI

*Placeholder — install notes, not production integration.*

The connector is MCP-standard and model-agnostic. For OpenAI-based agents, expose the same read-only
tools (`lexprov.*`) through your MCP bridge of choice, or wrap the pure-Python functions in
`mcp_server/tools.py` as function-calling tools.

```python
from lex_provenance_mcp import tools
result = tools.get_citation("space_law", "outer-space-treaty", "Article VI")
```

Keep the read-only posture and the reference-data notice intact when surfacing results to the model.

*A fuller, tested adapter example lands in v0.2.*
