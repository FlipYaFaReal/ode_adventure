# CaptureRapture

**Mar 26, 2026 · 12 commits · 8,709 lines · 1 active day · TypeScript + browser extension**
*Status: working prototype, one day of development*

---

## The ask

Every company runs enterprise systems — ERP, CRM, HRIS — and every one of them needs training material that goes stale the moment the vendor ships a UI update. The way that material gets made is genuinely bad: someone writes documentation from memory, or takes screenshots one at a time and pastes them into Word. The result is incomplete, out of date, and hard to follow, and rebuilding it costs as much as the first pass.

The PRD names three people who feel this. The **Training Manager**, who owns onboarding and needs guides fast and current. The **Subject Matter Expert**, not especially technical, who wants to capture what they know before they leave. The **L&D team member**, curating a library that has to stay standardized and reusable.

## The product

A browser-based capture tool. Share a screen, window, or tab through `getDisplayMedia`. Take snapshots from the live feed on demand, stored in order with timestamps. Annotate them non-destructively on a canvas overlay — text labels, rectangles, arrows, freeform highlights, configurable color and stroke — with the original always preserved underneath. Assemble the snapshots into ordered steps, each with a title and description, drag to reorder, duplicate, delete. Export the whole guide as a single self-contained HTML file with every image base64-inlined and print-friendly CSS. Projects persist in IndexedDB. No account. No login. No server.

That last part is the whole thesis, and the PRD says so directly: because it runs entirely in the browser, it works against any system the user can already see — including authenticated enterprise applications — **without server infrastructure and without transmitting screen data anywhere.**

## The day that's in the repo

Git history here covers one day, and the first commit is labeled *"initial: existing CaptureRapture codebase"* — so the application predates this repository and what's recorded is a single day of extending it.

That day added the most interesting feature in the project: **DOM serialization on click capture.** Instead of saving a picture of the screen, it saves the actual page structure, and exports an *interactive* HTML tutorial rather than a screenshot walkthrough. It also added IndexedDB persistence for those snapshots, relayed snapshot messages to the extension side panel, put an Export Interactive button in the guide editor, and mirrored the whole thing into a parallel Edge extension.

Then it fixed its own new code: a race condition, a DOMParser wrapping bug where `serializePage` returned a full HTML document instead of body content, a listener leak in the tutorial, and optional callbacks in the storage module that were throwing TypeErrors. The Edge extension got the same fixes in their own commits rather than drifting.

And it ends there, mid-momentum, with the most valuable capability just landed.

## The market read — this is the good one

This is the strongest commercial opportunity in the portfolio, and it is not close.

The category is real, funded, and growing: Scribe, Tango, and iorad all sell automatic process documentation, and enterprise L&D buyers already have budget lines for it. The problem is understood, the willingness to pay is proven, and nobody has to be convinced the category should exist.

The differentiator is where it gets genuinely interesting. Scribe and Tango transmit captured screens to a vendor cloud. That triggers security review at precisely the customers who need this tool most — regulated industries documenting ERP and HRIS workflows, where the screens contain employee records, financial data, and PII. "Your screen never leaves your machine" is not a technical footnote in that sale; it collapses a procurement cycle. Fully client-side operation, which reads as a simplification, is actually the wedge.

And the interactive DOM-snapshot export goes somewhere the screenshot-based incumbents structurally cannot follow.

## Where it went sideways

It didn't derail. It was never resourced.

One day. Against fifteen for ListingLift, in a market that is more crowded, more price-anchored, and harder to distribute into.

## The lesson

The honest question is why this got a day and the photo filter got fifteen, and the honest answer is probably that ListingLift was already further along. Momentum is its own gravity: the project you are already inside feels more real than the one that needs starting, regardless of which has the better market.

That is the exact failure mode a portfolio review is supposed to surface, and it is more useful to say out loud than to quietly leave CaptureRapture off the list because it only has twelve commits.

## Worth noting

For one day of work, the paper trail is disproportionate: a full PRD with personas and non-functional requirements, an architecture document, **two Architecture Decision Records**, and a paired design-and-plan for the single feature built that day. The ADR habit shows up more strongly here than anywhere else in the portfolio.

Somebody wrote all of that for a project they gave one day to. That is either excessive process or a genuine reflex, and given it recurs across all eight projects, it's the reflex.
