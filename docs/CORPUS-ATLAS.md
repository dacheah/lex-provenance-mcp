# Corpus atlas

One programme, many corpora. Each corpus is a **separate repository** that owns its own source texts,
licence, build history and maintenance decisions; `lex-provenance-mcp` is one **interface** over
whichever of them publish the standard pointer. This atlas is the roster: which corpora exist, which
ones the connector currently fronts, what shape each is in, and what it takes to add another.

It exists because the alternative is five half-remembered repositories and no way to tell, at a
glance, whether "the legal corpora" means three corpora or six, or which of them is still maintained.

Facts below were read from each repository's `main` branch and from this repo on **2026-09-15**
(the maintenance sections were revised that day after the monitor v3.10 change and the triage it
prompted; the rest of the atlas was read on **2026-09-14**; the toolchain-attestation section was read
on **2026-09-16**).
Counts are the corpora's own declared figures rather than re-derived here, and the source is named
for each one.

## The three layers

| Layer | Where | Role |
|---|---|---|
| Canonical corpora | their own repos + datasets | Source of truth: full texts, verified hashes, dated versions |
| **Connector (this repo)** | `lex-provenance-mcp` | AI access layer: search / fetch / cite, read-only |
| Enriched / hosted | private, commercial | Cross-corpus intelligence, monitoring, hosted API (see [`commercial.md`](commercial.md)) |

A corpus does **not** live in this repo and is never moved into it. The only thing that makes a
corpus part of *this* is a `corpora/<corpus_id>/` folder carrying a `source_pointer.json` and a
`sample_manifest.json` - see [the membership test](#the-membership-test).

## The roster

| Corpus | Body of law | Canonical repo | Machine dataset | Connector |
|---|---|---|---|---|
| `space_law` | International and national space law | [space-law-corpus](https://github.com/dacheah/space-law-corpus) | [Hugging Face](https://huggingface.co/datasets/dacheah/space-law-corpus) | **Yes** - sample only |
| `deep_seabed_mining` | Deep seabed mining (UNCLOS Part XI, ISA, US track) | [deep-seabed-mining-law-corpus](https://github.com/dacheah/deep-seabed-mining-law-corpus) | [Hugging Face](https://huggingface.co/datasets/dacheah/deep-seabed-mining-law-corpus) | **Yes** - sample only |
| `bbnj_high_seas` | 2023 BBNJ Agreement (High Seas Treaty) and UNCLOS framework | [bbnj-high-seas-treaty-corpus](https://github.com/dacheah/bbnj-high-seas-treaty-corpus) | [Hugging Face](https://huggingface.co/datasets/dacheah/bbnj-high-seas-treaty-corpus) | **Yes** - sample only |
| *unregistered* | Digital-asset market-structure and prudential law | [digital-asset-law-corpus](https://github.com/dacheah/digital-asset-law-corpus) | none published | No |
| *unregistered* | AML/CTF and financial sanctions | [aml-sanctions-law-corpus](https://github.com/dacheah/aml-sanctions-law-corpus) | [Hugging Face](https://huggingface.co/datasets/dacheah/aml-sanctions-law-corpus) | No |

Two further corpora exist privately, plus a parked expansion; they are deliberately out of scope for
a public document. Nothing in this atlas assumes this list is complete - the roster is what is
**publicly citable today**.

## Corpora the connector fronts

Three corpora share a thesis - the global commons / areas beyond national jurisdiction - and each is
addressable on its own. They are **not** merged, and relating them is a premium capability, not an
open one (see [`corpus-boundaries.md`](corpus-boundaries.md)).

### `space_law`

- **Scope.** UN space treaties, UN GA principle instruments, COPUOS soft-law guidelines, and a
  deliberate three-instrument national pilot (US, Luxembourg, France).
- **Size.** 12 UN-level instruments plus a 3-instrument national pilot (pointer declares
  `instrument_count_full: 15`); 23 authoritative records, because language siblings are separate
  records. The Outer Space Treaty is held in all five authentic languages.
- **Languages.** `en`, with five authentic languages for the OST.
- **Licence.** Compilation CC BY 4.0 (`LICENSE`); source texts keep their own terms.
- **Maintenance.** Live. Last sweep 2026-09-14 by monitor **v3.10**, 9 sources, 0 changed. v3.10
  unescapes HTML entities before hashing — a page that renders identically but encodes a space as
  `&nbsp;` no longer moves the hash — and refuses to sweep on an unrecognised argument (a typo used to
  run a full live sweep and silently advance every baseline). Baselines were re-derived in the same
  change, so the first v3.10 sweep reported no spurious churn.
- **Ships here.** 3 sample documents: `outer-space-treaty`, `liability-convention`,
  `luxembourg-space-resources-2017`.

### `deep_seabed_mining`

- **Scope.** UNCLOS Part XI, the 1994 Implementation Agreement, ISA exploration regulations and the
  draft Exploitation Regulations ("Mining Code"), the 2011 ITLOS Advisory Opinion, sponsoring-state
  laws, and the US non-UNCLOS track, which is marked as a distinct alternative.
- **Size.** Ten instruments - nine in force plus the live Mining Code draft; 37 records. The
  record-level layer added two on 2026-09-14: ITLOS Orders 2026/8 and 2026/9 of 4 August 2026 in
  the NORI and TOML inquiries against the Authority. **Issue #9 added seven on 2026-09-16**, closing
  the incidental-proceeding set for both cases: the Order of the Chamber of 18 July 2026 in each case
  (the order Orders 2026/8 and 2026/9 both cite), the two procedural Orders 2026/3 and 2026/4 of
  10 June 2026, and the three judges' declarations published with the 18 July order. The declarations
  opened a record class the corpus did not have, `itlos/declaration/*`. Five of the seven are
  born-digital and are extracted from the publisher's own text layer; the other two are scans
  recovered by two-engine OCR.
- **The 18 July 2026 order has no order number.** ITLOS publishes it as `C34_Order_18.07.2026_orig.pdf`
  and its 59 pages contain no "Order 2026/" string anywhere; the running header reads only
  "List of Cases: No. 34". It is therefore identified by date (`case34-order-18jul2026`) rather than
  by a number this corpus invented. This also closed the question left open in
  `ready__itlos-order-case34-order8-2026.json`: the guessed `C34_Order_18.07.2026-7.pdf` is a 404, and
  the instrument both ingested August orders cite by date is this one.
- **Licence.** Compilation CC BY 4.0; source texts keep their own terms.
- **Maintenance.** Live. Last sweep 2026-09-15 by monitor **v3.10**, 22 sources, 0 changed. **Two
  sources were added on 2026-09-14**: the per-case **incidental-proceeding sub-pages** for Cases 34 and
  35, which is where the provisional-measures documents actually live — the main case pages list only
  the numbered orders (3 and 2 documents) while those sub-pages carry 15 and 14. That gap concealed the
  **Order of 18 July 2026**, the order both ingested 2026/8 and 2026/9 cite; ingesting it and the
  accompanying declarations was open as **issue #9**, and is done as of 2026-09-16 - all seven
  documents are ingested, validated and on the board as 37 records.
- **Maintenance (diagnosis, corrected 2026-09-14).** "Most flagged" was never "most changed": triage of
  the 2026-08-01 and 2026-09-01 sweeps found 19 flags and **no legal change**. Of the three causes
  originally reported, **two turned out not to exist** — the anti-bot widget and the newsletter footer
  are *not on the extracted text surface at all*, because they sit in markup `to_text()` strips. What
  was real: the v3.10 entity change, plus footer/nav chrome (now excluded with two narrow
  `ignore_patterns`). The date-like strings on these pages are **substantive** — the session schedule,
  document citations, and the draft regulations' development chronology — and are deliberately **not**
  suppressed. The only genuine development in the period was caught by the **record-level** layer, not
  the page layer: ITLOS Orders 2026/8 and 2026/9 of 4 August 2026. Treat this corpus's page-mode flag
  count as a churn indicator, not a change indicator.
- **Ships here.** 2 sample documents: `unclos-part-xi`, `itlos-advisory-opinion-2011`.

### `bbnj_high_seas`

- **Scope.** The 2023 BBNJ Agreement, its founding UN resolutions, the UNCLOS framework, and
  Preparatory Commission / COP outputs.
- **Size.** Pointer declares `instrument_count_full: 15`. The agreement itself is held in **all six
  authentic UN languages** as sibling records.
- **Languages.** `ar`, `zh`, `en`, `fr`, `ru`, `es` - the widest of any corpus here.
- **Licence.** Our contributions - the derived layer, schema, scripts, docs and generated site - are
  CC BY 4.0 (`LICENSE-derived-CC-BY-4.0.txt`); source texts are not relicensed.
- **Maintenance.** Live. Last sweep 2026-09-15 by monitor **v3.10**, 7 sources, **1 flagged** — the UN
  Treaty Collection **status document** for XXI.10. That source is byte-hashed (it is a PDF, not a
  page), so the flag is a real republication of the published document rather than the v3.10 entity
  change: it currently reads *Signatories 145 · Parties 94 · entry into force 17 January 2026 ·
  registration No. 59087*. Triaged and closed (bbnj #1/#2) with **no ingest** and no metadata change —
  the `entry_into_force_date` on all six language variants already records `2026-01-17`.
- **Ships here.** 2 sample documents: `bbnj-agreement-2023`, `unclos-1982`.

## Corpora not yet connector-addressable

Both are built to the same two-layer convention as the three above, and both are one pointer file
away from being addressable. Neither has one.

### Digital-asset market-structure law

- **Scale.** 57 authoritative instruments across 21 jurisdictions, in their authentic enacting
  languages (14 language codes; parallel authentic texts - Swiss de/fr/it, Hong Kong en/zh-Hant - are
  separate records under one instrument).
- **Distinctive feature.** 13 further records are **withheld** from the public release because their
  reuse terms are not yet confirmed clean. This is the only corpus here that publishes a
  reuse-terms gate.
- **Maintenance.** No source monitor and no `monitoring/` directory at all; last repository activity
  2026-08-05, last content change 2026-07-11. Treat as **stale** rather than live.
- **Dataset.** None published to Hugging Face - the only corpus in the roster without one.
- **Why it matters for the connector.** It is the roster's largest and most commercially legible
  corpus, and the only one with a flat export (`data/documents.jsonl` + `data/provisions.jsonl`)
  already built.

### AML/CTF and financial sanctions

- **Scope.** Australian AML/CTF and financial-sanctions law over nine further jurisdiction branches
  (UK, US, EU, Canada, Singapore, Switzerland, Hong Kong, Japan, UAE) - ten in total - with the FATF
  Recommendations as backbone and the UN treaty / Security Council layer beneath.
- **Scale.** 60 monitored sources across the ten jurisdiction branches, each recorded from its own
  official source and never merged.
- **Distinctive feature.** Carries a FATF cross-jurisdiction crosswalk mapping each FATF
  Recommendation to its UN basis - the strongest cross-reference layer in the roster.
- **Status.** **FROZEN as at 2026-08-04.** Source monitoring was deliberately switched off; the final
  sweep ran 2026-08-03 (60 sources, 10 changed, 18 flagged for manual review). The corpus is frozen,
  not withdrawn: every record is still byte-exact, hash-verifiable and honestly dated. It carries a
  Zenodo DOI and its own frozen-notice document.
- **Why the frozen flag is the point.** This corpus is the roster's proof that honest dating works. A
  superseded AML compilation looks identical to a current one, so registering it as though it were
  live would be exactly the failure the provenance model exists to prevent. If it is ever registered,
  its frozen status must be a field a caller can see, not a README note.

## The membership test

A corpus is **connector-addressable** when this repo contains both files:

```
corpora/<corpus_id>/source_pointer.json    # metadata: what it is and where the real corpus lives
corpora/<corpus_id>/sample_manifest.json   # a few provisions, for demonstration
```

No code change is required. `registry.py` discovers corpora by globbing `corpora/*/source_pointer.json`,
so the folder is the registration.

### Pointer contract

Required by [`corpus.schema.json`](../mcp_server/schemas/corpus.schema.json): `corpus_id` (must match
`^[a-z0-9_]+$`), `title`, `canonical_repo`, `included_here` (`sample_manifest_only` or `none`), and
`full_corpus_included` (must be `false`).

Used in practice by all three registered corpora - the de-facto full shape, identical across all
three pointers: `corpus_id`, `title`, `domain`, `coverage_note`, `canonical_repo`, `canonical_dataset`,
`site`, `instrument_count_full`, `instrument_count_sample`, `languages`, `included_here`,
`full_corpus_included`, `license_note`.

### Two constraints worth knowing before editing a pointer

1. **`corpus.schema.json` sets `additionalProperties: false`.** Adding a field that the schema does
   not define - a maintenance status, say - fails `tests/test_schemas.py`, because `list_corpora`
   returns the pointer wholesale and every returned corpus is validated against the schema. Changing
   the pointer shape is a schema change, in two files, in a deliberate order.
2. **The full corpus is never bundled.** `full_corpus_included` is `const: false` in the schema and
   asserted by `tests/test_registry.py`. A pointer may only ever point.

### Verifying the roster

```bash
pytest tests/test_registry.py tests/test_schemas.py
```

`test_registry.py` asserts discovery, the no-bundling guarantee, and a document round-trip;
`test_schemas.py` validates the live `list_corpora` output against the read-interface schema. Together
they are the roster's regression test - if a corpus stops being addressable, these fail.

## Schema lineage: one intended spine, four variants

All five corpora publish `schema/authoritative-metadata.schema.json` with the same title
("Authoritative document metadata") and JSON Schema draft 2020-12. They are **not the same file**.
Hashes below are SHA-256 of the file at `main`, truncated to 16 hex characters.

| Variant | Corpora | Schema hash | Properties | `$id` |
|---|---|---|---|---|
| **Core** | `deep_seabed_mining`, `bbnj_high_seas` | `d4ff229dcb77620e` | 40 | `https://provenance-corpus/...` |
| **Extended** | `space_law` | `9c92c9b7689bfddf` | 44 | `https://space-law-corpus/...` |
| **Narrow** | digital-asset | `143178e93a45dc6d` | 37 | `https://provenance-corpus/...` |
| **AML** | aml-sanctions | `fcfe5f61821a7d39` | 40 | `https://provenance-corpus/...` |

The core variant is the shared spine; both registered corpora that were built together use it
byte-for-byte, which is why they agree on 40 properties and an identical required list.

The drift, and what it costs:

- **`space_law` is namespaced differently.** Its `$id` is `https://space-law-corpus/...` while every
  other corpus claims `https://provenance-corpus/...`. Four distinct files, two `$id` values: one
  corpus claims its own namespace, and the other four all claim the same one.
- **`digital-asset` has no binding-force fields at all.** `binding_force`, `issuing_authority` and
  `administering_authority` are absent from its properties *and* its required list. Every other
  corpus requires them. A record from the digital-asset corpus cannot be compared to a record from
  any other corpus on binding force, because the field does not exist on one side.
- **`space_law` carries build-session fields the others do not**: `session`, `adoption_mode`,
  `agenda_item`, `corroborating_sources`, and the `akn_*` identifier family.
- **`aml-sanctions` carries rights fields the others do not**: `legal_status`, `redistribution`,
  `text_derivation`, `authentic_source`. These reflect the FATF/sanctions domain, where
  redistribution terms genuinely vary per source.

**Practical consequence.** "The corpora share a schema" is true of the intent and false of the
artefacts. Anything that reads across corpora - a cross-reference graph, a `compare_provisions`
implementation, a conformance check - must tolerate four record shapes rather than assume one. Where
a cross-corpus claim depends on a specific field, check the field exists in all variants involved
before asserting it.

This is the concrete sense in which the corpora are separate projects with a shared methodology: the
methodology converged, the schema files did not.

## Layout drift

Same two-layer convention - `authoritative/<id>/<version>/{metadata.yaml,text.txt,original.*}` plus
a `derived/` layer, with the wall between them never crossed - but the supporting directories differ
per corpus and per generation.

| Directory | space | seabed | bbnj | digital-asset | aml |
|---|---|---|---|---|---|
| `authoritative/` + `derived/` | yes | yes | yes | yes | yes |
| `schema/` (2 or 3 files) | 3 | 3 | 3 | 2 | 2 |
| `LICENSE` | yes | yes | yes (derived + toolkit) | yes | yes |
| `NOTICE` | - | - | - | yes | yes |
| `CITATION.cff` | yes | yes | yes | yes | yes |
| `docs/` | 14 | 13 | 11 | - | 6 |
| `monitoring/` | 3 | 12 | 3 | - | 13 |
| `queue/` | 1 | 3 | 1 | - | - |
| `capture/` | - | 69 | 234 | - | - |
| `hf-dataset/` | 5 | 4 | - | - | - |
| `site/` | 20 | - | 19 | - | 72 |
| `site.json` | - | yes | yes | - | yes |
| `corrections/` | 48 | - | - | - | - |
| `extraction/` | 48 | - | - | - | - |
| `manifests/` | - | 19 | - | - | - |
| `references/` | - | 9 | - | - | - |
| flat export (`data/*.jsonl`) | - | - | - | 2 | - |
| integrity script | - | - | - | `verify_integrity.py` | `scripts/` |

Reading the table: `space_law` is the only one with a corrections register and an extraction
workspace; `seabed` and `bbnj` are the only ones with a persisted `capture/` layer; the two
unregistered corpora are the only ones carrying a `NOTICE` file, and digital-asset the only one with
a flat export. **A per-corpus toolkit is a corpus-local decision, not a programme-wide one** -
nothing in the connector depends on any of these directories, only on the pointer.

## Maintenance status

Status is evidenced by a corpus's own artefacts, never asserted:

| Status | Meaning | Evidence |
|---|---|---|
| **Live** | Source monitoring runs; changes are expected and swept | `monitoring/last_report.md` with a recent dated sweep |
| **Frozen** | Monitoring deliberately switched off; records honest as at their own retrieval date | A dated frozen notice; monitoring config removed or disabled |
| **Stale** | No monitoring and no recent activity; not deliberately frozen | Absent `monitoring/`, old last commit |

Current: `space_law`, `deep_seabed_mining`, `bbnj_high_seas` are **live** (last sweeps 2026-09-01);
`aml-sanctions` is **frozen** (2026-08-04); digital-asset is **stale** (last activity 2026-08-05).

### Two monitor versions, and why both are recorded

A `last_report.md` carries the version of the monitor that *produced it* (`_monitor v3.8_`), which is
not necessarily the version currently checked in. In the gap between shipping a monitor change and the
next scheduled sweep the two differ, and nothing inside a corpus can reveal it — a report filed by an
out-of-date monitor looks exactly like a healthy one. So each entry above names both: **last sweep by**
v3.8, **deployed code** v3.9. All four monitored corpora share a byte-identical `watch_sources.py`, so
their deployed versions should always agree; a divergence is drift, and is checked for automatically.

**Page-mode flags are not changes.** A whole-page hash can only report that *something* moved. A
re-flag at every sweep with a fresh hash is the signature of site churn, not law — see the
`deep_seabed_mining` entry for the worked case. Record-level (`schema` / `json_extract`) sources carry
a diff that says *what* changed and are the sources worth treating as signal.

Status is *not* currently exposed to connector callers. `list_corpora` returns the pointer, and the
pointer has no status field - adding one is a schema change, and the pointer-shape constraints below
apply.

## Toolchain attestation coverage

Reproducibility here is two properties, and they fail differently. **Pinning** says which toolchain
runs *now* - a statement about the present. **Attestation** says which toolchain a *given record* was
proven under - a historical claim, and the one that matters, because these corpora are append-only and
dated. A global pin cannot express "records 1-26 derive under 22.02.0, record 27 under something
else", and moving it silently restates the derivation claim for every record at once.

So an attestation is held beside the record it applies to (never in the derived layer - see below),
and is written **only where the text re-derived hash-for-hash in the same run**. Attesting an
unreproducible text would be a false provenance claim. Read from each repository's `main` on
**2026-09-16**:

| Corpus | Records attested | Where it lives | Toolchain pinned by | Engine gate in CI |
| --- | --- | --- | --- | --- |
| `space_law` | **18 of 24** - `poppler 22.02.0`; the 6 text-sourced records carry none | in the recipe: `extraction/<corpus_id>/<version_id>.json` -> `extractor.toolchain`, written at calibrate time | `runs-on: ubuntu-22.04` + fail-closed assert | **wired 2026-09-16** (`c08ae04`) |
| `deep_seabed_mining` | **32 of 37** - 26 at `poppler 22.02.0` (21 scan-derived, 5 born-digital), 6 text-sourced | per-record `extraction/<corpus_id>/<version_id>.json`, authored in CI | `runs-on: ubuntu-22.04`, module `PINNED_POPPLER`, fail-closed assert | wired |
| `bbnj_high_seas` | **14 of 16** - 13 at `poppler 24.02.0`, 1 at `pymupdf 1.28.2` | per-record `extraction/<corpus_id>/<version_id>.json`, authored in CI | `runs-on: ubuntu-24.04` + fail-closed assert; `pymupdf==1.28.2` | **wired 2026-09-16** (`fbd1dc8`) |
| `aml_sanctions` | **0 of 70, deliberately** | - | none | none |

**The engine gate had been dormant in two of these corpora.** `scripts/verify_engine.py` existed in
space-law and bbnj, but **no workflow referenced it** - so `scripts/extract.py`, the sole
version-pinned extractor, could have changed with nothing noticing. Both are wired now (`c08ae04`,
`fbd1dc8`); deep-seabed's was already live. AML has neither manifest nor gate.

**Records with no attestation, and why that is the honest record.** deep-seabed's five OCR-derived
ITLOS orders and bbnj's two OCR language versions (`-zh`, `-ar`) get **no file at all**: committed
deterministic code cannot re-derive an OCR text, so there is nothing to attest. The counts add up the
way the gates do - 32 + 5 = 37, and 14 + 2 = 16 - and the absence is named by the tool and by CI
rather than papered over. Text-sourced records are attested as `passthrough` where a format allows it,
which is a claim rather than a gap: nothing was derived from a toolchain.

**A born-digital record class where the pin turned out not to bite, and the claim is stronger for
knowing it.** The five born-digital #9 records (the two 18 July orders and the three declarations)
carry the Tribunal's own text layer, so they are extracted rather than OCR'd - and they derive
**byte-identically under `poppler 22.02.0` in CI and `26.01.0` on the workstation**, checked
hash-for-hash 2026-09-16. That does not make the CI derivation ceremony: the gate's claim is that a
record re-derives from committed code under the pinned toolchain, and only CI can make it. It does
mean the class is toolchain-stable where the scan-derived class is not, which is the opposite of what
"same corpus, same pin" would lead you to assume.

**AML is frozen, and its attestation is deliberately not backfilled.** Attesting it would mean
re-deriving 70 texts under a pinned toolchain - rewriting a frozen corpus to prove a property nobody
is querying. The freeze is the stronger statement: the corpus declares its own staleness and stops.
Backfilling would be the first change the freeze exists to prevent.

**Where attestation does not live.** The derived layer - all 147 `derived-metadata.yaml` files across
the four corpora (24 / 37 / 16 / 70) - contains **no toolchain string at all**, and no schema in the
lineage table declares a slot for one (checked 2026-09-16). Attesting there would be a *new* field,
not the reuse of an existing one, and generated metadata is the layer most prone to rebuild churn.

**The pitfall that makes this work, measured.** Attestations must be authored **where the pinned
toolchain runs - in CI, never on a workstation.** A local run under a different Poppler writes a
*confidently wrong* version into the file, which is worse than no attestation. Under a local Poppler
26.01.0 only **2 of bbnj's 14** recipes re-derive and **25 of deep-seabed's 26**; bbnj's texts are
attested at 24.02.0 rather than 22.02.0 because that is the toolchain they actually reproduce under,
which is why its pin is deliberately the newer image. Authoring is `workflow_dispatch`-only inside the
pinned job, and the commits come from CI.

One consequence worth knowing when reading a green history: GitHub suppresses workflow runs caused by
a push made with the default `GITHUB_TOKEN`, so **"CI committed it" is not "CI verified it"** - an
attestation commit does not re-trigger the job that checks attestations. Dispatch once more to see
them checked.

## Adding a corpus: checklist

1. **Build or identify the canonical repo.** It owns the texts, the hashes, the licence, the
   maintenance decision. It does not move into this repo, ever.
2. **Publish the dataset** (Hugging Face or equivalent) and record the URL - `canonical_dataset` is
   the field callers follow to get the full corpus.
3. **Decide `included_here`.** `sample_manifest_only` if a sample ships here; `none` if only a
   pointer does.
4. **Write `corpora/<corpus_id>/source_pointer.json`** using the 13-field shape above, honest
   `coverage_note` included.
5. **Write a `sample_manifest.json`** with a few provisions of a few instruments, official text
   only. Hashes are computed live from what ships here, so the sample must be genuinely official
   text.
6. **Check the schema constraint.** A new field means editing `mcp_server/schemas/corpus.schema.json`
   too, because `additionalProperties` is `false`.
7. **Run `pytest`.** All four test files. `test_read_only.py` will fail the build if anything
   write-shaped has crept in.
8. **Update this atlas and the README table.** An unregistered corpus in the README - or a registered
   one missing from it - is the drift this document exists to catch.

## What this atlas is not

- Not a client-facing summary. It is an internal roster that happens to live in a public repo, so it
  names no private corpus and carries no strategy.
- Not a conformance checker. It records what a corpus looks like today; a script that *tests*
  conformance is a separate artefact.
- Not authoritative about any corpus's contents. Where this atlas and a corpus repository disagree,
  the corpus repository wins - and the disagreement is a bug in this file.

## Provenance of this atlas

Read on **2026-09-14** from each corpus repository's `main` branch via the GitHub API and raw
content endpoints: manifest and schema files, directory trees, changelogs, `monitoring/` reports,
`NOTICE` files, and the Hugging Face dataset API. Schema hashes are SHA-256 of
`schema/authoritative-metadata.schema.json` at `main`, truncated to 16 characters. Counts are the
corpora's declared counts.

Refresh it when a corpus is registered, a corpus freezes or reactivates, a `schema/` file changes
hash, or **a corpus's deployed monitor version moves**. The schema-hash column is the cheapest early
warning: if a hash moves, the lineage table is wrong and any cross-corpus claim needs re-checking.

Two of those checks are automated outside this repo, in the portfolio monitor beside the corpora: it
verifies every schema hash above against the live repositories, alarms when a corpus's deployed
`watch_sources.py` version diverges from the rest of the portfolio, and reports a stale sweep. That
tool also runs weekly on a schedule. **The atlas is the claim; the monitor is the check** — when they
disagree, the atlas is wrong.
