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

1. Create `context/<your-name>/` using a lowercase, hyphenated form of your name.
2. Prefix your top-level documents with the same string.
3. Start with an `OVERVIEW.md` that says what your documents contain and how they should be used.

Nested files (like case studies) do not need the prefix — the folder path already carries it.

## Conventions worth keeping

**Mark provenance.** Paul's documents tag every claim as `verified` (checked against files or history), `quoted` (lifted from a document he wrote), `reported` (his recollection, not independently checkable), or `drafted` (written by a model as analysis). If these documents are going to be fed to a model or read by someone making decisions, the difference matters, and it is much easier to tag as you write than to reconstruct later.

**Keep a VERIFY file.** A single place listing what has not been confirmed is more useful than hedging inside every document.

**Redact before publishing, not after.** This repository is **public**. Anything client-confidential, employer-confidential, or personal should be withheld or abstracted before it is committed — git history keeps what you push even if you delete the file afterwards. Paul's folder has one item withheld on these grounds, marked in place rather than silently omitted, and contact details stripped from his CV and cover letter.
