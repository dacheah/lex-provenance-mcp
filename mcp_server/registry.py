"""Corpus registry — corpus-agnostic loader.

The connector knows nothing hard-coded about any specific corpus. It discovers
corpora by scanning `corpora/*/source_pointer.json` and lazily loads each
corpus's `sample_manifest.json` on demand.

Adding a new corpus (including, later, a PRIVATE commercial corpus in a separate
deployment) is a matter of dropping in a new folder with these two files — no
code change. That is what keeps the connector a reusable "razor" over swappable
"blades".
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

# corpora/ lives next to the repo root (one level up from this package dir).
_CORPORA_DIR = Path(__file__).resolve().parent.parent / "corpora"


def corpora_dir() -> Path:
    return _CORPORA_DIR


@lru_cache(maxsize=1)
def _pointer_paths() -> tuple[Path, ...]:
    if not _CORPORA_DIR.is_dir():
        return ()
    return tuple(sorted(_CORPORA_DIR.glob("*/source_pointer.json")))


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def list_pointers() -> list[dict[str, Any]]:
    """Return the source_pointer.json content for every discovered corpus."""
    return [_load_json(p) for p in _pointer_paths()]


def get_pointer(corpus_id: str) -> dict[str, Any] | None:
    for p in _pointer_paths():
        data = _load_json(p)
        if data.get("corpus_id") == corpus_id:
            return data
    return None


def get_manifest(corpus_id: str) -> dict[str, Any] | None:
    """Load the sample manifest for a corpus, or None if unknown."""
    for p in _pointer_paths():
        if _load_json(p).get("corpus_id") == corpus_id:
            manifest_path = p.parent / "sample_manifest.json"
            if manifest_path.is_file():
                return _load_json(manifest_path)
            return {"corpus_id": corpus_id, "documents": []}
    return None


def get_document(corpus_id: str, document_id: str) -> dict[str, Any] | None:
    manifest = get_manifest(corpus_id)
    if not manifest:
        return None
    for doc in manifest.get("documents", []):
        if doc.get("document_id") == document_id:
            return doc
    return None
