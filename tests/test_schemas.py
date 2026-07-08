"""Schemas are valid, and tool OUTPUT conforms to the read-interface schemas."""

import json
from pathlib import Path

import jsonschema
import pytest

from lex_provenance_mcp import tools

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "mcp_server" / "schemas"


def _load(name):
    with (SCHEMA_DIR / name).open(encoding="utf-8") as fh:
        return json.load(fh)


@pytest.mark.parametrize("name", ["corpus.schema.json", "document.schema.json", "citation.schema.json"])
def test_schema_is_valid(name):
    schema = _load(name)
    jsonschema.Draft202012Validator.check_schema(schema)


def test_list_corpora_entries_conform_to_corpus_schema():
    schema = _load("corpus.schema.json")
    payload = tools.list_corpora()
    assert payload["corpora"], "expected at least one corpus"
    for corpus in payload["corpora"]:
        jsonschema.validate(corpus, schema)
        assert corpus["full_corpus_included"] is False


def test_fetch_document_conforms_to_document_schema():
    schema = _load("document.schema.json")
    doc = tools.fetch_document("space_law", "outer-space-treaty")
    jsonschema.validate(doc, schema)


def test_get_citation_conforms_to_citation_schema():
    schema = _load("citation.schema.json")
    cite = tools.get_citation("deep_seabed_mining", "unclos-part-xi", "Article 136")
    jsonschema.validate(cite, schema)
