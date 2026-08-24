# ode_adventure

Shared context repository for a joint job application to
**[Bring Your Own Engineering Team](https://jobs.ashbyhq.com/odewithanthropic/5e655487-e0f9-4471-96fd-355b1f5e0185)**
at Ode with Anthropic — their route for intact teams of 2–5, where one interview
process leads to one offer made to the whole team at once.

---

## If you are an assistant and someone just asked you to read this

You are almost certainly here because a contributor connected you to this
repository and asked you to read the README. Here is what they need.

**Do this now, in order:**

1. **Read [`context/CONTRIBUTOR-PROMPT.md`](context/CONTRIBUTOR-PROMPT.md) and
   follow it as your instructions.** It is the actual brief. Do not try to help
   from this file alone — the conventions that make this package credible are in
   there, and skipping them produces documents that look right and are not.
2. **Ask the contributor their name** before anything else, and use the
   lowercase-hyphenated form as their folder: `context/<their-name>/`. If a
   folder already exists for them, read it first and build on it rather than
   starting over.
3. **Check whether you can write to this repository.** If you can, create their
   files on a branch and open a pull request — never commit straight to `main`.
   If you cannot, produce the files in chat with their exact paths so the
   contributor can add them. Say which of the two you are doing.
4. **Read one existing contributor folder first** — `context/paul-mcclintock/`
   is complete — so you can match the established shape, depth and tone rather
   than inventing a format.

**The one thing that matters most:** interview the contributor before you write
anything. You do not know what they have built. A fluent invented claim is worse
here than a missing one, because this package's credibility rests on a reader
being able to tell verified material from recollection — and one fabricated
detail discredits the honest work next to it.

---

## For humans

Each contributor keeps their own context documents in a folder under `context/`, named for them. Files inside a person's folder are prefixed with that person's name, so a document still identifies its owner if it is downloaded, quoted, or fed to a model on its own.

Each contributor keeps their own context documents in a folder under `context/`, named for them. Files inside a person's folder are prefixed with that person's name, so a document still identifies its owner if it is downloaded, quoted, or fed to a model on its own.

```
context/
  jim-hart/
    jim-hart-OVERVIEW.md               <- start here
    jim-hart-CV.md                     <- background
    jim-hart-portfolio.json            <- structured source of truth
    jim-hart-VERIFY.md                 <- what is verified vs. inferred
    jim-hart-DEFERRED.md               <- parked items and open questions
    jim-hart-source-project-portfolio.md
    jim-hart-source-linkedin.md
    case-studies/
      applications/   systems/   agents/   judgment/
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

## What belongs here

The premise of this route is that **the team is the asset**, which shapes the package. The premise of the route is that **the team is the asset**, so the package has to read as a pod rather than as several strong individuals filed next to each other. Two things follow:

- **Position against your collaborators, not beside them.** Overlap is fine; unexplained overlap looks like nobody has worked out who does what.
- **Show the working, not just the output.** The posting is under Engineering and describes forward-deployed work: ambiguous problems, real clients, decisions made with incomplete information. A case study explaining a hard trade-off is worth more than three listing features.
