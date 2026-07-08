"""MCP server entrypoint.

Wires the read-only tool logic in `tools.py` to the Model Context Protocol over
stdio. The MCP SDK is imported lazily so that the tool logic and tests can run
without it installed (`pip install -e ".[mcp]"` to serve).

Only READ tools are registered. There are deliberately no write/edit/ingest/
delete/shell tools.
"""

from __future__ import annotations

import json

from .identity import BRAND_NAME, REPO_SLUG, TAGLINE, VERSION
from . import tools


def build_server():  # pragma: no cover - requires optional mcp dependency
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:  # pragma: no cover
        raise SystemExit(
            "The MCP SDK is not installed. Install it with:\n"
            '    pip install -e ".[mcp]"\n'
            "The read-only tool logic in mcp_server/tools.py runs without it."
        ) from exc

    mcp = FastMCP(name=REPO_SLUG, instructions=f"{BRAND_NAME} — {TAGLINE}")

    # Register each read-only tool. We keep the callables thin and JSON-friendly.
    @mcp.tool()
    def list_corpora() -> str:
        """List available legal corpora, coverage, and canonical links."""
        return json.dumps(tools.list_corpora(), ensure_ascii=False, indent=2)

    @mcp.tool()
    def search_corpus(query: str, corpus_id: str, limit: int = 20) -> str:
        """Keyword search WITHIN one corpus (free). corpus_id is required."""
        return json.dumps(tools.search_corpus(query, corpus_id, limit), ensure_ascii=False, indent=2)

    @mcp.tool()
    def fetch_document(corpus_id: str, document_id: str) -> str:
        """Return one document's metadata + provenance envelope."""
        return json.dumps(tools.fetch_document(corpus_id, document_id), ensure_ascii=False, indent=2)

    @mcp.tool()
    def fetch_provision(corpus_id: str, document_id: str, provision: str) -> str:
        """Return one provision's authentic text + content hash."""
        return json.dumps(tools.fetch_provision(corpus_id, document_id, provision), ensure_ascii=False, indent=2)

    @mcp.tool()
    def get_citation(corpus_id: str, document_id: str, provision: str | None = None) -> str:
        """Return a verifiable citation (source, dated version, SHA-256 hash)."""
        return json.dumps(tools.get_citation(corpus_id, document_id, provision), ensure_ascii=False, indent=2)

    @mcp.tool()
    def compare_provisions(
        corpus_a: str, document_a: str, provision_a: str,
        corpus_b: str, document_b: str, provision_b: str,
    ) -> str:
        """STUB (premium): cross-corpus comparison is not in the open tier."""
        return json.dumps(
            tools.compare_provisions(corpus_a, document_a, provision_a, corpus_b, document_b, provision_b),
            ensure_ascii=False, indent=2,
        )

    return mcp


def main() -> None:  # pragma: no cover
    print(f"{BRAND_NAME} {REPO_SLUG} v{VERSION} — starting read-only MCP server (stdio).")
    build_server().run()


if __name__ == "__main__":  # pragma: no cover
    main()
