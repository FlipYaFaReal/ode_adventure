# VERIFY — read before publishing any of this

Four provenance levels are used throughout:

- **verified** — from git history or files on this machine. Safe as-is.
- **quoted** — lifted from a document you wrote. Safe as-is.
- **reported** — from your chat-history reconstruction. Specific and plausible, but **not checkable here.**
- **drafted** — my analysis or inference. **That's most of this list.**

---

# ⚠️ Parked items

Four items were parked on 2026-08-22 and moved to `paul-mcclintock-DEFERRED.md`: **Kip**, a **security
risk assessment**, a **contract evaluation project**, and a **POC built with Fable.**

The security item is **withheld from this public repository** pending a confidentiality decision. It is
client- and employer-confidential and is held locally only.

**Operation Teleport** stays in the portfolio and touches personal circumstances. The write-up covers only
operational and methodological content. Keep it that way.

---

# Corrections already made

## ✅ HouseHelper — I had this materially wrong
**First pass said:** "specified, never built." **Actually:** built. 4,432 hand-written lines, 37 files, 7 data models, workflow state reading *"All core features implemented. Build passes."* — 9 of 10 tasks done. Only the 103-line scaffold was ever committed.

I trusted `git log` and never looked at the filesystem. Fixed in the JSON and the case study, and the case study now leads with the discrepancy. **Total LOC revised 81,707 → 86,036.**

## ✅ CareerCalling — resolved, and my original read was wrong
Job Hunt OS's README carries a Retired list: *"CareerCalling (parked), Daily Search CLAUDE.md (superseded)."* Three generations — Daily Search (Feb) → CareerCalling (Mar) → Job Hunt OS (Jul). CareerCalling is the middle generation, parked; it was not displaced by a pipeline that already existed. Documented, not inferred.

---

# Still needs your confirmation

## Motives I attributed to you

**1. HouseHelper — why did it stop at "needs PostgreSQL running"?**
I wrote it as stalling at the transition from *generated* work to *operated* work. That's an inference from the blocker note and the uncommitted state. Is that what happened, or did something else pull you away that week?

**2. TradeParrot — was auto-execution deliberate?**
Final commit is `default auto-exec ON`. Was that a decision you'd defend, or drift you'd flag yourself? **And was it ever trading real money, or paper only?** The repo shows both a paper layer and live Alpaca execution. That distinction matters if anyone asks.

**3. ListingLift — why didn't it launch?**
I wrote "building was more rewarding than launching." TradeParrot's first commit is Apr 3; ListingLift's last is Apr 6. Simpler and more relatable: the next thing got more interesting. Which is true?

## Facts I couldn't check

| # | Claim | Where |
|---|---|---|
| 4 | **SoccerRatings is in real use by an actual league.** Build says production-intent; nothing proves a season ran on it. "Built for" and "used by" are different claims. | applications/03 |
| 5 | **CaptureRapture's pre-git history.** First commit reads `initial: existing CaptureRapture codebase`. How much predates Mar 26, and did you build that part? The 8,709-line count includes it. | applications/04 |
| 6 | **Job Hunt OS internals.** Everything comes from the SYSTEM README. The live repo (`FlipYaFaReal/jobhunt`) wasn't read — operating spec, ledger, trends, and any conversion numbers are unverified. **Is it still in TEST mode?** | systems/02 |
| 7 | **Gmail Cleanup was actually run** against your live account. `cleanup.log` exists, which suggests yes. | applications/07 |
| 8 | **Repo privacy.** Several linked project repos are under the `FlipYaFaReal` account. If the site links them, confirm each is intended to be public and has been checked for committed credentials before publishing the link. | README, JSON |

## Everything from the chat-history source

**The entire tier-2 set below has no on-disk artifacts on this machine:** the vendor-risk automation, the local inference stack, and the team infrastructure evaluation — plus the diagnostic story in judgment calls.

I searched for traces and found none: no AnythingLLM scripts, no agent-skill package, no policy documents, no infrastructure configs. That doesn't mean they don't exist — they're plausibly on another machine, in another account, or only in chat. But **before any of it goes on a public site, locate the actual artifacts.** If a hiring manager asks "can I see the agent skill you built?", the answer needs to be yes.

**The one exception, and it's a big one:** the multi-agent workflow system is **fully corroborated on disk.** Five repos carry `.workflow/` directories with decision records, work items, session logs, and state files. That one you can assert without hedging — within the limits below.

## The one place I'd trim a claim

The multi-agent workflow's on-disk evidence proves the system **ran and produced structured artifacts across five projects.** It does *not* prove every gate fired every time: TradeParrot's `.workflow/` is empty of records, and no project shows work items physically moving through `review/` and `qa/` directories — only `backlog/`, with progress in the state file's counters.

Defensible claim: *"a documented multi-role workflow with decision records and work-item tracking, applied across five projects."* That's plenty. Don't inflate it into a fully audited pipeline; the real version is strong enough and survives someone opening the folder.

---

# Market assessments — all mine, all arguable

Every `market_assessment` block is my analysis, not research you did. Named competitors (BoxBrownie, Styldod, VirtualStagingAI, Scribe, Tango, iorad, Teal, Simplify, Huntr) come from model knowledge and were **not verified against current conditions.**

Two are load-bearing enough to check before repeating:

- **CaptureRapture is the best commercial opportunity of the eight,** because client-side-only operation is a real enterprise wedge. Be ready for "have you talked to an L&D buyer?" The answer is no.
- **HouseHelper's market is too thin to build.** Reasonable read, not researched — and note it can't be why it stopped, since it was already built.

---

# Safe to use without checking

Commit counts, line counts, file counts, dates, active-day counts, branch names, commit messages, stack lists, document counts and filenames, `.workflow/` contents, and every direct quotation from your PRDs, design specs, and the Job Hunt OS README. All read from disk 2026-08-22.

**One number to state precisely:** *88 spec-and-plan documents* counts everything under a `docs/` folder across all projects, including HouseHelper's 10 uncommitted ones. Committed only: **78**.
