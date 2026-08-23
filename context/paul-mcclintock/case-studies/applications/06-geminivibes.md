# GeminiVibes *(originally LifePulse)*

**Apr 6 – Apr 7, 2026 · 37 commits · 3,630 lines · 2 active days · Expo + Fastify + tRPC + Claude**
*Status: prototype, abandoned after two days*

---

## The ask

A busy professional is running work, family, home, relationships, faith, and health simultaneously, and the tools meant to help all fail the same four ways. The design document lists them:

- They are **not proactive** — they store things but do not think for you.
- They force **rigid categories** that do not match how people actually think, in streams and contexts.
- They **fragment attention** across disconnected apps.
- They require **ongoing manual maintenance** just to stay current.

## The idea, which is genuinely good

LifePulse was to behave "like a thoughtful chief of staff for your life." You never assign a category. You just talk — *"Soccer practice moved to 5pm Thursday"*, *"Need to call the mortgage broker about the rate lock"*, *"Feeling like I should get back to morning devotionals"* — and the AI figures out where it belongs. Domains are lenses for viewing your life, not boxes you sort into.

Then it talks back, in three registers:

- **Time-sensitive:** "Realtor is calling in 15 min — here's context from your last conversation."
- **Drift alerts:** "Your faith domain has had zero activity in two weeks."
- **Opportunity:** "You have a free evening Thursday and mentioned wanting a date night."

And the design doc gets the hard part right, at least on paper: *"Nudge frequency is AI-calibrated — learns what you act on and dials back noise."*

The confirmation pattern is nicely specified too. Tell it practice moved, and it replies with what it understood, what it did, and what it noticed: *"Got it — moved Emma's soccer to Thursday 5pm, updated your calendar. Heads up: that overlaps with your 4:30 standup by 30 min. Want me to shift the standup?"*

## Day one

Real product. Database schema with Drizzle covering users, life items, messages, and nudges. A Fastify API with tRPC. A Claude conversation service with tool definitions and a system prompt, plus an executor that handles `tool_use` responses. Chat UI with message bubbles. The Today view with a timeline and domain badges. The Life Radar screen with domain cards and drilldown. Google OAuth with JWT and a sign-in screen.

In one day, the core loop existed.

## Day two

Almost none of it is product.

Deduplicate React in the monorepo to fix a Clerk hooks crash. Pin React 19.1.0 via overrides to fix the CI build. Switch from `@clerk/clerk-expo` to `@clerk/clerk-react` for web. Correct the Azure Static Web Apps workflow for an Expo monorepo. Add an SPA navigation fallback. Switch web output to SPA mode and guard Clerk init. Fix backend CommonJS output. Resolve Clerk user IDs to internal UUIDs for the database foreign key. Replace the custom OAuth/JWT stack with Clerk entirely, which is what set most of the above in motion.

Threaded through the same day: a complete visual rebrand from LifePulse to GeminiVibes. A cosmic aurora dark theme with a documented palette — deep space `#0B0F1A`, aurora teal `#06D6A0`, aurora purple `#9B5DE5` — seven per-domain colors, Ionicons instead of emoji, glow effects, a constellation-style Radar where node glow intensity encodes domain health, and the sign-in tagline "Align your universe."

The theme is genuinely lovely. It is also day two of a two-day project.

## Where it went sideways

The toolchain ate it, and the paint finished it.

Between fighting the monorepo and restyling the app, the one question this product lived or died on never got asked: **are the nudges any good?**

That is the entire thesis. Everything else — capture, sync, domains, radar — is table stakes that a dozen apps already do. The differentiator is whether the AI can tell a useful nudge from an annoying one, and a nudge that misfires twice gets notifications disabled forever. Calibration needs longitudinal data on real behavior, which means the fastest possible test was a week of the author's own life going through the crudest imaginable harness — a text file and a cron job would have done — with a human judging each generated nudge as useful or noise.

Instead the two days went to Expo, tRPC, Drizzle, Clerk, Docker Postgres, Azure Static Web Apps, and an aurora gradient. Then it stopped.

## The market read

The hardest category attempted here, and among the hardest in consumer software generally. The proactive-AI-life-assistant graveyard is large and extremely well funded, and it is full of products that shipped everything except reliable judgment about when to speak.

The insight about proactivity is real — "they store things but do not think for you" is a correct diagnosis of why every productivity app eventually becomes a chore. But the market punishes precisely the capability that was never tested here.

## The lesson

The stack was chosen as though the idea were already validated.

An Expo React Native monorepo with tRPC, Drizzle, Clerk, containerized Postgres, and Azure Static Web Apps is a defensible architecture for a product with users. For a two-day test of an unvalidated hypothesis it is enormously expensive, and the expense is not the setup time — it is that every hour spent on build configuration is an hour not spent on the risky assumption.

The rule this project teaches, at a cost of two days: **the riskiest assumption should be the cheapest thing you test.** Here it was the only thing never tested at all.
