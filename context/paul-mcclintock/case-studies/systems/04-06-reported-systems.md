# Three systems from the chat-history source

**Vendor-risk automation · Local inference stack · Team AI infrastructure evaluation**

---

> **Provenance warning.** Unlike everything else in this portfolio, these three have **no on-disk artifacts on this machine**. They come from `ai-journey-portfolio-source_1.md`, which the author reconstructed from chat history in August 2026. The detail is specific and internally consistent, which is a good sign — but it is recollection, not record. Before any of this goes on a public site, locate the actual scripts, packages, and documents. See `VERIFY.md`.

---

## 4 · Vendor-Risk Document-Comparison Automation
*May 2026*

### The problem
A baseline set of documents needed systematic comparison against an update set, one pair at a time, repeatably, for vendor risk assessment work.

### The diagnosis — this is the story
The platform's default similarity-based retrieval was **the wrong primitive for the task.** It pulls fragments from each document, so the model ends up comparing chunks rather than whole documents. The fidelity loss is invisible unless you go looking for it: you get an answer, it reads fine, and it is quietly built on a partial view of both documents.

Recognizing that *before* building is the entire value of this item. The obvious move is to point the RAG tool at the documents and accept what comes back.

### The build, in two stages

**Stage one — a script.** Python against the platform's REST API. Unpin the workspace for a clean slate. Pin each document pair, which bypasses vector search and forces deterministic full-document context. Send a structured comparison prompt returning JSON with `added` / `removed` / `changed` / `unchanged` sections plus risk flags. Write results incrementally to CSV so a long batch that dies partway through does not lose everything.

**Stage two — a product.** The same capability repackaged as a native agent skill: a three-file distribution with a manifest declaring setup arguments, a Node handler using progress streaming so the user can see the batch advancing, and a README with platform-specific install paths. Accepts a CSV path or inline JSON. Caps batch size. Cleans up pins after each run.

### Why it matters
Two things, and the second is rarer.

**Diagnosis before construction.** The build starts by rejecting the default tool for a structural reason, not a preference.

**It didn't stay a script.** Turning a personal fix into an installable package — manifest, progress output, install docs, cleanup — is what converts one person's solution into a team capability. A compliance review that used to queue behind an engineer became something a non-technical teammate could trigger themselves. That instinct is the difference between being fast and being scalable, and it is the single most transferable behaviour in this whole portfolio for a services role.

---

## 5 · Local Inference Stack
*April – May 2026*

### The setup
Two rigs already owned: an i9-13900KF with an RTX 4070, and a Xeon Gold 6242R with an RTX A4000, 96GB of RAM, and 20TB of storage.

### The design
A phased roadmap across Ollama, Open WebUI, ComfyUI, Tailscale, and Continue.dev, with a **single shared network model store** so weights are not duplicated across machines.

### Costed to the electricity bill

| Line | Figure |
|---|---|
| Hardware | $0 — both rigs already owned |
| Software | $0 — entirely open source |
| Build time | ~3 weeks of evenings; phase 1 (3 days) yields a working LLM server |
| Model weights | 200–300 GB against 20 TB available |
| Electricity | ~$15–30/month |

### Success criteria as pass/fail checks, not aspirations
- Sub-two-second first-token latency to Open WebUI from any Tailscale device
- A local coder model handling editor autocomplete without touching cloud APIs for routine work
- End-to-end local image-to-video generation
- Both rigs reading from one model share
- The Xeon surviving a reboot with the LLM server auto-starting

That last one is the tell of someone who has actually operated infrastructure. "Survives a reboot unattended" is the criterion people learn the hard way.

### The strategic layer
A deliberate split: **Claude Code for hard problems, local models for volume work** — boilerplate, refactors, test generation. Plus a documented path for the same ComfyUI pipelines to become production image processors for ListingLift, replacing or supplementing paid Replicate API calls.

That is the part worth drawing out. It is not a home lab for its own sake; there is a written route from personal infrastructure to production cost reduction on a real project.

---

## 6 · Team AI Infrastructure Evaluation
*May 2026*

### The question
Could a self-hosted AI assistant platform serve a 24-person work team — team-wide retrieval over shared documents plus agentic workflows — hosted at home for privacy?

### The work
Evaluated remote access approaches (Tailscale, Cloudflare Tunnel, WireGuard, port forwarding) with a recommendation on the ease-versus-security tradeoff. Established that no self-hosted retrieval tool had native Microsoft Teams integration, then scoped the two viable build paths: a Power Automate flow against the platform API, or a proper Teams bot via Bot Framework — which would require Cloudflare Tunnel to expose a Microsoft-reachable endpoint. Compared Onyx for permission-aware team retrieval with multi-user SSO against n8n for agentic workflows, against the existing Microsoft 365, SharePoint, Teams, Monday.com, and Notion stack.

That is a real evaluation. The Teams integration finding in particular is the kind of thing that kills a project three weeks in if nobody checks it first.

### The decision
Hosting work-team data on a personal home server raised security, policy, and reliability concerns. The evaluation **surfaced them rather than routing around them**, and split the two cases: the home stack for personal and non-sensitive experimentation, a company-sanctioned hosted instance for actual team use.

### Why it belongs
Standing up a home lab is common. Concluding that your own home lab should not hold the company's data — *while wearing the security officer hat, and after already doing the integration work* — is the harder and much less fun call.

The sunk cost was real and the conclusion went against it anyway. That is the behaviour a services client needs from someone they have handed access to, and it is not something you can claim credibly without a story like this attached.
