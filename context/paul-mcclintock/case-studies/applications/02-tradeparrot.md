# TradeParrot

**Apr 3 – Apr 24, 2026 · 132 commits · 25,056 lines · 13 active days · Python + Claude**
*Status: working, in personal use, stopped abruptly*

---

## The ask

Momentum day trading has a narrow window and too many inputs. Between 7:00 and 12:00 Eastern you need to know which stocks are gapping, which have news, which are running on unusual volume, what the options flow says, whether the float is short enough to squeeze, and where the technical levels sit — and you need it before the move is over.

The April 1 design document states it in one sentence: an automated dashboard that surfaces momentum opportunities during market hours, enriched with AI analysis, options flow, short interest, and technical levels.

## The constraints, written down first

This is the part worth noticing. Before any code, the design doc fixes five constraints:

- Bullish plays only. No shorting.
- No API requests outside 7:00–12:00 ET.
- Five-minute refresh cycle.
- Free or low-cost data sources preferred.
- Top 10 candidates per scan, explicitly to manage API cost and scan time.

Every one of those is a scope decision with a cost attached, made before the first line ran. The design also documents *why* each stack choice was made: yfinance over paid APIs because free is good enough for v1; server-side scanning to protect API keys; polling over websockets because a five-minute refresh does not need real-time; Claude Sonnet for analysis as a speed-versus-quality balance at ten candidates per scan.

## What got built

A scanner pair — pre-market for gaps, news catalysts, and volume surges; market-hours for price and volume breakouts on high relative volume — feeding an enrichment pipeline that layers on support and resistance, VWAP, RSI, moving averages, ATR, put/call ratio, unusual options activity, float size, short interest, and squeeze potential. Claude then grades each candidate A through F and produces an entry price, a stop loss, and three profit targets.

Then it got more ambitious. A political trading scanner pulling congressional STOCK Act disclosures from Quiver Quantitative against a curated watchlist of about twenty high-profile members, cross-referenced with political news catalysts classified by Haiku. Institutional positioning analysis: max pain, open-interest walls, point of control, anchored VWAP. Paper trading with realized P&L tracked by day. An analytics section split into paper-trade performance and signal quality, every chart click-through to a drill-down drawer.

And then automatic execution through Alpaca, with dedup, staged exits, and noise-floor stops.

## Where it went sideways

It changed category without ever changing its design document.

On April 1 the system is decision support: scan, enrich, grade, display, and a human decides. By April 21 it is sizing positions aggressively and charting realized dollars. On April 22 the commit reads *"harden auto-trade execution — dedup, staged exits, noise-floor stops."* The final commit of the project, April 24, is **"default auto-exec ON."**

A dashboard that recommends trades and a system that places them while you are not looking are different products. They carry different risk, need different failure handling, and deserve different scrutiny. The transition happened one reasonable commit at a time, and no document ever caught it — because it never arrived as a feature request. It accumulated.

Then it stops dead on April 24. No wind-down commit, no README update, no retrospective.

## What was actually good here

Twenty design and plan documents in twenty-two calendar days, including a dedicated test-coverage design *and* its implementation plan — a rare thing to spend a whole spec cycle on in a personal project.

The engineering matured visibly across the month. Early commits are features. Late commits are things like escaping user-influenced fields in client-side JavaScript, null-safe price formatting, destroying stale chart handles before redraw, replacing inline `onchange` handlers with proper `addEventListener` wiring, and an analytics data-integrity pass covering deduplication, a single unified win-rate definition, and small-sample guards so a 2-for-2 record does not display as a 100% strategy.

There is also a nice piece of operational judgment: an Alpaca websocket retry with exponential backoff, added specifically to stop a reconnect storm from killing the container in a death spiral.

Two-tier model routing is worth calling out too — Sonnet for the multi-factor trade analysis, Haiku for high-volume news classification — chosen on cost-versus-quality grounds and written into the design rather than discovered by accident.

## The market read

As a product, near zero, and that is the correct answer. Publishing graded trade recommendations to other people is investment advice. It carries licensing obligations and liability exposure that no solo side project should absorb, and nothing about this system was ever pointed at that. There is exactly one user.

Judge it as a systems build instead, and it is the most technically ambitious thing in the portfolio: scheduled scanners, multi-source enrichment, an LLM in the decision loop, a streaming market-data feed with real reconnect handling, and an execution path that places live orders against a broker API.

## The lesson

The most consequential scope change in the project was invisible to the process that was supposed to catch scope changes.

Design documents that are only ever *appended to* will not flag the moment a tool crosses into a different category of risk, because each increment looks like the last one. The check that was missing is not more documentation — it is a periodic re-read of the original problem statement against what the thing currently does, and a willingness to notice when the answer has changed.

That is a genuinely useful thing to have learned on a system that was only ever trading its author's own money.
