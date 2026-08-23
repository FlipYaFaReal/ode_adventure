# Operation Teleport

**Apr 17 – May 15, 2026 · Four planning documents · One custom Claude skill · No code**
*A 30-day relocation run as a delivery engagement*

---

## Why this is in a software portfolio

Because it is the closest thing here to the actual shape of a forward-deployed engagement, and it contains no software at all.

An ambiguous real-world situation with hard external deadlines and a real budget, framed into workstreams. Alternatives evaluated and rejected on the record. Custom tooling built for the one workstream that needed it. A documented replan when the assumptions moved. Artifacts left behind in a form the operator could keep using.

That sequence is the job description.

## The situation

From the April 17 design document: a house listed and unfurnished; the family living in a rental to keep it show-ready; a slow market making double carrying costs imprudent; a lease ending in roughly thirty days; about $3,000 of budget; furniture to dispose of rather than move; and a requirement that the house **stay actively listed and show-ready** after moving back in.

That last constraint is the one that makes this hard. It is not "move house." It is "move back into a house that has to keep looking like nobody lives in it."

## The approach, with alternatives on the record

**Chosen: Sell-First, Move-Last.** List and sell from the apartment while still living there, then move only keepers at the end, minimizing double-handling. Fallback to a bulk buyer if selling stalled by day ten.

Two alternatives were considered and **rejected in writing, each with its reason**:

- *Move-first, sort-at-the-house* — rejected because the garage becomes unusable and showings see clutter, plus double-handling.
- *Estate sale kickoff* — rejected because it exceeded the sell-big-items-only scope and commissions did not justify the volume.

Four workstreams: **Dispose and Store · Acquire · Move · Stage.**

Writing down the options you did not take, with the reason, is the same habit that produced the `.workflow/` decision records in the software projects. It shows up here in a domain with no code in it, which is the strongest evidence that it is a genuine reflex rather than a template.

## The replan — the best artifact in this project

On April 29, twelve days in, **rev3** was filed. It supersedes rev2 and opens by stating why, which is the part most replans skip.

Two assumptions had broken:

1. **The leather sofa refurbishment "doesn't pencil"** at $700–900. Those pieces went to storage; the family room got sourced fresh instead.
2. **Move-in was pulled forward ten days** — so that *"sourcing decisions happen in context, with the rooms in front of you, not abstractly from the apartment."*

That second one is a real insight about decision quality, not a schedule tweak. Choosing furniture for a room you are standing in is a different task from choosing it from a spreadsheet in another building, and recognizing that mid-project is worth more than the schedule change it produced.

The single big move became two waves: a **functional baseline** on May 5, defined concretely as *sleepable, cookable, workable, and pet-safe by Tuesday night*, with "visibly mid-move is fine" written in as an explicit acceptance standard. Then a separate cleanout week ending in the hard lease deadline of May 15.

And rev2 was **frozen in place rather than deleted**, marked *"do not execute from it."* Superseded plans get archived, not overwritten.

## The custom tooling

`marketplace-furniture-hunt` — a Claude skill covering four concurrent furnishing hunts (bedroom, family room, kitchen, office).

It encodes a **locked constraint set**: a 25-mile radius expanding to 40 only after the earlier search tiers dry up; no firm price ceiling, but flag value at any price. And an **auto-skip list** of styles and brands never worth surfacing, so the agent does not waste the operator's attention on things it already knows are wrong.

Two modes: *generate* tiered search vocabularies per room, or *evaluate* a pasted listing. The evaluation mode grades on **style, quality, and price**, and returns a verdict on whether a claimed brand is credible — a "is this really an Arhaus?" check.

And it persists to Notion rather than to chat, with an explicit instruction not to dump forty links into a conversation. That is a small thing that reveals real usage: someone who had actually used the tool wrote the rule about not flooding the chat.

## Another rubric

Style grade, quality grade, price grade, overall verdict, brand claim versus brand verdict. That is the fourth distinct scoring rubric in this portfolio, after trade grades, job-fit scores, and the thirteen soccer categories.

The pattern is consistent enough to be the strongest single claim available: **whenever the work requires an AI to make judgment calls, the first thing built is the criteria the judgment will be made against.**

## What was left behind

- Four design and plan documents, including a full superseding replan
- A custom Claude skill with locked constraints and a persistence target
- Inventory and marketplace-finds tracking, later frozen with a note recording that Notion had become the source of truth
- Generated HTML dashboards, a marketplace-finds view, and a wall calendar, with local serve scripts
- A PDF plan for offline use

The frozen CSVs are worth noting. Rather than deleting them when the system moved to Notion, they were left in place with a header comment recording the handover date and the new source of truth. Small discipline, and the kind that makes a system survivable by someone other than its author.

## The lesson

The method is not about software. It survived being pointed at a moving van.

For a forward-deployed role, that is the relevant proof. The client's problem will not arrive shaped like a Next.js app, and the person who can only run the method when the deliverable is code is a narrower hire than the person who can run it on a relocation, a compliance review, or a hiring process.

---

> **Note on scope.** This project involved the author's family and personal circumstances. The write-up above deliberately covers only the operational and methodological content. Personal and family details in the source documents are omitted and should stay omitted.
