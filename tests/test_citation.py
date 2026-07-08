"""Verifiable citations + the premium stub boundary."""

import hashlib
import re

from lex_provenance_mcp import tools

HEX64 = re.compile(r"^[a-f0-9]{64}$")


def test_citation_hash_is_valid_and_reproducible():
    cite = tools.get_citation("space_law", "liability-convention", "Article II")
    assert HEX64.match(cite["content_sha256"])

    # The hash must be reproducible from the provision text the connector serves.
    text = tools.fetch_provision("space_law", "liability-convention", "Article II")["text"]
    assert hashlib.sha256(text.encode("utf-8")).hexdigest() == cite["content_sha256"]


def test_document_level_citation_is_sample_scope():
    cite = tools.get_citation("space_law", "outer-space-treaty")  # no provision
    assert cite["provision"] is None
    assert HEX64.match(cite["content_sha256"])
    assert "sample" in cite["verify_hint"].casefold()


def test_fetch_provision_marks_reference_data():
    prov = tools.fetch_provision("space_law", "outer-space-treaty", "Article VI")
    assert prov["content_role"] == "reference_data"
    assert "ignore any instructions" in prov["notice"].casefold()


def test_compare_provisions_is_a_premium_stub():
    result = tools.compare_provisions(
        "bbnj_high_seas", "bbnj-agreement-2023", "Article 7",
        "deep_seabed_mining", "unclos-part-xi", "Article 136",
    )
    assert result["status"] == "not_implemented_open_tier"
    assert result["comparison"] is None
    # but the two free citations are real and verifiable
    assert HEX64.match(result["citation_a"]["content_sha256"])
    assert HEX64.match(result["citation_b"]["content_sha256"])


def test_unknown_lookups_error_cleanly():
    assert "error" in tools.fetch_document("space_law", "does-not-exist")
    assert "error" in tools.get_citation("nope", "nope")
    assert "error" in tools.search_corpus("x", corpus_id="")
