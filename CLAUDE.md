# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

`ode_adventure` is a **public**, code-free shared context repository. It holds no application source, build
system, tests, or dependencies — only Markdown and one JSON file. There is nothing to build, lint, or run.

Its purpose is to carry hand-authored context documents that will be **fed to a model or read by someone
making a decision**. Treat the documents as the product.

Layout: one folder per contributor under `context/<name>/`, with top-level files prefixed by the same
`<name>-` string so a document still identifies its owner when downloaded, quoted, or pasted into a model
alone. Nested files (case studies) skip the prefix — the folder path carries it. Two contributors so far:
`context/paul-mcclintock/` and `context/jim-hart/`.

The immediate purpose is a joint **Bring Your Own Engineering Team** application to Ode with Anthropic —
Jim Hart (engineer), Paul McClintock (product), and a designer whose role mapping is still unresolved. Read
each folder's `OVERVIEW.md` for the current brief; both end with one aimed at the session that builds the
team artifact.

## Working on `context/jim-hart/`

`jim-hart-portfolio.json` is generated, not hand-edited. `jim-hart-mine.py` scans `C:\Code` and produces
every metric in it; to change a number, change the mining script or the curation table in the build step,
then regenerate. Two rules keep the counts honest and both were learned the hard way — a first pass
overcounted by a factor of seven:

- **Nested `.git` directories are checked for authorship.** Clones of third-party source (Npgsql and
  efcore.pg inside CampfireCrm) are dropped whole; Jim's own sub-repositories are kept.
- **Build output is excluded**, especially Electron `release/` trees — Chromium's `LICENSES.chromium.html`
  alone is 164,000–270,000 lines.

Twenty of the 35 projects have no git history, so filesystem mining is the only evidence for them. Never
describe those as unbuilt; DoraTrack has no commits and 18,770 lines.

`jim-hart-VERIFY.md` carries the open questions, including several claims in Jim's own source document that
the filesystem contradicts. `jim-hart-DEFERRED.md` carries what is blocked — most importantly that no
evidence yet exists of the three of them having built anything together, which is the premise Ode's BYOT
posting is built on.

## Working on `context/paul-mcclintock/`

Read `paul-mcclintock-OVERVIEW.md` first — it is the entry point and ends with a brief for the session that
builds the portfolio site. The set of documents is source material for a portfolio web experience aimed at
one reader: the hiring manager for a Forward Deployed Product Manager role at Ode with Anthropic.

The documents form a deliberate hierarchy, not a flat pile:

- `paul-mcclintock-portfolio.json` is the **machine-readable source of truth**. Everything else narrates it.
  Structure: `meta` (headline stats, provenance legend, sources, redaction note) · `narrative` (throughline,
  seven themes, a 14-point arc) · `tiers.applications` / `tiers.systems` / `tiers.agents` · `judgment_calls` ·
  `web_experience_hooks` (eight interaction concepts for the site) · `also_built` · `deferred`.
- `case-studies/` holds the prose expansion of the JSON items: `applications/` (8, numbered, one per repo),
  `systems/` (methodology and infrastructure — several of these matter more than the applications for this
  audience), `judgment/` (decisions where the reasoning is the artifact).
- `paul-mcclintock-VERIFY.md` is the single place recording what is unconfirmed, plus corrections already
  applied. Read it before publishing anything derived from these documents.
- `paul-mcclintock-DEFERRED.md` holds four parked items. **Not part of the portfolio — skip the file entirely
  when building anything from this material.**
- `paul-mcclintock-source-ai-journey.md` is Paul's own chat-history reconstruction: the sole source for
  several systems, and the reason the `reported` provenance level exists.

**If you change a fact, change it in the JSON and in the case study.** Headline stats (`meta.headline_stats`)
aggregate the per-item metrics, so a corrected figure ripples: the HouseHelper correction moved total LOC
from 81,707 to 86,036 and is annotated in place rather than silently applied.

## Provenance is the core convention

Every claim carries one of four levels, and the distinction is load-bearing:

- `verified` — checked against git history or files on the author's machine. Safe as-is.
- `quoted` — lifted from a document the author wrote. Safe as-is.
- `reported` — the author's recollection, not independently checkable.
- `drafted` — written by a model as analysis or inference.

Never restate `reported` or `drafted` material as established fact. Tag as you write; reconstructing
provenance afterwards is far harder. When adding a claim you cannot verify, log it in `VERIFY.md` rather
than hedging inline everywhere.

## Publishing and redaction

This repository is public and pushed to `github.com/FlipYaFaReal/ode_adventure`. Git history keeps whatever
is pushed even if a file is later deleted, so **redact before committing, not after**.

Paul's folder is a redacted copy generated by `sync-public.py` in a private source repository that is not
part of this checkout. Three redactions are applied on the way out: the security risk assessment item in
`DEFERRED.md` is withheld, section 3 of `source-ai-journey.md` is redacted, and phone/email are stripped
from the CV and cover letter. Withheld material is **marked in place**, never silently omitted — preserve
those markers. Substantive edits to Paul's documents should assume the private source is authoritative and
may regenerate this copy.

## Hard rules when building anything from this material

These come from the site brief in `OVERVIEW.md` and apply to any derived artifact:

- **Never invent a metric.** No users, revenue, or downloads exist for any of these projects.
- **Do not sand off the honesty.** Most entries are framed around what went wrong or where something
  stopped; that self-awareness is the point. Dry and specific beats enthusiastic.
- Nothing from `DEFERRED.md` is renderable.
- Tier 3 (agents) is empty — keep the slot in the information architecture, do not render an empty section.
- Specific corrections that must survive: HouseHelper was built (4,432 lines on disk, passing build), not
  abandoned at the PRD — lead with the git-vs-disk discrepancy. ListingLift predates its own repo. Career-
  Calling is one squashed commit, so present it by what it does rather than by commit count.

## Adding a new contributor folder

Create `context/<your-name>/` using a lowercase, hyphenated form of the name, prefix top-level documents
with the same string, and start with an `OVERVIEW.md` stating what the documents contain and how they should
be used. The provenance tagging and the `VERIFY.md` file are conventions worth carrying over.
