# HouseHelper

**Mar 9, 2026 · 4,432 hand-written lines · 37 files · 9 of 10 tasks done · Next.js + Prisma**
*Status: built, never committed*

---

## A correction, first

The first pass through this portfolio described HouseHelper as "the complete product definition for a collaborative house-hunting app, and no product." That was wrong, and how it was wrong is more interesting than the project.

Git shows one commit: `Initial commit from Create Next App`, 103 lines of scaffold. Reading only the repository, the conclusion is obvious and incorrect.

The working directory holds 4,432 hand-written lines across 37 files. Auth routes with NextAuth. Group creation, settings, and an invite-by-code join flow. Listing CRUD with grid, detail, and edit pages. Star ratings with per-user and aggregate display. Threaded comments. A reorderable viewing queue. A dashboard. A Prisma schema with seven models — User, Group, GroupMember, Listing, Rating, Comment, QueueItem — exactly the seven named in TASK-001's acceptance criteria.

The workflow state file is unambiguous:

> `"work_items": { "total": 10, "backlog": 1, "done": 9 }`
> `"notes": "All core features implemented. Build passes. TASK-010 (sorting/filtering) still in backlog. Need PostgreSQL running to test at runtime."`

It was built. The build passed. None of it was ever committed.

## The ask

House hunting with other people is a coordination problem nobody has tooling for. The PRD: no simple way to collaboratively track listings, share opinions, and prioritize which homes to visit, so people fall back on scattered text messages, spreadsheets, and mental notes.

Three personas, drawn from life. The **Owner** searching for a house and making the final call. **Family Members** who want to see listings and care about specific things — room size, the neighborhood, the yard. **Friends** acting as trusted advisors who may find listings independently.

## The product definition

The most complete piece of front-half product work in the portfolio, and it was produced by the multi-agent workflow rather than written by hand.

A **MoSCoW-prioritized** backlog: eight Must Haves, three Should Haves, three Could Haves, and five explicit **Won't Haves** for v1 — mortgage calculator, AI recommendations, listing scrapers, chat between users. Writing down what you are *not* building, before building, is the highest-leverage habit in this portfolio, and here it appears in its purest form.

Then success metrics, non-functional requirements including WCAG 2.1 AA and sub-two-second loads on 4G, seven numbered user stories as separate documents, an architecture document, and an ADR on the Next.js App Router.

And underneath that, the machinery: four decision records, ten work items with acceptance criteria and dependency graphs, a session log for March 9 that opens `Agent: PM — Analyzing product idea — Convening expert panel for requirements definition`, and a state file tracking the backlog-to-done pipeline.

## Where it actually stopped

Not at the edge of building. At the edge of *running*.

Everything up to and including a passing build was delegable, and it got delegated. What remained was the part that could not be: stand up a PostgreSQL instance, point the app at it, and watch the thing work. The single recorded blocker is not a design problem or a market problem. It is `Need PostgreSQL running to test at runtime.`

That is where a working application stopped and sat for five months.

## The tell

The uncommitted state is the evidence, and it cuts in a specific direction.

Nine-tenths of a finished application sat in a directory without a `git add`. Not the PRD, not the user stories, not the decision records, not the 4,432 lines of source. A project that someone deliberately concluded tends to leave a note. This one left a full application nobody pressed save on.

Whatever happened here, it happened after the interesting work was done and before the boring work started — and the boring work was thirty minutes of Docker.

## The market read

Thin, and worth stating separately from the ending. Zillow and Redfin both ship collaborative shortlists and shared searches, free, inside the app where the listings already are. A standalone tool has to be materially better at the collaboration to overcome not owning the inventory, and the PRD's feature set is roughly what the incumbents already give away.

That is a good argument for not building it. But it cannot be the reason it stopped, because it was already built.

## The lesson

There are two, and the second one is the useful one.

**On the project:** the failure mode here is not losing interest in an idea. It is stalling at the transition from generated work to operated work — the moment the thing has to leave the model's hands and run in the world. That is a real and common failure in agentic development, it is worth naming precisely, and it is a more honest thing to say in an interview than "I decided the market was too thin."

**On the portfolio:** I got this wrong by trusting `git log` and never looking at the filesystem. The repository said 103 lines; the disk said 4,432. Anyone auditing this portfolio the way I first audited this project will reach the same wrong conclusion — which means the write-up has to *lead* with the discrepancy rather than let a reader discover it.

---

> **Correction logged 2026-08-22.** The earlier version of this case study, and the `specified, never built` status in the first release of `portfolio.json`, were both wrong. Corrected after inspecting the working tree rather than only git.
