# SoccerRatings

**Jul 25 – Jul 27, 2026 · 57 commits · 10,115 lines · 2 active days · Next.js + Supabase**
*Status: shipped*

---

## The ask

Every year a youth soccer league asks volunteer parents to rate players so a committee can place them on balanced teams. The instrument is a shared Excel file — the BAYS "Evaluation Scorecard" — and it fails in four specific ways, all of which the design document names before proposing anything:

- **Volunteers don't know how to evaluate.** The form's only guidance is a generic 1–5 legend and a block of instructions most people never read.
- **Free text invites garbage.** People enter `1-2` ranges, leave blanks, score horizontally across a player instead of vertically down a category. Forms come back for redo, days later.
- **Spreadsheets get lost,** versioned wrong, and merged by hand.
- **There is no memory.** Last season's ratings sit in an old file and rarely inform placement.

## The insight

The interesting move is in goal two: *"Teach while collecting."*

Rather than writing better instructions, the app makes the league's scoring doctrine structural. You cannot score horizontally, because the interface only shows you one category at a time across every player. You cannot enter `1-2`, because the only input is a tap on a whole number. You cannot rate your own child, because the system will not offer them. And if you have used only 4s and 5s, the app says so at submit — configurable per season to either warn or hard-block.

The rules that used to live in a paragraph nobody read are now the shape of the screen. That is a product decision, not an engineering one, and it is the best single idea in this portfolio.

A smaller decision shows the same instinct: **5 is displayed first**, not last, because a good rating is the most common case and the interface should be fastest for the thing that happens most.

## What got built, in one day

- Magic-link sign-in, invite-only against the imported roster. No passwords, no self-registration; a typo'd email simply never receives a link and the admin fixes it.
- Category-first rating flow with tap-to-select whole numbers, auto-save on every tap, guarded against stale completions racing the save.
- A three-step CSV import wizard with **returning-player matching**, so a player's history survives roster churn between seasons.
- An admin-editable rubric with per-category anchor text — what a "3 in Passing" actually looks like — **snapshotted per season**, so historical data keeps the rubric it was scored under rather than being silently re-interpreted under a new one.
- A committee report: per-category and group averages, a multi-season weighted score, trend against last season, CSV export, and drill-down.
- **Data-quality flags surfaced rather than hidden** — "raters disagree," "single rater," "N not-rated" — so thin evidence is visible to the committee instead of averaging into false confidence.
- Installable as a PWA, for parents standing on the sideline with a phone.

## What was actually good here

This is the most rigorously built project of the eight, and it was built in a day.

The scoring aggregation library was written test-first. Row-level security got its own access-matrix integration tests, asserting on specific error codes and existence proofs rather than just "access denied." Playwright drives an end-to-end happy path through real magic links. Database grants for the anonymous role were cut to least privilege. `organization_id` is pinned inside the write policies so a volunteer cannot write across tenants even with a forged payload. Submissions lock on insert.

Then there is an entire pass of accessibility work that most side projects never get: keyboard access to report sorting and drill-down, dialog semantics and focus management on the submit confirmation, `inert` backgrounds behind open panels, print-hiding, and a screen-reader fix to suppress a redundant category hedge.

And the multi-tenancy is handled with unusual restraint. Every table carries an `organization_id`, exactly one organization is seeded, and there is no signup UI at all. The design document calls this "deliberately cheap insurance, not speculative features" — which is the correct amount of future-proofing and a sentence worth stealing.

## Where it went sideways

Nothing did. This is the control case.

Fifty-six commits on July 25 carry it from design document to a tested, secured, accessible, deployed PWA. The only commit after that, two days later, replaces the circular rating buttons with soccer balls.

The scope that shipped is the scope that was specified, and the non-goals list held completely: no native apps, no self-serve signup for other regions, no automated placement decisions, no rater-leniency normalization, no payments, and no player data beyond name, birth year, and team. Every one of those is a thing the project could plausibly have grown into. None of them did.

## The market read

Not a business, and never pretended to be. It is a civic tool for one league, running on free tiers — Vercel and Supabase — with Resend handling email specifically because Supabase's built-in mailer allows only a couple of messages an hour, which the design doc correctly identifies as unusable on evaluation night when reminders go out in a batch.

The pattern generalizes further than the domain does. Any volunteer-scored evaluation with a rubric and a committee has this exact shape: judged competitions, grant review panels, other youth sports. Nothing in the data model is soccer-specific except the rubric content, and that is admin-editable.

The most genuinely useful thing in the portfolio is also the least commercial. Worth saying plainly rather than dressing up.

## The lesson

This is what the previous five months bought.

ListingLift, in February, spent forty-six days growing ten times past its own PRD and never launched. SoccerRatings, in July, went from blank page to shipped in two days and stopped exactly where it said it would. Same person, same tools, same method — with the addition of a non-goals list written before the code, and the discipline to let it hold.

The difference between those two projects is the entire argument this portfolio is making.
