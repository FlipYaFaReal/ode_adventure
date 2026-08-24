# Contributor prompt

Building your section of this repository from scratch is slower than it needs to
be. Paste everything below the line into Claude (or whatever you use) and it will
interview you, verify what it can, and write your files in the conventions this
repo already uses.

**It will ask you questions.** The answers are the work — everything else it can
do for you. Read what it produces before you commit it; a fluent invented claim
is worse here than a missing one, because this package's credibility rests on
being able to tell the two apart.

---

You are helping me build my contributor section of a joint job application. Work
with me interactively: **interview me first, write files second.** Do not draft
my portfolio from assumptions — you do not know what I have built, and guessing
is the one failure that would sink this.

**IF YOU ARE ALREADY CONNECTED TO THIS REPOSITORY**

Then you were probably sent here by the README rather than pasted into a chat.
Two adjustments: read `context/paul-mcclintock/` first to see the shape and depth
expected, and when you write, open a **pull request** rather than committing to
`main` — a contributor should get to read their own section before it lands. If
you have no write access, output the files with their full paths and say so.

**THE CONTEXT**

Ode with Anthropic is Anthropic's services venture — they take frontier AI into
production for client companies, working in small pods. We are applying together
through their **"Bring Your Own Engineering Team"** route: a posted programme for
intact teams of 2–5. One interview process, same day, same panel, then a single
offer made to the whole team at once. Their words: *"the same bar we hold every
Ode engineer to."*

**That posting sits under Engineering.** The package has to argue that we are an
engineering pod — not several individuals with adjacent skills who happen to know
each other. Your section needs to carry engineering weight and to show how you
work *with a team*, because the premise of the route is that the team itself is
the asset.

Ask me who my collaborators are and what they do, so you can position my section
against theirs rather than duplicating them.

**THE REPOSITORY AND ITS RULES**

Everything goes in `context/<my-name>/`, lowercase and hyphenated, in a **public**
GitHub repository. That means:

- **Nothing client-confidential or employer-confidential.** Abstract it or leave
  it out. If something matters but cannot be published, say that it exists and is
  withheld — do not silently omit it, and do not sanitise it into meaninglessness.
- **No contact details.** No phone, no personal email. LinkedIn is fine.
- Git history keeps whatever is pushed, so redact *before* committing, not after.
- Top-level files carry my name as a prefix, so a document still identifies its
  owner if it is downloaded or fed to a model on its own — `<my-name>-OVERVIEW.md`,
  `<my-name>-CV.md`. Files nested in subfolders do not need it.

**THE PROVENANCE RULE — this is the important one**

Every substantive claim gets tagged with where it came from:

- **`verified`** — checked against a real artifact: a repo, a commit history, a
  file, a live URL.
- **`quoted`** — lifted from something I wrote.
- **`reported`** — my recollection. Specific and plausible, *not independently
  checkable.*
- **`drafted`** — your analysis or inference, not my statement.

Keep a `<my-name>-VERIFY.md` listing everything `reported` or `drafted`. One
honest list of what is unconfirmed is worth more than hedged language scattered
through every document — and a reader who can see which claims are checkable will
trust the checkable ones more.

**HOW TO WORK WITH ME**

1. **Interview me first.** What have I built, where does the evidence live, what
   did I do versus what the team did, and what do I want to be known for. Ask
   follow-ups. Do not move on from a vague answer — *"led the migration"* is not
   yet a claim anyone can assess.
2. **Then verify what you can.** If you can read my filesystem or my repositories,
   look at them. Count commits, read the code, check whether the thing runs.
   **Do not rely on `git log` alone.** On this project a claim of "specified but
   never built" turned out to be wrong because the author trusted commit history
   and never opened the working tree — four thousand lines of finished,
   build-passing code were sitting there uncommitted. Check the files.
3. **Tell me what you could not verify** and tag it `reported`, rather than
   quietly promoting it to fact.
4. **Then write the files.**

**WHAT TO PRODUCE**

- `<my-name>-OVERVIEW.md` — start here. What my documents contain, how to read
  them, what a reader should conclude.
- `<my-name>-CV.md` — background, contact details stripped.
- `case-studies/` — one file per substantial thing I built. For each: the problem,
  what I chose and why, what I would do differently, and the evidence. **The
  reasoning is the artifact.** A case study that explains a hard trade-off is
  worth more than three that list features.
- `<my-name>-VERIFY.md` — everything unconfirmed.

**WHAT NOT TO DO**

- Do not invent projects, metrics, dates, or numbers. If you need a figure I have
  not given you, ask for it.
- Do not write in a voice I would not use out loud. Engineers read this.
- Do not pad. Four well-evidenced case studies beat ten thin ones, and the thin
  ones actively hurt — they invite a reader to discount the strong material too.
- Do not claim team achievements as mine. Say plainly what my part was; being
  specific about a smaller contribution reads as more credible, not less.

**START BY ASKING ME:** what have I built that I would be willing to be
questioned on for an hour by a good engineer — and where does the evidence live?
