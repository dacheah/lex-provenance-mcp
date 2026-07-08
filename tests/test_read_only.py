"""Guardrail: the connector is read-only. This test FAILS the build if a
write-like tool is ever added."""

from lex_provenance_mcp import tools

FORBIDDEN_VERBS = {
    "create", "update", "delete", "remove", "write", "ingest", "insert",
    "put", "post", "patch", "exec", "execute", "run", "shell", "modify",
    "edit", "upload", "commit", "push", "set", "add",
}


def test_every_tool_is_read_access():
    assert tools.TOOL_SPECS, "no tools registered"
    for spec in tools.TOOL_SPECS:
        assert spec["access"] == "read", f"{spec['name']} is not read-only"


def test_no_write_like_tool_names():
    for spec in tools.TOOL_SPECS:
        leaf = spec["name"].split(".")[-1].casefold()
        parts = set(leaf.split("_"))
        offending = parts & FORBIDDEN_VERBS
        assert not offending, f"{spec['name']} contains write-like verb(s): {offending}"


def test_tiers_are_known():
    for spec in tools.TOOL_SPECS:
        assert spec["tier"] in {"free", "premium_stub"}
