# Cross-corpus queries (premium frontier — STUB in the open tier)

Relating and comparing provisions *across* corpora — for example, how the BBNJ Agreement's use of
"common heritage" relates to UNCLOS Part XI, or how the ISA regime and the US DSHMRA track diverge —
is the connective intelligence that the **premium layer** provides. It is intentionally **not**
implemented in this open connector.

The open `compare_provisions` tool is a deliberate stub. It returns the response *shape* and the two
(free) verifiable citations, but performs no cross-corpus reasoning:

```python
from lex_provenance_mcp import tools

result = tools.compare_provisions(
    "bbnj_high_seas", "bbnj-agreement-2023", "Article 7",
    "deep_seabed_mining", "unclos-part-xi", "Article 136",
)

result["status"]      # -> "not_implemented_open_tier"
result["comparison"]  # -> None
result["citation_a"]  # -> a real, verifiable citation (free)
result["citation_b"]  # -> a real, verifiable citation (free)
result["premium"]     # -> pointer to docs/commercial.md
```

Why a stub and not the real thing? Because cross-corpus comparison, cross-reference graphs, and
treaty-status intelligence are exactly the value the enriched layer sells. The open connector gives
you addressable, citable corpora; it does not relate them for you. See
[`../docs/commercial.md`](../docs/commercial.md).
