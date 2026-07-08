"""LexProvenance — read-only MCP connector for provenance-first legal corpora."""

from . import identity, registry, tools

__all__ = ["identity", "registry", "tools"]
__version__ = identity.VERSION
