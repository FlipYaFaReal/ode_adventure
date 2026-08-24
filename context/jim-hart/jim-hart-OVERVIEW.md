*Context document for Jim Hart. Public copy — see the redaction note at the foot of this file.*

# Overview — Jim Hart

Source material for a team artifact supporting a **Bring Your Own Engineering Team** application to
[Ode with Anthropic](https://jobs.ashbyhq.com/odewithanthropic/5e655487-e0f9-4471-96fd-355b1f5e0185), and for
Jim's individual application to
[Staff Software Engineer](https://jobs.ashbyhq.com/odewithanthropic/d1218507-6d99-4cfb-b7d5-cd34a633cda2).

**Team:** Jim Hart (engineer) · Paul McClintock (product) · Darryl (design — role mapping unresolved, see
`jim-hart-DEFERRED.md`).

---

## What's here

| File | What it is |
|---|---|
| `jim-hart-portfolio.json` | Structured data across five tiers. **Machine-readable source of truth.** Every metric mined from disk. |
| `jim-hart-CV.md` | Career record, 2000–present |
| `jim-hart-VERIFY.md` | Discrepancies found, inferred claims, redactions. **Read before publishing.** |
| `jim-hart-DEFERRED.md` | Parked items and open questions |
| `jim-hart-source-project-portfolio.md` | Jim's own write-up of the projects. Source of every tagline. |
| `jim-hart-source-linkedin.md` | Jim's LinkedIn export. Source of the career record. |
| *(work portfolio)* | `AI_PORTFOLIO.md`, compiled on Jim's work machine. Source of the professional and practice tiers. **Held locally — deliberately not committed.** |
| `jim-hart-mine.py` | The mining script. Re-run it to regenerate every metric. |
| `case-studies/` | Narrative write-ups. **Empty — next pass.** |

## How the numbers were produced

`C:\Code` was scanned on 2026-08-24: 45 directories, of which 34 are real projects. Only non-blank lines in
hand-written source files are counted. Build and publish output, coverage reports, minified bundles,
lockfiles, EF migrations and agent worktrees are excluded.

Four corrections were applied during mining. All four moved a number that had already been written down:

0. **Commits counted across every ref.** `git log --all` includes unmerged and dependabot
   branches — CampfireCrm has **361 commits on `main` and 524 across all refs**, more than twenty of the
   difference being dependabot. Counting is now limited to what is reachable from the checked-out branch,
   which also stops the totals drifting whenever refs are pruned.
1. **Vendored third-party source.** `CampfireCrm` contains full clones of `Npgsql` and `efcore.pg`. A naive
   line count credited Jim with 247,456 lines there; the real figure is 33,297. Every nested `.git` below a
   project root is now checked for authorship — third-party clones are dropped whole, Jim's own
   sub-repositories are kept.
2. **Electron build output.** Four projects shipped a `release/` directory containing Chromium's
   `LICENSES.chromium.html`, a single file of 164,000–270,000 lines. `ClipRenamer` alone dropped from 224,018
   lines to 1,272.

A third pass excluded directories that are not Jim's projects at all — `npgsql-temp` is another clone of
the Npgsql library, at 87,770 lines.

The first pass returned 1,132,962 lines. **The honest figure is 164,418.** That gap is the reason this file
documents the method.

---

## Headline

**34 projects · 1,389 commits · 164,418 lines · 198 spec and plan documents · 71 active days**
**TypeScript · C# · JavaScript · SQL · Python · Vue · Java**

| Year | Active days |
|---|---|
| 2024 | 3 |
| 2025 | 7 |
| 2026 | 61 |

Provenance: `verified`.

## The tiers

Five tiers of personal work, mined and verified. Two tiers of work-machine projects that **could not be verified from this machine** and are held to a different standard — see the note below them.

### Tier 1 — Applications (12)
Products with a user, a data model and a deployment story.

| Project | Domain | Commits | LOC | Note |
|---|---|---|---|---|
| CampfireCrm | Events / CRM | 361 | 33,297 | Largest and still active. 55 spec documents. |
| AiVideoLab Films | Media production | 299 | 28,575 | Still active. |
| AiVideoLab Studio | Media production | 175 | 20,577 | The desktop→cloud port. |
| DoraTrack | Engineering analytics | — | 18,770 | No root repo; two of Jim's own sub-repos. |
| Talamar's Forgotten Tales | Interactive fiction | 191 | 13,664 | Stories are pure data. |
| AiVideoLab | Media production | 164 | 11,499 | The Electron original. |
| SwipeForCause | Nonprofit marketplace | 64 | 8,736 | Five days. |
| CombatHelper | Games / utility | 19 | 7,483 | Built with Lovable. |
| Huntr · ILMOSH · MerryPicks · AiVideoLab Films Launch | — | — | — | Smaller builds. |

### Tier 2 — Systems (4)
Repeatable machinery. **More relevant to this role than most of the applications.**

1. **Waterdeep — AI Software Factory.** *The anchor.* A system prompt turning Claude into the orchestrator of
   a phased delivery process with a panel of specialised expert agents, tracked in an on-disk kanban
   (`WORKBOARD.md`, `DECISIONS.md`, `REQUIREMENTS.md`, `ARCHITECTURE.md`). 36 markdown documents against
   1,180 lines of code — the ratio is the point.
2. **HartStack CLI.** One command scaffolds a full-stack SaaS project; a second runs a six-step Azure
   provisioning flow.
3. **Foundation.** Vertical-slice .NET template — each feature owns its controller, handlers and DTOs.
4. **jimhart.dev.** Built from a written design spec, behind a CI gate.

### Tier 3 — Agents (2)
**Navi** (orchestration REPL) and **Jexi** (Azure OpenAI, deliberately framework-free). Both small. Honest
description: experiments, not products.

### Tier 4 — Tools (8) · Tier 5 — Experiments (7)
Desktop and media utilities; small self-contained builds. **PromptForge Studio** is the one worth surfacing:
it exists to defeat prompt drift through enforced canonical phrasing, which is an evals problem wearing a
media-production costume.

---

## The work machine — professional (7) and practice (6)

**These 13 projects are on Jim's work computer. Nothing here was scanned, so there are no commit or line
counts and none of it contributes to the headline numbers above.** Provenance is `quoted` from a document
Jim compiled there. Descriptions are abstracted for this public repository; what was removed is listed in
`VERIFY.md`.

**They are also, collectively, the most relevant material in the folder.**

### Professional — AI built for the employer
1. **Lingo — Integration Brief.** An AI onboarding agent that walks a new tenant through a structured
   conversation and produces enough context to auto-generate their integration formulas, without a
   consultant on the call. A Step framework over a subagent contract, with session management, a label
   cache, and a tool layer reading live platform metadata — and a documented mission constraining every
   technical decision: *no fabrication, defer to the consultant, privacy on sample data.* **The closest
   thing in either portfolio to what Ode actually does.**
2. **AI Formula Copilot.** Strategy and plan, not code: a brief on how agentic tooling changes who builds
   integrations, plus a 47-story, 7-epic breakdown and an end-to-end trace of the edit flow to ground it.
   Frame the problem, argue the position, hand over something executable — that *is* the forward-deployed
   job.
3. **Tier 3 Support Agent.** Investigates production bugs across a distributed microservice system, then
   **writes what it learned back into a living knowledge base** so the next investigation starts further
   along.
4. **AI-Assisted Platform Engineering.** 37 repositories carrying a `CLAUDE.md`; 13 with committed
   `.claude/` configuration; architecture documentation written so agents can navigate a system too large
   to hold in one head. Eight-plus parallel feature worktrees at once.
5. **Milvus Contact Lookup** · **Omatic.PromptChain** · **Candlekeep** — vector matching as an alternative
   to rule-based dedup, prompt chains as declarative config, and RDF/SPARQL ontology work.

### Practice — tooling built for himself and the team
**Claude HQ** (Electron app for managing a Claude Code install) · **ai-agent-toolkit** (the team's shared
plugin marketplace) · **Team Process Toolkit** (a CLI drivable by human *or* agent) · **The Green Dragon**
(agents as pixel-art adventurers, on hexagonal architecture with an event-sourced reducer) · **Personal
Claude Code environment** (11 skills, 65 curated memories, 15 project contexts) · **Navi — Personal
Development Vault** (an Obsidian PARA vault the agent maintains).

> **Name collision:** this Navi is not the Navi in the agents tier. Different project, different machine,
> same name. Do not merge them.

---

## The argument

Not *"here are 35 projects."* Volume is the least interesting thing in the record.

**1. He went back to the code on purpose.** Director of Engineering — five teams, 16 FTE engineers, 3x growth
over three years, an on-prem-to-SaaS cloud transformation — then took a Senior Staff Engineer seat and now
works in ontologies, knowledge graphs, vector databases and prompt chaining. The Staff Software Engineer JD
opens by describing exactly this person: *"former engineering leaders (IC or EM) or founders who are
comfortable owning end-to-end technical outcomes but specifically want to continue being impactful as
individual contributors and spend more time in the code."* He did not have to be recruited into that
position; he was already standing in it.

**2. Context is engineered, not scratch.** 198 spec and plan documents across 34 personal projects — and
at work, 37 repositories carrying agent instructions, 13 with committed configuration, 11 custom skills and
65 curated memories across 15 project contexts. Ode says they *"curate durable data sets"* and ship things
that *"keep working long after we've handed it over."* `ai-agent-toolkit` is that exact move: a personal
workflow deliberately generalised into installable team infrastructure so nobody hand-copies files.
Separately, the spec-to-code ratio in the personal work says the same thing. Waterdeep has 36
markdown files and 1,180 lines of code. This is someone who writes the requirement down before writing the
code — which is Ode's stated engineering philosophy, *"applying standard software engineering discipline to
the non-deterministic world of frontier AI."*

**3. He ports rather than restarts.** AiVideoLab is the only complete architectural migration in the record: an
Electron desktop app taken to a React SPA on Azure Static Web Apps with a managed Functions API, Blob
Storage for workspace content and Clerk at the gate — with the desktop original still in the repo. Most
portfolios show a graveyard of restarts. This shows one system carried across a boundary.

**4. The same instinct shows up in three places.** Waterdeep (personal), Lingo's Step-and-subagent
architecture (work), and The Green Dragon's event-sourced agent visualisation (practice) are all attempts
to make agent behaviour legible and governable rather than trusting it. That is a consistent engineering
position, arrived at repeatedly, not a one-off.

**5. Jim and Paul independently built the same thing.** Waterdeep and Paul's Multi-Agent Software Development
Workflow are both simulated product organisations that force an idea through a requirements panel, an
architecture phase and a reviewed implementation loop, tracked in on-disk state. Neither knew the other was
building it. **For a Bring Your Own Team application this is the strongest single fact available** — it is
evidence of shared engineering values that no interview panel could have coached.

---

## BRIEF FOR THE SESSION BUILDING THE ARTIFACT

### What Ode actually asked for
- BYOT is scoped to *"an existing team of 2–5 engineers."* Team members are expected to map to Software
  Engineer, Senior/Staff Software Engineer or Forward Deployed PM. **There is no designer role on Ode's
  board** — all 12 open postings checked 2026-08-24.
- Their proof case is Fabius: a YC team with three years of shipping together. The quoted line is *"the team
  itself was an asset."*
- Values: **Overdeliver · Overuse AI · Over-engineer the culture.**

### The load-bearing claim
Not "three impressive people." **"We are already a working unit, and here is the evidence."** Everything else
is supporting material. This is also where the application is most exposed — see `DEFERRED.md`.

### The location problem
The BYOT posting lists San Francisco and New York only, 4 days in-person. The team needs Raleigh-Durham or
remote. **The artifact has to be good enough to make location negotiable.** Do not bury this; addressing it
directly is more credible than hoping nobody checks. Paul's Operation Teleport — a 30-day relocation run as
a delivery engagement — is directly relevant evidence here.

### Hard rules
- **Never invent a metric.** No users, revenue or downloads exist for any of these projects.
- **Respect `provenance`.** `verified` (git/filesystem) · `quoted` (Jim's own documents) · `drafted` (Claude's
  analysis) · `reported` (recollection). Never state `drafted` or `reported` as established fact.
- **Use 164,418, never the raw scan.** If a number cannot be traced to `portfolio.json`, it does not ship.
- **Tier 3 is thin and should be described as thin.** Two small experiments. Paul's agents tier is empty;
  overselling Jim's does not fix that.
- **AiVideoLab is described by its engineering facts only** — Electron→Azure port, Clerk, Blob Storage, the
  design-handoff canvases. No subject matter.
- **DoraTrack, PromptForge Studio, MusicSorter, Waterdeep and Foundation have no git repository.** Their
  metrics are filesystem-only and must be labelled that way.
- **The 13 work-machine projects have no metrics at all** and must never be given any. They are `quoted`,
  not `verified`, and they are excluded from every headline number.
- **The work descriptions are already abstracted.** Do not reintroduce internal business figures, the
  competitive-positioning argument, named customer connectors, or internal service names — even if Jim
  mentions them in conversation. `VERIFY.md` lists what was removed and why.

---

## Note on this copy

This is the **public** copy, published to `github.com/FlipYaFaReal/ode_adventure` under `context/jim-hart/`.

Two redactions are applied:

1. `VirtuousSync-JimHart` is withheld as employer-adjacent and excluded from every total.
2. The AiVideoLab cluster is described by its engineering facts only, with no subject matter.

Both are recorded in `jim-hart-VERIFY.md` rather than silently omitted.
