# Corpus module: `space_law`

This folder is a **pointer**, not the corpus. It contains:

- `source_pointer.json` — where the canonical corpus and dataset live, and what is (and isn't) included here.
- `sample_manifest.json` — a small sample of provisions, for demonstration and tests.

**The full corpus is not here.** Get it from the canonical sources:

- Repository: https://github.com/dacheah/space-law-corpus
- Dataset: https://huggingface.co/datasets/dacheah/space-law-corpus
- Browsable site: https://dacheah.github.io/space-law-corpus/

Each content hash the connector returns for this sample is computed live from the excerpt shipped
in `sample_manifest.json`, so it is fully reproducible. The full corpus carries verified hashes for
every instrument at its canonical home.
