# ListingLift

**Feb 20 – Apr 6, 2026 · 172 commits · 26,396 lines · 15 active days · .NET 8 + React**
*Status: built, never launched*

---

## The ask

An agent shoots a house on her phone, standing in the driveway, and wants a "Just Listed!" story on Instagram before she gets back in the car. The sky is gray. She is not going to open Lightroom, and she is not going to wait 12 to 24 hours for a human editor.

That is the whole problem, and the February 18 PRD states it cleanly. It even names the two people: *Speedy Sarah*, at the curb, needing a blue sky right now; and *Volume Vince*, a property manager with 200 iPhone photos of empty rental units to brighten in bulk.

## The product that was specified

The PRD is unambiguous about what this is. It calls the design "a magic button." React on Vite, deployed to Vercel. Firebase for auth, storage, and functions. A Google Vertex AI endpoint doing the enhancement. Upload, wait under 30 seconds, drag a before/after slider — the document calls that "the magic moment" — then pay $1.99 to download the clean high-res version without the watermark. Apple Pay and Google Pay, because speed on mobile is the entire proposition.

The PRD is explicit that this is a *pivot away from* a service model: "By removing the Human-in-the-Loop, we shift the value proposition from 'Service' to 'Utility.'" It even handles the failure mode a solo builder usually skips — since no human catches AI mistakes, the user becomes quality control, so there is a "Try Again" button that resubmits with a different seed, and a liability disclaimer.

It is a good, tight, well-scoped weekend product.

## The product that got built

An ASP.NET Core 8 Minimal API in C#. PostgreSQL 16 with Entity Framework Core. Clerk for authentication with RS256 JWT validation and JWKS auto-discovery. Stripe for subscriptions, credit packs, *and* per-photo purchases. Cloudinary for media. Replicate for the models, with async predictions and webhook callbacks. Serilog for structured logging. Docker Compose. GitHub Actions. Azure App Service and Azure Static Web Apps.

And the features kept coming. Listings, rather than photos, became the organizing unit. Then floorplan upload, with the AI analyzing the plan and auto-classifying which photo belonged to which room. Then room-level virtual staging that anchors furniture to room features rather than to camera position — genuinely clever, and a real differentiator against per-image filters. Then AI photo critique, where the model assesses its own output and a second pass enhances based on that feedback. Then listing collaboration: share links, a join flow, collaborators inheriting access to unlocked photos.

Not one of those is a bad idea. Several are better than the original idea. Together they turned a $1.99 utility into a B2B SaaS platform.

## Where it went sideways

The PRD stopped being a contract and became a souvenir.

There is no commit that decided to build a different product. There are just forty-six days of individually reasonable decisions, each one defensible in isolation, compounding into a system that needed a real launch. The infrastructure churned alongside the scope: a Railway deployment plan on March 4, replaced by Azure on April 2, plus a .NET 8 to .NET 10 upgrade mid-flight.

The ending is the part worth sitting with. The final two commits, on April 6, are a landing-page redesign with real before/after examples, and a document titled **Production Launch Roadmap**, marked *Status: Approved*. It is a genuinely good document — five phases, live Stripe keys, a production Clerk instance, Azure Communication Services for transactional email, welcome and purchase-confirmation templates, hardening, launch. Confirmed pricing: $1.99 single, $14.99 ten-pack, $29/month.

It was written. It was approved. It was never executed. The project ends on the checklist for shipping.

## What was actually good here

A written security review, dated February 18, covering the backend's real attack surface — and it found a HIGH severity flaw in its own code. Replicate webhook signature verification was wrapped in a conditional: if the secret environment variable was unset, the endpoint silently skipped verification entirely. An attacker who discovered the webhook URL could POST a crafted success payload for any job ID and get an attacker-controlled image URL stored and served to paying customers. The review names the risk, names the file and line range, and specifies the fix.

Elsewhere the same review confirms ownership checks were done properly — resource access enforced by joining through the user record rather than trusting a client-supplied ID — and file uploads validated four ways: size, extension, content-type header, and magic bytes.

That is not hobbyist work. Somebody who does this to their own side project does it to production systems too.

## The market read

The market is real. Virtual staging and listing enhancement is an established paid category — BoxBrownie, Styldod, VirtualStagingAI — and agents already spend money here. The floorplan-driven room staging was a credible wedge, more sophisticated than what most competitors ship.

But the category is crowded and anchored low on price, and winning it is a distribution problem: getting into MLS workflows, cutting brokerage deals, showing up where agents already are. Nothing in forty-six days and 26,000 lines touches distribution. The build outran the go-to-market by an enormous margin.

## The lesson

Building was more rewarding than launching, and nothing in the process ever forced the question. The PRD was written once and never re-litigated, so it could not do the one job a PRD exists to do: say no.

The uncomfortable, useful version of this story is that the discipline to *keep* a spec honest is a completely different muscle from the discipline to write one. The first was already strong here. The second showed up five months later, on a soccer field.
