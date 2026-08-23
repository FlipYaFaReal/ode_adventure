# CareerCalling

**Mar 8, 2026 · 1 commit · 7,313 lines · 1 active day · Next.js + Prisma + Claude**
*Status: built; superseded by a scheduled multi-agent pipeline*

---

## The ask

Job searching as a product professional is a coordination problem wearing a motivation problem's clothes. The PRD lists it plainly: scanning multiple boards manually, mentally assessing fit against dozens of listings, rewriting a resume and cover letter for each application, tracking it all in spreadsheets with no analytics, and slowly losing track of where you stand across everything in flight.

The target user is "Alex," a senior PM with eight-plus years, searching while employed, who wants to apply to five to ten well-matched roles a week. In practice the target user was the author.

## The success criteria, which are unusually specific

Most personal-project PRDs skip metrics. This one doesn't:

- Under **10 minutes** from discovering a job to a completed application.
- Manage **50+ active applications** without losing track.
- Fit scoring agrees with the user's own gut read **more than 80%** of the time.
- AI-generated materials need **under 3 minutes** of editing.

That third one is the interesting metric, because it is the only one that measures whether the AI is any good rather than whether the app is fast. It is a genuine evaluation criterion for a model-driven feature — the kind of thing the Ode role description calls "evaluation criteria for AI systems" — and it was written before the build.

## What got built

A structured professional profile: skills inventory categorized by technical, domain, leadership, and tools; experience; target titles and industries; compensation floor; location preferences; values.

Job ingestion four ways — Adzuna API search, manual entry, URL import with parsing, CSV bulk upload — all normalizing to the same record shape.

Claude-powered fit scoring, 0 to 100, across five dimensions: skills match, experience level, compensation alignment, culture fit, location compatibility. Critically, **explainable** — the UI shows which factors moved the number up or down, and the user can override the score manually. Somebody who has watched a black-box relevance score lose a user's trust built that override.

Then tailored resume and cover letter generation with in-app editing and PDF export, a kanban tracker with drag-and-drop stage management, and an analytics dashboard with funnel visualization and response rates.

## Where it went sideways — and why that's the good part

One squashed commit on March 8 containing the entire application, and nothing after. Git history tells you essentially nothing about how it was built, which is worth saying up front rather than letting a reader discover it and draw their own conclusion.

But the abandonment is more interesting than the build, because of what replaced it.

The author's own cover letter for this role describes his job search as running on "a multi-agent Claude pipeline — scheduled agents that scan, score, and verify roles daily and assemble tailored materials." The Job Hunt directory corroborates a *running process* rather than a running app: dated `Best_Fit_Opportunities` spreadsheets from February through May, `Top_5_Opportunity_Briefs` documents, a `SYSTEM README — Job Hunt OS`, and tailored CV and cover-letter pairs for roughly twenty employers, each named for its company.

So the app was built in a day, and then the same job-to-be-done kept getting done — by scheduled agents writing files, with no UI, no database, and no kanban board.

## The market read

The product market is crowded and unattractive. Teal, Simplify, Huntr, and a long tail of AI resume tools occupy this space, most of them free at the tier that matters. Consumer job-search tooling also has famously brutal retention economics: the product succeeds by making itself unnecessary, and every satisfied user churns by definition.

But the more useful read is not about the market at all. **For a single-user workflow, scheduled agents beat a web application.** No auth to build, no database to migrate, no UI to maintain, no deployment. The output is spreadsheets and markdown briefs, which are already the formats a human wants to read and edit. The agent pipeline does the same work with roughly none of the software.

That is the most interesting product decision in the entire portfolio, and it exists in no repository.

## The lesson

Building the app is the reflex. Asking whether the job actually needs an app is the product skill.

This is the one project where the second question got asked and answered — and it got answered by abandoning something that had just been built, which is the expensive way to learn it and the way that actually sticks.

There is also a neat recursion worth noting: the application materials submitted for this role were assembled by the pipeline that replaced this app. The cover letter says so explicitly.

---

> **Needs the author's confirmation.** The read above — that CareerCalling was deliberately superseded by the agent pipeline rather than simply abandoned — is inferred from the cover letter and the dated files in the Job Hunt directory. It is a strong inference and a great story, but it is an inference. If the truth is "I built it and lost interest," that should be the version told, because it is checkable and the other one isn't. See `VERIFY.md`.
