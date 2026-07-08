"""Corpus-agnostic registry discovers corpora from source_pointer.json files."""

from lex_provenance_mcp import registry


def test_discovers_the_three_corpora():
    ids = {p["corpus_id"] for p in registry.list_pointers()}
    assert {"space_law", "deep_seabed_mining", "bbnj_high_seas"} <= ids


def test_pointers_never_bundle_full_corpus():
    for p in registry.list_pointers():
        assert p["full_corpus_included"] is False
        assert p["included_here"] in {"sample_manifest_only", "none"}


def test_get_document_roundtrip():
    doc = registry.get_document("space_law", "outer-space-treaty")
    assert doc and doc["title"].startswith("Treaty on Principles")


def test_unknown_corpus_returns_none():
    assert registry.get_manifest("not-a-corpus") is None
    assert registry.get_document("not-a-corpus", "x") is None
