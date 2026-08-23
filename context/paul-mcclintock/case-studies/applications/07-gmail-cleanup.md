# Gmail Cleanup

**May 31, 2026 · 10 commits · 385 lines · 1 active day · Python + Gmail API**
*Status: shipped and used*

---

## The ask

An email account that has accumulated years of subscriptions, order confirmations, job alerts, marketplace notifications, and social digests, to the point where the inbox no longer functions as a signal. The goal, from the design spec: a near-zero inbox, mass-mailer noise routed out of sight, important mail self-organizing into labels, and the existing backlog cleaned up in one automated pass.

Small problem. Small program. It is in this portfolio for a reason that has nothing to do with size.

## The design, written first

The spec does the taxonomy work before any code, and the taxonomy is the actual product. Ten labels, each with a declared inbox behavior:

| Stays in the inbox | Skips the inbox |
|---|---|
| Personal, Work, Finance, Real Estate, Newsletters | Marketplace, Jobs, Retail, Social, Alerts |

The reasoning is stated: Personal, Work, Finance, and Real Estate are high-signal, so they stay and are labeled but not filed away. Everything else is routed out. Then the filter rules are specified concretely — sender domains and keyword patterns per category, down to naming the retailers and distinguishing Facebook Marketplace mail from other Facebook notifications, which are two different labels with two different inbox behaviors.

Decide the taxonomy, then write the code that installs it. The phase structure of the implementation ends up mirroring the phase structure of the spec exactly.

## The part that actually matters

This script permanently rewrites the label structure of a personal email account. Its first phase **deletes every existing label**. It then reaches into a backlog of years of mail and moves it.

That is a destructive, hard-to-reverse operation against irreplaceable personal data, and it was built:

1. **Dry-run first.** A phase that reports precisely what would change, before anything changes.
2. **Confirmation-gated.** The execute phase does not run until the user explicitly says go — and label deletion has its own separate confirmation.
3. **Fully logged.** Every action written to a file, so there is a record of what happened to what.

Nobody required that. There is no reviewer, no compliance requirement, no user to protect but himself. It is a 385-line personal script, and it was built with the same care you would want around a production data migration.

## What got built

OAuth against the Gmail API. Label setup that clears and installs the designed hierarchy. Filter installation, with skip-inbox-plus-label for mass mailers and label-only for newsletters. The dry-run phase. The execute phase with confirmation and file logging. Batched search and modify helpers to stay inside API quotas.

Then three cleanup commits that are worth reading as a set: remove dead code from `create_labels`; fix a logging initialization order bug and correct the no-reply matching patterns in the junk query; improve filter-deletion logging and clarify the query syntax. Someone went back through their own finished script, found the initialization-order bug, and fixed the log messages so the next person running it would understand what it was doing.

Then it stopped, because it was done.

## The market read

None, deliberately, and that is the point of including it.

This is a personal utility that took one day and solved the problem it was pointed at. It has no users to acquire, no roadmap, no v2. Putting it in a portfolio alongside a 26,000-line .NET platform is a statement about proportionality: the right amount of software for this problem was 385 lines, and recognizing that is a skill.

## The lesson

The most mature engineering judgment in this entire portfolio is in its smallest project.

Seven other projects here have more lines, more commits, more architecture, and more ambition. None of them demonstrate the instinct that shows up in this one: **irreversible operations should be inspectable before they run.** Dry run, confirm, log. It cost maybe an hour of the day and it is the difference between a script you can trust against your own email and one you cannot.

That instinct transfers directly. In a forward-deployed context — running something against a customer's real data, in their environment, where you do not get to undo it — that habit is worth more than any of the larger builds on this list. It is also the habit least likely to appear in a portfolio, because it does not look like a feature.

It looks like a phase called `--dry-run` that nobody asked for.
