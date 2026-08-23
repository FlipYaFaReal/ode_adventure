# Judgment calls

**Two items where the transferable evidence is the reasoning, not the artifact**

These are not projects and should not be presented as projects. They are decisions. The source document identifies them as the items that most resemble what a forward-deployed role actually is, and it is right.

> **Note:** a third item — the security risk assessment and Information Security Policy work — was parked on 2026-08-22 pending a confidentiality decision. It is preserved in `DEFERRED.md`, not deleted.

---

## 1 · Declining to host the team's data at home
*May 2026*

The full evaluation is written up in `systems/04-06-reported-systems.md`. It appears here separately because the transferable artifact is the decision, not the analysis.

Having scoped remote access approaches, established that no self-hosted retrieval tool had native Teams integration, mapped two viable build paths, and compared platforms against the existing Microsoft 365 stack — the conclusion was that a personal home server should not hold a 24-person team's data, and the two cases should be split: home stack for personal experimentation, company-sanctioned hosting for team use.

**The sunk cost was real and the conclusion went against it.** That is the whole point. Anyone can stand up a home lab; the harder call is deciding your own lab is the wrong place for someone else's data, especially after you have already done the work to make it possible.

For a role with access to client environments, this is the single most reassuring story in the portfolio — and it is reassuring precisely because nobody made him reach that conclusion.

---

## 2 · Compressing an unfamiliar expert domain in a week
*June – July 2026*

> **Framing.** Not an AI infrastructure project. Include it as *using AI to become genuinely useful in an unfamiliar expert domain, fast.* It is the most memorable item in the portfolio and the most human, which is exactly why it should be short and unembellished. Do not oversell it.

### The arc
Diagnosed active misfires (P0300, P0303, P0304) on a high-mileage engine, replaced plugs and coils, found oil in a spark plug well, and traced it to a leaking valve cover tube seal.

### The reasoning that mattered
A compression test returned **140 / 131 / 132 / 135 psi**. Uniformly low, but *consistent* — which rules out a localized head gasket breach between the two suspect cylinders. That is pattern analysis rather than parts-swapping, and it is structurally the same move as diagnosing the retrieval primitive before building the comparison tool: read the shape of the data, then decide what it eliminates.

In parallel, catalytic converter and oxygen sensor purchases were **deliberately deferred** until the misfire was confirmed resolved and readiness monitors completed — avoiding several hundred dollars of parts that might not have been needed. Expensive commitments after cheap information.

### The reframe
Quoted roughly $5,000 for a head gasket repair on a 250,000-mile engine, the analysis inverted the problem: the labor is nearly identical for a used engine swap, so the same money buys a reset engine rather than a rebuild around tired rings. Realistic market for the swap: $3,000–4,000, or $800–1,500 doing it yourself plus a hoist rental.

### The lateral move
Recognizing that a radiator replaced after a recent accident was a plausible root cause opened a different path entirely — preserve the parts as evidence, obtain a written shop diagnosis naming the cooling system, pursue the body shop's workmanship warranty, file a supplemental insurance claim, with small claims as backstop.

The technical diagnosis and the recovery path are two separate problems, and most people only work the first one.

### The technical bit
During the replacement search, VIN verification ran live against **NHTSA's free vPIC API** rather than paying for a report — confirming check digits to rule out tampering, and pulling recall campaigns, which surfaced **11 open items on one candidate including Takata airbag inflators.** Undercarriage photos on another candidate were assessed well enough to identify rot-through at body and frame seams, and to walk away from the purchase.

### Why it belongs
It is the clearest demonstration in the set of the actual forward-deployed skill: land in a domain you do not know, get to useful judgment quickly, and know which decisions are worth spending money on and which are worth waiting on.

It is also the story an interviewer will remember a week later, which is not nothing.
