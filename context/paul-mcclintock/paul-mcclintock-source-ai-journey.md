# AI Journey — Stories, Wins, and Value Delivered

*Source material for the Ode portfolio site. Reconstructed from chat history, Feb–Aug 2026.*

---

## The arc, in one line

In roughly seven months, the work moved from *using* AI tools → *building* with agentic workflows → *architecting* AI systems for teams, with security and governance judgment attached. That progression is the story. The individual projects are evidence for it.

**Timeline spine:**

| Month | Milestone |
|---|---|
| Feb 2026 | ListingLift MVP scaffolded by an orchestrated agent team |
| Mar 2026 | Designed a full multi-agent software development workflow system |
| Apr 2026 | TradeParrot running in Claude Code; mobile remote-control workflow |
| Apr–May 2026 | Two-rig local inference stack designed end to end |
| May 2026 | VRA document-comparison automation; team self-hosting evaluation |
| Jun 2026 | SOC 2-aligned Information Security Policy authored from zero |
| Aug 2026 | Local AI media pipeline (music/video generation) |

---

## Flagship stories

### 1. Multi-agent software development workflow system
*March 2026 — the single most Ode-relevant artifact*

**The ask:** Build a system where an AI agent team takes a product idea and delivers shippable software, resolving its own ambiguities.

**What was built:** A Claude Code orchestration prompt defining a full simulated product organization:

- **Phase 1 — Requirements panel:** Product Manager, Lead Engineer, UX Designer, QA Lead → PRD, user stories, acceptance criteria
- **Phase 2 — Architecture:** Software Architect + Engineering Lead → ADRs, technical design, task breakdown with dependencies
- **Phase 3 — Implementation loop:** Engineer → Code Reviewer → Engineer revision → Security Reviewer → QA validation

Supporting machinery: a `.workflow/` directory with JSON state management, decision records for every resolved ambiguity, a work-item state machine (backlog → in-progress → review → qa → done), session logs for traceability, enforced test-first development, mandatory security review, and a rule that every line of code traces back to an acceptance criterion. Maximum review cycles with escalation, so it can't loop forever.

**Why it matters for Ode:** This is forward-deployed methodology, written down. It's a repeatable system for taking a client's idea to shipped software with AI doing the volume work and quality gates preventing the usual failure mode — plausible-looking code nobody validated.

---

### 2. Vendor risk assessment automation
*May 2026 — process automation with a compliance paper trail*

**The problem:** A baseline set of documents needed systematic comparison against an update set, one pair at a time, repeatably, for vendor risk assessment work.

**The diagnosis:** AnythingLLM's default similarity-based retrieval was the wrong primitive — it pulls fragments from each document, so the model compares chunks rather than whole documents. Fidelity loss invisible until you check.

**The build, in two stages:**

*Stage one* — a Python script against the AnythingLLM REST API that unpins the workspace for a clean slate, pins each document pair (bypassing vector search for deterministic full-document context), sends a structured comparison prompt returning JSON with `added` / `removed` / `changed` / `unchanged` sections plus risk flags, and writes results incrementally to CSV.

*Stage two* — productized as a native AnythingLLM agent skill: a three-file package with a `plugin.json` manifest declaring setup arguments, a `handler.js` Node implementation using `this.introspect()` for progress streaming and returning a markdown summary table, and a README with platform-specific install paths. Accepts CSV file path or inline JSON. Batch size safety cap. Pin cleanup after each run.

**Value delivered:** A manual, error-prone compliance review became a repeatable batch process with an audit trail — and one that non-technical teammates could trigger themselves rather than queueing behind an engineer.

---

### 3. [Redacted in the public copy]

*This section described client-confidential and employer-confidential security work. It is withheld from
this public repository pending a confidentiality decision. The unredacted document is held locally.*

---

### 4. Team AI infrastructure evaluation — and knowing where the line is
*May 2026 — the judgment story*

**The question:** Could a self-hosted AI assistant platform serve a 24-person work team? Team-wide RAG over shared docs plus agentic workflows, hosted at home for privacy.

**The work:** Evaluated remote access approaches (Tailscale, Cloudflare Tunnel, WireGuard, port forwarding) with a recommendation on ease-versus-security tradeoffs. Established that no self-hosted RAG tool has native Microsoft Teams integration, and scoped two viable build paths — a Power Automate flow against the platform API, or a proper Teams bot via Bot Framework, with Cloudflare Tunnel required for Microsoft-reachable endpoints. Compared Onyx for permission-aware team RAG with multi-user SSO against n8n for agentic workflows given the existing M365 / SharePoint / Teams / Monday.com / Notion stack.

**The decision that matters:** Hosting work-team data on a personal home server raised legitimate security, policy, and reliability concerns. The resolution split the two cases — home stack for personal and non-sensitive experimentation, company-sanctioned hosted instance for actual team use.

**Why it belongs in the portfolio:** Anyone can stand up a home lab. Recognizing when your own home lab shouldn't hold the company's data — while wearing the Security Officer hat — is the harder call. Consulting clients need people who make that call unprompted.

---

### 5. The Broosity local inference stack
*April–May 2026 — costed infrastructure design*

**Hardware:** Two rigs already owned — an i9-13900KF / RTX 4070 workstation and a Xeon Gold 6242R / RTX A4000 with 96GB RAM and 20TB storage.

**The design:** A phased roadmap across Ollama, Open WebUI, ComfyUI, Tailscale, and Continue.dev, with a single shared network model store so weights aren't duplicated across rigs.

**Costed honestly:**

| Line | Figure |
|---|---|
| Hardware | $0 — both rigs already owned |
| Software | $0 — entirely free / open source |
| Build time | ~3 weeks of evenings; Phase 1 (3 days) yields a working LLM server |
| Model weights | 200–300 GB against 20 TB available |
| Electricity | ~$15–30/month |

**Success criteria written as testable checkboxes** rather than vibes — sub-2-second first-token latency to Open WebUI from any Tailscale device; local coder model handling VS Code autocomplete without touching cloud APIs for routine work; end-to-end local image-to-video generation; both rigs reading from one model share; the Xeon surviving a reboot with the LLM server auto-starting.

**The strategic layer:** a deliberate split between Claude Code for hard problems (depth) and local models for volume work — boilerplate, refactors, test generation. Plus a path for the same ComfyUI pipelines to become production backend image processors for ListingLift, replacing or supplementing paid Replicate.com API calls.

**Value delivered:** A private, rate-limit-free inference environment at essentially zero marginal cost, with a documented route from personal infrastructure to production cost savings.

---

### 6. ListingLift — MVP built by an agent team
*February 2026*

An AI real estate photo enhancement product on React / C# / PostgreSQL with Replicate.com for the enhancement models. Scaffolded through an orchestrated Claude Code agent workflow starting with an architect agent, with Clerk authentication including JWKS endpoint configuration and JWT verification, and each agent required to report assumptions made and decisions deferred to a future sprint.

**The product decision worth naming:** the MVP was deliberately scoped to a *single* enhancement type rather than shipping all of them, with the rest pushed to v1.1. Scope discipline under an agentic build is the interesting part — it's easy to let agents sprawl.

---

### 7. TradeParrot — daily-driver agentic development
*April 2026*

A Claude Code project run with Remote Control enabled, allowing sessions to start locally with full filesystem, MCP server, and project configuration intact, then be steered from the mobile app. Small story, but it's proof of genuine daily agentic workflow rather than occasional experimentation — including keeping up with tooling changes as flags and features shifted underneath.

---

### 8. The Honda Element diagnostic saga
*June–July 2026 — the AI-as-expert-partner story*

Not an AI infrastructure project, but the clearest demonstration of using AI to compress an unfamiliar expert domain, and the most *human* story in the set.

**The diagnostic arc:** Identified a missing air intake resonator, then diagnosed active misfires (P0300 / P0303 / P0304) and replaced plugs and coils on cylinders 3 and 4. Found oil in the cylinder 4 spark plug well, traced to a leaking valve cover tube seal.

**The decision that saved real money:** A full compression test returned 140 / 131 / 132 / 135 psi. The reading — uniformly low but *consistent* — ruled out a localized head gasket breach between cylinders 3 and 4. Pattern analysis, not parts-swapping. In parallel, catalytic converter and O2 sensor purchases were deliberately deferred until the misfire was confirmed resolved and readiness monitors completed, avoiding several hundred dollars of parts that might not have been needed.

**The reframe:** When a shop quoted ~$5,000 for a head gasket repair on a 250,000-mile engine, the analysis flipped it — the labor is identical for a used engine swap, so the same money buys a reset engine instead of a rebuild around tired rings. Realistic market for that swap: $3,000–4,000, or $800–1,500 DIY plus a hoist rental.

**The lateral move:** Recognizing that a radiator replaced after a recent accident was a plausible root cause opened an entirely different path — preserving parts as evidence, obtaining a written shop diagnosis naming the cooling system, pursuing the body shop's workmanship warranty, filing a supplemental insurance claim, with NC small claims as backstop.

**The technical bit:** During the replacement-vehicle search, VIN verification was done live against NHTSA's free vPIC API rather than paying for a report — confirming check digits to rule out VIN tampering, and pulling recall campaigns that surfaced 11 open items on one candidate including Takata airbag inflators. Undercarriage photos on a 2006 candidate were assessed well enough to identify rot-through at body and frame seams and walk away from the purchase.

---

## Qualitative themes to draw out

These are the through-lines a hiring team will actually respond to:

**Diagnosis before construction.** The AnythingLLM story starts with recognizing that the default retrieval mechanism was structurally wrong for the task. The compression test story is the same move in a different domain. The pattern is refusing to build until the problem is correctly framed.

**Sequencing to avoid waste.** Deferring the catalytic converter until the misfire was confirmed fixed. Scoping ListingLift's MVP to one enhancement type. Splitting Claude Code for depth from local models for volume. Consistently ordering work so that expensive commitments come after cheap information.

**Productizing one's own tooling.** The VRA script didn't stay a script — it became an installable agent skill with a manifest, progress streaming, and a README so other people could run it. That instinct to turn a personal solution into a team capability is the difference between a strong individual contributor and someone who scales.

**Governance instinct under pressure.** Running a gap analysis against the existing policy *before* sending the new one. Declining to host team data on a personal server. Both cost time and neither was required.

**Honest cost accounting.** The local stack was costed to the electricity bill, with success criteria written as pass/fail checks rather than aspirations.

---

## Notes on curation

**Include:** items 1–7 above (item 3 redacted here), with #1 as the anchor. For a forward-deployed product role, the multi-agent workflow system, the VRA automation, and the ISP work are the three that most resemble what the job actually is — taking a messy client problem, framing it, building the thing, and leaving behind something the client can operate.

**Include with framing:** the Element story. It's not AI infrastructure, but it demonstrates domain compression, cost discipline, and multi-path problem solving — and it's memorable in a way the technical work isn't. Frame it as "using AI to become dangerous in an unfamiliar expert domain in a week."

**Omit:** any personal or relationship material, and anything touching health or family. It discloses information you're under no obligation to share and shifts the frame away from the work.

**Verify before publishing:** the dynamic HTML document built for evaluating Element candidates during the beach trip didn't surface in the searches run here. Worth locating separately — it's a good small artifact if you can find it.
