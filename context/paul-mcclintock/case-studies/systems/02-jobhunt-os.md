# Job Hunt OS

**Live since Jul 27, 2026 · Third generation · Running in TEST mode**
*The longest-running system in the portfolio, and the only one that acts on the world*

---

## The problem

A senior job search is a daily operations problem wearing a writing problem's clothes. Scan the boards. Score each role against criteria that drift as you learn what you actually want. Verify the posting is still live rather than a ghost listing. Assemble tailored materials. Track replies. Follow up on schedule. Every day, for months, while employed.

## What it is

A scheduled agent whose brain is a private GitHub repository.

Every weekday at about 7:00 AM Eastern, a run clones the repo, does the day's work, commits, and pushes. The system README states the design principle in one line:

> "The commit history is the audit log of your search."

State lives in version-controlled markdown — settings, pipeline, ledger, trends. The operator edits any file, commits, and the next morning's run obeys it. The README again: **"Your edits always win."**

That is a genuinely good architecture choice. Git gives it durability, history, diffing, rollback, and an audit trail for free, and it makes the human's override the highest-precedence input in the system rather than a special case bolted on.

## The pipeline

Scan → score against rubric v2 → canonical-ATS verification that the posting is real and live → pipeline and ledger updates against a **213-role dedupe index** so nothing re-surfaces → packet generation for anything scoring 85 or above → submission by tier and mode → Gmail watched for replies with responses drafted → follow-ups at 7 and 14 days → warm-intro targets identified per submission → a morning brief pushed to the operator's phone.

The operator's share is about twenty minutes a day.

Submission is tiered rather than uniform, which is the detail that shows someone thought about failure: **Tier 1** auto-submits when the system is LIVE, **Tier 2** is prepared and handed to the operator's browser, **Tier 3** is queued with micro-guides for sites the agent cannot drive.

## The rubric, and why the version number matters

Rubric v2 weights **Talent 40 / Dynamism 25 / Compensation-against-target 25 / Practical 10**, with mission alignment as a **+5 bonus that is explicitly never a gate**.

The version number is the interesting part. Rubric v1 lived in the earlier Daily Search scanner and weighted **Compensation 35 / Mission 25 / Dynamism 22 / Company size 18**.

So between generations the weights were rewritten: compensation dropped from the top slot, company size disappeared entirely, "talent" — the quality of the people you'd work with — was introduced and given the largest weight, and mission was demoted from a 25% criterion to a bonus that can never disqualify a role on its own.

That is not a scoring system someone wrote once. It is a scoring system someone wrote, ran against real roles for months, watched behave badly, and revised. "Mission is a bonus, not a gate" is a specific correction to a specific failure mode — v1 was presumably scoring mission-aligned roles above roles that were better on every other axis.

**This is evaluation-criteria design with a feedback loop attached**, which is exactly what the role description asks for and is much harder to fake than a rubric that has only ever been written down.

## The safety design

The system can submit job applications on the operator's behalf. That is an irreversible, outward-facing action against real employers, and it ships gated.

A settings file carries `MODE: TEST`. Auto-submission engages only when that is changed to `MODE: LIVE` and committed. The README's status section describes the first run as a backlog triage in TEST mode, and advises flipping to LIVE only **"when you trust what you see."**

As of the README's writing, it is still in TEST.

This is the same instinct as Gmail Cleanup's dry-run phase, five months later, applied to something with much higher stakes than a mislabeled inbox. Nobody required either gate.

## What it retired

The README keeps an explicit **Retired** list, which is unusual and quietly impressive:

- **Notion** as the state store — killed within hours by the workspace's block cap
- **A Gmail-draft-as-state idea** — recorded verbatim as *"gross, correctly vetoed"*
- **CareerCalling** — parked
- **The Daily Search prompt** — superseded
- **Manual scan kickoffs**
- **The metric "roles surfaced"** — dropped as a vanity number

A system that documents its own dead ends is documenting its reasoning, and the last item is the sharpest one. "Roles surfaced" is the metric that makes a scanner look productive while telling you nothing about whether it works. Killing your own favourable metric is a real discipline.

## Three generations

This is the same job-to-be-done attacked three times in three different forms:

| | When | Form | Fate |
|---|---|---|---|
| **Daily Search** | Feb 2026 | A manual Cowork prompt producing ranked spreadsheets and briefs | Superseded |
| **CareerCalling** | Mar 2026 | A Next.js app with a database, fit scoring, and a kanban board | Parked |
| **Job Hunt OS** | Jul 2026 | An autonomous scheduled agent with git as its state store | Live |

The form that won has **no user interface at all**. For a single-user workflow, an agent writing version-controlled markdown beat an application with a database, auth, and a deployment — and it took building the application to learn that.

## Why it matters here

It is the longest-running thing in the portfolio, spanning February to the present across three architectures, and the only system that takes consequential real-world actions on the author's behalf.

It is also the claim most likely to be tested. The cover letter for this exact role says: *"my job search itself runs on a multi-agent Claude pipeline — scheduled agents that scan, score, and verify roles daily and assemble tailored materials. This application was assembled inside that system."*

This is that system. The hiring manager reads the claim before they reach the portfolio, which makes this the one entry that has to be airtight.

---

> **Note on evidence.** Everything above comes from the `SYSTEM README — Job Hunt OS — 2026-07-27.md` file on disk. The live repository (`FlipYaFaReal/jobhunt`) was not read — the operating spec, ledger, and trends files are described by the README but not independently verified. If the site quotes conversion numbers or ledger counts, pull them from the repo first.
