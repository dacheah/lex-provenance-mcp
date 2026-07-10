# Commercial model & how to get more

This connector is intentionally the **free razor**. It is genuinely useful on its own - but the
enriched, connected, and hosted layers are a separate offering. This page is both the boundary
(what's free) and the invitation (how to get the rest).

## Free / open (this repo)

- The read-only connector and its tools (in-corpus search, fetch, verifiable citations).
- The JSON Schemas and adapter notes.
- Sample manifests pointing to the public canonical corpora.
- The full public corpora themselves, at their canonical homes (GitHub + Hugging Face), under
  CC BY 4.0 for the compilation (source texts keep their own terms).

## Premium (not in this repo)

| Capability | What it adds |
|---|---|
| **Full enriched corpora** | Every instrument, verified hashes, complete provision coverage, concept tags - kept current as the law changes |
| **Cross-corpus intelligence** | A working `compare_provisions` (the shipped tool is a stub): cross-reference graphs (e.g. BBNJ <-> UNCLOS) and relation queries |
| **Change alerts & relevance** | The corpus is kept current in-house; this layer proactively notifies you when a change lands - with a plain-language summary of what changed and why it matters to your use |
| **Hosted MCP endpoint** | Managed, authenticated, SLA-backed access - no local setup |
| **Embeddings / semantic search** | Vector search over the authoritative + derived layers |
| **Private-corpus onboarding** | Stand up a provenance-first corpus for *your* domain (sanctions, financial regulation, AML, data protection, ...) behind the same connector |

The open `compare_provisions` tool is a deliberate **stub**: it returns the response shape and the two
(free) verifiable citations, but performs no cross-corpus reasoning. The connective intelligence is
the paid frontier.

## Distribution

The maintained layer is delivered two ways, to fit how you already work - the same
provenance-verified, kept-current corpus through either channel:

- **Hosted MCP endpoint** - a managed, authenticated API for AI agents and applications (this
  connector, hosted, with SLAs).
- **Governed data marketplaces** - the maintained dataset listed on AWS Data Exchange, Snowflake
  Marketplace, and/or Databricks Marketplace, so enterprise data teams can subscribe with entitlement
  and billing handled by the platform.

Pick the channel that fits your stack; both serve the same corpus.

## Trust posture

- **Neutral.** The corpora record what legal instruments say. They take no legal position and do not
  represent anyone's view of the law - a neutral record is what makes them safe to build on.
- **Verifiable.** Every provision carries a source, a dated version, and a SHA-256 content hash. Items
  not independently verified are flagged **[verify]** so a reviewer can check them. Provenance is the
  product: a citation you can re-verify, not a scraped snippet.

## Who this is for

Legal-AI and data teams building retrieval or training pipelines that need provenance-tagged,
low-drift legal sources; GRC / reg-tech vendors wanting a rigorously-sourced legal spine; and
institutions that need a specific body of law stood up as auditable, machine-readable infrastructure.

## Getting in touch

> **Interested in the full corpora, cross-corpus intelligence, a hosted endpoint, or a
> provenance-first corpus for your own domain?**
>
> - Open a GitHub issue on this repo (label: `commercial`), or
> - Reach the maintainer via the contact on **contact@danielcheah.com**.

Tell us: the body of law or jurisdiction, whether you need hosted vs self-managed, and your use case
(RAG, compliance, research, product). That's enough to scope a pilot.

---

*Business information, not an offer or financial/legal advice. Any engagement is under a separate
written agreement.*
