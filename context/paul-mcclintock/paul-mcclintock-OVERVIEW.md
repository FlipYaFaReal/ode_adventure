*Context document for Paul McClintock. Public copy — see the redaction note at the foot of this file.*

# Portfolio — Building with AI

Source material for a personal portfolio web experience about Paul McClintock's personal AI work, Feb–Aug 2026.

**Primary audience:** the hiring manager for [Forward Deployed Product Manager @ Ode with Anthropic](https://jobs.ashbyhq.com/odewithanthropic/d93607e0-3e38-4a6f-a05e-f293d3f3bdf4) (SF/NY, $200–275K).

---

## What's here

| File | What it is |
|---|---|
| `paul-mcclintock-cover-letter.md` | Cover letter submitted for this role. **Read before the portfolio** — it makes the claims the portfolio substantiates. |
| `paul-mcclintock-CV.md` | CV submitted for this role |
| `paul-mcclintock-portfolio.json` | Structured data, organized into three tiers plus judgment calls. **Machine-readable source of truth.** |
| `case-studies/applications/` | Eight narrative write-ups of the software projects |
| `case-studies/systems/` | Six write-ups of the methodology, agents, and infrastructure |
| `case-studies/judgment/` | Two decisions where the reasoning is the artifact |
| `paul-mcclintock-VERIFY.md` | Inferred claims and unverified sources. Read before publishing. |
| `paul-mcclintock-DEFERRED.md` | Four parked items awaiting Paul's input. **Not part of the portfolio — skip entirely.** |

## Two sources, different reliability

1. **This machine** — git history and in-repo documents, read 2026-08-22. Covers all eight applications, Operation Teleport, the Job Hunt OS README, and the on-disk evidence for the multi-agent workflow.
2. **`paul-mcclintock-source-ai-journey.md`** — supplied by Paul, reconstructed from chat history. Sole source for the inference stack, vendor-risk automation, team infrastructure evaluation, and the diagnostic story. Tagged `provenance: reported`.

---

## The three tiers

### Tier 1 — Applications (8)
Software with a repository. Metrics are git-verifiable.

**422 commits · 86,036 lines · 88 spec documents · 36 active days · C#, TypeScript, Python, SQL**

| Project | Domain | Stack | Commits | LOC | Ended because |
|---|---|---|---|---|---|
| ListingLift | Real estate photo AI | .NET 8 + React | 172 | 26,396 | Outgrew its own PRD; stopped on the launch checklist |
| TradeParrot | Momentum trading | Python + Claude | 132 | 25,056 | Became an autonomous trading agent, then stopped dead |
| SoccerRatings | Youth sports evaluation | Next.js + Supabase | 57 | 10,115 | **Shipped.** Scope held. |
| CaptureRapture | Enterprise L&D | TS + browser ext | 12 | 8,709 | Never resourced. Best market of the eight. |
| CareerCalling | Job search | Next.js + Prisma | 1 | 7,313 | Parked — generation two of three |
| HouseHelper | House hunting | Next.js + Prisma | 1 | 4,432 | **Built, build passing, never run, never committed** |
| GeminiVibes | AI life assistant | Expo + tRPC | 37 | 3,630 | The toolchain ate it |
| Gmail Cleanup | Inbox automation | Python | 10 | 385 | **Finished.** |

### Tier 2 — Systems (6)
Repeatable machinery, methodology, and infrastructure. No single repo; commit counts don't apply. **Several of these are more relevant to this role than the applications are.**

1. **Multi-Agent Software Development Workflow** — a simulated product organization. *The anchor.*
2. **Job Hunt OS** — an autonomous agent, live, that commits its own audit log
3. **Operation Teleport** — a 30-day relocation run as a delivery engagement
4. **Vendor-Risk Automation** — diagnosed the wrong primitive, then productized the fix
5. **Local Inference Stack** — two owned rigs, costed to the electricity bill
6. **Team AI Infrastructure Evaluation** — scoped it, then argued against hosting it himself

### Tier 3 — Agents (0)
Empty for now. The intended occupant, **Kip**, is parked in `DEFERRED.md`. Leave the slot in the information architecture but **do not render an empty tier.**

### Plus — Judgment calls (2)
Declining to host team data at home · compressing an unfamiliar expert domain in a week.

### Parked — see `DEFERRED.md` (4)
Kip · a security risk assessment · a contract evaluation project · a POC built with Fable. **None of these render on the site.**

---

## The argument

Not *"here are eight apps I built with AI."* Weak, checkable, and everyone is making it.

**Two arcs run through this, and they're different claims.**

**Scope:** over seven months the work moved from *using* AI tools → *building* with agentic workflows → *architecting* AI systems for other people, with governance judgment attached.

**Craft:** over the same period the individual builds got smaller, faster, and more finished. February's ListingLift ran 46 days past its own PRD and never launched. July's SoccerRatings shipped in two days with its non-goals intact.

Neither is the whole story. The scope arc without the craft arc is a tourist. The craft arc without the scope arc is a hobbyist.

### The seven themes

1. **He writes evaluation criteria for AI judgment in every domain he touches.** Trade grades A–F. Job fit across five dimensions, then rubric v2 with revised weights. Furniture style/quality/price with a brand verdict. Thirteen soccer categories with per-category anchor text. Photo critique feeding a second pass. *Five domains, same skill — and it maps exactly onto the JD's phrase about evaluation criteria for AI systems.*
2. **Irreversible actions get a gate, unprompted.** Gmail Cleanup's dry run. Job Hunt OS's `MODE: TEST` before it emails employers. The workflow's mandatory security review and capped review cycles. Nobody required any of it.
3. **The spec is the unit of work, not the commit.** 88 dated documents — and a machine that produced them.
4. **The discipline lagged the ambition.** Learned in public, in order.
5. **Knowing when to stop is the rarest thing here.** Both patterns are in the record.
6. **The best market got the least time.** CaptureRapture got one day; ListingLift got fifteen.
7. **Diagnosis before construction.** Reject the default retrieval primitive. Read the compression pattern. Gap-analyse before sending.

---

## BRIEF FOR THE SESSION BUILDING THE SITE

### Tone
Deliberately, unusually honest — most entries are framed around what went wrong or where something stopped. **Do not sand that off.** The self-awareness *is* the differentiator. Dry and specific beats enthusiastic: "it stops on the launch checklist" lands harder than "an ambitious journey."

The framing is someone who genuinely enjoys building, not a candidate performing rigor.

### Hard rules
- **Never invent a metric.** No users, revenue, or downloads exist.
- **Respect `provenance`.** `verified` (from git/files) · `quoted` (Paul's own docs) · `reported` (his chat-history reconstruction, unverified) · `drafted` (my analysis). Never state `reported` or `drafted` as established fact.
- **Nothing from `DEFERRED.md` goes on the site.** Four items are parked there, including the security policy work, which carries an unresolved confidentiality question.
- **HouseHelper was built, not abandoned at the PRD.** Git says 103 lines; disk says 4,432 with a passing build. Lead with the discrepancy.
- **ListingLift predates its own repo.** The MVP was scaffolded by an agent team on Feb 18–19; git was initialized Feb 20 *as an audit finding.*
- **CareerCalling is one squashed commit.** Present it by what it does.
- **Tier 3 is empty.** Keep the slot in the IA; don't render an empty section.

### Eight interaction concepts
Details in `web_experience_hooks`. The three strongest:

1. **The Org Chart That Isn't Real** — render the simulated product organization, then let the visitor open a real decision record it produced (CaptureRapture's DEC-001: three options weighed, video deferred to v2, *Participants: Product Manager, Lead Engineer, UX Designer, QA Lead*). The reveal is that none of them are people. **Lead with this.**
2. **Five Rubrics** — the five scoring systems side by side, with job-fit v1 next to v2 so the revision is visible.
3. **The Gate** — Gmail Cleanup's dry run and Job Hunt OS's `MODE: TEST`, five months apart, neither required.

Then: Why It Stopped · The Drift · Spec to Ship · Two Days · Range.

*Recommendation:* open on **The Org Chart That Isn't Real**, close on **Why It Stopped**. The first is the most surprising verifiable thing here; the second is the most honest.

---

## Also built with Claude (not case-studied)
A business continuity plan, a generated interior design plan, property comparison spreadsheets, and a Python media-library utility.



---

## Note on this copy

This is the **public** copy, published to `github.com/FlipYaFaReal/ode_adventure` under `context/paul-mcclintock/`,
generated by `sync-public.py` in the source repository.

Three redactions are applied on the way out:

1. The security risk assessment item in `paul-mcclintock-DEFERRED.md` is withheld.
2. Section 3 of `paul-mcclintock-source-ai-journey.md` is redacted.
3. Phone number and email are stripped from the CV and cover letter.

The unredacted working copy is held locally.
