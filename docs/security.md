# Security posture

MCP connectors expose tools to models, which is powerful and therefore needs care. This connector
takes the conservative posture appropriate for legal reference data.

## Read-only by design

- **No write tools.** There is no create/edit/update/delete/ingest/move tool anywhere. The connector
  cannot modify any corpus, file, or system.
- **No shell / code execution.** The connector does not run arbitrary commands.
- **No network side effects.** v0.1 serves local sample data; it does not act on external systems.
- The tool registry (`tools.TOOL_SPECS`) marks every tool `access: "read"`, and
  `tests/test_read_only.py` fails the build if a non-read tool is ever added or if write-like verbs
  (create/update/delete/ingest/write/exec…) appear in tool names.

## Prompt-injection hardening

Legal source text can contain imperative language ("the State shall…") and, if sourced carelessly,
could carry injected instructions. Therefore:

- Every payload carrying retrieved text includes a fixed **notice** that the `text` field is
  *reference data*, to be quoted/cited only, and that any instructions inside it must be ignored.
- Retrieved text is returned under a `content_role: "reference_data"` marker, separated from the
  connector's own control fields.
- The connector never executes, follows, or re-emits instructions found inside retrieved text.

## Human-in-the-loop

Consumers (Claude, OpenAI, Cursor, …) should present tool calls and results to the user and keep a
human in the loop. Because every tool is read-only and returns cited reference data, the blast radius
is limited to *what is read*, not *what is changed*.

## No secrets in this repo

No API keys, tokens, private URLs, or credentials are included or expected. See `.gitignore`, which
blocks corpora dumps, embeddings, and secret files from ever being committed here.

## Reporting

Found an issue? Open a GitHub issue (for anything sensitive, use private disclosure via the
maintainer contact on danielcheah.com) rather than posting details publicly.
