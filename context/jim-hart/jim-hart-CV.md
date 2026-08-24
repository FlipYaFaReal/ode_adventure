*Context document for Jim Hart. Public copy — contact details withheld.*

# Jim Hart — CV

**Software Engineer · AI Engineer · Azure Architect · Team Builder**
Charleston County, South Carolina

Contact details are withheld from this public repository. Held locally.

---

## Summary

Twenty-six years building software, the last thirteen at one company across the full arc from senior IC to
Director of Engineering and back to senior IC by choice. Currently Senior Staff Engineer working on AI
systems — ontologies, knowledge graphs, vector databases and prompt chaining — after leading a five-team,
16-engineer organisation through an on-premises to cloud SaaS transformation.

AI work at Omatic spans shipped agents, product strategy and team tooling. Outside work: 34 personal
projects, 1,389 commits and 164,418 lines across TypeScript, C#, JavaScript, SQL,
Python and Vue, built with Claude Code and other AI tooling. Full record in `jim-hart-portfolio.json`.

Provenance: career record `quoted` from LinkedIn; project figures `verified` from disk.

---

## Experience

### Omatic · Jan 2013 – present · 13 yrs 5 mos
*Charleston, South Carolina*

**Senior Staff Engineer** — Jan 2024 – present *(2 yrs 8 mos)* · Remote

- Applying AI, ontologies, knowledge graphs, vector databases and prompt chaining to build Omatic's future
  solutions.
- **Integration Onboarding Agent** — walks a new tenant through a structured conversation and produces
  enough context to auto-generate their integration mappings, removing the consultant from the call.
  Python, DSPy, FastAPI, Azure. Built to a documented mission: no fabrication, defer to the consultant,
  privacy on sample data.
- **Production Support Investigation Agent** — investigates production bugs across a distributed
  microservice system, traces root cause through service and schema documentation, and writes findings
  back into a living knowledge base so each investigation makes the next faster.
- **Integration Authoring Copilot** — strategic brief on how agentic tooling changes who builds
  integrations, with a 47-story, 7-epic engineering breakdown and an end-to-end technical trace.
- Platform worked agent-first: 37 repositories carrying agent instructions, 13 with committed
  configuration, and architecture documentation authored for agent consumption.
- **ai-agent-toolkit** — generalised a personal Claude Code workflow into an installable plugin marketplace
  for the team.
- Technical leadership on multi-year, cross-cutting projects.
- Established and grew a new team to improve the company's systems-thinking and drive customer outcomes.

**Director of Engineering** — May 2019 – present *(7 yrs 4 mos)*

- Led an engineering group of five teams: 16 FTE engineers, 6 nearshore engineers and 2 offshore teams.
- Grew the organisation 3x over three years.
- Led the transformation of products and teams into the cloud — on-premises software to a cloud-based,
  distributed-architecture SaaS product.

**Senior Software Engineer** — Apr 2013 – May 2019 *(6 yrs 2 mos)*

- Built integration solutions for fundraising, accounting and donor management software serving non-profit
  organisations.

### Blackbaud · Dec 2007 – Apr 2013 · 5 yrs 5 mos
**Senior Software Engineer**

- Custom software solutions across The Raiser's Edge, The Financial Edge, NetCommunity, BBEC and Endowment
  Manager.

### NovaStar Financial · Sep 2003 – Oct 2007 · 4 yrs 2 mos
**Software Engineer**

- Collateral management accounting software.

### Abacus Communications · Jun 2000 – Sep 2003 · 3 yrs 4 mos
*Virginia Beach, Virginia*
**Software Engineer**

- Custom call-centre applications for inbound and outbound operators.

---

## Technical

**Languages** TypeScript · C# · JavaScript · SQL · Python · Java · Vue
**Backend** .NET 8/9/10 Web API · Entity Framework Core · PostgreSQL · vertical-slice architecture
**Frontend** React 18/19 · Vite · Tailwind CSS · React Router · Next.js · Electron · Quasar
**Cloud & CI** Azure App Service · Azure Static Web Apps · Azure Functions · Azure Blob Storage ·
GitHub Actions · Clerk · Stripe
**AI** Claude Code · Azure OpenAI · knowledge graphs · ontologies · vector databases · prompt chaining ·
agent orchestration · local inference (faster-whisper, CUDA)
**Testing** xUnit · Vitest · hurl · node:test

---

## Selected personal work

Full detail in `jim-hart-portfolio.json`; narrative case studies to follow.

**Waterdeep — AI Software Factory.** A system prompt turning Claude into the orchestrator of an autonomous
software factory: a raw product idea forced through phased delivery with a panel of specialised expert
agents, ambiguity resolved through the right expert before proceeding, everything tracked in an on-disk
kanban. 36 markdown documents against 1,180 lines of code.

**CampfireCrm.** 361 commits, 33,297 lines, 55 spec documents, still active. Full-stack CRM — React 18 +
TypeScript + Vite against a .NET Minimal API on PostgreSQL, Clerk auth with automatic JWT injection, split
CI/CD pipelines deploying API and web app independently.

**AiVideoLab → AiVideoLab Studio.** A complete architectural migration: local-first Electron desktop application
ported to a React SPA on Azure Static Web Apps with a managed Functions API, workspace content in Blob
Storage and access gated by Clerk. 674 commits across the cluster.

**HartStack CLI.** One command scaffolds a production-ready full-stack SaaS project from a Handlebars
template tree; a second runs a six-step Azure provisioning flow.

**PromptForge Studio.** Structured world-building with enforced canonical phrasing, so generated media stays
consistent across clips — repeatable, reviewable and auditable prompt generation.

**VideoTranscripts.** Local batch transcription with CUDA/CPU auto-detection and voice-activity detection,
emitting text and timestamped subtitles, with per-file error isolation.
