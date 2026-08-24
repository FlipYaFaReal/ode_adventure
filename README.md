# ode_adventure

Shared context repository.

Each contributor keeps their own context documents in a folder under `context/`, named for them. Files inside a person's folder are prefixed with that person's name, so a document still identifies its owner if it is downloaded, quoted, or fed to a model on its own.

```
context/
  paul-mcclintock/
    paul-mcclintock-OVERVIEW.md        <- start here
    paul-mcclintock-cover-letter.md    <- the claims
    paul-mcclintock-CV.md              <- background
    paul-mcclintock-portfolio.json     <- structured source of truth
    paul-mcclintock-VERIFY.md          <- what is verified vs. inferred
    paul-mcclintock-DEFERRED.md        <- parked items
    paul-mcclintock-source-ai-journey.md
    case-studies/
      applications/   systems/   judgment/
  <second-contributor>/
  <third-contributor>/
```

## Adding your own

**Fastest path: [`context/CONTRIBUTOR-PROMPT.md`](context/CONTRIBUTOR-PROMPT.md).** Paste it into an assistant and it will interview you, verify what it can, and write your files in these conventions. Read what it produces before committing — a fluent invented claim is worse here than a missing one.

Or by hand:

1. Create `context/<your-name>/` using a lowercase, hyphenated form of your name.
2. Prefix your top-level documents with the same string.
3. Start with an `OVERVIEW.md` that says what your documents contain and how they should be used.

Nested files (like case studies) do not need the prefix — the folder path already carries it.

## Conventions worth keeping

**Mark provenance.** Paul's documents tag every claim as `verified` (checked against files or history), `quoted` (lifted from a document he wrote), `reported` (his recollection, not independently checkable), or `drafted` (written by a model as analysis). If these documents are going to be fed to a model or read by someone making decisions, the difference matters, and it is much easier to tag as you write than to reconstruct later.

**Keep a VERIFY file.** A single place listing what has not been confirmed is more useful than hedging inside every document.

**Redact before publishing, not after.** This repository is **public**. Anything client-confidential, employer-confidential, or personal should be withheld or abstracted before it is committed — git history keeps what you push even if you delete the file afterwards. Paul's folder has one item withheld on these grounds, marked in place rather than silently omitted, and contact details stripped from his CV and cover letter.

## What this repository is for

A joint application to **[Bring Your Own Engineering Team](https://jobs.ashbyhq.com/odewithanthropic/5e655487-e0f9-4471-96fd-355b1f5e0185)** at Ode with Anthropic — their route for intact teams of 2–5, where one interview process leads to one offer made to the whole team at once.

That shapes what belongs here. The premise of the route is that **the team is the asset**, so the package has to read as a pod rather than as several strong individuals filed next to each other. Two things follow:

- **Position against your collaborators, not beside them.** Overlap is fine; unexplained overlap looks like nobody has worked out who does what.
- **Show the working, not just the output.** The posting is under Engineering and describes forward-deployed work: ambiguous problems, real clients, decisions made with incomplete information. A case study explaining a hard trade-off is worth more than three listing features.
